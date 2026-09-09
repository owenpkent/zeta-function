# Verification

What the `ZetaRH` library actually establishes, what it trusts, and how to keep
those two facts from drifting. Machine-readable summary in the repo-root
`formalization.yaml`.

Nothing here contradicts the source. Every finding below is already stated in
some file's own comments. The problem this document solves is that those
statements are scattered across 47 files, so the aggregate picture is only
visible to someone who reads all of them.

## The honest one-paragraph summary

This is Phase 1 scaffolding. **None of the headline classical RH-equivalence
criteria are proved.** Li, Nyman-Beurling, Robin, Lagarias, Mertens and Weil
positivity are `sorry`-stated targets: correct types, no content. What is
machine-checked is a small set of elementary results one step removed from RH
(finite Euler-product zero-freeness, elementary functional-equation algebra),
plus a function-field Hasse-Weil chain conditioned on one named axiom. That is
a reasonable state for a Phase 1 substrate. It is not a partial proof of RH.

## Sorry census: use the script, not grep

`grep -c sorry lean/ZetaRH/*.lean` reports about 140 hits across 33 files. The
true figure is **33 across 11 of 47 files**. The gap is prose: this codebase
discusses sorries constantly (`sorry-free`, `` `sorry` ``, `sorryAx`, "the
former sorry-bodied lemma"), and grep counts all of it.

```sh
python3 lean/sorry_census.py            # per-file summary
python3 lean/sorry_census.py --list     # every occurrence with its VERIFIER id
python3 lean/sorry_census.py --check 33 # exit 1 if the count moved
```

It strips Lean comments (line, nested block, doc) and counts whole tokens.

**Registry drift.** `experiments/lemma_db/lean_targets.py` builds the 108-target
registry by parsing the table in `lean/README.md`, i.e. from prose, not from the
Lean source. It is therefore accurate only while status lines are kept current
by hand. The census is source-derived and is the ground truth; the registry's
finer taxonomy (targets with no code yet, many-to-one mappings) explains why its
OPEN count is larger. Wiring `--check` into `smoke_test.sh` makes a silent
regression loud.

**20 of the 33 sorries carry no VERIFIER id.** They sit outside the tracking
convention entirely, concentrated in `HodgeIndex.lean` (5), `PrismaticFoliation.lean`
(4) and the unimported draft. Assigning ids is cheap and closes the gap between
what the registry tracks and what the source contains.

## Trust base

One real `axiom` in the library:

`frobeniusTateData_exists` (`ZetaRH/FrobeniusExistence.lean:155`) asserts that a
Weierstrass curve with good reduction has a rank-2 integer Frobenius on the Tate
module with prescribed determinant and trace. This is Silverman III.8.6, a true
classical fact that Mathlib lacks the scheme-theoretic API to prove.

This is handled well and should stay handled well: it does **not** assume RH,
the file proves a non-vacuity witness (`frobeniusTateData_companion`) showing the
contract is satisfiable exactly when Hasse's theorem holds, and everything
downstream names it under `#print axioms` by design. Scope note worth repeating
because the naming invites confusion: the chain below it proves the
**function-field** (Hasse-Weil) analogue for one elliptic curve's local factor.
It says nothing about the classical Riemann Hypothesis.

No `opaque`, `native_decide`, `unsafe`, `implemented_by`, `extern`, or
`set_option maxHeartbeats` anywhere in the library.

## Declarations that compile without carrying their content

These are the ones to keep visible, because a reader who greps for `sorry` will
not find them and a name-level skim will misread them. All three are documented
in their own source comments.

**`line_restriction_lemma`** (`ZetaRH/LineRestriction.lean:134`) is vacuous as
stated. It claims `exists c1eff, c1eff <= 2 * fejerMax ...` and discharges it by
taking the witness to *be* the bound: `refine <2 * fejerMax ..., le_refl _>`.
The intended mathematical content, the restriction-to-1D operator returning a
cosine polynomial whose `c_1` is that witness, is VERIFIER target #LR-2 and is
not expressed by the statement. Until #LR-2 lands, the corollary that "closes
the LP/SDP escape family" rests on a lemma that says nothing.

**`PrismaticCohomology.lean` Q1 through Q5 and Q3b** are stated as
`theorem ... : True := by sorry`. The *statement* is vacuous, not merely the
proof. Discharging the sorry would prove nothing.

**`HodgeIndex.lean`** `hodge_index_theorem_open` and `hodge_index_escapes_K1`
follow the same pattern, in the file the repo bills as "Direction 8: the central
open problem".

This is the single most valuable pattern to keep an eye on, because it is
exactly the failure mode that machine verification cannot catch: a proof
assistant confirms `True := by sorry` as readily as a real theorem, and a
Comparator run on such a statement would pass. Being able to point at this list
is what makes the rest of the repo's claims credible.

## Statement provenance

Every definition here is this project's own, including `nonTrivialZeros` and
`riemannHypothesis`. Google DeepMind's Formal Conjectures carries a third-party
statement at `FormalConjectures/Millenium/RiemannHypothesis.lean`, plus
`Wikipedia/RiemannZetaValues.lean`. They have not been diffed against these
definitions.

Restating the equivalence criteria against the upstream statement would buy an
independence guarantee that self-authored statements cannot, and would matter
most precisely for the criteria, since an equivalence to a subtly different
notion of RH is worth nothing. This is the highest-value verification task
outstanding.

## Reproducing

Toolchain `leanprover/lean4:v4.30.0`, mathlib `v4.30.0`
(`c5ea00351c28e24afc9f0f84379aa41082b1188f`). The tree was last built green and
`.lake/build` is current.

```sh
cd lean
lake exe cache get
lake build
bash smoke_test.sh
python3 sorry_census.py --check 33
```

Then audit the trust base directly:

```lean
#print axioms functionfield_RH_localPolynomial   -- names frobeniusTateData_exists
#print axioms np1_reduction                      -- standard three
```

There is no CI. `smoke_test.sh` and the registry checker are run by hand.

## Independent checking

Once a target is genuinely discharged, it can be checked the way an outside
party would: a challenge file stating the theorem, a solution module that never
imports it, and Comparator with an external kernel. The harness is at
`~/.local/share/lean-verify/` and the workflow is in the `lean-verify` skill.

Do not point Comparator at anything on the vacuous list above. It will pass, and
the pass will mean nothing.
