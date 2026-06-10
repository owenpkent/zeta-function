# Local-compute workarounds (2026-06-09): routing around the walls instead of hitting them

> A follow-on to the session-019 conjecture program
> ([`first_principles_conjecture_program.md`](first_principles_conjecture_program.md), LEARNINGS #76)
> and the EDF discriminator result (#77). Eight locally runnable experiment ideas
> (Python: mpmath / numpy / sympy / cvxpy on existing repo blocks), each designed as a
> WORKAROUND: it routes around a named wall rather than re-fighting it. Per the
> soft-detector freeze ([`soft_detector_wall.md`](soft_detector_wall.md)), every idea
> below is a falsification instrument or a producer of exact proof objects, never a
> certified-margin claim from floats.

## The four workaround axes

The project's no-go results dictate the shape of anything new:

1. **Exact arithmetic over truncations.** The $e^{-4\pi x}$ wall (#52) makes float
   margins meaningless, but it says nothing about EXACT rational/algebraic certificates
   for finite truncations. A rational LP dual or a rational PSD factorization is a
   kernel-checkable finite lemma, not a soft detector. Workaround: make the numerics
   output proof objects instead of margins.
2. **Substrate shift to the function-field wind tunnel.** Over $\mathbb{F}_q$ the answer
   is known (RH is a theorem) and every object is finite and exact. Test the named open
   lemma THERE first; extract the mechanism if it holds, kill the lemma cheaply if it
   fails even where RH is true.
3. **Integer invariants instead of real margins.** Inertia triples, negative-eigenvalue
   counts, jump locations. An integer cannot be marginally true (the session-019
   pattern), and the freeze does not apply to counting.
4. **Mine certificates, not values.** #45 (e3o) proved value-side PSLQ is K2-blind: the
   reachable closed forms are the archimedean half D-H shares. But DUAL VECTORS and
   certificates are K2-loaded by construction (they encode the prime side). Run the
   integer-relation machinery on the proof objects the LPs emit.

The named single target is unchanged: the **composite-pinching lemma** (a fully
saturated point of the Weil cone has no mass off the prime powers), shared by LCC and
EFR. Ideas 1-3 attack it from three sides; 4-5 build the EDC ladder; 6-7 extend EDF;
8 is the cross-cutting miner. The two already-queued session-019 tests (LCC LP triple
`e3x_lonely_crystal_lp.py`, ECC leakage `e1x_euler_crystal.py`) are not duplicated
here, but idea 5's interval rider folds into e1x when it runs.

---

## 1. Function-field wind tunnel for composite pinching (top pick)  [RAN 2026-06-09, PINCHING CONFIRMED, LEARNINGS #79]

**File**: `experiments/arithmetic_geometric/e2ll_ff_crystal_cone.py`
**Wall routed around**: "the answer is unknown" (axis 2).

> **Result.** Composite pinching HOLDS on all 7 curves (elliptic + genus-2 over
> q in {5,7,11,13}). RH = PSD Frobenius-moment Toeplitz (`|alpha|=sqrt q` to 0);
> the closed-point counts `a_d` invert exactly to nonnegative integers (Mobius);
> Prony recovers exactly the `rank(R)` distinct Frobenius angles and the rank
> stabilizes (flat extension) => the representing measure is UNIQUE = pinched. The
> supersingular `y^2=x^5+x+1/F_5` (`rank 2 < 2g=4`) is a strengthening witness.
> Anti-curve control fires (off-line modulus => non-PSD). MECHANISM: the FF
> pinching IS flat-extension uniqueness of the truncated trig moment problem
> (Curto-Fialkow); the transfer gap to zeta is the DISCRETE (2g atoms) -> the
> pole-sourced CONTINUOUS archimedean spectrum (outside Curto-Fialkow /
> Olevskii-Ulanovskii / BRS) = LCC's named open core. No ghost comb over F_q, so
> the cheapest kill of LCC/EFR is ruled out; a clean positive coordinate.

Build the crystal-cone problem over $\mathbb{F}_q$, where RH is a theorem and the
explicit formula is a finite exact identity. For a curve $C/\mathbb{F}_q$ (reuse the
e2f/e3x point-count machinery: elliptic and genus-2 over small $q$), the von Mangoldt
analogue is supported on $\{k \log q\}$ with coefficient
$a_k = \sum_{d \mid k} d \cdot \#\{\text{closed points of degree } d\} \cdot q^{-k/2}$:
the divisor sum $d \mid k$ is the EXACT function-field analogue of zeta's composite
structure. Pose LCC clause (i) there: among nonnegative combs $(c_k)$ feasible for the
FF explicit-formula source (paired against the finite Fejer family on the circle),
is the saturated point UNIQUE and equal to $(a_k)$? This is finite-dimensional exact
linear algebra (sympy over $\mathbb{Q}[\sqrt{q}]$ or integer point counts), so the
face structure of the truncated cone is enumerable EXACTLY, no floats anywhere.

**Readout and kills.** If ghost combs exist even over $\mathbb{F}_q$ (where RH holds),
LCC/EFR rigidity as stated is DEAD and years are saved: that is a clean negative
coordinate. If rigidity holds, extract the exact dual certificates that pin each
divisor-sum node and read off the MECHANISM (which test functions pin which nodes,
and what role the $d \mid k$ structure plays); the mechanism is the portable object,
the thing to translate back to $\operatorname{Spec}(\mathbb{Z})$.

**Cost**: an afternoon; everything is exact and small. **Freeze-compliant**: no
floats, no margins, theorem-world control.

## 2. Exact rational dual certificate for $c_6$ pinching

**File**: `experiments/positivity/e3bb_pinching_dual_exact.py`
**Wall routed around**: float64 / soft-detector freeze (axis 1).

The zeta-side composite-pinching attack, run so that its output is a proof object.
Truncate the crystal feasibility problem (nodes $\log n$, $n \le N$ for small $N$;
constraints = explicit-formula pairings against a FINITE Fejer/Hann family with
RATIONALIZED coefficients; prime data only, no zeros, K1-clean). Solve
$\max c_6$ by exact-arithmetic simplex (hand-rolled over `fractions.Fraction`, or
float LP first then exact rational verification of the candidate optimal basis).
If $\max c_6 = 0$ exactly, the optimal dual vector IS a finite proof of truncated
pinching at level $N$. Store the exact duals for $N = 8, 12, 16, \dots$.

**Readout and kills.** A persistent exact $c_6 > 0$ floor under refinement kills LCC
clause (i) (same kill as the queued e3x test (b), but in exact arithmetic the verdict
is not arguable). Exact duals across $N$ feed idea 8 (certificate mining) and idea 9
(Lean export). **Cost**: small LPs, dimensions $\le 30$; a day including the exact
simplex. **Freeze-compliant**: output is a rational certificate, not a margin.

## 3. Ghost-crystal adversarial search

**File**: `experiments/positivity/e3cc_ghost_crystal.py`
**Wall routed around**: confirmation bias (run the KILL on purpose).

The mirror of idea 2: actively try to construct the second feasible crystal that
kills LCC. Feasibility LP with $c_6 \ge \delta$ forced, maximize $\delta$ under
refinement of the test family; also try multi-node ghosts ($c_6, c_{10}, c_{12}$
jointly free) and ghosts with perturbed prime-power mass ($c_4 = \Lambda(4)/2 \pm
\epsilon$). Track $\delta^*(N)$ as the test family refines.

**Readout.** $\delta^*(N) \to \delta_\infty > 0$: ghost exists, LCC dead, large
negative coordinate. $\delta^*(N) \to 0$ with a clean rate: the rate IS the
quantitative pinching strength, and the active constraint set at the optimum names
which test functions do the pinching (input to idea 2's certificate). D-H control:
the same search under the D-H source must be INFEASIBLE outright (the provable
firewall); if it is feasible the whole lens falls. **Cost**: same infra as idea 2.

## 4. The EDC Haynsworth octave ladder  [RAN 2026-06-09, EDC SURVIVED, LEARNINGS #78]

**File**: `experiments/positivity/e3dd_edc_octave_ladder.py`
**Wall routed around**: real margins (axis 3: integers only).

> **Result.** Clause (i) CONFIRMED (every octave Schur complement PSD for zeta and
> chi_3 on the non-circular input-side form, and zeta to 7 octaves on the zero
> side; Haynsworth identity exact at every octave, `cond <= ~90`). Clause (ii):
> NO octave-graded wall: zero-side zeta margins stay flat in `[0.014, 0.039]`
> across support `b in [1.5, 2.8e9]`, ~1e117 above the `e^{-4 pi a}` wall, and the
> global marginality (`+0.007`/`+0.023`) is the telescoped accumulation of healthy
> per-octave margins, exactly EDC's predicted picture. Caveats: the zero-side
> flatness is near-tautological under RH; the input side (the side that matters)
> caps at `n_oct = 5` by the `e^{2L}` ceiling so its clause (ii) is 4 points
> (that ceiling IS the feasibility wall, and the margin lower bound past it is an
> ANALYTIC question); and the off-line break did NOT appear at `m = 3`/octave
> (a resolution limit, 3D.3 needed `K = 100-1000`). EDC stays a live PURSUE
> direction. Next: a dense (`m >> 3`) zero-side run for the break, and idea 1.

First test of Eratosthenes Descent, which nothing has touched yet. Build the nested
Weil Grams $G_k$ on support octaves $[\,0, a_k]$, $a_k = 2^k a_0$ (reuse
`arch_block_bombieri` + `finite_block` + `pole_block` exactly as e3aa does), form the
octave Schur complements $S_k$, and verify the EXACT Haynsworth identity
$\operatorname{In}(G_{k+1}) = \operatorname{In}(G_k) + \operatorname{In}(S_k)$
numerically as a consistency gate. Report the INERTIA TRIPLE of each $S_k$ (integers)
for zeta, $\chi_3$, D-H, Epstein non-principal.

**Readout and kills.** EDC clause (i) predicts every zeta $S_k$ is PSD: any robustly
indefinite octave kills clause (i) in one run. For D-H the chain must BREAK at some
octave $k^*$ (the off-line resonance entering the window); the value and stability of
$k^*$ is the integer-valued discriminator, the octave-graded refinement of 3J's
`schur_neg = #off-line heights` law. **The decisive sub-test is clause (ii)**: fit
$\log |\lambda_{\min}(S_k)|$ against both $k$ (exponential in LEVEL, certificate
survives) and $a_k = 2^k a_0$ (exponential in SUPPORT $=$ the #52 wall in octave
clothing, certificate VOID). One regression separates "new structure" from "wall
restatement"; that distinction is exactly what EDC's viability hangs on. **Cost**:
the blocks exist; an afternoon at $K = 16$, $k \le 5$. **Freeze-compliance**:
inertia integers and a decay-RATE comparison, no certified margin claimed.

## 5. Interval-arithmetic rider for ECC clause E1

**Fold into**: the queued `experiments/spectral/e1x_euler_crystal.py`.
**Wall routed around**: "numerics prove nothing" (axis 1, rigorous finite theorems).

When e1x runs, certify $J$-contractivity of the truncated Blaschke-Potapov products
with `mpmath.iv` (interval arithmetic) for the first $N$ primes. A verified interval
enclosure of $\|\cdot\|_J \le 1$ for $N = 10^3$ factors is a machine-checked FINITE
THEOREM (clause E1 truncated), not an observation, and it is the induction base a
builder needs. Also settles the adversary's K1 flag by construction: the recursion is
built from the accelerant (prime side) with the spectral measure never touched.
**Cost**: rider on e1x, hours.

## 6. Decimation bifurcation diagram (EDF clauses C+D quantified)

**File**: `experiments/positivity/e3ee_decimation_bifurcation.py`
**Wall routed around**: single-point tests (make the #77 finding a CURVE, not a dot).

e3aa tested one decimation depth ($\theta = 1/2$). Sweep the full $(t, \theta)$
rectangle, $\theta \in [0.3, 1.1]$, and record (a) the integer negative-count
$n_-(t,\theta)$ and (b) the collapse depth. EDF predicts a sharp critical window at
$\theta = 1$ (clause C: the matched line is the positivity boundary, exponent 1);
the bifurcation set $\{(t,\theta) : n_- \text{ jumps}\}$ should be a clean curve
approaching $\theta = 1$ as $t$ grows. On D-H, clause D predicts the off-line
unstable manifold with Lyapunov exponent $2\beta_1 - 1 = 0.617$: test whether D-H's
collapse depth scales as $e^{0.617\, t \cdot(\dots)}$ along the matched line while
zeta's stays flat. A measured exponent near $0.617$ on D-H and $0$ on zeta is the
first quantitative confirmation of clause D; any other exponent kills it.
**Cost**: e3aa already computes single points; the sweep is a loop, one evening of
compute at $K = 16$. **Freeze-compliant**: integer counts, jump locations, and
exponent fits.

## 7. Two-prime exact identity hunt (the EDF exactness lemma, rung one)

**File**: `experiments/positivity/e3ff_two_prime_identity.py`
**Wall routed around**: flow well-posedness being untestable in the abstract.

#77 verified the single-prime angular-mean-one identity to $10^{-16}$ and its closed
form exactly. The flow's missing skeleton (well-posedness, the "exactness lemma")
needs the TWO-prime version: for $(p, q) = (2,3), (2,5), (3,5)$, compute the joint
angular mean of the product symbol
$\big(1 - \tfrac1p\big)\big(1 - \tfrac1q\big)\, R_p R_q$ over both phases at 50
digits, and PSLQ the result against $\{1, \log p, \log q, \zeta(2), \gamma_E, \dots\}$.
Exactly 1 (independence persists): the center-fixed-point identity factorizes and the
EDF linearization is diagonal, a real structural lemma one sympy proof away. Not 1:
the deviation IS the composite cross-term, and its size vs $1/(pq)^{1/2}$ measures
the composite obstruction $P_{\mathrm{comp}}$ (M3/#33) in the EDF basis, tying the
two threads together. Either outcome is a coordinate. **Cost**: hours; pure mpmath
quadrature plus PSLQ.

## 8. Certificate mining: PSLQ on proof objects

**File**: `experiments/_shared/certificate_mining.py`
**Wall routed around**: #45's K2-blindness of value-side PSLQ (axis 4).

Collect every exact dual vector and active-set pattern emitted by ideas 1-3 (and the
queued e3x) across truncation levels, normalize, and run `mpmath.pslq` against the
arithmetic basis $\{1, \log 2, \log 3, \log 5, \gamma_E, \log 2\pi, \zeta(2),
\zeta(3)\}$ plus rational scans. e3o established that VALUES reachable this way are
the shared archimedean half; certificates are different objects: they encode which
prime constraints bind, so a detected closed form is a conjecture for the GENERAL
dual certificate, i.e. for the composite-pinching proof itself. **Cost**: free once
1-3 emit data; the miner is 100 lines.

## 9. Lean export rider: the finite-lemma family

**Pipeline**: python writes `lean/ZetaRH/FiniteCertificates.lean`.

Any exact rational object from ideas 1, 2, 4 (an LP dual proving $\max c_6 = 0$ at
level $N$, a rational $LDL^T$ of an octave $S_k$) exports mechanically as a
`decide`/`norm_num`-checkable Lean lemma over $\mathbb{Q}$. This continues the
AccidentAudit precedent (#49: kernel-checked non-circularity) and builds the indexed
family of machine-checked truncated lemmas that EDC's clause-(iii) induction would
quantify over. The workaround: the gap between "numerics" and "proof" is crossed
per-truncation NOW, leaving only the uniformity step open (which is where the
mathematics actually lives). **Cost**: mechanical templating, cheap per certificate.

---

## Recommended order

1. ~~**e3dd octave ladder** (idea 4)~~ **DONE 2026-06-09 (#78): EDC survived.**
   Clause (i) holds, Haynsworth skeleton exact, no octave-graded wall. The
   decisive input-side clause (ii) is ceiling-limited to 4 octaves (the `e^{2L}`
   prime-sum feasibility wall), so it is suggestive not decisive; the open core is
   now the analytic input-side margin lower bound and a dense-`m` run for the break.
2. ~~**e2ll FF wind tunnel** (idea 1)~~ **DONE 2026-06-09 (#79): pinching confirmed,
   mechanism = flat-extension uniqueness (Curto-Fialkow), gap = discrete->continuous
   spectrum transfer.** No ghost comb over F_q; LCC/EFR's cheapest kill ruled out.
   Follow-on: a moment-problem transfer theorem (discrete -> pole-sourced continuous)
   is now the named mathematical target for LCC/EFR, replacing "find the mechanism".
   **Zeta-side mirror DONE 2026-06-10 (e3gg_zeta_moment_mirror.py, #80):** ran the
   same flat-extension machinery on zeta's zeros and EXHIBITED the fail mode -- zeta's
   zero-measure Toeplitz never goes flat (ghost room persists ~15 orders of magnitude
   above the F_q floor; |c_k| ~ O(1/sqrt N), C->I), so the moments do not pin the comb.
   D-H behaves identically (mechanism, not a detector). The transfer obstruction is now
   concrete and quantitative.
3. **Queued session-019 pair**: e3x LCC LP triple, then e1x ECC with the idea-5
   interval rider.
4. **e3bb + e3cc exact dual / ghost pair** (ideas 2-3): the zeta-side pinching
   attack, feeding the miners.
5. **e3ee + e3ff EDF riders** (ideas 6-7): quantify the #77 win, hunt the
   exactness lemma.
6. **Miners 8-9** run continuously as the above emit certificates.

## Honest scope

Nothing here attacks AX-POL frontally, claims a certified margin, or proposes a new
soft detector. Each idea either (a) produces an exact finite proof object, (b) tests
a named falsifiable clause of a PURSUE conjecture with a stated kill, or (c) moves
the question to a substrate where the answer is known. The composite-pinching lemma
remains the single named target; ideas 1, 2, 3, 8 are four independent approaches to
it, and a clean kill of it (a ghost crystal in the FF wind tunnel or an exact
persistent $c_6$ floor) would retire LCC and EFR together, which is exactly the kind
of coordinate the program runs on.

Cross-refs: #76/#77 (the conjecture program and the EDF result), #52/#56 (the wall
axes 1 and 3 route around), #45 (the K2-blindness axis 4 routes around), #49 (the
Lean finite-certificate precedent), #54/e3x-FF (the function-field polarization
machinery idea 1 reuses), 3J/#19 (the inertia-counting law idea 4 refines).
