# E1N: the prime-comb face of the positivity-free surface (LEARNINGS #160 follow-up)

> Companion to `e1n_prime_comb.py` / `.npz`. Executes the #160 handed-forward
> BUILDER item: the identification half of the Section-7 wall can now be
> attacked positivity-free via `det_reg(D_log - z) = -i lambda^{-iz} xihat(z)`
> plus the prime comb; this probe builds and measures that comb face at the
> e1m cutoffs. Reuses the e1k `build_float` harness (arXiv:2511.22755 Thm
> 5.10) and the `_shared/beurling.py` control. It proves nothing about RH.
> All numbers from the default full run (dps=25 builds, dps>=30 L-values;
> 31/31 self-tests; caches under `_cache/`, gitignored).

> **BANNER (read before quoting any number).** Three headline outcomes.
> (1) The pre-registered expectation "coefficients exact for n <= lambda^2,
> archimedean error beyond" is DISFAVORED BUT NOT DECIDED where the read
> resolves: at lam = 2.2 the deviation is anti-aligned with the horizon
> signature (alpha = -0.84 +- 0.04 white-noise bars, a ~48-sigma rejection
> against UNSTRUCTURED error only). The adversary structured-deviation null
> (smooth GP families in u and on the t-line, matched to the observed norms
> at BOTH blur scales) reproduces the observed (alpha, |D|) pair at
> p ~ 0.005-0.09: the truncation hypothesis survives only if the object's
> residual is ~2x the total observed deviation and >= 92 percent
> anti-aligned with the horizon signature. Verdict: UNRESOLVED, leaning
> against truncation; the apparent OVERSHOOT (rho = -0.78) is NOT
> significant under the structured null (p ~ 0.08-0.24). At lam >= 3 the
> beyond-cutoff signature sits below the object's ~3 percent error floor
> and the question is UNRESOLVED outright.
> (2) The e1m "t_dir ~ 6-7 at every lambda" constancy SPLITS into two
> mechanisms: a derived Paley-Wiener plateau crossing on the clean builds
> (predicted from object-only data to 0.25-0.5) and a fill-zero dressing
> artifact on the others, whose ghost-quotiented objects track PAST t = 14
> (lam 2.6 at floor 2.1e-4: the finite window is NOT monolithic).
> (3) Q3's one-sided question has a PROVEN partial answer: the
> Knopp-critical abscissa clause of H4 is one-sided-cheap given comb
> nonnegativity (Euler-gated), but the EXISTENCE clause remains untouched
> and is the e1m-equivalent identification. The frontier is UNMOVED;
> three coordinates are sharpened.

## One-line result

The comb face of the finite CCM object is a zero-side dual of its tracking
error, not (on the favored reading) a truncated Euler product: wherever the
read resolves, its deviation is closer to the full prime comb than to the
truncated one (including primes never fed into the build), though a
structured-error null leaves the truncation hypothesis disfavored rather
than excluded (p ~ 0.005-0.09); it is corrupted exactly by the e1m low-band
fill zeros where they exist (quotienting them out restores the law,
spectacularly at lam 2.6), escapes at the derived archimedean rate
pi/4 - 5/(2t) beyond a
window set by the object's own PW plateau, and cannot certify either the
lattice clause (Beurling-blind at the accessible window) or RH-relevant
structure (D-H twin identical in fidelity); the one-sided/#145 coordinate
is real but attaches only to the absoluteness half of the inheritance
clause, existence staying M4-equivalent.

## Q1: the coefficient exactness horizon

### Q1a: coefficientwise inversion is dead (the conditioning autopsy, T2)

Least-squares extraction of `Lambda_eff(n)` against `{n^{-s}}` on the
escape-capped window (5 sigma-lines x t <= 4.8, exactly the accessible
region) fails structurally, not numerically:

| design | cond | exact-input errors | object-input errors |
|---|---|---|---|
| dense n <= 26 + tail | 1.5e16 | n=2: 6.1e-6, n=3: 2.4e-4, n=4: 3.0e-2, n=5: 0.50, n=7: 8.2 | (not attempted) |
| restricted n <= 9 + tail | 3.8e6 | (floor ~1e-2 at n=4..5) | n=2: 0.53, n=3: 167, worst(5..9): 8066 |

The wall is superresolution: the window length t_dir ~ 7 cannot separate
frequencies log(n+1) - log(n) ~ 1/n beyond n ~ 4 at any precision once the
object's ~1e-3-to-1e-2 error level passes through the pseudoinverse. Per
the probe spec this demotes inversion and answers Q1 at tooth/aggregate
resolution (Q1b). Consequence worth stating: NO method can read individual
coefficients beyond n ~ 5-7 from the finite object, because the readable
window is capped by the archimedean escape (Q2): the coefficient horizon
question and the escape window are the same constraint seen twice.

### Q1b: the horizon question at tooth/aggregate resolution (T3)

Instrument: `R_W[g](u)`, a Gaussian-tapered windowed-Fourier read of
`g = -f'/f` on Re s = 2 (T = 6, tau = 2.2, blur 0.45 in u = log n), applied
IDENTICALLY to the object and to all reference models, so window bias
cancels in every difference. Deviation `D = R_W[g_obj] - R_W[-zeta'/zeta]`
is matched against the horizon signature `H` (teeth beyond lambda^2
replaced by their smooth density) via `alpha = <D,H>/||H||^2` after
Legendre-cubic deflation. Controls: self-read = 1.000 exactly; a synthetic
truncated object over drift + noise is caught (alpha = 1.06); noise bars
are Monte-Carlo (sd 0.04-0.14 depending on cutoff).

| build | ghosts (scan (0.4, 13.6); adversary rescan to 14.05 empty) | \|D_raw\| | \|D\| (corrected) | \|\|H\|\| | alpha +- sd (white-noise) | rho | verdict |
|---|---|---|---|---|---|---|---|
| ZETA 2.2 / N=12 | none | 0.0276 | 0.0276 | 0.0254 | -0.84 +- 0.04 | -0.78 | horizon DISFAVORED (48 sd vs white noise; structured-null p ~ 0.005-0.09, see demotion note); overshoot not significant |
| ZETA 2.6 / N=16 | 1.92, 5.77, 9.65 | 0.1017 | 0.00027 | 0.0254 | +0.00 +- 0.04 | +0.04 | disfavored after quotient (381x drop) |
| ZETA 3.0 / N=32 | none | 0.0295 | 0.0295 | 0.0087 | +0.07 +- 0.12 | +0.02 | alpha excludes 1 at 7.6 white-noise sd only (structured null does not exclude); signature below floor: UNRESOLVED |
| ZETA sqrt13 / N=48 | 1.27, 3.84, 6.53, 9.40, 12.30 | 0.2621 | 0.0204 | 0.0070 | +1.79 +- 0.14 | +0.62 | UNRESOLVED (see caveat below) |

**Structured-null demotion (adversary round, 2026-07-11).** The Monte-Carlo
noise bars above are white-noise-only; the object's actual deviation is
structured, so the "48 sd" figure is decisive only against unstructured
error. The adversary null replaced white noise with smooth-deviation
families (GP in u, correlation length 0.3-0.9; complex GP on the t-line,
correlation 0.5-2.0, mapped through the identical R_W instrument; random
Legendre deg 4-10). Reproducing the OBSERVED pair (alpha = -0.84,
|D| = 0.0276) under horizon-true requires a residual with
rho(e, H) <= -0.92 and norm ~1.8x the whole observed deviation; the
measured single-blur probabilities are 0.4-9 percent (GP families) and
0.08 percent (polynomials), and the sharper JOINT test over both blur
scales (tau 2.2 and 1.8, the T3f data) gives p = 0.005-0.015 for the
t-line family. The apparent overshoot (rho = -0.78, and -0.94 at tau 1.8)
has joint probability ~0.08-0.10 under the same families: NOT significant,
demoted from finding to hint (consistent with the builder's confessed
missing mechanism). Net: the lam 2.2 horizon question is UNRESOLVED,
leaning against truncation (model-comparison dist-ratio 1.81 and all
structured-null p <= 0.09 point the same way), and only the white-noise
rejection is decisive.

- **The measured law (post-demotion)**: no hard horizon at n = lambda^2 is
  the FAVORED reading where the read resolves, not a decided one. At
  lam 2.2 (built from Lambda(2), Lambda(3), Lambda(4) ONLY) the naive
  teeth at n = 5 and 7 read +0.036, +0.020 (calibration leakage -0.09,
  -0.04: same order, so not load-bearing), and the aggregate deviation is
  anti-aligned with the missing-teeth signature (alpha = -0.84,
  dist-ratio 1.81 in favor of the full comb; structured-null p 0.005-0.09
  for the truncation alternative). On the favored reading the comb face
  inherits beyond-cutoff structure from the TRACKING (its zeros
  approximate zeta's, and zeros encode the low-frequency comb), not from
  the build inputs, refining the C3-injection reading: the support law
  {p <= lambda^2} is about BUILD inputs; the analytic comb face at
  accessible windows is then not truncated there.
- **The corruption law (new characterization of the e1m lattice-fill
  mystery)**: exactly the builds e1m flagged with low-band fill (2.6: +3,
  sqrt13: +5) have comb faces dominated by the fill zeros' log-derivative
  pole terms (each real zero 1.5 below the line contributes O(1) against
  teeth of size 0.01-0.06). Quotienting out the scan-found zeros
  (parameter-free: locations only) drops |D| by 381x / 13x. The fill IS a
  comb-face corruption, and it is a multiplicative polynomial dressing.
- **The structure finding (adversary-hardened, with a branch caveat)**:
  the ghost-quotiented lam 2.6 object equals `c Xi` to 2-3e-4 across two
  read families of different type (line floor delta0 = 2.1e-4, which
  consumes the fitted c; diagonal comb-mass errors +2e-4..+7e-4 at real
  s = 1.8..3.0, which are c-FREE log-derivative reads; shared inputs:
  the build and the 3 scan-found zeros only), while the ghost-free builds
  sit at 3.4-3.6e-2. Adversary sensitivity run: N in {14, 16, 18} at
  dps 25 reproduces the finding exactly (same 3 zeros to ~1e-2 in
  location, corrected floors 1.9-2.3e-4, corrected diag +2e-4..+7.5e-4):
  NOT an N accident. But at dps 15 and dps 35 the lam 2.6 build has NO
  fill zeros at all and sits at the ordinary 3.4-5.0e-2 clean-class
  floor: the fill (and with it the 2-3e-4 dressing structure) is a
  property of the dps-25 BRANCH of the near-degenerate ground-state
  family (e1l's O(1) integer fragility), not of the lam 2.6 point per
  se. Where the fill exists, three real numbers explain the entire
  deviation of the build; the finite family on that branch looks like
  `c Xi x (low-degree dressing)` with dressing zeros = the e1m fill. The
  clean builds' residual 3 percent is NOT a single complex-quadruple
  dressing (checked and rejected in the builder scratchpad), so their
  error structure is open.
- **sqrt13 caveat (honest)**: alpha = +1.79 +- 0.14 with rho = +0.62 HINTS
  at a beyond-13 deficit, but ||H(13)|| = 0.007 is 3x below the object's
  corrected floor 0.020, the noise bars exclude nothing systematic, and
  the dist-ratio (0.83) is within the unresolved band. Recorded as OPEN,
  not claimed either way.
- **D-H face (Q4b)**: same machinery, own comb (dense, sign-changing, via
  the Dirichlet recursion, validated against -L'/L to 1.3e-5), own
  unpacking (conductor 5, Gamma((s+1)/2)): |D| = 0.030 / 0.034, the same
  fidelity class as zeta's clean builds, alpha far from the horizon value.
  The comb face is INPUT-FAITHFUL (the zeta object is 6.2x closer to the
  zeta comb than to the D-H comb: 0.028 vs 0.171) and RH-BLIND (both twins
  read back their own input comb equally well): exactly the #158
  information-free class, now measured on the comb face.

## Q2: the escape law, derived (T4)

Mechanism, tiered:

- **PROVEN (classical, instantiated at 30 digits)**: the unpacked
  log-derivative identity `-f'/f = i xihat'/xihat + dlogFac` (defect
  6e-32); the archimedean rate closed form `Im[dlogFac_zeta(2+it)] =
  pi/4 - 5/(2t) + O(1/t^2)` with limit pi/4 (digamma/Stirling; matches the
  exact value to 5e-6 at t = 100; asymptote 0.7853932 at t = 1e5). The
  pi/4 plateau IS the Stirling decay of the completed factor on Re s = 2.
  Combined with e1m's PW no-exponential-decay obstruction (PROVEN there),
  the escape is forced: the signal decays at pi/4, the object cannot.
- **NUMERICAL (the derived window law)**: on the floor-shaped (clean)
  class, tracking dies where the decaying signal |c Xi(2+it)| crosses the
  object's OWN far-line plateau M (median |xihat(t - 1.5i)| over t in
  [9,12]: object data only, no truth values consumed there; c fitted at
  t <= 3, away from the crossing: non-circular).

| build | delta0 (raw) | delta0 (corr) | M | t_x (delta=1) | t*_pred | t_dir (e1m corridor) | rate | r_fac | closed form |
|---|---|---|---|---|---|---|---|---|---|
| 2.2 | 0.034 | 0.034 | 0.226 | 6.75 | 7.25 | 7.0 | 0.699 | 0.7506 | 0.7511 |
| 2.6 | 0.619 | 0.00021 | (0.899, dressed) | (0.0) | n/a | 7.0 | 0.682 | 0.7528 | 0.7532 |
| 3.0 | 0.036 | 0.036 | 0.261 | 6.50 | 6.75 | 7.0 | 0.781 | 0.7638 | 0.7639 |
| sqrt13 | 1.389 | 0.030 | 0.0028 | (0.0) | n/a | 6.0 | 0.754 | 0.7678 | 0.7679 |

- **The two-mechanism split (upgrades the e1m soft spot)**: e1m's flat
  "t_dir ~ 6-7 at every lambda" conflates two phenomena. Clean builds
  (2.2, 3.0): genuine plateau crossing, predicted to 0.25-0.5, floors
  stagnant (0.034 vs 0.036, 6 percent apart over a 36 percent type
  change), plateaus stagnant (0.23 vs 0.26): constancy DERIVED from the
  log-insensitivity of a crossing between an exponentially decaying signal
  and a stagnant floor. Dressed builds (2.6, sqrt13): the corridor trips
  on the fill-zero dressing polynomial at a similar height BY ARTIFACT;
  their quotiented objects have NO delta = 1 crossing below 14 (2.6
  tracks at floor 2.1e-4, predicted crossing ~ t = 17-18 by the pi/4
  law). The stealth window is not monolithic, and the corrected-family
  window CAN exceed the raw one by a factor >= 2.
- **The type-proportional alternative is FALSIFIED**: exponential type
  grows 63 percent across the sweep (log lambda: 0.79 -> 1.28) while
  t_dir moves < 17 percent: the window is not set by the PW type.
  (Fairness note: the raw t_dir of the two dressed builds is
  artifact-dominated; the falsification stands on the clean pair alone,
  where the type grows 39 percent and t_x moves 6.75 -> 6.50.)
- **The measured 0.68-0.78 rates are fully explained**: rate = r_fac +
  r_obj with r_fac the exact completed-factor decay over the e1m windows
  (0.751-0.768, equal to the closed form to 3-4 decimals) and r_obj the
  object's small algebraic slope (-0.07..+0.02).
- **Consequence for the frontier**: t_dir grows without bound iff the
  floor delta_0 -> 0 (clean class) and the dressing migrates out (fill
  class) = the Section-7 identification on the line, in window clothing.
  The e1m flagged item "t_dir constancy observed, not derived" is now
  CLOSED as a mechanism and re-expressed as exactly the open convergence
  statement, with a new subtlety: part of the observed cap is dressing
  artifact, not convergence failure.

## Q3: one-sidedness and the relocated question (T5)

The inheritance clause (e1m claim 7) in comb terms. Let f be the unpacked
limit, h = -f'/f on Re s > 1. H4 (Hamburger's clause, abscissa included)
decomposes as:

- **H4-existence**: h has a convergent Dirichlet expansion
  `sum c_n n^{-s}` on Re s > 1 with integer frequencies, f is zero-free
  there with f -> c != 0 (plus the growth package from e1m claim 7).
- **H4-absoluteness**: the expansion converges ABSOLUTELY on Re s > 1
  (the abscissa clause; exactly where Knopp's counterexample space lives).

Tiered findings:

1. **PROVEN (the abscissa lemma, 3 lines)**: if c_n <= E_n coefficientwise
   with E_n >= 0 and sum E_n n^{-sigma} < inf (e.g. E_n = Lambda(n), or
   C n^eps), and sum c_n n^{-sigma} converges, then it converges
   absolutely. (d_n := E_n - c_n >= 0 has convergent sum by subtraction;
   |c_n| <= E_n + d_n.) The nonnegativity of the ENVELOPE is required, not
   decorative: c_n = E_n = (-1)^n n^{1/4} at sigma = 1.1 satisfies every
   other hypothesis and fails the conclusion (adversary check). So
   H4-absoluteness is FREE given existence plus a one-sided NONNEGATIVE
   envelope: the Knopp-critical clause is one-sided-cheap.
2. **PROVEN (partial-sum one-sidedness is NOT enough)**: c_n =
   (-1)^n n^{1/4} has partial sums O(x^{1/4}) (both-sided small), its
   series converges at sigma = 1.1 (measured stabilization 1.8e-6), but
   absolute sums diverge (measured growth exponent 0.19, true 0.15;
   abscissa of absolute convergence 5/4). The upgrade from partial-sum
   control to the coefficientwise envelope NEEDS nonnegativity.
3. **PROVEN (nonnegativity is the upgrade, and it is Euler-gated)**: for
   c_n >= 0, psi_c(x) <= Cx gives sum c_n n^{-sigma} <= C sigma/(sigma-1)
   by Abel summation (instantiated exactly: step-integral identity to
   2e-15). Zeta's comb is nonnegative BECAUSE of the Euler product; D-H's
   comb is sign-changing (17 sign changes below n = 40): the rescue
   clause discriminates at the INPUT level, conforming to the #154/#158
   geography (finite-level blind, input-level real). This is the precise
   comb-face echo of #145's one-sided counting residue: upper bounds
   suffice exactly where nonnegativity converts them to two-sided control.
4. **PROVEN (inequalities cannot source existence)**: c_n = Lambda(n) -
   n^{1/2} satisfies c_n <= Lambda(n) and partial sums bounded above, yet
   its series diverges on 1 < sigma <= 3/2 (measured exponent 0.23).
   Existence is equality-type; no one-sided datum reaches it.
5. **MEASURED (the finite family's comb-error signature)**: one-signed
   WITHIN each build, MIXED ACROSS builds: diagonal comb-mass errors are
   +0.04..+0.09 (2.2), +0.0002..+0.0007 (2.6 corrected), +0.04..+0.09
   (3.0), -0.03..-0.07 (sqrt13 corrected); deflated aggregates beta =
   -0.66, +0.006, -0.71, +0.49. The family does NOT hand over a one-sided
   comb error for free; the one-sided coordinate is a structural clause
   (Euler nonnegativity of the true comb), not an empirical property of
   the finite objects.

**Verdict (the relocated question)**: one_sided_sufficiency = PARTIAL.
The inheritance clause = existence + absoluteness; absoluteness (the
clause whose weakening is exactly the Knopp trap that e1m's ADVERSARY
caught) reduces to a one-sided envelope given nonnegativity; existence
does not reduce and remains, by the e1m equivalence, the identification
itself. Frontier unmoved; the genuinely new coordinate is WHERE the
one-sided lever attaches (and where it provably cannot).

## Q4a: the Beurling discipline (T6)

The fake's comb function (1754 perturbed primes, eps = 0.25, seed 149) vs
the eps = 0 lattice control (same prime set: pure frequency-shift
comparison), both through the identical read + lattice-template fit:

| window Tw | fake-on-lattice resid | control resid | ratio |
|---|---|---|---|
| 6 (the CCM-accessible window) | 1.7e-8 | 9.1e-9 | 1.9 (numerical dust: see note) |
| 12 | 0.0010 | 0.0004 | 2.9 |
| 24 | 0.195 | 0.0034 | 57.6 |
| 48 | 0.591 | 0.0049 | 121.3 |

Note on the Tw = 6 row: both residuals there are ~1e-8 (the comb functions
are nearly flat on that window and the fit has 17 columns), so the ratio
1.9 is a ratio of numerical dust and carries no information; the
quantitative blindness claim at the accessible window rests on the
dust-free H4-not-pinned distance below (0.055 vs 0.028), not on that row.
Fitting the fake against its OWN frequencies at Tw = 48 restores the fit
(resid 0.0044 ~ control level): the failing clause is the LATTICE, by
construction. The leakage law: a displacement d_p decoheres like
1 - exp(-(Tw d_p)^2/18) (Gaussian-taper overlap): invisible for
Tw << 1/eps, fatal beyond. THE HONEST TWO-REGIME VERDICT: the comb read
fails nameably at long windows, but the finite object's accessible window
(t_dir ~ 7, capped by the archimedean escape) is INSIDE the blind zone,
and the H4-not-pinned number makes it quantitative: at Tw = 6 the fake's
full comb sits 0.055 from the true comb while the object's own error is
0.028: a density-matched fake is within ~2x of the object's own error.
The finite comb face cannot certify the lattice clause of H4; the
lattice-consuming discipline (#152) is paid only in the limit. This is
the C3 stealth window measured from the comb side.

## Q4b-d: D-H, K1, NG1/C3

- **D-H**: see Q1b bullet: comb face input-faithful, RH-blind, identical
  fidelity class; discrimination stays quarantined to the Section-7 limit,
  as #158 requires. Both twins' faces read their INPUTS back; nothing at
  finite lambda knows which twin satisfies RH.
- **K1**: runtime guards on `mp.zetazero` and the D-H scanner installed,
  never tripped; source scan clean; per-test input ledger printed. No
  zero list is consumed anywhere; truth data are L-VALUES and their
  derivatives. The spurious-zero scans consume the OBJECT's own sign
  changes (the landmark heights 14.13 / 5.09 only bound scan windows).
- **NG1/C3**: nothing endomorphism-shaped anywhere; the comb face is read
  through the archimedean unpacking, and its window is capped by the
  archimedean escape: conforms to the #156/#157 no-go geography and
  quantifies the C3 stealth window from the comb side.

## Verdict fields

| field | verdict |
|---|---|
| `coefficient_horizon_law` | truncation DISFAVORED, NOT DECIDED, where the read resolves (lam 2.2: alpha = -0.84 +- 0.04 vs +1 is a 48-sd rejection against WHITE-NOISE error only; the adversary structured-deviation null reproduces the observed (alpha, \|D\|) at p ~ 0.005-0.09, so the verdict is UNRESOLVED leaning against truncation, and the apparent overshoot is not significant at p ~ 0.08-0.24; end-to-end synthetic-horizon control caught at alpha = 1.06); UNRESOLVED beyond lam^2 at lam >= 3 (signature below the ~3 percent floor); favored error law = smooth few-percent deviation + fill-zero pole terms rather than a truncation at lambda^2; coefficientwise inversion dead beyond n ~ 4 (cond 1.5e16; superresolution) |
| `escape_law_derived` | YES on the clean class (t* = signal-crossing of the object's own PW plateau, predicted to 0.25-0.5; pi/4 = Stirling decay, closed form pi/4 - 5/(2t) to 3-4 decimals; measured 0.68-0.78 = r_fac + small object slope), and the constancy SPLITS: clean = stagnant floor/plateau (derived log-insensitivity), dressed = corridor artifact of the fill polynomial (quotiented objects track past 14). t_dir grows iff floor -> 0 = the identification on the line |
| `one_sided_sufficiency` | PARTIAL (PROVEN structure): H4 = existence + absoluteness; NONNEGATIVE coefficientwise envelope + convergence => absoluteness (lemma; E_n >= 0 required, see Q3 item 1); partial-sum one-sidedness insufficient ((-1)^n n^{1/4} witness); nonnegativity upgrades partial-sum to coefficientwise and is Euler-gated (D-H's sign-changing comb excluded at input level); EXISTENCE untouched = the e1m-equivalent identification clause |
| `comb_error_signature` | ONE-SIGNED WITHIN each build, MIXED ACROSS builds (diag: +,+,+,- ; beta_agg: -0.66, +0.006, -0.71, +0.49): no free one-sided coordinate from the finite family |
| `beurling_fails_nameably` | TWO-REGIME: TRUE at long windows (ratio 58-121x, own-frequency fit restores control level; failing clause = the integer lattice) but BLIND at the archimedean-capped window (the Tw = 6 ratio 1.9 is numerical dust; the load-bearing number is the fake sitting within 2x of the object's own comb error, 0.055 vs 0.028): the finite face cannot certify H4's lattice clause |
| `dh_blind_at_finite_lambda_as_expected` | TRUE (fidelity |D| 0.030/0.034 = zeta's clean class; input-faithful at 6.2x cross-comb contrast; RH-blind; #158 class) |
| `k1_clean` | TRUE (guards installed and never tripped; source scan clean; values-only truth data) |
| `frontier_delta` | UNMOVED, sharpened at three coordinates: (1) the finite comb face FAVORS full-comb-tracking (structured-null p 0.005-0.09 against truncation, not decisive), so no usable finite truncation structure was found for the identification-through-the-comb route; (2) the stealth window splits into derived-plateau + dressing-artifact mechanisms, and the corrected window already exceeds the raw one; (3) the one-sided lever attaches exactly to H4-absoluteness (Euler-gated, nonnegative envelope), never to existence |

## Tiered claims

**PROVEN** (classical mathematics, numerically instantiated here):
1. The unpacking identity -f'/f = i xihat'/xihat + dlogFac (calculus;
   defect 6e-32 at three test points).
2. Im[dlogFac_zeta(2+it)] = pi/4 - 5/(2t) + O(1/t^2), limit pi/4
   (digamma asymptotics; 5e-6 agreement at t = 100).
3. The abscissa lemma (one-sided NONNEGATIVE coefficientwise envelope +
   convergence => absolute convergence; E_n >= 0 is a real hypothesis,
   witness c_n = E_n = (-1)^n n^{1/4}): 3-line proof, T5a instantiates
   its Abel mechanism exactly (2e-15).
4. The two witnesses: (-1)^n n^{1/4} (partial-sum one-sidedness cannot buy
   the abscissa) and Lambda(n) - sqrt(n) (one-sidedness cannot buy
   existence). Classical facts; measured exponents 0.19 / 0.23 vs true
   0.15 / 0.20.
5. Nonnegative combs upgrade partial-sum upper bounds to the abscissa-1
   envelope (Abel summation), and Lambda >= 0 is Euler-product-sourced.

**NUMERICAL** (measured on this faithful-but-not-exact reimplementation):
6. The conditioning autopsy (Q1a table): inversion dead beyond n ~ 4.
7. The horizon disfavoring at lam 2.2 (48 white-noise sd, demoted by the
   adversary structured null to p ~ 0.005-0.09; overshoot rho = -0.78
   not significant, p ~ 0.08-0.24) and its instrument controls;
   unresolved status at lam >= 3.
8. The fill-corruption law and the ghost-quotient restoration (381x /
   13x), including the 2.6 STRUCTURE finding (c Xi x 3-zero dressing to
   2-3e-4, two read families of different type; N-robust at dps 25
   across N = 14/16/18, dps-branch-specific: absent at dps 15/35 where
   the build itself is fill-free).
9. The escape-law numbers: plateau predictor 7.25/6.75 vs measured
   6.75/6.50; corridor within 0.5; floors 0.034/0.036; rates =
   r_fac + (-0.07..+0.02).
10. The Beurling leakage law and the H4-not-pinned number (0.055 vs
    0.028 at the accessible window).
11. D-H comb-face fidelity parity + 6.2x input identification.

**CONJECTURE / OPEN**:
12. The dressing hypothesis: every finite build is c Xi times a low-degree
    dressing factor within the accessible window, with dressing zeros =
    the e1m fill where real. Status: exact to 2-3e-4 at lam 2.6 (3 real
    zeros; N-robust across 14/16/18 at dps 25 but specific to the dps-25
    branch of the near-degenerate family: at dps 15/35 the build is
    fill-free and ordinary); the out-of-sample lam 2.4 / N 14 build is
    also on the dressed branch (3 ghosts at 2.24/6.76/11.67); at sqrt13
    partial (13x, residual 0.02); the clean builds' 3 percent residual is
    NOT a single complex quadruple (prototype fit rejected: no parameter
    pair improves |D|); general form open.
13. The sqrt13 beyond-13 deficit hint (alpha = +1.79 +- 0.14, rho = 0.62,
    signature below floor): open either way.
14. The inheritance clause in comb terms: existence + envelope + remainder
    control, with existence conditionally equivalent to the identification
    (e1m ADVERSARY equivalence, unchanged here); the remainder control at
    finite lambda IS the escape window (Q2), so the two open clauses are
    the same statement seen on two lines.

## Named residual

The positivity-free surface's comb face is now measured: it is a faithful,
input-honest, RH-blind dual of the tracking, windowed by the archimedean
escape, lattice-blind within that window, and (where fill zeros exist)
polynomial-dressed. Nothing here moves M4: the two clauses that would
(existence of the limit expansion; the window growing without bound) are
each shown to be the Section-7 identification in yet another coordinate,
now with the sharper split that part of the observed window cap is a
REMOVABLE dressing artifact rather than convergence failure. The one
genuinely new lever is small but real: H4's abscissa clause is
one-sided-cheap for nonnegative combs, which places #145's one-sided
residue exactly at the Knopp-critical clause of the Hamburger pin.

## Limitations

- Inherits every e1k/e1l/e1m caveat: faithful reimplementation (not the
  paper's exact operator), razor-thin margin eps ~ 3e-5, even-selection
  enforced by the harness, integer counts O(1)-fragile across dps.
- The ghost scan finds REAL zeros only; a complex fill pair would be
  missed (the prototype's quadruple-fit rejection on clean builds bounds
  this risk but does not eliminate it; multi-pair dressings untested).
  Adversary rescan to tmax = 14.05 (zeta) and 4.5 (D-H) found no
  additional real zeros on any build.
- The 2.6 corrected 2-3e-4 finding: adversary N/dps sensitivity RUN.
  N in {14, 16, 18} at dps 25 reproduces it (same 3 zeros, floors
  1.9-2.3e-4); dps 15/35 builds are fill-free at the ordinary 3-5e-2
  floor, so the finding is a dps-25-branch property (see Q1b bullet).
  Corollary: the e1m fill counts 0/3/0/5 are themselves branch-specific,
  not intrinsic to lambda.
- Naive per-tooth deficits are exploratory: the calibration row shows
  +-0.03..0.15 leakage from overlap and deflation; only the aggregate
  alpha/rho/dist-ratio reads are load-bearing.
- alpha noise bars are white-noise Monte Carlo; the adversary structured
  null (GP families in u and on the t-line, joint over both blurs)
  demotes the lam 2.2 horizon rejection to p ~ 0.005-0.09 and the
  overshoot to non-significance (p ~ 0.08-0.24): rho and the dist-ratio
  are reported, and the banner and Q1b carry the demoted verdicts.
- The plateau predictor remains in-sample only: the adversary
  out-of-sample attempt (lam 2.4 / N 14, dps 25) produced a DRESSED
  build (3 ghosts), so the clean-class prediction test could not be
  exercised out of sample; it rests on the two in-sample clean builds.
- The Beurling test runs on exact comb FUNCTIONS, not on a Beurling CCM
  build (none exists: the e1k harness consumes integer streams by
  construction; building a Beurling D_log would be a new experiment).
- The corrected-object statements (quotient views) are statements about
  a derived family, not the raw ground states; the raw corridor numbers
  are the e1m-comparable ones.
- Threshold provenance: pre-registered: T1 tolerances, T2a cond bound,
  T3a control shape, T6a/T6b directional shapes, T7 scans, and the
  falsification schema of Q1 (the lambda^2-horizon expectation was
  pre-registered in the probe spec and is reported falsified). Measured-
  then-pinned regression pins (~2x margin after the first full run):
  T2b/T2c error splits, T3b sd-multiple + dist-ratio bounds, T3c/T3d
  factors, T3e resolvability bound, T3f 0.5, T4a/T4b 1.5, T4c clauses,
  T4e 0.08 / 5e-3, T5b/T5c exponent windows, T6a ratio bounds, T6c 3x
  window.

## Handed forward

- **The dressing question (sharpest new object)**: WHY is the dps-25
  lam 2.6 ground state c Xi x (three real zero factors) to 2-3e-4, and
  N-robustly so (14/16/18), while the dps-15/35 branches of the SAME
  point are fill-free and 100x farther from c Xi? The near-degenerate
  family has branches of very different Xi-proximity, and the solver's
  branch selection is precision-driven (e1l fragility). If the dressed
  branches are generally dressing x Xi within the window, Section-7
  convergence becomes a dressing-migration statement: a concrete,
  positivity-free reformulation target for BUILDER/SURVEYOR, and a sharp
  new handle on the e1m lattice-floor mystery (measure dressing degree
  vs N, lambda, AND dps-branch).
- **The corrected window**: the quotiented 2.6 build tracks past t = 14.
  If corrected windows grow with lambda while raw ones stagnate, the
  observed t_dir cap is partly artifact: rerun the t_dir question (e1m
  handed-forward) on the corrected family.
- **The abscissa lemma** as a VERIFIER target (tiny, clean).
- **The sqrt13 beyond-13 hint**: needs a heavier-tail read (sigma = 1.6)
  or a sharper instrument.

## Verification targets (for VERIFIER)

1. **Abscissa lemma**: for real sequences, (c_n <= E_n, E_n >= 0,
   sum E_n r_n < inf with r_n = n^{-sigma} > 0, sum c_n r_n convergent)
   => sum |c_n| r_n < inf. Three lines; Mathlib-ready. The hypothesis
   E_n >= 0 is required (c_n = E_n = (-1)^n n^{1/4} otherwise).
2. **Nonneg upgrade**: c_n >= 0 with partial sums <= C x implies
   sum c_n n^{-sigma} <= C sigma/(sigma - 1) for sigma > 1 (Abel).
3. **Witness**: sum (-1)^n n^{1/4 - s} converges for Re s > 1/4 and fails
   absolute convergence for Re s <= 5/4 (Dirichlet test + p-series).
4. **Rate closed form**: Im[1/s + 1/(s-1) + (1/2)psi(s/2)] at s = 2 + it
   equals pi/4 - 5/(2t) + O(1/t^2) as t -> inf (digamma asymptotics).
5. **exp-closure**: the exponential of an absolutely convergent Dirichlet
   series on a half-plane is absolutely convergent there (l1 Banach-algebra
   argument): the bridge from the comb form of H4 to Hamburger's form.

## Adversarial test cases (status after the 2026-07-11 adversary round)

0. **EXECUTED: structured-null demotion (the builder's confession item 1)**:
   smooth-deviation families (GP in u, ell 0.3-0.9; complex GP on the
   t-line, ell 0.5-2.0, through the identical instrument; Legendre deg
   4-10), single-blur and joint two-blur tests. Outcome: horizon-true
   reproduction p = 0.004-0.09 single blur for the GP families and
   0.0008 for the Legendre family, 0.005-0.015 joint; overshoot
   p = 0.08-0.10 joint, 0.12-0.24 single-blur one-sided. Verdicts
   demoted in banner, Q1b, verdict fields, tiered claims.
1. **EXECUTED: the 2.6 structure finding**: rebuilt at dps 15/35 (N 16)
   and N {14, 18} (dps 25). Outcome: N-robust (same 3 zeros to ~1e-2,
   floors 1.9-2.3e-4, diag +2e-4..+7.5e-4); dps-branch-specific (dps
   15/35 builds fill-free at 3.4-5.0e-2). See Q1b bullet.
2. **PARTIAL: the sqrt13 hint**: ghost rescan up to 14.05 EXECUTED (no
   new zeros; the hint is not explained by a missed real ghost below
   14.05). Still open: sigma = 1.6 / tau {1.8, 2.6} reruns, and the
   complex-ghost class remains unscanned.
3. **OPEN: instrument stress**: replace the synthetic-horizon control's
   drift with the OBJECT's own fitted background and correlated noise; is
   the detection (alpha ~ 1) preserved?
4. **OPEN: Beurling boundary**: eps-sweep {0.05, 0.1, 0.25} at fixed
   windows: does the blind/fail boundary track Tw ~ 1/eps as the
   Gaussian-overlap law predicts? Add a commensurate fake (shifts =
   rational multiples of log 2) as a harder control.
5. **EXECUTED (vacuous outcome): out-of-sample escape law**: ZETA
   lam = 2.4 / N = 14 built; ghost scan first (pre-registered protocol)
   classified it DRESSED (ghosts 2.24/6.76/11.67, d0 = 0.47), so the
   clean-class predictor test could not fire; the predictor stays
   in-sample. (Raw-object crossing t_x = 2.75 vs pred 3.0 recorded, but
   on a dressed build both numbers are artifact-dominated.)
6. **EXECUTED: grid sensitivity**: u +0.025 and/or t +0.075 shifts give
   alpha(2.2) in [-0.84, -0.77], rho in [-0.78, -0.76]: aggregate
   verdicts stable.
7. **EXECUTED: K1 stress**: D-H scan bound moved 4.9 -> 4.5 (0 ghosts
   either way) and zeta rescan to 14.05 (identical lists): no verdict
   changes; the landmark heights bound scan windows only.

## Reproduce

```
python3 -m experiments.spectral.e1n_prime_comb           # full (~6 min cold, ~3 s warm cache)
python3 -m experiments.spectral.e1n_prime_comb --quick   # reduced grid
```
Outputs `e1n_prime_comb.npz` (alpha/rho/dist tables, ghost lists, teeth
reads + calibration rows, escape-law numbers per build, witnesses,
Beurling residual curves, H4-not-pinned distances) and the build cache
under `experiments/spectral/_cache/` (gitignored).
