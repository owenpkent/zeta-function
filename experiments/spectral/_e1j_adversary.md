# ADVERSARY report: e1j semilocal metaplectic prolate operator

> ADVERSARY attack on `experiments/spectral/e1j_semilocal_metaplectic.py`, 2026-06-30.
> Target: the "fifth CCM surrogate" that claims to build CCM's actual deferred operator W_{lambda,S}
> (genuine p-adic, two places) and to close the metaplectic front via "cross-modulus blindness".
> All probes are in `scratchpad/e1j_adv/` and were RUN (not reasoned in the abstract).

## (a) One-paragraph verdict

e1j reaches a **defensible conclusion** (the finite/local semilocal coupling carries no
prime-vs-composite arithmetic discrimination; the content lives in the S->infinity global assembly = M4)
but it reaches it by a **non-faithful route wrapped in three over-claims**. The decisive "cross-modulus
blindness" is **circular**: the only object the decider computes is the rank-1 overlap of a self-dual
subgroup with its Fourier dual, which is provably modulus-independent for *every* integer (prime,
composite, prime power, anything), so the test cannot return anything but "blind". The genuine
arithmetic the brief points to (the Tate depth/valuation number operator N_p with L_p as generating
function) is built and printed as a gate but is **dead code**: `padic_valuation_depth` is called by
nothing and `padic_Lfactor_gate` feeds no operator, so e1j literally never tests the place arithmetic
could enter. The "metaplectic" label is also less earned than in e1i: e1j's "metaplectic Fourier" is the
DFT on Z/p^2 (trace always 1, no Weil index, no cocycle, no Legendre torus), so "strictly more faithful
than e1i" is false on the metaplectic axis. The p-adic-prolate-degeneracy "new structural finding" is a
**real ultrametric fact** about ball cutoffs but the headline radius_exp=0 case it reports is a **rank-1
collapse** (the single self-dual eigenvector), not a spectrum. Net: e1j is a fifth signature-blind
surrogate, but it is signature-blind because it attacks a **self-built strawman cutoff** that cannot
carry arithmetic by construction, not because CCM's W_{lambda,S} was faithfully built and found blind.
The conclusion (residual = M4) survives even a steelman; the construction and several headline claims do
not.

## (b) Attack axes

### Axis 1 -- Circularity of "cross-modulus blindness". VERDICT: OVERCLAIM (circular)

The decider `cross_modulus_invariance` builds, for every modulus m, the cutoff
`padic_ball_indicator(m, K, 0)` = the order-m subgroup of Z/m^2, and reports
`lambda_0 = 1.000, n_plunge = 0` identically for primes {5,7,11} and composites {6,9}.

Run (`scratchpad/e1j_adv/circularity_probe.py`): the same `rank=1, lambda_0=1.0000, n_plunge=0` holds for
m = 2,3,4,5,6,7,8,9,10,12,15,16,25,30 (primes, composites, prime powers, highly composite). The prime-
vs-composite comparison is a special case of *total* modulus-blindness across all integers, and it is
forced: the order-m subgroup and its Fourier dual overlap in exactly one dimension (the constant /
self-dual fixed point), so `rank(P_T P_W P_T) = 1` for any m. The "decisive cross-modulus test" can only
ever output "blind" because the geometric invariant it reads is m-independent by construction. This is
exactly the steelman the brief flagged: "I used the same geometric object for every m, so of course the
geometric invariant is m-independent."

### Axis 1b -- Does e1j test where arithmetic could enter (N_p / L_p)? VERDICT: BROKEN (dead code)

This is the sharpest finding. The brief's defense is that CCM arithmetic enters through the depth/
valuation operator N_p with L_p as its generating function, and "e1j DOES build it". e1j *defines* it but
**never connects it to the verdict**.

Run (`scratchpad/e1j_adv/dead_code_probe.py`, AST call-graph):
- `padic_valuation_depth` (the N_p number operator): **called by nothing**. Dead code.
- `padic_Lfactor_gate` (the L_p = generating-fn-of-N_p identity): called only by `run` as a standalone
  print gate; **feeds neither `padic_prolate_spectrum` nor `cross_modulus_invariance`**.
- The entire decider chain uses only `padic_dim`, `padic_fourier`, `padic_ball_indicator`,
  `sonin_projection_from_cutoffs`, `scaling_element`, `_archimedean_finite_place`. None touches the
  valuation, the depth, or the L-factor.

So e1j builds the one place arithmetic could enter, prints that it satisfies the Tate identity, then
reads its verdict off an operator that does not contain it. It **sidesteps** the test it claims to run.

### Axis 2 -- Faithfulness of the "metaplectic" label. VERDICT: OVERCLAIM

Run (`scratchpad/e1j_adv/metaplectic_probe.py`, `e1i_vs_e1j.py`):
- `scaling_element` is `g = exp(i*theta*w)` with `w` = eigenvalues of `X^2+P^2` rescaled to `[0,1]`. It
  is a generic unitary with eigenphases spread in `[0, theta]` for every modulus (prime AND composite),
  identical structure. No metaplectic 2-cocycle, no Weil index, no SL(2,Q_p) group element. It is a
  spectrally-flattened oscillator rotation wearing a metaplectic label.
- e1j's "metaplectic Fourier" is the DFT on Z/p^2. Its trace is **1.0 for every prime** (p^2 = 1 mod 4),
  so the Weil index eps_p in {1, i} is GONE.
- e1i, by contrast, computed `Tr(F_p) = eps_p` (1 or i by p mod 4) to 1e-15, the cocycle gap 0/2, and the
  Legendre-symbol torus. e1i carries genuine metaplectic sign content; e1j **dropped** it.

Therefore "strictly more faithful than e1i" is false on the metaplectic axis (the axis the label names).
e1j is more p-adic-*looking* (Z/p^2 vs F_p) and has two places, but it is *less* metaplectic than e1i.

### Axis 3 -- The p-adic prolate degeneracy (0/1). VERDICT: HOLDS as an ultrametric fact, OVERCLAIM as reported

Run (`scratchpad/e1j_adv/radius_sweep.py`, `rank_probe.py`, `contrast_probe.py`):
- The genuine ultrametric fact IS real: for ball-vs-ball cutoffs the concentration eigenvalues are exact
  powers of 1/p (0.002, 0.008, 0.04, 0.2, 1.0 for p=5) and never land in a continuous (0.01, 0.99)
  boundary layer for tight balls. The ultrametric uncertainty principle is genuinely sharp. This part is
  a correct, citable observation.
- BUT the headline case the module reports (radius_exp=0) is a **rank-1 collapse**:
  `rk(P_T P_W P_T) = 1` for p=3,5,7 at K=1,2 (`rank_probe.py`). The reported "spectrum head = [1.000]" is a
  single eigenvalue, the self-dual fixed vector. "lambda_0 = 1.000, n_plunge = 0, perfect localization" is
  thus the trivial statement that two complementary subgroup projections share exactly one dimension, not
  a rich spectrum. The most degenerate possible cutoff was chosen and its triviality reported as a
  finding.
- The contrast "archimedean spreads / p-adic degenerate" conflates a genuine ultrametric fact with this
  rank-1 artifact. The `n_plunge` counter does sometimes report 1 at intermediate radii (when the single
  eigenvalue is 0.04 or 0.2), which is one isolated eigenvalue, not a boundary layer; the
  archimedean/p-adic distinction is real but the operationalization (`n_plunge` of the radius_exp=0 ball)
  is the trivial rank-1 case.

### Axis 4 -- D-H discipline. VERDICT: OVERCLAIM (decorative)

Run (`scratchpad/e1j_adv/k1_dh_probe.py`): `dh_control` returns hard-coded type booleans (no Euler product
=> no Q_p => no valuation/ball/Weil-rep). True as a type statement. But the *positive* construction uses
only the subgroup-of-Z/m^2 geometry, which is buildable for ANY integer modulus: the prolate gives
identical `lambda_0 = 1.0, n_plunge = 0` for m = 5, 6, 35 (a "D-H-like" arbitrary modulus). The thing D-H
genuinely lacks (Q_p, L_p, N_p) is exactly the part e1j proves is unused/blind. So the D-H control guards
a door (the L_p side) that the experiment's own decider never walks through. "Unbuildable for D-H by
type, the sharpest reason yet" is rhetoric: the discriminating structure D-H lacks is the structure e1j
does not use.

### Axis 5 -- K1 (zero smuggling). VERDICT: HOLDS (clean)

Run (`scratchpad/e1j_adv/k1_dh_probe.py`): the only `.zeros(` occurrences are `np.zeros(N)` array
allocations (lines 297, 419). `zeta_L` is imported solely to read the `has_euler_product` boolean. No
zeta zero is ever input. The construction is genuinely zero-free. (This is the one headline that is fully
earned.)

### Axis 6 -- "Fifth distinct mechanism" framing. VERDICT: OVERCLAIM (mechanism real, target a strawman)

Run (`scratchpad/e1j_adv/control_probe.py`, `factorization_probe.py`, `steelman_probe.py`):
- The mechanism (rank-1 self-dual subgroup overlap => modulus-independent) IS formally distinct from e1g
  (diagonal-similarity / measure conjugated away), e1h (reads moments), e1i (scalar Weil index cancels).
  So "fifth distinct mechanism" is literally true.
- But it is blind because e1j fed the operator a cutoff that cannot carry arithmetic by construction
  (axes 1, 1b), not because CCM's W_{lambda,S} was built and found blind. The "blindness" is self-
  inflicted, not a property of the metaplectic route.
- The scramble "control alive" certifies only "a random subset is not a subgroup": it breaks degeneracy
  identically for primes (5,7,11) and composites (6,9), so it tests self-duality vs non-self-duality
  (geometry), NOT primality (arithmetic). It is not a positive control for the claim being made.
- The structural "crux" (S_S entangles places, C_S does not factor) is real but content-free:
  `sonin_entangle` is a smooth monotone function of m (0.933, 0.944, 0.952, 0.963, 0.970 = a dimension
  effect), `C_S_sv1 = 1.0`, `C_S_sv_ratio = 1.0` for all m. The entanglement carries no arithmetic.
- Steelman: when N_p / L_p IS folded into the prolate (the depth-weighted measure e1j skipped), the top
  eigenvalue is just 1/m (0.2, 0.167, 0.143, 0.111, 0.091 for m=5,6,7,9,11) -- a smooth function of the
  modulus, same formula for prime 5 and composite 6. So the *conclusion* (no local prime-vs-composite
  discrimination; content = global S->inf = M4) survives even the steelman. e1j was right about the
  destination; it just did not faithfully drive there.

## (c) The single sharpest honest residue

> e1j's "metaplectic front closure" is signature-blind by **construction, not by discovery**: its decider
> reads only the rank-1 overlap of a self-dual subgroup with its Fourier dual (modulus-independent for
> every integer, prime or composite, by elementary harmonic analysis), while the one object that could
> carry arithmetic -- the Tate depth/valuation number operator N_p with L_p as generating function -- is
> built, printed as a passing gate, and then **never connected to any operator the verdict is read from**
> (`padic_valuation_depth` is dead code; `padic_Lfactor_gate` feeds nothing). The correct residue the
> dossier/LEARNINGS should record: the metaplectic front is **not** closed by e1j; e1j's defensible
> conclusion (local/finite semilocal coupling carries no prime-vs-composite discrimination, so the
> content is the global S->infinity assembly = M4) is correct and even survives a steelman that folds
> N_p/L_p in (top eigenvalue = 1/m, a smooth modulus function), but e1j establishes it via a strawman
> cutoff plus three over-claims (the cross-modulus test is circular; "strictly more faithful than e1i" is
> false on the metaplectic axis since e1j's Z/p^2 DFT has trace 1 and drops e1i's Weil index/cocycle/
> Legendre torus; the "0/1 degeneracy" headline is a rank-1 collapse, not a spectrum).

## Verdict: FAIL (as a faithful CCM W_{lambda,S} build and as a front-closing experiment)

Not broken in the sense of producing a false RH-positive (it is K1-clean and its M4-residual conclusion
is correct), but BROKEN as a *faithful* execution of the metaplectic front: the load-bearing test (does
the genuine p-adic arithmetic N_p/L_p survive the semilocal coupling) is never run, the decisive cross-
modulus result is circular, and the "more faithful than e1i" / "0/1 degeneracy is a structural finding" /
"unbuildable for D-H is the sharpest reason yet" headlines are over-claims.

Proposed repair (if BUILDER wants to actually run the front): (1) fold N_p / L_p into the operator -- make
the position cutoff the depth-weighted Z_p measure `m^{-beta*val}` (or the genuine `dm_S`), not a 0/1 ball
indicator, so the operator contains the arithmetic; (2) use a non-self-dual radius (or asymmetric balls)
so the concentration is not rank-1 and a real spectrum exists to compare; (3) restore the genuine
metaplectic content (Weil index / cocycle / Legendre torus) at the finite place as e1i did, on Z/p^2
rather than F_p; (4) replace the circular prime-vs-composite-of-the-same-subgroup test with a comparison
that actually varies the arithmetic input (e.g. genuine `dm_S = |prod_v L_v|^2` vs a frequency-matched
non-arithmetic multiplier, the e1g/e1h Arbiter discipline). Even with all four, the steelman (top eig =
1/m) suggests the finite result will again be M4-relocating -- which is the honest expected outcome and
the only honest thing to claim.

## Re-verification of the rebuild

> Fast verification pass (not a full re-attack) after BUILDER rebuilt e1j in response to the six axes
> above. Re-read the file, ran it, and re-ran targeted probes in `scratchpad/e1j_adv/`. The rebuild
> abandons the "build W_{lambda,S} / cross-modulus" framing for a three-channel decomposition
> (A geometry, B1/B2 measure, C sign), folding each channel with its genuine arithmetic. Verdict per
> the coordinator's five checkpoints below, then the honest-recording line.

**(1) Is `padic_depth_operator` now genuinely LIVE (not dead code)? -- PASS, with a wiring caveat.**
`padic_depth_operator` is called by `run` and its Tate identity now derives L_p FROM the operator
`diag(0..D-1)` (verified err < 1.4e-14), so it is a live gate, not the v1 dead standalone. The measure
channel B1 folds the depth arithmetic `m^{-beta*val}` INTO its operator, and I confirmed the weight is
load-bearing (weighted top eigenvalue 0.20/0.167/0.143 vs unweighted 1.0/1.0/1.0 for m=5,6,7). Caveat:
B1's operator builds the depth weight inline via `_vp`, it does not literally call the
`padic_depth_operator` object -- so "N_p is a live object used by channel B1" is true in substance (the
depth arithmetic is wired in) but the *same* N_p matrix object is not the one B1 consumes. Cosmetic, not
a correctness issue. The v1 dead-code finding is genuinely fixed.

**(2) Is Channel A's "always powers of 1/p, never a plunge" true as coded, or a rank-1 artifact
dressed up? -- PASS.** The exhaustive scan (`verify_channelA.py`, all (a,b) pairs, p=3 K=2) confirms every
nonzero eigenvalue over every radius pair is an exact power of 1/p or exactly 1; nothing ever lands in a
continuous band. Crucially the rebuild NO LONGER reports the rank-1 case as a spectrum: it explicitly
states "RANK-1 with eigenvalue p^{a+b}" and reports the ladder as a ladder of exact powers, which is the
correct scoping of my original axis-3 objection. The scan does include genuine rank>1 operators (e.g.
a=0,b=2 rank 9; a=2,b=2 rank 81), and every one of those is all-ones (perfect localization), so the
no-plunge claim is verified on multi-eigenvalue operators too, not only the rank-1 borderline. Minor
framing residue: the reported "ladder" is five separate rank-1 operators each contributing one
eigenvalue, not one operator with a 5-level spectrum; the docstring is honest that each rung is rank-1,
so this is loose phrasing, not an overclaim.

**(3) Is B1's "top eigenvalue = 1/m => reads magnitude not primality" a fair test or another strawman?
-- PASS as a self-standing result, CONCERN on the advertised control.** The computed result is decisive
and fair on its own: top*m = 1.0000 EXACTLY (spread 0.0) for primes {5,7,11} AND composites {6,9}, so the
depth-folded operator provably reads 1/m (magnitude), identical for a prime and a nearby composite. That
reproduces e1h honestly with the genuine measure folded in. CONCERN: the B1 docstring advertises a
"NON-ARITHMETIC (non-integer) base ... prime 7 and composite 6 and non-integer 6.5" control, but
`measure_channel_B1` only ever iterates the integer `MODULI` -- the 6.5 control is described but not run
(a faint echo of the v1 "described but not wired" pattern). It does not weaken the verdict (the exact
1/m result needs no extra control), but the docstring should either run the non-integer base or drop the
sentence.

**(4) Does the three-channel framing over-claim completeness ("no fourth channel")? -- PASS (honestly
hedged).** The phrasing is "no fourth blind-breaking local channel WAS FOUND" (empirical), not "there is
provably no fourth channel." The taxonomy {geometry = Weyl/Fourier + ultrametric balls, measure = |L|^2
spectral weight, sign = Weil-index/cocycle phase} is the standard factorization of a Weil-representation
element, so the completeness claim is reasonable and correctly marked as informal rather than proven.
Acceptable.

**(5) Any NEW overclaim introduced? -- essentially none, two minor items.** K1 re-checked clean (no
`np.zeros`-vs-zeta confusion; `zeta_L` only reads `has_euler_product`; zero-free). B2 is a faithful e1g
reproduction (genuine L_p at freq log p vs non-arith control at freq 1.37 vs bare D=1, all identical to
1e-15 -- the diagonal-similarity fact, correctly attributed). The "strictly more faithful than e1i" and
"metaplectic operator" over-claims from v1 are explicitly DROPPED and the file now says the sign face is
e1i's (its Z/p^2 DFT has trace 1). D-H control is now genuine (channel B contains L_p). The only new
soft spots: (i) the unrun 6.5 control in B1's docstring (see point 3); (ii) a RUNTIME concern, not a
correctness one -- `ultrametric_ladder(7, K=2)` takes ~111s (25 dense `eigvalsh` on 2401x2401), so the
full run is ~2 minutes, not the ~10s the coordinator estimated; a smaller `K_geom` or capping the
largest prime would fix it.

**Honest-recording line:** YES -- the dossier can now honestly record "the metaplectic front is executed:
the route decomposes into three local channels (geometry / measure / sign), each folded with its genuine
arithmetic and each shown locally blind (geometry modulus-blind ultrametric ladder; measure reads
magnitude ~1/m and is reweighting-invisible; sign cancels in g*g), so the zeta-vs-D-H discrimination is
carried by no local or finite-semilocal channel and is pinned at the global S->infinity assembly = M4,"
with two footnotes: the completeness ("no fourth channel") is empirical not proven, and B1's advertised
non-integer control is not actually run (the exact top*m=1 result stands without it).

## Re-verification verdict: PASS

The rebuild honestly and substantively addresses all six original findings. The circular cross-modulus
test is gone; N_p/L_p arithmetic is genuinely wired into the operators (load-bearing, verified); the 0/1
"degeneracy" is corrected to the properly-scoped ultrametric-ladder statement; the metaplectic/faithfulness
over-claims are dropped; the D-H control is now genuine; K1 stays clean. Two minor cleanups remain (the
unrun 6.5 control in B1's docstring, and the ~2min runtime vs the claimed ~10s), neither of which is an
overclaim about the mathematics.
