# The S4 slot on the CCM carrier: the majorant landscape audited, the skeleton posed, the slot measured empty

> Dossier, 2026-07-11. Assembled by SYNTHESIZER from the adversary-corrected SURVEYOR map
> (`scratchpad/s4_carrier/01_surveyor_majorants.md`, gitignored working file per the repo
> pattern) and the e1o probe
> ([`../../experiments/spectral/e1o_s4_carrier.md`](../../experiments/spectral/e1o_s4_carrier.md)
> + `.py`/`.npz`, 19/19 self-tests full and quick, adversary-reproduced). One ADVERSARY round
> over both artifacts, verdict PASS_WITH_FIXES twice (fixes applied in place; no claim demoted;
> several upgraded; report in `scratchpad/s4_carrier/03_adversary.md`). Arc provenance:
> LEARNINGS #161 named the S4/R1 proof-engine question on the CCM carrier as the sharpest live
> coordinate ([`landau_one_sided.md`](landau_one_sided.md) Sections 3.4-3.6/5); this arc executed
> its first survey + probe round; integrated as LEARNINGS #162.
>
> Status: the survey's two ABSENCE findings are verified at search depth; the DMV kill is
> VERIFIED (adversary, line by line; conditional on two SECONDARY-tier construction facts,
> stated); the probe's headline laws are NUMERICAL with adversary-derived structural covers;
> the S4 spec is CONJECTURE tier by construction. It proves nothing about RH.
>
> Cross-links: [`landau_one_sided.md`](landau_one_sided.md) (the translator this arc prices;
> its Section 2.2 carries this arc's adversary correction),
> [`sourcing_gap_r1.md`](sourcing_gap_r1.md) (the fourth analytic shape of the R1 slot, which
> this arc gives a measured negative baseline),
> [`parity_vs_polarization.md`](parity_vs_polarization.md) (the sieve factor 2 the probe
> derives and measures), [`ccm_semilocal_prolate.md`](ccm_semilocal_prolate.md) (the carrier's
> ledger), [`stepanov_engine_audit.md`](stepanov_engine_audit.md) (the S4 move this arc
> transplants). No em dashes.

## 1. The question

Can an operator-theoretic mechanism on the CCM prolate/PW carrier (the $D_{\log}$ family,
arXiv:2511.22755) produce a lambda-uniform ONE-SIDED bound `psi(x) <= x + C x^{1/2+eps}`
(the Landau threshold, which forces RH by
[`landau_one_sided.md`](landau_one_sided.md) Theorem A), the way Stepanov's S4 move (cheap
multiplicity buying a count upper bound) does over `F_q`? Two halves this arc executed:
what does the literature hold (Section 2), and what does the known cheap mechanism certify
when actually posed on the carrier (Section 4)?

## 2. The survey: two verified absences and a proven ceiling

Process rule (#157): every load-bearing statement tagged. [FETCHED] = read at source that
session. [SECONDARY] = verified via snippets or a citing paper fetched at source.
[UNVERIFIED-MEMORY] = model memory, not pinned. [REPO] = carried by an existing repo dossier.
Evidence base fetched at source: Revesz arXiv:2207.00665 pp. 1-5 (Beurling/DMV summary,
Eqs. 4-10); Lerma 1996 (Vaaler-advised extremal-functions report, 14 pp.); arXiv:2404.01003
(Brun-Titchmarsh history); Granville arXiv:2010.01211 abstract; CMS arXiv:1708.04122
abstract; CCM arXiv:2511.22755 abstract; Broucke-Vindas arXiv:2102.08478 abstract.

### 2.1 Stepanov on archimedean carriers: VERIFIED ABSENT

No published work transplants the Stepanov/Bombieri auxiliary-function engine (vanishing
budget paying for a sharp count UPPER bound) to any archimedean carrier: Paley-Wiener,
de Branges, or prolate/Sonin spaces. Three systematic searches (2026-07-11) returned only
the finite-field Stepanov corpus, de Branges structure theory with no arithmetic counting
content, and false cognates. ABSENCE IS THE FINDING, at search depth: the S4 slot on any
archimedean carrier is EMPTY in the literature, exactly as
[`stepanov_engine_audit.md`](stepanov_engine_audit.md) (#145) concluded from the engine side
and vF 2008 testified in his own words (#147) [REPO]. Calibration: the nearest archimedean
auxiliary-function tradition (Gelfond-Schnirelman, 1936) is LOWER-bound direction at
Chebyshev scale, with the univariate ceiling PROVEN unattainable (Gorshkov 1956; integer
Chebyshev constant in (0.4213, 0.4232)) [SECONDARY]; wrong direction AND wrong scale for the
Landau threshold. The repo's #149 Gauss floor is the same lcm-vs-polynomial trade run in
reverse [REPO].

### 2.2 The one-sided slot in Sonin spaces: also ABSENT (the second verified absence)

The one-sided extremal machinery (Beurling-Selberg; Graham-Vaaler; Carneiro-Littmann-Vaaler
Gaussian subordination; Carneiro-Littmann extremal problems SOLVED in de Branges spaces
H(E); Holt-Vaaler) and the Sonin/prolate-zeta corpus (Burnol's Sonine-as-de-Branges spaces;
Connes-Moscovici prolate operator, UV spectrum matching squared zeta zeros; the CCM carrier
itself) are BOTH alive and DISJOINT at search depth: no published work poses a
Beurling-Selberg-type one-sided extremal problem in a Sonine/prolate space, and no published
work connects prolate dimension/eigenvalue counts (Shannon, Landau-Pollak-Slepian) to an
arithmetic UPPER bound of any kind. Every published USE of the Sonin space in the zeta
program is FORM-SIDE (Weil positivity at the archimedean place, the M4-shaped route); the
counting-side use the S4/R1 arc wants has no precedent. The open door this maps (BUILDER,
not built in this arc): pose the Carneiro-Littmann extremal problem IN the Sonin space of
the CCM carrier; no literature collision found; whether it is even well-posed there (chain
structure, the right E-function) is open.

### 2.3 The factor-2 ceiling of the majorant/sieve family: PROVEN, twice

The strongest unconditional ONE-SIDED prime bound the entire majorant family has ever
produced is the factor-2 family (Brun-Titchmarsh and relatives; the majorant acts through
the large-sieve/BT pipeline, whose inputs are the sieve axioms). The 2 is literally the
square root in the level of support (`log D -> (1/2) log D`, Selberg `Lambda^2`)
[FETCHED via 2404.01003]. Status of the ceiling:

1. **Axiom-relative (parity), PROVEN**: Selberg 1949 sign-flip invariance; Bombieri 1976
   asymptotic sieve (`delta_x in [0,2]`, both endpoints realized). Carried at verified tier
   by [`parity_vs_polarization.md`](parity_vs_polarization.md) Section 1 (#146) [REPO].
2. **Conditionally numerically sharp**: Granville arXiv:2010.01211 [FETCHED abstract]:
   assuming infinitely many Siegel zeros, the (Rosser-)Jurkat-Richert linear-sieve bounds
   cannot be improved. Converse classical: Klimov 1961 observed, Motohashi 1979 formalized,
   that improving 2 to `2 - delta` eliminates Siegel zeros [FETCHED via 2404.01003]. The
   numerical 2 is the Siegel-zero watermark: crossing it is a zero-location theorem, not a
   refinement.

Care point: the extremal-function literature's own optimality theorems (e.g.
`int(B - sgn) >= 1` sharp) are FUNCTION-CLASS statements, not arithmetic ceilings; the
arithmetic ceiling enters only through the sieve-axiom embedding.

### 2.4 The structural law (direction of conditionality)

In every published pairing of band-limited majorants with the explicit formula, the majorant
positivity is deployed on the ZERO side and consumes RH (zero reality) BEFORE it fires
(S(t) bounds, prime gaps, pair correlation, zeta size: all conditional); the unconditional
mode runs inside the sieve axioms and walls at the factor 2. NO published instance runs the
reverse direction (counting bound out of majorant positivity without location input). The
one-sided Landau threshold is exactly the reverse direction, and that direction is exactly
what is absent. Correction to a tasking premise, on record: "Selberg's N(T) work" is not a
majorant application (his extremal-function application was the 1974 large sieve); the
genuinely unconditional zero-side yield of the family is zero-DENSITY only, and that yield
is Beurling-generic in print (Revesz 2209.01689; Broucke 2409.10051) [REPO], hence
location-blind by proven example.

### 2.5 The uniformity precedent: exactly three corners

Is there ANY mechanism where a family of finite-dimensional operator bounds, uniform in the
family parameter, glues to an asymptotic psi-type bound?

- **The large sieve**: the ONE proven instance of the shape (family-uniform finite-rank
  positive-kernel inequality gluing to unconditional arithmetic bounds), AND the measured
  price: its arithmetic output tops out at the factor-2/parity scale (2.3).
- **Connes' semilocal trace formula** (Selecta Math. 5 (1999)): a family of finite-cutoff
  IDENTITIES, not bounds; the global positivity that would close RH is M4, not produced by
  the gluing [REPO: [`ccm_semilocal_prolate.md`](ccm_semilocal_prolate.md), #158].
- **The Haas/Hejhal episode** (the cautionary pole) [SECONDARY]: Haas 1977 numerics found
  zeta zeros among modular-surface Laplacian eigenvalues; Hejhal 1979-81 exposed the hidden
  logarithmic singularity; Colin de Verdiere 1983 identified the objects as eigenfunctions
  of a RANK-ONE perturbation (pseudo-Laplacian). Lessons: (1) spectral EXHIBITION of the
  zeros carries zero inequality content; (2) [ANALOGY tier, adversary-tempered] the rank-one
  perturbation shape is structurally the CCM 2511.22755 construction shape (both rank-one
  modifications, of very different operators: a designed spectral triple vs an accidental
  pseudo-Laplacian), so the CCM family can be READ as a designed Haas configuration; the
  point is exhibition-carries-no-inequality, NOT that CCM is wrong or an artifact. #158's
  information-free finite reality echoes Hejhal's diagnosis in the modern setting.

Net: NO known mechanism glues a lambda-uniform finite-rank operator INEQUALITY to a psi
bound finer than factor 2. The S4/R1 mechanism, if it exists, has no published relative.

### 2.6 Verdict table (adversary-audited, verbatim-faithful from the survey)

| Mechanism family | Bound shape | Constant/scale achieved | What it consumes | Ceiling: proven or open | Lattice-consuming or system-generic |
|---|---|---|---|---|---|
| Selberg/linear sieve + Brun-Titchmarsh | one-sided UPPER on pi, psi; unconditional | factor 2 (2x/(phi(q)log(x/q))) | congruence-density axioms (one-variable positive cone) | PROVEN axiom-relative (Selberg 1949 parity; Bombieri 1976) and conditionally sharp (Granville 2010.01211: Siegel zeros => Jurkat-Richert unimprovable); Klimov/Motohashi: beating 2 kills Siegel zeros | SYSTEM-GENERIC (axioms lattice-free; runs on Beurling systems) |
| Beurling-Selberg majorants, unconditional mode | same outputs via optimal cone weights | N + 1/delta; pi/delta; factor 2 downstream | same axioms (majorant = optimized weight) | same wall (proven, inherited through the embedding); extremal-class optimality is separate and non-arithmetic | SYSTEM-GENERIC |
| Majorants + Guinand-Weil ("Fourier optimization") | sharp constants: S(t), gaps, zeta size, short-interval zero counts | (1/4+o(1))log t/loglog t for S(t); CMH-94 gap constants | RH (zero reality) BEFORE the positivity fires | not a production mechanism for location; conditional by construction | lattice enters only via the FE inside the explicit formula |
| Zero-free-region route (de la Vallee Poussin) | TWO-sided psi error, unconditional | x exp(-c sqrt(log x)) | Euler product + crude continuation | PROVEN system-generic-optimal: DMV fakes attain it under Axiom A, theta > 1/2 (Revesz (9)-(10) [FETCHED]); "Vinogradov estimates and many other technology cannot prevail in this generality" (ibid.) | improvement beyond it (V-K) is LATTICE-CONSUMING; the base mechanism is generic |
| Zero-density via MV mean values | N(sigma, T) upper bounds, unconditional | Carlson-type exponents | mean-value/density data only | Beurling-generic in print (Revesz 2209.01689; Broucke 2409.10051): FE-blind, location-blind | SYSTEM-GENERIC |
| Gelfond-Schnirelman aux polynomials (archimedean) | LOWER bounds on psi | c x, c < 1; univariate form capped (Gorshkov 1956) | integer coefficients + sup-norms ([0,1] capacity) | PROVEN capped in original form; multivariate open but Chebyshev-scale | lattice-consuming (integrality) but wrong direction AND wrong scale |
| Stepanov on band-limited/de Branges/prolate carriers | (the S4 shape: vanishing budget => count UPPER bound) | NONE: no instance exists | n/a | ABSENT (verified at search depth, 2026-07-11) | n/a: the empty slot IS the R1 finding |
| Prolate/Sonin corpus (Burnol, Connes-Moscovici, CCM) | positivity (form-side) + count IDENTITIES | Weil positivity at the archimedean place; UV count = RvM | scaling-action compression; Sonin structure | no one-sided/counting inequality posed anywhere in it | the carrier is lattice-adjacent (theta/FE lives nearby) but its published uses are M4-shaped |

The single sharpest gap the table exhibits: every unconditional upper mechanism delivers
relative error O(1) (sieve) or `x exp(-c sqrt(log x))` (zero-free region); the Landau
threshold needs `x^{-1/2+eps}`. Between the proven ceilings and the threshold sits the FULL
exponent gap 1/2, with NO unconditional mechanism living strictly between Vinogradov-Korobov
(lattice-consuming, still `x^{1-o(1)}`) and the RH-conditional `sqrt(x) log^2 x`. The gap is
a missing MECHANISM CLASS, and the two verified absences (2.1, 2.2) say the operator-carrier
version of that class has never been attempted in print.

## 3. The DMV kill (the arc's verified screen)

VERIFIED: derivation checked line by line, adversary round 2026-07-11. Verbatim-faithful
from the survey's Section 6.3.

THE SYSTEM-GENERIC TRAP, fully sourced. The DMV fake (Diamond-Montgomery-Vorhauer, Math.
Ann. 334 (2006) 1-36; refined by W.-B. Zhang, Math. Ann. 337 (2007) 671-704; discretization
improved by Broucke-Vindas arXiv:2102.08478 [FETCHED abstract]) is a Beurling system with:
Euler product in print (Revesz Eq. 4 [FETCHED]); NONNEGATIVE von Mangoldt comb in print
(Revesz Eqs. 5-6: Lambda_G(g) = log|p| >= 0 [FETCHED]); integer density
N(x) = kappa x + O(x^theta) with 1/2 < theta < 1 [SECONDARY]; infinitely many zeta_G zeros
on sigma = 1 - a/log t, none to its right [SECONDARY]; and nothing better than the classical
zero-free region and error term psi(x) = x + O(x exp(-c sqrt(log x))) follows under Axiom A
with theta > 1/2 (Revesz p.3, Eqs. 9-10 [FETCHED]).

COROLLARY (repo-derived, NOT in the fetched sources; adversary-checked line by line below):
the DMV fake VIOLATES the one-sided Landau-threshold bound on the upper side, at every
exponent below 1. Run the [`landau_one_sided.md`](landau_one_sided.md) engine on the fake:
if psi_G(x) <= x + C x^a eventually (any a < 1), then F(s) = 1/(s-1) + C/(s-a) +
zeta_G'/(s zeta_G) is the Mellin transform of a nonnegative integrand (comb nonnegativity =
Revesz Eq. 5), so Landau's lemma makes its abscissa sigma_c a REAL singularity with F
analytic on Re s > sigma_c. The DMV zeros accumulate at Re s = 1, so sigma_c >= 1. But every
real point s >= 1 is REGULAR: the pole at 1 cancels exactly as in the dossier's Step 2
(zeta_G ~ kappa/(s-1) under Axiom A, and the residue of zeta_G'/(s zeta_G) is -1 independent
of kappa), and zeta_G(sigma) > 0 for real sigma > 1 by the Euler product. Contradiction.
Hence psi_G(x) - x = Omega_+(x^a) for EVERY a < 1: the majorant/sieve route runs verbatim on
the fake (all its inputs present) and the fake fails the RH-analogue AND the one-sided
bound, maximally.

ADVERSARY VERIFICATION (2026-07-11, line by line). The derivation is SOUND. Checked:
(i) sigma_c is FINITE and <= 1 (psi_G >= 0 gives g <= x + Cx^a, so F converges on Re s > 1;
this clause was implicit and is needed before Landau applies). (ii) The oscillation
direction is the one PROVEN in the dossier (Lemma L as used in Theorem A's Step 4): the
failed hypothesis is the UPPER bound, so the conclusion is Omega_+, the + side; bookkeeping
correct. (iii) The zeros need only ACCUMULATE at Re s = 1 with Im rho != 0 (each is an
uncancellable pole of zeta_G'/(s zeta_G), forcing sigma_c >= 1); zeros AT Re s = 1 are not
needed, and the DMV curve sigma = 1 - a/log t has t -> inf so all relevant zeros are
non-real. (iv) The two-case split closes: sigma_c < 1 contradicts analyticity past a zero;
sigma_c = 1 contradicts Landau at the regular point s = 1 (pole cancellation residue -1
independent of kappa, checked against Axiom A: zeta_G = kappa/(s-1) + kappa + h(s), h
analytic on Re s > theta). (v) The kill ROUTES AROUND the D1 real-zero caveat (the
[`landau_one_sided.md`](landau_one_sided.md) Section 2.2 correction): the contradiction
point is s = 1, where the Euler product excludes a real zero; real zeros of zeta_G in
(a, 1) are singularities LEFT of sigma_c = 1 and are irrelevant. (vi) Input tiers as stated:
Euler product + nonnegative comb [FETCHED, Revesz Eqs. 4-6]; N = kappa x + O(x^theta) and
the accumulating-zero statement [SECONDARY]. The kill's strength is therefore: PROVEN
conditional on two SECONDARY-tier facts about the DMV construction, both pinned to Math.
Ann. 334 (2006) via the fetched Revesz summary (Eqs. 9-10).

CONSEQUENCE: any upper-bound mechanism whose inputs are all possessed by an
Axiom-A(theta > 1/2) Beurling system (Euler product, nonnegative comb, linear integer
density with power-saving error, sieve/majorant axioms, mean-value technology) is PROVEN
unable to reach any exponent below 1, let alone 1/2 + eps. The factor-2 family cannot reach
the Landau threshold without lattice input. The exhaustive escape routes a genuine
S4-on-the-CCM-carrier mechanism must take, by this screen: consume the additive lattice
(N(x) = x + O(1), Poisson, theta FE: the #152 fourth clause), or consume the FE itself, or
consume sub-sqrt density regularity theta <= 1/2. The last is the one OPEN CORNER: no fake
with theta <= 1/2 and off-line zeros is known [UNVERIFIED-MEMORY; the exponent-matching
constraint "the two largest of the three best-possible exponents for R, Delta, M_G are
>= 1/2 and must match" (Revesz p.3, citing [24],[37]) [FETCHED] PERMITS such a system but
does not construct one]. ADVERSARY standing instruction: the sharpest attack on any future
BUILDER construction is to run it on the DMV/Broucke-Vindas fake and on the repo's
`_shared/beurling.py` default fake and demand it name the clause that fails; the citation
set to use is exactly: DMV Math. Ann. 334 (2006) + Zhang Math. Ann. 337 (2007) +
Broucke-Vindas arXiv:2102.08478 + the four already-verified references in the beurling.py
docstring (Revesz 2209.01689, 2207.00665, 2110.11463; Broucke 2409.10051).

## 4. The probe (e1o): what the carrier measures

Full record: [`../../experiments/spectral/e1o_s4_carrier.md`](../../experiments/spectral/e1o_s4_carrier.md)
(banner + verdict fields are the citable surface). Post-adversary results, compact:

1. **The skeleton posed exactly, with a PROVEN-tier ill-posedness clause.** The
   Beurling-Selberg majorant pairing against the FULL von Mangoldt comb DIVERGES at every
   type and for every majorant family (the comb density `e^u` beats every admissible tail:
   Krein factorization + the Cartwright log-integral cap real-axis decay strictly below
   `e^{-u}`; adversary-upgraded from Selberg-measured to family-universal). A horizon device
   is therefore MANDATORY for any band-limited pairing, and the CCM carrier's injection
   horizon `p <= lambda^2` is exactly such a device: the carrier's structure is FORCED by
   the pairing (horizon consonance, observation tier, not progress on the bound).
2. **The certified bound at the sharp horizon is the factor-family, derived not cited.**
   `psi(x) <= x (1 + c/delta)` with `c -> m+/2 = 0.0957` (m+ = the inside excess mass of
   Beurling's B), verified as a derived density-tilt law within ~2 percent at every delta up
   to 64 (adversary extension; frac-robust). Error LINEAR in x (exponents 0.99-1.02): the
   Landau threshold is not approached. The sieve normalization independently matches the
   analytic law `2/(1 + 2E/log x)` (E = 1.3326) to 4 digits at x = 1e6, rising monotonically
   to the parity ceiling 2. The factor-2 family of Section 2.3, derived and measured on this
   carrier.
3. **The budget is NOT the wall (the honest surprise).** Dimension needed for x^{1/2}
   resolution is `x^{1/2} log x` vs the carrier's Shannon budget 4x at its horizon window:
   ratio 3.5e-3 at x = 1e6 (adversary-corrected convention; the draft's /(2 pi) was a slip),
   scaling as `x^{-1/2} log x -> 0`. Unlike over F_q (where the degree budget binds and
   Frobenius relaxes it), the binding constraint on this carrier is that the smoothed prime
   sum at that type is unconditionally UNEVALUABLE (the explicit-formula zero side IS
   location data). The S4 absence is a mechanism shortfall, not a budget shortfall.
4. **The multiplicity heart: full price at {log p}, exact collapse at commensurate combs.**
   No subspace family achieves well-conditioned rank collapse at the log-prime comb:
   builder decimations cost ratio 1.000 across all 12 (lambda, K) cells (min sv 0.08-0.98,
   genuinely full rank), and the adversary's five smarter families all fail (half-set
   Stepanov transfer rank-full at min sv 0.81; near-commensurate decimations are a
   conditioning mirage AND budget-excluded at J >= 3; ground-state modulation nil;
   structured sparse frequency sets inside the random-subset null; 50-digit SVD confirms
   the AP collapse exact at 1.2e-14 and the log-prime full rank genuine). Commensurate AP
   combs collapse exactly (= the F_q mechanism: over F_q the point set IS an AP in u;
   circle endomorphisms reduce to the tested decimation class). MECHANISM-tier reading:
   Frobenius = commensurability of the value group; the S4 absence on this carrier IS the
   Q-linear independence of {log p}, the additive-lattice wall met from the
   extremal-function side (#62/#153/#156 re-met). Proven core: decimated nodes stay
   distinct by unique factorization, and distinct nodes give a nonsingular trig Vandermonde.
5. **The S4 spec, banked (the arc's forcing question, conjecture tier).** Produce, for each
   lambda, a one-sided device on the carrier's log-circle (dim budget <= 4 lambda^2) whose
   vanishing conditions at {k log p} of total order M cost o(M) dimensions, lambda-uniformly
   and well-conditioned, restoring the LINEAR Stepanov pairing in place of the quadratic
   sieve one (deleting the level-halving 2), sourced by an identity that FAILS for perturbed
   logs: the lattice clause is MANDATORY by the DMV kill (a candidate running on
   nonneg-comb + density alone is pre-killed at every exponent below 1). Screen every
   candidate against the repo fake, the DMV system, and D-H (must be unposable). Full spec:
   e1o .md Q4.
6. **Disciplines.** D-H: UNPOSABLE (sign-changing comb, 25 sign changes below n = 60;
   measured exhibit: negative excess -0.288), the same Euler gate as the Landau translator.
   Beurling: runs IDENTICALLY (same law, max rel diff 0.14 at x >= 1000): system-genericity
   proven by execution, then capped by the DMV kill. K1: CLEAN (guards never tripped; the
   zero side is discussed analytically and never evaluated in code; adversary code-reading
   confirmed). Parity crosscheck: the two 2-shaped constants kept apart: the sieve 2 is
   parity-explained (#146, the quadratic pairing's level-halving), the majorant cell
   constant m+/2 is uncertainty-explained (Beurling extremality); conflating them would
   overclaim.

## 5. Reconciliation

- **Against #161 / [`landau_one_sided.md`](landau_one_sided.md)**: the S4/R1 question was
  POSED there (Sections 3.4/3.6); this arc gives it its first measured content. The known
  cheap mechanism (the only occupant of the slot) is a Nyquist-cell tax, relative error
  O(1/delta) at fixed type, system-generic; the proven ceilings (factor 2, parity,
  Siegel-watermark) all live strictly at exponent-1 error. The dossier's Section 2.2
  dictionary was corrected in this arc's adversary round (real-zero caveat + Axiom-A pole
  clause + reverse-arrow scope; surveyor D1 adjudicated surveyor-right); the DMV kill routes
  around the caveat.
- **Against #146**: consistent, and sharpened. The majorant family IS the optimal-weight
  face of the sieve axioms when unconditional (walls at parity), and is RH-consuming when
  paired with the explicit formula; no third mode in print, and e1o's divergence measurement
  is WHY (the raw line pairing is not even posable without a horizon).
- **Against #152/#153**: the lattice clause reappears as the unique glue across
  incommensurable circles: per-prime cheapness is EXACT (the {k log p} orbit on
  R/(log p)Z costs 0.20 = 1/5 ideal, the multiplicity avatar of #153's per-prime W6
  exactness); what is missing is the glue, whose only known carrier is N(x) = x + O(1) /
  theta-FE. Fourth witness for the #152 bracket, now from the extremal-function side.
- **Against #145/#149**: the vF-model verdict ("S4 is the only open slot") is re-verified on
  a second carrier, now with numbers: the slot is empty not for lack of searching but
  because decimation-sourced cheapness provably requires commensurability.

## 6. Adversary catches banked (process record)

1. The budget formula 2 pi convention slip (dim_need = 2 delta L, not delta L/pi): fixed in
   .py and .md; the affordability conclusion ROBUST (ratio 3.5e-3, still -> 0).
2. The `--quick` npz clobber: a quick run silently overwrote the tracked full-run artifact;
   fixed (quick no longer saves), npz regenerated from the fixed full run.
3. Precision: the .md's c range corrected to the actual npz span 0.073-0.093 (per-delta
   medians 0.080/0.087/0.088).
4. The [`landau_one_sided.md`](landau_one_sided.md) Section 2.2 lossless-dictionary claim
   fixed in place (real-zero/Siegel-damper caveat; Axiom-A pole normalization; reverse arrow
   is not Lemma-L content). Its Section 2.2 off-line-zero existence RE-RUN flag DISCHARGED
   (Revesz 2207.00665 fetched).
5. The survey's Haas/CCM sentence tempered to [ANALOGY tier] (2.5 above carries the
   corrected form).

Upgrades in the same round: the c = m+/2 identification from scale-match to verified tilt
law (delta to 64, x to 1e6); the divergence from Selberg-measured to family-universal
(structural tier); the multiplicity absence from decimations-only to 5-family-hardened.

## 7. Frontier and handed forward

**Frontier: UNMOVED**, sharpened at three coordinates: (1) the pairing's ill-posedness
forces a horizon = the carrier's own structure (consonance, not progress); (2) the dimension
budget is NOT the binding constraint on this carrier (the mechanism is what is missing);
(3) the multiplicity absence is measured to be exactly the incommensurability of {log p},
so the missing glue is the additive lattice, as the DMV/Beurling screen independently
demands. Nothing here moves M4 or BRIDGE-H.

Handed forward:

- **BUILDER (next executable)**: the Sonin projector build (the ONE candidate family this
  probe could not test: the true operator eigenbasis / Sonin-space projector is unbuildable
  from the e1k/e1n caches; the literature slot is also empty, 2.2). And the Q4 forcing
  question (Section 4 item 5).
- **SURVEYOR (next round)**: the theta <= 1/2 Beurling corner (the one unsourced escape
  hatch in the kill screen: construct or exclude a fake with sub-sqrt density error and
  off-line zeros); the Carneiro-Littmann well-posedness question in the CCM Sonin space.
- **VERIFIER**: five targets named in the e1o .md (the prime-side inequality with the Euler
  gate as hypothesis; the tail divergence via Chebyshev blocks; the structural span nil;
  the decimation rank-1 collapse; trig-Vandermonde full rank at distinct points).
- **Standing citation flag**: the von Koch/Schoenfeld converse remains the one open
  RE-RUN-NEEDED item from #161 (the Beurling off-line-zero flag was discharged this arc).
