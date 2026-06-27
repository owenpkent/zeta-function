# 2M: the Arakelov-side M4 construction attempt (three fronts, one wall)

> Direction 8 / Arakelov-face follow-up. [2L](2L_arakelov_face_probe.md) (LEARNINGS
> #131) localized the Arakelov face as the MIRROR of the AHK failure: it has a genuine
> carrier and a genuine proven per-surface polarization, but dies at the BASE (the
> nonexistent `Spec(Z) x Spec(Z)` + `Gamma_S`, = PROP-global, bundled with R1). 2L's
> recommended next step was: stop surveying, attack the BASE by attempting the
> strictly-construction-weaker object directly. This dossier executes that, in the
> shape of the #128 three-front M4 attempt: three BUILDER fronts, each adversarially
> attacked, each asking whether the Arakelov side can produce an actual construction
> (not another all-roads re-statement). Fronts: (1) carrier-spectrum-severance, (2)
> sharp-vs-generic, (3) (1,p)-bidegree-assembly. Companions: [2L](2L_arakelov_face_probe.md),
> [2K](2K_spec_z_squared_dictionary.md), [e2ad](e2ad_fh_gamma_certificate.md),
> [sourcing_gap_r1](../../docs/03_research/sourcing_gap_r1.md).

## 1. Headline verdict

The attempt produced a SHARP NO-GO with one genuinely-new invariance, not a candidate
construction, and the rest is honest re-cataloging of the already-named gap. The single
most important thing learned, surviving all three adversaries: on the BEST concrete
motivic carrier the program can name (Kuga-Sato / the universal elliptic curve over a
modular curve, the one carrier that GENUINELY realizes a degree-2 L-function via
Eichler-Shimura, unlike AHK which has no carrier at all), the cohomology that REALIZES
the L-function (Galois `H^{k-1}_et`, Frobenius eigenvalue moduli = the L-zeros) and the
object that Yuan-Zhang POLARIZES (the arithmetic Chow group `CH-hat^1_0`, the height
pairing) are DISTINCT, ORTHOGONAL cohomologies on the same carrier. This pins WHY having
a real carrier still does not help: realize and polarize sit on orthogonal cohomologies
even when both are present, and their only coincidence is the GEOMETRIC Hodge index on
middle cohomology, which is the function-field case (Deligne, already a theorem, over
`F_q` not over `Z`) and does not transport. This is the same universal-gap wall as 2L
#131 / #128, reached this time from the construction side and made invariant across the
candidate carrier list. It moves the wording, not the open kernel.

All three fronts SURVIVED their adversary as correct no-go / re-cataloging coordinates.
None produced a construction. The marginal-positivity / D-H discipline held throughout
by NON-MIMICRY (Davenport-Heilbronn is the L-function of no motive, so it has no carrier,
no `Frob_p`, no `H^{k-1}_et`, no `CH-hat` to enter any of the three constructions), and
the survival is hollow in the recorded sense: all zeta-vs-D-H discriminating power stays
delegated to the unbuilt `Gamma_S`.

## 2. Per-front results

### Front 1: carrier-spectrum-severance

**Construction attempted.** Carrier = the Kuga-Sato variety / universal elliptic curve
over a modular curve, the one carrier whose cohomology genuinely realizes a degree
`>= 2` L-function (Eichler-Shimura-Deligne). REALIZE side: the geometric Frobenius
`Frob_p` on the 2-dim Eichler-Shimura piece `M_f` of `H^{k-1}_et(W_Qbar, Q_l)`, char
poly `X^2 - a_p X + p^{k-1}` (the Frobenius eigenvalue moduli = the L-zeros). POLARIZE
side: the Yuan-Zhang / Faltings-Hriljac arithmetic intersection (= Neron-Tate height) on
`CH-hat^1_0` of the arithmetic model. Worked exactly at weight 2 on `E = 37a1`:
REALIZE gives `|alpha_p|^2 = p` on every good `p` (disc `a_p^2 - 4p < 0`, `p = 2..43`),
POLARIZE gives the `p`-independent `O(1)` regulator `<P,P> = 0.051111`.

**Where it walls (the open step, sharply).** The wall is the disjointness of two
cohomological objects on the SAME carrier: REALIZE lives on Galois `H^{k-1}_et(W_Qbar)`
(eigenvalue moduli = zeros), POLARIZE lives on `CH-hat^1_0` over `Z` (the height
pairing = the Yuan-Zhang negative-definite signature). The only coincidence is the
GEOMETRIC (not arithmetic) Hodge index on middle cohomology = the function-field case
(Deligne, a theorem), living over `F_q` on geometric cohomology, NOT over `Z` on the
arithmetic Chow group where the global modular zeros sit. The open step: produce a single
arithmetic carrier on which the SAME pairing both polarizes (negative-definite primitive)
AND has its polarized spectrum equal the global Frobenius/flow spectrum carrying `L(f)`'s
zeros across all places. That is the unbuilt `Gamma_S` / PROP-global bundled with R1,
unchanged from 2L.

**Residue that survived the adversary.** The orthogonality of REALIZE and POLARIZE on a
single genuine carrier, pinned to the one coincidence point (the geometric Hodge index =
Deligne over `F_q`, which fails to transport to `Z`). The verified computational facts:
`a_p(37a1)` for `p = 2..43` independently re-derived by point counting (all disc `< 0`,
so `|alpha_p|^2 = p`); regulator `0.051111` = the LMFDB canonical height; K1-clean (only
point counts + the curve's own height; no zeros input); D-H control 9/9. The
GENUINELY-NEW survivor: the severance is INVARIANT across the candidate carrier list
(Kuga-Sato, arithmetic-surface self-product, abelian variety over a Shimura variety),
all failing identically by the same realize/polarize split. The front correctly does NOT
re-make either withdrawn e2ad move: it uses the full `CH-hat^1_0` regulator (not a single
`(0,0)` entry), and it cites the BSD L-link as the OBSTRUCTION (not a bridge).

**Adversary deflations folded in (the builder's self-label was generous).** The three
advertised "independent severance proofs" are re-namings of already-cataloged findings:
"scale divergence" = #25 (the place-dependent `(1,p)` bidegree); "operator mismatch" =
#30 / the spec_z master thesis (trace vs signature); "BSD L-link" = disqualifier #113 /
e2ad. They are ONE known gap (realize-vs-polarize on orthogonal cohomologies) seen from
three angles, not three independent results. The headline numeric ("ratio
`sqrt(43)/0.051111 = 1.28e2`, divergent in `p`") is a dimensional category mismatch: it
compares a per-prime LOCAL `|alpha_p| = sqrt(p)` against a GLOBAL `p`-independent
regulator with no prime index, so "does not grow with `p`" is vacuously true of any
global invariant and proves nothing about severance vs relatedness. It is downgraded to
an illustration; the structural orthogonality is the only load-bearing content.

**Honest classification: NO-GO (precise, worked, on the best carrier), but the analysis
is mostly RE-CATALOGING of #25/#30/#113 and 2L #131, with one genuine minor sharpening
(the invariance across the carrier list).**

### Front 2: sharp-vs-generic

**Construction attempted.** None. The front was a LOCALIZATION of the generic-vs-sharp
positivity gap, examining (1) the Yuan-Zhang arithmetic Hodge index for adelic line
bundles (Math. Ann. 367, 2017), a SHARP negative-(semi)definite signature on the
primitive part against a fixed nef class, on a FIXED scheme; and (2) the
Gao-Habegger / Cantat-Gao-Habegger-Xie (Duke 170(2), 2021) geometric Bogomolov engine,
whose positivity is NON-DEGENERACY of the Betti form off a special locus. The `F_q`
template (e2g / e2t): genus-1 primitive form `M = [[-2, -t], [-t, -2q]]`, RH-for-curve =
`M` negative definite = `|t| < 2 sqrt(q)` (Hasse-Weil); over `Z` the analogue is
`M = A_arch + P_fin + B_pole` with the pole block as the single hyperbolic direction and
the `(1,p)` bidegree giving infinitely many circles `sqrt(p)`.

**Where it walls (the open step).** Four tasks, each landing on the same place with a
sharper diagnosis: (1) "generic" attaches to the HYPOTHESIS (Betti-form
non-degeneracy / non-special locus = excluded degenerate base geometry), not a
measure-zero exception in the sharp conclusion. (2) The excluded locus is NOT where a
zeta off-line zero lives, because zeta has no Yuan-Zhang object at all (no abelian
scheme, no Betti form, no Neron-Tate height for its zeros): the two gaps live in
different categories. (3) Generic cannot be soft-bootstrapped to sharp: a density / limit
argument needs a uniform lower bound at the boundary, which the marginal wall (#18/#19,
e2w stealth window, e3m floor) proves absent, and rigidity gives no per-point control.
(4) Over `F_q`, generic = sharp because the spectrum is FINITE + on ONE circle, so the
integer trace lattice misses the irrational boundary `2 sqrt(q)`; over `Z` this breaks.
The exact open step: SHARP (not generic) arithmetic Hodge-standard positivity on the
primitive part of an object that simultaneously defeats the accumulation / no-buffer
floor and reconciles the infinitely many `sqrt(p)` scales = M4.

**Residue that survived the adversary.** (a) The `F_q` template signature = Hasse-Weil
for genus 1 (e2g, K1-clean, K3 = Weil 1948), independently re-verified across
`q in {5,7,11,13}`. (b) The category-mismatch firewall (zeta has no Yuan-Zhang object
until R1 + the base are built) = 2L section 5 / spec_z NODE-fh-too-local, correct and
faithful. (c) The no-soft-bootstrap conclusion (density needs a uniform boundary lower
bound that the marginal wall proves absent) = 08A M2.5/M2.6/M3 chain, correct and
faithful. (d) The D-H firewall (the cluster is unbuildable for D-H by type) = correct,
control 9/9. The front did NOT re-make either e2ad-withdrawn move (no `(0,0)`-entry = FH
claim; no `Gamma_S`-assembles-the-FH-height claim; height-to-L correctly stated as BSD
central derivative at `s = 1` only).

**Adversary deflations folded in (two corrections).** The ONE piece advertised as
genuinely new, the claim that the generic-vs-sharp gap is "STRICTLY LARGER than / CONTAINS"
the marginal wall plus the multi-scale break, does NOT survive: it is internally
inconsistent with the front's own Task-2 firewall. A containment / ordering relation is a
relation WITHIN one structure, and cannot coexist with "no functor / different
categories / does not parse for zeta." The two gaps coincide over zeta ONLY through the
unbuilt `Gamma_S`, so the containment statement quantifies over a nonexistent object and
is vacuous. WITHDRAWN; the honest residue is a parallel-failure observation (over `F_q`
the coincidence has two structural enablers, finiteness and single-circle, both of which
fail over `Z`), not a containment. Second correction: VERIFIER target V1 must be
restated. "Non-degenerate `<=>` negative-definite" holds on ADMISSIBLE traces only
(`|t| <= 2 sqrt(q)`, the Hasse bound, a theorem), NOT on the full integer lattice
(counterexample `t = 5, q = 5`: det `= -5 < 0`, indefinite non-degenerate). Irrationality
of `2 sqrt(q)` only upgrades `<=` to `<`; the load-bearing fact is Hasse-Weil = e2g.
(Minor non-load-bearing slip: `~44` zeros below `T = 100` should be `29`; the mean-gap
`-> 0` conclusion is unaffected.)

**Honest classification: NO-GO / almost entirely RE-CATALOGING (the universal gap
restated, plus a true-but-minor irrationality footnote that needs the V1 correction),
with one advertised-new claim (strictly-larger / contains) that is unsound and is
WITHDRAWN. Not a construction.**

### Front 3: (1,p)-bidegree-assembly

**Construction attempted.** The only front to attempt an actual ASSEMBLY (e2ad verified
per-prime Hasse but never assembled). Per-prime `(1,p)`-bidegree primitive Gram
`G_p = [[-2g, -t_p], [-t_p, -2g p]]`, `t_p = p + 1 - #X(F_p)`, each negative definite iff
`t_p^2 < 4 g^2 p` (per-prime Hasse, a theorem). The pairing being assembled is the 2K
dictionary `M = A_arch + P_fin + B_pole`; Yuan-Zhang's adelic-line-bundle index theorem
is the natural assembly machinery (bundles all places into one scalar
`<L,L> = sum_v <L,L>_v`). Realized fibre-by-fibre on three carriers (11a1, 389a1,
genus-2 `y^2 = x^5 + x + 1` on its good primes) with three assembly models: (A) single
common scale, (B) the Yuan-Zhang adelic block collapsed to a single scalar, and the
archimedean-rank test.

**Where it walls (the open step).** The wall is the `(2,2)` slot of `G_p` (the
`f.Gamma_p = p` bidegree). Normalizing row/column 2 by `sqrt(p)` is the only scale making
the per-prime forms comparable, and it is `p`-dependent: no single scale works because
the diagonal asymmetry (slot11 `= -2g` constant vs slot22 `= -2g p`) is unbounded in `p`.
Yuan-Zhang's all-places collapse to a single scalar removes the `p`-many distinct matrix
scales, but only by summing the off-diagonal couplings into a single prime-side series,
whose sign and growth are NOT controlled by the per-prime bound `|t_p/sqrt(p)| < 2g`. The
single archimedean place (rank 1) cannot host the `p`-indexed scale family. So the adelic
structure RELOCATES the #25 scale mismatch from `p` incompatible matrix scales into one
regularized RH-gated prime sum; it does not dissolve it. Proving that scalar has the
right sign IS M4, untouched. The open step: SHARP arithmetic Hodge-standard positivity of
the single adelic scalar / the primitive part, inheriting both variety-gated facets R1
(Deligne purity of a `sqrt(p)`-weight-1 carrier) and M4 (Weil/Rosati polarization).

**Residue that survived the adversary.** (1) The `(1,p)`-bidegree primitive Gram is
negative definite for every good prime of the two genuine g=1 carriers (11a1, 389a1) =
Hasse, a theorem, K1-clean, integer-exact (all numbers reproduced independently). (2) The
no-single-scale fact (the normalizing scale is exactly `sqrt(p)`, `p`-dependent, with
unbounded forced-single-scale diagonal asymmetry). This is the load-bearing fact, and it
IS the #25 `(1,p)`-bidegree obstruction; the only delta is the 2x2 intersection-pairing
vocabulary (vs e2ad's moment-Gram), which the writeup concedes. (3) The front does NOT
re-make either withdrawn e2ad move (no FH-as-single-entry, no `Gamma_S`-assembles-the-
height; only the Euler/Frobenius trace side enters). K1-clean; K2 pass-by-non-mimicry.

**Adversary deflations folded in (three corrections).** (i) The headline "Yuan-Zhang
adelic bundling RELOCATES rather than dissolves the #25 mismatch" is already the verdict
of e2ad, 2L, and 2K; the per-prime `sqrt(p)` mismatch is #25 verbatim. (ii) The one
advertised-new object is MIS-IDENTIFIED: the front claims the relocated single adelic
scalar IS the `P_fin` / von Mangoldt explicit-formula prime block, computed as
`sum_p t_p/sqrt(p)`. It is not: the explicit-formula prime block is
`sum_{p,k>=1} a_{p^k} p^{-k/2} (log p) f-hat`, carrying a `log p` weight, prime-power
(`k >= 2`) terms, and a test function, all of which `sum_p t_p/sqrt(p)` drops. The
relocation is right in spirit (per-place definite, global scalar uncontrolled by per-place
bounds) but the specific arithmetic identification fails. (iii) The genus-2 "carrier" is
a relabeled genus-1 computation: it forces `g = 1` into the Gram and uses a scalar `t_p`
as the single off-diagonal, whereas genuine genus-2 Hodge index has `2g = 4` Frobenius
eigenvalues, Weil bound `|t| <= 4 sqrt(p)`, and the `(g+1) x (g+1)` Toeplitz moment
structure of e2vv (#123). The code uses the wrong bound (`2g = 2` vs `4`). So there are
TWO genuine carriers (both g=1), not three; this does not flip the no-go verdict.

**Honest classification: NO-GO with a genuine K1-clean ASSEMBLY computation (the one new
artifact), but adding NO localization beyond #25/e2ad/2L; mostly RE-CATALOGING of #25
with one mis-identified scalar and one overstated genus-2 carrier. Not a construction.**

## 3. The convergence

YES, all three fronts wall at the SAME place, exactly as the #128 three-front M4 attempt
converged. The place is the ALREADY-NAMED gap, not something new:

- Front 1 walls at orthogonality of REALIZE (`H^{k-1}_et`, Frobenius spectrum = zeros)
  and POLARIZE (`CH-hat^1_0`, the height pairing) on a single carrier = the realize-vs-
  polarize split = the universal trace-vs-signature thesis, missing the base `Gamma_S`.
- Front 2 walls at SHARP (not generic) positivity on a primitive part that defeats the
  marginal / no-buffer floor and reconciles the `sqrt(p)` scales = M4 = the same gap, with
  the carrier and base unbuilt (the category-mismatch firewall).
- Front 3 walls at the sign of the single adelic scalar into which the `(1,p)` bidegree
  relocates = M4 / PROP-global, the `Gamma_S` assembly = the same gap.

This is the FIRST construction-side three-front convergence onto the Arakelov base
specifically (the #128 convergence was on the analytic Euler-trace-vs-signature gap; this
one is on the Arakelov realize-vs-polarize / `(1,p)`-assembly gap). The convergent place
decomposes as the SAME two variety-gated facets recorded in `sourcing_gap_r1.md` plus the
base: R1 (sourcing / Deligne-purity of a `sqrt(p)`-weight-1 carrier) + M4 (the
Weil/Rosati polarization / SHARP Hodge-standard positivity) + PROP-global (the base
`Spec(Z) x Spec(Z)` / `Gamma_S` that attaches per-motive positivity to zeta's actual
zeros). The marginal wall (sharp-vs-generic = the no-buffer floor) is what makes the
SHARP step non-soft. No new gap. The convergence is itself the result: three
independently-constructed Arakelov-side attacks land on one wall, confirming the wall is
structural, not a defect of any single front's choice.

## 4. The computed artifacts

Two K1-clean Python artifacts (Front 1 and Front 3) plus one localization markdown
(Front 2). None committed to git.

**Front 1: `e2ag_carrier_severance.py`** (`python -m experiments.arithmetic_geometric.e2ag_carrier_severance`,
mpmath, 40 dps). REALIZE side, `E = 37a1`: `a_p` for `p in {2..43}`, disc `= a_p^2 - 4p
< 0` on every good `p` (e.g. `p = 43`: `a_p = 2`, disc `= -168`), so `|alpha_p|^2 = p`
(the per-prime Hasse / Ramanujan circle). POLARIZE side: Neron-Tate regulator
`<P,P> = 0.051111` (`P = (0,0)`, validated against LMFDB in 2H). Validation: D-H control
9/9. K1-clean (only point counts `a_p` + the curve's own height; no zeros input). The
"divergent ratio" was downgraded by the adversary to an illustration (category mismatch),
not load-bearing; the load-bearing content is the structural orthogonality.

**Front 3: `e2af_adelic_assembly.py`** (`python -m experiments.arithmetic_geometric.e2af_adelic_assembly`,
numpy + sympy). All per-prime `G_p` negative definite (Hasse) for 11a1, 389a1, genus-2-on-
good-primes across the first 15 primes; `|t_p/sqrt(p)| < 2g = 2` at every prime (max 1.89
at 389a1 `p = 7`). Model A: scale spread max/min `= 4.8477`, single common scale exists =
False, forced-single-scale diagonal asymmetry grows as `p/p_mid` (2.47 full list, 1.62
genus-2 good-prime list). Model B: block-diagonal definite only with per-block scale
`sqrt(p)`; single adelic scalar = regularized diagonal (`-2g * #primes`, e.g. `-30` for
15 primes) + prime-side coupling sum (11a1: `-0.83`; 389a1: `-9.62`; genus-2: `-2.41`);
389a1 partial sums `[-1.41, -2.57, -3.91, -5.80, -7.01, -7.84, -9.29, -8.15, ...]`.
Model B archimedean test: distinct per-prime scales 15 (12 genus-2) vs archimedean rank
1, rank deficit 14 (11). Genus-2 restricted to good primes (disc `= 3 * 7^2 * 23` via
sympy, drops 3, 7, 23). Artifact `e2af_adelic_assembly.npz`. Validation: assertions pass,
D-H control 9/9. K1-clean (only point counts enter; no zeta zeros). Adversary caveats:
the single-scalar = `P_fin` identification is mis-stated (the bare sum drops `log p`,
`k >= 2`, and the test function); the genus-2 entry is a relabeled g=1 Gram (wrong Weil
bound). So the artifact correctly DEMONSTRATES the no-single-scale relocation, but two of
its labels overstate; both are corrected here.

**Front 2: `2M_generic_vs_sharp_localization.md`** (no new numerics beyond e2g/e2t
re-checks). Two K1-clean re-verifications: the `F_q` coincidence (genus-1 form, `q in
{5,7,11,13}`, nondeg = def on ADMISSIBLE traces per the V1 correction) and the Z-side
accumulation (Riemann-von Mangoldt mean gap `~2.27` at `T = 100`, `~0.52` at `T = 1e6`,
`-> 0`). D-H control 9/9.

All artifacts K1-clean and D-H-controlled. The one VERIFIER target needing restatement
is Front 2's V1 (the `F_q` coincidence holds on admissible traces = the Hasse bound, not
on the full integer lattice).

## 5. New-vs-re-cataloging self-assessment (per the e2ad caution)

GENUINELY NEW (and adversary-verified):

- **Front 1's invariance result.** The realize-vs-polarize severance is INVARIANT across
  the concrete motivic carrier list (Kuga-Sato, arithmetic-surface self-product, abelian
  variety over a Shimura variety), all failing identically by the orthogonal-cohomologies
  split. This sharpens 2L's "mirror not escape" from one carrier to the carrier CLASS:
  no single arithmetic variety escapes, because realization and polarization sit on
  orthogonal cohomologies even when both are present. This is a real, minor sharpening.
- **Front 3's assembly artifact `e2af_adelic_assembly.py`.** e2ad verified per-prime
  Hasse but never attempted the intersection-pairing ASSEMBLY; this is the first explicit
  attempt, with a new K1-clean computation (no-single-scale, the regularized-scalar split,
  the archimedean rank deficit). The COMPUTATION is new; the CONCLUSION it reaches (#25
  relocation) is not.
- **The construction-side three-front convergence onto the Arakelov base** (section 3):
  the first time three independently-built Arakelov-side attacks are shown to land on one
  wall (the realize-vs-polarize / `(1,p)`-assembly gap), confirming the wall is structural.

MERELY RE-CATALOGING (the open kernel is UNCHANGED):

- Front 1's "three independent severance proofs" = re-namings of #25 (scale = the `(1,p)`
  bidegree), #30 / the spec_z master thesis (operator = trace vs signature), and #113 /
  e2ad (BSD L-link). One known gap from three angles. The headline numeric is a category
  mismatch, downgraded to illustration.
- Front 2's structural conclusion = the universal-gap verdict restated (the category-
  mismatch firewall = 2L section 5; no-soft-bootstrap = 08A M2.5/M2.6/M3; D-H firewall =
  spec_z FH row). Its one advertised-new claim (generic-vs-sharp "strictly larger / contains"
  the marginal wall) is UNSOUND and WITHDRAWN (it contradicts the front's own firewall and
  is vacuous over the unbuilt `Gamma_S`).
- Front 3's headline relocation = #25/e2ad/2L verbatim; the new wrapper is the 2x2
  intersection-pairing vocabulary. The advertised-new scalar = `P_fin` identification is
  MIS-STATED (corrected). The genus-2 carrier is a relabeled g=1 computation (corrected to
  two genuine carriers).

NET HONEST ACCOUNTING: the attempt produced ONE correct minor sharpening (Front 1's
carrier-class invariance), ONE new K1-clean computation (Front 3's assembly, whose
conclusion is not new and two of whose labels were overstated), and ONE construction-side
convergence localization. Its structural conclusion is a CONSOLIDATION of the already-
established universal-gap verdict (R1 + M4 + PROP-global, the same place 2L #131 reached),
not new leverage on the open kernel. Three would-be-new claims did not survive: Front 1's
divergent-ratio numeric (category mismatch), Front 2's "strictly larger / contains"
relation (vacuous), and Front 3's scalar = `P_fin` identification (wrong object). This is
fully consistent with the e2ad caution: more all-roads / Arakelov re-cataloging is not
where the leverage is. Self-labels of "mixed" on all three fronts are generous; "mostly
re-cataloging with one genuine sharpening apiece, two of which did not survive" is the
accurate accounting.

D-H discipline (all three fronts): held by NON-MIMICRY. Each construction requires the
carrier to be an actual motive (Eichler-Shimura, `Frob_p`, `CH-hat`, per-prime
`t_p = p + 1 - #X(F_p)`); Davenport-Heilbronn is the L-function of no motive (no Euler
product, no carrier, no `Frob_p`, no `H^{k-1}_et`, no `CH-hat`), so it cannot even ENTER
any of the three constructions. No positivity claim in any front would "work" for D-H.
Control 9/9 across all fronts. The pass is K2-clean by structure but HOLLOW in the
marginal-positivity sense: the entire zeta-vs-D-H discriminating content is delegated to
the unbuilt `Gamma_S` (= R1 + M4), so the face has not entered the discipline's domain
with any positive zeta claim. This is the recorded 2L reading, unchanged.

## 6. Recommended next step

The honest answer: this is construction-grade, multi-year work, and the head-on Arakelov
attack has now WALLED from the construction side exactly where 2L predicted it would, with
the wall confirmed invariant across the carrier class. Three full construction fronts
converged on the same already-named gap (R1 sourcing + M4 polarization + PROP-global
base). The program should NOT spend the next loop on a fourth Arakelov front or another
survey: the universal gap is now triply-confirmed from the construction side and adding a
fifth all-roads coordinate is the exact pattern e2ad warned against.

Concretely, the recommended posture (in priority order):

1. **Spend the loop on isolable, RH-INDEPENDENT sub-pieces, not on M4 head-on.** The
   highest-value buildable residue is the Lean / VERIFIER targets that are theorems on
   their own: Front 3's per-prime Hasse 2x2 sign (VT1) and the no-single-scale
   impossibility (VT2) are K1-clean, integer-exact, and Lean-formalizable WITHOUT touching
   the open kernel. Formalize these as the Arakelov-side companions to the existing
   function-field Lean substrate (IsogenyDegree / FunctionFieldRH). They harden the
   localization and add to the publishable substrate; they do not pretend to close RH.
   **DONE (2026-06-27): `lean/ZetaRH/ArakelovAssembly.lean` (#2M-VT), sorry-free and
   axiom-clean (`#print axioms` = `[propext, Classical.choice, Quot.sound]`; full build
   green, 3745 jobs).** VT1 = `perPrime_negDef_iff_hasse` / `perPrime_negDef_of_hasse`
   (honestly a specialization of `negDef_iff_hasseWeil` at `q = p`); VT2 (the new content)
   = `conj_lowerRight` + `no_single_normalizing_scale` + `forced_scale_asymmetry_unbounded`,
   packaged in `assembly_obstruction` (both per-prime fibres negative definite, yet no
   single scale assembles them). The adelic-scalar SIGN (= M4) remains the open kernel,
   untouched.

2. **Watch for an EXTERNAL polarization theorem, do not try to manufacture one.** The
   open step (SHARP arithmetic Hodge-standard positivity of the single adelic scalar /
   primitive part, the polarization on the global product) is the same object every
   all-roads convergence has named. The realistic source is an external advance (a
   genuine `Spec(Z) x Spec(Z)` / `Gamma_S`, or a Deninger / prismatic / Hesselholt
   cohomology that carries BOTH the Frobenius spectrum AND a Rosati polarization on the
   global `H^1`). Maintain the spec_z landscape scorecard as the watch-list; the 2026
   Connes-Consani Jacobian is the closest trace-side datapoint and still carries no
   pairing.

3. **Cheap bookkeeping, do first.** Promote the two corrected VERIFIER targets (Front 2's
   V1 restated around the Hasse bound; Front 3's VT1/VT2). Record the three withdrawn /
   corrected claims (Front 1's divergent-ratio illustration-only status, Front 2's
   withdrawn containment claim, Front 3's mis-identified scalar and relabeled genus-2
   carrier) so no future session re-makes them, exactly as e2ad's two withdrawn moves are
   now respected by all three fronts here.

The frame for ORCHESTRATOR: 2M confirms the Arakelov face is the mirror AND that the
construction side of it walls at the same triple-facet gap (R1 + M4 + PROP-global). This
is a successful dead branch in the program's sense (a sharp coordinate with a verified
residue), not a failure. It does not move the open kernel. The remaining work is building
the base, the same place every convergence has left the program. Spend on isolable
sub-pieces and the external-theorem watch; do not run a fourth Arakelov front.

## Connections

- 2L ([2L](2L_arakelov_face_probe.md)): the mirror localization (#131) this dossier executes the next-step of.
- 2K ([2K](2K_spec_z_squared_dictionary.md)): the `M = A_arch + P_fin + B_pole` dictionary; the gap = the product surface.
- e2ad ([e2ad](e2ad_fh_gamma_certificate.md)): the height-to-L link = BSD central derivative at `s = 1` (the two withdrawn moves, respected by all three fronts).
- e2g / e2h: the `F_q` template + single-surface Faltings-Hriljac (the K3 = Weil 1948 baseline).
- e2vv ([#123]): the genuine genus-2 Toeplitz moment structure (Front 3's genus-2 "carrier" is NOT this; it is a relabeled g=1 Gram).
- `sourcing_gap_r1.md`: the two variety-gated facets (R1 sourcing + M4 polarization) the convergence decomposes into.
- `spec_z_cohomology_landscape.md`: NODE-ahk-too-blind vs NODE-fh-too-local; the 4-property M4 decomposition (PROP-global = the base).
- #25 (the `(1,p)` place-dependent bidegree), #30 (trace vs signature), #113 (BSD L-link), #18/#19 (the marginal / no-buffer wall): the cataloged findings the three fronts re-name.
- New artifacts: `e2ag_carrier_severance.py`, `e2af_adelic_assembly.py` (+ `.npz`), `2M_generic_vs_sharp_localization.md`.
