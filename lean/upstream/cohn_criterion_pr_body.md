# Mathlib PR body: Cohn's criterion for self-inversive polynomials

## Sequencing note (read first)

**This PR queues AFTER the digamma PR
([mathlib4#41132](https://github.com/leanprover-community/mathlib4/pull/41132)) and the
P10 rational-root-floor PR clear.** Both are already open / staged (see
[`README.md`](./README.md), [`rational_root_floor_pr_body.md`](./rational_root_floor_pr_body.md)).
This is the project's standing rule for the upstream queue: keep review load on
Owen's fork to one live PR conversation at a time where possible, oldest-staged first.
Do not open this PR until at least one of those two has merged or the reviewer load is
otherwise clear.

No new `.lean` file accompanies this PR body: the three theorems below are already
proved sorry-free in-repo, in
[`../ZetaRH/GaussLucas.lean`](../ZetaRH/GaussLucas.lean) and
[`../ZetaRH/SchurCohn.lean`](../ZetaRH/SchurCohn.lean). Porting means lifting them (plus
their auxiliary lemmas, scoped in §4) into Mathlib's own polynomial-reflection material,
not authoring anything new.

---

## 1. PR title

```
feat(Algebra/Polynomial): Cohn's criterion for self-inversive polynomials
```

---

## 2. PR description

This PR would add Cohn's criterion to Mathlib: for a real self-inversive (palindromic)
polynomial, every root lies on the unit circle if and only if every root of its
derivative lies in the closed unit disk. Three theorems, all sorry-free in this project
against Lean/Mathlib v4.30.0:

- `reflect_derivative_self_inversive` (the reversal identity behind Cohn's derivative
  trick): for self-inversive `p` over any `CommRing`,
  `reflect (n-1) p' = n • p - X * p'` where `n = p.natDegree`.
- `reflect_conj_prod_form` (the product form of the conjugate-reflection): for any
  `g : ℂ[X]`, `reflect (natDegree g) (g.map conj) = C (conj (leadingCoeff g)) *
  ∏ (1 - conj r_i * X)` over the roots `r_i` of `g` with multiplicity -- the polynomial
  `gStar` of the classical Cohn argument.
- `cohn_criterion` (the capstone): for real self-inversive `q` with `natDegree q ≥ 1`,
  every complex root of `q` has modulus `1` **iff** every complex root of `derivative q`
  has modulus `≤ 1`.

**Motivation.** Cohn's criterion (Cohn 1922, building on Schur's 1917 test) is the
classical decision procedure for "does this polynomial have all its roots on the unit
circle," used throughout the theory of self-inversive / palindromic polynomials, in
signal processing (linear-phase filter design), and in the arithmetic-geometry
application that produced this port: certifying that a genus-`g` L-polynomial over
`F_q` satisfies its Riemann hypothesis (all Frobenius eigenvalues on `|z| = sqrt(q)`) by
running the Schur-Cohn test on its derivative instead of solving for the roots directly.
That application is recorded in this project's LEARNINGS.md entry **#143**: "the toy
grader's genus-1 certificate `4 - t^2/p ≥ 0` is exactly the 1x1 Schur-Cohn quantity of
`phi'(z) = 2z - c`," generalized here to arbitrary degree. Mathlib already has the tool
Cohn's proof is built on (Gauss-Lucas:
`Polynomial.rootSet_derivative_subset_convexHull_rootSet`,
`Mathlib.Analysis.Complex.Polynomial.GaussLucas`) and the polynomial-reversal API Cohn's
statement is phrased in (`Polynomial.reflect`, `Mathlib.Algebra.Polynomial.Reverse`), but
not the criterion itself, nor any self-inversive/palindromic-polynomial theory, nor the
Schur-Cohn test.

**Discrepancy check against LEARNINGS #143's absence claim (this session).** #143 states
"Cohn's criterion is ABSENT from Mathlib." Searched the pinned checkout
(`lean/.lake/packages/mathlib`, commit `c5ea00351c`, tag `v4.30.0`) for
`self-inversive`/`selfInversive`, `schur.cohn`/`schurCohn`, `cohn.criterion`/
`cohnCriterion`, and `palindrom*` (case-insensitive, whole-tree): zero hits anywhere
except `Mathlib/Data/List/Palindrome.lean` (list palindromes, an unrelated combinatorial
notion) and `Mathlib/Data/Nat/Digits/Div.lean` (digit palindromes, likewise unrelated).
**#143's claim is confirmed accurate at the pin**: no self-inversive-polynomial theory,
no Schur-Cohn test, no Cohn criterion anywhere in Mathlib. Unlike the arcosh package
staged alongside this one (see `arcosh_pr_body.md` -- that gap claim turned out to be
stale), this gap claim holds up.

---

## 3. Theorem statements to add (verbatim from the proved source)

### 3.1 The reversal identity

Source: [`../ZetaRH/SchurCohn.lean:181-183`](../ZetaRH/SchurCohn.lean) (signature;
proof runs to line 220, ~40 lines total including the file's closing `end`).

```lean
/-- **The reversal identity (#SC-2).** If `p` is self-inversive
    (`reflect (natDegree p) p = p`), then
    `reflect (natDegree p - 1) (derivative p) = natDegree p • p - X * derivative p`.
    Proved coefficient-wise over any commutative ring: for `j <= n-1` the reflected
    coefficient is `(n-j) a_{n-j} = (n-j) a_j`; at `j = n` the right side cancels; for
    `j > n` everything vanishes. -/
theorem reflect_derivative_self_inversive {R : Type*} [CommRing R] (p : R[X])
    (hp : reflect p.natDegree p = p) :
    reflect (p.natDegree - 1) (derivative p) = p.natDegree • p - X * derivative p
```

Fully general over `CommRing R` already (no `ℂ`/`ℝ` specialization needed for this one),
so it ports as-is with no genericity work.

### 3.2 The conjugate-reflection product form

Source: [`../ZetaRH/GaussLucas.lean:116-118`](../ZetaRH/GaussLucas.lean) (signature;
proof runs to line 135, ~20 lines).

```lean
/-- **The product form of the conjugate-reflection.** For any `g : Polynomial C`,
    `reflect (natDegree g) (g.map conj) = conj (lead g) * prod_i (1 - conj r_i * X)`
    where the `r_i` are the roots of `g` with multiplicity. This is the polynomial
    `gStar` of the classical Cohn argument, with the degree-drop bookkeeping
    (`g(0) = 0` reflecting to a lost degree) handled by the splitting itself. -/
theorem reflect_conj_prod_form (g : ℂ[X]) :
    reflect g.natDegree (g.map (starRingEnd ℂ))
      = C (conj g.leadingCoeff) * ((g.roots.map conj).map fun r => 1 - C r * X).prod
```

### 3.3 The capstone

Source: [`../ZetaRH/GaussLucas.lean:323-333`](../ZetaRH/GaussLucas.lean) (11 lines).

```lean
/-- **The general-degree Cohn criterion (#SC-4 + #SC-5).** For real self-inversive `q`
    with `natDegree q >= 1`: every complex root of `q` lies on the unit circle IFF
    every complex root of `derivative q` lies in the closed unit disk. This is the
    degree-n statement whose genus-1 shadow is #SC-1
    (`schur_cohn_certifies_circle`). -/
theorem cohn_criterion (q : Polynomial ℝ) (hq : 1 ≤ q.natDegree)
    (hself : reflect q.natDegree q = q) :
    (∀ z : ℂ, (q.map Complex.ofRealHom).eval z = 0 → normSq z = 1)
      ↔ ∀ w : ℂ, (derivative (q.map Complex.ofRealHom)).eval w = 0 → normSq w ≤ 1
```

All three are sorry-free and `#print axioms`-clean
(`[propext, Classical.choice, Quot.sound]`) in-repo, verified this session by
re-elaborating both source files against the pinned toolchain
(`lake env lean` on each; zero errors).

---

## 4. Port scope: what rides along

`cohn_criterion` is a capstone sitting on top of essentially the entire content of both
source files, not a standalone lemma. A faithful port carries the following auxiliaries
(all in `GaussLucas.lean` unless noted; each already proved sorry-free in-repo):

| Auxiliary | Lines (exact, GaussLucas.lean) | Role |
|---|---|---|
| `derivative_roots_in_disk` | ~30 (59-89) | Cohn forward: circle roots of `p` force disk roots of `p'`, via Mathlib's own Gauss-Lucas |
| `normSq_factor_identity` | ~6 (91-96) | the elementary Blaschke-factor algebraic identity |
| `reflect_multiset_prod_X_sub_C` | ~14 (100-113) | reflection of a product of monic linear factors; feeds `reflect_conj_prod_form` |
| `reflect_conj_prod_form` | ~25 (116-141) | §3.2 above |
| `reflect_conj_eval`, `eval_prod_form`, `prod_normSq_le` | ~40 (143-183) | eval-level restatements and factor-by-factor dominance over a root multiset |
| `normSq_eval_le_normSq_reflect_eval` | ~12 (185-196) | reflection dominance: `\|g(z)\| \le \|gStar(z)\|` on the closed disk |
| `reflect_conj_eval_ne_zero` | ~28 (198-226) | `gStar` has no root strictly inside the disk |
| `cohn_converse` | ~74 (228-301) | the pinch-and-pair argument: no root strictly inside (via reflection dominance + the #SC-2 identity from `SchurCohn.lean`), none strictly outside (self-inversive pairing `z ↔ 1/z`) |
| `cohn_converse_real` | ~19 (303-321) | real-coefficient specialization, maps into `ℂ[X]` via `ofRealHom` |
| `cohn_criterion` | 11 (323-333) | §3.3 above: `derivative_roots_in_disk` (forward) + `cohn_converse_real` (backward) |
| `reflect_derivative_self_inversive` (`SchurCohn.lean`, not `GaussLucas.lean`) | ~40 (181-220) | §3.1 above; used inside `cohn_converse`'s pinch step |

That is essentially the full non-header content of `GaussLucas.lean` (349 lines total;
LEARNINGS #143 records "12 new theorems" for this file's #SC-3/4/5 arc) plus the one
`SchurCohn.lean` declaration listed. **Not** required: `SchurCohn.lean`'s #SC-1 content
(`roots_on_circle_of_window`, `schur_cohn_gate`, `schurCohn1_normalized`,
`certificate_iff_hasse`, etc.) -- that is the genus-1 (2x2 matrix) instantiation tied to
this project's own toy grader and the Hasse-window application, has no bearing on the
general-degree criterion, and should NOT be ported (it is project-specific, not a
Mathlib-shaped statement).

Also **not** required from `GaussLucas.lean`: `#SC-3` itself is a zero-line dependency --
the file's docstring records that Gauss-Lucas is already in Mathlib
(`rootSet_derivative_subset_convexHull_rootSet`,
`Mathlib.Analysis.Complex.Polynomial.GaussLucas`) and is used directly, with no new code.

Total new Mathlib-facing content: roughly 220-240 lines across ~11 declarations (10 from
`GaussLucas.lean`'s SC-4/SC-5 arc + 1 from `SchurCohn.lean`'s SC-2), most of it
elementary complex-algebra and multiset-induction bookkeeping; the substantive steps are
the Blaschke-factor dominance argument (`normSq_eval_le_normSq_reflect_eval`) and the
inside/outside pinch-and-pair (`cohn_converse`).

---

## 5. Mathlib placement

- **`Polynomial.reflect`** (the self-inversivity condition `reflect n p = p` is phrased
  in terms of it) lives in `Mathlib/Algebra/Polynomial/Reverse.lean` (module docstring:
  "Reverse of a univariate polynomial"; NOT a file called `Reflect.lean` -- confirmed
  this session against the pinned checkout). `revAt`, `reflect_mul`, `reflect_sub`,
  `reflect_C`, `reflect_zero`, `coeff_reflect` all live there and are used as-is by the
  port.
- **Gauss-Lucas** (`rootSet_derivative_subset_convexHull_rootSet`) lives in
  `Mathlib/Analysis/Complex/Polynomial/GaussLucas.lean`.
- **No existing file is a natural home for the new material** -- there is no
  self-inversive-polynomial or root-location file in Mathlib to extend (confirmed by the
  §2 discrepancy search). The cleanest placement is a **new file**,
  `Mathlib/Analysis/Complex/Polynomial/CohnCriterion.lean` (sibling of `GaussLucas.lean`,
  since the criterion is proved BY Gauss-Lucas and lives in the same "root location via
  convexity/algebra" family), importing `Mathlib.Analysis.Complex.Polynomial.GaussLucas`
  and `Mathlib.Algebra.Polynomial.Reverse`. A maintainer may instead prefer
  `Mathlib/Algebra/Polynomial/SelfInversive.lean` for the purely algebraic reversal
  identity (§3.1, no complex-analysis content) with the analytic capstone (§3.2-3.3)
  in the `Analysis/Complex/Polynomial/` file; defer to review on the split.
- **A reviewer will likely ask for a named predicate**, e.g.
  `Polynomial.IsSelfInversive p := reflect p.natDegree p = p` (or the standard term
  "palindromic," though Mathlib's `List.Palindrome` precedent argues for spelling it out
  rather than reusing that name in a different category), to state the self-inversivity
  hypothesis by name instead of unfolding `reflect` at each call site. The in-repo proofs
  do not use such a predicate (they carry `reflect q.natDegree q = q` as a raw
  hypothesis throughout); introducing one is a naming/API decision for review, not a
  proof-content change -- the proofs transfer either way by `unfold`/`show`.

---

## 6. Remaining manual steps for Owen

Same shape as the other two staged packages (see `README.md` §"Per-PR workflow"),
specific additions:

- [ ] **Wait for the digamma and rational-root-floor PRs to clear review** (sequencing
      note, top of this file) before opening this one.
- [ ] **Decide the file split** (§5) -- one new file or two -- and, if a maintainer
      prefers a named `IsSelfInversive`/palindromic predicate, add it and restate the
      three headline theorems in terms of it.
- [ ] **Port the ~11 declarations** (§4 table) from `GaussLucas.lean` /
      `SchurCohn.lean` into the new file(s); proof bodies transfer with only import-path
      and (if a predicate is introduced) hypothesis-unfolding changes.
- [ ] Build, `#print axioms` check (expect `[propext, Classical.choice, Quot.sound]` on
      all three headline theorems, then delete the `#print axioms` lines), lint, shake,
      commit, open PR, request review, respond in your own words (Mathlib's AI policy).

---

## 7. What this proves / what remains

**Proves.** The general-degree Cohn criterion and its two headline auxiliaries are
mathematically and formally established: eleven declarations, sorry-free, `#print axioms`
clean, built on Mathlib's own Gauss-Lucas and polynomial-reversal API, re-verified this
session against the exact pinned toolchain.

**Remains.** The file-placement/predicate decision (§5, genuinely open, worth a
maintainer's input rather than guessing further), the standard fork/branch/PR/review
workflow, and the sequencing wait (§ "Sequencing note"). None of these is a mathematical
gap.
