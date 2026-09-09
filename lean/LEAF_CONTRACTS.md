# Leaf contracts: making VERIFIER targets independently dischargeable

A migration plan for the 45 open VERIFIER targets, so that N agents can work on
N targets concurrently without merge conflicts and without shared context.

This is not a refactor for its own sake. It buys two specific things:

1. **Parallelism.** A target that is a `sorry` inside a theorem can only be
   worked by whoever holds that file. A target that is a `Prop`-valued
   definition can be *assumed* by one agent while another proves it.
2. **Vacuity resistance.** Writing the obligation out as a standalone `def`
   forces the statement to be stated. `def LR_2 : Prop := True` is visibly
   absurd in a way that `theorem line_restriction_lemma ... := by sorry` is not.
   See `VERIFICATION.md` for the three declarations here that currently compile
   without carrying their content.

The pattern is not speculative. `github.com/tristanbuckmaster/fluid_lean`
shipped it in September 2026: 207 leaf obligations in `Leaves/`, one proof unit
per leaf in `Proofs/`, and **402 of 410 proof modules depend on no other proof
module**. Import-DAG depth 30, against 96 for a comparable corpus built without
it.

## The shape

Today, `RHEquivalences.lean:129`:

```lean
theorem li_criterion (L : LiData) :
    (∀ n : ℕ, 1 ≤ n → 0 ≤ L.lambda n) ↔ RiemannHypothesis zeta := by
  sorry  -- #LI-1
```

The obligation exists only as a hole inside a theorem. Nothing else can refer to
it, so nothing else can proceed without it.

After:

```lean
-- Leaves/LI.lean  -- the obligation as an object
/-- VERIFIER target #LI-1. Li's positivity criterion for the Keiper-Li
    coefficients of zeta. -/
def LI_1 : Prop :=
  ∀ L : LiData, (∀ n : ℕ, 1 ≤ n → 0 ≤ L.lambda n) ↔ RiemannHypothesis zeta

-- Proofs/LI_1.lean  -- one file, named for the target
theorem LI_1.proof : LI_1 := by
  intro L
  ...
```

Note this repo is already most of the way there. `li_criterion` takes `LiData`,
`weil_positivity_criterion` takes `WeilExplicitFormula`, `fejer_ceiling` takes
`UnivariateCosPoly` - the hypotheses are already bundled into structures. The
only change is hoisting the statement into a `def` and universally quantifying
the bundle.

## The case that actually pays: dependent targets

The `#EF` cluster is the clearest example. `weil_positivity_criterion` (#EF-2)
needs the explicit formula (#EF-1) and the quadratic form (#EF-2a). Today all
three are sorries in one file, so they are one unit of work.

As leaf contracts they are three:

```lean
-- Leaves/EF.lean
def EF_1  : Prop := ∀ W : WeilExplicitFormula, ...      -- the explicit formula
def EF_2a : Prop := ∀ W : WeilExplicitFormula, ...      -- weilForm well-defined
def EF_2  : Prop :=
  ∀ W : WeilExplicitFormula,
    (∀ T : AdmissibleTest, 0 ≤ weilForm W T) ↔ RiemannHypothesis zeta

-- Proofs/EF_2.lean  -- assumes its siblings, does not import their proofs
theorem EF_2.proof (hEF1 : EF_1) (hEF2a : EF_2a) : EF_2 := by
  ...
```

Three agents, three files, no shared state, no merge conflict. The assembly
module is the only place that knows the whole graph:

```lean
-- Assembly.lean
theorem weil_positivity_criterion (W : WeilExplicitFormula) :
    (∀ T : AdmissibleTest, 0 ≤ weilForm W T) ↔ RiemannHypothesis zeta :=
  EF_2.proof EF_1.proof EF_2a.proof W
```

And it degrades gracefully: while #EF-1 is open, `EF_2.proof` can still be
written and checked. It just cannot yet be applied. That is strictly better than
a `sorry`, because the conditional content is real and machine-checked.

## The case that catches a bug

`#LR-2` is the reason to do this before adding more targets. Today
`LineRestriction.lean:134` states an existential and discharges it by taking the
witness to be the bound, so it proves nothing while compiling cleanly. As a leaf
contract you would have to write:

```lean
def LR_2 : Prop :=
  ∀ {N : ℕ} (P : BivariateCosPoly N N), P.NonNegOnTorus →
    ∀ (p q : ℕ) (hq : 0 < q),
      -- the restriction operator, stated
      ((restrictTo1D P p q hq).coeffs 1) ≤ 2 * fejerMax (restrictionEffectiveDegree N N p q hq)
```

which does not typecheck until `restrictTo1D` exists. The migration surfaces the
gap rather than letting it compile. The same exercise applied to
`PrismaticCohomology` Q1-Q5 and the `HodgeIndex` placeholders would force each
`: True` to become a real statement or be deleted.

## Suggested order

Do not migrate everything. Migrate where the parallelism or the vacuity check
pays.

1. **`#EF-1` / `#EF-2a` / `#EF-2`.** Three coupled targets in one file, the
   stated Architecture-3 centerpiece. Highest parallelism payoff.
2. **`#LR-2` and `#Fejer-1`.** `#Fejer-1` is self-contained and a Mathlib
   upstream candidate, so it is a clean single-agent task; `#LR-2` is the vacuity
   case above and blocks the LP/SDP escape claim.
3. **The five criteria in `RHEquivalences.lean`** (`#LI-1`, `#NB-1`, `#RB-1`,
   `#LG-1`, `#MT-1`). Mutually independent already; making that explicit means
   five agents instead of one file.
4. **The 20 untagged sorries.** `python3 lean/sorry_census.py --list` shows which.
   Assign ids before contracts; an obligation without a name cannot be scheduled.

Leave `AccidentAudit`, `MathlibBridge` and the unimported draft alone. They are
not on any critical path.

## What it costs, and what it does not change

The assembly indirection is real: `Assembly.lean` grows a line per target, and
`#print axioms` on the assembled theorem now traverses the proof modules. Trust
base is unchanged - a leaf contract is an ordinary definition, and discharging
one is an ordinary theorem.

The existing registry keeps working. VERIFIER ids stay the unit of tracking;
`lean_targets.py` keeps parsing `lean/README.md`. But once targets are `def`s,
the registry can be checked *against the source* rather than trusted: a target
with no corresponding `def` is a registry entry with no obligation, and a `def`
with no `.proof` is an open target the README may not know about. That closes
the drift noted in `VERIFICATION.md`.

`sorry_census.py --check N` should be updated as sorries convert, since a
migrated target has no `sorry` at all - it has an unproven `def` with no
`.proof` theorem. Counting *those* is the better long-run metric, and is a
two-line addition to the census once the first contracts land.
