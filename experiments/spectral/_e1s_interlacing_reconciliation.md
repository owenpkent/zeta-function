# ADVERSARY reconciliation: e1s (#169) vs #165/e1p interlacing verdicts

**VERDICT: NO CONFLICT.** The twisted-inner-product caveat bites only the
non-normal operator-level object (e1p's `D = D_0 + P_1`, e1s's `M`); it does
not touch, and neither dossier ever claimed it touches, the Hermitian
form-level `Q`. Read past their one-line headlines, #165/e1p and #169/e1s
make the *identical* two-object split internally and agree on every disputed
number. The apparent contradiction in TODO.md was created by quoting e1p's
**Q1** grade ("not a theorem instance") against e1s's **Q** grade
("rigorous") as if about the same matrix. They are not the same matrix.

## The crux, answered directly

Does the twisted-inner-product caveat undercut the Hermitian-`Q` reading, or
only the non-normal `M`-shadow? **Only the `M`-shadow.** The Hermitian-`Q`
Weyl/Cauchy reading is unaffected and is independently confirmed by both
runs.

## Why: the two objects are built differently, in the shared source

Both e1p and e1s reuse `experiments/spectral/e1k_dh_dlog_testbed.py`
verbatim (`build_float`, `operator_spectrum`); neither invents its own
matrices. Read directly from that source (`e1k_dh_dlog_testbed.py:216-246`,
`:279-294`):

- **`Q` (Weil form).** `Q = A + P - Ts`, then explicitly
  `Q = 0.5*(Q + Q.conj().T)` (line 244: forced Hermitian symmetrization
  w.r.t. the STANDARD/ambient inner product on `C^D`), diagonalized by
  `np.linalg.eigh` (line 246), which both requires and exploits ambient
  Hermitian symmetry. The pole term is
  `P = 2*Re(outer(conj(av), av))` where `av_n = Vhat(n, i/2)`. Writing
  `av = p + iq` (real `p,q`), `Re(outer(conj(av),av)) = pp^T + qq^T`: a sum
  of two rank-1 PSD Hermitian matrices, hence `P` is Hermitian PSD, rank
  `<= 2`, verified numerically rank exactly 2 (third singular value
  literally `0.0`, not just small) in both dossiers independently.
- **`M`/`D` (the physical operator).** `M = Dlog - outer(Dlog @ xin,
  delta.conj())` (`e1s`'s `Mmatrix`, line 156) / equivalently e1p's
  `D = D_0 + P_1`, `P_1 = -|D_0 xi><delta_N|`. This is a rank-1 update of
  the form `-w u^T` for **two different vectors** `w = Dlog@xin` and
  `u = delta` (not `w w^T` for a single vector), hence NOT Hermitian in the
  ambient inner product in general. `operator_spectrum`'s own docstring
  (line 284) computes "the G-self-adjointness residual... `G = Q - eps*I`
  the Weil inner product": `M` is only approximately self-adjoint w.r.t.
  this *different*, physically-motivated (and indefinite) bilinear form,
  not the standard one used to sort/count eigenvalues. That is exactly the
  twisted-inner-product caveat, and it is a fact about `M`/`D`, not about
  `Q`.

The classical rank-`r` Weyl/Cauchy counting bound
(`|N_{A'}(t) - N_A(t)| <= r`) needs the perturbation to be Hermitian
(equivalently: self-adjoint w.r.t. the SAME inner product used to sort
eigenvalues for the count). `P` on `Q` satisfies this by construction
(machine-exact, not approximate). `P_1`/the `M`-difference does not: it is
self-adjoint only w.r.t. a different indefinite form `G`, so the textbook
hypothesis is not manifestly met, and no interlacing theorem bounds the
`M`-count. This is precisely what both dossiers say internally.

## e1p's own internal split (Q1 vs Q3), not a contradiction of e1s

`e1p_rank_one_interlacing.md`:
- **Q1** (operator level, `D = D_0+P_1`): "interlacing HOLDS... but only as
  a *measurement*. The CF coupling is self-adjoint w.r.t. the twisted
  Weil-form inner product, not the ambient one, so the textbook
  one-directional PSD-rank-1 Cauchy hypothesis is not manifestly satisfied."
  This is the sentence the TODO item quotes as "#165 grades the profile
  not-a-theorem-instance." It grades **Q1**, the operator level.
- **Q3** (form level, `Q_full - Q_noPole = P_pole`): "**FORM-level
  (provable, verified).** `Q_full - Q_noPole` has numerical SVD rank exactly
  2... `P_pole` **is** a genuine PSD rank-`<=2` Hermitian addition, so the
  classical Weyl/Cauchy rank-2 bound applies with its hypotheses actually
  met. The probe confirms it holds (max shift 1 and 2 respectively, both
  `<=2`)." This is e1p's OWN rigorous-Weyl-on-Q statement, stated in the
  same dossier that the TODO quotes for the opposite reading.

e1p even explicitly separates the two: "these numbers are measured and
reported, not graded against an assumed bound [operator level]... in
contrast to Q1's murkier operator-level case" vs. Q3's "hypotheses actually
met."

## The matching numbers: same anomaly, same location, in both runs

The "same single sqrt(13) exception cell reaches 3" that both dossiers flag
is, in **both** cases, an operator-level (`D`/`M`) reading, not a
form-level (`Q`) reading:

| dossier | object | lambda, N | value | graded as |
|---|---|---|---|---|
| e1p Q3 | operator (`D_noPole -> D_full` shift) | sqrt(13)=3.606, N=24 | 3 | "informational, not gated... no theorem backing a bound there" |
| e1s ADVERSARY (2026-07-12) | operator (`M` unfiltered move) | sqrt(13), N=34 | +3 (exceeds rank(P)=2) | "a non-normal shadow, NOT a bound... ghost-fragile (a second build reads +2)" |

Meanwhile the **form-level `Q`** stays inside the rigorous `<= 2` bound at
every tested cell in both dossiers, including at sqrt(13):

| dossier | object | cell(s) | max shift/move | graded as |
|---|---|---|---|---|
| e1p Q3 | form (`Q_full - Q_noPole`) | (2.6,16) and (3.606,24) | 1, 2 (both `<=2`) | "provable, verified... hypotheses actually met" |
| e1s T1 | form (Weyl on `Q`) | 400-point grid + the ADVERSARY's own sqrt(13),N=34 push | max 1, robust everywhere | "RIGOROUS... Weyl-on-Q stayed `<=2` at every cell" (adversarial test case 1, e1s .md) |

So the two dossiers do not merely avoid contradicting each other in the
abstract: they report the *same* numerical anomaly at the *same* parameter
regime, attributed to the *same* object-level distinction, independently.

## Independent corroboration: e1p's own prior ADVERSARY pass (2026-07-17)

`_e1p_adversary.md` Axis 4 already rebuilt `Q_full`/`Q_noPole` from scratch
(not reusing e1p's own code) and independently reconstructed
`2(pp^T+qq^T)` from `Vhat(n, i/2)` with a hand-written closed form:
`max|dQ - 2(pp^T+qq^T)| = 9.0e-17` and `4.9e-16` at two grid points (machine
epsilon), with the third singular value "*literally* `0.0` in the printed
output, not just below a tolerance." That report explicitly grades this
"provable, verified... as opposed to Q1's operator-level 'measurement' tier,
which is correctly kept separate" -- the identical split argued here, banked
before this reconciliation task was even opened.

## Attempts to break this reconciliation (adversarial stress, this pass)

1. **Is `Q`'s Hermitian-ness itself fragile / only approximate, undermining
   "hypotheses actually met"?** No: `Q` is forced Hermitian by an explicit
   `0.5*(Q+Q.conj().T)` symmetrization in the shared `build_float` (not an
   emergent numerical accident), and e1s independently measured
   `||Q - Q^H|| = 0` exactly. Not fragile.
2. **Could the pole term `P` fail to be genuinely PSD (not just rank<=2)?**
   Checked the algebra directly: `P = 2*Re(outer(conj(av),av))` with
   `av = p+iq` real-decomposed gives `P = 2(pp^T + qq^T)`, a sum of two
   outer products of a REAL vector with itself, manifestly PSD. Confirmed
   independently in both dossiers' numeric SVDs (exact rank 2, positive
   singular values) and in e1p's from-scratch ADVERSARY rebuild.
3. **Could the reconciliation just be re-labeling a real disagreement
   about which object is "the" ingredient?** No: #154's upgrade-spec item
   was always about the operator/CF coupling (`P_1`), which is why e1p
   grades Q1 (the actual ingredient) as "measurement, not theorem" -- that
   grade is correct and stands. Q3/the e1s Q-Weyl claim is a *separate*,
   additional, and also-true fact about a different perturbation (the pole
   term on the form). Neither dossier claims Q3/Q-Weyl discharges the Q1
   ingredient; both keep them explicitly separate ("in contrast to Q1's
   murkier operator-level case").
4. **Does re-reading change any of #165's other verdicts (Q2, the #143
   grading, RH-blindness)?** No: Q2's "lands on #143 side" and Q3's
   "input-faithful, RH-blind" are untouched; this reconciliation only
   resolves the Q1-vs-Q wording collision, not the substance of any grade.

None of these break the reconciliation; each closes off a plausible escape
route and the split holds.

## Downstream impact

**Nothing moves.** #165's retirement of the #154 ledger and its "the
rank<=2 pole block is the ONE genuine Weyl/Cauchy instance, input-faithful,
RH-blind" claim (Q3) is CONFIRMED, not contradicted, by e1s's independent
Q-Weyl measurement -- if anything it is now doubly-independently verified
(two separate probes, two separate implementations of the counting/shift
harness, same conclusion). e1s's own Weyl-on-Q rigor claim also stands
unchanged. The frontier stays UNMOVED either way: the count-half of the W6
budget was already graded structure-cheap by both dossiers, and the
location-half (= M4) was never touched by either. This is a bookkeeping and
cross-reference clarification, not a new result and not a correction to any
prior verdict.

## Recommended follow-up (cheap, not required)

Add one cross-reference sentence to each of `e1p_rank_one_interlacing.md`'s
Q1/Q3 split and `e1s_rank_one_interlacing.md`'s `Q`/`M` split, pointing at
each other by name, so a future reader does not have to redo this
reconciliation from the raw text. Done here as the ADVERSARY section
appended to `e1s_rank_one_interlacing.md`; e1p's own text already states the
split clearly enough (Q1 vs Q3) that no edit to e1p is strictly needed.
