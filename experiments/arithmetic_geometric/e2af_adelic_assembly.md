# 2AF: the (1,p)-bidegree intersection-pairing assembly attempt (Front 3)

> Experiment [e2af_adelic_assembly.py](e2af_adelic_assembly.py). Front 3 of the
> Arakelov-face program: lift e2ad from the moment matrix to an honest
> intersection-pairing ASSEMBLY attempt, and pin the EXACT step where the per-prime
> sqrt(p) scales fail to combine into a single Arakelov intersection number, and
> whether Yuan-Zhang's all-places adelic structure dissolves or merely relocates the
> mismatch. Companion to [2L](2L_arakelov_face_probe.md), [2K](2K_spec_z_squared_dictionary.md),
> [e2ad](e2ad_fh_gamma_certificate.md), [e2g](e2g_intersection_signature.md).

## Verdict (honest, up front)

This is a precise NO-GO LOCALIZATION, not a new construction and not a re-run of e2ad.
The new content (which e2ad did not do) is the ASSEMBLY attempt: build the per-prime
(1,p)-bidegree primitive intersection Gram matrices fibre-by-fibre, then try to
assemble them into one signed pairing the way Yuan-Zhang's adelic-line-bundle index
theorem would. The computation exhibits, across three genuine carriers and the first
15 primes:

1. Each per-prime form G_p is negative definite (Hasse, a theorem, K1-clean,
   RH-independent). The assembly INPUTS are sound.
2. No single common scale assembles them (Model A): the per-prime normalizing scale
   is sqrt(p), p-dependent, with spread max/min = 4.85 over the first 15 primes;
   forcing one scale leaves a diagonal asymmetry growing as p/p_mid, unbounded.
3. The adelic block (Model B) IS definite block-diagonally, but only because each
   block uses its OWN scale sqrt(p): it is p separate intersection numbers, not the
   single adelic <L, L>. Collapsing to the single scalar sum_v <L, L>_v moves the
   entire burden onto the prime-side sum sum_p t_p/sqrt(p) (= the P_fin / von Mangoldt
   block of 2K), whose behavior IS RH-gated. Per-prime Hasse (each term < 2g) does not
   control the sum.
4. The archimedean place (Yuan-Zhang's bundling) supplies rank 1; the scale family
   {sqrt(p)} has rank #primes. A rank-1 object cannot absorb a rank-15 family. So the
   adelic all-places structure RELOCATES the #25 scale mismatch into one regularized
   prime-side term; it does NOT dissolve it.

NET: the per-prime sqrt(p) scales do not assemble into a single Arakelov intersection
number, and Yuan-Zhang's adelic bundling relocates rather than dissolves the mismatch.
M4/#25 is untouched. This is a sharper, intersection-pairing-side statement of the
#25 / #44 (1,p)-bidegree obstruction.

## The object (the (1,p)-bidegree Frobenius cycle class, made concrete)

On the function-field surface C x C (2G) the primitive intersection Gram is

```
G_prim(q, t) = [[ -2g,  -t ],     t = q + 1 - N_1  (Frobenius trace)
                [ -t,  -2gq ]]     RH-for-curve <=> G_prim neg def <=> t^2 < 4g^2 q
```

The (2,2) slot -2gq is the f.Gamma = q bidegree: Frobenius is a (1,q) correspondence
at the ONE scale q. Over Spec(Z) the fibre over a prime p is Spec(F_p), a curve over
F_p of its own, so the Frobenius cycle class Gamma_S carries a PLACE-DEPENDENT (1,p)
bidegree (f.Gamma_p = p, no single q). The per-fibre primitive Gram is therefore

```
G_p = [[ -2g,   -t_p ],     t_p = p + 1 - #X(F_p)  (per-prime Frobenius trace)
       [ -t_p,  -2g p ]]     neg def <=> t_p^2 < 4g^2 p  (per-prime Hasse, a THEOREM)
```

A would-be single Arakelov intersection number is what Yuan-Zhang's adelic-line-bundle
index theorem (Math. Ann. 367, 2017) produces: it bundles all places (finite p and
archimedean) into one adelic pairing <L, L> = sum_v <L, L>_v, a SCALAR, and the index
theorem controls the signature on the primitive part of that ONE global pairing. The
target pairing is the 2K dictionary M = A_arch + P_fin + B_pole, with B_pole the
hyperbolic (+1) direction and A_arch + P_fin the negative primitive part.

## The new probe (what e2ad did not do)

Carrier honesty notes: the two elliptic carriers (11a1, 389a1) are genuine g=1 curves
with honest point counts. The genus-2 carrier y^2 = x^5 + x + 1 has discriminant
3 * 7^2 * 23, so it is restricted to its GOOD primes (it drops 3, 7, 23 where the fibre
is singular and t_p is not a smooth-fibre Frobenius trace). The genus-2 carrier uses the
SCALAR (1,p) template (the single first trace t_p = p + 1 - N_p with the leading
coefficient set to 1) as a faithful scalar surrogate, not the full rank-4 Frobenius
form; this is sufficient for the assembly probe (the scale mismatch lives in the (2,2)
slot's p-scaling, identical for any genus) and is flagged so no claim rests on a
higher-genus refinement not computed here.

e2ad computed the per-prime a_p for one curve and verified per-prime Hasse-boundedness;
its explicit verdict was "a re-cataloging of #25/#44/#125/#30, no new theorem, object,
or localization." It did NOT build the per-prime intersection Gram matrices and try to
assemble them. e2af does exactly that, across three carriers (11a1, 389a1, a genus-2
hyperelliptic curve), with three honest assembly models. The point counts #X(F_p) are
intrinsic to each carrier; no zeta zeros enter (K1-clean). The per-prime definiteness
is Hasse, unconditionally true; the FAILURE exhibited is of the ASSEMBLY, not of RH
(RH-independent).

## Results (the actual numbers)

Per-prime forms (all three carriers): every G_p is negative definite across the first
15 primes. The normalized Frobenius coupling t_p/sqrt(p) satisfies |.| < 2g = 2 at
every prime (the per-prime unit-circle bound). Sample (389a1, rank 2):

```
p= 2: t_p= -2  neg-def=True  t_p/sqrt(p)=-1.414   diag22=  -4.0
p= 7: t_p= -5  neg-def=True  t_p/sqrt(p)=-1.890   diag22= -14.0   (closest to the bound)
p=19: t_p=  5  neg-def=True  t_p/sqrt(p)= 1.147   diag22= -38.0
```

Model A (single common scale): FAILS for all carriers.

```
per-prime normalizing scale = sqrt(p): [1.41, 1.73, 2.24, 2.65, 3.32, 3.61, 4.12, 4.36, ...]
scale spread max/min  = 4.8477   (1.0 would mean ONE common scale)
diag asymmetry under a forced single scale = 2.4737  (= p_max/p_mid; grows unbounded in N)
single common scale exists = False
```

Model B (Yuan-Zhang adelic block -> single scalar): block-diagonal is definite
(each |t_p/sqrt(p)| < 2g), but it uses a per-block scale sqrt(p), so it is 15 separate
intersection numbers, not one. The single adelic scalar splits as:

```
carrier      diag part (reg.)   prime-side coupling sum  sum_p t_p/sqrt(p)
11a1            -30.0                  -0.83
389a1           -30.0                  -9.62
genus-2         -30.0                  -4.25
```

The diagonal part -2g * #primes is a regularized count (the same for all carriers at
fixed N); the prime-side sum sum_p t_p/sqrt(p) is carrier-dependent and is exactly the
P_fin / von Mangoldt block of 2K. Its partial-sum trajectory (the RH-gated object) for
389a1: [-1.41, -2.57, -3.91, -5.80, -7.01, -7.84, -9.29, -8.15, ...], i.e. it does not
visibly converge or stay sign-controlled by the per-prime bound alone.

Model B archimedean test: distinct per-prime scales = 15, archimedean block rank = 1,
rank deficit = 14. A rank-1 archimedean direction cannot absorb a rank-15 scale family.

## The EXACT step where it walls (the localization the prompt asked for)

The wall is at the (2,2) slot of G_p, the f.Gamma_p = p bidegree. The off-diagonal
coupling t_p is Hasse-bounded by 2g sqrt(p), so dividing row/column 2 by sqrt(p)
normalizes BOTH the coupling (to |t_p/sqrt(p)| < 2g) and the (2,2) slot (to -2g),
turning G_p into the unit-circle form [[-2g, -t_p/sqrt(p)], [-t_p/sqrt(p), -2g]]. This
is the ONLY scale that makes the per-prime forms comparable, and it is sqrt(p), which
is p-dependent. There is no single scale that does this for all p simultaneously
because the diagonal asymmetry (slot11 = -2g constant vs slot22 = -2g p) is unbounded
in p. This is the #25 / #44 (1,p)-bidegree obstruction, now exhibited not as a property
of a moment matrix (e2ad) but as the precise obstruction to forming a single signed
intersection pairing out of the per-fibre data: the assembly the Weil template requires.

Does Yuan-Zhang's all-places-at-once structure help? It bundles the finite places AND
the archimedean place into a single scalar sum_v <L, L>_v. That collapse removes the
p-many distinct matrix scales but at the price of summing the off-diagonal couplings
into the single prime-side series sum_p t_p/sqrt(p). The per-prime bound |t_p/sqrt(p)|
< 2g controls each term but NOT the sum: a conditionally-controlled series whose
sign/growth IS the RH content (it is the explicit-formula prime block). So the adelic
structure RELOCATES the mismatch: it moves it from "p incompatible matrix scales" to
"one regularized prime sum whose behavior is RH-gated." It does not dissolve it,
because the single archimedean place (rank 1) cannot host a p-indexed (rank #primes)
scale family. This is the intersection-pairing-side confirmation of 2I's "positivity
is global" and 2K section 4's "the gap is the product surface": the adelic bundling
gives a single number, but proving that number has the right sign IS M4, untouched.

## D-H discipline

The per-prime traces t_p = p + 1 - #X(F_p) require an Euler-product / motivic carrier.
Davenport-Heilbronn has NO Euler product, hence no Frobenius t_p, no per-prime G_p, no
fibre to assemble: the construction is UNBUILDABLE for D-H (survival by non-mimicry, as
in 2G/2L, failing at the motive not at the positivity). No positivity statement in this
file would "work" for D-H. The shared smoke-test control passes 9/9 (including Test 9:
the Li detector is blind to D-H while D-H's off-line zero at 0.8085 + 85.699 i is
detectable). The assembly failure exhibited is structural and RH-independent, so it is
not a positivity claim that could be mistakenly satisfied by D-H.

## New-vs-re-cataloging self-assessment (per the e2ad caution)

GENUINELY NEW (and verified):

- The assembly attempt itself. e2ad explicitly did NOT build the per-prime intersection
  Gram matrices or attempt their assembly; it computed a_p and re-narrated #25. e2af
  builds G_p fibre-by-fibre across three carriers and runs three honest assembly models,
  producing the concrete numbers above (the scale-spread 4.85, the rank deficit 14, the
  prime-side coupling sums, the partial-sum trajectories). This is the lift "from moments
  to an intersection-pairing attempt" the prompt specified, and it is new computational
  content.
- The sharpened localization. The wall is pinned to the (2,2) slot's p-scaling, and the
  adelic-bundling answer is made precise: it RELOCATES the mismatch from p incompatible
  matrix scales to a single RH-gated prime sum (because the archimedean place is rank 1
  vs the scale family's rank #primes). This is a more precise statement than #25's "no
  single compatible scale": it identifies WHY the adelic structure does not rescue it.

RE-CATALOGING (the universal gap is UNCHANGED):

- The underlying obstruction is #25 / #44 (the (1,p) place-dependent bidegree). e2af
  does not move the open kernel; it confirms, on the intersection-pairing side, the same
  verdict 2K/2L/e2ad reached on the dictionary/moment side. The per-prime definiteness is
  Hasse (a theorem); the single-surface index is Faltings-Hriljac (a theorem, 2H); the
  missing thing remains the global signed pairing on the actual zeros (PROP-global = the
  base = M4).
- Model B's "block-diagonal is definite but uses per-block scales" is the precise
  numerical face of "FH is positive-definite per surface but does not globalize" (2L
  headline). New as a computation, re-cataloging as a verdict.

Net honest accounting: one genuinely new computation (the assembly attempt and its
numbers) that sharpens the #25 localization (the adelic structure relocates, does not
dissolve, the scale mismatch), wrapped around an unchanged universal gap. Consistent
with e2ad's caution that more all-roads re-cataloging is not the leverage: the leverage
remains the construction of the base, untouched here.

## Verification targets (for VERIFIER)

- VT1 (K1-clean, true): for each carrier and prime, G_p = [[-2g, -t_p], [-t_p, -2gp]]
  is negative definite iff t_p^2 < 4g^2 p (per-prime Hasse). Formalizable as a 2x2
  determinant + trace sign condition; the Hasse bound t_p^2 < 4g^2 p is the input
  theorem (Mathlib has the elliptic-curve Hasse bound machinery for g=1).
- VT2 (linear algebra, true): there is no single positive scalar s with -2gp/s^2 = c
  for all p in a set of >= 2 distinct primes (the diagonal asymmetry is unbounded). A
  one-line impossibility.
- VT3 (the relocation, structural): the block-diagonal assembly with per-block scale
  sqrt(p) is negative definite, while the single adelic scalar's off-diagonal part is
  sum_p t_p/sqrt(p), whose convergence/sign is NOT implied by the per-prime bounds
  |t_p/sqrt(p)| < 2g (a counterexample-friendly statement: bounded terms, uncontrolled
  partial sums).

## Adversarial test cases (for ADVERSARY)

- AT1: attempt to find a single common scale (a fixed weighting of all places) that
  assembles the per-prime forms into a definite pairing with a bounded condition number
  as N -> infinity. The claim is this is impossible (the scale spread sqrt(p_max/p_min)
  diverges). Break it by exhibiting such a weighting.
- AT2: attempt a higher-rank archimedean block (more than one archimedean direction) and
  check whether finite extra rank absorbs the p-indexed scale family. The claim is no
  finite rank suffices (the family has rank #primes -> infinity). Break it with a
  finite-rank construction.
- AT3 (D-H): confirm the construction cannot be built for D-H (no Euler product => no
  t_p). The claim is unbuildability; break it by supplying a D-H "t_p" that yields
  per-prime definite G_p and assembles.
- AT4: check whether the prime-side sum sum_p t_p/sqrt(p) for a SPECIFIC carrier could be
  made to converge/stay sign-controlled by the per-prime bounds alone (without RH). The
  claim is it cannot (the sum is the RH-gated explicit-formula block).

## Outputs

- `e2af_adelic_assembly.npz`: 389a1 per-prime data (primes, t_p, t_p/sqrt(p), needed
  scale sqrt(p)).

## Connections

- e2ad ([e2ad](e2ad_fh_gamma_certificate.md)): the moment-lens per-prime computation
  this lifts to the intersection-pairing side; the two withdrawn moves NOT re-made here.
- 2K ([2K](2K_spec_z_squared_dictionary.md)): the target pairing M = A_arch + P_fin +
  B_pole; the (1,p) bidegree; the prime-side P_fin block the relocation lands on.
- 2L ([2L](2L_arakelov_face_probe.md)): the Arakelov face relocates, not escapes; the
  base (PROP-global) is the gap; Yuan-Zhang fixed-scheme.
- 2G ([e2g](e2g_intersection_signature.md)): the function-field primitive Gram template
  G_prim, the single-scale q version this generalizes to per-prime p.
- 2H ([e2h](e2h_arithmetic_hodge_index.md)): Faltings-Hriljac per single surface (the
  block-diagonal definiteness face).
- 2I: positivity is global (the archimedean place is one contribution, not separable).
- #25 / #44: the (1,p) place-dependent bidegree (the obstruction this sharpens).
