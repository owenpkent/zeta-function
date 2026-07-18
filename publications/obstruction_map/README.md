# Obstruction map (expository survey)

A focused research note that maps the obstruction to RH for the Riemann zeta function as a single
missing object, an RH-equivalent polarization, pinned from four sides by four proven near-misses.

## Status

- **Tier:** DRAFT, expository survey. Not a proof; no new theorem claimed.
- **Type:** survey / methodology (the project's own localization + the standard literature).
- **Target venue class:** arXiv math.NT survey (or math.HO), an expository slot.
- **Relation to the registry:** this is a sharpened sibling of P4
  ([`../P4_survey_draft.md`](../P4_survey_draft.md)). P4 is the broad "all roads" survey; this note is
  the focused account of the **four-sided bracket** (FH / AHK / de Branges / Rankin-Selberg-Weil-II)
  and the **two disciplines** (marginal positivity, Davenport-Heilbronn). It can ship standalone or be
  folded into P4 as its bracket section. Decide at draft-finalization.

## What it argues

Every serious approach to RH reduces to one missing object: a signed intersection pairing of indefinite
signature $(1, n-1)$ on the cohomology of $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$,
whose positivity is RH. Over a curve $C/\mathbb{F}_q$ this is Weil's proof (the Hodge index theorem on
$C \times C$). Over $\mathrm{Spec}(\mathbb{Z})$ it is variety-gated and splits into two facets (R1
sourcing/purity, M4 polarization/signature). The organizing device is a four-sided bracket plus the two
cross-cutting disciplines.

## Honesty contract (same standard as PUBLICATIONS.md)

- The convergence claim (RH = the missing polarization = the arithmetic Hodge standard conjecture) is
  **known folklore**, framed as an organizing equivalence, never as progress toward a proof.
- The novel residue is the **organizing device** (the four-sided bracket, with the fourth side
  Rankin-Selberg / Weil-II "too shallow" as the 2026 addition) and the two disciplines as a spine.
- Every result is tagged PROVEN or CONJECTURAL; every named theorem is attributed.

## Open review items (must clear before any "ready" / submission)

1. **Source-verify the literature.** Re-confirm at the source the arXiv ids, authors, venues, and dates
   for the items not personally re-verified in this draft: Rodgers-Tao $\Lambda \ge 0$ (Duke 2020);
   Connes-Consani archimedean Weil positivity (Selecta 2021, arXiv:2006.13771); the CCM semilocal
   prolate operator (arXiv:2310.18423, confirm year/authorship); Petrov Sen-non-semisimplicity
   (arXiv:2302.11389, Annals); Dobner $S^\#$ (2020) and Newman-Wu (2019); Fuchs 1964 / Slepian 1965;
   Yuan-Zhang (Math. Ann. 367, 2017); Bost (Prog. Math. 334, 2020, arXiv:1512.08946). Pin Connes'
   Figure 1 / equation number in arXiv:2602.04022 by human eyeball (the HTML fetch renders figures
   poorly; this caveat is carried from PUBLICATIONS.md P8). Now source-read (VERIFIED-BY-FETCH per the
   four 2026 reading notes): the Arakelov triple (He 2512.01811, Abboud 2503.14099, Chen-Moriwaki
   2207.02033) and Connes-Consani 2606.06604; the model-theoretic corpus (Kaplan-Shelah 1601.07099,
   Hrushovski math/0406514, Ax 1968) is source-anchored via the two dossiers
   (`model_theoretic_frobenius.md`, `tameness_trade.md`).
2. **Expert reader for the polarization column** (the same prerequisite P4 carries): the scorecard makes
   precise arithmetic-geometry claims (prismatic duality without sign, Sen non-semisimplicity blocking
   eigenspace polarizations, the Arakelov base relocation) that want a referee-grade reader before
   circulation.
3. **Confirm the bracket's fourth side is not pre-empted as a *frame*.** The four-sided
   pinning-from-four-sides device is the note's claimed organizational novelty; lit-check that no
   existing survey already organizes the obstruction this way (the P4 lit-check found Connes 2602.04022
   and the MDPI Symmetry 2025 survey do not; extend to Deninger's program notes and a prismatic/THH
   survey). The `fh-too-local` side now carries fresh 2022-2025 multi-paper confirmation (He, Abboud,
   Chen-Moriwaki), which strengthens (does not weaken) the frame's robustness.
4. **Decide standalone vs fold-into-P4** once items 1-3 clear.

## Files

- `obstruction_map.md`: the draft (this directory's deliverable).
- `README.md`: this file.
