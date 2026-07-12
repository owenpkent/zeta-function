# The Landau one-sided route: the #145 residue developed into a translator, and its finite-lambda bridge

> Dossier, 2026-07-11. BUILDER+SURVEYOR draft, ADVERSARY-corrected in place (verdict
> PASS_WITH_FIXES; the L1 reconciliation, Section 3.6, is the adversary's). Promoted from the
> gitignored working file `scratchpad/prime_comb/02_opus_145_landau.md` per the repo pattern
> (dossier tracked, working files gitignored). Arc provenance: the LEARNINGS #145 one-sided
> residue (Stepanov engine audit, [`stepanov_engine_audit.md`](stepanov_engine_audit.md) S7 row)
> -> the #160 positivity-free surface (the Hamburger pin, e1m) -> the e1n prime-comb interlock
> ([`../../experiments/spectral/e1n_prime_comb.md`](../../experiments/spectral/e1n_prime_comb.md))
> -> the adversary reconciliation (Section 3.6 here; LEARNINGS #161).
>
> Status: Theorem A is PROVEN tier (classical; independently re-derived end to end in adversary
> review). The route is a TRANSLATOR, not a discriminator (Section 2). BRIDGE-H is CONJECTURE /
> spec tier with the transfer clause settled per layer (input: exact and vacuous; built object:
> false without an error term); the one surviving open sub-lemma is the lambda-uniform MECHANISM
> question (S4/R1 on the CCM carrier, Section 3.4/3.6). RE-RUN-NEEDED flags: von Koch
> converse (Section 1.4) remains open; Beurling off-line-zero existence (Section 2.2) was
> DISCHARGED 2026-07-11 (S4/R1 surveyor round, Revesz 2207.00665 fetched). Section 2.2's
> dictionary carries a dated ADVERSARY correction (real-zero caveat + reverse-arrow scope),
> 2026-07-11. No em dashes anywhere.

> Original working header: BUILDER+SURVEYOR dossier, 2026-07-11. Develops the "useful residue" of LEARNINGS
> #145 (the Stepanov engine audit): a ONE-SIDED bound `psi(x) <= x + O(x^{1/2+eps})`
> for every `eps > 0` already forces RH, via Landau's oscillation theorem. This note
> writes the theorem out to PROVEN tier, runs the D-H and Beurling mirror checks, and
> specifies the bridge to the #160 positivity-free surface (the finite-cutoff CCM comb).
> Runs in parallel with the e1n numerical probe (comb-error one-signedness); it does
> not touch any `experiments/` file. Self-contained.

## Executive summary (read this first)

1. THEOREM STATUS: PROVEN, classical. If `psi(x) <= x + C_eps x^{1/2+eps}` for every
   `eps > 0` (upper bound ONLY), then RH. Engine: Landau's oscillation theorem applied
   to `g(x) = x + C x^a - psi(x) >= 0` with `a = 1/2 + eps`; the planted pole at `s = a`
   is the abscissa, and `sup Re rho <= a` follows because zeta has no real zero in `(0,1)`.
2. TRANSLATOR, NOT DISCRIMINATOR: Landau converts "one-sided counting bound" <-> "zero-free
   region `Theta <= 1/2 + eps`" for ANY nonnegative-coefficient Dirichlet series. It runs
   unchanged for Beurling (nonnegative comb, but nothing forces the bound). It cannot even
   be POSED for D-H (no Euler product => log-derivative comb is sign-changing). So the
   zeta-special content is NOT in Landau; it is in (a) why the bound holds and (b) the FE
   upgrade of `<=` to `=`.
3. WHAT IT CONSUMES: coefficient nonnegativity of `Lambda(n)`, which IS an Euler-product
   face (`log zeta` = a nonnegative Dirichlet series). This is the named clause and the
   exact reason D-H escapes and Beurling does not.
4. SINGLE-eps vs ALL-eps: a single `eps` gives `Theta <= 1/2 + eps` (a zero-free region /
   quasi-RH); with the functional equation this narrows zeros to the strip `|Re rho - 1/2|
   <= eps` but is NOT full RH. All `eps` gives `Theta <= 1/2`, and the FE (`rho <-> 1-rho`)
   upgrades to `Theta = 1/2` = RH. The FE is load-bearing exactly as S7 over `F_q`.
5. THE BRIDGE SPEC (new, conjecture tier, RECONCILED against e1n in Section 3.6): with
   `psi_lambda(x) = sum_{n<=x} Lambda_eff(n; lambda)` (primes injected up to the horizon
   `~lambda^2`), the exact forcing hypothesis is `psi_lambda(x) <= x + C x^{1/2+eps}` with
   `C, x_0` INDEPENDENT of `lambda`, valid on `x_0 <= x <= X(lambda)` with `X(lambda) ->
   infinity`. The transfer clause is LAYER-DEPENDENT: at the INPUT layer (the injected
   coefficient stream) the comb equals the true von Mangoldt comb below the horizon by
   construction, so the bound transfers to `psi` verbatim, at the price of vacuity
   (BRIDGE-H there IS the classical hypothesis on a window; Section 3.6 regime A); at the
   BUILT-OBJECT layer e1n measures a comb face that is NOT below-horizon-exact
   (few-percent deviations, fill-zero corruption), so an object-read bound transfers only
   with an error term (Section 3.6 regime B). lambda-uniformity is where it bites either
   way.
6. SHARPEST GAP (posed, not answered): the uniform one-sided upper bound is
   positivity-free and one-directional, structurally WEAKER-LOOKING than M4 (the uniform
   det-class limit). Whether it is genuinely weaker, equivalent, or incomparable is open,
   and it is the SAME question as "does a Spec(Z)-Stepanov exist," i.e. it reroutes the
   finite-lambda wall from M4 (polarization) to R1 (a lambda-uniform cheap-upper-bound
   mechanism), because Landau needs only an upper bound and over `F_q` upper bounds come
   from S4 cheap multiplicity, which is R1-gated over `Z`. (Post-e1n status: the reroute
   survives only in the proof-engine reading; see Section 3.6.)

---

## 1. The theorem, written out (PROVEN tier)

Throughout, `psi(x) = sum_{n<=x} Lambda(n)` is the second Chebyshev function, `Lambda` the
von Mangoldt function, and `Theta = sup{ Re rho : zeta(rho) = 0, 0 < Re rho < 1 }` the
supremum of real parts of the nontrivial zeros. Classically `1/2 <= Theta <= 1`, with
`Theta = 1/2 <=> RH` (the lower bound `Theta >= 1/2` is the functional equation, below).

### 1.1 Statement

**Theorem A (one-sided bound forces RH).** Suppose that for every `eps > 0` there are
constants `C_eps` and `x_eps` with
```
  psi(x)  <=  x  +  C_eps * x^{1/2+eps}       for all x >= x_eps.
```
Then `Theta = 1/2`, i.e. every nontrivial zero of `zeta` has `Re rho = 1/2` (RH).

Note the hypothesis is an UPPER bound only. No lower bound on `psi(x) - x` is assumed. The
whole force comes from the fact that the true error oscillates to BOTH signs at order
`x^{Theta - eps}` (the `Omega_pm` theorem), so controlling the `+` side alone already pins
`Theta`.

### 1.2 The engine: Landau's oscillation theorem (PROVEN, classical)

**Lemma L (Landau, 1905).** Let `A: [1, inf) -> R` be Riemann-integrable on every finite
interval and bounded there, with `A(x) >= 0` for all sufficiently large `x`. Let `sigma_c`
be the infimum of `sigma` for which `int_1^inf A(x) x^{-sigma} dx < inf` (the abscissa of
convergence). If `sigma_c` is finite, then `F(s) = int_1^inf A(x) x^{-s} dx` is analytic on
`Re s > sigma_c` and is NOT analytic at the real point `s = sigma_c`.

The nonnegativity of `A` is exactly what upgrades the general "a singularity lies somewhere
on the line `Re s = sigma_c`" to "the REAL point `s = sigma_c` is itself a singularity."
This single fact is the whole load-bearing input, and it is where the argument consumes
positivity (Section 2). The `A >= 0` "for sufficiently large `x`" form (not "for all `x`")
is the standard statement: the finite part `int_1^{x_eps}` contributes an entire function
and moves neither `sigma_c` nor the singularities. Proof of Lemma L: expand `F` in a Taylor
series about a real point `sigma_1 > sigma_c`; if `sigma_c` were a regular point, the
radius of convergence at `sigma_1` would exceed `sigma_1 - sigma_c`, so the series
converges at some real `sigma < sigma_c`; interchange sum and integral there (legal
because all terms are nonnegative: the derivatives `F^{(k)}(sigma_1)` carry `(log x)^k
A(x) >= 0`), and deduce convergence of the defining integral strictly left of `sigma_c`,
contradicting the definition of the abscissa. (Reference: Montgomery-Vaughan, MNT I, and the self-contained
writeup Titichetrakun UBC-613E, Lemma 2.1, which follows M-V and gives exactly this proof.)

### 1.3 The construction and the proof of Theorem A

Fix `eps > 0` and write `a = 1/2 + eps in (1/2, 1)`. Let `C = C_eps`, `x_a = x_eps`, and
set
```
  g(x)  =  x  +  C x^a  -  psi(x).
```
By hypothesis `g(x) >= 0` for `x >= x_a`. Put `A(x) = g(x)/x >= 0` (eventually), so that
`F(s) = int_1^inf A(x) x^{-s} dx = int_1^inf g(x) x^{-s-1} dx`.

**Step 1 (evaluate `F` for `Re s > 1`).** Three elementary Mellin transforms, each
convergent for `Re s > 1` (the second also needs `Re s > a`, implied by `Re s > 1 > a`):
```
  int_1^inf x   * x^{-s-1} dx  =  1/(s-1),
  int_1^inf C x^a * x^{-s-1} dx  =  C/(s-a),
  int_1^inf psi(x) * x^{-s-1} dx  =  (1/s) * (-zeta'(s)/zeta(s)),
```
the last by partial summation (`int_n^inf x^{-s-1} dx = n^{-s}/s` and
`-zeta'/zeta(s) = sum_n Lambda(n) n^{-s}` for `Re s > 1`). Hence for `Re s > 1`
```
  F(s)  =  1/(s-1)  +  C/(s-a)  +  zeta'(s) / ( s * zeta(s) ).      (star)
```
The right side is meromorphic in the whole plane; by uniqueness of analytic continuation it
IS the continuation of the integral `F`.

**Step 2 (the pole at `s = 1` cancels).** Near `s = 1`, `zeta(s) = 1/(s-1) + gamma + ...`
gives `zeta'/zeta(s) = -1/(s-1) + O(1)`, so `zeta'/(s zeta) = -1/(s-1) + O(1)` (residue
`-1`). The `1/(s-1)` term has residue `+1`. They cancel: `F` is REGULAR at `s = 1`. This is
the analytic shadow of `psi(x) ~ x` (the main term removes the pole).

**Step 3 (locate the singularities of `F`).** In `Re s > 0` the singularities of (star) are:
- `s = a`, a simple pole with residue `C > 0` (the planted pole);
- the nontrivial zeros `rho` of `zeta` (poles of `zeta'/zeta`), at heights `Im rho != 0`.

Zeta has NO zero on the real segment `(0,1)`: for real `s in (0,1)`, `eta(s) = (1 -
2^{1-s}) zeta(s) = sum (-1)^{n-1} n^{-s} > 0` while `1 - 2^{1-s} < 0`, so `zeta(s) < 0 != 0`.
In particular `zeta(a) != 0`, so `s = a` contributes only the planted pole, and there is NO
real singularity of `F` anywhere in `(a, inf)` (on `(a,1)` zeta is nonzero, at `s = 1` we
cancelled, on `(1, inf)` zeta is nonzero). So `s = a` is the RIGHTMOST real singularity.

**Step 4 (apply Landau and conclude `Theta <= a`).** `A(x) >= 0` eventually, so Lemma L
applies: the abscissa `sigma_c` is real, is a singularity of `F`, and `F` is analytic on
`Re s > sigma_c`. Two constraints:
- Analyticity on `Re s > sigma_c` forbids any singularity there. If `Theta > a`, then `F`
  is singular at zeros `rho` with `Re rho` up to `Theta`, forcing `sigma_c >= Theta > a`.
- But `sigma_c` is a REAL singularity, and by Step 3 there is no real singularity of `F` at
  any real point `> a`. So `sigma_c <= a`.

These collide unless `Theta <= a`. Hence `Theta <= a = 1/2 + eps`. (When `Theta <= a` the
two constraints are consistent: the rightmost singularity is the real pole at `a`, so
`sigma_c = a` cleanly, and Landau is satisfied.)

**Step 5 (let `eps -> 0`, then use the FE).** Since `Theta <= 1/2 + eps` for every `eps >
0`, we get `Theta <= 1/2`. The functional equation `xi(s) = xi(1-s)` pairs zeros `rho <->
1 - rho`: for any zero `rho`, `1 - rho` is a zero, so `Re(1 - rho) <= Theta <= 1/2`, i.e.
`Re rho >= 1/2`; combined with `Re rho <= Theta <= 1/2` this gives `Re rho = 1/2`. Hence
`Theta = 1/2` and RH holds. QED.

### 1.4 The direct construction is the standard `Omega_pm` machine (cross-check)

Theorem A is the contrapositive packaging of the classical two-sided oscillation theorem,
which I verified at source and which uses the identical device:

**Theorem B (classical `Omega_pm`, Schmidt-Landau-Ingham).** With `Theta = sup Re rho`, for
every `eps > 0`,
```
  psi(x) - x  =  Omega_pm( x^{Theta - eps} ).
```
(Titichetrakun UBC-613E Theorem 2.2, following Montgomery-Vaughan; Ingham 1932 Ch. V.) The
proof forms `1/(s - Theta + eps) + zeta'(s)/(s zeta(s)) - 1/(s-1) = int_1^inf (x^{Theta-eps}
+ psi(x) - x) x^{-s-1} dx`, assumes the one-sided bound `psi(x) - x >= -x^{Theta-eps}` to
make the integrand nonnegative, notes the LHS is analytic for real `s > Theta - eps` because
`zeta` has no real zero in `(0,1)`, applies Landau, and contradicts the existence of a zero
with `Re rho > Theta - eps`. The `Omega_+` half runs the mirror function. Theorem A is the
immediate corollary: the hypothesis `psi(x) - x <= C x^{1/2+eps}` contradicts `Omega_+(
x^{Theta - eps'})` whenever `Theta - eps' > 1/2 + eps`, forcing `Theta <= 1/2 + eps`.

Two further classical facts fix the two ends of the `Theta` interval and confirm nothing is
being smuggled:
- `Theta >= 1/2` ALWAYS (unconditional): `psi(x) - x = Omega_pm(x^{1/2})` with no hypothesis
  (Schmidt 1903 for the sign changes; the `x^{1/2}` order is Titichetrakun Cor. 2.5). So the
  conclusion `Theta = 1/2` is the strongest possible, not vacuous.
- RH `=> psi(x) - x = O(x^{1/2} log^2 x)` (von Koch 1901; explicit Schoenfeld 1976), which
  in particular gives the one-sided bound. So Theorem A's hypothesis is EQUIVALENT to RH,
  not strictly stronger: the implication is an iff at the level of statements.
  [RE-RUN-NEEDED: the converse direction of the iff rests on von Koch, which is
  UNVERIFIED-MEMORY this session (Section 4.2); the forward direction (Theorem A itself,
  the load-bearing one for this route) is self-contained above. A SURVEYOR pass should pin
  von Koch/Schoenfeld at source before the iff is quoted anywhere as verified.]

### 1.5 Honest fine print (all discharged)

- Integrability/regularity: `A(x) = g(x)/x` is a bounded piecewise-smooth function on every
  finite interval (`psi` is a step function), Riemann-integrable, exactly Lemma L's class.
- `A >= 0` only for `x >= x_a`: harmless (the finite part is entire; Lemma L is stated for
  "sufficiently large `x`").
- Convergence: `g(x) <= x + C x^a` (since `psi >= 0`), so `A(x) <= 1 + C x^{a-1}` and the
  integral converges for `Re s > 1`; thus `sigma_c <= 1 < inf`, finite as Lemma L requires.
- The planted pole at `s = a` is not a problem, it is the anchor: `C x^a` (with `C, a > 0`)
  is a legitimate nonnegative function whose Mellin transform `C/(s-a)` is a real simple
  pole with residue `C > 0`, precisely engineered to make `g >= 0` and to sit at the
  abscissa. Its residue sign (`> 0`) is consistent with `sigma_c = a` being the abscissa of
  a nonnegative-integrand transform (the transform blows up to `+inf` as `s -> a+`).
- Single `eps` vs all `eps`: a single `eps` yields only `Theta <= 1/2 + eps`, a zero-free
  region `Re s > 1/2 + eps` (quasi-RH). Adjoining the FE narrows all zeros to the closed
  strip `1/2 - eps <= Re rho <= 1/2 + eps` (a clustering result), still NOT full RH. Full RH
  needs `eps -> 0`. This is the exact analogue of the `F_q` picture: S6 gives a one-sided
  bound at each level, S7's FE upgrades `<=` to `=`, and only the full family closes it.

TIER for Section 1: PROVEN (classical). Every step is either an elementary computation
(Steps 1-3, 5) or a cited classical theorem (Lemma L; Theorem B). No step needs an
undischarged hypothesis.

---

## 2. The mirror check (the discipline)

### 2.1 Why it fails for Davenport-Heilbronn: the named clause

D-H has a functional equation but no Euler product, and it has off-line zeros (the first at
`rho ~ 0.8085 + 85.699 i`). Trace the failure precisely.

The engine of Theorem A needs a nonnegative comb: `A(x) = g(x)/x` with `g = x + C x^a -
(Chebyshev function)` must be eventually one-signed, which requires the underlying
`-L'/L(s) = sum_n Lambda_L(n) n^{-s}` to have nonnegative coefficients `Lambda_L(n) >= 0`.
For `zeta` this holds because `log zeta(s) = sum_{p,k} (1/k) p^{-ks}` is a Dirichlet series
with nonnegative coefficients (the Euler product with the right sign structure), so
`Lambda(n) = log p >= 0` on prime powers and `0` elsewhere.

D-H has NO Euler product. Its defining Dirichlet coefficients are periodic mod 5 and already
sign-changing (the construction is a linear combination of two Dirichlet L-functions chosen
to force the FE), and consequently `-f_{DH}'/f_{DH}(s)` is NOT a nonnegative-coefficient
Dirichlet series: the log-derivative comb `Lambda_DH(n)` takes both signs. (Precise point:
nonnegativity of the log-derivative comb is equivalent to `log f` being a nonnegative
Dirichlet series, which is the Euler-product property; D-H lacks it.) Therefore
`g_DH(x) = x + C x^a - psi_DH(x)` is NOT eventually one-signed, `A_DH = g_DH/x` is not
eventually nonnegative, and **Lemma L cannot be posed at all**. The mechanism does not stall
late, it never starts. (e1n instantiates this numerically: the D-H log-derivative comb from
the Dirichlet recursion, validated against `-L'/L` to 1.3e-5, shows 17 sign changes below
`n = 40`; e1n T5e.)

NAMED CLAUSE (the Euler-product face): *the one-sided / Landau route consumes coefficient
nonnegativity of the comb, which IS an Euler-product face.* D-H's off-line zeros are
permitted precisely because it lacks that face, so the route carries no obligation for it.
This is the counting-side twin of the project's D-H discipline: D-H kills form-side methods
that ignore the Euler product; it kills the Landau route at the same joint, the nonnegative
comb.

REFINEMENT of the #145 audit (Section 6 of [`stepanov_engine_audit.md`](stepanov_engine_audit.md)):
that audit said "S7 (Landau conversion) applies to any FE-symmetric L-function including D-H, which is fine
because S7 alone proves nothing." This is slightly conflated. S7 has two sub-steps: (a) the
LANDAU oscillation step (one-sided bound `=>` `Theta <= a`), which needs coefficient
nonnegativity and does NOT apply to D-H; and (b) the FE UPGRADE step (`<=` to `=` via
`rho <-> 1-rho`), which needs only the FE and DOES apply to D-H. So the Euler-gating of S7
sits specifically in the Landau/nonnegativity sub-step, not in the FE sub-step. This
localizes exactly where in S7 the "RH content is Euler-gated" claim bites, sharpening the
audit without contradicting it.

### 2.2 Why it RUNS for Beurling: translator, not discriminator

A Beurling generalized number system has an Euler product `zeta_B(s) = prod_p (1 -
beta_p^{-s})^{-1}` over generalized primes `beta_p`, so `-zeta_B'/zeta_B(s) = sum Lambda_B(n)
n^{-s}` has NONNEGATIVE coefficients `Lambda_B` (the generalized von Mangoldt function,
supported on generalized prime powers, values `log beta_p >= 0`). Lemma L's hypothesis is
satisfiable: **the engine runs for Beurling.**

What fails is different: nothing FORCES the one-sided bound `psi_B(x) <= x + O(x^{1/2+eps})`
for a Beurling system: no functional equation and no additive lattice pin the abscissa
relationship (this is exactly the repo's Beurling control: an Euler product with no
`x + O(1)` integer-counting law, no Poisson, no theta FE). Beurling systems whose `zeta_B`
has zeros off the critical line and whose `psi_B(x) - x` is genuinely large are reported in
the literature [DISCHARGED 2026-07-11, S4/R1 surveyor round: Revesz arXiv:2207.00665
pp. 1-5 fetched at source (the DMV summary, its Eqs. 9-10); construction details pinned to
Diamond-Montgomery-Vorhauer, Math. Ann. 334 (2006) 1-36 at SECONDARY tier. See
`scratchpad/s4_carrier/01_surveyor_majorants.md` Section 6.3, adversary-verified. The
translator claim below does NOT depend on this existence statement, only on the absence of
any forcing mechanism in the hypotheses].
For such a system Lemma L still yields the TRANSLATION
```
  psi_B(x) <= x + O(x^{alpha})  for all alpha > alpha_0   <=>   Theta_B <= alpha_0,
```
a dictionary between a one-sided counting bound and a zero-free region. It USES nothing
zeta-specific.

[ADVERSARY correction, 2026-07-11 (surveyor D1 adjudicated: surveyor right; wording
fixed in place). The dictionary is lossless only with two scope clauses the original
sentence ("valid for ANY nonnegative-coefficient Dirichlet series with finite
abscissa") omitted. (1) REAL-ZERO CAVEAT, forward direction: Landau pins the abscissa
to the rightmost REAL singularity of the transform, and for a general Beurling zeta
that set includes possible real zeros of `zeta_B` in `(0, 1)`. The forward arrow
therefore yields only `Theta_B <= max(alpha_0, beta*)` with `beta*` the supremum of
real zeros of `zeta_B` in `(0, 1)`: either `Theta_B <= alpha_0`, or the strip supremum
is attained by a REAL zero. This is not a technicality: a real zero contributes a
definite-sign term `~ -c x^{beta*}` to `psi_B - x` (the Siegel-zero phenomenon), which
DAMPS the upper side and lets the one-sided bound coexist with off-line complex zeros
below `beta*`. For zeta the caveat is discharged by Step 3 of Theorem A (`zeta < 0` on
`(0,1)` via eta positivity, a lattice fact); for a general Beurling system it is not
dischargeable. The forward direction also consumes the pole normalization
`zeta_B ~ kappa/(s-1)` (an Axiom-A-type density input), not bare coefficient
nonnegativity. (2) The REVERSE arrow (`Theta_B <= alpha_0 =>` the bound) is not
Lemma-L content at all: it is explicit-formula/Perron bookkeeping (for zeta: von Koch,
still flagged in Section 1.4). Net corrected statement: the dictionary is lossless for
Axiom-A systems with no real zeros in `(alpha_0, 1)`, with the reverse arrow carried
by its own classical machinery. The 6.3 DMV kill in the S4/R1 survey is unaffected: it
routes around the caveat (its contradiction point is `s = 1`, where the Euler product
forbids a real zero).]

NAMED CLAUSE (translator status): *Landau's theorem is a TRANSLATOR (one-sided counting
bound `<->` zero-free region), not a zeta-special mechanism.* State this plainly so nobody
mistakes it for a proof engine: it is a reformulation of the target into a one-sided /
counting shape, exactly as classical as the Weil explicit formula reformulating RH into a
positivity. Its value is that it moves RH onto the Stepanov (counting) surface; it supplies
no gradient toward the bound.

### 2.3 The bracket

- D-H (FE, no Euler product): the route cannot be POSED (no nonnegative comb). Kills any
  claim that Landau discriminates by using the FE alone.
- Beurling (Euler product, no FE/lattice): the route RUNS but proves nothing (nothing forces
  the bound). Kills any claim that a nonnegative comb is sufficient.
- Zeta = the intersection (Euler product AND FE/lattice): the comb is nonnegative (Landau
  poseable) and the FE upgrades `<=` to `=`. The whole discriminating content therefore sits
  in whatever FORCES the one-sided bound, which is Section 3.

---

## 3. The bridge spec (CONJECTURE / spec tier, the handed-forward artifact)

This connects the Landau translator to the #160 positivity-free surface: the finite-cutoff
CCM object of e1k/e1l/e1m. The point is to write the exact hypothesis on the finite comb
that would feed Theorem A, and to pin where lambda-uniformity bites.

### 3.1 The finite-lambda object and its effective comb

The e1k/e1l/e1m harness builds a band-limited operator `D_log` on a log-circle of
Paley-Wiener support `L/2 = log lambda`, whose regularized determinant satisfies
`det_reg(D_log - z) = -i lambda^{-iz} xihat(z)` (the CCM Section-7 object). Its arithmetic
input is an effective von Mangoldt comb `Lambda_eff(n; lambda)`, with primes injected up to
the horizon `p <= lambda^2` (equivalently the two-meter cutoff `x = T/2pi` in the realized
CCM door; the far budget is the exact lattice tail `xihat(phi m) = 0` for `|m| > N`, proven
in-build in e1m). Define the finite Chebyshev function
```
  psi_lambda(x)  =  sum_{n <= x} Lambda_eff(n; lambda).
```
Two structural facts frame the bridge, and they live at DIFFERENT LAYERS (the distinction
Section 3.6 turns on):
- INPUT LAYER: below the injection horizon the injected coefficient stream is the true
  comb: `Lambda_eff(n; lambda) = Lambda(n)` for all prime powers `n <= H(lambda)`, where
  `H(lambda) ~ lambda^2` (in the e1k harness, literally `kmax = floor(lambda^2)` with the
  von Mangoldt stream; K1-clean, never read off zeros; adversary-confirmed by code
  inspection). Hence, with `psi_lambda` defined from the INPUT stream, `psi_lambda(x) =
  psi(x)` EXACTLY for `x <= H(lambda)`, by construction.
- BUILT-OBJECT LAYER (e1m + e1n): the finite object's ANALYTIC comb face (the effective
  coefficients of `-f'/f` of the built ground state) is a different thing: it tracks the
  true comb only to a few percent inside a window capped at `t ~ 7` by the archimedean
  escape, is corrupted by fill-zero pole terms on the dressed branch, admits no
  coefficientwise extraction beyond `n ~ 4` (superresolution), and is NOT below-horizon
  exact. So the finite OBJECT does not manifestly carry a clean `x^{1/2+eps}` one-sided
  bound with a lambda-independent constant, and its comb face is not the input comb.

### 3.2 The exact forcing hypothesis

**(BRIDGE-H).** There exist constants `C, x_0` INDEPENDENT of `lambda` and a window bound
`X(lambda) -> infinity` as `lambda -> infinity` such that, for all sufficiently large
`lambda`,
```
  psi_lambda(x)  <=  x  +  C * x^{1/2+eps}     for  x_0 <= x <= X(lambda),
```
for every `eps > 0` (the constant `C` may depend on `eps` but not on `lambda`).

**Coupling for free (the injection horizon):** take `X(lambda) <= H(lambda) ~ lambda^2`.
Then on the whole window `psi_lambda(x) = psi(x)` exactly, so (BRIDGE-H) transfers verbatim
to the true Chebyshev function:
```
  psi(x)  <=  x  +  C * x^{1/2+eps}     for  x_0 <= x <= X(lambda),  X(lambda) -> infinity.
```
Because `C, x_0` are lambda-independent and `X(lambda) -> infinity`, letting `lambda ->
infinity` gives `psi(x) <= x + C x^{1/2+eps}` for ALL `x >= x_0`, which is precisely the
hypothesis of Theorem A. Landau then yields `Theta <= 1/2 + eps`; all `eps` plus the FE give
RH.

Note what the coupling buys, stated per layer (adversary reconciliation, Section 3.6): the
one-sided route runs Landau on the TRUE `zeta` (the genuine `-zeta'/zeta`), and the finite
carrier only needs to supply the BOUND on a growing window where its comb coincides with
the true comb. At the INPUT layer that coincidence is exact by construction, so the route
takes a limit of the BOUND, not a limit of the OBJECT, and does not need the #160
Dirichlet-face inheritance clause; but exactly there the coupling is also EMPTY (regime A
below). The former FLAG is now resolved: (i) below-horizon comb agreement is exact and
K1-clean at the INPUT layer (confirmed) and FALSE at the built-object layer (e1n Q1); (ii)
the transfer of lambda-independent constants is the surviving open joint, and at the
object layer it needs an explicit error term whose measured floor (~3 percent) did not
shrink over lambda in [2.2, 3.6].

### 3.3 Where lambda-uniformity bites, and what M4 becomes on this route

At FIXED `lambda` the finite object satisfies a bound on its finite window trivially. The
entire content of (BRIDGE-H) is that `C`, `x_0`, and the exponent `1/2` are UNIFORM in
`lambda` while `X(lambda) -> infinity`. This uniformity is the archimedean uniformity, the
same place every finite-cutoff thread lands (M4). The new content is WHICH quantitative
statement it becomes on the one-sided route:
- On the det-class / positivity route (M4, #148/#160), the statement is: the truncated Weil
  quadratic form is uniformly positive-definite, equivalently `det_reg` converges in
  determinant class as `lambda -> infinity`. This is TWO-SIDED and a POSITIVITY.
- On the one-sided route (BRIDGE-H), the statement is: `psi_lambda(x) <= x + C x^{1/2+eps}`
  with lambda-uniform `C` on a growing window. This is UPPER-BOUND-ONLY and POSITIVITY-FREE.

### 3.4 The sharp open question (posed, not answered)

Is (BRIDGE-H) genuinely weaker than M4, equivalent to it, or incomparable?

- As STATEMENTS both are RH-equivalent (Section 1.4: the one-sided bound is an iff with RH,
  and M4 is an iff with RH), so at the level of propositions they are equivalent. That is the
  trivial sense and not the interesting one.
- As ATTACK SURFACES they differ, and this is the genuine content. (BRIDGE-H) is one-sided
  (Landau supplies the FE-upgrade for free), positivity-free, and a sup-style upper bound
  rather than an L^2 quadratic-form positivity. The strongest evidence it could be genuinely
  weaker-to-establish: over `F_q` the analogous one-sided count bound is achieved by the
  Stepanov engine WITHOUT ever proving the Hodge index theorem (the `F_q` avatar of M4). So
  the one-sided surface inherits Stepanov's promise: bypass the polarization.
- The catch (and the likely resolution): over `F_q` the one-sided bound is CHEAP because
  Frobenius makes vanishing cheap (S4). Over `Z` there is no such operator (S1/S4 absent =
  R1). The only currently-known route to the lambda-uniform upper bound is through the
  ground-state / det-class control = M4. So while the CONCLUSION is weaker-looking, the only
  available MECHANISM is M4.

THE PRECISE POSED QUESTION: *does the lambda-uniform one-sided upper bound (BRIDGE-H) follow
from, imply, or neither, the uniform det-class positivity (M4)? Equivalently: can the
finite-lambda comb supply a lambda-uniform cheap-upper-bound mechanism for `psi_lambda`
without passing through a positivity, i.e. is there a Spec(Z) analogue of Stepanov's S4 on
this carrier?* This is an R1 question, not an M4 question.

### 3.5 Why this is the new content (not another M4 costume)

#160's Hamburger pin produced a positivity-free RESTATEMENT of the IDENTIFICATION half
(`limit = c Xi`) that netted zero logical reduction (equivalent to the identification it
replaced). The one-sided route is a positivity-free surface for the OTHER half, the LOCATION
half (do the zeros lie on the line), via a bound rather than an identification. And crucially
it reroutes to a DIFFERENT wall: whereas #160 stayed at M4/identification, the one-sided
route converts the M4 uniformity into an R1-shaped question (a lambda-uniform cheap upper
bound = a Stepanov S4 on the CCM carrier). This is the first place the CCM finite-lambda
thread (a form-shaped, M4-walling object) makes explicit contact with the counting-shaped R1
wall. The handed-forward artifact is therefore: **the finite-lambda CCM comb is a candidate
CARRIER for a counting-side (Stepanov) attack, not only a form-side (positivity) attack, and
the two attacks wall at different facets (R1 vs M4); (BRIDGE-H) is the exact interface, and
its lambda-uniformity is the joint to attack.** Post-reconciliation caveat (3.6): this
survives specifically in the S4/R1 reading (the carrier as a potential PROOF ENGINE for the
bound); the transfer-from-the-finite-object reading is dead (regime B), and the
transfer-from-the-input reading is free but empty (regime A).

### 3.6 Reconciliation with e1n (ADVERSARY round, 2026-07-11)

e1n ran; the transfer clause of 3.2 must be read against its data. There are two regimes,
and BOTH obtain, at different layers of the construction. The original clause conflated
them.

**Regime A (input layer): the transfer is exact AND vacuous.** In the e1k harness the
prime input is injected as the literal von Mangoldt stream up to `kmax = floor(lambda^2)`;
with `psi_lambda` defined from that stream, `psi_lambda = psi` on `x <= lambda^2` exactly,
by construction. On this layer BRIDGE-H restricted to the window IS the classical
hypothesis `psi(x) <= x + C x^{1/2+eps}` on `[x_0, X(lambda)]`, verbatim: the reduction
content of the transfer step is ZERO. The route is not thereby dead, but its entire value
concentrates in one place: whether the CARRIER (the D_log operator whose spectral data
constrain the window) can PROVE the bound operator-theoretically, i.e. the S4/R1 reading.
Nothing about the finite object makes the bound easier to STATE; the question is whether
it makes it easier to PROVE.

**Regime B (built-object layer): the transfer clause is false without an error term.**
e1n's Q1 measured the built object's analytic comb face: it is NOT the truncated input
comb and NOT below-horizon exact. Concretely: aggregate comb-mass errors +4 to +9 percent
at the clean builds (lam 2.2, 3.0), fill-zero pole corruption dominating the dressed
branch (lam 2.6, sqrt13, raw |D| 0.10-0.26), no coefficientwise extraction beyond n ~ 4
(superresolution wall, cond 1.5e16), readable window capped at t ~ 7 by the archimedean
escape, and the truncation model for its deviation DISFAVORED though not excluded
(structured-null p ~ 0.005-0.09 after the adversary demotion of the white-noise bars). So
any bound READ OFF the built object transfers to `psi` only with an explicit error term
`E(x; lambda)` whose measured floor (~3 percent, delta0 = 0.034-0.036) did NOT shrink over
lambda in [2.2, 3.6]; lambda-uniform control of that error term is precisely the
M4-shaped uniformity this route was trying to sidestep. Worse for a naive object-side
bridge: a counting-shaped `psi_lambda` is not even well-posed on the object at finite
lambda, since the object's comb face has no known convergent Dirichlet expansion
(H4-existence untouched, e1n Q3).

**Net corrected clause.** BRIDGE-H must be posed at the input layer, where it is exactly
the windowed classical hypothesis (regime A). Its non-vacuous content is therefore NOT the
transfer (free and empty) but the MECHANISM question: can the finite-lambda carrier
produce the lambda-uniform upper bound from operator data (a Spec(Z)-Stepanov / S4 on the
CCM carrier, the R1-shaped question of 3.4)? e1n's measured comb-error signature bears on
exactly this and is not encouraging for a free ride: the comb error is one-signed WITHIN
each build but MIXED ACROSS builds (+, +, +, - over lam 2.2/2.6/3.0/sqrt13), so the finite
family does not hand over a lambda-uniform one-sided coordinate for free; the sign flip
locates the obstruction at the lambda-uniformity joint, as 3.4 predicted. The reroute
claim of 3.5 SURVIVES, but only in the S4/R1 reading: the carrier is a candidate proof
engine for the bound, not a source of a cheaper bound statement.

TIER for Section 3: CONJECTURE / spec. (BRIDGE-H) is a precisely stated hypothesis, not a
theorem; after the 3.6 reconciliation the below-horizon coupling is settled per layer
(exact-and-vacuous at input, false-without-error-term at object), and the single surviving
open sub-lemma is the lambda-uniform MECHANISM (R1/S4 on the carrier).

---

## 4. Citations and novelty sanity check

### 4.1 Verified this session (fetched / read at source)

- **Landau's oscillation theorem** (Lemma L): verified via the self-contained writeup
  T. Titichetrakun, "Oscillation of Error Terms; Littlewood's Result," UBC MATH 613E notes
  (following Montgomery-Vaughan), Lemma 2.1, with full proof. The statement "a Dirichlet
  series with nonnegative coefficients has a singularity at its abscissa of convergence,
  Landau 1905" independently confirmed via multiple search hits (Missouri J. Math. Sci. 23
  (2010), Maurizi-Ouimet "Extending Landau's Theorem," arXiv:1009.0228, which opens with the
  classical statement).
- **The `Omega_pm` theorem via `Theta`** (Theorem B): verified at source, Titichetrakun
  Theorem 2.2, exact construction `1/(s-Theta+eps) + zeta'/(s zeta) - 1/(s-1) = int (x^{Theta
  -eps} + psi - x) x^{-s-1} dx`, one-sided hypothesis fed to Landau, uses "zeta nonzero for
  real `s in (0,1)`." Theorem 2.4 there is literally the one-sided form: "Assume `psi(x) <=
  x + c x^Theta` ... then by Landau's theorem ...", concluding `Omega_pm(x^Theta)` with
  constant `1/|rho|`.
- **`Theta = sup Re rho`, `1/2 <= Theta <= 1`, `Theta = 1/2 <=> RH`**, with `Theta >= 1/2`
  from "the existence of nontrivial zeros and their symmetry about `sigma = 1/2`": confirmed
  verbatim in search results (Steklov / Ingham-question literature) and in the notes.
- **Unconditional `psi(x) - x = Omega_pm(x^{1/2})`**: Titichetrakun Corollary 2.5.
- **Schmidt 1903**: confirmed, "E. Schmidt proved in 1903 by elementary means that
  `psi(x) - x` changes sign infinitely often" (Titichetrakun Section 2 intro, citing Schmidt
  [12]).
- **Littlewood 1914**: `psi(x) - x = Omega_pm(x^{1/2} log log log x)` (Titichetrakun Theorem
  3.1), context only.
- **RH `=> psi(x) - x = O(x^{1/3})` refinement / `O(x^{1/2} ...)`**: Titichetrakun Theorem
  1.7 (`nu(x) = psi(x) - x^{1/2} + O(x^{1/3})` under RH), consistent with the standard von
  Koch / Schoenfeld `O(x^{1/2} log^2 x)`.

### 4.2 Cited from memory, flagged

- **[UNVERIFIED-MEMORY]** E. Schmidt, "Uber die Anzahl der Primzahlen unter gegebener
  Grenze," Math. Ann. 57 (1903), 195-204 (exact page range from memory; the RESULT is
  verified above via the notes).
- **[UNVERIFIED-MEMORY]** Ingham, "The Distribution of Prime Numbers," CUP 1932, Chapter V
  (the Omega-theorems chapter): the standard textbook home of Theorem B. The result is
  verified via the notes that follow Montgomery-Vaughan; the specific Ingham chapter number
  is from memory.
- **[UNVERIFIED-MEMORY]** Montgomery & Vaughan, "Multiplicative Number Theory I: Classical
  Theory," CUP 2007: the notes cite this as reference [14] and follow it; the exact section
  for Landau (Section 15 / 1.x) and for the `Omega` results is from memory (the notes give
  "[14, Theorem 1.3]" for the Dirichlet-to-integral bridge and "[14, Section 10.2]" for the
  zero count, so the Landau/oscillation material is nearby but I did not pin the exact
  theorem number).
- **[UNVERIFIED-MEMORY]** Widder, "The Laplace Transform," Princeton 1941, Ch. II Thm 5b:
  the Laplace-transform form of Landau's theorem ("Landau's theorem" for `int e^{-st} dA`).
- **[UNVERIFIED-MEMORY]** J. Pintz, "On the remainder term of the prime number formula"
  I-V (Acta Arith. / Studia Sci. Math. Hungar., c. 1980-1984): sharper oscillation results
  (removing the `eps` and giving explicit constants / connecting a single zero to a definite
  oscillation). Related modern surveys located but not read: "Distribution of zeta zeros and
  the oscillation of the error term of the PNT" (Proc. Steklov Inst. 2017); Revesz,
  "The method of Pintz for the Ingham question ... in the Beurling context" (arXiv:2207.00665);
  "Oscillations of the error term in the prime number theorem" (arXiv:1912.00853). These
  confirm the Beurling-context oscillation literature exists but I did not pin exact Pintz
  citations.
- **[UNVERIFIED-MEMORY]** von Koch 1901 (RH `=>` `psi(x) - x = O(sqrt(x) log^2 x)`) and
  Schoenfeld 1976 (explicit form `|psi(x) - x| < (1/8pi) sqrt(x) log^2 x` for `x >= 73.2`):
  standard, not fetched this session.

### 4.3 Novelty sanity check (10-minute pass, done)

The statement "one-sided `psi(x) <= x + O(x^{1/2+eps})` for all `eps` implies RH" is CLASSICAL
FOLKLORE, an immediate corollary of the `Omega_pm` theorem (Theorem B), and it is NOT novel.
Cleanest citable home for the repo, so it cites a source rather than folklore:
- **Ingham 1932, Chapter V** (the Omega-theorems), and
- **Montgomery-Vaughan, MNT I** (Landau oscillation + the `Theta`-error dictionary),
with **Titichetrakun UBC-613E, Lemma 2.1 + Theorems 2.2 / 2.4** as a free, self-contained,
verified-at-source writeup of exactly the construction in Section 1.3. The repo should cite
these three and stop calling it folklore.

What IS new here (and belongs to this note / a possible LEARNINGS entry):
1. The S7 REFINEMENT: localizing the Euler-gating of the audit's S7 to the Landau /
   nonnegativity sub-step, not the FE sub-step (Section 2.1).
2. The BRIDGE SPEC (BRIDGE-H) and its posed open question (Section 3): the one-sided route
   reroutes the finite-lambda CCM wall from M4 to R1 ONLY in the proof-engine reading (3.6:
   the input-layer transfer is exact and vacuous, the built-object transfer needs an error
   term), and the finite comb is a candidate Stepanov carrier in that reading alone. Not found in the literature (the CCM object is repo-native; no published
   work runs a Stepanov/one-sided attack on a regularized-determinant comb).

---

## 5. Handed forward

- To e1n / ADVERSARY: RESOLVED this round (Section 3.6). (i) Below-horizon comb agreement:
  exact and K1-clean at the INPUT layer (by construction, confirmed); FALSE at the
  built-object layer (e1n Q1: few-percent comb-mass errors, fill corruption, no
  extraction beyond n ~ 4). (ii) Transfer with lambda-independent constants: at the input
  layer free but vacuous; at the object layer needs an error term whose ~3 percent floor
  did not shrink over lambda in [2.2, 3.6]. e1n's comb-error signature came out MIXED
  ACROSS builds (one-signed within each build only), which is the "sign flips" arm: the
  obstruction sits at the lambda-uniformity joint = the R1-shaped question of Section 3.4.
- To SYNTHESIZER: the one-line scope note, "the #145 one-sided residue is a TRANSLATOR
  (one-sided count bound `<->` zero-free region), Euler-gated at coefficient nonnegativity
  (D-H cannot pose it, Beurling runs it but nothing forces the bound); on the CCM carrier it
  reroutes the finite-lambda wall from M4 to R1 ONLY in the proof-engine reading (3.6): the
  below-horizon transfer is exact-and-vacuous at the input layer, false without an error
  term at the built-object layer."
- To VERIFIER (clean Lean targets, all classical): Lemma L (Landau: nonnegative integrand =>
  abscissa is a real singularity); the elementary `zeta(s) < 0` on `(0,1)` via the eta
  function; the pole cancellation at `s = 1`. Theorem A itself is a good medium-term target
  once Mathlib has enough of the `zeta'/zeta` Mellin identity.

---

## 6. e1n's measured answers (SYNTHESIZER pointer, added at integration)

The parallel probe [`e1n_prime_comb.md`](../../experiments/spectral/e1n_prime_comb.md)
(`.py`/`.npz`, 31/31 full and quick, adversary-reproduced) supplies the numbers this
dossier's open joints turn on:

- **The mixed-sign comb error (the "sign flips" arm of Section 5 item (i)).** The finite
  family's comb-mass errors are one-signed WITHIN each build but MIXED ACROSS builds
  (+, +, +, - over lam 2.2/2.6/3.0/sqrt13; deflated aggregates -0.66, +0.006, -0.71,
  +0.49): no lambda-uniform one-sided coordinate comes for free, so the obstruction sits
  at exactly the lambda-uniformity joint Section 3.4 named.
- **Input-layer vacuity vs built-object error term (Section 3.6).** e1n Q1 is the
  measurement behind regime B: comb-mass errors +4 to +9 percent on the clean builds,
  fill-zero pole corruption on the dressed branch (ghost quotient drops |D| up to 381x),
  no coefficientwise extraction beyond n ~ 4, the ~3 percent floor not shrinking over
  lambda in [2.2, 3.6].
- **The abscissa-side companion (e1n Q3).** H4 splits as existence + absoluteness; a
  nonnegative one-sided envelope makes absoluteness cheap (the corrected abscissa lemma,
  Euler-gated exactly at the same clause Section 2.1 names), while EXISTENCE stays
  equivalent to the Section-7 identification: the two positivity-free surfaces (this
  dossier's location half, e1n's identification half) wall at different clauses of the
  same limit.

Cite Section 3.6, not the bare 3.2 transfer clause, whenever this route is quoted. The
surviving live coordinate is the S4/R1 proof-engine question on the CCM carrier
(Section 3.4), tracked in [`sourcing_gap_r1.md`](sourcing_gap_r1.md) and LEARNINGS #161.
