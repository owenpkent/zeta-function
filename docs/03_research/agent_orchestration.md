# Orchestrating agents for formalization

Reference for the `lean-verify` skill. Load when planning how to formalize
something large with many agents, or when reading a machine-generated Lean
corpus and trying to infer how it was made.

Everything here is either measured from a public artifact, quoted from a paper,
or marked as inference.

---

## The pattern that works: contract and discharge

Several groups converged on the same shape independently. It has one idea.

**Make each obligation a first-class object, and let proofs take other
obligations as hypotheses.** Then agents can work on siblings concurrently
without seeing each other's output, and the dependency graph is machine-readable
rather than implied by imports.

The cleanest shipped example is `github.com/tristanbuckmaster/fluid_lean`
(Alpoge/Claude, September 2026). Layout: `Statement/`, `Framework/`,
`Construction/`, **`Leaves/`**, **`Proofs/`**. `Leaves/` holds 207
`def <name> : Prop := ...` declarations. `Proofs/R0x/<leafname>.lean` holds one
closed proof unit per leaf, filename matching the obligation. And the
signatures carry the dependencies:

```lean
-- Leaves/: the obligation as an object
def rbcFrame_rec : Prop := ...
def rbcLetters_rec : Prop := ...
def rbcOmTop_rec : Prop := ...

-- Proofs/: one file per leaf, siblings assumed as hypotheses
theorem rbcFrame_rec.proof (hL : rbcLetters_rec) (hO : rbcOmTop_rec) :
    rbcFrame_rec := ...
```

Measured payoff: **402 of 410 proof modules depend on no other proof module**.
They depend only on the shared `Leaves/` and `Framework/` substrate. That is 402
mutually independent discharge tasks, and it shows up as an import-DAG of depth
**30** with max fan-in 123: a wide shared base, then a flat fan-out.

Compare `openai/NavierStokesAndEuler`, same month, adjacent mathematics: **6**
obligation defs, **0** theorems named `*.proof`, import-DAG depth **96**, mean
2.3 dependencies per module. A long serial ladder. Inference, but a well
supported one: that shape is what you get when formalization accretes
incrementally rather than being decomposed up front.

### Migrating an existing target list

If a project already tracks open gaps by identifier - a `sorry` with a comment
tag, a registry table, a TODO ledger - it is most of the way there. The move is:

1. Turn each tracked gap into `def <target> : Prop := <the actual statement>`.
   The statement has to be written out honestly; this is where vacuity gets
   caught, because writing `def foo : Prop := True` is visibly absurd in a way
   that `theorem foo : True := by sorry` is not.
2. Replace the `sorry` with `theorem <target>.proof : <target> := ...`, in its
   own file named for the target.
3. Where a proof needs a sibling, take it as a hypothesis rather than importing
   its module. Now the two can be worked concurrently.
4. Assemble at the top by feeding proofs into each other. The assembly module is
   the only place that knows the whole graph.

The payoff is not elegance, it is that N agents can be pointed at N files with
no merge conflicts and no shared context.

---

## What the literature agrees on

**Iterative compiler feedback dominates model choice.** SorryDB
(arXiv:2603.02668) harvested 5,663 real sorries from 78 live Lean projects and
measured pass@1 going from 5-11% for plain LLM attempts to **27-30%** with
iterative self-correction against the compiler. The loop matters more than the
model. Design for many cheap retries.

**Skeleton first, then discharge.** LeanMarathon (arXiv:2606.05400) runs a
Blueprinter that emits a Lean skeleton with every proof as `sorry`, a
Target-Reviewer that audits statements against canonical targets, and a Refiner
that repairs mismatches - and only then a DAG-scheduled discharge phase that
finds "dynamic leaves" (unproved nodes whose dependencies are already proven)
and assigns each to an independent Worker on a mechanically frozen editable
region, so that "Workers acting on disjoint spans produce patches that commute
by construction." Measured: 258 lemmas, zero remaining sorries, **135 Worker PRs
merged with zero merge conflicts**, $189-$624 per paper.

Kontorovich (arXiv:2510.15924) names the same roles from the mathematician's
side: **Decomposer**, **Translator** (emits a formal scaffold as sorry'd `have`
statements), **Solver**, **Conductor**.

**Hierarchy plus racing, at scale.** AutoformBot (arXiv:2605.29955) is the
closest published analogue to a swarm: Workers, Reviewers, Supervisors,
thousands of agents, Workers isolated in **git worktrees**, and multiple workers
permitted to **race the same target** - first to clear all quality gates wins,
the rest are cancelled. Per-task persistent agents maintain "skill guides" that
workers must read before retrying. Its supervisor watches for named
anti-patterns: "frontal assault", "cheating" (hidden axioms, weakened
hypotheses), "infrastructure panic". Scale: 26 textbooks, ~1 week each, 45,000+
declarations, 500,000 lines.

**Scheduling discipline matters more than it sounds.** LeanFlow
(arXiv:2607.20503) uses a project-wide queue plus a file-scoped queue exposing
**one active declaration at a time**, with per-declaration failure memory,
explicitly to stop the agent losing active theorems after context compaction.
Their ablation: all no-queue variants exhaust the call budget. They also ship
LeanProbe, a cached same-file verifier at ~0.03-0.05s, a 9-14x speedup over full
`lake build` - fast rechecking is the economic constraint when the loop is the
product.

**Blueprint-driven, human-reviewed.** Math Inc's Gauss did the strong Prime
Number Theorem in ~3 weeks (~25,000 lines, ~1,100 theorems) against 18+ months
of partial human progress, with humans providing "the high-level blueprint" and
reviewing critical lemmas. They are candid that the bottleneck is systems, not
reasoning: "thousands of concurrent agents, each with its own Lean runtime,
consuming multiple terabytes of cluster RAM". Their orchestrator is partly open
as OpenGauss, exposing `prove, draft, review, checkpoint, refactor, golf,
autoprove, formalize, autoformalize` as workflows spawning managed children.

---

## Reading a machine-generated corpus

Structural fingerprints, all measured across two 2026 corpora totalling ~2.3M
lines.

**Keyword monoculture.** `theorem` 36,115 against `lemma` 29 in one corpus;
66,578 against 2 in the other. Humans vary the keyword stylistically; a
generator picks one and never deviates. The single cleanest tell.

**No proof-engineering infrastructure.** Zero `macro`, `syntax`, `notation`,
`elab` across 616k lines. Agents do not build shared abstractions, because an
abstraction only pays if the consumer knows it exists, and a custom tactic is a
second thing that can be subtly wrong while hiding proof structure from review.
Expect plain `rw`, `ring`, `calc`, `funext`.

**Forward-chaining, everything named.** `have` dominant roughly 2:1 over
`exact`; heavy `unfold`; the `linarith only [...]` idiom naming hypotheses
rather than searching. Identifiers run to 60+ characters. The type-checker
verifies well-typedness, not intent, so nothing is left implicit that could be
named.

**Namespace per module.** 1,646 distinct namespaces across 2,482 modules. When
agents generate names without seeing each other's output, per-module
namespacing is the cheap collision fix.

**Dead code is never deleted.** ~6% of one corpus is unreachable from its
solution root, including a fully duplicated abandoned attempt at the same
theorem by a different method. Deletion has no value when compute is cheap and
nothing downstream imports it. Its presence is evidence of search-with-discard,
not of sloppiness.

**Module size tracks the compile budget, not the agent count.** In the one
corpus where both are known, the 100-agent half produced 1,839 modules at a
95-line median while the 10,000-agent half produced 643 at a 464-line median.
The small-module half was the one whose lakefile set `warningAsError = true` with
zero `set_option`, forcing every module to compile warning-free inside default
heartbeats. Reported figures put reliable single-turn authoring around 300 lines,
which is consistent with the first but not the second, so the per-turn ceiling
is at best partial.

**Docstring volume says nothing about intent.** 12,083 docstrings and 24 line
comments in one corpus; 23 docstrings and zero line comments in the other.
Neither wrote comments *for* a reader. One model had the habit, the other did
not.

---

## The thing none of it fixes

An audit of three agent-formalization corpora (arXiv:2606.14000) found semantic
divergence from the source material in **18 to 42 percent of statements despite
zero open sorries**: "Kernel acceptance establishes only that a formalization is
well-formed and compiled, not that it is semantically correct."

So throughput is not the constraint and has not been for some time. The
constraint is the statement, and the review surface is whatever file states it.
In both September 2026 fluid-dynamics artifacts that surface was a single
challenge file of a few hundred lines against developments of 616k and 1.68M
lines. Design for that: keep the statement layer small, take it from a third
party where one exists, and name the human who read it.

Buzzard's formulation is the one to keep in mind while orchestrating anything:
if a model "forgets or mangles an axiom which is part of a definition then the
code is likely to compile, it just won't mean what it's supposed to mean."
