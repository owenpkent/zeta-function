# Research Directions for the RH Proof Program

> Eight focused research directions identified by the project as the out-of-scope, research-grade work that would close the proof program described in [`../proof_program.md`](../proof_program.md). Each direction is documented with: problem statement, what "done" looks like, prerequisites, sub-problems, falsifiability, estimated effort, connections, references.
>
> These are not project-internal experiments. They are research programs requiring expert mathematicians at the postdoc-or-faculty level, operating over years. The documents here are the operational specifications that would allow such mathematicians (or research groups) to begin.

## The eight directions

| # | Direction | Doc | Phase in proof_program.md | Cumulative success probability |
|---|---|---|---|---|
| 1 | R2.5 Lambda-blueprints, developed rigorously | [`01_lambda_blueprints.md`](01_lambda_blueprints.md) | Phase 1 | 64% |
| 2 | R4 Borger+Connes hybrid Hilbert space and trace formula | [`02_borger_connes_hybrid.md`](02_borger_connes_hybrid.md) | Phase 2 (alt to #1) | 50% |
| 3 | R5 prismatic cohomology of Spec(W(Z)), all five Q resolved | [`03_prismatic_cohomology.md`](03_prismatic_cohomology.md) | Phase 2 | 35% |
| 4 | 2D-M3 prismatic foliation hypothesis verified | [`04_prismatic_foliation.md`](04_prismatic_foliation.md) | Phase 2 / 3 boundary | 25% |
| 5 | R3.6.3.a/b/c Connes-Consani infrastructure follow-ups | [`05_cc_infrastructure_followups.md`](05_cc_infrastructure_followups.md) | Phase 3 / 4 support | 15% |
| 6 | Bombieri variational SOS (outside LP/SDP framework) | [`06_bombieri_variational_sos.md`](06_bombieri_variational_sos.md) | Alternative escape route | 5-10% |
| 7 | Heath-Brown explicit multi-zero MT combined with 4E.2 | [`07_heath_brown_multi_zero_mt.md`](07_heath_brown_multi_zero_mt.md) | Architecture 4 partial escape | 10-15% (for ZFR constant, not RH) |
| 8 | The Hodge index theorem on a constructed surface | [`08_hodge_index_surface.md`](08_hodge_index_surface.md) | Phase 4 (THE central problem) | 5-12% |

## Reading order

For someone choosing what to work on:

- If you have background in **arithmetic geometry / F_1**: directions 1, 2, 4, 8.
- If you have background in **noncommutative geometry / Connes program**: directions 2, 5.
- If you have background in **prismatic cohomology / p-adic Hodge theory**: directions 3, 4.
- If you have background in **tropical geometry**: directions 5, 8.
- If you have background in **analytic number theory** (V-K, MT, exponential sums): directions 6, 7.

The most central direction is **#8: the Hodge index theorem on a constructed surface**. Directions 1-4 build the surface and surrounding infrastructure; direction 8 is the actual positivity theorem that closes RH. Direction 5 is a supporting infrastructure piece. Direction 6 is an alternative escape from the LP/SDP family; direction 7 is a partial improvement to the V-K zero-free region constant (which alone does not prove RH but is independently valuable).

## How the directions relate

```
                                    [proof_program.md]
                                           |
                       +-------------------+-------------------+
                       |                   |                   |
                  Surface side       Hodge index side    Other architectures
                       |                   |                   |
            +----+-----+-----+             |              +----+----+
            |    |     |     |             |              |         |
           R2.5  R4   R5   2D-M3        Direction        Bombieri  Heath-Brown
           #1   #2   #3    #4              #8             #6        #7
            |    |     |     |             ^
            +----+-----+-----+             |
                       |                   |
                  Infrastructure --------> assembles into
                       |
                   R3.6.3 #5
                       |
                  (infrastructure support)
```

Directions 1-4 build the surface, cohomology, foliation, and intersection theory that direction 8 needs. Direction 5 is infrastructure that might help direction 8. Directions 6 and 7 are alternative escape routes for the architectures other than 2's geometric route.

## Per-direction probability rationale

Each direction's success probability reflects:
- Existing partial progress in the literature (where there is more, probability is higher)
- The structural depth of the open problem (where it is shallower, probability is higher)
- The number of distinct attack angles available (where there are more, probability is higher)
- The historical track record of similar problems

Cumulative success probability for the FULL proof program (all directions executed successfully) is under 1%. Most directions, executed seriously, would produce major independent results even without the full proof.

## Per-direction estimated effort

| # | Direction | Effort (postdoc-years) | Effort (calendar years for a 3-5 person group) |
|---|---|---|---|
| 1 | Lambda-blueprints | 3-6 | 1-2 |
| 2 | Borger+Connes hybrid | 5-10 | 2-3 |
| 3 | Prismatic Q1-Q5 | 4-8 | 2-3 |
| 4 | Prismatic foliation | 4-8 | 2-4 |
| 5 | CC infrastructure | 8-15 | 3-5 |
| 6 | Bombieri variational SOS | 6-12 | 3-5 |
| 7 | Heath-Brown + 4E.2 | 5-10 | 2-4 |
| 8 | Hodge index | 20-50 | 7-15 |

Total: 55-119 postdoc-years for all directions in parallel. Realistic minimum funded program: $5-15M over 10-15 years for a group of 3-5 mathematicians plus collaborators and graduate students.

## What this project (the repo) can do for someone executing a direction

- Provide the 2A scorecard methodology and existing per-candidate analyses (Phase 0 of proof_program.md).
- Provide the Davenport-Heilbronn discipline as a K2 unit test (`experiments/_shared/davenport_heilbronn.py`).
- Provide the Bombieri explicit formula implementation as a validation tool (`experiments/positivity/e3f_weil_form_zeta.py`).
- Provide the R3.5 no-shortcut theorem as a structural input (`experiments/arithmetic_geometric/2A_R3_5_K1_universality.md`).
- Provide the LFunction interface for cross-Selberg-class testing.

What the project cannot do: execute the research-grade mathematics in any of the directions. That requires expert mathematicians.

## See also

- [`../proof_program.md`](../proof_program.md): the operational proof program.
- [`../../../experiments/arithmetic_geometric/2A_path_forward.md`](../../../experiments/arithmetic_geometric/2A_path_forward.md): the strategic plan one level up.
- [`../f1_arakelov_survey_2025.md`](../f1_arakelov_survey_2025.md): the F_1 and Arakelov landscape survey.
- [`../../../experiments/LEARNINGS.md`](../../../experiments/LEARNINGS.md): cross-architecture findings.
- [`../../../experiments/PROOF_ARCHITECTURES_PLAN.md`](../../../experiments/PROOF_ARCHITECTURES_PLAN.md): the test plan with all per-experiment status.
