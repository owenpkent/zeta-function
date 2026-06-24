# e2vv: NP-1 -- does the finite-prime modular data continue past Re(s)=1 as a t_p-detecting positivity?

Run: `python -m experiments.arithmetic_geometric.e2vv_np1_modular_continuation`
(uses repo `.venv`; D-H control 9/9 live).

## The question (AT-MOD-4 probe, dossier Part 8)

The Bost-Connes (BC) / KMS modular carrier lives at Re(s) > 1 (Gibbs convergence; phase
transition at the pole s=1; type III_1). The off-line obstruction lives in the strip
1/2 < Re(s) < 1. **NP-1**: does the finite-prime modular data (KMS state, log Delta,
modular flow, relative modular operator / Connes cocycle) have ANY analytic continuation
past Re(s)=1 into the strip carrying a positivity or constraint that (a) detects the
off-line obstruction (|t_p| < 2 sqrt p vs |t_p| > 2 sqrt p) and (b) is NOT shared with
Davenport-Heilbronn? Prediction (K2 firewall): **NO**.

## Two distinct t's (load-bearing)

- **t_flow** = the modular flow time: the KMS two-point function is n^{-(beta - i·t_flow)};
  continuation "past Re(s)=1" is continuation in s = beta - i·t_flow.
- **t_p** = the Frobenius trace at p. The off-line obstruction is a t_p-phenomenon.

The carrier is parametrized by (prime set S, beta, t_flow); it has **no t_p slot**.

## Honest scope: how NP-1 = NO is established

**NP-1 = NO is established by the ANALYTIC M4-reduction, not by a numerical measurement.**
There is no honest way to "measure" t_p-independence of the carrier, because the carrier
quantities are a pure function of (S, beta) with no t_p argument (Part 4, a structural
fact about the construction). The experiment runs **two genuine computations** that
support the reduction (both have a real data path that could register a change), plus
structurally-labeled facts. No "measured invisibility" / "non-vacuous witness" claim is
made; an earlier version of this file made such a claim on a no-op and it was struck.

## The two genuine computations

**(1) The C_E flip contrast (Part 1).** The genus-1 block B_E(p, t_p) = [[2, t_p], [t_p, 2p]]
(the object the C_E-twist polarizes) is a real function of t_p. Its minimum eigenvalue
crosses zero EXACTLY at |t_p| = 2 sqrt p:

| p | edge = 2√p | min ev at edge-0.3 | min ev at edge+0.3 | flip located at |
|---|---|---|---|---|
| 2 | 2.828 | +0.281 | -0.284 | 2.828 |
| 3 | 3.464 | +0.257 | -0.262 | 3.464 |
| 5 | 4.472 | +0.220 | -0.227 | 4.472 |
| 7 | 5.292 | +0.195 | -0.202 | 5.292 |

PD below the edge, indefinite above; the flip lands at 2√p to within 0.06. **This is the
object that genuinely sees t_p** -- t_p acts on the C_E polarization phase, which is NOT
modular-carrier data (#101/MC.2).

**(2) Finite-truncation zero-freeness in the strip (Part 2).** The finite local Euler
product Z_S(s) = prod_{p in S}(1 - p^{-s})^{-1} swept across the strip Re(s) in {0.51, 0.6,
0.75, 0.9, 0.99}, t in [0, 120], for two truncations:

| k = |S| | min \|Z_S\| over the sweep |
|---|---|
| 4 (S={2,3,5,7}) | 0.219 (at beta=0.51) ... 0.397 (at beta=0.99) |
| 8 (S up to 19) | 0.124 (at beta=0.51) ... 0.342 (at beta=0.99) |

Overall min |Z_S| = 0.124 > 0. **Every finite truncation is zero-free across the strip.**
So no off-line zero appears in any finite-prime carrier; reaching the strip WITH the
obstruction is the infinite-product limit S -> all primes (= the M4 coupling = #104).

## Supporting structural facts (honestly labeled)

- **Part 0 (link i):** the off-line obstruction is a t_p-phenomenon. For 2√p < t_p < p+1
  the genus-1 factor's zero pair sits off Re=1/2 in the strip (p=5: Re = 0.858, FE-partner
  0.142), on Re=1/2 at the edge, touching Re=1 only at the Hasse bound t_p=p+1.
- **Part 3 (the modular axes):** the relative modular operator / Connes cocycle DOES move,
  under the choice of state (phi vs psi) and under the flow time t_flow (both with real
  distinct inputs, not self-vs-self). These are the modular degrees of freedom; they are
  axes ORTHOGONAL to t_p. By #101 the BC weights have no t_p slot, so there is no
  t_p-bearing modular object. This is the analytic argument, NOT a measured
  t_p-independence.
- **Part 4 (structural / leak-check, NOT a measurement):** the carrier quantities (Z_S,
  Gibbs weights, log Delta spectrum) are functions of (S, beta) alone; t_p does not enter
  their definitions. A fact about the construction, not an experimental result.
- **Part 5 (D-H):** zeta's comb >= 0 (carrier forms); D-H's comb < 0 at n=3 (no carrier).
  The one un-shared structure is the Re(s)>1 comb sign (the easy half); no strip
  discriminator exists. Confirms clause (b).

## Verdict

**NP-1 = NO**, established by the analytic M4-reduction:
- t_p acts on the C_E polarization phase (Part 1), not on the carrier (Part 4).
- The off-line obstruction is absent from every finite-prime truncation (Part 2); it is a
  property of the infinite-product limit + completion.
- That limit IS the M4 coupling. So "does the finite-prime carrier continue into the strip
  as a t_p-detecting positivity" = "does the M4 coupling exist" = #104.

**What NP-1 adds over #104 (one sentence):** NP-1 states the #104 coupling reduction from
the continuation side -- the off-line obstruction is absent from every finite-prime
truncation, so reaching it in the strip is the infinite-product limit = the M4 coupling --
and it does NOT upgrade the firewall to a convergence theorem (that question IS M4).

This is a one-sentence sharper framing of #104, not a new convergence theorem and not a
"measured/structural continuation-invariance theorem." K1-noncircularity is confirmed (no
zeros used anywhere), but noncircular alone does not make a new result.

## Lean handoff (VERIFIER target)

The continuation-invariance framing has rfl-vacuous clauses (the carrier literally has no
t_p argument, so "t_p-independence" is a definitional triviality, not worth formalizing).
The one formalizable piece is the genuine finite-truncation fact + the M4-reduction:

**VT-NP1 (finite Euler product zero-freeness + the M4-reduction).** For a finite prime set
S, prod_{p in S}(1 - p^{-s})^{-1} is holomorphic and non-vanishing on Re(s) > 0 (each
factor 1 - p^{-s} vanishes only on Re(s) = 0). Consequence (the M4-reduction, stated, not a
new theorem): the off-line obstruction (a zero of the completed object with Re != 1/2) is
not present in any finite truncation; it is a property of the infinite-product limit +
completion, which is the M4 coupling. Extends `HodgeIndex.negDef_iff_hasseWeil` (the per-p
window) and `R3_5.lean` (the no-shortcut wall). No RH-equivalence, no zeros; pins the
firewall, does not move it.

## Adversary test cases (for ADVERSARY)

1. **No-op check.** Confirm every reported value comes from a real computation: Part 1's
   min-eigenvalue uses `np.linalg.eigvalsh(b_e(p, t))` (a genuine t_p data path; feeding a
   different t_p changes the output); Part 2's min|Z_S| varies with k and beta (it is not a
   constant). (The prior version's Part 4 "witness" was a no-op and was removed.)
2. **The C_E flip location.** Re-derive that det B_E = 4p - t_p^2, so the flip is exactly at
   |t_p| = 2 sqrt p, independent of any tuning.
3. **The zero-freeness.** Push S larger and finer t-grid; confirm min|Z_S| stays > 0 in the
   strip (a finite product of 1/(1-p^{-s}) cannot vanish for Re(s) > 0).
4. **The conflation trap.** Confirm the experiment does NOT claim the finite-prime data is
   global zeta: the finite Euler product is zero-free in the strip; only the infinite limit
   + completion produces strip zeros. NP-1 is about the finite-prime structure's
   continuation, not about a global function reaching the strip.
