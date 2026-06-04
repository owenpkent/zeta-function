# Overnight autonomous work log (started 2026-06-03)

Owen said "work overnight." Autonomous BUILDER/VERIFIER/SYNTHESIZER cycles on the RH program.
Each cycle: pick the next backlog item, build/run an experiment or write a dossier, document
(LEARNINGS + TODO + this log), commit and push. Honesty discipline: negative results are
coordinates; no fabricated proofs; every Arch 1/3/4 result must pass the Davenport-Heilbronn check.

Stop condition: when the high-value backlog is genuinely exhausted, stop and record it rather than
generate filler.

## Backlog (curated, buildable now, distinct, each adds a real coordinate)

- [x] C1. Function-field polarization made concrete (the case where Level 5 EXISTS). Build the
  intersection form on NS(E x E) for elliptic curves over F_p, verify the Hodge-index signature
  (1, n-1) and the primitive-part negative-definiteness = the Rosati/RH bound a^2 <= 4q, and show
  the buffer is O(q) (healthy/definite) vs the integer case's e^{-4 pi x} (marginal, e3v). Exhibits
  exactly what the missing object looks like where it is a theorem.
- [ ] C2. Verify Connes Theorem 7.1 (Sonin-space archimedean positivity) numerically:
  W_inf(g*g*) >= Tr(theta(g) S theta(g)*) for g supported in [2^-1/2, 2^1/2]. A proven paper claim.
- [ ] C3. The seam, quantified: across a family, show the off-line indefiniteness is attributable
  entirely to the prime block (sharpening #46) and the archimedean block carries none of it, by a
  clean ablation that varies mu/Q (archimedean) vs the coefficients (prime).
- [ ] C4. Bost-Connes K2 sharpening: D-H is a KMS mixture, never a pure product state. Make the
  multiplicativity failure concrete (a_{mn} != a_m a_n for D-H; a_m a_n = a_mn for zeta) as the
  obstruction to the product-state / Euler-factor construction.
- [x] C5. Session capstone synthesis dossier: Connes 2602 -> candidate proof -> assume-RH ->
  marginal wall -> construction sweep, with the single sharpened statement of the missing math and
  the full coordinate map of what this session ruled out.
- [ ] C6. Lean: formalize the Rankin loglog-coefficient discriminator as a def, or attempt an #ACC sorry.
- [ ] C7. (stretch) de Branges Q(rho) density refinement / second L-function controls.

## Cycle log

- C1 (e3x_function_field_polarization, LEARNINGS #54): built the intersection form on NS(E x E) for
  23 elliptic curves over F_p. Signature exactly (1,3) for ALL (Hodge index theorem confirmed),
  primitive part negative-definite, buffer 4q - a^2 > 0 with median 2.88 q (O(q), healthy). The
  polarization the integer case lacks, exhibited where it is a theorem; contrast with the e3v
  e^{-4 pi x} marginal wall names the missing math precisely. Committed + pushed.
- C5 (session_2026_06_03_capstone.md): coordinate map of the whole session (Connes 2602 -> candidate
  proof -> assume-RH -> marginal wall -> construction sweep -> function-field contrast), with the
  single sharpened statement of the missing math and the full negative map of what was ruled out.
  Done out of order (low-risk synthesis) so a coherent narrative exists early. Committed + pushed.
