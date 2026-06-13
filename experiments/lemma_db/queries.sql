-- queries.sql
-- Named example queries for the RH lemma-graph DuckDB database.
--
-- Run after building:  python experiments/lemma_db/build_db.py
-- Then, e.g.:          duckdb experiments/lemma_db/lemma_graph.duckdb < experiments/lemma_db/queries.sql
-- or paste individual blocks into the duckdb CLI / a Python duckdb connection.
--
-- All reachability queries traverse ONLY load-bearing edges (depends_on,
-- specializes), surfaced by the load_edge view. Annotation edges (instantiates,
-- contradicts, bridges, motivates, informs, constrains, contextualizes) do not
-- carry proof obligation and are excluded from the load path on purpose.

-- ===========================================================================
-- Q1. FRONTIER
-- Open nodes ALL of whose load-bearing dependencies are already proven. These
-- are where work can start right now: nothing below them is still open.
-- The deep prize here is AX-polarization (M4): the open arithmetic axiom whose
-- only load dependency, PRIM-cup-target, is a proven_lean formation node.
-- ===========================================================================
SELECT id, kind, name, status, layer, dh_buildable, milestone
FROM frontier
ORDER BY (milestone IS NULL), milestone, id;

-- ===========================================================================
-- Q2. RH TRANSITIVE DEPENDENCIES
-- Everything TGT-rh needs, transitively, along load-bearing edges. This is the
-- full proof-obligation set for the Riemann Hypothesis. depth = shortest
-- load-edge distance from TGT-rh.
-- ===========================================================================
SELECT id, kind, name, status, layer, dh_buildable, milestone, depth
FROM rh_transitive_deps
ORDER BY depth, id;

-- Q2a. RH dependency COUNT, split by whether the dependency is discharged.
SELECT
    count(*)                                                        AS total_deps,
    count(*) FILTER (WHERE status IN ('proven_ff','proven_char0','proven_lean')) AS proven,
    count(*) FILTER (WHERE status NOT IN ('proven_ff','proven_char0','proven_lean')) AS still_open
FROM rh_transitive_deps;

-- Q2b. The OPEN remainder of the RH proof obligation, deepest-content first.
SELECT id, kind, status, layer, milestone, depth
FROM rh_transitive_deps
WHERE status NOT IN ('proven_ff','proven_char0','proven_lean')
ORDER BY depth DESC, id;

-- ===========================================================================
-- Q3. OPEN SIGNATURE-LAYER NODES  (the real work)
-- Signature-layer nodes still open / conjectured / numerical_only. These are the
-- D-H-UNbuildable objects that ARE the content of RH (or the soft shadows of
-- them). AX-hodge-riemann is the single deep open axiom (= M4 = arithmetic Hodge
-- standard conjecture).
-- ===========================================================================
SELECT id, kind, name, status, dh_buildable, milestone, experiment_ref
FROM open_signature_nodes
ORDER BY (milestone IS NULL), milestone, status, id;

-- Q3a. Just the open AXIOMS (the exposed open content), with their milestone.
SELECT id, name, status, milestone, dh_buildable
FROM node
WHERE kind = 'axiom' AND status IN ('open','conjectured','numerical_only')
ORDER BY (milestone IS NULL), milestone, id;

-- ===========================================================================
-- Q4. D-H DISCIPLINE AUDIT
-- Flag any dh_buildable='true' CONTENT node (layer realization/signature/bridge)
-- on a load-bearing path to TGT-rh. A non-empty result is a discipline
-- VIOLATION: a Davenport-Heilbronn-buildable realization-half object would be a
-- logical premise of RH, so the proof would also "work" for the counterexample.
-- Expected result after the adversary fixes: ZERO rows.
-- ===========================================================================
SELECT id, kind, name, status, layer, dh_buildable, depth, verdict
FROM dh_audit
ORDER BY depth, id;

-- Q4a. The exempt neutral carrier(s): dh_buildable='true' FOUNDATION nodes on the
-- path. These are the shared substrate (every proof is built on an L-function),
-- below where discrimination happens. Surfaced so the exemption is never silent.
SELECT d.id, d.name, d.depth
FROM rh_transitive_deps d
WHERE d.dh_buildable = 'true' AND d.layer = 'foundation'
ORDER BY d.depth, d.id;

-- Q4b. The full D-H ledger: every node by dh_buildable, layer, and whether it is
-- on the RH load path. Lets you read off the firewall at a glance.
SELECT
    n.dh_buildable,
    n.layer,
    count(*) AS n_nodes,
    count(*) FILTER (WHERE rd.id IS NOT NULL) AS on_rh_load_path,
    string_agg(n.id, ', ' ORDER BY n.id) AS ids
FROM node n
LEFT JOIN rh_transitive_deps rd ON rd.id = n.id
GROUP BY n.dh_buildable, n.layer
ORDER BY n.dh_buildable, n.layer;

-- ===========================================================================
-- Q5. DISCHARGEABLE AXIOMS
-- Axioms / targets PROVEN in a model (proven_ff over F_q, or proven_char0 via
-- Hodge theory) but still OPEN over Z. Joined to their proven model-face via the
-- 'specializes' edge: the function-field theorem is the template, the arithmetic
-- lift over Spec(Z) is the remaining work. This is the M1 -> M4/M5 ladder made
-- explicit: AX-hodge-riemann specializes the proven four-faces equivalence;
-- LEM-pole-eigenvalue-bridge specializes |alpha|=sqrt(q); M4 specializes M1.
-- ===========================================================================
SELECT open_axiom_id, open_axiom_name, open_axiom_status, milestone,
       proven_face_id, proven_face_name, proven_face_status
FROM dischargeable_axioms
ORDER BY (milestone IS NULL), milestone, open_axiom_id;

-- ===========================================================================
-- Q6. THE EXPOSED OPEN AXIOM (what proving discharges what)
-- AX-hodge-riemann is the unique deep open axiom. Show what TGT-rh-relevant
-- nodes become reachable / dischargeable once it is proven: everything that
-- load-depends on it, directly or transitively.
-- ===========================================================================
WITH RECURSIVE consumers(id) AS (
    SELECT from_id FROM load_edge WHERE to_id = 'AX-hodge-riemann'
    UNION
    SELECT e.from_id FROM consumers c JOIN load_edge e ON e.to_id = c.id
)
SELECT n.id, n.kind, n.status, n.layer, n.milestone
FROM consumers c JOIN node n ON n.id = c.id
ORDER BY n.id;

-- ===========================================================================
-- Q7. MILESTONE LADDER STATUS  (M1 .. M5)
-- One row per milestone node with its status, so the M1-M5 ladder reads off the
-- DB directly. M1 done (proven_ff); M2.x numerical_only; M3 numerical_only;
-- M4/M5 open.
-- ===========================================================================
SELECT milestone, id, kind, status, layer, dh_buildable
FROM node
WHERE milestone IS NOT NULL
ORDER BY milestone, id;

-- ===========================================================================
-- Q8. OBSTRUCTION LEDGER
-- Every obstruction node and what it blocks / explains / makes hard, via the
-- derived obstruction_link table.
-- ===========================================================================
SELECT ol.obstruction_id, o.name AS obstruction_name, ol.relation,
       ol.target_id, t.name AS target_name
FROM obstruction_link ol
JOIN node o ON o.id = ol.obstruction_id
JOIN node t ON t.id = ol.target_id
ORDER BY ol.obstruction_id, ol.target_id;

-- ===========================================================================
-- Q9. K1 NON-CIRCULARITY GUARD
-- Confirm no positivity-certificate / numerical node feeds AX-hodge-riemann or
-- LEM-pole-eigenvalue-bridge along a load-bearing edge. Any row here would be a
-- K1-circular leak (positivity read off the zeros). Expected: ZERO rows.
-- ===========================================================================
SELECT e.from_id, src.status, e.kind, e.to_id
FROM load_edge e
JOIN node src ON src.id = e.from_id
WHERE e.to_id IN ('AX-hodge-riemann','LEM-pole-eigenvalue-bridge')
  AND src.status = 'numerical_only';


-- queries.sql addition: COLLAPSE vs OFF-TO-SIDE diagnostic for the 17 candidate
-- cohomologies (Spec(Z) zeta-realization landscape).
--
-- Question this answers: do the candidates' missing-positivity all COLLAPSE onto
-- the single node TGT-m4-hodge-standard (gap irreducible => the no-go IS the
-- target), or do some sit genuinely OFF TO THE SIDE as distinct bracket nodes
-- (=> that near-miss is the attack target)? It counts candidate nodes grouped by
-- the node their annotation edge resolves to, classifies each group, and shows
-- the single gap property each off-to-side bracket is missing.
--
-- A candidate resolves via its (non-load-bearing) annotation edge:
--   instantiates TGT-m4-hodge-standard  => COLLAPSE onto the universal gap
--   instantiates/specializes NODE-*      => OFF-TO-SIDE proven-signature bracket
--   instantiates OBS-k1-circularity      => K1 WALL (circular, must escape first)
--   instantiates PRIM-euler-product      => PRE-REALIZATION (upstream of the gap)
-- The off-to-side brackets carry a 'constrains'/'contradicts' edge to the one
-- PROP-* node they violate; that edge supplies the missing_property column.
WITH cand AS (
    SELECT id
    FROM node
    WHERE kind = 'candidate' AND id LIKE 'CAND-%'
),
resolves AS (
    SELECT c.id AS candidate_id, e.to_id AS resolves_to
    FROM cand c
    JOIN edge e ON e.from_id = c.id
    WHERE e.kind IN ('instantiates', 'specializes')   -- annotation edges only
      AND ( e.to_id = 'TGT-m4-hodge-standard'
         OR e.to_id = 'OBS-k1-circularity'
         OR e.to_id = 'PRIM-euler-product'
         OR e.to_id LIKE 'NODE-%' )
),
-- The single PROP a given resolve-target (a bracket) is tagged as missing.
missing_prop AS (
    SELECT e.from_id AS resolves_to, e.to_id AS prop
    FROM edge e
    WHERE e.kind IN ('constrains', 'contradicts')
      AND e.to_id LIKE 'PROP-%'
)
SELECT
    r.resolves_to,
    CASE
        WHEN r.resolves_to = 'TGT-m4-hodge-standard' THEN 'COLLAPSE (= the universal gap, irreducible)'
        WHEN r.resolves_to LIKE 'NODE-%'             THEN 'OFF-TO-SIDE proven-signature bracket'
        WHEN r.resolves_to = 'OBS-k1-circularity'    THEN 'K1 WALL (circular; escape before attacking)'
        WHEN r.resolves_to = 'PRIM-euler-product'    THEN 'PRE-REALIZATION (upstream; no zeta yet)'
        ELSE 'other'
    END AS classification,
    COUNT(*) AS n_candidates,
    COALESCE(MAX(m.prop), '(none: the four-property conjunction itself)') AS missing_property
FROM resolves r
LEFT JOIN missing_prop m ON m.resolves_to = r.resolves_to
GROUP BY r.resolves_to, classification
ORDER BY n_candidates DESC, r.resolves_to;
-- Expected result: TGT-m4-hodge-standard collapses 9 realization candidates with
-- missing_property = the conjunction (no single drop); three NODE-* brackets each
-- carry 1-2 candidates and a distinct single missing PROP (NODE-fh-too-local /
-- PROP-global x2 = Faltings-Hriljac + Gillet-Soule; NODE-ahk-too-blind /
-- PROP-carries-trace; NODE-debranges-too-strong / PROP-rh-equivalent); 2 on the
-- K1 wall; 2 pre-realization. Collapse count (9) dominates; off-to-side count (4
-- candidates over 3 distinct nodes) brackets but does not dissolve the gap.

-- ===========================================================================
-- Q10. VALUE RANKING  (Reduction Engine increment 3)
-- Rank the frontier by DEPTH in the load-bearing graph and PROVEN support
-- (load_in_degree), never by asserted support. M4 (AX-polarization) ranks high
-- by depth; ranking it by annotation_in_degree instead would be the circular
-- "all roads converge" count the engine refuses. asserted_minus_proven rides
-- alongside as a diagnostic, never a score to maximize.
-- ===========================================================================
SELECT id, layer, milestone, rh_depth, load_in_degree, annotation_in_degree,
       asserted_minus_proven
FROM frontier_ranked;

-- ===========================================================================
-- Q11. ASSERTED-VS-PROVEN GAP  (the engine's headline diagnostic)
-- For every node with support, the gap between asserted (annotation) and proven
-- (load-bearing) in-degree. TGT-m4-hodge-standard tops it: 17 CAND-* edges
-- ASSERT convergence onto it; only 1 is a load-bearing reduction (gap 16). A
-- large gap = much believed, little reduced, and names the edges to go prove.
-- ===========================================================================
SELECT id, layer, milestone, annotation_in_degree, load_in_degree, gap
FROM asserted_vs_proven
WHERE gap > 0;
