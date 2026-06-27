# 2M: the generic-vs-sharp positivity gap, localized

> FRONT 2 follow-up to the 2L Arakelov-face probe (LEARNINGS #131). Question: the
> existing arithmetic Hodge-index / Beilinson-Bloch height positivity (Yuan-Zhang
> Math. Ann. 367 2017; Gao-Habegger; the geometric Bogomolov conjecture) is proved
> in a GENERIC regime. The M4 open step is SHARP positivity (definiteness on the
> WHOLE primitive part, no excluded locus, forcing |alpha| = sqrt(q) at the
> boundary). What does "generic" exclude, is the excluded locus where an off-line
> zero would live, and is the sharp/boundary case exactly the marginal wall?
> Honest classification: this is a NO-GO / LOCALIZATION (one new sharp localization
> plus re-cataloging), not a construction. Companion to
> [2L](2L_arakelov_face_probe.md), [2K](2K_spec_z_squared_dictionary.md),
> [e2g](e2g_intersection_signature.md), [e2h](e2h_arithmetic_hodge_index.md),
> [08A](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md).

## 1. Headline verdict

The generic-vs-sharp gap is NOT identical to the marginal-positivity wall, but the
two interlock through a precise mechanism, and the net is that the generic results
give ZERO leverage on the sharp case for zeta. Three findings:

1. (Task 1.) The Yuan-Zhang / Gao-Habegger positivity is genuinely SHARP on its own
   object (definiteness everywhere on the relevant primitive part, not modulo an
   excluded set). What is "generic" is the HYPOTHESIS (non-degeneracy of the Betti
   form / the non-special-locus condition), not the CONCLUSION. The excluded locus
   is a hypothesis-side condition on the base, not a measure-zero exception in the
   positivity verdict.

2. (Task 2.) The excluded locus is NOT where a zeta off-line zero would live, for a
   reason more basic than geometry: zeta has no Yuan-Zhang object at all (no abelian
   scheme, no Betti form, no special subvariety). The generic/sharp distinction is
   about which heights on which subvarieties are positive; an off-line zero of zeta
   is not a point on any such subvariety. So the gap "RH true generically vs RH true
   everywhere" does NOT have a Yuan-Zhang realization. The two gaps are in different
   categories.

3. (Tasks 3-4.) Over F_q "generic" and "sharp" provably coincide, and the coincidence
   has a one-line cause: the Frobenius spectrum is FINITE and lies on ONE circle, so
   the integer trace lattice never reaches the irrational boundary |t| = 2g sqrt(q).
   Over Z the boundary Re = 1/2 is exactly the ACCUMULATION locus of an INFINITE
   spectrum, the (1,p) bidegree gives infinitely many distinct circles sqrt(p), and
   that double break (infinite + multi-scale) is what destroys the F_q coincidence.
   The sharp case IS the hard core, and it is hard for the same reason as the
   marginal wall (no buffer at the accumulation boundary), but the generic-vs-sharp
   distinction is a SECOND, logically independent gap layered on top.

## 2. Task 1: the generic positivity theorem, stated precisely, and what it excludes

The relevant theorem cluster (the geometric Bogomolov conjecture and its height
machinery):

- Yuan-Zhang, "The arithmetic Hodge index theorem for adelic line bundles"
  (Math. Ann. 367, 2017): an arithmetic Hodge index theorem for adelic line bundles
  on a fixed projective variety over a number field / function field. The signature
  is the arithmetic analogue of (1, n-1): the intersection form against a fixed nef
  adelic class is negative-(semi)definite on the primitive part. SHARP on that fixed
  scheme.
- Gao-Habegger (and Cantat-Gao-Habegger-Xie, Duke 170(2), 2021): the geometric
  Bogomolov conjecture. The central analytic input is the NON-DEGENERACY of the
  Betti form (the (1,1) form pulled back from the universal abelian variety / the
  Betti map). On the locus where the Betti form is non-degenerate (the "non-special"
  locus), the height is positive and a subvariety with dense small points must be a
  torsion/special subvariety.

The crucial parse: in BOTH results the positivity CONCLUSION is sharp. The word
"generic" attaches to the HYPOTHESIS:

- the Betti form is non-degenerate only OFF the special locus (degenerate Betti rank
  on subvarieties of "special" type: isotrivial pieces, subgroup-translate fibres);
- the index theorem needs a fixed nef/big polarization, and degenerates where that
  class degenerates.

So "what generic excludes" = the SPECIAL LOCUS of the base (isotrivial / torsion /
subgroup-coset subvarieties where the Betti form drops rank). It is an exclusion of
DEGENERATE GEOMETRY in the hypothesis, not an exception in the positivity verdict.
There is no "the height is positive except on a measure-zero set of points"; it is
"the height is positive on subvarieties not of special type."

## 3. Task 2: is the excluded locus where an off-line zero lives?

NO, and the reason is the firewall, not a coincidence of loci.

For the generic-vs-sharp distinction to BE the gap "RH-true-generically vs
RH-true-everywhere," there would have to be a single object on which (a) Yuan-Zhang /
Gao positivity is the relevant signature and (b) the points/zeros of zeta sit, with
the off-line zeros landing precisely in the excluded special locus. None of that
exists:

- zeta is the L-function of no abelian scheme: no universal abelian variety, no Betti
  map, no Betti form to be non-degenerate or degenerate. The non-degeneracy
  hypothesis has no zeta instance.
- the Yuan-Zhang index lives on a FIXED scheme and certifies that scheme's own
  height / preperiodic-point / Calabi data. zeta's zeros are not heights of points on
  any such scheme (the 2L / e2ad severance: the only height-to-L channel is
  Gross-Zagier / BSD, the central derivative at s = 1, severed from where the other
  zeros sit; disqualifier #113).
- the excluded special locus is a sub-GEOMETRY (isotrivial/torsion subvarieties). An
  off-line zero is a complex number beta + i gamma with beta != 1/2. There is no map
  carrying one to the other.

Conclusion: the gap between generic and sharp positivity, in Yuan-Zhang/Gao, is a
gap about DEGENERATE BASE GEOMETRY. The gap between "RH generically" and "RH
everywhere" would be a gap about a measure-zero set of EXCEPTIONAL ZEROS. These are
not the same gap and there is no functor between them, because the object on which
the first lives (an abelian scheme with a Betti form) does not exist for zeta. This
is the firewall in its strongest form: the generic-vs-sharp distinction does not even
PARSE for zeta until the missing carrier (R1) and base (PROP-global) are built.

## 4. Tasks 3 and 4: why F_q coincides and what breaks it over Z (the load-bearing finding)

This is the one genuinely new localization. The function-field coincidence "generic =
sharp" is real (2G/2T), and its cause is now pinned to a single mechanism that fails
in exactly two independent ways over Z.

### 4a. Over F_q: generic and sharp coincide, exact (computed)

The genus-1 primitive intersection form is M = [[-2, -t], [-t, -2q]] with
t = q + 1 - N the integer Frobenius trace. Sharp positivity (RH for the curve) =
M negative-definite = det = 4q - t^2 > 0 = |t| < 2 sqrt(q) (Hasse-Weil).
"Non-degenerate" = det != 0 = M has no zero eigenvalue = |t| != 2 sqrt(q).

Computed across q in {5, 7, 11, 13} (e2g/e2t data, re-checked here): for every
admissible integer t, non-degenerate and definite agree. The reason is exact:

- t is an INTEGER (t = q + 1 - #C(F_q)).
- the boundary |t| = 2 sqrt(q) is IRRATIONAL for q prime (and any non-square q).
- so the integer lattice of admissible traces NEVER lands on the boundary.

Hence over F_q there is no room between non-degenerate and definite: the would-be
"excluded boundary locus" |t| = 2 sqrt(q) is empty on the integer spectrum. Two
structural facts force this:

- FINITE spectrum: g (genus) eigenvalue pairs, a finite integer datum t.
- ONE circle: all Frobenius eigenvalues have the same modulus target sqrt(q), one
  scale q, so the boundary is a single number 2g sqrt(q), not an accumulation set.

### 4b. Over Z: the coincidence breaks twice, independently

The boundary in the zeta picture is Re(s) = 1/2. Two facts each independently
destroy the F_q coincidence:

1. INFINITE spectrum that ACCUMULATES at the boundary. Riemann-von Mangoldt:
   N(T) ~ (T / 2pi) log(T / 2pi), mean gap ~ 2pi / log(T / 2pi) -> 0. The zeros
   accumulate toward the critical line; the spacing shrinks to zero. So the boundary
   Re = 1/2 is the accumulation locus, not an empty irrational gap. An off-line zero
   at beta = 0.51 sits arbitrarily close to the line, inside any neighborhood a
   generic statement is allowed to except. (Computed: ~44 zeros below T = 100,
   ~1.9e6 below T = 1e6.)

2. MULTI-SCALE: the (1, p) place-dependent bidegree (#25). Over F_q there is one
   circle sqrt(q). Over Z the Frobenius correspondence Gamma_S has bidegree (1, p)
   at the fibre over p, so there are INFINITELY MANY distinct circles sqrt(p), one
   per prime. The "boundary" is no longer a single number; it is a regularized join
   across infinitely many scales (the e2ad per-prime sqrt(p) scale mismatch; the M =
   A_arch + P_fin + B_pole assembly of 2K/3M). A generic (single-scale, single nef
   class) index theorem has no native way to be sharp simultaneously across all
   scales.

### 4c. The synthesis: two layered gaps, both real

Over F_q the spectrum is finite + single-circle, so (i) there is no accumulation at
the boundary and (ii) there is one scale; the generic index theorem is automatically
sharp. Over Z BOTH properties fail. The marginal-positivity wall (#18/#19/#27/#34:
no buffer at the boundary, the off-line obstruction sits below the reconstruction
floor) is the shadow of property (i)'s failure: accumulation at the line means there
is no margin to spare. The generic-vs-sharp gap is the shadow of BOTH (i) and (ii):
a generic statement may except the measure-zero accumulation set AND cannot pin all
scales at once.

So the sharp case IS the marginal wall in the precise sense that both are caused by
the accumulation of an infinite spectrum at the boundary. But the generic-vs-sharp
gap carries an EXTRA layer (the multi-scale (1,p) obstruction) that the marginal-wall
framing alone does not name. The two are not identical; the generic-vs-sharp gap is
strictly the larger of the two.

## 5. Task 3 settled: can generic be bootstrapped to sharp?

NO, by a limiting/density argument, for a structural reason. Bootstrapping
"definite off a special locus" to "definite everywhere" by density requires the
special locus to be approachable by non-special points on which the form stays
uniformly bounded below. But:

- the marginal wall (#18/#19) is exactly the statement that there is NO uniform
  lower bound as one approaches the boundary: the margin -> 0 (the e2w stealth
  window, the e3m floor). A density/limit argument would need a buffer that #18/#19
  prove is absent.
- over Z the accumulation of zeros at the line means the "non-special" approximants
  get arbitrarily close to the would-be off-line exception, so any uniform bound is
  exactly what fails.
- there is no rigidity statement available, because rigidity (Bogomolov-style: dense
  small points force special type) is precisely the GENERIC theorem; it does not
  upgrade to "every individual point is controlled."

So the boundary case is provably the hard core: it is the marginal-positivity finding
restated (zero buffer at the boundary) PLUS the multi-scale obstruction. Generic
positivity cannot be bootstrapped to sharp by soft means; a sharp proof must engage
the exact accumulation + multi-scale structure, which is M4.

## 6. D-H discipline

The generic-vs-sharp distinction does not even make sense for Davenport-Heilbronn,
which is the firewall working correctly:

- D-H is the L-function of no variety (no Euler product => no Frobenius => no motive
  => no abelian scheme => no Betti form => no Neron-Tate height). Neither Yuan-Zhang
  nor Gao-Habegger applies: there is no object to be generically or sharply positive.
- so a positivity that "worked for D-H" cannot arise from this theorem cluster at
  all; the cluster is unbuildable for D-H by type (2L section 5, 08A section 3 K2).
- conversely, this is also why the cluster gives no leverage on zeta: its entire
  zeta-vs-D-H discriminating power is delegated to the unbuilt carrier + base, so it
  has not entered the discipline's domain (2L section 5, the hollow-survival reading).

The D-H off-line zero at 0.8085 + 85.699 i has beta = 0.8085. In the marginal-wall
picture this is a (gross) off-line zero; in the Yuan-Zhang picture it is nothing,
because D-H has no Yuan-Zhang object. The two framings agree that D-H is excluded,
for the same root reason (no variety). This confirms the gap localized here is
zeta-only and is not a soft positivity that D-H could satisfy.

## 7. New-vs-re-cataloging self-assessment

GENUINELY NEW (and verified):

- The precise parse that "generic" in Yuan-Zhang/Gao attaches to the HYPOTHESIS
  (non-degeneracy of the Betti form / non-special locus) and the CONCLUSION is sharp
  on its own object. This corrects the prompt's natural-but-imprecise framing
  ("RH true on a generic set") and shows the gap "generic vs sharp" is not a
  measure-zero exception in the verdict but a degenerate-base-geometry condition in
  the hypothesis.
- The two-independent-breaks localization (Task 4): the F_q coincidence
  generic = sharp has a single cause (finite + single-circle spectrum => integer
  lattice misses the irrational boundary), and over Z it breaks in TWO logically
  independent ways (infinite accumulating spectrum; multi-scale (1,p) bidegree). The
  generic-vs-sharp gap is therefore STRICTLY LARGER than the marginal wall: it
  contains the marginal wall (the accumulation break) plus the multi-scale break.
  This is a new relation between two previously-separately-named obstructions
  (#18/#19 marginal wall; #25 (1,p) bidegree).
- The category mismatch (Task 2): the generic-vs-sharp gap and the
  RH-generically-vs-everywhere gap are not the same gap and there is no functor
  between them, because the carrying object does not exist for zeta. This sharpens
  the firewall.

MERELY RE-CATALOGING:

- That the sharp/boundary case is the hard core, with zero buffer, is the
  marginal-positivity finding (#18/#19/#27/#34) restated. The contribution is the
  CAUSAL link to accumulation, not the wall itself.
- The D-H section is a faithful restatement of 2L section 5 / 08A K2 (D-H has no
  variety, so the cluster is unbuildable for it).
- The no-bootstrap conclusion (Task 3) is the project's standing "M3 must be
  analytic; soft/density arguments fail at the marginal floor" (08A, the M2.5/M2.6/M3
  chain), now attached specifically to the generic-to-sharp upgrade.

Net: this front produced a precise localization (the generic-vs-sharp gap = marginal
wall PLUS the multi-scale break, with a verified causal account and a category-
mismatch firewall), not a construction and not new leverage. It is a coordinate: it
tells a future builder that bootstrapping any generic arithmetic-Hodge-index
positivity to sharp over Z must simultaneously (i) defeat the accumulation/no-buffer
floor and (ii) reconcile the infinitely many sqrt(p) scales, and that no soft/density
or rigidity argument can do either. That is exactly M4.

## 8. Verification targets (for VERIFIER) and adversarial tests (for ADVERSARY)

VERIFIER (Lean / Mathlib, or a clean numerical re-check):

- V1. Over F_q (genus 1): for q prime, the integer-trace lattice never meets the
  boundary |t| = 2 sqrt(q); hence "primitive form non-degenerate" and "primitive
  form definite" are equivalent on admissible t. (Elementary: 2 sqrt(q) irrational
  for q prime.) This is the formal core of the F_q coincidence.
- V2. Riemann-von Mangoldt density forces zero spacing -> 0, so the critical line is
  an accumulation locus of the zero set. (Mathlib has the zero-counting asymptotics
  ingredients; the spacing-to-zero corollary is the target.)

ADVERSARY:

- A1. Try to exhibit a single object (any cohomology / height theory in the repo's
  scorecard) on which BOTH a Yuan-Zhang-type generic positivity holds AND zeta's
  off-line zeros would land in the excluded special locus. (Claim: impossible; the
  category mismatch of section 3. If found, the firewall is wrong.)
- A2. Attempt a density/limit bootstrap from generic to sharp that does NOT require a
  uniform lower bound at the boundary. (Claim: impossible by #18/#19; if a buffer-free
  bootstrap exists it would contradict the e2w stealth-window finding.)
- A3. Confirm the cluster is unbuildable for D-H (no Betti form, no height), so no
  generic-vs-sharp positivity here can be D-H-blind-and-passing. (Expected: confirms
  firewall.)

## Connections

- 2L ([2L](2L_arakelov_face_probe.md)): the Arakelov-face probe; the BSD severance;
  PROP-global = the base; the strictly-weaker carrier this front prices.
- 2K ([2K](2K_spec_z_squared_dictionary.md)): M = A_arch + P_fin + B_pole; the (1,p)
  bidegree; the multi-scale break.
- e2g/e2t ([e2g](e2g_intersection_signature.md), 08A M1): the F_q template; the
  primitive form whose definiteness = Hasse-Weil; the single-circle finiteness.
- e2h ([e2h](e2h_arithmetic_hodge_index.md)): Faltings-Hriljac sharp per single
  surface (ranks 1-3), the precedent that sharpness IS attainable when the object
  exists.
- e2ad ([e2ad](e2ad_fh_gamma_certificate.md)): the per-prime sqrt(p) scale mismatch;
  the two withdrawn moves (not re-made here); height-to-L = BSD.
- 08A ([08A](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md)):
  M2.5/M2.6/M3 chain (M3 must be analytic; the marginal floor); M4 = the sharp
  arithmetic Hodge standard conjecture.
- spec_z landscape: Yuan-Zhang fixed-scheme; PROP-global / PROP-rh-equivalent /
  PROP-noncircular; the master "trace everywhere, polarization nowhere" thesis.
- Marginal-positivity thesis (#18/#19/#27/#34): the no-buffer wall, here causally
  attached to spectral accumulation at the line.
