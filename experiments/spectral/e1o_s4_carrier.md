# E1O: the S4 skeleton on the CCM carrier (the S4/R1 arc, first executable)

> Companion to `e1o_s4_carrier.py` / `.npz`. Executes the first probe of the
> S4/R1 arc left open by [`landau_one_sided.md`](../../docs/03_research/landau_one_sided.md)
> Sections 3.4-3.6/5 (LEARNINGS #161): pose Stepanov's S4 move (cheap
> multiplicity buying a one-sided COUNT upper bound) on the CCM prolate/PW
> carrier, measure what the known cheap mechanism (Beurling-Selberg
> majorants) certifies, test whether the carrier adds leverage, and bank
> the forcing spec. Companion SURVEYOR map: `scratchpad/s4_carrier/01`
> (gitignored); builder derivations: `scratchpad/s4_carrier/02`. Reuses
> comb streams from e1k and the `_shared/beurling.py` control; no operator
> is rebuilt. It proves nothing about RH. All numbers from the default
> full run (19/19 self-tests, ~2 s; `--quick` reduced grids, 19/19).

> **BANNER (read before quoting any number).** Three headline facts.
> (1) The naive band-limited majorant pairing against the full von
> Mangoldt comb DIVERGES at every type (the comb density e^u beats the
> majorant's sinc^2 tails): the classical skeleton is ILL-POSED without a
> horizon device, and the CCM carrier's injection horizon p <= lambda^2
> is exactly such a device. (2) With the sharp horizon the certified
> bound is psi(x) <= x (1 + c/delta) with c = m+/2 ~ 0.096 measured: the
> factor-family, error LINEAR in x; the Landau threshold x^{1/2+eps} is
> not approached, and the DIMENSION BUDGET IS NOT THE WALL (needed
> dimension x^{1/2} log x vs carrier Shannon 4x: ratio 3.5e-3 at
> x = 1e6; adversary-corrected 2026-07-11, the draft's /(2 pi) was a
> convention slip). The wall is that the smoothed sum is unconditionally
> unevaluable (its explicit-formula zero side IS location data). (3) The
> carrier adds no leverage where testable: majorant-nil (structural: the
> carrier's function space at fixed type is the generic trig space),
> Sonin untestable from cache, and multiplicity FULL PRICE at the
> log-prime comb for every decimation at every lambda, while the SAME
> probe shows multiplicity cheap at commensurate (AP / per-prime-circle)
> combs: the S4 absence re-measured on the newest carrier, with the
> lattice clause visible. Frontier: UNMOVED; the Q4 spec is banked.

## One-line result

The S4 slot on the CCM carrier is posed exactly and measured empty: the
only occupant (Beurling-Selberg one-sidedness) is a Nyquist-cell tax
(c/delta relative, system-generic, proven-by-execution on the Beurling
fake, unposable for D-H), the carrier's structure supplies the horizon
the pairing needs but no majorant or multiplicity discount (full price at
log-primes, cheap exactly at the commensurable combs where Frobenius
lives), and the missing mechanism is now a spec: a lambda-uniform
rank-collapse at the log-prime comb whose only known sources are
commensurability (absent over Z) or the additive lattice (unconsumed).

## Q1: the skeleton, posed exactly (skeleton_posed = YES, with an ill-posedness clause)

**The formalization chosen** (the Beurling-Selberg route, the cleanest
classical form). Aux function class: F entire of exponential type
2 pi delta, F(u) >= chi_[0,L](u) on R, L = log x; the extremal solution
is Selberg's S(u) = (1/2)[B(delta u) + B(delta(L-u))] built from
Beurling's B (type 2 pi, B >= sgn, int(B - sgn) = 1, extremal; T1
validates the polygamma implementation: interpolation nodes exact, min
violation 0.0, excess integral 0.9987 with tail estimate 1e-3, interval
excess 1/delta to 3 percent).

**The pairing, written explicitly, sides marked.**

```
  psi(x) = sum_n Lambda(n) chi_[0,L](log n)
        <= sum_n Lambda(n) S(log n)                       [PRIME SIDE]
         = (explicit formula) pole term + archimedean term
           - sum_rho Shat-type(z_rho)                     [ZERO SIDE]
```

- PRIME SIDE: unconditional, GIVEN Lambda(n) >= 0. This is the Euler
  gate (the same clause as Landau's Lemma L): coefficient nonnegativity
  is an Euler-product face. It is also system-generic: any nonnegative
  comb passes (Q2).
- ZERO SIDE: NOT unconditional as a bound. Shat-type(z) at a zero
  rho = beta + i gamma grows like x^{beta - 1/2} off the line; bounding
  the zero sum by structure alone (N(T) from the argument principle,
  K1-legal) returns psi(x) <= x + O(x^Theta polylog): the Landau
  DICTIONARY back again, no location produced. Every published
  majorant+explicit-formula instance consumes RH before the positivity
  fires (surveyor Section 3's structural law); the reverse direction is
  the absent one, and this probe now adds a sharper clause:

**The ill-posedness finding (T2a, measured).** Against the FULL comb the
prime side diverges at every type: teeth at u = log n carry weight
Lambda(n) ~ density e^u while S's tails decay only like
(delta(u - L))^{-2}; measured excess at (x, delta) = (300, 8) grows
3.3 -> 28.5 as the horizon Xh runs from x to e^8 x (factor 6.3 by e^6 x,
monotone). So the classical skeleton cannot even be POSED on the line
against the raw comb: it requires a horizon truncation (valid for any
Xh >= x since S >= chi >= 0 pointwise). The CCM carrier's log-circle +
injection horizon p <= lambda^2 is exactly such a device: the carrier's
structure is FORCED by the pairing, a nontrivial consonance between the
CCM construction and the counting skeleton. (The classical literature
avoids the divergence by pairing on circles/finite windows (large sieve,
Erdos-Turan) or by consuming RH on the zero side; the surveyor's map has
no third mode, and this measurement is why.) ADVERSARY NOTE (2026-07-11,
structural tier): the divergence is FAMILY-UNIVERSAL, not
Selberg-specific. Re-measured increments follow e (k/(k+1))^2 exactly
(ratios 2.03/2.10/2.18/2.22 vs model 2.00/2.08/2.15/2.20 at x0 = 30,
horizon to e^10 x): genuine divergence, not slow convergence. And no
band-limited majorant family evades it: S >= chi >= 0 integrable of
exponential type factors as |g|^2 (Krein) with g in the Cartwright
class, whose log-integral condition caps real-axis decay strictly below
e^{-u}, while convergence against the e^u comb density needs
e^{-(1+eps)u}; true exponential decay would make the transform analytic
in a strip, contradicting compact spectrum. Fatter-tailed variants only
trade constants for onset: a sinc^{2m} bump majorant (m = 4, same type)
inflates the horizon excess ~6x while pushing the visible divergence
onset beyond e^{40} x. Horizon device REQUIRED for every family.

**The excess law and the constant (T2b, measured).** At the sharp
horizon Xh = x:

```
  excess(x, delta) = c(delta) x / delta,   c -> m+/2 = 0.0956
```

with m+ = int_0^inf (B - 1) = 0.1912 (measured; the INSIDE excess mass
of B; the factor 1/2 because Selberg's majorant carries half a B-excess
per endpoint and only the right endpoint sees the e^L density; the
e^{-w/delta} tilt is the O(1/delta) correction). Measured c: 0.073-0.093
across delta in {4, 8, 16}, x in [300, 1e5] (per-delta medians
0.080/0.087/0.088), stable in x (median at delta = 16: 0.088 vs 0.096
predicted). ADVERSARY EXTENSION (2026-07-11): delta pushed to {32, 64},
x to 1e6: c = 0.089-0.095, frac(delta L)-robust (0.0955 at two
incommensurate x); and the measured c(delta) tracks the derivable tilt
law c_tilt(delta) = (1/2) int_0^inf (B(w) - 1) e^{-w/delta} dw =
0.0784/0.0850/0.0893/0.0920/0.0935 at delta = 4/8/16/32/64, limit
m+/2 = 0.0957 (m+ re-measured 0.191348 on a grid to 2000 with tail),
within ~2 percent at every delta: the m+/2 identification is CONFIRMED
as the delta -> inf limit of a verified law, not a coincidence of the
delta range. Certified bound:
psi(x) <= x (1 + c/delta): RELATIVE error O(1) at fixed type, and the
certified error grows LINEARLY in x (fitted exponents 0.989/0.995/1.022
vs the Landau threshold's 1/2). This is the factor-FAMILY: the
one-sidedness tax is a fixed fraction of a Nyquist cell of comb mass.

**Where the dimension budget appears (T2c), and the honest surprise.**
To force c x/delta <= x^{1/2+eps} one needs type delta ~ c x^{1/2-eps},
i.e. majorant dimension ~ 2 delta L ~ x^{1/2} log x (frequencies
|n| <= delta L on the circle R/LZ have exponential type 2 pi n/L <=
2 pi delta, count 2 delta L + 1, the same 2N+1 convention as the
carrier's 4 lambda^2 = 2 N_c + 1, N_c = 2 lambda^2; adversary-corrected
2026-07-11, the draft's delta L/pi was a tau-vs-delta slip, off by
2 pi). The carrier's Shannon budget at its horizon window x = lambda^2
is 4 lambda^2 = 4x (e1g/e1l verified). Ratio needed/available = 3.5e-3
at x = 1e6 and -> 0. THE BUDGET IS AFFORDABLE: unlike over F_q (where the
degree budget is the binding constraint that Frobenius relaxes), on this
carrier the binding constraint is not dimension at all; it is that the
smoothed prime sum at that type is unconditionally unevaluable (the zero
side above). S4's real absence is therefore NOT a budget shortfall but a
mechanism shortfall, which Q3(c) then locates precisely.

**The factor 2, derived not cited (T2d + T2b).** Two DISTINCT 2-shaped
constants, kept apart:
- The SIEVE 2: a minimal Selberg Lambda^2 sieve (implemented: G(z) =
  sum_{d<=z} mu^2(d)/phi(d), bound = x/G(sqrt x)) gives
  bound * log x / x = log x / ((1/2) log x + c') = 1.558, 1.626, 1.677
  at x = 1e4, 1e5, 1e6: monotone INCREASING toward the ceiling 2, never
  through it. The 2 is the level-halving log D -> (1/2) log D: the
  quadratic pairing (Lambda^2 weights, the only unconditional positivity
  available) spends the budget at its square root. Over F_q Stepanov's
  pairing is LINEAR (degree counts, not squared weights) because
  Frobenius supplies the vanishing; the halving is exactly what S4-over-Z
  would delete. #146's parity mechanism explains why the sieve 2 is a
  ceiling (sign-flip invariance of the axioms).
- The MAJORANT cell constant c ~ m+/2: a band-limit uncertainty price
  (Beurling extremality), NOT parity. The majorant+minorant bracket
  costs one full cell (excess = deficit = 1/delta each side).
Conflating the two would overclaim; the parity_crosscheck field carries
both.

## Q2: the constant measured, and the trap made concrete (system_generic_proven = YES)

Zeta numbers: Q1 above (c = 0.073-0.093, linear-in-x error, sieve
constants 1.56-1.68 rising to 2).

**The Beurling fake through the IDENTICAL machinery (T3).** The default
repo fake (b_p = p e^{eps_p}, eps = 0.25, seed 149; 3245 perturbed
primes, 3796 teeth) has a nonnegative comb, so the prime side runs
verbatim:

| delta | x | c_zeta | c_fake | rel diff |
|---|---|---|---|---|
| 4 | 1000 | 0.076 | 0.083 | 0.09 |
| 4 | 3000 | 0.082 | 0.070 | 0.14 |
| 4 | 10000 | 0.081 | 0.079 | 0.02 |
| 8 | 1000 | 0.088 | 0.075 | 0.14 |
| 8 | 3000 | 0.082 | 0.074 | 0.10 |
| 8 | 10000 | 0.088 | 0.086 | 0.02 |

Same law, same constant scale (max rel diff 0.14, median 0.10; at small
x the fake's local density jitter dominates, excluded by pre-registered
x >= 1000). The mechanism consumes ONLY nonneg-comb + density, so it
cannot distinguish zeta from a lattice-free fake: system-generic PROVEN
BY EXECUTION. By the surveyor's sourced DMV kill (6.3: the
Diamond-Montgomery-Vorhauer system has every input this mechanism reads
and violates the one-sided Landau bound at EVERY exponent below 1), any
mechanism in this input class is pre-killed. The lattice-consumption
clause of the tasking is therefore not optional hygiene; it is the
difference between a mechanism and a tautology.

## Q3: the carrier delta (carrier_delta = NIL / UNBUILDABLE / ABSENT-with-control)

Per candidate, tested vs not-buildable stated precisely:

- **(a) Carrier-native majorant: NIL, structural + measured.** On the
  log-circle R/LZ the carrier's u-side function space at frequency
  budget N is span{e^{2 pi i n u/L} : |n| <= N} = the FULL degree-N trig
  space (the Vhat_n basis is exactly its z-side image; the ground state
  xi only chooses coefficients INSIDE it, and the det_reg identity
  constrains those coefficients, not the space). So "a better majorant
  from the E-map/det_reg structure at the same type" is structurally
  impossible: the extremal problem over the space is the generic one.
  Measured confirmation (T4a): LP extremal excess over the span at
  degree N in {8, 16, 32} (grid 4096 + 10x off-grid robustness pass,
  violations <= 1.3e-3 handled by margin re-solve) = 0.247, 0.127,
  0.075 vs periodized-Selberg L/N = 0.275, 0.137, 0.069: ratios
  0.90-1.10, i.e. Nyquist-cell scale, the [L/(N+1), L/N] generic band.
  No carrier discount exists at any tested degree.
- **(b) Sonin/two-sided structure: UNBUILDABLE FROM CACHE.** The
  e1k/e1n artifacts carry ground states and xihat evaluators, no Sonin
  projector; building one is a new experiment (the e1g/e1l prolate
  operators are counts, not a usable Sonin basis on this grid).
  Recorded, not faked. The surveyor's Section 4 found the corresponding
  literature slot (one-sided extremal problems in Sonine spaces) also
  empty, so nothing is being silently skipped that print answers.
- **(c) Multiplicity: ABSENT at the arithmetic comb, PRESENT at
  commensurate combs (T4c/T4d, the heart).** The F_q mechanism in
  carrier terms: a decimated subspace V_K = span{e^{2 pi i (Km) u/L}}
  consists of functions through the K-fold covering of the circle (the
  circle's "Frobenius"); it cannot separate points differing by L/K, so
  if the comb is an AP of spacing L/K, one vanishing condition pays for
  all K points. Measured cost ratio (rank of the evaluation matrix /
  number of conditions), 12 (lambda, K) cells, lambda in {2.2, 3.0,
  sqrt13, 6.0}, K in {2, 3, 4}:
  - log-prime comb {log p : p <= lambda^2}: ratio = 1.000 EVERYWHERE
    (min sv 0.08-0.98: genuinely full rank, not lenient-threshold rank;
    conditioning reported precisely so near-rank-deficiency cannot be
    passed off as cheapness, which would be the superresolution mirage).
    FULL PRICE, lambda-uniformly: the S4 absence re-measured on this
    carrier.
  - AP comb at kernel spacing: ratio 0.50 / 0.25 / 0.20 / 0.09 (= 1/J):
    maximal collapse. The mechanism CLASS exists on the carrier; it
    fires exactly at commensurate combs.
  - per-prime circle (T4d): the orbit {k log p} on R/(log p)Z has cost
    ratio 0.20 (1/5 ideal at 5 points): per-prime cheapness is EXACT,
    the multiplicity avatar of #153's per-prime W6 exactness.
  Reading (mechanism tier, not theorem): over F_q the point set IS an
  AP in u (log of the geometric lattice q^k): Frobenius = the
  commensurability of the value group. Over Z the logs of distinct
  primes are Q-linearly independent: no decimation, hence no
  decimation-sourced cheap multiplicity, at any lambda (what IS proven:
  decimated nodes stay distinct by unique factorization, and distinct
  nodes give a nonsingular trig Vandermonde; non-decimation families
  are the forcing question, adversary-attacked below with five
  families, none collapsing). The absence is not a failure to find a
  trick; it is the incommensurability of {log p}, and the glue that
  would tie incommensurable circles together is the additive lattice
  (integer counting x + O(1) / Poisson), which nothing in this probe
  consumes.

  [AMENDED (correction 2026-08-26, salvaged from PR #7; LEARNINGS #210),
  docs/03_research/reading_notes/modular_hecke_sweep_2026-07-30.md D1.]
  This paragraph previously read "the only KNOWN structure that ties
  incommensurable circles together is the additive lattice". That is
  FALSE AS WRITTEN. There are exactly TWO known glues: the additive
  lattice, and Lee-Yang stability of a multivariate polynomial
  (Kurasov-Sarnak, J. Math. Phys. 61 (2020) 083501, arXiv:2004.05678,
  Thm 1: for ARBITRARY reals b_1..b_n > 1, a positive Fourier
  quasicrystal with spectrum {sum m_j log b_j} supported on the real
  zeros of P(b_1^-s, ..., b_n^-s); classification by Alon-Cohen-Vinzant
  arXiv:2303.03201 Cor. 1.4). The VERDICT SURVIVES WITH A BETTER REASON:
  the second glue needs no lattice and no integrality, and takes an
  arbitrary multiplicative generator set as input, so it is
  Beurling-generic BY ITS OWN HYPOTHESES and the DMV screen
  (s4_carrier_audit.md Section 3) kills it BY NAME. S4 clause 4
  (lattice-consuming, MANDATORY) is CONFIRMED, not weakened. One open
  tension is logged as D3 (Kurasov-Sarnak's mechanism IS Lee-Yang
  stability, which the breadth program demoted as wrong polarity;
  LEARNINGS #210), unresolved here.

## Q4: the diff, stated (s4_spec, the handed-forward artifact)

**S4-SHARP ON THE CCM CARRIER (spec, conjecture tier).** Produce, for
each lambda, a nonzero functional device F_lambda on the carrier's
log-circle (dim budget <= 4 lambda^2) with:

1. ONE-SIDEDNESS: F_lambda >= chi_[0,L] on the comb support, L <=
   2 log lambda (the certified window; BRIDGE-H's input layer).
2. CHEAP MULTIPLICITY (the S4 slot): the vanishing/interpolation
   conditions at the log-prime-power points {k log p} of total order M
   cost o(M) dimensions, lambda-uniformly. Equivalently: a
   lambda-uniform RANK COLLAPSE of the evaluation matrix at the
   arithmetic comb, of the kind T4c measures at ratio 1.0 today. This
   is the exact operator-theoretic statement whose truth would break
   the factor-family: with cost o(M) the pairing can be run LINEARLY
   (Stepanov-style degree count) instead of quadratically
   (Lambda^2/large-sieve), deleting the level-halving 2 and pushing the
   excess from c x/delta toward the budget-limited x^{1/2+eps} that T2c
   shows is affordable.
3. UNIFORMITY: the constants in (1)-(2) independent of lambda on
   x <= lambda^2-windows (BRIDGE-H's clause; the e1n sign-flip data
   already shows the finite family hands over no uniform one-sided
   coordinate for free).
4. LATTICE CLAUSE (mandatory, by Q2/T3 and the DMV kill): the mechanism
   must nameably consume the additive lattice: per-prime Poisson on
   R/(log p)Z is already exact (T4d, #153); what is missing is the GLUE
   across incommensurable circles, whose only known carrier is
   N(x) = x + O(1) / theta-FE. A candidate that runs on nonneg-comb +
   density alone is pre-killed at every exponent below 1. Screen every
   candidate against: the repo fake (`_shared/beurling.py`), the DMV
   system (Math. Ann. 334 (2006), via the surveyor's sourced corollary),
   and D-H (must be unposable).

FORCING QUESTION (the arc's next round): is there ANY subspace family
(not necessarily decimations) of the carrier's trig spaces on which the
log-prime evaluation matrix suffers lambda-uniform rank collapse with
non-degenerate conditioning, sourced by an identity that fails for
perturbed logs? T4c proves decimations are not it and that conditioning
must be watched; the spec says any winner must consume the lattice.

## Q5: disciplines

- **D-H (dh_unposable = TRUE, T5a).** Lambda_DH is dense and
  sign-changing (25 sign changes below n = 60, stream validated in
  e1k/e1n): Step 2's inequality direction does not exist; measured
  exhibit: excess(x=10, delta=2) = -0.288 < 0 (a "majorant" read that
  undershoots). Same clause as the Landau translator: the route is
  Euler-gated at coefficient nonnegativity, and D-H fails it at input
  level. Cheap check as tasked; no finite-lambda D-H discrimination is
  claimed (none exists, #158).
- **Beurling: Q2.** Runs identically = proven system-generic; the
  lattice is the only separator, unconsumed by the present machinery.
- **K1 (k1_clean = TRUE, T5b/c).** Runtime guards on `mp.zetazero` and
  the D-H scanner installed, never tripped; source scan clean (the
  probe's own allocations avoid the scan tokens); per-test input ledger
  printed. NO zero list, zero scan, or zero-location datum is consumed
  anywhere: the zero side of the pairing is discussed analytically in
  this .md but never evaluated in code; all measured bounds are
  comb-side.
- **#146 crosscheck (parity_crosscheck).** The measured sieve constant
  rises to the ceiling 2 (1.677 at x = 1e6), and the parity dossier's
  mechanism explains that ceiling (axiom sign-flip invariance; the
  quadratic pairing's level-halving). The majorant cell constant
  c ~ m+/2 ~ 0.096 is a DIFFERENT, uncertainty-sourced constant. The
  tasking's "factor-2-family" is the sieve/bracket family; the probe
  derives both constants and keeps them distinct rather than forcing
  the match.

## Verdict fields

| field | verdict |
|---|---|
| `skeleton_posed` | YES, exactly (majorant class, pairing with sides marked, extremal implemented and validated), WITH the ill-posedness clause: the full-comb pairing diverges at every type (T2a, growth 6.3x by e^6 x); horizon device required; the carrier's p <= lambda^2 horizon is such a device |
| `measured_constant` | c(delta) = 0.073-0.093 (delta 4-16, x 300-1e5; per-delta medians 0.080/0.087/0.088), stable in x, predicted m+/2 = 0.0957 from B's inside mass; ADVERSARY-CONFIRMED at delta 32/64 (c = 0.089-0.095, tilt law c_tilt(delta) matched <= 2 percent at every delta); certified bound psi <= x(1 + c/delta), error exponent in x = 0.99-1.02 (linear); sieve normalization 1.558/1.626/1.677 at 1e4/1e5/1e6 rising to the parity ceiling 2 (adversary: matches the analytic law 2/(1 + 2E/log x), E = gamma + sum_p log p/(p(p-1)) = 1.3326, to 4 digits at 1e6); budget check: dimension for x^{1/2} affordable (ratio 3.5e-3 at 1e6, adversary-corrected convention): the wall is the unevaluable zero side, not the budget |
| `carrier_delta` | (a) majorant leverage NIL (structural span identity + LP 0.90-1.10 of periodized Selberg); (b) Sonin UNBUILDABLE from cache (honest skip; literature slot also empty); (c) multiplicity ABSENT at log-primes (cost ratio 1.000 across 12 (lambda, K) cells, min sv reported 0.08-0.98) and PRESENT at commensurate combs (0.09-0.50; per-prime circle 0.20): the S4 absence re-measured, lattice clause visible; ADVERSARY (2026-07-11): five further subspace families (half-set transfer, adapted near-commensurate, ground-state modulation, structured sparse frequencies, 50-digit SVD) found NO collapse; the absence is 5-family-hardened, see Adversarial test cases |
| `system_generic_proven` | YES BY EXECUTION (T3: identical code on the Beurling fake, same law, max rel diff 0.14, median 0.10 at x >= 1000) + the surveyor's sourced DMV kill closes the class at every exponent < 1 |
| `s4_spec` | banked (Q4): lambda-uniform rank collapse at the log-prime comb with non-degenerate conditioning, linear pairing replacing quadratic, lattice consumption mandatory; forcing question stated |
| `dh_unposable` | TRUE (25 sign changes below 60; negative excess exhibit -0.288; Euler gate closed at input) |
| `k1_clean` | TRUE (guards never tripped; source scan clean; ledger printed; zero side never evaluated) |
| `parity_crosscheck` | sieve constant -> 2 = parity-explained (#146); majorant cell c ~ m+/2 = uncertainty-explained; kept distinct; the S4-relevant reading: the sieve 2 is the quadratic pairing's level-halving, and cheap multiplicity is exactly what would restore the linear pairing |
| `frontier_delta` | UNMOVED, sharpened at three coordinates: (1) the pairing's ill-posedness forces a horizon = the carrier's own structure (a consonance, not progress on the bound); (2) the budget is NOT the binding constraint on this carrier (dimension is plentiful; the mechanism is what is missing); (3) the multiplicity absence is measured to be exactly incommensurability of {log p}, so the missing glue is the additive lattice, as the DMV/Beurling screen independently demands |

## Tiered claims

**PROVEN (classical mathematics, instantiated here):**
1. B >= sgn, int(B - sgn) = 1, interpolation at negative integers
   (Beurling/Vaaler; polygamma closed form validated to machine
   precision on nodes, T1a/T1b).
2. Selberg interval majorant: S >= chi, excess 1/delta (T1c, 3 percent).
3. The prime side psi(x) <= sum_{n<=Xh} Lambda(n) S(log n) for every
   Xh >= x, GIVEN Lambda >= 0 (pointwise S >= chi >= 0; the Euler gate).
4. The structural nil (a): span{carrier basis at type N} = the full
   degree-N trig space, so no carrier majorant beats the generic
   extremal at fixed type.
5. Confluent-Vandermonde full rank at distinct nodes = full-price
   multiplicity for distinct incommensurable points (the measured 1.000
   is the generic case, not an accident).

**NUMERICAL (measured on this implementation):**
6. The divergence law (T2a: 3.3 -> 28.5 over Xh/x = 1 -> 2981;
   adversary: increments match e (k/(k+1))^2, genuine divergence).
7. The excess law c -> m+/2 (T2b: medians 0.080-0.088 at delta <= 16;
   adversary: 0.089-0.095 at delta 32/64, tilt law matched <= 2 percent,
   limit 0.0957) and the linear error exponent (0.989-1.022).
8. The budget ratio 3.5e-3 at x = 1e6 (T2c, adversary-corrected).
9. The sieve constants 1.558/1.626/1.677 rising toward 2 (T2d).
10. Beurling parity of the law (T3: max rel diff 0.14).
11. LP ratios 0.90-1.10 to periodized Selberg (T4a).
12. Multiplicity table: 1.000 at log-primes everywhere (min sv
    0.08-0.98); 1/J at AP combs; 0.20 per-prime circle (T4c/T4d).
13. D-H negative excess exhibit (T5a).

**STRUCTURAL / CONJECTURE:**
14. The consonance reading (the CCM horizon as the pairing's required
    device) is an observation about shape, not a theorem of equivalence.
15. The Q4 spec and its forcing question (open by construction).

## Named residual

The S4 slot on the CCM carrier is now measured empty in all three
testable directions, with a control showing the mechanism class itself
is alive exactly where combs are commensurable. What survives of the
S4/R1 route is precisely the Q4 spec: a lambda-uniform, well-conditioned
rank collapse at {log p} that consumes the additive lattice. Nothing
here moves M4 or BRIDGE-H; the probe converts "the S4 slot is empty"
from an audit conclusion (#145/#149, surveyor round) into a measured,
carrier-specific, control-calibrated statement with a banked forcing
question.

## Limitations

- The majorant pairing is measured comb-side only; no explicit-formula
  evaluation is implemented (deliberate, K1), so the zero-side claims
  are classical statements cited, not computed.
- The excess-law constant was measured at delta <= 16 and x <= 1e5 in
  the build; the adversary round pushed to delta = 64, x = 1e6 and
  derived the tilt integral: converged (see Adversarial test cases,
  case 1). The residual correction is ~(log delta)/delta scale.
- The sieve implementation is the textbook Selberg main term without
  the remainder bookkeeping; its constants are normalization exhibits
  (rising toward 2), not sharp BT re-derivations.
- T4a's LP enforces one-sidedness on a grid with off-grid re-check and
  margin re-solve (residual violations <= 1.3e-3 before margin); LP
  excesses are therefore lower bounds up to that tolerance, which is
  why the 1.096 ratio at N = 32 (grid resolution effect) is read as
  cell-scale, not as sub-Selberg.
- T4c's rank threshold is 1e-8 relative, with min singular values
  reported (0.08-0.98): no near-threshold cells occurred; a denser
  prime set at much larger lambda (beyond 31) was not tested.
- The Beurling comparison uses the repo's default fake, not a DMV-grade
  construction; the DMV kill is carried by the surveyor's sourced
  corollary, not re-implemented here.
- No Beurling or Sonin OPERATOR build (inherited e1n limitation).

## Handed forward

- **To ADVERSARY**: the sharpest attack surfaces: (i) the m+/2
  identification (is the measured c really the half-inside-cell, or a
  coincidence of the delta range? the tilt correction is derivable and
  checkable); (ii) T4c's honest scope: decimation subspaces only; the
  Q4 forcing question explicitly invites a smarter subspace family, and
  a counterexample subspace with rank collapse at {log p} would be a
  MAJOR positive finding, not a bug; (iii) the consonance reading (2a)
  could be deflated by exhibiting a natural non-carrier horizon device
  that does the same job (it exists: plain truncation; the claim is
  only that the carrier's horizon is one, so attack the "consonance"
  wording if it drifts toward significance).
- **To SURVEYOR (next round)**: the theta <= 1/2 Beurling corner (the
  one unsourced escape hatch in the kill screen) and the
  Carneiro-Littmann well-posedness question in the CCM Sonin space.
- **To BUILDER (next executable)**: the Q4 forcing question, plus the
  Sonin projector build (the one candidate this probe could not test).
- **To SYNTHESIZER**: one line: "e1o posed the S4 skeleton on the CCM
  carrier and measured the slot empty with a control: majorant
  machinery is a system-generic Nyquist-cell tax (ill-posed without the
  carrier's own horizon), the budget is not the wall, multiplicity is
  full price at {log p} and cheap exactly at commensurable combs, so
  the missing S4 mechanism = a lattice-consuming rank collapse, spec
  banked."

## Verification targets (for VERIFIER)

1. **The prime-side inequality**: for Lambda >= 0, S >= chi >= 0
   pointwise implies psi(x) <= sum_{n <= Xh} Lambda(n) S(log n) for all
   Xh >= x. (Trivial; the point is formalizing the Euler gate as the
   hypothesis.)
2. **The divergence**: sum_n Lambda(n) (delta (log n - L))^{-2} = inf
   for the tail n > e^L (comparison with sum Lambda(n)/log^2 n over
   dyadic blocks; classical Chebyshev input only). Formalizes T2a's
   ill-posedness clause.
3. **The structural nil**: span{e^{2 pi i n u/L} : |n| <= N} equals the
   degree-N trig space (definition-level; anchors the (a) claim).
4. **Decimation collapse**: for u_j = u_0 + j L/K, the evaluation
   functionals of V_K = span{e^{2 pi i K m u/L}} at {u_j} all coincide
   (rank 1). The clean Lean-sized kernel of T4c's control.
5. **Full price at incommensurable points**: distinct points on the
   circle give a nonsingular Vandermonde for the full trig space
   (Mathlib has `Matrix.vandermonde` infrastructure; the trig version
   is the target).

## Adversarial test cases (outcomes, adversary round 2026-07-11)

1. **The c-vs-m+/2 stress**: RUN. delta in {4, 8, 16, 32, 64}, x to
   1e6: c rises 0.078 -> 0.093-0.095 and tracks the tilt law
   c_tilt(delta) = (1/2) int (B - 1) e^{-w/delta} dw within ~2 percent
   at every delta (0.0784/0.0850/0.0893/0.0920/0.0935 -> 0.0957 =
   m+/2); frac(delta L)-robust. Identification CONFIRMED (upgraded
   from scale-match to verified law).
2. **A smarter subspace**: RUN, five families, NO collapse found.
   (a) Half-set Stepanov transfer (vanish at half the primes, test the
   rest): rank full, min sv 0.81-0.82 at lam = 6, 8; the same test on
   V_K at an AP comb transfers exactly (max residual 5e-14): the
   transfer mechanism exists and fires only at commensurate combs.
   (b) Adapted near-commensurate decimations (CF convergents of
   log 3/log 2): rank never drops; min sv decays 0.95 -> 6e-3 as the
   approximation sharpens = the pre-registered mirage, and the needed
   budget explodes (2-point case already needs N ~ 3K ~ 2900 >> the
   lam = 3 Shannon 36). 11-point case (lam = 6): best simultaneous h
   at q <= 4000 still misses by 0.23 cells, needs N ~ 1e5 >> Shannon
   144, and stays rank 11/11: the mirage is BUDGET-EXCLUDED at J >= 3.
   (c) Carrier ground-state modulation (cached e1n xi): |xi(log p)|
   shows no systematic vanishing at the primes (one accidental
   near-zero, 0.03x median at p = 7, lam = 3; 7 of 9 valid points at
   0.3x-46x median): no cheapness source. (d) Structured sparse
   frequency sets (primes, squares, Beatty, powers of 2 as
   frequencies): min sv 0.29-0.34, inside the random-subset null
   (median 0.28): no arithmetic resonance. (e) 50-digit SVD: the AP
   collapse is EXACT (sv2/sv1 = 1.2e-14 = input rounding, not a
   threshold artifact) and the log-prime min sv 0.079316 is identical
   at float64 and dps = 50. The Q4 forcing question stays open but is
   now 5-family-hardened.
3. **Commensurate-L trap**: NOT RUN separately; subsumed by T4d (the
   per-prime orbit IS the one-prime commensurate case, ratio 0.20) and
   case 2(b) (collapse tracks approximation to commensurability, not
   primality).
4. **The Beurling eps-sweep**: NOT RUN (secondary; T3 is quoted at
   law level, 35 percent tolerance, and nothing downstream leans on
   the digits).
5. **Horizon-device deflation**: NOT RUN; the .md already claims only
   that the carrier horizon is *a* regularizing device (observation
   tier), which is all the deflation would establish.

## Reproduce

```
python3 -m experiments.spectral.e1o_s4_carrier           # full (~2 s)
python3 -m experiments.spectral.e1o_s4_carrier --quick   # reduced grids
```
Outputs `e1o_s4_carrier.npz` (excess laws, divergence table, sieve
constants, Beurling comparison, LP rows, multiplicity table, D-H
exhibit). `--quick` does NOT write the npz (adversary fix 2026-07-11:
a quick run had silently clobbered the tracked full-run artifact). No
cache is written; e1k/e1n caches are read-only inputs (comb streams
only; no operator rebuild).

