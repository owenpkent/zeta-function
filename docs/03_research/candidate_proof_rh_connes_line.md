# The Connes eta_x Candidate Proof of the Riemann Hypothesis (with one identified gap)

> Candidate proof of RH along the Connes eta_x line (arXiv:2602.04022), assembled 2026-06-03 by the
> BUILDER/ADVERSARY/SYNTHESIZER loop. Status: a complete chain with ONE identified, RH-equivalent gap
> (Lemma C); four committed proofs of that gap, each broken under the Davenport-Heilbronn discipline.
> This is a BUILDER artifact and the autopsy is the payload. It does NOT prove RH. Companion to
> [connes_2602_letter_to_riemann.md](connes_2602_letter_to_riemann.md), the assessment of the paper,
> and to experiments e3s/e3t. See [researcher_mindset.md](researcher_mindset.md): a failed proof is a
> coordinate.


## 0. Preamble (honest status)

This is a BUILDER artifact, not a claimed theorem. It assembles the Connes / Connes-van Suijlekom eta_x line (arXiv:2602.04022, "Letter to Riemann") into a single complete chain whose every link is proven EXCEPT one: a Convergence/Positivity lemma we call Lemma C. The scaffolding below (Setup, Lemma A, Lemma B, and the reduction Theorem) is genuinely proven and is reproduced cleanly. Lemma C is the gap; it is RH-equivalent. We then write out in full the strongest single candidate proof of Lemma C the program has produced (the monotonicity / no-first-failure strategy), commit to it as written, and follow it with a complete autopsy of that proof and three sibling attempts. The verdict in every case is fatal and the failure is the same one each time: the discriminating step is either circular (it assumes its conclusion) or zeta-blind (it works verbatim for the Davenport-Heilbronn L-function, which is RH-FALSE). The document ends with the precise specification a correct proof must meet. Nothing here proves or disproves RH. It maps, to the millimeter, where a proof on this line must live.

---

## 1. The proven scaffolding

### Setup (PROVEN)

For x > 1 let lambda = sqrt(x) and Lambda = (1/2) log x. Pass from the multiplicative line R*_+ to the additive line by t = log u, so even test functions g supported in [lambda^-1, lambda] become even functions supported in the symmetric interval I_Lambda = [-Lambda, Lambda].

Define QW_lambda, the Weil quadratic form: the Guinand-Weil explicit-formula functional applied to g * g^*, restricted to even g supported in I_Lambda, with the constraint ghat(+- i/2) = 0 (which kills the pole). In the additive coordinate it splits as

    QW_lambda(g) = A_arch(g) - P_lambda(g),
    A_arch(g)   = (1/2 pi) integral |ghat(t)|^2 Omega(t) dt,   Omega(t) = 2 log Q + Re psi(1/4 + i t/2) - log pi,
    P_lambda(g) = 2 sum_{n <= x} Lambda_vM(n) n^{-1/2} (g * g^*)(log n),

with Lambda_vM the von Mangoldt function and psi the digamma function. A_arch is the archimedean block (the place at infinity, the Gamma factor); it carries NO primes. P_lambda is the Euler / prime block; it is the only place the multiplicative structure of zeta enters.

QW_lambda is represented by a lower-bounded self-adjoint operator A_lambda with compact resolvent on the admissible even, pole-killed space V_Lambda = { g : supp g subset I_Lambda, g even, ghat(+- i/2) = 0 }. Write eps(x) for its minimal eigenvalue and eta_x for the corresponding minimal eigenvector ("the true minimizer"). All of this is proven (Connes-van Suijlekom; instrumented in experiments e3s, e3t).

### Lemma A (Connes-van Suijlekom, Theorem 6.1, PROVEN)

If A_lambda's minimal eigenvalue eps(x) is simple, isolated, with EVEN eigenvector eta_x, then the entire function eta_x-hat(z) has ALL its zeros on the real line.

Proof sketch. The minimal eigenvector of a marginally positive-semidefinite Toeplitz form has all its associated-polynomial roots on the unit circle (Caratheodory-Fejer / Schur). Transported to the Fourier side via the exponential coordinate, "roots on the circle" becomes "zeros on the real axis." Hurwitz stability under the eigenproblem preserves this. (Instrumented in e3s: the minimal eigenvector recovers the first 8 zeta zeros to ~1e-2, with 117/119 polynomial roots on the circle; the exact Caratheodory-Fejer realization gives 1.000.)

CAUTION recorded here, used in the autopsy. Lemma A is INPUT-AGNOSTIC. The same construction forces all-real-zeros for a D-H-derived symbol and even for a pseudo-random symbol (LEARNINGS #50). It is a property of the construction, not of zeta.

### Lemma B (Connes, Fact 6.4, PROVEN)

Let h_lambda = h_{4,lambda} - (I_4/I_0) h_{0,lambda} be the unique even vanishing-integral combination of the localized prolate spheroidal wave functions on I_Lambda (eigenfunctions of the prolate / Heun operator PW_lambda descending from the Hermite / harmonic-oscillator family; built from ARCHIMEDEAN data, NO primes). Let E be Connes' summation map E(f)(u) = sqrt(u) sum_{n>=1} f(nu), and set k_lambda = E(h_lambda), the prolate ansatz. Then

    k_lambda-hat -> Xi   uniformly on closed substrips of |Im z| < 1/2,

with explicit rate, where Xi is Riemann's Xi function.

Proof sketch. The prolate construction reproduces the archimedean side of the explicit formula exactly; the summation map E folds it onto the completed zeta. (Instrumented in e3t: k_lambda recovers the first zeta zero to 14.133-14.135.)

CAUTION recorded here, used in the autopsy. k_lambda is archimedean-only. It references no Dirichlet coefficient, no Euler factor. The SAME k_lambda is the prolate ansatz for D-H; the construction code is byte-for-byte identical (LEARNINGS #50; verified in the autopsy of attempt 3).

### Theorem (RH, modulo Lemma C)

By Lemma A each eta_x-hat has only real zeros. If eta_x-hat -> Xi uniformly on compacts (Lemma C), then by Hurwitz Xi has only real zeros. Xi's zeros are exactly the nontrivial zeros of zeta mapped to the critical line, so RH holds. QED modulo Lemma C.

---

## 2. The gap: Lemma C, stated precisely

### LEMMA C (Convergence / Positivity Lemma, UNPROVEN)

As x -> infinity, eta_x-hat -> Xi uniformly on compact subsets of C.

Three equivalent formulations (Connes sec 6.4 / 6.6):

- (C1, convergence) eta_x-hat -> Xi uniformly on compacts.
- (C2, minimizer = ansatz) The true minimizer is asymptotic to the prolate ansatz: ||eta_x - k_lambda|| -> 0 in the relevant norm (after normalization and scale identification).
- (C3, positivity) QW_lambda is positive with radical contracting to {0} as lambda -> infinity.

Why this is the whole problem. By Bombieri-Weil, positivity of the Weil functional for all admissible test functions is equivalent to RH; the cutoff family V_Lambda exhausts the admissible functions, so (C3) is exactly global Weil positivity. Lemma C is RH.

Three facts the adversary will use against any proof of Lemma C:

1. eps(x) decays doubly-exponentially: 1 - chi_2 ~ exp(-4 pi e^L) (Connes Fig 1; experiments e3s, e3j). The near-radical is high-dimensional and the spectral gap collapses. A proof that needs an isolated, simple ground state with a gap bounded below is fighting this.
2. The Davenport-Heilbronn (D-H) L-function has a functional equation, its own QW_lambda^DH, its own Lemmas A and B, BUT is RH-FALSE (off-line zeros at 0.8085 + 85.699 i). So Lemma C is FALSE for D-H. The prolate ansatz k_lambda is archimedean-only and SHARED with D-H. Any proof of Lemma C that does not use a structure D-H lacks (the Euler product) is therefore wrong.
3. Weil positivity of QW_lambda for all lambda is itself equivalent to RH (Bombieri/Weil), so any "soft" route that does not engage the exact structure of zeta is circular.

---

## 3. The committed candidate proof of Lemma C (monotonicity / no-first-failure)

We commit to the single most instructive attempt: treat eps(x) as a function of the one real parameter Lambda, and run a continuity / no-first-failure (induction-on-the-cutoff) argument, with the Euler product entering as the sign of the prime increment. This is the strongest attempt because its scaffold (Lemmas A and B proven; the no-first-failure organization) is genuinely reusable, and it localizes the entire RH content into ONE inequality (Step 5), which is the cleanest possible statement of where the Euler product must enter.

NOTATION. Lambda = (1/2) log x, lambda = e^Lambda. H = L^2_even(R, dt). The form, the admissible cone V_Lambda, the operator A_lambda, the minimal eigenvalue eps(x), and the even ground state eta_x are as in the Setup.

**Step 1 (Dilation embedding, nesting of cones).** For Lambda' < Lambda the extension-by-zero map J : V_{Lambda'} -> V_Lambda is an isometry of H, preserves the pole constraint (ghat unchanged), and commutes with autocorrelation (supports only enlarge). Hence

    V_{Lambda'} subset V_Lambda     for Lambda' < Lambda.        (1)

**Step 2 (Same form on the smaller cone).** For g in V_{Lambda'} the prime sums agree: any prime power n with log n > 2 Lambda' contributes Lambda_vM(n) n^{-1/2} (g * g^*)(log n) = 0, since (g * g^*) is supported in [-2 Lambda', 2 Lambda']. A_arch is cutoff-independent. Therefore

    QW_Lambda(g) = QW_{Lambda'}(g)     for all g in V_{Lambda'}.        (2)

The family is a single quadratic form on H minimized over a growing nested family of subspaces.

**Step 3 (Monotonicity by min-max).** A larger feasible set lowers an infimum, while the value on any fixed feasible vector is unchanged. So eps is non-increasing in Lambda:

    Lambda' < Lambda  ==>  eps(x) <= eps(x').        (3)

If positivity ever fails it fails by first crossing zero from above. The failure set { eps < 0 } is an up-set (Lambda_*, infinity) with a well-defined first-failure time Lambda_* = sup{ Lambda : eps(x) >= 0 }. The question is whether Lambda_* = +infinity.

**Step 4 (Continuity and the spectral derivative).** By Step 2 the form depends on Lambda only through which prime powers are switched on, a step function in Lambda. Between thresholds, eps(Lambda) is real-analytic; globally it is continuous (Kato; the pole constraint is a fixed rank-1 codimension preserved by J). By Feynman-Hellmann, on the normalized ground state,

    d eps / d Lambda = < eta_x, (d A_lambda / d Lambda) eta_x >.        (4)

**Step 5 (KEY INEQUALITY: the increment is signed by the von Mangoldt coefficients).** A_arch is Lambda-independent; the boundary dilation contributes a non-negative relaxation term. The prime block contributes, at each threshold and through the moving autocorrelation support,

    d/dLambda [ -P_Lambda(eta_x) ] = -2 sum_{newly active n} Lambda_vM(n) n^{-1/2} (eta_x * eta_x^*)(log n).

Each newly activated rank-one shift-overlap operator enters with the FIXED-SIGN weight Lambda_vM(n) n^{-1/2}. Since Lambda_vM(n) >= 0 for every n (log p on prime powers, 0 otherwise) and n^{-1/2} > 0, and the even prolate-type ground state's edge autocorrelation (eta_x * eta_x^*)(2 Lambda) is non-negative (claimed: the even vanishing-integral combination of h_0, h_4 is sign-stable near the support edge), the prime increment is a single-signed, definite perturbation. The only mechanism that could drive eps below 0 is an archimedean cushion shortfall, bounded below by the prolate variational value (Lemma B). This is the Euler-product input: Lambda_vM(n) >= 0 is precisely the statement that -zeta'/zeta = sum Lambda_vM(n) n^{-s} has non-negative Dirichlet coefficients. D-H lacks it (its coefficients oscillate in sign), so for D-H the increment is indefinite and the no-first-failure handle does not exist.

**Step 6 (Base case: Yoshida positivity).** For Lambda small enough that x = e^{2 Lambda} admits no or few prime powers, QW_Lambda = A_arch (plus finitely many dominated prime overlaps) is strictly positive: Omega(t) = Re psi(1/4 + i t/2) - log pi (Q=1) is bounded below, the associated Toeplitz form is positive, and the pole constraint removes the only would-be null direction. Yoshida's interval-positivity theorem extends this to an explicit [0, Lambda_0]:

    eps(x) > 0     for all Lambda in [0, Lambda_0].        (6)

**Step 7 (No-first-failure: closing the induction).** Suppose Lambda_* < +infinity. By continuity eps(Lambda_*) = 0, so eta_{x_*} is a null vector of QW_{Lambda_*}. By Lemma A and the Connes-van Suijlekom simplicity bound the marginal-positive ground state is simple and isolated, so the form does not degenerate transversally: a downward crossing requires d eps/dLambda < 0 at Lambda_*. But (5) bounds the derivative below by the controlled boundary term, and at Lambda_* the variational value equals the prolate value k_{lambda_*}, whose energy is non-negative for every finite Lambda (the archimedean variational minimum, lowered only by the single-signed prime amount of Step 5, dominated by the cushion via the explicit Fact-6.4 exp-decaying residual). Hence eps(Lambda_*) = 0 forces eps >= 0 immediately to the right, contradicting eps < 0 for Lambda > Lambda_*. Therefore Lambda_* = +infinity:

    eps(x) >= 0     for all x > 1.        (7)

**Step 8 (Global positivity = RH; radical contraction).** By (7), QW_lambda >= 0 for every cutoff. Bombieri-Weil + exhaustion of admissible test functions gives global Weil positivity, hence RH. Moreover eps >= 0 together with the Fact-6.4 vanishing residual squeezes eps(x) -> 0 from above and pins the minimizing direction; the radical contracts to the directions where the prolate model is energy-exact, so any normalized near-radical g satisfies ||g - k_lambda|| -> 0 (Lemma B uniqueness + Lemma A simplicity). This is (C3).

**Step 9 (Convergence; RH).** By Step 8, ||eta_x - k_lambda|| -> 0. The Fourier transform is continuous from this norm to uniform-on-compacts convergence of exponential-type entire functions (Paley-Wiener). Hence eta_x-hat -> k_lambda-hat -> Xi uniformly on compacts (this is C1 = Lemma C). By Lemma A each eta_x-hat has only real zeros; by Hurwitz Xi has only real zeros; Xi's zeros are zeta's nontrivial zeros on the critical line. RH. QED.

---

## 4. Autopsy

All four candidate proofs of Lemma C are FATAL and CIRCULAR, and every one of them would, run verbatim, prove the FALSE Davenport-Heilbronn RH. The shared disease: the only step that purports to distinguish zeta from D-H is either assumed (it is RH itself) or zeta-blind (every input to it is archimedean, shared with D-H). This is the marginal-positivity thesis seen from four sides: there is no soft buffer, so no perturbation-with-vanishing-bound, no pointwise domination, no archimedean-cone projection, and no termwise sign fact can close the gap.

### 4.1 Attempt 1: Gamma-convergence / variational stability

- Break point: Part 2 Step 2.2, the limsup/recovery half. The asserted estimate QW_lambda(k_lambda)/||k_lambda||^2 = eps(x) + o(sigma(x)) is the only place the limit minimizer is pinned to k_infty.
- Why fatal: it is a category error about which quantity controls the rescaled limit. The cited numerical input (e3t) measures a finite-N discretization FLOOR (eps_min and Q(k)/||k||^2 both ~0.1 and increasing with x in the reachable range), not the TRUE eps(x), which decays like exp(-4 pi e^L). The archimedean prolate ansatz carries no prime data and cannot track that doubly-exponential descent, so after normalization by the polynomially-growing sigma(x) the recovery energy stays bounded away from 0. The limsup inequality fails. Second independent break: the limit form A_arch with log-growing symbol Omega is not Rellich-compact, so normalized minimizers need not be tight (Step 3.2), and the prolate limit is not isolated (gap collapse, e3s/e3j); the "unique up to scale" identification (Step 3.3) is unjustified.
- Proves D-H RH: YES. The recovery sequence, the form domain, the archimedean Toeplitz limit, the compactness, and Hurwitz are identical for D-H; Step 1.2 declares the only difference (the prime block) a vanishing-relative-bound perturbation. So it yields eta_x^DH-hat -> Xi_DH with only real zeros, contradicting the known off-line zero.
- D-H failure locus: Step 1.3 (identify the Gamma-limit minimizer as k_infty), reached via the archimedean-only recovery of Step 2.2. The Euler product, living entirely in P_lambda, is explicitly discarded.

### 4.2 Attempt 2: archimedean pointwise domination (M3 / e3m)

- Break point: Step 3, the pointwise inequality Psi_infty(tau) - Pi_x(tau) >= 0, in particular the Step 3(a) order claim (bulk prime mass O(sqrt(x)/log x) vs archimedean+boundary O(x)).
- Why fatal: numerically FALSE for zeta itself. The bracket attains its minimum at tau = 0 and is massively negative and growing: -25.95 (x=25), -45.90 (x=100), -87.27 (x=400). Pi_x(0) ~ 4 sqrt(x) (measured 4.1 sqrt(x)), not O(sqrt(x)/log x): the proof silently dropped the log p weight and the geometric factor 1/(1 - p^{-1/2}). The "8x vs 4 sqrt(x)/log x surplus" is a units error: W_pole is a per-test-function scalar (killed by the pole constraint), Pi_x(tau) is a density inside the integral. The project's own e3f confirms near-total cancellation to O(0.1) (boundary +144.4, prime -120.3, const -18.6, gamma -5.4, sum +0.088 at b=20), never an order-x margin.
- Proves D-H RH: YES, and revealingly the false inequality is CLOSER to holding for D-H (min -4.5) than for zeta (min -87.3) at x=400, because D-H's sign-oscillating coefficients partially cancel while zeta's non-negative von Mangoldt weights ADD. The very feature the proof claims breaks D-H makes its bracket less negative.
- D-H failure locus: there is NO step true for zeta and false for D-H. The Euler product is invoked rhetorically (rank-one ladder, Weyl independence of {log p}) but never made load-bearing, because the load-bearing inequality is false for zeta regardless of Euler structure. e3g shows D-H is Weil-positive on the same reachable test functions (W_DH = +0.37 at b=20) exactly as zeta is.

### 4.3 Attempt 3: de Branges / Hermite-Biehler cone projection (bypass eta_x)

- Break point: Step 2, the cone-distance bound dist_{H(E_lambda)}(k_lambda-hat, C_lambda)^2 <= sum_{j>2M} chi_j(lambda) ~ exp(-4 pi lambda^2).
- Why fatal: it conflates two distinct distances. The Slepian tail measures basis-truncation ENERGY (archimedean, depends only on PW_lambda and lambda). C_lambda is the cone of ONLY-REAL-ZEROS functions; the metric distance to it is governed by the target's complex zeros. The truncation tail does not bound the distance-to-cone. Counterexample: z^2 + 1 has zero truncation residual in span{1, z, z^2} yet L2 distance 2.0 to the nearest real-rooted quadratic on [-2, 2], precisely because of its complex zeros at +- i. So Step 2's bound holds for k_lambda only if Xi has only real zeros, i.e. only if RH. The conclusion is smuggled into the distance estimate. K1 circularity.
- Proves D-H RH: YES (with a twist). Steps 1-3 are L-function-blind verbatim: every input (PW_lambda, E_lambda, H(E_lambda), C_lambda, k_lambda*, the reproducing-kernel bound) is a function of (lambda, PW_lambda) alone; the construction code is byte-for-byte identical for zeta and D-H. There is no separate D-H prolate ansatz: the same archimedean k_lambda recovers the first ZETA zero 14.138, not D-H's 5.094. The closing "self-selection" paragraph ("for D-H the ansatz converges to Xi_DH") is FALSE; no such ansatz exists. Substituting Xi_DH as the limit, the identical false Step 2 proves Xi_DH has only real zeros.
- D-H failure locus: Step 2's distance-to-cone bound, structurally identical for both because every input is archimedean. The de Branges framing adds nothing past Lemma A: it relocates the on-line-zero-manufacturing mechanism from the minimizer to the ansatz, but the gap (dist(k_lambda-hat, C_lambda) -> 0) is provably equivalent to RH.

### 4.4 Attempt 4: monotonicity / no-first-failure (the committed proof above)

- Break point: Step 5, the KEY INEQUALITY. The increment sum_n Lambda_vM(n) n^{-1/2} (eta_x * eta_x^*)(log n) is claimed single-signed because Lambda_vM(n) >= 0.
- Why fatal: the non-negative weights multiply a SIGN-INDEFINITE autocorrelation. Computed on the actual minimal eigenvector (zeta, x=49, N=160), (eta_x * eta_x^*)(log n) changes sign across n: 13 positive and 10 negative increment terms. The "prolate edge sign-stability" sub-claim is contradicted by the real eigenvector. The required object is the NET sign of the global sum, a cancellation statement, not a termwise sign fact, and it is itself RH-equivalent (finding #43: the RH-equivalent pairing is a global sum, never termwise positive). Secondary: Step 2 fails numerically (extension-by-zero of the x'=25 minimizer into the x=81 form gives relative form-difference 2.84 and drifts ghat(i/2) from 1e-17 to 6.5e-3), so the clean min-max nesting does not hold; Step 7's "no downward crossing" also leans on a spectral gap that e3s/e3j show collapses (eps ~ exp(-4 pi e^L) reaches 0 with vanishing slope AND vanishing gap, exactly the regime where "cannot dip below 0" fails).
- Proves D-H RH: YES. Measured eps(Lambda) over x in {9,...,81} is monotone and stays positive for BOTH zeta and D-H, so Steps 1-4, 6, 7-9 give the identical conclusion for D-H. Step 5 is the only claimed discriminator and it is false for zeta too: zeta's increment is mixed-sign (13+/10-) just like D-H's (19+/16-).
- D-H failure locus: Step 5. The D-H coefficients do carry mixed signs, but that is irrelevant because the autocorrelation factor is sign-indefinite for zeta as well, so zeta's increment is also mixed-sign. No surviving discriminating step.

### 4.5 Summary table

| Attempt | Strategy | Break point | Why fatal (one line) | Proves D-H RH? | D-H failure locus | Circular? |
|---|---|---|---|---|---|---|
| 1 | Gamma-convergence / variational stability | Step 2.2 (recovery) | Recovery energy compares discretization floors, not the true exp(-4 pi e^L) eps; rescaled limsup fails | YES | Step 1.3 via archimedean-only recovery; P_lambda discarded as vanishing-bound | YES |
| 2 | Archimedean pointwise domination | Step 3 (domination) | Psi_infty - Pi_x is negative and growing for zeta (-87 at x=400); units error scalar vs density | YES | None: no step true-for-zeta-false-for-DH; Euler invoked rhetorically | YES |
| 3 | de Branges cone projection | Step 2 (cone distance) | dist-to-cone bounded by archimedean truncation tail; true only if Xi real-rooted = RH | YES | Step 2 identical for both; closing self-selection paragraph is false | YES |
| 4 | Monotonicity / no-first-failure | Step 5 (key inequality) | Non-negative Lambda_vM multiplies sign-indefinite autocorrelation; zeta increment is 13+/10- | YES | Step 5; zeta's increment mixed-sign too, so no discriminator | YES |

The four break points are four disguises of one fact: the discriminating step in each is either RH itself (attempts 1, 3) or a termwise/pointwise positivity that is numerically false for zeta (attempts 2, 4). The archimedean half (Lemmas A, B, the prolate ansatz, the cushion Omega) is shared with D-H; the discriminating Euler/{log p} half is exactly what each attempt fails to make load-bearing.

---

## 5. What we actually need

A correct proof of Lemma C must satisfy BOTH:

1. **Non-circular.** It must not assume any statement about the location of Xi's zeros, the positivity of QW_lambda at large Lambda, or the convergence eta_x-hat -> Xi. Concretely: every quantity in the discriminating step must be computable from the archimedean data plus the von Mangoldt coefficients WITHOUT evaluating zeta off the half-plane of absolute convergence. (Lean cheap-probe 5 / #49 already machine-certifies the static form is non-circular; the dynamic argument must inherit this.)

2. **Uses an Euler-product / Frobenius input D-H lacks, made LOAD-BEARING.** The step must measurably differ between zeta and D-H. The discrimination must ride the prime block P_lambda as a GLOBAL CANCELLATION property (a Li-coefficient-type sum, #43), not as termwise non-negativity (#46: zeroing the prime block makes zeta FAIL exactly as D-H does, so the sign genuinely lives there). The autocorrelation-sign test is the cheap gate: any proof whose discriminating step evaluates the same on zeta and D-H is dead on arrival.

The precise missing object. A net-sign / lower-bound control on the global sum

    S(Lambda) = sum_{n <= x} Lambda_vM(n) n^{-1/2} (eta_x * eta_x^*)(log n)

(or its rescaled-residual analogue), proving that for zeta S(Lambda) stays dominated by the archimedean cushion down to the doubly-exponential scale eps_zeta(x) ~ exp(-4 pi e^L), WHILE for D-H the analogous sum is bounded away (the off-line obstruction floor, e3j: -78.7% deficit). This is genuinely RH-hard; it is the real content, and the variational / domination / de Branges / monotonicity wrappers add nothing to it.

Three concrete sub-targets (in increasing difficulty):

- **ST1 (rescaled-residual benchmark, VERIFIER).** Define the true test: any claimed recovery sequence k must satisfy (QW_lambda(k) - eps_true(x))/sigma(x) -> 0 where eps_true is the high-precision minimal eigenvalue TRACKING exp(-4 pi e^L), not the finite-N floor e3t reports. Build the high-precision eps_true(x) ladder and the D-H twin (mu=1, log_Q = log sqrt 5) so every future attempt is gated against both. This makes the marginal-positivity wall a standing regression assertion.

- **ST2 (Euler enters the cushion-vs-prime margin).** Prove the prime block forces eps_zeta(x) -> 0 at rate exp(-4 pi e^L) while eps_DH(x) is bounded away from 0 (converges to the off-line obstruction floor). This is the redirection all four autopsies converge on: replace the soft step with an estimate where P_lambda controls eps down to the doubly-exponential scale. It is RH-hard but it is the correct target.

- **ST3 (global cancellation = Euler structure).** Prove the net sign of S(Lambda) is governed by a global Li-coefficient-type cancellation that is present for zeta (multiplicativity of Lambda_vM, equivalently the Euler product) and ABSENT for D-H (non-multiplicative, no Euler product). This is the deepest sub-target and is essentially Lemma C itself; ST1 and ST2 are the operational footholds toward it.

The compass reading is unchanged and now quadruply confirmed: RH on the Connes eta_x line is true only at the margin. The proof must engage the exact multiplicative structure of zeta (the Euler product as a global cancellation), not any generic positivity, archimedean domination, or soft variational stability. Every attempt that routes its discriminating power through the shared archimedean prolate world fabricates the same false theorem for Davenport-Heilbronn.