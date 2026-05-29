# Reading notes: Deninger, *Motivic L-functions and regularized determinants II*

> Highest-priority source for the live front (Direction 4.6 -> 8). Entry in the
> reference-library read-through ([`references/README.md`](../../../references/README.md)).
> Its content is, almost line for line, the object the program is trying to build:
> a cohomology `H^1(Y, F(Q(0)))` whose `Theta`-eigenvalues are exactly the non-trivial
> zeros of the Dedekind/Riemann zeta function, the completed zeta as a regularized
> determinant `prod_i det_inf((s - Theta)/2 pi | H^i)^{(-1)^{i+1}}`, the section 3.7
> statement of the 2K product-surface gap in Deninger's own words ("not over an
> absolute base point"), and the section 6 orthogonal-motive root-number computation
> that is the Direction-8 SIGNATURE mechanism (a skew-adjoint shift of `Theta` on a
> perfect alternating cup-product pairing forces the order of vanishing to be even,
> hence the sign `+1`). Mapped to 2Q, 2R, 2K, 2I and to Direction 4.6, Direction 8.
> Pages refer to the PDF in `references/02_deninger_program/`.

## One-line takeaway

Deninger's `H^1(Y, F(Q(0)))`, whose generalized `Theta`-eigenspaces have eigenvalues
the non-trivial zeros of `zeta_k`, together with the completed zeta as the regularized
determinant `L-hat(M, s) = prod_{i=0}^{2} det_inf((s - Theta)/2 pi | H^i(Y, F(M)))^{(-1)^{i+1}}`
(formula 3.8), IS the object Direction 4.6 must construct. 2R realized its spectrum (a
dynamical zeta with orbit lengths `{log p}` and log-derivative `-zeta'/zeta`); Deninger
specifies the cohomology that spectrum should be the spectrum OF. Section 3.7 states the
2K / 2Q product-surface gap verbatim ("fibre products over the generic point spec Q, not
over an absolute base point"). Section 6 is the Direction-8 signature mechanism: on a
perfect alternating cup-product pairing the operator `Theta - (n+1)/2 . id` is skew-adjoint,
which forces the order of vanishing `r_sigma` to be even, hence the global root number
`w(M) = +1`. That sign-from-a-pairing step is the part 2R does NOT supply.

## Technical content (section by section)

**Section 0, Introduction (p.1).** States the central wish: "the `H^1` of the space
associated to spec `Z` u {inf} in this new geometry would carry a canonical automorphism
whose eigenvalues would be the non-trivial zeros of the Riemann zeta function.
Mathematicians have been looking for such an operator since the time of Hilbert, but no
really satisfactory construction has been found." The only guidelines come from interpreting
analytic-number-theory assertions cohomologically. Deninger is explicit that "rather little
is proved and the assertions often involve quantities for which there is as yet no rigorous
definition," published only "in view of the fantastic impact the searched-for cohomology
theory would have." This is the Hilbert-Polya target plus its honest caveat.

**Section 1, Preliminary comments on [De1] section 7 (pp.2-3).** Two cautions that match the
project precisely. First, Deninger expects only an action of the SEMIGROUP `T^+ = (R^{>=0}, +)`
on the arithmetic site, NOT the group `(R, +)`, "because explicit formulas in analytic number
theory take the form of a Lefschetz trace formula only if we restrict attention to test
functions with support on `R^+`" (citing Deninger-Schroeter 3.2.3). `Theta` is the
infinitesimal generator of this semigroup action. Second, the space `Y = Y_k` associated to
`spec(O_k) u {p | inf}` is analogous to `Y = Y_0 (x)_{F_q} F-bar_q` for a curve `Y_0 / F_q`,
with `T^+` corresponding to the Frobenius semigroup `Z^+ = {Fr_q^nu | nu >= 0}`. `Y` "is
expected to be highly singular in the points corresponding to the archimedean places," so
`H^i(Y, j_* M)` is really INTERSECTION cohomology (1.1), which is why Poincare duality and the
weight theory survive. The Dedekind-zeta target is then stated (p.3, from [De1] 7.9, 7.10):
`H^0(Y, F(Q(0))) = C(0)`, `H^2(Y, F(Q(0))) = C(-1)` via the trace, and **`H^1(Y, F(Q(0)))`
decomposes into the finite-dimensional generalized eigenspaces `lim_N Ker(Theta - rho . id)^N`
with eigenvalues `rho` the non-trivial zeros of `zeta_k(s)`** (with multiplicities), where the
generator acts on `C(s)` by `Theta_{C(s)} = -s . id`.

**Section 2, Ext-groups, K-theory, and the prospected cohomologies (pp.3-4).** For a finite set
of places `S`, `Y_S = Y \ S`, and the functor `F: MM_{Y_S} -> {sheaves on Y_S}` is exact,
inducing maps on extension groups `F: Ext^nu(Q(0), M) -> Ext^nu(F(Q(0)), F(M))^{Theta ~ 0}`
(2.1). When `S` contains all infinite primes these are expected to be isomorphisms after
tensoring with `C` (2.2-2.4):
`F: Ext^nu_{MM}(Q(0), M) (x) C -> H^nu(Y_S, F(M))^{Theta ~ 0}`. The Beilinson-type translation
(2.5) reads motivic cohomology `H^i_M(X, C(n)) = Gr^n_gamma K_{2n-i}(X) (x) C` as
`H^i(X, C(n))^{Theta ~ 0}`, equivalent in the characteristic-p case to Tate's conjecture.

**Section 3, the Artin conjecture, weights, and the product gap (pp.4-5).** The L-series is a
product of regularized determinants over `H^0, H^1, H^2` (3.1, made global in 3.8). **Weights
3.6**: the real parts of the `Theta`-eigenvalues on `H^nu(Y, F(N))` are `(w + nu)/2` for `w` a
weight of `N`; this is the structural source of RH (`Re rho = 1/2` is the `H^1`, weight-0,
`nu = 1` case). **The regularized-determinant form (3.8)**, the precise 4.6 target:
`L-hat(M, s) = prod_{i=0}^{2} det_inf((s - Theta)/2 pi | H^i(Y, F(M)))^{(-1)^{i+1}}`.
The completed L is the `H^1` determinant divided by the `H^0 . H^2` determinants (the zeros
over the pole / archimedean factors), the function-field pattern lifted.

**Section 3.7 (the product-surface gap, in Deninger's own words).** Because `Theta` is a
DERIVATION for cup product (Leibniz), Kontsevich and Manin suggested looking for additive
relations `rho_1 + rho_2 = rho_3` among zeros of the Hasse-Weil zetas of `X, Y, X x Y`. The
cup product gives pairings
`H^i(Y, F(H^p(X))) (x) H^j(Y, F(H^q(Y))) -> H^{i+j}(Y, F(H^p(X) (x) H^q(Y)))`, and (3.2),
(3.3) imply the only `Theta`-eigenvalues on `H^0` and `H^2` are integers, so the only
forced additive relations are among zeros and POLES (where at least one `rho_i` is an integer
pole). "No non-trivial such relations were found by the computer in examples though." The
stated reason (the verbatim gap): **"The deeper reason why we don't get interesting relations
between three zeroes in this way is of course this: the fibre products `X x Y` are taken over
the generic point spec Q of the curve `Y` and not over an absolute base point."**

**Section 4, explanations for Deligne-Scholl critical-motive conjectures (pp.6-8).** A motive
`M` is critical iff the L-factors at infinity `L_inf(M, s)` and `L_inf(M^*(1), s)` have no
pole at `s = 0`, equivalently `F_inf^R(M)^{Theta = 0} = 0` and `F_inf^R(M^*(1))^{Theta = 0} = 0`
(4.1), equivalently (4.6) the map `H^1_c("spec Z", F(M))^{Theta ~ 0} -> H^1(Y, F(M))^{Theta ~ 0}`
is an isomorphism and the boundary `H^0, H^2_c` vanish. Scholl's "highly critical" condition
`Ext^i_{MM_Z(E)}(E(0), N) = 0` for `i = 0, 1` translates into (4.9-4.10). Remark (4.11): for
critical `M`, `L(M, 0) = c . det_Q I_inf^+(M)`, the Beilinson conjecture, and a "principle
relating the regularized `det_inf` on infinite-dimensional spaces to the finite determinant
`det_Q I_inf^+(M)` up to powers of `2 pi` and rational factors remains to be found." This is
the same finite-vs-infinite determinant puzzle ("observed before in physics, the mechanism
remains unclear").

**Section 5, an asymmetry between finite and infinite places (pp.8-9).** The conjecture
`Ext^2_{MM_Z}(Q(0), M) = 0` (so `Y \ inf` is an "affine curve" with vanishing `H^2`) is shown
to be COMPATIBLE with `Ext^2_{MM_{Y_p}}(Q(0), Q(1)) != 0` (5.1-5.3): the discrepancy is exactly
that `inf` is a singular point of `Y`, so `F(Q(0)) != C_{Y_p}` and the Ext-group is not the
cohomology of `Y_p`. The model computation (5.4-5.7) on an affine curve `X_0 / F_q` with one
node `inf` (two `F_q`-points of `A^1` glued) gives `Ext^2_X(j_* Q_l, j_* Q_l(1))^{Fr_q} != 0`
while the smooth `Ext^2 = 0`, exhibiting the singularity-at-infinity mechanism concretely.

**Section 6, the sign in the functional equation of an orthogonal motive (pp.10-12). THE
SIGNATURE MECHANISM.** Let `M` be a pure orthogonal motive of weight `n` over `K` with
coefficients `E`: there is a symmetric morphism `S: M (x) M -> E(-n)` inducing `M^* = M(n)`.
Write `L-hat(M, s) = eps(M, s) L-hat(M^*, 1 - s) = eps(M, s) L-hat(M, n + 1 - s)`, root number
`w(M) = eps(M, (n+1)/2)`, so `w_sigma(M) = (-1)^{r_sigma}` with
`r_sigma = ord_{s = (n+1)/2} L-hat(M, s)_sigma` (6.1). Taking sigma-components of 3.8 and using
the weight statement 3.6 (the `Theta`-eigenvalues on `H^i` have real part `(n + i)/2`, so the
center `(n+1)/2` lives in `H^1`):
`r_sigma = dim_C H^1(Y, F(M))_sigma^{Theta ~ (n+1)/2}` (6.2). The decisive structure: the
cup-product pairing
`[ , ]: H^1(Y, F(M))_sigma x H^1(Y, F(M))_sigma -(cup)-> H^2(Y, F(M (x) M))_sigma -(S)->
H^2(Y, F(E(-n)))_sigma = C(-n-1)`
is "perfect (in the sense of [De1] 7.19) and alternating." Since `Theta` satisfies the Leibniz
rule with respect to cup product, `[Theta h, h'] + [h, Theta h'] = (n+1)[h, h']`, so the shifted
operator `Theta - (n+1)/2 . id` is SKEW-ADJOINT with respect to `[ , ]`. Hence the induced
alternating pairing on the generalized eigenspace
`H^1(Y, F(M))_sigma^{Theta ~ (n+1)/2} x H^1(Y, F(M))_sigma^{Theta ~ (n+1)/2} -> C(-n-1)^{Theta ~ n+1} = C`
is again perfect, so by (6.2) the dimension `r_sigma` "must be even. It follows from (6.1)
that `w_sigma(M) = 1` for all sigma and hence that `w(M) = 1`." This is the cohomological
proof that the global root number of an orthogonal motive is `+1` (compare T. Saito's [S]),
and it is the template for "positivity / sign from a perfect cup-product pairing on `H^1`,"
i.e. the Direction-8 signature.

**Section 7, `Ext^nu(C(0), C(s))` and the symplectic pairing at the center (pp.12-13).**
Conjectures a category `NM_{O_k}` of "motives with C-coefficients" where a zero `rho` of
`L(M, s)` gives a non-trivial extension. The special case that matters: the formalism implies
`V_k = H^1(Y, F(Q(0)))^{Theta ~ 1/2}` is a finite-dimensional space with a SYMPLECTIC pairing
`cup: V_k x V_k -> H^2(...)^{Theta ~ 1} = C` coming from Poincare duality, and
`dim V_k = ord_{s = 1/2} zeta_k(s)`. By the functional equation `zeta_k` vanishes to EVEN order
at `s = 1/2` if at all (consistent with `V_k` being even-dimensional / symplectic). Suggestion
(7.2-7.3): to `k` should be associated a finite-dimensional `V_k` with a symplectic pairing
`cup: V_k x V_k -> CH^1(Y_k)_C -(deg)-> C` such that `ord_{s = 1/2} zeta_k(s) = dim V_k`, the
construction of `cup` to "use the arithmetic of the ring of integers." This is the
center-of-the-strip avatar of the section-6 signature.

**Section 8, the algebra of correspondences (pp.13-14).** The correspondences on `Y` should
form a `C^*`-algebra Corr(`Y`); the `T^+`-action gives `sigma: T^+ -> Corr(Y)`,
`sigma_{t_1 + t_2} = sigma_{t_1} o sigma_{t_2}`, with a convolution algebra `C(T^+)` of test
functions mapping in by `Lambda(phi) = int_0^inf phi(t) sigma_t dt`. By a Titchmarsh result
`C(T^+)` has no zero divisors / no idempotents except 1, so the action "induces no exotic
decompositions of cohomology." Deninger recalls Deligne's observation (from the Lefschetz
formula of [De1] 7.2) that a correspondence must be MORE than a cycle (else `Theta_sigma`
would act as the identity since its support reduces to the diagonal), connecting to
Gillet-Soule (a cycle as a current). The `(2 pi i)/log q`-periodicity of the poles of the
finite L-factor is visible in `[Theta_q, z] = (2 pi i / log q) z` on `H^w(X/L)`, but in the
number-field case `H^0(Y, F(Q(0)))` is only a C-module structure on `H^1` and `Theta` is
C-linear, "so that nothing follows for the eigenvalues" (the absence of an a-priori periodicity
over `Q` is the structural difference from the function-field case).

**Section 9, relations with Selberg's class (pp.14-16).** Speculates a category Perv(`Y`) of
perverse sheaves on the singular curve `Y`, with `0-Perv^{gen}(Y)` the semisimple subcategory
of generic weight-0 objects. For `F` in it, `F(s) = L(F, s)` defined by the same regularized
determinant should lie in Selberg's class `S`, with `n_F = dim End_Y(F)`, so `dim End_Y(F) = 1`
(simple object) corresponds to a primitive function, and the orthogonality of distinct
primitive functions to `Hom_Y(F_1, F_2) = 0` for non-isomorphic simple sheaves. The functor
`F: 0-M_Q (x) C -> 0-Perv^{gen}(Y)` is fully faithful (granting 2.2), so `F(M)` is simple iff
`End M = Q`.

**Section 10, tentative remarks on constructions (pp.16-17).** The (intersection) cohomologies
`H^i(Y, F(Q(0)))` "look like singular cohomology with coefficients in C of a compact oriented
surface of infinite genus," singular at the infinite primes. The space associated to a finite
prime `p` (i.e. `spec(O_k / p)`) should be `R / log Np . Z = S^1_p` with its sheaf of
real-algebraic sections and the `T^+`-action by translation; the space associated to an
infinite prime should be `R^+` (NOT `R`), with `C_p = L_p^+` as `T^+`-modules. The closed point
`x_0 in X_0` "is" the `Fr_q`-orbit of `x | x_0`; the analogue is that `p` "is" the `T^+`-orbit
`R / log Np . Z` (resp. `R^+`). "Suitable von Neumann algebras of type III are such structures,
disregarding inner automorphisms" (the explicit bridge to the Connes / Leichtnam type-III
picture). Strikingly, in connection with Ruelle's zeta function "there also appears the
regularized determinant of the infinitesimal generator of the induced flow on cohomology" (the
2R dynamical-zeta object).

## Points mapped to the project

1. **The 4.6 target stated verbatim (section 1 / section 3).** `H^0 = C(0)`, `H^2 = C(-1)`,
   and `H^1(Y, F(Q(0)))` = the generalized `Theta`-eigenspaces with eigenvalues the
   non-trivial zeros of `zeta_k`, completed zeta `=` the regularized determinant 3.8. 2R gave
   the spectrum side (`-zeta'/zeta`, orbit lengths `{log p}`); this is the `H^1` that spectrum
   should be the spectrum of, and the `H^0 / H^2` give the pole / `C(-1)` (the `B_pole` block
   of 2K).
   -> Direction 4.6's `det_zeta(s - Phi_t | H^*_{F,pr})` is Deninger's 3.8; build the `H^1`.

2. **The semigroup caution = 2Q's one-sided Frobenius (section 1).** `T^+ = (R^{>=0}, +)`, not
   the group, "because explicit formulas take the Lefschetz form only for test functions
   supported on `R^+`." This is exactly the flow `Phi_t = prod_p U_{log p}^{t / log p}` forced
   by 2Q and the test-function restriction in the Weil-form work; the analytic shadow of 2Q's
   place-dependent bidegree (a one-sided Frobenius semigroup `{Fr_q^nu | nu >= 0}`).
   -> Treat the semigroup, not group, as settled: it is forced by the explicit formula's
   support condition, independently of the project's bidegree argument.

3. **The archimedean singularity = 2I / 2K (section 1, section 5).** `Y` is singular at the
   infinite primes, so `H^i(Y, j_* M)` is intersection cohomology, and the finite-vs-infinite
   asymmetry (section 5) is precisely "inf is a singular point." This is the home for 2I's
   `lambda_inf` (the archimedean local height / Gamma-factor) and matches the project's #23
   (the surface must be compactified / singular at infinity; positivity is global).
   -> 2I's archimedean block lives in the intersection cohomology at the singular point;
   section 5's node computation is the concrete model.

4. **Section 3.7 = the 2K / 2Q product-surface gap, verbatim.** "The fibre products `X x Y`
   are taken over the generic point spec Q of the curve `Y` and not over an absolute base
   point." The missing absolute base point is `Spec(F_1)`; `X x_Q Y` is not the product surface
   `Spec(Z) x_{F_1} Spec(Z)`. Deninger NAMES the exact obstruction the program calls "the one
   missing object," and confirms a computer search for the naive additive relations
   `rho_1 + rho_2 = rho_3` came up empty (the structure is invisible at `x_Q`, only over the
   absolute base).
   -> Cite 3.7 as the literature statement of the 2K gap. The Connes-Consani square (char-1
   tensor square over the Boolean base `B`) is one candidate "absolute base"; the gap there is
   a signed pairing, the gap here is the base point itself. Same missing object from two sides.

5. **Section 6 = the Direction-8 signature mechanism.** The cup-product pairing
   `H^1 x H^1 -> H^2 -> C(-n-1)` is perfect and alternating; `Theta` is a derivation (Leibniz),
   so `Theta - (n+1)/2 . id` is skew-adjoint; the induced pairing on the central eigenspace is
   perfect; hence `r_sigma` is EVEN and `w(M) = +1`. This is positivity / sign from a perfect
   cup-product pairing on `H^1`, the exact thing 2R does NOT supply (only the spectrum) and
   Direction 8 needs. The center-of-strip avatar (section 7) is the symplectic pairing on
   `V_k = H^1(Y)^{Theta ~ 1/2}` with `dim V_k = ord_{1/2} zeta_k`.
   -> Direction 8's job is to put exactly this perfect alternating cup-product pairing (with a
   controlled Hodge-* signature) on the `H^1` of the missing surface. The mechanism is known;
   the surface carrying it is the gap. Note this is the same `Theta`-as-derivation that, in
   Deninger I section 1, controlled the sign via the eta-invariant `sdim_inf`: section 6 is the
   pairing-level realization of Deninger I's trace-level sign.

6. **Finite-vs-infinite determinant puzzle (4.11) stays open.** Even granting 4.6, the bridge
   from the regularized `det_inf` to a COMPUTABLE finite determinant `det_Q I_inf^+(M)` "up to
   powers of `2 pi` and rational factors" is itself unsolved ("the mechanism remains unclear").
   -> Relevant if we ever try to make 4.6's determinant numerically checkable beyond the
   Euler-product piece 2R already did.

7. **The local space is `R^+` / `S^1_p`, and "type-III von Neumann algebras are such
   structures" (section 10).** Deninger himself points at the type-III picture and at the
   Ruelle-zeta regularized determinant of the induced flow on cohomology.
   -> This is the explicit pointer from Deninger to Leichtnam 2006 / Connes: the `T^+`-orbit
   over a prime is `R / log Np . Z` (finite) or `R^+` (infinite), realized by a type-III flow.
   2R's dynamical zeta is the Ruelle zeta Deninger names here.

## What this changes for the program

- **2Q / 2R are confirmed as the right reduction.** Deninger independently arrives at the
  semigroup / flow, the `{log p}` orbit / Frobenius structure, the archimedean singularity, and
  the regularized determinant. 2R's dynamical zeta is the spectrum of his `H^1`; 2Q's bidegree
  is his one-sided Frobenius semigroup. External validation that the session-005 work points
  correctly.
- **The 4.6 target is now precise: build the `H^1` of formula 3.8.** Not a spectrum (2R has
  that) but a cohomology with a perfect alternating cup-product pairing on which `Theta` is a
  derivation.
- **The gap is sharpened identically (3.7) and the signature mechanism is named (section 6).**
  Section 3.7 is the 2K "absolute base point" / product-surface gap in Deninger's words;
  section 6 is the Direction-8 cup-product signature on `H^1` that 2R does not reach. The two
  together say: the missing object is a surface (over an absolute base) carrying a perfect
  alternating `H^1`-pairing whose Hodge-* signature is controlled.
- **The sign / eta of Deninger I is realized at the pairing level here.** Deninger I section 1's
  `sdim_inf` / eta-invariant (the trace-side signature governing the functional-equation sign)
  becomes, in section 6, the skew-adjointness of `Theta - (n+1)/2` on the cup-product pairing.
  This is the cleanest available statement of how the trace-side sign and the signature pairing
  are the same structure seen two ways.

## Actionable

- Study section 6 as the concrete signature template: a perfect alternating cup-product pairing
  on `H^1`, `Theta` a derivation, skew-adjoint shift forcing even order. Any Direction-8
  construction (e.g. on the Connes-Consani square or a future product surface) must reproduce
  this pairing with a Hodge-* signature; the marginal-positivity thesis says this pairing is
  the whole game.
- Cross-link 3.7 (this paper) with the Connes-Consani square note: both name the missing
  "absolute base point" / product surface, from the motivic side (Deninger: `x_Q` is wrong) and
  the char-1 side (Connes-Consani: the Boolean base `B` supplies it but the operations are
  idempotent, no signed pairing). The Direction-8 statement is the intersection of the two.
- Next read in program order: Deninger I (the local `F_p(M)` and `det_inf` construction, now
  done), then Leichtnam 2006 (a Lefschetz trace formula for laminated spaces built for exactly
  this `H^1`), then Alvarez-Lopez-Kordyukov-Leichtnam 2017 (the general foliated-flow trace
  formula and Hodge decomposition that 4.6 needs).

## Status

Read deeply: pp.1-19 (all of it). Section 0 introduction (the Hilbert-Polya target + caveat);
section 1 the semigroup `T^+` caution, the archimedean singularity / intersection cohomology,
and the Dedekind-zeta target `H^0 = C(0)`, `H^2 = C(-1)`, `H^1` = zeta-zero eigenspaces; section
2 the Ext / K-theory translation; section 3 weights 3.6, the regularized determinant 3.8, and
the section-3.7 product-surface gap verbatim; section 4 the critical-motive / Beilinson
explanations and the finite-vs-infinite determinant puzzle 4.11; section 5 the finite-infinite
asymmetry and the node model 5.3-5.7; ALL of section 6 (the orthogonal-motive root-number proof:
the perfect alternating cup-product pairing, `Theta - (n+1)/2` skew-adjoint, `r_sigma` even,
`w(M) = +1`); section 7 the central symplectic pairing on `V_k` with `dim V_k = ord_{1/2}
zeta_k`; section 8 the correspondence algebra and Deligne's "more than a cycle"; section 9
the Selberg-class / perverse-sheaf speculation; section 10 the `R^+` / `S^1_p` local spaces and
the type-III / Ruelle-zeta pointer; the reference list. Honest depth: sections 1, 3, 6, 7, 10
(the on-front material) are understood at the statement level with the key arguments traced;
sections 2, 4, 5, 8, 9 (the Ext / K-theory and Selberg-class speculations) are understood at the
statement level, with the finest motivic-Ext computations summarized rather than re-derived.
