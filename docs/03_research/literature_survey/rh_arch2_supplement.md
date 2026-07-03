# Supplement — literature aligned to the repo's live proof front

*Companion to `rh_literature_map.md`. That map surveyed the RH literature by the generic six-thread taxonomy (spectral, RMT/moments, log-correlated, positivity criteria, zero-density, general-RH) — the right frame for the field at large, but it __under-samples the arithmetic-geometry substrate where this repo's live work actually sits__. This supplement corrects that, using the repo's own architecture as the organizing frame.*

## Why this supplement exists

Per `STATE_OF_THE_PROGRAM.md`, three of the four candidate architectures are closed at the project level (Arch 1 spectral, Arch 3 direct positivity, Arch 4 analytic / zero-free), and the **live front is Architecture 2 (arithmetic-geometric)**: the target is a **Hodge-index / Rosati positivity (M4)** on a Spec(Z) x Spec(Z) product surface, with two concrete candidate substrates — **Bhatt–Lurie's Cartier–Witt stack `WCart`** and the **Connes–Consani square**.

My general search vocabulary (zeros, critical line, moments, pair correlation) maps onto the three *closed* architectures. A supplementary sweep on prismatic cohomology, Sen/Frobenius operators, arithmetic Hodge-index theory, F_1 geometry, and the Connes–Consani / Deninger programs surfaced **108 papers the main map missed** (mostly `math.AG`), of which the 17 below are most relevant to the M4 signature question.

**State of this substrate literature (2021–2026):** This substrate literature is highly active but fragmented — Bhatt-Lurie/WCart prismatic foundations and Sen-operator theory are maturing rapidly, arithmetic Hodge-index/positivity results are proliferating in Arakelov settings, and Connes-Consani continue building spectral/adelic RH strategies, but no paper yet supplies the missing polarization linking these two substrates into a single signature.

---

## A. Prismatic / WCart / Sen-operator foundations
*The `WCart` substrate. Direction 8B/8C, and the 2026-06-04 needle-map's choice of WCart over the Connes–Consani square, live here.*

- **The prismatization of $p$-adic formal schemes** — Bhargav Bhatt; Jacob Lurie (2022-01, [2201.06124](https://arxiv.org/abs/2201.06124))  
  Bhatt-Lurie WCart/Cartier-Witt stack — the literal candidate substrate for M4 signature
- **Absolute prismatic cohomology** — Bhargav Bhatt; Jacob Lurie (2022-01, [2201.06120](https://arxiv.org/abs/2201.06120))  
  Bhatt-Lurie absolute prismatic cohomology defining Frobenius on WCart, foundational to Architecture 2
- **Hodge-Tate prismatic crystals and Sen theory** — Hui Gao (2022-01, [2201.10136](https://arxiv.org/abs/2201.10136))  
  Hodge-Tate prismatic crystals classified by nilpotent Sen operator, core WCart structure
- **v-vector bundles on $p$-adic fields and Sen theory via the Hodge-Tate stack** — Johannes Anschütz; Ben Heuer; Arthur-César Le Bras (2022-11, [2211.08470](https://arxiv.org/abs/2211.08470))  
  Realizes Sen theory via vector bundles on Hodge-Tate locus of Cartier-Witt stack directly
- **Non-decomposability of the de Rham complex and non-semisimplicity of the Sen operator** — Alexander Petrov (2023-02, [2302.11389](https://arxiv.org/abs/2302.11389))  
  Non-semisimplicity of Sen operator constrains eigenvalue/positivity structure needed for signature

> **Repo tie-in:** `STATE_OF_THE_PROGRAM.md` already flags **Petrov's non-semisimplicity of the Sen operator** as the reason "the polarization must be built intrinsically, not eigenspace-by-eigenspace." *Non-decomposability of the de Rham complex and non-semisimplicity of the Sen operator* is the primary source for that constraint. The two Bhatt–Lurie foundational papers and the Hodge–Tate-stack Sen-theory papers are the construction-level references for the M4a-POSITIVITY target.

## B. Arithmetic Hodge-index & Arakelov positivity
*The theorem-side of M4: signature / positivity results on arithmetic surfaces. Direction 8 (Hodge index on the surface) and the Arakelov-face probes (#131/#132).*

- **The theta invariants and the volume function on arithmetic varieties** — Mounir Hajli (2022-02, [2202.09397](https://arxiv.org/abs/2202.09397))  
  Theta invariants and generalized Hodge index theorem on arithmetic varieties
- **Riemann-Roch for $\overline{\text{Spec}\mathbb Z}$** — Alain Connes; Caterina Consani (2022-05, [2205.01391](https://arxiv.org/abs/2205.01391))  
  Connes-Consani Riemann-Roch on Arakelov Spec(Z), cohomology/duality needed for signature
- **The arithmetic volume of hypersurfaces in toric varieties and Mahler measures** — Mounir Hajli (2022-06, [2206.14232](https://arxiv.org/abs/2206.14232))  
  Generalized Hodge index theorem for arithmetic toric hypersurfaces, model positivity result
- **Quasi-projective and formal-analytic arithmetic surfaces** — Jean-Benoît Bost; François Charles (2022-06, [2206.14242](https://arxiv.org/abs/2206.14242))  
  Bost-Charles formal-analytic arithmetic surfaces, Arakelov framework for Spec(Z)xSpec(Z)-type surfaces
- **Hilbert-Samuel formula and positivity over adelic curves** — Huayi Chen; Atsushi Moriwaki (2022-07, [2207.02033](https://arxiv.org/abs/2207.02033))  
  Arithmetic Hilbert-Samuel and positivity of adelic line bundles, Arakelov positivity toolkit
- **A local version of the arithmetic Hodge index theorem over quasiprojective varieties** — Marc Abboud (2025-03, [2503.14099](https://arxiv.org/abs/2503.14099))  
  Local arithmetic Hodge index theorem — direct analogue of needed intersection positivity
- **Numerical cohomology for arithmetic surfaces and applications** — Wei He (2025-12, [2512.01811](https://arxiv.org/abs/2512.01811))  
  Numerical cohomology and absolute arithmetic Riemann-Roch for arithmetic surfaces

> **Repo tie-in:** These are the closest existing analogues of the missing polarization. Your notes record that the Arakelov face "HAS a carrier AND a proven per-surface polarization (Faltings–Hriljac / Yuan–Zhang) but dies at the BASE (no Spec(Z) x Spec(Z))." The local arithmetic Hodge-index and adelic-curve positivity papers are exactly the per-surface theorems whose *product-surface* generalization is the open step.

## C. Connes–Consani / NCG / F_1 and Deninger dynamics
*The competing substrate and the spectral-realization program. Arch 1's 1D thread and the Connes–Consani square of Direction 8.*

- **Spectral Triples and Zeta-Cycles** — Alain Connes; Caterina Consani (2021-06, [2106.01715](https://arxiv.org/abs/2106.01715))  
  Connes-Consani zeta-cycles/spectral triples, explicit-formula quadratic form eigenvalue positivity
- **Hochschild homology, trace map and $ζ$-cycles** — Alain Connes; Caterina Consani (2022-07, [2207.10419](https://arxiv.org/abs/2207.10419))  
  Connes-Consani spectral realization of zeta zeros via Hochschild homology/sheaf cohomology
- **Knots, Primes and the adele class space** — Alain Connes; Caterina Consani (2024-01, [2401.08401](https://arxiv.org/abs/2401.08401))  
  Connes-Consani adele class space dynamical system, Deninger-style foliated flow analogue
- **Zeta Spectral Triples** — Alain Connes; Caterina Consani; Henri Moscovici (2025-11, [2511.22755](https://arxiv.org/abs/2511.22755))  
  Connes-Consani-Moscovici spectral realization strategy directly targeting RH proof
- **On the Absolute Geometry of $\operatorname{Spec}\mathbf{Z}$** — Alain Connes; Caterina Consani (2026-06, [2606.06604](https://arxiv.org/abs/2606.06604))  
  Connes-Consani absolute F1 arithmetic site/square, exact competing substrate for signature

> **Repo tie-in:** Two of these — *On the Absolute Geometry of Spec Z* (2026-06) and *Zeta Spectral Triples* (2025-11) — sit at or past the edge of your last `STATE_OF_THE_PROGRAM.md` update (2026-06-04) and may not be in your WATCH catch-net yet. Since the needle-map closed the soft-max route to a signature on the C–C square (2CC.4 / LEARNINGS #65), these are worth checking for whether the *newer* C–C machinery reopens a signed pairing.

---

## D. Status of your named WATCH-list papers

Your session-012 plan lists specific arXiv IDs to watch. Current metadata:

| arXiv | Title | Authors | Date |
|---|---|---|---|
| [2602.15941](https://arxiv.org/abs/2602.15941) | On the Jacobian of $overline{{{rm Spec},mathbb Z}}$ | Connes, Consani | 2026-02-17 |
| [2407.01304](https://arxiv.org/abs/2407.01304) | Heights of Ceresa and Gross-Schoen cycles | Gao, Zhang | 2024-07-01 |
| [2301.12392](https://arxiv.org/abs/2301.12392) | Prismatization over $mathbf{Z}$ | Gurney | 2023-01-29 |
| [2504.07005](https://arxiv.org/abs/2504.07005) | A stacky approach to prismatic crystals via $q$-prism c | Liu | 2025-04-09 |
| [1807.06400](https://arxiv.org/abs/1807.06400) | Dynamical systems for arithmetic schemes | Deninger | 2018-07-17 |

- **2602.15941** (Connes–Consani Jacobian) and **2407.01304** (Gao–Zhang, Ceresa / Gross–Schoen heights) are your two "does the follow-up cross into a signed pairing / self-product + Γ_S?" watch items.
- **2301.12392** (Drinfeld, *Prismatization over Z*) and **2504.07005** (stacky prismatic crystals) are the WCart-globality references your session-012 plan gated the relabel behind.
- **1807.06400** (Deninger, *Dynamical systems for arithmetic schemes*) is the dim-3 foliated-space object your foundational-object brief cites as the refutation of "the surface cannot exist."

## How to use this

1. The main map (`rh_literature_map.md`) remains the right artifact for tracking the *field* — where the Guth–Maynard-driven zero-density front and the RMT / moments machinery are moving. Context, not critical path.
2. **This supplement is your critical-path literature.** The Section-A prismatic / Sen papers and Section-B arithmetic-Hodge-index papers are the ones whose results could feed Direction 8 / the M4a-POSITIVITY target.
3. Candidate `reading_notes/` additions likely not yet present: the Sen non-semisimplicity paper (A), the local arithmetic Hodge-index and adelic-curve positivity papers (B), and the two 2025–2026 Connes items (C).

## Method & caveats
- Supplementary sweep: 9 Architecture-2-targeted arXiv queries + a 5-ID WATCH-list fetch, 2021-01-01 → 2026-07. 137 raw → 111 relevant → 108 new (not in the main map's 303). LLM curation (reasoning model) selected the 17 most relevant to the M4 signature front.
- **This is a relevance map, not a refereeing.** "Most relevant" means *could plausibly inform the signature question*, judged from abstracts — not that any paper supplies the missing object (none does; your docs are explicit it is unconstructed).
- Citation weighting still unavailable (OpenAlex key not configured).
- Full data: `rh_arch2_supplement.csv` (the 17) and `rh_full_corpus.csv` (the original 303).
