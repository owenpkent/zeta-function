# Lemma dependency graph (DuckDB)

VERIFIER/INFRA scaffold for the bespoke RH proof system. It stores the lemma /
axiom / primitive dependency graph and makes the program's two disciplines
queryable as SQL: the Davenport-Heilbronn (D-H) wrong-approach detector and the
K1 non-circularity guard, plus the M1-M5 milestone ladder of Direction 8A.

The point of the system is structural: a bespoke system that only captures the
**realization** half (trace / determinant / explicit-formula side) is worthless,
because that half is *buildable for the D-H counterexample*. The graph is
engineered so every load-bearing path to the Riemann Hypothesis passes only
through **signature** (polarization / positivity) nodes that are *unbuildable*
for D-H. The database lets you prove that property holds, not just assert it.

## Files

| File | Role |
|------|------|
| `schema.sql` | DuckDB DDL: tables `node`, `edge`, `obstruction_link`; views `frontier`, `rh_transitive_deps`, `dh_audit`, `open_signature_nodes`, `dischargeable_axioms`, `load_edge`. |
| `seed_lemmas.json` | The graph itself: 60 nodes, 96 edges. Single sink `TGT-rh`. Reconciled with the adversary audit (see below). The 36-node core (the RH proof skeleton) plus the 2026-06-05 candidate import: the four gap-property conjuncts (`PROP-global`, `PROP-carries-trace`, `PROP-rh-equivalent`, `PROP-noncircular`) and the 17 `CAND-*` Spec(Z) cohomology candidates wired by annotation edges to the node each resolves onto. |
| `build_db.py` | Idempotent loader (duckdb + stdlib only). Validates the DAG is acyclic, checks the single-sink property, loads the seed, and prints the frontier + RH-dependency count + D-H audit. |
| `queries.sql` | Named, commented example queries (frontier, RH transitive deps, open signature nodes, D-H audit, dischargeable axioms, K1 guard, milestone ladder). |
| `.gitignore` | Excludes the generated `*.duckdb` build artifact. |

## Run

```powershell
# From the repo root. Builds experiments/lemma_db/lemma_graph.duckdb and prints a report.
python experiments/lemma_db/build_db.py

# or as a module
python -m experiments.lemma_db.build_db

# build to a chosen path (or :memory: for a throwaway build)
python experiments/lemma_db/build_db.py --db experiments/lemma_db/lemma_graph.duckdb
```

The loader is **idempotent**: re-running drops and recreates every table and
view and reloads the seed from scratch. It exits non-zero if the D-H discipline
is violated, so it can gate CI.

Run the example queries against a built DB:

```powershell
# DuckDB CLI
duckdb experiments/lemma_db/lemma_graph.duckdb ".read experiments/lemma_db/queries.sql"

# or from Python
python -c "import duckdb; duckdb.connect('experiments/lemma_db/lemma_graph.duckdb').execute(open('experiments/lemma_db/queries.sql').read())"
```

## The model

### Layers (which half a node lives in)

- `foundation` - logical / methodological calibration (RH is Pi^0_1; the K1
  discipline). Substrate, not mathematical content.
- `realization` - the trace / determinant / explicit-formula side. The easy
  half. Usually `dh_buildable=true`: D-H has it too.
- `signature` - the polarization / positivity side. The hard half = the actual
  content of RH. `dh_buildable=false`: structurally unbuildable for D-H.
- `bridge` - proven function-field theorems (over F_q) that connect realization
  to signature. The template the arithmetic axioms abstract.

### `dh_buildable` (the D-H discipline flag)

- `'true'`  - the object can be instantiated on Davenport-Heilbronn (a number
  comes out). Realization-half. Must NOT lie on a load-bearing path to `TGT-rh`.
- `'false'` - structurally unbuildable for D-H (no Euler product => no Frobenius
  => no algebra to polarize). The real content.
- `'N/A'`   - function-field theorem; D-H has no analogue, so the flag does not
  apply (the `BRIDGE-ff-*` faces, `LEM-rosati-gram-formula`, `TGT-m1-ff-rosati`).

### Edge kinds

**Load-bearing** (carry proof obligation; traversed by every reachability view
and by the acyclicity check):

- `depends_on` - A's truth logically requires B's truth.
- `specializes` - A is the arithmetic abstraction / lift of a proven
  function-field face B. (Still a genuine logical lift on the load path.)

**Annotation** (record structure; do NOT propagate dependency):

- `instantiates` - a concrete lemma realizes an obstruction / axiom.
- `contradicts` - records a negative result or a K1 guard.
- `bridges` - links obstruction-cluster nodes.
- `motivates` / `informs` - the source informs but is not a premise of the target.
- `constrains` / `contextualizes` - a foundation / numerical node frames a target.

This split is the load-bearing distinction. The whole D-H firewall rests on it:
the realization spine reaches `TGT-rh` only through annotation edges, so it is a
dead end with respect to the proof obligation.

## The five queries this DB makes cheap

1. **Frontier** (`frontier` view) - open nodes all of whose load-bearing
   dependencies are proven. Where work can start now. The deep prize is
   `AX-polarization` (M4).
2. **RH transitive dependencies** (`rh_transitive_deps` view) - everything
   `TGT-rh` needs along load-bearing edges, with depth. The full proof
   obligation. Currently 23 nodes, 9 still open.
3. **Open signature-layer nodes** (`open_signature_nodes` view) - the real work.
   `AX-hodge-riemann` is the single deep open axiom (= M4 = arithmetic Hodge
   standard conjecture).
4. **D-H audit** (`dh_audit` view) - any `dh_buildable='true'` content node on a
   load-bearing path to `TGT-rh` is a discipline VIOLATION. Returns ZERO rows:
   the firewall holds by type. The neutral carrier `PRIM-l-function`
   (`foundation`, shared substrate below where discrimination happens) is
   exempt and surfaced separately, never silently.
5. **Dischargeable axioms** (`dischargeable_axioms` view) - axioms / targets
   proven in a model (`proven_ff` / `proven_char0`) but open over Z, joined to
   their proven function-field face by a `specializes` edge. The M1 -> M4/M5
   lift templates.

## Adversary reconciliation (applied to the seed)

The seed graph is the reconciliation of the original draft with the adversary
graph audit. The corrections applied:

1. `LEM-m3-discriminator-no-geometry`: `dh_buildable` flipped `false -> true`
   (D-H instantiates the matrix and returns -0.929, a finite value; only the
   geometry is absent, which `dh_buildable` does not measure).
2. Edge `TGT-m4-hodge-standard -> LEM-m3-discriminator-no-geometry`: downgraded
   `depends_on -> motivates` (M3 adds no geometric content, so M4 cannot
   logically consume it).
3. `OBS-marginal-positivity`: `dh_buildable` flipped `false -> true` (the 78.7%
   figure is computed FROM D-H, same convention as `OBS-stealth-window`).
4. `TGT-rh`: the three non-logical premises downgraded from `depends_on`:
   `-> FND-rh-pi01` (`constrains`), `-> OBS-marginal-positivity`
   (`contextualizes`), `-> LEM-zeta-can-form-cup` (`contextualizes`). Only
   `-> TGT-m4-hodge-standard` and `-> LEM-pole-eigenvalue-bridge` remain as
   logical load.
5. `AX-noncircular-source`: layer retagged `signature -> foundation` (it is a
   methodology constraint, not a signature object).
6. The four placeholder-Euler `proven_lean` nodes (`PRIM-euler-product`,
   `PRIM-tate-twist-target`, `PRIM-cup-target`, `LEM-zeta-can-form-cup`)
   annotated "formation-only; zeta side rests on `has_euler_product := True`
   placeholder, VERIFIER #EP-1 still open" so the toy-witness caveat is not
   hidden.
7. Metadata corrected to 36 nodes / 63 edges (the original summary's 40/64 was
   wrong).
8. `dh_buildable = 'N/A'` set on the four `BRIDGE-ff-*` faces +
   `LEM-rosati-gram-formula` + `TGT-m1-ff-rosati` (function-field theorems have
   no D-H analogue; `'false'` overstated a category that does not apply).

After (1) + (2), the realization spine genuinely dead-ends and the firewall sits
at the type-level Euler-gated nodes (`PRIM-euler-product` and above), where it
belongs. The post-fix D-H audit is clean: the only `dh_buildable='true'` node on
the load path is the neutral foundation carrier `PRIM-l-function`, exempt by
design.

## How to add a lemma

1. Add a node object to `seed_lemmas.json` `"nodes"`:
   ```json
   {
     "id": "LEM-my-new-lemma",
     "kind": "lemma",
     "name": "Short title",
     "statement": "What it asserts.",
     "status": "open",
     "layer": "signature",
     "dh_buildable": "false",
     "milestone": null,
     "lean_ref": "",
     "experiment_ref": "experiments/...",
     "notes": "Why it matters; any caveat."
   }
   ```
   - `kind` in {primitive, axiom, lemma, theorem, target, obstruction}.
   - `status` in {open, conjectured, proven_ff, proven_char0, proven_lean,
     numerical_only, refuted}.
   - `layer` in {foundation, realization, signature, bridge}.
   - `dh_buildable` in {`"true"`, `"false"`, `"N/A"`}. Be honest: if the object
     can be evaluated on D-H, it is `"true"` even if it lacks geometry.
2. Add its dependency edges to `"edges"`. Use `depends_on` / `specializes` ONLY
   when the new node's truth genuinely requires the target's truth. Use an
   annotation kind (`motivates`, `instantiates`, ...) otherwise. Edges point
   from dependent to dependency.
3. Re-run `python experiments/lemma_db/build_db.py`. The loader will:
   - reject duplicate ids, dangling endpoints, and self-loops;
   - fail loudly if your new edges introduce a cycle in the load-bearing graph;
   - fail if `TGT-rh` stops being the unique sink;
   - re-run the D-H audit (exit non-zero if you put a `dh_buildable='true'`
     content node on a load-bearing path to `TGT-rh`).
4. If you added a load-bearing edge into `AX-hodge-riemann` or
   `LEM-pole-eigenvalue-bridge` from a `numerical_only` node, query Q9 (the K1
   guard) will flag it: positivity must come from a polarization, never from the
   zeros.
