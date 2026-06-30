# Narration script: Episode 2, "The Functional Equation"

Graduate course on the Riemann Hypothesis. Spoken-narration script for the
episode in `functional_equation.py`. The video shows this narration as on-screen
subtitles, so it plays as a self-contained silent video. This document is for
recording a voiceover or reading along, and it records the precise theorem
statements behind each beat.

- Audience: graduate (complex analysis, Poisson summation, the Gamma function).
- Pronunciation: "Euler" is "Oiler"; "psi", "theta", "xi", "Lambda" are the Greek letters.
- Run time about 11 minutes.
- Render commands: see the module docstring in `functional_equation.py`.

---

## Where this episode sits (the course)

1. The Euler Product and Analytic Continuation: zeta as a Dirichlet series and Euler product, absolute convergence on Re(s)>1 as the analytic shadow of unique factorization, the simple pole at s=1, a first continuation into Re(s)>0 via the Dirichlet eta series.
2. **The Functional Equation (this episode):** theta and Poisson summation, the modular law theta(1/x)=sqrt(x) theta(x), Riemann's symmetric integral, meromorphic continuation, Lambda(s)=Lambda(1-s), the entire xi, the asymmetric form, trivial zeros, the critical strip.
3. The Explicit Formula: the Hadamard product for xi, the logarithmic derivative -zeta'/zeta, and the Riemann-von Mangoldt explicit formula linking a sum over primes to a sum over the nontrivial zeros.
4. Counting the Zeros, N(T): the argument principle on a box, N(T) = (T/2pi)log(T/2pi) - T/2pi + 7/8 + S(T), the density log(T/2pi)/2pi, and the oscillating term S(T).
5. Zero-Free Regions and the Prime Number Theorem: non-vanishing on Re(s)=1 via the 3+4cos+cos2 trick, the de la Vallee Poussin region, the Vinogradov-Korobov widening, and PNT with error term.
6. RH-Equivalent Criteria: Li coefficients, Weil explicit-formula positivity, Nyman-Beurling, de Bruijn-Newman, with the Davenport-Heilbronn L-function as the structural counterexample any honest criterion must exclude.

## Prerequisites for this episode

- Complex analysis: analytic continuation, contour integration, residues, the identity theorem, Liouville.
- Basic Fourier analysis on the line, including Poisson summation and the Fourier transform of a Gaussian.
- The Gamma function: integral representation for Re(s)>0, the reflection formula, the Legendre duplication formula.
- From Episode 1: zeta as a Dirichlet series and Euler product on Re(s)>1, and its simple pole at s=1 with residue 1.

---

## Theorems established (the rigorous backbone)

- **T1 (given from Episode 1).** For Re(s)>1, zeta(s)=sum n^{-s}=prod_p (1-p^{-s})^{-1}, absolutely; in particular zeta(s) != 0 there. Zeta has a simple pole at s=1 with residue 1.
- **T2 (Mellin term identity).** For Re(s)>0, t = pi n^2 x gives pi^{-s/2} Gamma(s/2) n^{-s} = int_0^inf x^{s/2-1} e^{-pi n^2 x} dx.
- **T3 (Tonelli, definition of Lambda).** For Re(s)>1, Lambda(s) := pi^{-s/2} Gamma(s/2) zeta(s) = int_0^inf x^{s/2-1} psi(x) dx, with psi(x)=sum_{n>=1} e^{-pi n^2 x}.
- **T4 (Poisson summation, cited).** For Schwartz f, sum_{n in Z} f(n) = sum_{k in Z} f-hat(k).
- **T5 (Gaussian self-duality, cited).** The Fourier transform of e^{-pi x y^2} is x^{-1/2} e^{-pi xi^2/x}.
- **T6 (Jacobi theta transformation).** theta(x)=sum_{n in Z} e^{-pi n^2 x}=1+2 psi(x) satisfies theta(1/x)=sqrt(x) theta(x); equivalently psi(1/x) = -1/2 + (1/2)sqrt(x) + sqrt(x) psi(x).
- **T7 (symmetric representation and continuation).** For all s != 0,1, Lambda(s) = -1/s - 1/(1-s) + int_1^inf psi(x)(x^{s/2-1} + x^{(1-s)/2-1}) dx. The two elementary terms are derived on Re(s)>1 (where int_1^inf -(1/2)x^{-s/2-1}dx converges for Re(s)>0 and int_1^inf (1/2)x^{(1-s)/2-1}dx for Re(s)>1) and the closed forms continue everywhere. Since psi=O(e^{-pi x}), the surviving integral is entire; Lambda is meromorphic with simple poles only at s=0, 1.
- **T8 (functional equation, symmetric form).** Lambda(s)=Lambda(1-s), since the T7 right side is invariant under s -> 1-s.
- **T9 (completed entire xi).** xi(s) := (1/2)s(s-1)Lambda(s) = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s) is entire and xi(s)=xi(1-s).
- **T10 (asymmetric form).** zeta(s) = 2^s pi^{s-1} sin(pi s/2) Gamma(1-s) zeta(1-s) (from T8 via the Legendre duplication and Gamma reflection formulas).
- **T11 (zero classification).** Trivial zeros at s=-2,-4,-6,... (sin(pi s/2)=0, or the strictly negative even Gamma poles). NOT at s=0 (there the Gamma pole is matched by Lambda's own pole, and zeta(0)=-1/2). Zeta's only pole is the simple pole at s=1. Nontrivial zeros lie in the closed strip 0<=Re<=1; the open strip 0<Re<1 needs zeta != 0 on Re=1 (Episode 5). The zero set of xi is symmetric under rho -> 1-rho and rho -> conj(rho), hence symmetric about Re=1/2.
- **T12 (Riemann Hypothesis, open, stated only).** Every nontrivial zero has Re(rho)=1/2; equivalently every zero of xi lies on Re(s)=1/2. Asserted, not proved.

---

## Part I. The Theorem First

### Beat 1. The destination (3D)
[VISUAL] The 3D |zeta(s)| terrain: the pole spike at s=1, the nontrivial zeros as dips on the critical line, a slow rotation, then the mirror plane at Re=1/2. On screen: the xi formula and xi(s)=xi(1-s).

> Here is where this episode lands. The zeta function, defined by a series only for real part of s greater than one, extends to a meromorphic function on the whole plane. After multiplying by the right Gamma factor and a quadratic, we get an entire function, xi of s, perfectly symmetric under s going to one minus s. The pole sits at s equals one, the nontrivial zeros lie in the strip, and the functional equation forces them to be symmetric across the line real part one half. We will prove all of this exactly.

### Beat 2. What we start from (recap)
On screen: the series (Re(s)>1), the Euler product, residue 1 at s=1.

> We take three facts as given from the previous episode. The Dirichlet series converges absolutely for real part greater than one. There it equals the Euler product over primes, which already shows zeta has no zeros in that half-plane. And zeta has a simple pole at s equals one with residue one. The series and the product are useless past real part one, so we need a genuinely new representation that continues zeta and exposes the symmetry.

## Part II. The Gamma Factor Completes Zeta

### Beat 3. One Gaussian integral per term
On screen: Gamma(s/2) integral; t = pi n^2 x; pi^{-s/2}Gamma(s/2)n^{-s} = int_0^inf x^{s/2-1}e^{-pi n^2 x}dx.

> The whole proof begins with one substitution. In the integral for Gamma of s over two, replace t by pi n squared x. The measure dt over t is scale invariant, so it becomes dx over x, and the rest pulls out pi n squared to the s over two. Rearranging, pi to the minus s over two times Gamma of s over two times n to the minus s equals the integral of x to the s over two minus one times e to the minus pi n squared x. Each term of zeta now carries a Gaussian integral, and the Gamma and pi factors are forced on us, not decoration.

### Beat 4. Sum over n: the completed zeta
On screen: psi definition; Lambda definition; Lambda = int_0^inf x^{s/2-1} psi(x) dx (Re(s)>1).

> Now sum over all n at least one. On the left the terms assemble into pi to the minus s over two, Gamma of s over two, times zeta of s. We call this the completed zeta function, capital Lambda. On the right the sum of the Gaussians defines psi of x, the half theta function. Interchanging sum and integral is legal here, because for real part above one the integrand is positive and the iterated integral is finite, so Tonelli applies. The completed zeta is exactly the Mellin transform of psi.

### Beat 5. All the trouble lives near x = 0
[VISUAL] Plot of psi(x): tame e^{-pi x} decay for large x, blow-up as x -> 0, a cut marked at x=1.

> Look at the two ends. As x goes to infinity, psi is dominated by its first term and decays like e to the minus pi x, faster than any power, so the tail from one to infinity converges for every s and is already entire. All the analytic difficulty lives at the other end, near x equal to zero, where psi blows up. To control that end we need to know exactly how psi behaves as x goes to zero, and that is what the theta function will give us.

## Part III. Theta and Its Modular Symmetry (the engine)

### Beat 6. Pass to the full lattice sum
On screen: theta = 1 + 2 psi; Poisson summation; the Fourier transform convention.

> Extend the sum to all integers and add the n equals zero term. That is the Jacobi theta function, theta of x, equal to one plus two psi of x. Because the summand depends only on n squared, the negative terms double the positive ones and n equals zero contributes a lone one. Theta is a sum over the integer lattice, and the master tool for such sums is Poisson summation: the sum of f over the integers equals the sum of its Fourier transform over the integers. We apply it to the Gaussian f of y equal to e to the minus pi x y squared.

### Beat 7. The Gaussian is its own Fourier transform (the climax)
[VISUAL] Narrow Gaussian and its wide transform; the gold banner theta(1/x)=sqrt(x) theta(x).

> The Fourier transform of e to the minus pi x y squared is one over root x times e to the minus pi k squared over x. This is the one computation that makes everything work: the Gaussian is essentially its own transform, with x inverted to one over x and an amplitude root x out front. Feeding this into Poisson summation gives the modular law: theta of one over x equals root x times theta of x. The width inverts, narrow maps to wide, and this single law is the entire source of the symmetry we are after.

### Beat 8. Translate the law to psi
On screen: 1+2psi(1/x)=sqrt(x)(1+2psi(x)); psi(1/x) = -1/2 + (1/2)sqrt(x) + sqrt(x)psi(x).

> Restate the law in terms of psi, since psi is what appears in Lambda. Substitute theta equals one plus two psi on both sides and solve for psi of one over x. It equals minus one half, plus one half root x, plus root x times psi of x. Watch those two extra elementary terms, the minus one half and the one half root x. They come from the lone n equals zero term in theta, and they are exactly the algebra that will produce the two poles of Lambda.

## Part IV. The Symmetric Representation (continuation for free)

### Beat 9. Split at x = 1 and fold (0,1) over
On screen: the split; x -> 1/x; int_0^1 x^{s/2-1}psi dx = int_1^inf x^{-s/2-1}psi(1/x)dx.

> Split the Mellin integral at x equals one. The tail from one to infinity is already entire, so leave it. In the dangerous piece from zero to one, substitute x to one over x. The interval flips to one to infinity, the measure picks up the right power of x, and crucially psi of x becomes psi of one over x, where we can now feed in the modular law. This single substitution converts the divergent end into a convergent one.

### Beat 10. Insert the theta law; two terms integrate
On screen: the three-term integrand; the closed forms -1/s (Re(s)>0) and -1/(1-s) (Re(s)>1); the psi term with exponent (1-s)/2-1.

> Substitute the expression for psi of one over x. Three terms appear, all integrals over one to infinity. The constant minus one half integrates to minus one over s, for real part positive. The one half root x term integrates to minus one over one minus s, for real part greater than one. These are the only elementary integrals, and they are exactly where the two poles come from. The remaining term gives psi of x times x to the one minus s over two minus one. Notice the exponent: the substitution has sent s to one minus s. Every piece converges together on real part greater than one, where we performed the split.

### Beat 11. Riemann's symmetric formula: continuation for free
On screen: Lambda(s) = -1/s - 1/(1-s) + int_1^inf psi(x)(x^{s/2-1}+x^{(1-s)/2-1})dx; the integral is entire; poles only at s=0, 1.

> Assemble the pieces. Lambda of s equals minus one over s, minus one over one minus s, plus the integral from one to infinity of psi times the quantity x to the s over two minus one plus x to the one minus s over two minus one. We derived this for real part greater than one, but now read the right side on its own. Because psi decays like e to the minus pi x, that integral converges for every complex s and is entire. The two fractions are meromorphic with poles only at zero and one. By analytic continuation the right side equals Lambda everywhere. We have continued the completed zeta to all of C, essentially for free.

### Beat 12. The symmetry is now manifest
On screen: s -> 1-s; the fractions and the two x-powers are invariant; Lambda(s)=Lambda(1-s).

> Now the payoff. Send s to one minus s in the symmetric representation. The pair of fractions swaps with itself. Inside the integral, the two powers of x interchange, so the integrand is unchanged. Every single term is invariant. Therefore Lambda of s equals Lambda of one minus s. The functional equation is not a coincidence checked afterward: it is manifest in a representation we built symmetrically from the theta law. The mirror at real part one half was there all along.

## Part V. Harvest: xi, the Asymmetric Form, and the Zeros

### Beat 13. Clearing the poles: the entire function xi
On screen: xi(s) = (1/2)s(s-1)Lambda(s); xi entire; xi(s)=xi(1-s).

> Lambda has two simple poles, at zero and one. Multiply by one half times s times s minus one, which vanishes at exactly those two points and cancels both poles. Define xi of s to be one half s times s minus one times Lambda. Then xi is entire. The prefactor is itself invariant under s to one minus s, since s minus one maps to minus s, so xi inherits the symmetry exactly: xi of s equals xi of one minus s. This is the clean object promised at the start: a single entire function with a perfect functional equation.

### Beat 14. The asymmetric functional equation
On screen: the symmetric identity in zeta variables; zeta(s) = 2^s pi^{s-1} sin(pi s/2) Gamma(1-s) zeta(1-s).

> Unpack Lambda of s equals Lambda of one minus s into the zeta variables. Solving for zeta of s, and using the Legendre duplication formula and the reflection formula for Gamma to simplify the ratio of Gamma factors, gives the classical asymmetric form: zeta of s equals two to the s, times pi to the s minus one, times sine of pi s over two, times Gamma of one minus s, times zeta of one minus s. The two faces carry the same content, but the asymmetric form makes the consequences for the zeros immediate.

### Beat 15. Trivial zeros and the pole, read off
On screen: sin(pi s/2)=0 at s=-2,-4,...; Gamma(s/2) poles, zeta(0)=-1/2 != 0; only pole at s=1.

> Read the asymmetric equation at the negative even integers. There the sine factor vanishes while the other factors are finite and nonzero, forcing zeta to vanish. These are the trivial zeros at minus two, minus four, minus six, and on. Equivalently, Gamma of s over two has poles at zero and the negative even integers; at the strictly negative ones zeta must carry compensating zeros, the trivial ones. At s equals zero the story differs: there the Gamma pole is matched by Lambda's own pole, and zeta of zero is minus one half, not zero. The lone pole of zeta at s equals one matches the s equals one pole of Lambda.

### Beat 16. The critical strip, and the Riemann Hypothesis
[VISUAL] The complex plane: the shaded strip, the critical line, an off-line zero quartet rho, 1-rho, conj(rho), 1-conj(rho), then a collapse onto the line.

> Now isolate the remaining zeros. The Euler product gives none for real part above one, and the functional equation reflects that below zero, leaving only the trivial ones outside. So every nontrivial zero sits in the closed strip, real part between zero and one. Ruling out the two boundary lines needs one more input, the nonvanishing of zeta on real part equal to one, which we prove in Episode five. The symmetry xi of s equals xi of one minus s pairs each zero rho with one minus rho, and real coefficients pair rho with its conjugate, so the four points form a rectangle symmetric about the line real part one half.
>
> The Riemann Hypothesis is the assertion that this enforced symmetry is achieved on the nose: every nontrivial zero already sits on the critical line, real part exactly one half. We have proved the functional equation that frames the problem. Whether the zeros truly lie on the line is the open question this whole course exists to confront.

---

## Honesty ledger

Derived on screen end to end: the Mellin term identity and the Tonelli interchange (T2, T3), the Jacobi theta transformation (T6), Riemann's symmetric representation and the meromorphic continuation (T7), the symmetric functional equation Lambda(s)=Lambda(1-s) (T8), and the entire xi with xi(s)=xi(1-s) (T9).

Imported as cited classical inputs, stated with hypotheses but not re-proved: Poisson summation (T4) and Gaussian Fourier self-duality (T5). The asymmetric form (T10) uses the Legendre duplication and Gamma reflection identities (stated, not re-derived).

Subtlety flagged, not glossed: after folding (0,1) onto (1,infinity), the two elementary terms are integrals over [1,infinity), convergent for Re(s)>0 and Re(s)>1 respectively, so jointly on Re(s)>1, exactly where the split was performed; their closed forms -1/s and -1/(1-s) then continue to all s, supplying the poles at s=0 and s=1.

Inherited from Episode 1 as given (T1): the Euler product, non-vanishing on Re(s)>1, and the simple pole at s=1. The zero classification (T11) places the nontrivial zeros in the closed strip 0<=Re<=1; strict containment in the open strip needs zeta != 0 on Re=1 (Episode 5). The Riemann Hypothesis itself (T12) is stated, not proved: it is the open problem this course exists to confront.
