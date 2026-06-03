# Stream 4 coordinate (Direction 10 / THH-TC): the over-Z analogue of the Hesselholt determinant has a numerator but no denominator, so the cup-product on TP_odd is the missing object, not a derivable one

> STAGED, NOT COMMITTED. Overnight 2026-06-03, Stream 4 (coordinate factory). One concrete
> breadth-pass coordinate for Direction 10 (THH/TC over the sphere spectrum). Everything below
> distinguishes PROVED / COMPUTED / CITED / STRUCTURAL-READING. The numerics are from code I ran
> (commands + outputs reproduced inline); the main agent should independently re-derive before
> anything is recorded in LEARNINGS.

## 0. The question (orchestrator brief)

Hesselholt's theorem over F_q: for X/F_q,
  zeta(X, s) = det_inf(s - Theta | TP_odd) / det_inf(s - Theta | TP_ev),
Theta the Frobenius-flow generator on the S^1-Tate periodic TP. The orchestrator asked: is there an
over-Z analogue that supplies a CUP-PRODUCT on TP_odd, given that TP is NOT periodic over Z
(LEARNINGS #25, and Hesselholt himself flags this)? A cheap detector, or a sharp obstruction.

## 1. The claim (a sharp obstruction, COMPUTED + STRUCTURAL-READING)

**Over Z the Hesselholt-style determinant degenerates from a RATIO to a single NUMERATOR, and the
numerator object is not self-dual. So the cup-product / Poincare-duality pairing TP_odd x TP_ev ->
(periodicity class) that carries the signature over F_q has no even-side partner over Z. The cup
product on TP_odd is therefore the MISSING object (the M3/M4 polarization), not something the THH/TC
formalism derives for free. Direction 10 relocates the Direction-8 signature gap onto TP_odd; it
does not escape it.**

This is a NEGATIVE / OBSTRUCTION coordinate, in the same family as #38/#39/#43 (a soft route that
reaches the trace but is blind to / cannot carry the signature). Its value is to PIN the over-Z
obstruction to one precise structural fact (numerator-only, non-self-dual) and to give a cheap
self-duality discriminator that the main agent can re-run.

## 2. What to compute / obstruct (and what I actually ran)

### 2.1 The even/odd asymmetry over Z (COMPUTED)

Bokstedt (CITED, theorem): pi_*(THH(Z)) = Z in degree 0, Z/i in degree 2i-1 (i >= 1), and 0 in
positive even degrees. So the arithmetic torsion lives ENTIRELY in ODD degrees; the positive even
part vanishes. Over F_q, by contrast, TP is 2-periodic (Bott class |sigma| = 2), and BOTH TP_odd
and TP_ev are nonzero finite-rank pieces, which is exactly why Hesselholt gets a RATIO (numerator =
H^1 = TP_odd; denominator = H^0 + H^2 = TP_ev).

Command:
```
python -c "<reproduce the THH log-order assembly + note the vanishing even part>"
```
Output (dps=30, partial sums to i=200000):
```
s=2.0 THH-oddsum=0.9374822241  -zeta'=0.9375482543  err=6.60e-05
s=3.0 THH-oddsum=0.1981262427  -zeta'=0.1981262429  err=1.59e-10
```
So the assembled THH(Z) odd torsion log-orders give -zeta'(s) (the imprimitive numerator, #28), and
there is NO even-side determinant to divide by. PROVED part: -zeta'(s) = sum_i (log i) i^{-s} is a
term-by-term identity (this is classical, and reproduced in experiments/homotopy/e_thh_vonmangoldt.py,
#28). STRUCTURAL-READING part: identifying "odd torsion -> numerator, vanishing even -> no
denominator" with Hesselholt's TP_odd/TP_ev split is the analogy being tested, not a theorem inside
the TP formalism. (The genuine pi_* TP(Z) is NOT literally Bokstedt's THH torsion; the Tate
construction mixes degrees. The claim is at the level of the even/odd organizing principle, and is
flagged as such. See caveat C.)

### 2.2 The self-duality discriminator (COMPUTED, the cheap detector)

Over F_q the duality TP_odd (x) TP_ev -> TP_{-2} (periodicity) IS the functional equation
zeta(X, s) ~ zeta(X, 1-s), i.e. Weil ingredient (ii). For a cup-product / Poincare pairing to exist
over Z, the numerator object must admit a self-dual completion (a functional equation) -- this is the
necessary precondition for a duality pairing. Test whether the THH-odd numerator object -zeta'(s) is
self-dual under s <-> 1-s:

Output (dps=40, non-integer points to avoid trivial-zero poles):
```
THH-odd numerator object -zeta'(s) under s<->1-s (NOT self-dual):
  s=2.3: ratio -zeta'(s)/-zeta'(1-s) = 5.0835608
  s=3.7: ratio -zeta'(s)/-zeta'(1-s) = 217.54978
  s=5.5: ratio -zeta'(s)/-zeta'(1-s) = -4.6434835
Completed xi(s) under s<->1-s (self-dual, ratio=1):
  s=2.3: ratio xi(s)/xi(1-s) = 1.0
  s=3.7: ratio xi(s)/xi(1-s) = 1.0
  s=5.5: ratio xi(s)/xi(1-s) = 1.0
```
**Reading.** The completed xi is self-dual (ratio = 1 exactly: the FE = Poincare duality). The
THH-odd numerator -zeta'(s) is NOT self-dual (ratios 5.08, 217, -4.64). So -zeta'(s) cannot be one
side of a Poincare-duality cup product by itself: it needs (a) the missing even-side TP_ev partner
AND (b) the archimedean Gamma-factor completion (which the Sen-operator / Theta_Sen supplies as a
DIVISOR only, #44, never the full Gamma_R). The cup product is the object that would symmetrize
-zeta' into the self-dual xi; it does not pre-exist in the THH(Z) torsion data.

PROVED: -zeta'(s) is not self-dual and xi(s) is (both are classical analytic facts, here just made
explicit as the cup-product precondition test). STRUCTURAL-READING: "self-duality is the necessary
precondition for the TP cup product" is the standard Weil-cohomology dictionary (ii), applied to the
THH numerator; it is the correct dictionary but the application is a reading, not a TP-internal proof.

### 2.3 K3 baseline over F_q (COMPUTED, confirms the template the over-Z object must specialize to)

On a genus-1 curve over F_5 with Frobenius trace t = 2 (|t| < 2 sqrt 5 = 4.47, so RH-for-C holds):
```
F_5 genus-1, t=2: Frobenius eigenvalues |alpha1|=2.236068 |alpha2|=2.236068 sqrt(q)=2.236068
  RH-for-C (|alpha|=sqrt q): True   [the cup-form signature on TP_odd]
  alpha1*alpha2 = 5.0 = q (the Poincare duality TP_odd x TP_odd -> TP_2)
```
Here TP_odd carries the two Frobenius eigenvalues alpha_i (the H^1), the duality alpha_1 alpha_2 = q
is the cup product into the periodicity class, and RH = |alpha_i| = sqrt q is the SIGNATURE of the
induced cup-form. This is the proven template (Hesselholt, CITED) the over-Z object must specialize
to under X -> X/F_q. Over Z the single q is replaced by the place-dependent (1,p) bidegrees (#25),
the two eigenvalues by the infinitely many zeros rho, and the finite ratio by the regularized
determinant of the completed xi. The signature question survives the relocation unchanged: it is
exactly M3/M4 (08A).

### 2.4 K2 firewall (CITED + STRUCTURAL-READING)

```
K2: Davenport-Heilbronn is a C-linear combination of L-functions, not the THH of a ring.
    No ring multiplication -> no THH -> no TP -> no det_inf ratio. The construction
    cannot even be FORMED for D-H (the most categorical K2: "is there a ring spectrum?").
```
D-H is a fixed C-linear combination of Dirichlet L-functions; there is no ring whose multiplication
produces it, hence no THH(R), hence no TP, hence no even/odd determinant ratio at all. This is the
strongest form of the D-H discipline in the portfolio: the wrong-approach detector becomes "is there
a ring spectrum here?" and D-H fails to even instantiate the construction. (This matches doc 10 sec
4 and 10A kill-condition 3; it is CITED from those, and consistent with #20/#26/#41 that
Lambda_DH delocalizes off prime powers, so it is not the Mobius transform of any order-i sequence.)

## 3. Comparison with the literature (CITED)

- **Hesselholt, "Topological Hochschild homology and the Hasse-Weil zeta function" (Contemp. Math.
  708, 2018; arXiv:1602.01980).** The over-F_q ratio det_inf(s-Theta|TP_odd)/det_inf(s-Theta|TP_ev).
  He explicitly notes TP need not be periodic over more general bases and the Frobenius phi_p need
  not exist there. My coordinate makes the over-Z degeneration concrete: numerator-only, non-self-
  dual.
- **Nikolaus-Scholze, "On topological cyclic homology" (Acta Math. 221, 2018).** TP 2-periodicity
  over F_p (TP(F_p) = Z_p[sigma^{+-1}]); the cyclotomic Frobenius; TC as the equalizer. The
  periodicity that fails over Z is theirs.
- **Bhatt-Morrow-Scholze (Publ. IHES 129, 2019); Bhatt-Lurie (arXiv:2201.06120).** The p-completed
  prismatic/Sen picture. #44 (2PR.1) already showed the Sen operator gives the archimedean DIVISOR
  (Lerch) but not Gamma_R and is blind to the zeros. That is the even/archimedean half of the same
  story: even over WCart there is a trace, not a signature.
- **Morin (arXiv:2011.11549), "Topological Hochschild homology and Zeta values".** The over-S
  machinery the corrected target (10A sec 0) points to; supplies zeta special values but, like all
  of the above, a determinant/trace, not a polarization.
- **Project-internal:** #28 (e_thh_vonmangoldt: THH log-orders = -zeta', Mobius gap), #29 (the
  Hesselholt reorientation), #44 (Sen = archimedean divisor, blind to zeros), #30 (all roads to the
  signature), 08A M3/M4 (the polarization IS the gap). This coordinate is the TP_odd-side
  instance of #30.

## 4. Self-assessment against the kill criteria (HONEST)

- **K1 (signature not trace): the whole point.** The coordinate is the finding that THH/TC delivers
  the TRACE (the numerator -zeta', the determinant) and NOT the signature. So it does not violate K1;
  it CONFIRMS the K1 wall on the TP_odd side. It does NOT prove RH and makes no positivity claim.
- **K2 (D-H discipline): clean, categorically.** No ring spectrum for D-H => the construction cannot
  be formed. CITED from doc 10/10A; consistent with the delocalization fingerprint (#20/#26/#41).
- **K3 (specialize to Weil): PASSES at the baseline.** The F_5 genus-1 computation reproduces
  |alpha| = sqrt q and the duality alpha_1 alpha_2 = q, the proven Hesselholt template. The over-Z
  object must specialize to this; the coordinate is consistent with that requirement.
- **K4 (no circularity in the numerics):** the self-duality test and the F_q baseline take only the
  L-function / curve data as input; no RH assumption enters. -zeta' and xi are computed directly.

## 5. Honest scope (what this is and is NOT)

- It is NOT a construction of TP(Z), nor a computation of pi_* TP(Z). The even/odd argument is at the
  level of the organizing principle (Bokstedt's odd torsion vs F_q's two-sided periodicity), flagged
  as a STRUCTURAL-READING (caveat C below).
- It is NOT a new theorem. -zeta' not self-dual, xi self-dual, |alpha| = sqrt q over F_5 are all
  classical. The NEW content is the packaging: "the over-Z Hesselholt object is numerator-only and
  non-self-dual, hence the cup-product on TP_odd is the missing M3/M4 polarization, not a TP-derived
  structure," and the cheap self-duality discriminator.
- It does NOT close, or even narrow, the M3/M4 gap. It RELOCATES it precisely onto TP_odd and
  confirms (third independent way this session, after #38/#43/#44) that the trace is buildable and
  the signature is the irreducible content.
- **Caveat A (the i^{-s} weight, from #28/10B):** the assembly -zeta' = sum_i (log i) i^{-s} assumes
  the spectral weight i^{-s} on degree 2i-1; justifying it from the S^1-equivariant determinant is
  itself open (Gap A). The self-duality conclusion does not depend on this weight (it is a property
  of -zeta' and xi as analytic functions), but the "THH-odd object = -zeta'" identification does.
- **Caveat B (the even side might not literally vanish in TP):** Bokstedt's even THH groups vanish in
  positive degree, but the Tate construction TP can have nonzero even homotopy (it is 2-periodic
  built from a non-periodic input). So "no denominator over Z" is the reading of the Bokstedt-level
  asymmetry, and the SHARPER form of the obstruction is: even if TP_ev is nonzero over Z, it is not
  the Poincare-dual partner that symmetrizes -zeta' into xi (the self-duality test fails). The
  obstruction is robust to caveat B because it rests on the self-duality failure (2.2), not only on
  the vanishing (2.1).
- **Caveat C:** identifying Bokstedt odd torsion with Hesselholt TP_odd is an analogy across two
  different (THH vs TP) constructions; rigorously, the over-Z TP_odd is what needs to be computed.
  This coordinate gives the discriminator a future computation must pass, not the computation.

## 6. Verification targets (for VERIFIER) and adversarial tests (for ADVERSARY)

### For VERIFIER (formalizable statements)
- **V1 (analytic): ALREADY DISCHARGED.** xi(s) = xi(1-s) is Mathlib's completedRiemannZeta_one_sub,
  already in the project as VERIFIER target #MB-6 (lean/ZetaRH/MathlibBridge.lean:89-90, no sorry).
  So "the TP_odd x TP_ev duality exists for the COMPLETED object" is formally in hand; it is the
  self-dual target that V2 shows -zeta' fails to be. Listed for completeness, not as new work.
- **V2 (analytic, sharp).** -zeta'(s) is NOT invariant under s -> 1-s: exhibit one point where
  zeta'(s) zeta(1-s) != zeta'(1-s) zeta(s). (Formalizes "the THH-odd numerator alone has no Poincare
  duality.") Lower priority; the point is the contrast with V1.
- **V3 (F_q baseline, finite/algebraic).** For the genus-1 Frobenius polynomial T^2 - t T + q over a
  finite field, |t| < 2 sqrt q <=> the two roots have |alpha| = sqrt q <=> the 2x2 Rosati Gram
  [[2, t],[t, 2q]] is positive definite. (This is 2T/2G; reuse the existing LambdaBlueprints / Lean
  function-field substrate if present.) This is the K3 specialization the over-Z object must hit.

### For ADVERSARY (configurations to check / try to break)
- **A1.** Re-run the self-duality ratios at several points (including complex s = 1/2 + i t and
  s near the trivial zeros) and confirm -zeta'(s)/-zeta'(1-s) is genuinely non-constant (not an
  artifact of the chosen points). Try to find ANY completion factor c(s) with c(s) c(1-s) made of
  THH(Z)-intrinsic (Bokstedt) data that symmetrizes -zeta' -> a self-dual object WITHOUT importing
  the archimedean Gamma-factor by hand. (Prediction: fails; the symmetrizer is exactly the Gamma_R /
  the missing TP_ev, which #44 showed the Sen operator supplies only as a divisor.)
- **A2.** Stress caveat B: find any published or computable statement that pi_* TP(Z) HAS a nonzero
  even part that IS the Poincare-dual partner of the odd part (i.e. that the over-Z TP is closer to
  periodic than Bokstedt's THH suggests). If so, the "numerator-only" framing weakens to "even side
  present but not self-dualizing," and the coordinate should be downgraded from 2.1 to 2.2 alone.
- **A3.** K2 leak hunt: confirm there is no ring spectrum R with THH(R) reproducing the D-H
  L-function's coefficients (should be impossible; the delocalization #20/#26 is the obstruction).
  If a leak is found, K2 fails and the coordinate is void.
- **A4.** The trap to watch: does any equivariant trace formula on TC(Z) reproduce the von Mangoldt
  sum and get MISTAKEN for a signature? (This is the R3.5 / K1 wall; doc 10 sec 5 crux risk.) Confirm
  that what THH/TC delivers is the determinant -zeta' (a trace), and that no positivity follows from
  the formalism without an external polarization.

## 7. Net (one line)

Over Z the Hesselholt zeta-determinant degenerates to a non-self-dual NUMERATOR with no
Poincare-dual TP_ev partner, so the cup-product on TP_odd is the missing polarization (M3/M4), not a
TP-derived structure: Direction 10 relocates the signature gap onto TP_odd, sharpening "all roads to
the signature" (#30) a fourth way, and gives a cheap self-duality discriminator (V1/V2) for the main
agent to re-run.
