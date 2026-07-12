# E1M: the Hamburger-type converse pin (LEARNINGS #154 upgrade-spec item 4)

> Companion to `e1m_hamburger_pin.py` / `.npz`. Probes the last unexecuted #154
> upgrade-spec ingredient: replace the ground-state forcing of the CCM
> Section-7 identification (`xihat_lambda -> Xi`, an RH-equivalent positivity
> = M4) by a Hamburger-style uniqueness statement whose engine is
> Poisson/theta, i.e. lattice-consuming (the #152 fourth clause). Reuses the
> e1k D_log harness (`build_float`; arXiv:2511.22755 Thm 5.10) and the
> `_shared/beurling.py` control. It proves nothing about RH. It measures the
> pin's hypotheses, proves the bare pin false by construction, and isolates
> the corrected pin's one new open lemma. All numbers from the default run
> (dps=25 builds, dps>=30 L-values; 34/34 self-tests).

> **BANNER (read before quoting any number).** The headline negative is
> PROVEN: the bare pin "FE + order 1 + RvM budget => F = c Xi" that #154's
> wording suggests is FALSE (T4g: an explicit two-function counterexample on
> the RvM comb, built from gamma-factor data only). The corrected pin is
> classical Hamburger (1921), whose load-bearing hypothesis is the
> DIRICHLET-SERIES / lattice face, and the finite CCM objects verifiably do
> NOT carry that face globally (T3g: Paley-Wiener obstruction, escape at the
> archimedean rate ~ pi/4). So the identification is split from convergence
> ONLY conditionally, modulo a new open lemma (Dirichlet-face inheritance in
> the limit). ADVERSARY downgrade (2026-07-11): conditional on the limit
> existing with its growth package, that lemma is EQUIVALENT to the
> identification `F = c Xi` it replaces (forward by Hamburger; backward
> trivially, since `c Xi` unpacks to `c zeta`, which IS an absolutely
> convergent Dirichlet series). The corrected split is a positivity-free
> RESTATEMENT of the identification with a different proof surface, not a
> strength reduction; the SURVEYOR's converse-theorem scan reached the same
> verdict independently ("the M4/Section-7 content in yet another costume:
> the pin relocates the work"). Nothing here moves M4. All integer zero
> counts are leading-order +- O(1) (e1l precision caveat class).

## One-line result

The pin's proof engine (Poisson/theta/Mellin, T1) and its type-exclusion face
(T2: D-H fails the Riemann-type FE at O(1) and overshoots the Riemann-type
budget by ~21 zeros at its first off-line height) both work and are K1-clean;
but the budget CANNOT replace Hamburger's Dirichlet hypothesis (T4:
counting-compliant relocations are invisible to it), and the finite-cutoff
family inherits only the cheap faces (FE to 1e-11, exponential type =
log lambda) while the two identifying faces (RvM budget, Dirichlet series)
are measurably NOT inherited (T3): identification-without-positivity survives
only as a conditional route through a cleanly named open lemma that is
conditionally equivalent to the identification itself (see the banner and
the Named residual).

## The pin, stated precisely

For entire `F` in the z-plane (`s = 1/2 + iz`), the candidate hypotheses:

- **H1 (FE data, Riemann type)**: `F` even and real on `R`, unpacking through
  conductor 1 and `Gamma(s/2)` with simple poles of `f` at `s = 0, 1`
  (residues normalized).
- **H2 (growth)**: `F` of order <= 1.
- **H3 (budget)**: full-plane zero count `n_F(r) = (r/pi) log(r/(2 pi e)) +
  O(log r)`, derived from H1 by the argument principle (K1-clean: gamma data
  only, never a zero list).
- **H4 (Hamburger / lattice face)**: the unpacked `f(s)` is a Dirichlet
  series absolutely convergent for `Re s > 1` (the FE partner needs only some
  half-plane). The abscissa clause is load-bearing, not decoration: Knopp
  (Inventiones 117, 1994) shows that weakening it to "absolutely convergent
  in SOME half-plane" leaves an infinite-dimensional solution space
  satisfying H1+H2 (SURVEYOR report, Section 2a), so a pin stated with the
  weaker clause is false too. [ADVERSARY fix: an earlier draft of this
  bullet said "on a half-plane", which is exactly the Knopp-insufficient
  form.]

**Bare pin (H1+H2+H3 => F = c Xi): FALSE** (T4g, proven by construction).
**Corrected pin (H1+H2+H4 => F = c Xi): classical Hamburger 1921**, and then
H3 is redundant. The pin is genuinely lattice-consuming: T1 shows the engine
is Poisson/theta; T5 shows the Beurling fake starves it.

## T1: the lattice engine, verified (all ~1e-36)

| identity | defect |
|---|---|
| Jacobi theta FE `theta(1/t) = sqrt(t) theta(t)` | 1.5e-36 |
| Poisson, shifted-Gaussian dual form | 1.5e-36 |
| `N(x) = x + O(1)` (sup <= 1) | exact |
| Mellin/residue bridge `pi^{-s/2}Gamma(s/2)zeta(s) = 1/(s-1) - 1/s + int_1^inf omega(t)(t^{s/2-1}+t^{(1-s)/2-1})dt` | rel 5.9e-37 |
| completed FE read off the bridge (s <-> 1-s) | 0.0 |

The two residue terms `1/(s-1) - 1/s` are the `s = 0, 1` pole budget: the
half of the #154 determinant data the theta FE produces for free. This is the
engine the pin runs on, and every step consumes the integer lattice.

## T2: D-H excluded BY TYPE, with numbers

- Own FE (conductor 5, `Gamma((s+1)/2)`): max rel residual **1.7e-30** (exact).
- Riemann-type FE (conductor 1, `Gamma(s/2)`): min rel defect **1.72** = O(1).
- Budget curves validated by argument-principle windings of the completed
  functions (function values only): zeta winding 3.000 vs smooth 3.44 at
  T=29.5; D-H winding 10.000 at T=30 (calibrating `c0 = -0.499`), 6.000 at
  T=20 vs predicted 5.25.
- Type-exclusion number: D-H's own FE-derived budget exceeds the Riemann-type
  budget by **20.7 zeros at T = 85.699** (leading term `(log 5/2pi) T = 22.0`).

So a pin stated with Riemann FE data excludes D-H at the level of TYPE (wrong
gamma factor, wrong conductor, wrong budget curve), not by an approximation
defect: D-H's own exact FE is irrelevant to it. This kills the classic
D-H-mimicry route into any converse-pin argument.

## T3: the pin's hypotheses at finite lambda (the new content)

Measured on the FUNCTION `xihat_lambda` (sign changes + winding cross-checks;
NOT the operator eigenvalue budget e1l measured; windings agree with sign
counts exactly: 13 = 13 at lam 3.0, 29 = 29 at sqrt13).

| build | FE defect (even/real) | type/log lam | edge count vs own-RvM vs lattice | low-band fill (T<=13) |
|---|---|---|---|---|
| ZETA 2.2 / N=12 | 1.1e-11 / 9.3e-13 | 0.939 | 4 vs 3.7 vs 7.6 (nearer own) | -0.3 |
| ZETA 2.6 / N=16 | 2.2e-12 / 7.2e-13 | 0.955 | 11 vs 7.0 vs 12.9 (nearer lattice) | +2.7 |
| ZETA 3.0 / N=32 | 1.3e-10 / 8.3e-12 | 0.928 | 13 vs 11.7 vs 19.8 (nearer own) | -0.3 |
| ZETA sqrt13 / N=48 | 6.7e-10 / 2.4e-12 | 0.979 | 29 vs 21.2 vs 33.3 (nearer lattice) | +4.7 |
| D-H 2.6 / N=16 | 2.7e-15 / 6.5e-17 | 0.973 | 12 vs 16.7 vs 12.9 (lattice) | own-curve clean |
| D-H sqrt13 / N=48 | 3.9e-11 / 3.6e-13 | 0.974 | 31 vs 40.9 vs 33.3 (lattice) | own-curve clean |

Face by face:

- **FE face: INHERITED, conditionally and information-freely.** Evenness +
  realness defects 1e-10..1e-15 at every cutoff. Two caveats (SURVEYOR
  Section 3c + ADVERSARY): (i) exact finite-lambda evenness is a one-line
  consequence of CCM's even-simplicity assumption (Def 5.3), which the e1k
  harness ENFORCES by selecting the lowest EVEN eigenvector (`even_frac =
  1.00000` at all six builds this run; at a Remark 2.3 event, where the
  global minimum is odd, the TRUE ground state would fail this face at O(1)
  and the harness substitutes the lowest even state, flagged via
  `even_assumption_ok`); (ii) because evenness is free-by-assumption, the
  tiny defect carries NO pinning content: it is a numerics/even-simplicity
  monitor, in the same information-free class as finite-cutoff reality
  (#154/#158). All pinning content must come from the budget/lattice faces.
- **Growth face: INHERITED, and it is the PW bound.** Exponential type =
  0.93..0.98 x log lambda (the Paley-Wiener support `L/2 = log lambda` of the
  log-circle). Also PROVEN in-build: `xihat(phi m) = 0` exactly for `|m| > N`
  (common `sin(zL/2)` factor; measured <= 1.5e-17 relative), so the far
  budget is the exact lattice line: an installed, arithmetic-free tail.
- **Budget face (H3): NOT inherited; it is TWO-REGIME and type-aware.**
  - D-H (clean control): arithmetic own-RvM core below its own
    conductor-rescaled horizon (~`Twin/5`), then LATTICE regime: mean spacing
    in `[0.5 Twin, Twin]` is `phi` to 2-3 percent while its own-RvM spacing
    is 48-64 percent away. Below the horizon the own conductor-5 curve beats
    the zeta-type curve decisively (n(41) = 15 vs own 15.8 vs zeta-type 6.5
    at sqrt13): the budget face KNOWS the conductor at finite lambda. This
    refines e1l, whose eigenvalue count with the zeta window imposed on both
    twins was blind; against each twin's OWN curve the low-window zero
    profile is type-aware (an input-level distinction, exactly where #154
    said the real discrimination lives; the edge count law stays blind).
  - ZETA: accurate arithmetic core in the middle band, but the low band
    `[0, 14]` (own-RvM ~ 0.3 zeros) is ERRATICALLY filled with ~phi-spaced
    zeros: cleared at lam = 2.2, 3.0; filled (+3, +5) at lam = 2.6, sqrt13.
    The edge count is only BRACKETED between own-RvM and the lattice line.
    **Pole ablation (T3i)**: rebuilding zeta without the pole term leaves the
    low-band fill unchanged (3 -> 3 at lam 2.6; 5 -> 5 at sqrt13) and pushes
    the edge count UP to the lattice value (11 -> 12 at 2.6; 29 -> 33 = 33.3
    at sqrt13): the fill is the finite object's LATTICE FLOOR, not a pole
    artifact, and the pole term actually pulls the count toward RvM.
  - Consequence for the pin: H3 for the limit cannot be certified by finite
    truncations; the budget is exactly what the (M4) limit must PRODUCE.
- **Dirichlet face (H4): NOT inherited; windowed with a measured escape
  rate.** Unpacking `f_lam(s) = xihat(z)/[(s(s-1)/2) pi^{-s/2} Gamma(s/2)]`
  on `Re s = 2`: it tracks `zeta(2+it)` only for `t <= t_dir ~ 6..7` at ALL
  four cutoffs, then diverges at rate 0.68..0.78 ~ `pi/4 = 0.785` (fit beyond
  `phi N`). The obstruction is structural (PROVEN-tier, classical): a
  Paley-Wiener function of finite type cannot decay exponentially on the real
  axis (compact FT support + exponential decay would force a real-analytic,
  hence zero, FT), while the Gamma factor demands decay `e^{-pi t/4}`. So NO
  finite-cutoff object of this family carries H4 globally; the archimedean
  decay face IS the Dirichlet face, and it can only appear in the limit.
  (This is the C3 archimedean-injection statement in converse-theorem
  clothing, and it quantifies e1k's stealth window from the modulus side.)

## T4: the pin's teeth, and its edge

- **P1 (budget kills profusion).** `F1 = Xi(z)(1 + 0.9 cos 2z)`: even, real,
  order 1, extra zeros in-strip at `Im z = +-0.2336` (closed form, verified
  `|F1(z0)| = 2.5e-17`, winding 1). Strip count on `[1, 29.5]`: **21 vs bare
  Xi 3 vs RvM 3.4** (measured excess 18, predicted `(a/pi)T = 18.1`): any
  FE-preserving oscillation factor adds a LINEAR zero excess and the budget
  kills it. The budget clause has real teeth: Knopp-profusion-type solutions
  are counting-incompatible.
- **P2 (the budget must be full-plane).** `F2 = Xi(z)(1 + 0.05 cos 2z)`:
  extra zeros at `Im z = +-1.84`, OUTSIDE the strip. Strip count unchanged
  (3 = 3): a strip-only budget is blind to it. Full-plane count catches it:
  **42 vs 6** on `[-29.5, 29.5] x [-2.6, 2.6]`. H3 must be the Hadamard/genus
  full-plane count.
- **P3 (the kill: budget does not pin).** RvM-comb points `t_k` defined by
  smooth inversion `n_smooth(t_k) = k` (gamma data only; no zeta zero
  consumed; `t_1 = 17.85 != gamma_1`, deliberately). `G1 = prod(1 -
  z^2/t_k^2)`, `G2` = same with the first 60 points relocated by 0.3 of the
  local gap, alternating sign (no crossings). Both: even, real, order 1 (the
  infinite products; exponent of convergence 1), identical zero-counting
  functions = RvM + O(1) (verified at T = 50, 150, 250), both unpackable at
  the pole slot (`|G(-i/2)| = 1.0045`). Distinct: max pointwise
  `|G1-G2|/(|G1|+|G2|) = 1.000` on `[1, 30]`. **Hence H1+H2+H3 admit at least
  a 60-parameter family (in fact infinite-dimensional): the bare pin is
  FALSE.** Uniqueness needs zero LOCATIONS, and counting can never supply
  them; only Hamburger's lattice hypothesis (H4) does.

## T5: Beurling failure, named clause

Density-matched fake (`b_p = p e^{eps_p}`, eps iid U[-0.25, 0.25], seed 149,
1754 primes): theta FE relative defect **0.37** (Z: < 1e-25); integer count
best-linear sup error **297** at x <= 2e4 (Z: <= 1); Euler product side fine
(`zeta_B(2) = 2.1393`, stable). NAMED FAILING CLAUSE: no additive lattice =>
no Poisson => no theta FE => no completed function symmetric in `s <-> 1-s`
=> H3 is UNDERIVABLE (the argument-principle budget needs the FE strip
symmetry) and the T1 engine has no fuel. The fake even HAS a Dirichlet series,
but on non-lattice frequencies `{log n_B}`, where Hamburger's mechanism has
no purchase. The pin fails at H1-engine + H3 + H4 simultaneously: it pays the
#152 fourth clause at three named sites.

## T6: K1 / discipline audit

Source scan clean (no zero-list or zero-scanner token in the pin path);
runtime guards on the mpmath and D-H zero scanners installed and never
tripped; per-test input ledger printed (T1: lattice + Gaussians + gamma data;
T2: function VALUES + gamma data; T3: e1k ground state + smooth curves +
reference VALUES; T4: Xi values + smooth-inverted comb; T5: the fake). The
budget hypothesis is used ONLY in its FE-derived form. NG1/C3: nothing
endomorphism-shaped anywhere; the only route from the finite object to prime
data is the archimedean unpacking (T3g), conforming to the #156/#157 no-go
geography automatically. One transparency note (builder-flagged, ADVERSARY
concurs it is placement-only): the T4a/T4b contour height 29.5 was chosen to
keep `gamma_4 = 30.42` off the contour for numerical conditioning; the
counts are integer-certified by winding residuals < 0.02 and no claim
consumes the ordinate (any nearby height works).

## Verdict fields

| field | verdict |
|---|---|
| `pin_hypotheses_verifiable_at_finite_lambda` | MIXED: FE YES (1e-11), growth YES (type = log lambda), budget NO (two-regime, type-aware core + lattice floor/tail), Dirichlet NO (window t ~ 7, escape at pi/4) |
| `budget_kills_fe_perturbations` | TRUE for profusion (measured excess 18 ~ (a/pi)T = 18.1, and 36 off-strip caught full-plane); FALSE as a uniqueness pin (P3) |
| `beurling_fails_nameably` | TRUE: no lattice => no theta FE (defect 0.37) => budget underivable; engine unfueled |
| `dh_excluded_by_type` | TRUE: own FE 1.7e-30 vs Riemann-type defect 1.72; budget surplus 20.7 zeros at T = 85.7 |
| `k1_clean` | TRUE (T6; budget curves from gamma data only, guards never tripped) |
| `identification_split_from_convergence` | REFORMULATED, NOT REDUCED (ADVERSARY downgrade): bare split DEAD (PROVEN, T4g); corrected split = Hamburger modulo Dirichlet-face inheritance, which is conditionally EQUIVALENT to the identification it replaces (given the limit + growth package: H4 => F = c Xi by Hamburger, F = c Xi => H4 via zeta's own series). The gain is a positivity-free proof surface, not a weaker open statement |

## Tiered claims

**PROVEN** (constructions/classical facts, numerically instantiated here):
1. H1+H2+H3 do not pin `Xi`: the P3 relocation family (T4g). The #154
   wording "FE + budget + growth => limit = Xi" is false as stated.
2. The Dirichlet face cannot hold globally at any finite cutoff: Paley-Wiener
   functions of finite type cannot decay exponentially on `R` (T3g's
   obstruction), while H4 + the Gamma factor force decay `e^{-pi t/4}`.
3. `xihat_lambda(phi m) = 0` for `|m| > N`: the far budget is an installed
   lattice line, exactly (two-line algebra from the common sin factor).

**NUMERICAL** (measured on this faithful-but-not-exact reimplementation):
4. The budget face is two-regime and type-aware: own-RvM core below a
   conductor-rescaled horizon (D-H's at ~`Twin/5`), lattice regime above
   (spacing = phi to 2-3 percent); zeta's low band erratically lattice-filled
   (not pole-caused: T3i ablation, edge 29 -> 33 = lattice without the pole).
5. The Dirichlet-face window is `t_dir ~ 6..7` across lambda in [2.2, 3.6]
   with escape rate 0.68..0.78 -> pi/4; the window did NOT grow over this
   lambda range (a quantitative face of the archimedean stealth window).
6. D-H type-exclusion numbers (T2) and the budget-kill numbers (T4b/T4d).

**CONJECTURE / OPEN**:
7. THE OPEN LEMMA (Dirichlet-face inheritance): if `xihat_lambda -> F`
   uniformly on compacts of the strip (weaker than the full CCM Section-7 /
   M4 statement, which also names the limit), does `F` extend to an entire
   function of finite order whose unpacking carries a Dirichlet expansion
   absolutely convergent for `Re s > 1` (H4, abscissa included) with the
   Riemann FE data? If YES, Hamburger pins `F = c Xi` with NO positivity
   input. Nothing at finite lambda supplies any part of this: not H4
   (claims 2, 5), and not the growth/entirety package either (the finite
   types `log lambda` DIVERGE, and strip-local convergence bounds nothing
   off the strip), so only the FE face is genuinely free in the limit.
   ADVERSARY status of the lemma: conditional on the limit + growth
   package, it is EQUIVALENT to the identification `F = c Xi` (backward
   direction trivial via zeta's own series), i.e. it is the Section-7
   identification restated in lattice vocabulary; and the SURVEYOR's scan
   (report Section 2c) found NO converse theorem that weakens H4 to
   something the family visibly inherits: the nearest relatives (Ki 2012,
   Hu-Li 2016) consume zero SETS plus a sigma->+inf normalization, both
   failing at finite cutoff. The only candidate route is the determinant
   identity `det_reg = -i lambda^{-iz} xihat(z)` plus the prime comb,
   unproven.

## Citation-level facts (SURVEYOR-verified 2026-07-11; see
`scratchpad/hamburger_pin/01_surveyor_converse_theorems.md`)

- Hamburger 1921, fetched form (K-P survey arXiv:1605.02354 Thm 2.1,
  cross-checked vs arXiv:2008.02570 Thm D): Dirichlet series absolutely
  convergent for `sigma > 1` + `(s-1)^m F` entire of finite order + Riemann
  FE => `F = c zeta`. The abscissa is the load-bearing clause.
- Knopp 1994 (Inventiones 117, 361-372, as quoted by 2008.02570): weakening
  the abscissa to "absolutely convergent in SOME half-plane" leaves
  infinitely many linearly independent solutions (modular integrals with
  rational period functions). Our P3 is an independent constructive witness
  at the counting level (outside the Dirichlet class), so the probe does not
  DEPEND on this citation.
- Kaczorowski-Perelli, extended Selberg class `S#`, degree-1 classification
  (fetched via arXiv:1903.06145 eq. 1.3): conductor-1 even data collapses to
  `c zeta`; at conductor q the solution space has dimension growing with q
  (D-H lives in the q = 5 space, itself a witness that FE-uniqueness fails
  away from conductor 1).
- Budget-substitution converse theorems: NONE exist (surveyor
  fetched-absence, Section 2c); nearest relatives Ki 2012 (level sets) and
  Hu-Li arXiv:1610.01583 (zero-set inclusion + sigma->+inf normalization,
  with their Thm 2.4 warning that such normalization clauses can be
  RH-hard).
- Titchmarsh (D-H construction, kappa value): already repo-verified in
  `_shared/davenport_heilbronn.py` numerics.
- CCM: constant-density remark for the finite spectrum and Thm 5.10(ii)
  (zeros of xihat = spectrum of the perturbed operator): consistent with our
  function-count = e1l's eigenvalue plateau (13 at lam 3.0, 29 at sqrt13).

## Named residual

The pin, corrected, removes POSITIVITY from the vocabulary of the
identification step and replaces it with the lattice (Hamburger). What
remains is exactly: (1) the uniform det-class limit itself = M4 (untouched,
as expected), and (2) the Dirichlet-face inheritance lemma (claim 7).
ADVERSARY correction: the lemma is NOT strictly smaller than the
identification; conditional on the limit + growth package it is EQUIVALENT
to it (claim 7). What the pin genuinely buys is a different proof surface:
the open step can now be attacked zero-free and positivity-free (via the
determinant identity + prime comb) instead of variationally, and the bare
budget route into it is proven closed (T4g). Upgrade-spec scoreboard
(#154): (1) trivial circle budget = the exact lattice tail, PROVEN in-build
(claim 3); (3) absorption count = e1l (measured); (4) Hamburger pin = this
probe. Ingredient (2), rank-one interlacing, remains UNTOUCHED: three of
the four ingredients are now executed, not all four.

## Limitations

- e1k inheritance: faithful reimplementation, not the paper's exact operator
  (razor-thin margin `eps ~ 3e-5`, approximate pole realization); integer
  counts are O(1)-fragile across dps (e1l STEP 5). The two-regime LAW and
  the face verdicts are robust; individual integers are not.
- The low-band lattice-fill clearance (0/3/0/5 across zeta builds) is
  unexplained: erratic in N and lambda; the ablation only rules OUT the pole
  term as the cause.
- `t_dir` was measured at four smallish lambdas; its (non-)growth with
  lambda is not established beyond this range.
- The D-H budget `c0` constant is calibrated by one winding (type-level, but
  a calibration); the density is pure gamma data.
- P3's numerical instances are truncated products (polynomials); the PROOF
  of non-uniqueness uses the classical canonical-product facts (order =
  convergence exponent), not the numerics. The numerics instantiate
  distinctness and budget compliance in the working window. ADVERSARY
  robustness sweep (2026-07-11): relocation fractions {0.1, 0.3, 0.45} x
  blocks {[0,60), [40,99), [100,160)} x K in {100, 400} all stay ordered,
  budget-compliant (<= 2 off the smooth curve at T = 50/150/250), and
  pointwise-distinct (supdiff 1.000); distinctness is structural
  (`G1(t_1) = 0` exactly, `|G2(t_1)| != 0`), and no scaling symmetry maps
  the zero sets (head ratio 1.0895 vs tail ratio 1.0000).
- Threshold provenance (builder notes, kept honest here): T1, T2b/T2e,
  T3b/T3c, and the T4 family were pre-registered; the T3e/T3f/T3h spacing
  and bracket tolerances, the T3g rate window [0.55, 1.15] x pi/4, and T3i
  are measured-then-pinned REGRESSION PINS (set at ~2x margin after the
  first full run). Claims about the second group are stated from the
  measurements, not from the thresholds.
- Even-simplicity conditionality: every T3 build had `even_frac = 1.00000`,
  but the harness selects the lowest EVEN eigenvector by construction, so
  the FE face is enforced, not discovered (see the T3 FE-face bullet; a
  Remark 2.3 odd-minimum event would falsify the assumption, not this
  probe's numbers).

## Handed forward

- The Dirichlet-face inheritance lemma (claim 7) as a BUILDER/SURVEYOR
  target: can `det_reg = -i lambda^{-iz} xihat(z)` + the prime comb produce
  H4 for the limit without passing through Weil positivity?
- The type-aware horizon law (budget face knows the conductor below
  `~2 pi lambda^2 / q`) as a cheap discriminator for any future finite-cutoff
  determinant family: a family whose low-window zero profile does NOT track
  its own conductor-rescaled RvM curve is not even input-faithful.
- The `t_dir` non-growth question (does the Dirichlet window widen with
  lambda at fixed absolute height? measured: no, ~7 throughout): if it
  provably cannot widen, that is a sharper form of the stealth window.

## Verification targets (for VERIFIER)

1. **Lattice tail**: for the explicit finite family, `xihat(phi m) = 0` for
   all `|m| > N` (finite real algebra; the common `sin(zL/2)` factor).
2. **Non-uniqueness kernel (finite surrogate)**: two distinct even real
   polynomials with identical zero counts in every interval (trivial), then
   the honest target: distinct even real entire order-1 functions with
   zero-counting functions differing by O(1) (canonical products over two
   interlacing combs; needs Mathlib's `order` machinery or an axiomatized
   order statement).
3. **P1 excess law**: the zero set of `1 + c cos(az)` for `0 < c < 1` is
   `{(2k+1) pi / a +- (i/a) arccosh(1/c)}`: closed form, formalizable; count
   in a rectangle = `(a/pi) T + O(1)`.
4. **PW no-exponential-decay**: an entire function of exponential type whose
   restriction to `R` is `O(e^{-a|t|})`, `a > 0`, and whose FT is compactly
   supported, vanishes (the T3g obstruction; classical, good Lean target).

## Adversarial test cases (for ADVERSARY)

1. **P3 robustness**: rerun with different relocation fractions (0.1..0.45),
   different relocated blocks, K in {100, 400}: non-uniqueness and budget
   compliance must persist. Attack the truncation: verify the tail factor
   beyond K does not re-pin uniqueness (it cannot: it is zero-free in the
   window, but check the numbers).
2. **Budget rescue attempts**: try adding S(T)-type constraints (bounded
   argument fluctuation, mean-square of S) to H3 and check P3 still passes
   them (predicted: yes, relocations of size o(gap) leave S-statistics
   within allowance): would show even refined counting cannot pin.
3. **dps sensitivity**: rerun T3 at dps 15/35; the two-regime law and face
   verdicts should hold, individual counts may shift by O(1) (e1l class).
4. **The lattice-floor mystery**: vary N at fixed lambda = 2.6 (N = 12..24)
   and map when the zeta low band clears; if clearance correlates with the
   even-block margin or `N mod` structure, name it.
5. **t_dir growth**: measure the Dirichlet window at lambda = 5 (N ~ 90
   build, expensive) to test whether `t_dir` stays ~7 (predicted) or grows.
6. **Winding-vs-sign-count**: rerun T3d at dps 15 where e1l saw zeta ghosts
   at `re = +-26.6` INSIDE the window; the winding should then EXCEED the
   sign count by the ghost pairs: confirms the cross-check has teeth.

## Reproduce

```
python3 -m experiments.spectral.e1m_hamburger_pin           # full (~3.5 min)
python3 -m experiments.spectral.e1m_hamburger_pin --quick   # ~35 s
```
Outputs `e1m_hamburger_pin.npz` (budget profiles + zero lists per build, FE/
type/tail defects, Dirichlet windows and escape rates, T2 type-exclusion
numbers, T4 windings and comb, T5 fake numbers).
