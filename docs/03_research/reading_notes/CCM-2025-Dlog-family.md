# Reading notes: the CCM D_log family (arXiv:2511.22755 + arXiv:2511.23257)

> Section-by-section, theorem/equation-level notes on the two Nov-2025 papers that carry the
> Connes-Consani-Moscovici "zeta spectral triple" and its self-adjointness engine, read
> **fetch-verified from the arXiv PDFs** (both downloaded in full; 22755 = 34 pp, 23257 = 26 pp).
> Companion to the existing repo treatment: this note is the reimplementation-grade extraction the
> earlier notes flagged as needed. The strategic mapping (CCM converges on M4 / the Section-7 uniform
> limit; finite-cutoff reality is information-free) is already recorded in
> [`ccm_semilocal_prolate.md`](../ccm_semilocal_prolate.md) (Addenda 2026-07-02, LEARNINGS #153/#154),
> [`ccm_zeta_cycle_density_gate.md`](ccm_zeta_cycle_density_gate.md), and
> [`Connes-2026-RH-Past-Present-Letter.md`](Connes-2026-RH-Past-Present-Letter.md). This note EXTENDS
> those by pinning the exact operator, the exact determinant identity, the exact CF condition, and the
> exact Section-7 statement, so a BUILDER can reimplement in mpmath and an ADVERSARY can run the K2
> Davenport-Heilbronn probe. Page/eq refs are to the arXiv v1 PDFs.
>
> - **arXiv:2511.22755**, Connes-Consani-Moscovici, *Zeta Spectral Triples* (27 Nov 2025; to appear,
>   EMS). The operator D_log^(lambda,N), Theorem 5.10, the determinant identity, Section 7.
> - **arXiv:2511.23257**, Connes-van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral
>   Action* (28 Nov 2025; dedicated to Huzihiro Araki). The Caratheodory-Fejer self-adjointness engine
>   = reference [7] of 22755. Read in full (Theorems 1.1/1.2/3.1, Props 2.1/2.2/4.1/4.2, Lemmas
>   5.1-5.3, Remark 2.3).

## One-line takeaway

The 2511 family bypasses the deferred metaplectic Jacobi operator W_{lambda,S} of the 2310.18423 program
and replaces it with an **explicit, elementary, unconditionally-computable** object: a rank-one
perturbation D_log^(lambda,N) of the scaling Dirac on the log-circle [lambda^{-1}, lambda], whose
**regularized determinant is exactly** det_reg(D_log^(lambda,N) - z) = -i lambda^{-iz} xihat(z) with
xihat the Fourier transform of the ground state of the truncated Weil form. Because the perturbation is
rank-one and the surviving block is a **finite self-adjoint matrix**, **all zeros of xihat are real at
every finite cutoff, unconditionally** (Thm 5.10(iii)) - this is D-H-blind, information-free finiteness.
The zeta-vs-D-H discrimination lives entirely in the unproven Section-7 uniform limit xihat_lambda -> Xi,
which the authors call "the main remaining obstacle to our approach to RH."

## The two papers and how they fit

- **23257 (Connes-van Suijlekom) is the engine.** It proves the abstract fact "real + even + lower-bounded
  + simple lowest eigenvalue => all zeros of the eigenvector's Fourier transform are real," as a
  distributional generalization of a Caratheodory-Fejer 1911 corollary about Toeplitz matrices. It never
  mentions zeta.
- **22755 (Connes-Consani-Moscovici) is the application.** It feeds the Weil quadratic form (restricted to
  test functions supported on [lambda^{-1}, lambda], so only prime powers <= lambda^2 enter) into that
  engine, packages the result as a spectral triple, computes the regularized determinant, and shows the
  determinant zeros approximate the zeta zeros with the extraordinary numerics (primes <= 13 give the
  first zero to 2.44e-55; error grows to ~1e-3 by the 50th zero).

---

## (a) The operator D_log^(lambda,N) (22755 Section 5) -- reimplementation-grade

**Base operator (the scaling Dirac on the log-circle).** eq (5.14):
> D_log^(lambda) = -i u d/du = -i d/d(log u), acting on L^2([lambda^{-1}, lambda], d*u), d*u = du/u,
> with periodic boundary conditions.

Set L = 2 log lambda (the circumference). The isometry kappa: L^2([0,L], dx) -> L^2([lambda^{-1},lambda], d*u),
kappa(f)(u) = f(log(lambda u)) (eq 3.17), turns the interval [lambda^{-1}, lambda] into a circle of length L.

**Orthonormal basis.** U_n(x) = L^{-1/2} exp(2 pi i n x / L) on [0,L] (eq 2.6); transported,
V_n(u) := U_n(log(lambda u)) = kappa(U_n) on [lambda^{-1}, lambda] (eq 3.21). Then D_log^(lambda) V_n =
(2 pi n / L) V_n, so on E_N := span{V_n : |n| <= N} one has D_log^(lambda)|_{E_N} = (2 pi / L) diag(n),
|n| <= N (the periodic Dirac / Dirichlet spectrum). E_N^perp is its orthogonal complement in
L^2([lambda^{-1}, lambda], d*u).

**The perturbation vector = ground state of the truncated Weil form.** QW_lambda^N = restriction to E_N of
the Weil quadratic form QW_lambda (eq 3.19, below). Let epsilon_N = smallest eigenvalue of QW_lambda^N,
**assumed simple**, and xi = Sum_{|k|<=N} xi_k V_k the corresponding eigenvector, **assumed even** (invariant
under u -> u^{-1}, i.e. xi_{-k} = xi_k), normalized by delta_N(xi) = 1.

**The Dirichlet-kernel co-vector.** eq (5.15): delta_N := L^{-1/2} Sum_{n=-N}^{N} V_n. It represents the
Dirichlet kernel and satisfies lim_{N->inf} <delta_N | f> = f(lambda) (Cor 5.6): it is the
approximate-evaluation-at-the-boundary functional.

**The rank-one perturbation (Theorem 1.1 / Prop 5.7), verbatim:**
> D_log^(lambda,N) = D_log^(lambda) - |D_log^(lambda) xi><delta_N|

It is the unique operator with the same domain as D_log^(lambda) that (i) agrees with D_log^(lambda) on
ker delta_N and (ii) kills xi: D_log^(lambda,N)(xi) = 0 (Prop 5.7). It is self-adjoint in the direct sum
E_N' (+) E_N^perp, where E_N' = E_N / C xi carries the inner product = restriction of QW_lambda^N -
epsilon_N <.|.> (Thm 1.1(i)). NOTE: self-adjointness is with respect to the **Weil-form inner product on
the quotient**, not the ambient L^2 -- this is the content the CF engine supplies.

**mpmath recipe (self-contained):**
1. Fix lambda > 1, L = 2 log lambda, integer N (paper uses N = 120).
2. Assemble the (2N+1) x (2N+1) real symmetric matrix Q of QW_lambda^N in the {V_n} basis via eq (3.19):
   archimedean theta-density term (eqs 3.8-3.9) + pole term 2 Re(Vhat_m(i/2) conj Vhat_n(-i/2)) (3.11) -
   Sum_{1 < k <= lambda^2} Lambda(k) <V_m | T(k) V_n>, with T(k) from eq (3.20) evaluated via the closed
   forms q(U_m,U_n) of eqs (2.9)/(2.10). Equivalently use the CF-paper "divided-difference" normal form
   (23257 Prop 4.1): q_{m,n} = (psi(m) - psi(n))/(m - n) for m != n, psi'(n) for m = n.
3. Diagonalize Q; take smallest eigenvalue epsilon_N (verify simple + even: xi_{-k} = xi_k). Normalize by
   delta_N(xi) = L^{-1/2} Sum_k xi_k = 1.
4. The finite-block spectrum of D_log^(lambda,N) = the real zeros of xihat (below) = the zeta-zero
   approximations. Requires ~200-digit mpmath precision (paper's stated working precision).

## (b) The regularized determinant and what xihat is (22755 Section 5.5-5.6)

**Regularized determinant, defined by the spectral zeta** (eq 5.16): det_reg(D - s) = exp(-zeta_D'(0; s)),
zeta_D(z; s) := Sum (mu - s)^{-z} over the spectrum {mu}. The negative-eigenvalue branch requires the
spectral-cut choice (-1)^{-z} := e^{-i pi z} (this phase is load-bearing: it repairs spectral invariance
s -> s + 1 that the naive sine-product would violate).

**Baseline (Lemma 5.8):** for the bare Dirac D with spectrum (2 pi / L) Z,
det_reg(D - s) = 1 - e^{-i L s} (eq 5.17).

**Fourier transform (the "duality <R*_+ | R>").** F_mu(f)(s) := integral_{R*_+} f(u) u^{-i s} d*u. For the
ground state xi(u) = Sum_{|j|<=N} xi_j V_j(u) (extended by 0 off [lambda^{-1}, lambda]), Prop 5.9 / eq (5.25):
> xihat(z) = 2 L^{-1/2} sin(z L / 2) ( Sum_{j=-N}^{N} xi_j / (z - 2 pi j / L) ).
The sin(z L/2) zeros at z in (2 pi / L) Z cancel the poles at 2 pi j / L wherever xi_j != 0, leaving xihat
entire.

**The exact determinant identity (Theorem 5.10(ii)), verbatim:**
> det_reg(D_log^(lambda,N) - z) = -i lambda^{-iz} xihat(z),  where xihat is the Fourier transform of xi
> for the duality <R*_+ | R>.

So **xihat is literally the regularized characteristic function of the operator**, up to the explicit
prefactor -i lambda^{-iz} = -i e^{-i z L / 2}. Proof route: det_reg factors as
Det(D_log^(lambda,N)|_{E_N'} - z) * det_reg(D_log^(lambda)|_{E_N^perp} - z); the first factor is the
characteristic polynomial of a finite self-adjoint matrix, the second has zeros {2 pi j / L : |j| > N}.

**The truncated Weil form (eq 3.19), verbatim:**
> QW_lambda(f,f) = integral_R |Fhat(t)|^2 (2 d_t theta(t) / 2 pi) dt + 2 Re( Fhat(i/2) conj Fhat(-i/2) )
> - Sum_{1 < n <= lambda^2} Lambda(n) <f | T(n) f>,
with theta(t) = -(t/2) log pi + Im log Gamma(1/4 + i t/2) the Riemann-Siegel angle (eq 3.9), Lambda(n) the
von Mangoldt function, and T(n) (eq 3.20) <f | T(n) g> = n^{-1/2}((f * g)(n) + (f * g)(n^{-1})). The support
[lambda^{-1}, lambda] of f forces f * g into [lambda^{-2}, lambda^2], so **only prime powers n <= lambda^2
enter**: the sum is finite. (This is the "only Euler products p <= x = lambda^2" of the abstract.)

## (c) The finite-cutoff reality theorem (Thm 5.10(iii)) -- the D-H-blind, information-free fact

**Theorem 5.10(iii), verbatim:**
> The Fourier transform xihat(z) is an entire function, all its zeros are on the real line and coincide
> with the spectrum of D_log^(lambda,N).

**Why it is unconditional and D-H-blind.** The proof (p.24) factors the regularized determinant as
det_reg(D_log^(lambda,N) - z) = Det(D_log^(lambda,N)|_{E_N'} - z) * det_reg(D_log^(lambda)|_{E_N^perp} - z).
The **first factor is the characteristic polynomial of a self-adjoint matrix** (D' on E_N' is self-adjoint
for the Weil-form inner product, by the CF engine), hence has only real zeros; the second factor has zeros
{2 pi j / L : |j| > N}, all real. **No property of zeta is used.** The theorem holds for ANY lambda > 1 and
N for which QW_lambda^N is even-simple. Consequently the on-line reality of the finite-cutoff determinant
zeros carries **zero bits about RH**: it is the "total form of the stealth window" (LEARNINGS #154), the
information-free finiteness the project's move-criterion names as non-moving. The numerics (Figure 1;
Section 6 tables) show the finite-cutoff real zeros approximating the zeta zeros, but the reality itself is
manufactured by finite self-adjointness, not by the arithmetic.

## (d) The Caratheodory-Fejer self-adjointness condition (23257) -- the K2 gate

**The classical seed (23257 Section 1, Corollary 1.1), verbatim:**
> Let T in M_{n+1}(C) be a Hermitian, positive semidefinite Toeplitz matrix of rank n, and let xi in ker T.
> Then all the zeros of the polynomial P(z) := Sum_{j=0}^{n} xi_j z^j lie on the unit circle.
This is a corollary of the Caratheodory-Fejer 1911 structure theorem (a rank-r PSD Toeplitz matrix
factors as V D V* with V a Vandermonde on r distinct unit-circle points z_1,...,z_r and D positive
diagonal). Props 2.1-2.2 give a purely *-algebraic proof: the palindromic/anti-palindromic kernel vector's
polynomial P generates an ideal whose GNS measure is supported on the unit circle.

**The distributional main theorem (23257 Theorem 1.2, refined as Theorem 6.1), verbatim:**
> Let L > 0, D be a real distribution on the interval [0,L] and tilde-D the associated even distribution on
> [-L,L]. Assume that the quadratic form with Schwartz kernel tilde-D(x - y) defines a lower-bounded
> self-adjoint operator A on L^2([-L/2, L/2]), and that the minimum of its spectrum is a simple, isolated
> eigenvalue lambda, with even eigenfunction xi. Then all the zeros of the entire function xihat(z), z in C,
> Fourier transform of xi, lie on the real line.

**Exactly what the coefficient/moment stream must satisfy (the four conditions):**
1. **Real:** the distribution D is real (=> the matrix q_{m,n} is Hermitian; a_{-k} = conj(a_k)).
2. **Lower-bounded / self-adjoint:** the quadratic form with kernel tilde-D(x-y) is lower-bounded.
3. **Simple + isolated lowest eigenvalue:** the spectral minimum is a simple, isolated eigenvalue.
4. **Even eigenfunction:** the minimizing eigenvector xi is even (which the reflection symmetry of the
   even distribution tilde-D guarantees is achievable).

The matrix that carries this in the finite case has the special "divided-difference" normal form (23257
eq (11), Props 4.1/4.2): q_{i,i} = a_i, q_{i,j} = (b_i - b_j)/(i - j) for i != j, with a_{-i} = a_i,
b_{-i} = -b_i. Section 4.3 shows this is exactly the matrix of the second Gateaux derivative of the spectral
action (the "Echoes of the Spectral Action" of the title): q_{ij} = (b_i - b_j)/(lambda_i - lambda_j) with
b_i = f'(lambda_i), a_i = f''(lambda_i), lambda_i = i the Dirac spectrum on the circle.

**Remark 2.3 (the essential caveat, verbatim in substance):** when the lowest eigenvalue is NOT simple, the
theorem can FAIL; the correct statement is then that the **intersection** of the zeros of the various lowest
eigenfunctions lies on the circle (the radical of the quadratic form). Simplicity is therefore load-bearing;
it is exactly the hypothesis 22755 flags as "to be verified" (Thm 1.1: "assumed simple ... assumed even").

**Why this is the K2 gate.** Conditions 1-4 reference **only the real/even/lower-bounded/simple structure of
the form**, never an Euler product and never RH. The CF engine is **input-agnostic**: it runs on any stream
that produces a real, even, lower-bounded form with a simple even ground state. This is the precise 2511
restatement of the repo's e3s finding ("Caratheodory-Fejer is input-agnostic; the identical machine
reproduces D-H on-line zeros").

## (e) The Section-7 uniform-convergence statement (22755 Section 7) -- the main remaining obstacle

**The claimed convergence (Section 7, p.27), verbatim:**
> When lambda -> inf the functions xihat_lambda(z) multiplied by suitable constants, converge uniformly on
> closed substrips of the open strip Im(z) < 1/2 towards the Xi-function of Riemann
> Xi(s) = xi(1/2 + i s), xi(z) = (1/2) z(z-1) pi^{-z/2} Gamma(z/2) zeta(z). ... This convergence would
> entail RH using Hurwitz theorem on the zeros of limits of holomorphic functions.

Two-step structure (fixed lambda then lambda -> inf):
- **Fixed lambda, N -> inf (proven):** det_reg(D_log^(lambda,N) - s) -> -i lambda^{-is} xihat_lambda(s)
  uniformly on compact subsets of C (footnote 2, p.27), xihat_lambda = FT of the true minimal eigenvector
  xi_lambda of QW_lambda normalized by xi(lambda) = 1.
- **lambda -> inf (the gap):** xihat_lambda -> Xi. The route factors through the educated-guess ansatz
  k_lambda = E(h_lambda) (eq 7.6), where E(f)(u) = u^{1/2} Sum_{n>=1} f(nu) (eq 7.2), h_lambda the
  vanishing-integral combination of the localized prolate/Hermite functions h_{0,lambda}, h_{4,lambda} of
  the prolate wave operator PW_lambda = -d_x[(lambda^2 - x^2) d_x] + (2 pi lambda x)^2 (eq 7.5).

**What is PROVEN vs the gap:**
- **Lemma 7.3 (proven):** khat_lambda -> Xi uniformly on closed substrips of |Im(z)| < 1/2 (via the classical
  prolate-to-Hermite-Weber estimates of Lemma 7.2: max_{[-lambda,lambda]} |h_{n,lambda} - h_n| <= c lambda^{-2},
  and 1 - chi_4(lambda) ~ (2^14/3) sqrt(2) pi^5 e^{-4 pi lambda^2 + 9 log lambda}).
- **The gap (Section 7, p.28), verbatim:** the educated guess k_lambda approximates a scalar multiple of the
  true eigenvector xi_lambda; "Justifying rigorously this step is the main remaining obstacle to our approach
  to RH."

So the mode of convergence is **uniform on closed substrips of the open strip Im(z) < 1/2**, and the missing
link is the identification xi_lambda ~ k_lambda (true minimal eigenvector ~ prolate ansatz), NOT the ansatz's
own limit (which is Lemma 7.3, proven). Combined with Thm 5.10(iii) (each xihat_lambda has only real zeros),
uniform convergence + Hurwitz would force Xi to have only real zeros = RH.

## (f) HONEST feasibility: transplanting the machinery onto Davenport-Heilbronn

**Question.** D-H has the same functional-equation shape (a completed function with the zeta Gamma-factor)
but no Euler product, and KNOWN off-line zeros near 0.808 + 85.699 i. Can the D_log machine be run with the
D-H completed function substituted for xi/Xi? What breaks, and where?

**Buildability of the D-H truncated form.** The operator T(n) (eq 3.20) is defined for ALL n by evaluation at
n, n^{-1}; it needs no Euler product. The D-H L-function has a Dirichlet series and a functional equation, so
its logarithmic-derivative coefficients Lambda_DH(n) (from -L'_DH/L_DH(s) = Sum Lambda_DH(n) n^{-s}) exist as
a genuine coefficient stream. The support argument (f * g in [lambda^{-2}, lambda^2]) still truncates the sum
to n <= lambda^2, so QW_lambda^{DH}(f,f) = archimedean theta-density term [same Gamma-factor as zeta] +
pole/constant term - Sum_{1 < n <= lambda^2} Lambda_DH(n) <f | T(n) f> is a well-defined finite form. Two
structural differences from zeta: (i) D-H has NO pole, so the 2 Re(Fhat(i/2) conj Fhat(-i/2)) term is
replaced/absent; (ii) Lambda_DH(n) is supported on ALL integers n (no Euler factorization => the log-derivative
coefficients do not vanish off prime powers) and can change sign, so the coefficient stream is
non-multiplicative and denser, but still finite under truncation.

**Does the CF self-adjointness gate (K2) run on the D-H stream? YES, structurally.** The CF condition (d)
requires only real + even + lower-bounded + simple lowest eigenvalue. None of these references the Euler
product. The D-H completed function is real on the critical line (built from real Dirichlet L-functions with a
zeta-type functional equation), so its Weil distribution is real and its even symmetrization is even. The
archimedean theta-density term is IDENTICAL to zeta's (shared Gamma-factor), and it dominates for small lambda
(Yoshida-type lower-boundedness is archimedean-sourced and D-H-shared), so the form is generically
lower-bounded with a simple even ground state at finite cutoff. Therefore the CF engine produces a
self-adjoint D' and, by Thm 5.10(iii) applied verbatim, **all zeros of xihat_lambda^{DH} are real at every
finite cutoff, unconditionally.** The finite-cutoff reality theorem is D-H-blind: it manufactures on-line
zeros for the D-H form exactly as for zeta. This is the K2 firewall passing through the finite machine
untouched -- consistent with e3s and LEARNINGS #153/#154.

**Where it MUST break: the Section-7 uniform limit (not before).** D-H's completed function Xi_DH has genuine
off-line zeros (near 0.808 + 85.7 i). But every finite-cutoff xihat_lambda^{DH} has only real zeros. By the
Hurwitz contrapositive, a sequence of entire functions with only real zeros cannot converge uniformly on an
open strip to a function with a complex zero. Therefore the D-H analogue of the Section-7 convergence
xihat_lambda^{DH} -> Xi_DH **provably fails to be uniform** somewhere in Im(z) < 1/2 -- the failure must
localize near the off-line zero height gamma ~ 85.7. The discrimination is thus **quarantined entirely to the
uniform-limit step**, exactly where zeta's own open obstacle sits, and nowhere in the finite construction.

**Honest caveats on the transplant (what could break earlier, and why it probably does not):**
- **Pole term:** zeta's construction uses the s = 0, 1 pole contribution (eq 3.11); D-H, being entire, lacks
  it. A faithful transplant must drop or reinterpret that term. This is a cosmetic difference, not a K2
  discriminator (it is a rank-<=2 modification of the form).
- **Lower-boundedness at large lambda:** for zeta, global lower-boundedness of QW_lambda for ALL lambda is
  RH-equivalent (Bombieri-Weil); for D-H it is FALSE (D-H fails its own Weil positivity). So the D-H form is
  expected to develop a negative eigenvalue as lambda grows past the scale that resolves gamma ~ 85.7
  (lambda^2 ~ gamma/2pi ~ 13.6, i.e. lambda ~ 3.7). Below that scale the CF gate runs; above it the "even
  simple lowest eigenvalue" hypothesis may be where the machine first stumbles for D-H. This is the
  concrete, cheap ADVERSARY probe: build QW_lambda^{DH} and watch the lowest eigenvalue's sign/simplicity as
  lambda crosses ~3.7 (the archimedean stealth-window suppression e^{-(pi/4) d gamma} ~ 1e-30 near gamma ~
  85.7 means the finite reality is preserved to enormous precision; the break is a large-lambda / uniformity
  phenomenon, not a finite-cutoff one, requiring lambda^2 >~ gamma_0/2pi to even see it).
- **Simplicity (Remark 2.3):** if the D-H lowest eigenvalue degenerates (non-simple) at some cutoff, Thm
  5.10(iii) does not apply as stated and only the radical-intersection reality survives. This is a genuine
  place the D-H machine could diverge from zeta's before the limit, but there is no a-priori reason it does
  at small lambda.

**Net feasibility verdict.** The D_log machinery is **transplantable onto D-H at every finite cutoff**: the
CF self-adjointness gate is input-agnostic (K2 = CF does not discriminate), and the finite-cutoff reality
theorem is unconditional and D-H-blind. Nothing in the finite construction distinguishes zeta from D-H. The
entire discrimination is deferred to, and must appear as a failure of, the Section-7 uniform limit -- which is
also zeta's sole open step. This is the sharpest possible statement of "finite reality is information-free":
the D-H twin is a clean testbed for a convergence-failure signature at gamma ~ 85.7, and the machine's inability
to separate zeta from D-H before the limit is a feature of, not a bug in, the D-H discipline.

---

## Project mapping (verdict lives in the dossiers)

- **Proven unconditional:** the operator D_log^(lambda,N) exists and is self-adjoint (Thm 1.1(i) / 5.10(i),
  via CF engine 23257 Thm 1.2); the exact determinant identity det_reg = -i lambda^{-iz} xihat (Thm
  5.10(ii)); finite-cutoff reality of all determinant zeros (Thm 5.10(iii)); the CF distributional theorem
  (23257 Thm 6.1); Lemma 7.3 (khat_lambda -> Xi). Assumed (per cutoff): even-simplicity of the lowest QW
  eigenvalue.
- **The gap (= RH):** xi_lambda ~ k_lambda (Section 7, "main remaining obstacle") => xihat_lambda -> Xi
  uniformly on substrips of Im(z) < 1/2 => RH by Hurwitz. Equivalent to uniform ground-state control of the
  truncated Weil form = global Weil positivity with a rate = M4 in yet another costume.
- **R3.5 / K1 (from LEARNINGS #154, unchanged by this fetch):** the wall is MET, not escaped, at exactly the
  Section-7 step. The perturbation vector is the Weil form's OWN variational (ground-state) vector, not an
  external geometric sign source, so the geometric-positivity escape clause is NOT walked. Condition (dagger)
  of `ccm_semilocal_prolate.md` Section E is retired (metaplectic operator bypassed); the live escape
  condition is (double-dagger): a zero-free, geometry-sourced proof of the uniform (N, lambda) -> inf control
  not routed through global Weil positivity.
- **D-H discipline (K2):** the finite machine passes D-H through untouched (this note, part f). The
  discrimination is quarantined to the uniform limit. This CONFIRMS and sharpens e3s / #153 / #154.
- **Determinant-class ledger (W6-vs-#143 gate, #154):** NOT a W6 hit; a determinant-class shell around a #143
  (CF self-adjointness) core -- exact at finite cutoff, but the spectral side runs through the argmin of the
  truncated Weil form (a variational, positivity-sourced step), not a symmetry computation. At this family the
  W6 upgrade and the M4 statement coincide, verbatim the Section-7 bridge.

## References (fetch-verified unless marked)

- **arXiv:2511.22755** (Connes-Consani-Moscovici, *Zeta Spectral Triples*): fetch-verified in full (PDF,
  34 pp). Theorem 1.1 (p.2), Weil form eqs 3.8-3.20 (pp.6-8), D_log Section 5.1-5.6 (pp.18-24), Theorem 5.10
  (p.23), numerics Section 6 (pp.25-26), Outlook Section 7 (pp.27-31).
- **arXiv:2511.23257** (Connes-van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral
  Action*): fetch-verified in full (PDF, 26 pp). Abstract + Corollary 1.1 + Theorem 1.2 (pp.1-2), Toeplitz
  Props 2.1-2.2 + Remark 2.3 (pp.3-4), continuous Theorem 3.1 (p.4), quadratic-form normal form Props
  4.1/4.2 + eq (11) (pp.7-8), spectral-action link Section 4.3 (p.9), finite even case Lemmas 5.1-5.3 (pp.9-10).
- Internal cross-refs (bibliographic, previously read): 2106.01715 (zeta-cycles), 2112.05500 /
  Connes-Moscovici PNAS (prolate UV), 2310.18423 (semilocal), 2602.04022 (survey), 2605.20224 (Groskin
  numerics). Reference [7] of 22755 = 23257 (the CF engine); reference [4] = the earlier realization paper
  carrying the educated guess k_lambda; reference [9] = the prolate special-function estimate (Meixner/Flammer
  style) used in Lemma 7.2.

## What this enables / what remains open

- **For BUILDER:** the operator is now fully specified for an mpmath reimplementation (part a recipe). The
  cheap, high-value build: assemble QW_lambda^N via eq (3.19), extract xi, form xihat via eq (5.25), verify
  Thm 5.10(iii) (real zeros) and the zeta-zero match (Section 6 table, e.g. lambda = sqrt(13), N = 120 gives
  the 50-zero error profile 2.44e-55 -> 2.04e-3). This is a faithful, non-surrogate build of CCM's actual
  new object (unlike the e1f-e1j surrogates, which built the deferred metaplectic route the 2511 family
  bypasses).
- **For ADVERSARY (the two cheap probes from #154, now spec'd):** (i) **CF-on-D-H:** build QW_lambda^{DH}
  with the D-H log-derivative stream Lambda_DH(n) (no Euler product => support on all n <= lambda^2, drop the
  pole term), run the CF gate, and confirm it produces real determinant zeros at finite cutoff (predicted:
  YES, D-H-blind) while the lowest eigenvalue loses simplicity or lower-boundedness as lambda crosses ~3.7
  (lambda^2 ~ gamma_0^{DH}/2pi ~ 13.6). (ii) **D-H twin as Section-7 convergence-failure testbed:** track
  where xihat_lambda^{DH} fails to converge uniformly to Xi_DH near gamma ~ 85.7 (needs lambda^2 >~ 13.6 to
  resolve; archimedean stealth suppression ~1e-30 means the finite reality is preserved to extreme precision,
  so the failure is a uniformity/rate phenomenon).
- **Open (theirs and ours):** the Section-7 uniform limit xihat_lambda -> Xi (uniform on closed substrips of
  Im(z) < 1/2), which is simultaneously CCM's "main remaining obstacle," the project's #148 determinant-class
  clause, M4 restated as uniform truncated-Weil ground-state control, and the sole place the zeta-vs-D-H
  discrimination can live. The door is wall-met-at-one-step: the eigenvalue budget, the operator, the
  determinant, and the finite reality are all installed and exact; only the uniform-limit control -- an
  RH-equivalent positivity with a rate -- remains.
