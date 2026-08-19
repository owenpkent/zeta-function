# References library (reading list)

> Curated reference library for the proof program. The PDFs themselves are
> copyrighted and **gitignored** (`*.pdf`); this index is tracked. Organized by
> role, mapped to the research directions in
> [`docs/03_research/research_directions/`](../docs/03_research/research_directions/)
> and the strategic snapshot [`STATE_OF_THE_PROGRAM.md`](../STATE_OF_THE_PROGRAM.md).
> Reading notes (as they are produced) live in
> [`docs/03_research/reading_notes/`](../docs/03_research/reading_notes/).
> **How to add a paper / process a PDF (file -> extract -> note -> index):**
> [`docs/03_research/reading_notes/PROCESSING_PDFS.md`](../docs/03_research/reading_notes/PROCESSING_PDFS.md).
>
> **Priority for the live front (Direction 4.6 → 8):** 02 (Deninger) and 03
> (foliated trace formulas) are the direct blueprint; 01 (prismatic) is the
> cohomology substrate; 06 (Hodge/intersection) is the signature step. Read in
> that order.

## 01 Prismatic cohomology (Direction 3 — the cohomology substrate)

| File | Reference | Role |
|---|---|---|
| `Bhatt-Scholze-2019-Prisms-and-Prismatic-Cohomology.pdf` | Bhatt & Scholze, *Prisms and prismatic cohomology*, Annals 2022 | The definitive source for the cohomology theory Direction 3/4 builds on. |
| `Bhatt-Lurie-2022-Absolute-Prismatic-Cohomology.pdf` | Bhatt & Lurie, *Absolute prismatic cohomology*, arXiv:2201.06120 | The "absolute" flavor — the one relevant to Spec(ℤ) rather than a fixed prime. |
| `Bhatt-Morrow-Scholze-Integral-p-adic-Hodge-Theory.pdf` | Bhatt–Morrow–Scholze, *Integral p-adic Hodge theory* (BMS1) | The BMS framework the direction docs cite (R5/Direction 3). |
| `Bhatt-Morrow-Scholze-THH-and-Integral-p-adic-Hodge-Theory.pdf` | Bhatt–Morrow–Scholze, *Topological Hochschild homology and integral p-adic Hodge theory* (BMS2) | The THH/filtration precursor. |

## 02 Deninger program (Direction 4 — the 4.6 blueprint)

| File | Reference | Role |
|---|---|---|
| `Deninger-Motivic-L-functions-and-Regularized-Determinants-I.pdf` | Deninger, *Motivic L-functions and regularized determinants* | ζ as a regularized determinant; the precise form of 4.6's `det_ζ(s − Θ)`. |
| `Deninger-Motivic-L-functions-and-Regularized-Determinants-II.pdf` | Deninger, *…II* | **Direct on target:** H¹ of `Spec ℤ ∪ {∞}` with an automorphism whose eigenvalues are the ζ zeros; a "proof" of RH assuming a Hodge-∗ operator (the Direction 8 signature step in Deninger's own words). |
| `Deninger-1998-ICM-...-Foliated-Spaces.pdf` | Deninger, ICM Berlin 1998 | The cohomology wishlist (what H* must satisfy); the program's manifesto. |
| `Deninger-2002-Number-Theory-and-Dynamical-Systems-on-Foliated-Spaces.pdf` | Deninger, 2002 | Post-ICM developments of the foliated-dynamical picture. |
| `Deninger-2005-Arithmetic-Geometry-and-Analysis-on-Foliated-Spaces.pdf` | Deninger, 2005 | The most readable survey of the analysis-on-foliated-spaces analogy. |

## 03 Foliated cohomology + trace formulas (Direction 4.3–4.6 — the analytic substrate)

| File | Reference | Role |
|---|---|---|
| `Moore-Schochet-Global-Analysis-on-Foliated-Spaces-2nd-ed.pdf` | Moore & Schochet (book) | Standard reference for leafwise cohomology, finiteness, duality (milestones 4.3–4.5). |
| `Alvarez-Lopez-Kordyukov-Leichtnam-2017-Trace-Formula-for-Foliated-Flows.pdf` | Álvarez López, Kordyukov, Leichtnam, 2017 | A genuine trace formula for foliated flows — the closest existing analogue of 4.6. |
| `Leichtnam-2006-Scaling-Group-Flow-and-Lefschetz-Trace-Formula-Laminated-Spaces.pdf` | Leichtnam, arXiv:math/0603576 | Lefschetz trace formula for laminated spaces with p-adic transversal, built explicitly for Deninger's ζ picture. |

## 04 NCG / Connes (the other half of the Morishita bridge)

| File | Reference | Role |
|---|---|---|
| `Connes-2026-RH-Past-Present-and-a-Letter-Through-Time.pdf` | Connes, arXiv:2602.04022 (2026) | The Feb-2026 survey + the "Letter to Riemann": extremize the truncated Weil form, Thm 6.1 gives on-line zeros per cutoff (primes ≤13 → first 50 zeros to 2.6e-55), RH = the unproven convergence; Shannon/Slepian bridge; prolate UV model. Notes: [Connes-2026-RH-Past-Present-Letter](../docs/03_research/reading_notes/Connes-2026-RH-Past-Present-Letter.md); assessment: [connes_2602_letter_to_riemann](../docs/03_research/connes_2602_letter_to_riemann.md). |
| `Connes-1998-Trace-Formula-in-NCG-and-Zeros-of-Riemann-Zeta.pdf` | Connes, Selecta 1999 | Spectral interpretation of the critical zeros; the NCG trace formula. |
| `Connes-Consani-2015-Geometry-of-the-Arithmetic-Site.pdf` | Connes & Consani, *Geometry of the Arithmetic Site* | The adèle-class-space geometry; the Connes side of the bridge (R3.5/3M context). |
| `Connes-1994-Noncommutative-Geometry.pdf` | Connes, *Noncommutative Geometry* (book) | Foliations, the trace, foundational NCG. |

## 05 Arithmetic topology (Morishita bridge background)

| File | Reference | Role |
|---|---|---|
| `Morishita-2009-Analogies-Knots-Primes-3Manifolds-Number-Rings.pdf` | Morishita, arXiv:0904.3399 | Expository knots↔primes; background for the bridge paper arXiv:2508.15971 (closed orbits ↔ primes, used in 2R). |
| `Li-Sia-2012-Knots-and-Primes-Harvard-Tutorial-Notes.pdf` | Li & Sia, Harvard tutorial 2012 | Accessible course notes on the Morishita book. |

## 06 Intersection theory / Hodge index (Direction 8 — the signature step)

| File | Reference | Role |
|---|---|---|
| `Hartshorne-Algebraic-Geometry-GTM52.pdf` | Hartshorne, *Algebraic Geometry* (GTM 52) | Ch. V: surfaces + intersection theory; the C × C signature in classical form (the 2G template). |
| `Voisin-Hodge-Theory-and-Complex-Algebraic-Geometry-I-frontmatter.pdf` | Voisin, *Hodge Theory and Complex Algebraic Geometry I* (front matter only) | Hodge index / Hodge–Riemann signature (the thing to lift). NOTE: this file is front matter/TOC only, not the full book. |
| `Adiprasito-Huh-Katz-2018-Hodge-Theory-for-Combinatorial-Geometries.pdf` | Adiprasito–Huh–Katz, Annals 2018 | The tropical Hodge index (Direction 8 attack angle 4.A). |

## 07 Elliptic-curve heights (single-surface computational; used by 2I/2L/2P)

| File | Reference | Role |
|---|---|---|
| `Cohen-1993-Course-in-Computational-Algebraic-Number-Theory-GTM138.pdf` | Cohen, GTM 138 | Authoritative local-height algorithm (Alg 7.5.6/7.5.7) used in 2P. |
| `Silverman-1994-Advanced-Topics-in-Arithmetic-of-Elliptic-Curves-GTM151.pdf` | Silverman, GTM 151 (ATAEC) | Néron local heights, the σ-function, archimedean theory (2I/2L). |
| `Silverman-1988-Computing-Heights-on-Elliptic-Curves-MathComp.pdf` | Silverman, Math. Comp. 1988 | The original Tate-series archimedean-height algorithm (2I). |
| `Silverman-1997-Computing-Canonical-Heights-with-Little-or-No-Factorization.pdf` | Silverman, Math. Comp. 1997 | Improved canonical-height computation. |
| `Cremona-Algorithms-for-Modular-Elliptic-Curves-Ch3.pdf` | Cremona, *Algorithms for Modular Elliptic Curves*, Ch. III | The §3.4 local-height conventions used in 2P. |

## 08 Misc

| File | Reference | Role |
|---|---|---|
| `Gerasimov-Lebedev-Oblezin-From-Archimedean-L-factors-to-Topological-Field-Theories.pdf` | Gerasimov, Lebedev, Oblezin | Archimedean L-factors as topological field theories; a lens on the archimedean place (A_arch / 2I). |

## 09 Quantum gravity and the primes (the 2026-08 sweep, LEARNINGS #176)

Pulled 2026-08-19 for [`local_quantum_gravity_and_primes.md`](../docs/03_research/local_quantum_gravity_and_primes.md).
Verdict of the sweep: this field reproduces the #113 pattern (ζ realized as a trace, no polarization
attached), and the structure it hands you for free (unitarity) is provably RH-blind.

| File | Reference | Role |
|---|---|---|
| `arxiv_2505.03068.pdf` | Godet, *Möbius randomness in the Hartle-Hawking state*, arXiv:2505.03068 | **The sharpest live candidate.** WDW operator = Casimir on `L²(SL(d,ℤ)\h_d)`; Hartle-Hawking state as a sum over the ζ zeros; primes via primitivity (mechanism 5). Uses RH as input. |
| `arxiv_2405.09833.pdf` | Godet, *Quantum cosmology as automorphic dynamics*, arXiv:2405.09833 | The 3d predecessor: Artin's billiard, Maloney-Witten, the Möbius average. |
| `arxiv_2406.01828.pdf` | LeClair, *Spectral Flow for the Riemann zeros*, arXiv:2406.01828 | S-matrix from the Euler product. **Runs the D-H test itself and passes**; independently reaches this repo's conservation law. Gap: the Hamiltonian is never built. |
| `arxiv_2004.09523.pdf` | Betzios, Gaddam, Papadoulaki, *Black holes, quantum chaos, and the Riemann hypothesis*, SciPost Phys. Core 4, 032 | Gauging CPT discretizes the dilation spectrum; Berry-Keating with a black-hole reading. Existing BK verdict applies. |
| `arxiv_1510.05818.pdf` | Kim, *Arithmetic Chern-Simons Theory I*, arXiv:1510.05818 | **The named gap.** A Dijkgraaf-Witten TQFT on Galois representations over `Spec(O_K)`; the most literal "quantum gravity on Spec(ℤ)". No contact with the zeros yet. Cross-ref 05. |
| `arxiv_1609.03012.pdf` | Kim et al., *Arithmetic Chern-Simons Theory II*, arXiv:1609.03012 | Decomposition formula and worked computations. |
| `arxiv_1705.04758.pdf` | Dragovich, Khrennikov, Kozyrev, Volovich, Zelenov, *p-Adic Mathematical Physics: The First 30 Years* | The Volovich-hypothesis program: non-archimedean spacetime at the Planck scale. Background for "local = local field". |
| `arxiv_0712.0155.pdf` | Maloney, Witten, *Quantum Gravity Partition Functions in Three Dimensions* | The `SL(2,ℤ)` sum Godet analytically continues. |
| `arxiv_1101.3116.pdf` | Schumayer, Hutchinson, *Physics of the Riemann Hypothesis* | Survey of the whole physics-of-RH literature; useful map, no new leverage. |
| `arxiv_0802.4077.pdf` | Agullo, Barbero, Diaz-Polo, Fernandez-Borja, Villaseñor, *Black hole state counting in LQG: a number theoretical approach* | The one genuine LQG-meets-number-theory result. Combinatorial, not zeta-facing. |
| `arxiv_1507.05818.pdf` | Connes, Consani, *The Scaling Site* | Already covered in 04; filed here for the sweep's completeness. |
| `arxiv_2205.01391.pdf` | Connes, Consani, *Riemann-Roch for `Spec ℤ`* | As above. |
| `arxiv_1509.05576.pdf` | Connes, *An essay on the Riemann Hypothesis* | As above. |

