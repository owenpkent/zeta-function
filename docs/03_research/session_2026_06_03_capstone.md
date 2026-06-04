# Session capstone (2026-06-03): the Connes 2602 arc, and the sharpened map of the missing math

> A single coordinate map of one session's work, triggered by Connes' Feb-2026 paper
> "The Riemann Hypothesis: Past, Present and a Letter Through Time" (arXiv:2602.04022). The session
> ran the paper through the project's discipline, attempted the proof, attempted to build the missing
> object from first principles, and exhibited that object where it is a theorem. Net result: no
> proof (none was possible), but the most precise statement yet of what is missing and a stack of
> new coordinates ruling out where it is not. Honesty discipline per
> [researcher_mindset.md](researcher_mindset.md): every "no" is a coordinate.

## The arc, in order

1. **Assessment of Connes 2602.04022** ([connes_2602_letter_to_riemann.md](connes_2602_letter_to_riemann.md)).
   The paper reframes Weil positivity constructively: the minimal eigenvector eta_x of the truncated
   Weil form has a Fourier transform with all zeros on the line (Theorem 6.1, unconditional per
   cutoff), and RH would follow IF eta_x-hat -> Xi. Verdict: Theorem 6.1 manufactures on-line zeros
   for ANY admissible form, so it is zeta-blind; the entire RH content is the unproven convergence,
   which is the project's (N_off, N_off) obstruction restated. Instrumented in e3s/e3t (LEARNINGS
   #50): the identical machine reproduces Davenport-Heilbronn's on-line zeros and (Caratheodory-
   Fejer) gives all-roots-on-circle for zeta-, D-H-, and random-derived symbols alike.

2. **The candidate proof** ([candidate_proof_rh_connes_line.md](candidate_proof_rh_connes_line.md)).
   Assembled the full chain reduced to one lemma (Lemma C: eta_x-hat -> Xi, = RH). Four committed
   proofs of Lemma C (Gamma-convergence, archimedean domination, de Branges cone, monotonicity), all
   four fatal and circular, each would prove the false D-H RH. The autopsy located every break.

3. **Assume RH and work backwards** (e3u, LEARNINGS #51). The object RH hands you (the Hilbert-Polya
   operator D) reproduces Connes' Theorem 7.3 heat trace to 1e-5, but depends ONLY on the imaginary
   parts gamma: a double on-line zero and an off-line pair at the same height give the identical heat
   trace. The spectral realization is provably blind to beta, the coordinate RH is about. Level 3 is
   categorically insufficient, re-derived from the assume-RH direction.

4. **The marginal-positivity wall, quantified** (e3v, LEARNINGS #52). The Weil-form minimal
   eigenvalue collapses doubly-exponentially, eps(x) ~ e^{-4 pi x} (Slepian prolate eigenvalues,
   reproducing Connes' Figure 1). Below float64 by x ~ 3, ~1e-71 at x=13. The "marginal" in
   marginal-positivity now has a number on it.

5. **Provability ledger** ("can we prove it?"). The D-H floor (eps_DH bounded away from 0) is
   provable from the verified off-line zero. The zeta upper rate is NOT cleanly proven (only
   eps <= R(k_lambda), a finite archimedean number; the e^{-4 pi x} rate is Connes' empirical Fig 1).
   The zeta lower bound eps >= 0 IS Bombieri-Weil = RH.

6. **First-principles construction sweep** ([building_the_missing_positivity.md](building_the_missing_positivity.md),
   LEARNINGS #53). Four fresh mechanisms (Rankin-Selberg pole, Bost-Connes Fock modular, fibered
   arithmetic surface, prime free-field reflection) to build the missing positivity. All collapse to
   arithmetic Rosati / Hodge-standard positivity (= RH) or de Branges / Conrey-Li (= stronger and
   false). The one live invariant, the Rankin loglog-coefficient (e3w), detects non-Euler-ness, not
   RH-failure (c < 1 for both RH-false D-H and RH-true Epstein): necessary-not-sufficient.

7. **The polarization exhibited where it is a theorem** (e3x, LEARNINGS #54). On E x E over F_q the
   intersection form has signature exactly (1,3) (Hodge index), primitive part negative-definite, RH
   bound a^2 <= 4q with a HEALTHY O(q) buffer. This is the missing object, made automatic by a
   theorem, in the one setting where the substrate exists.

## The single sharpened statement of the missing math

Every thread converges on one object and one obstruction.

**The object (Level 5).** A signed intersection pairing on the global H^1 of the product
Spec(Z) x Spec(Z), carrying the Frobenius correspondence Gamma of place-dependent bidegree (1,p),
whose negative-definiteness on the primitive part is proven WITHOUT RH input. This is the arithmetic
Hodge standard conjecture (08A M4). Over F_q it is the Hodge Index Theorem (e3x); over Z it does not
exist as a theorem, and the substrate (the product surface, the Frobenius class) is not even
constructed.

**The obstruction, stated four ways this session (all the same seam).** The Euler product cleanly
fixes the OBJECT'S EXISTENCE / block structure (this is real, non-circular, and D-H-discriminating:
e3w's loglog-coefficient, the primitivity, the product-state, the orthogonal place-grading). But the
off-line-zero content lives in the analytic continuation across Re = 1/2, carried by the Gamma
factor and the functional equation, which are SHARED with D-H and which the Euler product does not
touch. So multiplicativity gives the existence of the right kind of object but not the positivity of
its continuation pairing. Supplying that positivity is not a route to RH; it IS RH.

**Why it is hard, with a number (the compass).** Even if the integer polarization existed, e3v shows
its buffer would be e^{-4 pi x} (doubly-exponentially marginal), versus the O(q) buffer that is
automatic over F_q (e3x). RH over Z is true at the very edge; the function-field analogue is true
with room to spare. The proof must therefore engage the EXACT multiplicative structure of zeta as a
global cancellation on the continuation, not any generic or soft positivity.

## Coordinates this session ruled out (the negative map)

- Spectral / Hilbert-Polya realization (Level 3): provably beta-blind (e3u). Cannot close RH.
- The four soft proofs of the convergence lemma (Gamma-convergence, archimedean domination, de
  Branges cone, monotonicity): all circular, all D-H-fatal (candidate proof autopsy).
- Termwise / pointwise positivity of the prime sum: the von Mangoldt weights multiply a sign-
  indefinite autocorrelation (zeta increment is mixed-sign).
- The four first-principles construction mechanisms: all collapse to RH or de Branges (LEARNINGS #53).
- The Rankin loglog-coefficient and every #20-family fingerprint: non-Euler detectors, necessary-
  not-sufficient (the reformulation trap, e3w).

## What is genuinely live (for the human-led program)

- The product surface Spec(Z) x Spec(Z) + the Frobenius cycle class Gamma (08A M4 / spec_z landscape
  section 9): construct the substrate, then attempt the Faltings-Hriljac-type negative-definiteness.
  This is the only forward direction not foreclosed; it is research-grade and not session-completable.
- The proven fragments worth building on: the archimedean Weil positivity (Connes-Consani Sonin
  space), the function-field template (e3x / 2G/2T), the single-surface arithmetic Hodge index
  (Faltings-Hriljac). The gap is always the same: assemble them on the product with a Frobenius.

## Artifacts produced this session

Experiments: e3s (Connes eta classifier), e3t (prolate residual), e3u (assume-RH heat trace),
e3v (marginal wall), e3w (Rankin loglog-coefficient), e3x (function-field polarization).
Docs: the 2602 assessment, the candidate proof + autopsy, the construction sweep, this capstone.
LEARNINGS #50-#54. All committed and pushed.

## Bottom line

The session did not prove RH and could not. It did produce the most precise statement the project
has of the missing object (a polarization on a not-yet-constructed arithmetic surface, with a
doubly-exponentially marginal buffer), exhibited that object where it is a theorem (e3x), and ruled
out, with construction-level detail, the spectral side, the rate side, four candidate proofs, and
four first-principles mechanisms. The compass reading is unchanged and now overdetermined: RH lives
at Level 4/5 (positivity / polarization), it is true only at the margin over Z, and the proof must
engage the exact Euler structure as a global cancellation on the continuation.
