-- schema.sql
-- DuckDB schema for the RH bespoke-system lemma dependency graph.
--
-- The graph is a DAG whose single sink is TGT-rh (the Riemann Hypothesis for
-- zeta). Every node is a primitive, axiom, lemma, theorem, target, or
-- obstruction in the purpose-built system that takes the SIGNATURE/polarization
-- structure as its core (not the realization/trace half, which is shared with
-- the Davenport-Heilbronn counterexample).
--
-- Two cross-cutting disciplines are operationalized as SQL:
--   * The D-H discipline: dh_buildable flags whether the object can be
--     instantiated on Davenport-Heilbronn. Any dh_buildable=true node on a
--     LOAD-BEARING path to TGT-rh is a discipline violation (the dh_audit view).
--   * The K1 non-circularity discipline: positivity must come from a
--     polarization, never read off the zeros.
--
-- The M1-M5 milestone ladder (Direction 8A) is encoded by the milestone column
-- and the layer column (foundation / realization / signature / bridge).

-- Idempotent (re)build: drop in dependency order (views before tables).
DROP VIEW IF EXISTS frontier_ranked;
DROP VIEW IF EXISTS asserted_vs_proven;
DROP VIEW IF EXISTS node_support;
DROP VIEW IF EXISTS dischargeable_axioms;
DROP VIEW IF EXISTS open_signature_nodes;
DROP VIEW IF EXISTS dh_audit;
DROP VIEW IF EXISTS rh_transitive_deps;
DROP VIEW IF EXISTS frontier;
DROP VIEW IF EXISTS load_edge;
DROP TABLE IF EXISTS obstruction_link;
DROP TABLE IF EXISTS edge;
DROP TABLE IF EXISTS node;

-- ---------------------------------------------------------------------------
-- node: one row per primitive / axiom / lemma / theorem / target / obstruction.
-- ---------------------------------------------------------------------------
CREATE TABLE node (
    id              VARCHAR PRIMARY KEY,
    kind            VARCHAR NOT NULL,   -- primitive | axiom | lemma | theorem | target | obstruction
    name            VARCHAR NOT NULL,
    statement       VARCHAR NOT NULL,
    -- proof / verification status, controlled vocabulary:
    --   open | conjectured | proven_ff | proven_char0 | proven_lean
    --   | numerical_only | refuted
    status          VARCHAR NOT NULL,
    -- which half of the program the node lives in:
    --   foundation | realization | signature | bridge
    layer           VARCHAR NOT NULL,
    -- D-H discipline flag. TRUE  => the object can be instantiated on
    -- Davenport-Heilbronn (a number comes out); this is the easy realization
    -- half and MUST NOT lie on a load-bearing path to TGT-rh.
    -- FALSE => structurally unbuildable for D-H (the signature half = real work).
    -- 'N/A' => function-field theorem; D-H has no analogue, the flag does not apply.
    dh_buildable    VARCHAR NOT NULL,   -- 'true' | 'false' | 'N/A'
    -- M1..M5 milestone tag (Direction 8A), NULL when the node is not a milestone.
    milestone       VARCHAR,
    lean_ref        VARCHAR,
    experiment_ref  VARCHAR,
    notes           VARCHAR,
    CHECK (kind IN ('primitive','axiom','lemma','theorem','target','obstruction','candidate')),
    CHECK (status IN ('open','conjectured','proven_ff','proven_char0',
                      'proven_lean','numerical_only','refuted')),
    CHECK (layer IN ('foundation','realization','signature','bridge')),
    CHECK (dh_buildable IN ('true','false','N/A'))
);

-- ---------------------------------------------------------------------------
-- edge: directed edges from dependent node to its dependency / related node.
--
-- LOAD-BEARING (logical) kinds: 'depends_on', 'specializes'. These are the only
-- kinds the DAG-validation and the frontier / rh_transitive_deps / dh_audit
-- views traverse. An edge A --depends_on--> B means "A's truth logically
-- requires B's truth". 'specializes' means A is the arithmetic abstraction of a
-- proven function-field face B (still a genuine logical lift on the load path).
--
-- NON-LOAD (annotation) kinds: do NOT propagate proof obligation. They record
-- structure without making the target consume the source as a premise:
--   'instantiates'      a concrete lemma realizes an obstruction/axiom
--   'contradicts'       records a negative result or a K1 guard
--   'bridges'           links obstruction-cluster nodes
--   'motivates'/'informs'  the source informs but is not a premise of the target
--   'constrains'/'contextualizes'  a foundation/numerical node frames a target
-- ---------------------------------------------------------------------------
CREATE TABLE edge (
    from_id   VARCHAR NOT NULL REFERENCES node(id),
    to_id     VARCHAR NOT NULL REFERENCES node(id),
    kind      VARCHAR NOT NULL,
    notes     VARCHAR,
    PRIMARY KEY (from_id, to_id, kind),
    CHECK (kind IN ('depends_on','specializes','instantiates','contradicts',
                    'bridges','motivates','informs','constrains','contextualizes')),
    CHECK (from_id <> to_id)
);

-- ---------------------------------------------------------------------------
-- obstruction_link: explicit, queryable association between an obstruction node
-- and the node it obstructs / explains, with the relation spelled out. This is
-- a denormalized convenience surface over the obstruction edges so the
-- discipline can be inspected without re-deriving it from edge.kind each time.
-- ---------------------------------------------------------------------------
CREATE TABLE obstruction_link (
    obstruction_id  VARCHAR NOT NULL REFERENCES node(id),
    target_id       VARCHAR NOT NULL REFERENCES node(id),
    relation        VARCHAR NOT NULL,   -- e.g. 'blocks' | 'explains' | 'gates' | 'why_hard'
    notes           VARCHAR,
    PRIMARY KEY (obstruction_id, target_id, relation)
);

-- ===========================================================================
-- VIEWS
-- ===========================================================================

-- load_edge: the logical sub-graph. Only these edges carry proof obligation and
-- are traversed by the reachability views below.
CREATE VIEW load_edge AS
    SELECT from_id, to_id, kind
    FROM edge
    WHERE kind IN ('depends_on','specializes');

-- A node counts as "proven" (a discharged dependency) when its status is one of
-- the terminal-verified states. numerical_only and conjectured do NOT count as
-- proven; open and refuted obviously do not. We centralize this predicate as a
-- macro so every view shares one definition.
CREATE OR REPLACE MACRO is_proven(s) AS
    s IN ('proven_ff','proven_char0','proven_lean');

-- ---------------------------------------------------------------------------
-- frontier: open nodes ALL of whose load-bearing dependencies are proven.
-- These are the nodes where work can actually start: nothing below them is
-- still open. An open node with no load-bearing dependencies at all also counts
-- (vacuously all-proven), which surfaces axioms/primitives ready to be attacked.
-- ---------------------------------------------------------------------------
CREATE VIEW frontier AS
SELECT n.id, n.kind, n.name, n.status, n.layer, n.dh_buildable, n.milestone
FROM node n
WHERE n.status NOT IN ('proven_ff','proven_char0','proven_lean','refuted')
  AND NOT EXISTS (
        SELECT 1
        FROM load_edge e
        JOIN node d ON d.id = e.to_id
        WHERE e.from_id = n.id
          AND NOT is_proven(d.status)
  );

-- ---------------------------------------------------------------------------
-- rh_transitive_deps: the transitive closure of everything TGT-rh needs along
-- LOAD-BEARING edges (depends_on / specializes). This is the actual proof
-- obligation set for the Riemann Hypothesis. depth = shortest load-edge
-- distance from TGT-rh.
-- ---------------------------------------------------------------------------
CREATE VIEW rh_transitive_deps AS
WITH RECURSIVE reach(id, depth) AS (
    SELECT to_id AS id, 1 AS depth
    FROM load_edge
    WHERE from_id = 'TGT-rh'
    UNION
    SELECT e.to_id, r.depth + 1
    FROM reach r
    JOIN load_edge e ON e.from_id = r.id
)
SELECT n.id, n.kind, n.name, n.status, n.layer, n.dh_buildable, n.milestone,
       MIN(r.depth) AS depth
FROM reach r
JOIN node n ON n.id = r.id
GROUP BY n.id, n.kind, n.name, n.status, n.layer, n.dh_buildable, n.milestone;

-- ---------------------------------------------------------------------------
-- dh_audit: THE D-H DISCIPLINE AUDIT. Flag any dh_buildable='true' node that
-- lies on a LOAD-BEARING dependency path to TGT-rh AND carries mathematical
-- content (layer in realization / signature / bridge). Such a node would mean a
-- Davenport-Heilbronn-buildable (realization-half) object is a logical premise
-- of RH, i.e. the proof would also "work" for the counterexample = structurally
-- wrong. After the adversary fixes this view returns ZERO rows: the firewall
-- holds by type on every content spine.
--
-- WHY foundation-layer nodes are exempt. The neutral carrier PRIM-l-function is
-- dh_buildable='true' (both zeta and D-H instantiate it) and is necessarily on
-- the load path, because everything is built on an L-function. It is the shared
-- substrate BELOW which discrimination cannot happen, by design (see its node
-- note). A foundation-layer node carries calibration/substrate, never the
-- proof's mathematical content, so its being shared is expected, not a leak.
-- The discipline is about content nodes (realization / signature / bridge): a
-- dh_buildable='true' content node on the path is a realization-half object
-- masquerading as load-bearing signature work, which is the actual violation.
--
-- The view reuses rh_transitive_deps (already load-edge-only) and filters to the
-- D-H-buildable content nodes. Any row here is a violation to be investigated.
-- ---------------------------------------------------------------------------
CREATE VIEW dh_audit AS
SELECT d.id, d.kind, d.name, d.status, d.layer, d.dh_buildable, d.depth,
       'VIOLATION: dh_buildable content node on load-bearing path to TGT-rh' AS verdict
FROM rh_transitive_deps d
WHERE d.dh_buildable = 'true'
  AND d.layer <> 'foundation';

-- ---------------------------------------------------------------------------
-- open_signature_nodes: the real work. Signature-layer nodes whose status is
-- still open/conjectured/numerical_only. These are the unbuildable-for-D-H
-- objects (the actual content of RH) that remain to be established.
-- Ordered so the deepest open axiom surfaces first.
-- ---------------------------------------------------------------------------
CREATE VIEW open_signature_nodes AS
SELECT id, kind, name, status, dh_buildable, milestone, experiment_ref
FROM node
WHERE layer = 'signature'
  AND status IN ('open','conjectured','numerical_only');

-- ---------------------------------------------------------------------------
-- dischargeable_axioms: axioms/theorems PROVEN in a model (function field or
-- char-0 Hodge theory) but still OPEN over Z. These are the templates whose
-- arithmetic lift is the remaining work: proven_ff / proven_char0 establishes
-- the shape, but the integral (over Spec Z) statement is not yet a theorem.
--
-- Operationally: a node that is proven in some model AND has a load-bearing
-- consumer that is still open, OR is itself an axiom marked open while its
-- function-field face is proven. We surface both the proven model-faces and the
-- open arithmetic axioms they discharge, joined by 'specializes' edges.
-- ---------------------------------------------------------------------------
CREATE VIEW dischargeable_axioms AS
SELECT
    open_ax.id        AS open_axiom_id,
    open_ax.name      AS open_axiom_name,
    open_ax.status    AS open_axiom_status,     -- open over Z
    open_ax.milestone AS milestone,
    ff.id             AS proven_face_id,
    ff.name           AS proven_face_name,
    ff.status         AS proven_face_status      -- proven_ff / proven_char0
FROM edge sp
JOIN node open_ax ON open_ax.id = sp.from_id
JOIN node ff      ON ff.id      = sp.to_id
WHERE sp.kind = 'specializes'
  AND open_ax.status IN ('open','conjectured','numerical_only')
  AND ff.status IN ('proven_ff','proven_char0');

-- ---------------------------------------------------------------------------
-- node_support: per-node support metrics, the substrate for the value function
-- and the asserted-vs-proven gap (Reduction Engine increment 3).
--   load_in_degree       = LOAD-BEARING dependents: how many nodes logically
--                          REQUIRE this one. This is PROVEN support.
--   annotation_in_degree = non-load (annotation) edges pointing at it
--                          (instantiates / motivates / contradicts / ...). This
--                          is ASSERTED support: it carries no proof obligation.
--   rh_depth             = shortest load-bearing distance from TGT-rh (0 if off
--                          the RH load path).
-- The convergence onto the signature is almost entirely ASSERTED, and the gap
-- between the two in-degrees is the engine's honesty diagnostic.
-- ---------------------------------------------------------------------------
CREATE VIEW node_support AS
SELECT
    n.id, n.kind, n.name, n.status, n.layer, n.milestone, n.dh_buildable,
    COALESCE((SELECT r.depth FROM rh_transitive_deps r WHERE r.id = n.id), 0) AS rh_depth,
    (SELECT COUNT(*) FROM load_edge e WHERE e.to_id = n.id) AS load_in_degree,
    (SELECT COUNT(*) FROM edge e
       WHERE e.to_id = n.id
         AND e.kind NOT IN ('depends_on','specializes')) AS annotation_in_degree
FROM node n;

-- ---------------------------------------------------------------------------
-- frontier_ranked: the value function. Rank the live edge of the search by
-- DEPTH in the load-bearing graph and PROVEN support, never asserted support.
-- M4 (AX-polarization) dominates by DEPTH: its load_in_degree is small and its
-- annotation_in_degree is large, and ranking by the latter would be the
-- circular "all roads converge" count the engine refuses. asserted_minus_proven
-- rides alongside as the honesty diagnostic, never as a score to maximize.
-- ---------------------------------------------------------------------------
CREATE VIEW frontier_ranked AS
SELECT
    s.id, s.kind, s.name, s.status, s.layer, s.milestone, s.dh_buildable,
    s.rh_depth, s.load_in_degree, s.annotation_in_degree,
    (s.annotation_in_degree - s.load_in_degree) AS asserted_minus_proven
FROM node_support s
JOIN frontier f ON f.id = s.id
ORDER BY s.rh_depth DESC, s.load_in_degree DESC, asserted_minus_proven DESC, s.id;

-- ---------------------------------------------------------------------------
-- asserted_vs_proven: the engine's headline diagnostic. For every node carrying
-- any support, the gap between asserted (annotation) and proven (load-bearing)
-- in-degree. A large gap = "much believed, little reduced." The deepest open
-- kernel tops this list: many CAND-* instantiation edges ASSERT that candidates
-- converge on it, while almost none is a PROVEN reduction. The gap points at
-- exactly which annotation edges to go prove. It is a diagnostic to read, never
-- a loss to minimize (minimizing it by declining to survey is gaming, not work).
-- ---------------------------------------------------------------------------
CREATE VIEW asserted_vs_proven AS
SELECT
    id, kind, name, status, layer, milestone,
    annotation_in_degree, load_in_degree,
    (annotation_in_degree - load_in_degree) AS gap
FROM node_support
WHERE annotation_in_degree > 0 OR load_in_degree > 0
ORDER BY gap DESC, annotation_in_degree DESC, id;
