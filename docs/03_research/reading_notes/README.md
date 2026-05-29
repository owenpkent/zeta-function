# Reading notes — reference library read-through

> Notes from going through the [reference library](../../../references/README.md)
> (26 sources), each mapping a source to the project's findings (2G, 2Q, 2R, 2K, 2I,
> 3M) and milestones (Direction 4.6 trace formula, Direction 8 signature). The PDFs
> are gitignored; these notes are tracked. **Coverage: all 26 sources noted.**

## Top findings from the read-through

The literature **independently confirms the session-005 reduction and locates the
gap identically** to the in-house work, and it surfaces concrete candidate objects:

1. **The strongest concrete candidate for the missing object: Bhatt-Lurie's
   Cartier-Witt stack `WCart`.** Absolute prismatic cohomology is "de Rham cohomology
   relative to the field with one element" (a candidate for 2K's missing `F_1` base
   point, with the right `+1` dimension count), it carries a **global Frobenius `F`**
   (candidate assembly of 2Q's place-dependent `Gamma_S`), and a **Sen operator `Θ`**
   (a genuine flow generator, the closest existing object to Deninger's eigenvalue
   generator / 2R / Direction 4.6). This is the single most actionable thread.
2. **Connes-Consani 2015 already builds the SQUARE.** `N^2`-hat (`Z_min ⊗_B Z_min`,
   Newton polygons in `Z×Z`) with one-parameter **Frobenius correspondences `Ψ(λ)`**,
   `Ψ(λ)Ψ(λ') = Ψ(λλ')`: a concrete product surface + `Gamma_S` over the
   characteristic-1 base, exactly the 2K / Direction-8 target. The gap is isolated and
   sharp: the characteristic-1 operations are idempotent, so **there is no signed
   intersection pairing / Hodge index yet** (Direction 8, not Direction 4.6).
3. **A Hodge-index signature can exist with NO underlying variety** (Adiprasito-Huh-
   Katz): the matroid Chow ring satisfies Hodge-Riemann with no projective variety
   beneath. This is Direction 8 attack angle 4.A, and a precedent against the
   "no-variety" obstruction for `Spec(Z)^2`.
4. **The signature is the content, not the trace formula.** Deninger's RH mechanism is
   `Θ = 1/2 + A` (`A` skew), forced by a **Hodge-`*` positivity** input; Connes 1998
   shows trace-formula positivity `⟺` RH (the K1 wall, R3.5/3M circularity); the
   AHK/Babaee-Huh "Poincaré duality + Hard Lefschetz but NOT Hodge-Riemann" example is
   the tropical analogue of the D-H discipline. Consistent across all four corners:
   **2R-style spectrum/trace is necessary but the Direction-8 signature is the open,
   load-bearing step.**
5. **`R*_+` as continuous Frobenius at the archimedean place** has three independent
   attestations (Leichtnam type III_{1/q}, Connes-1994 flow of weights, Connes-Consani
   characteristic-1), grounding 2I and 2Q's "what plays the role of `q`" question.

## Notes by folder

### 01 Prismatic cohomology (Direction 3 substrate)
| Note | Headline |
|---|---|
| [Bhatt-Scholze-2019-Prisms](Bhatt-Scholze-2019-Prisms.md) | The definitive one-prime prismatic theory; Frobenius as the delta-ring structure; the cohomology substrate for Leichtnam's p-adic transversal. |
| [Bhatt-Lurie-2022-Absolute-Prismatic](Bhatt-Lurie-2022-Absolute-Prismatic.md) | The absolute (all-primes) theory: WCart = "de Rham relative to F_1", global Frobenius F, Sen operator Theta. The standout candidate for the F_1 base / Gamma_S / Deninger generator. |
| [BMS-Integral-p-adic-Hodge](BMS-Integral-p-adic-Hodge.md) | The A_inf single-place model; Breuil-Kisin-Fargues modules = local model of what Gamma_S induces. |
| [BMS-THH-Integral-p-adic-Hodge](BMS-THH-Integral-p-adic-Hodge.md) | Frobenius traced to the cyclotomic Frobenius of THH; the canonical Nygaard/motivic filtration (the grading a det(s-Theta) or Hodge-star would live over). |

### 02 Deninger program (Direction 4.6 blueprint)
| Note | Headline |
|---|---|
| [Deninger-1998-ICM-Analogies-Foliated](Deninger-1998-ICM-Analogies-Foliated.md) | The founding manifesto: Direction 4.6 (det_inf / Lefschetz) and Direction 8 (Hodge-* signature) as two halves of one cohomology; RH via Theta = 1/2 + A. |
| [Deninger-I-regularized-determinants](Deninger-I-regularized-determinants.md) | Rigorous det_inf formalism; local cohomology via Riemann-Hilbert (Sp Theta = e^{-1} Sp F); the functional-equation sign = APS eta-invariant (a trace-side signature). |
| [Deninger-II-regularized-determinants](Deninger-II-regularized-determinants.md) | H^1 with Theta-eigenvalues = zeta zeros + det (3.8) ARE the 4.6 target; sec 3.7 states the 2K product-surface gap verbatim ("over spec Q, not an absolute base point"). |
| [Deninger-2002-NT-Dynamical-Foliated](Deninger-2002-NT-Dynamical-Foliated.md) | The first real theorem (ALK trace formula, A_phi trace class); Re = alpha/2; why manifolds force alpha=0 and forbid fixed points = the 2K gap in flow language. |
| [Deninger-2005-Arithmetic-Geometry-Foliated](Deninger-2005-Arithmetic-Geometry-Foliated.md) | Best single citation: every Euler factor (finite + real-inf + complex-inf) from one det_inf formula (Prop 3.1); the archimedean place as the p=inf stationary point (2I). |

### 03 Foliated cohomology + trace formulas (Direction 4.3-4.6)
| Note | Headline |
|---|---|
| [Leichtnam-2006-Lefschetz-laminated-spaces](Leichtnam-2006-Lefschetz-laminated-spaces.md) | A conditional Lefschetz trace formula + Re=1/2 for foliated laminated spaces; the p-adic transversal Z_p^m is the prismatic x foliation bridge (makes the trace class). Function-field g=1 only. |
| [Alvarez-Lopez-Kordyukov-Leichtnam-2017-Trace-Formula-Foliated-Flows](Alvarez-Lopez-Kordyukov-Leichtnam-2017-Trace-Formula-Foliated-Flows.md) | The general foliated-flow trace formula behind Leichtnam 2006: A_f smoothing via leafwise-Hodge projection; the fixed-point (archimedean) case is a work-in-progress strategy. |
| [Moore-Schochet-Global-Analysis-Foliated-Spaces](Moore-Schochet-Global-Analysis-Foliated-Spaces.md) | Role-note: standard reference for leafwise/tangential cohomology, finiteness, transverse measures (the trace), the measured-foliation index theorem (Direction 4.3-4.6). |

### 04 NCG / Connes (the other half of the Morishita bridge)
| Note | Headline |
|---|---|
| [Connes-1998-Trace-Formula-NCG-Zeros](Connes-1998-Trace-Formula-NCG-Zeros.md) | RH reduced to a trace formula on the adele class space; Weil dictionary's bottom rows = Directions 4.6 + 8; trace-formula positivity <=> RH pins the K1 wall. |
| [Connes-Consani-2015-Geometry-Arithmetic-Site](Connes-Consani-2015-Geometry-Arithmetic-Site.md) | Builds the square N^2-hat with Frobenius correspondences Psi(lambda): a concrete product surface + Gamma_S over char-1, but idempotent ops => no signed pairing yet (the Direction-8 gap, isolated). |
| [Connes-1994-Noncommutative-Geometry](Connes-1994-Noncommutative-Geometry.md) | Role-note: foliations + Ruelle-Sullivan current (I.5), flow of weights = why R*_+ is canonical Frobenius (V.8/11), transverse fundamental class = where an NCG Lefschetz pairing / K1 wall lives (III.7). |

### 05 Arithmetic topology (Morishita bridge background)
| Note | Headline |
|---|---|
| [Morishita-2009-Analogies-Knots-Primes](Morishita-2009-Analogies-Knots-Primes.md) | Primes = knots, Spec(Z) = 3-manifold; the Legendre symbol as a cup-product intersection form, quadratic reciprocity = its symmetry (the 3-manifold precursor of the Direction-8 signature thesis). |
| [Li-Sia-2012-Knots-and-Primes-Notes](Li-Sia-2012-Knots-and-Primes-Notes.md) | The clean undergraduate version; Spec(Z) U {infinity} = S^3; reciprocity as the simplest signature datum. |

### 06 Intersection theory / Hodge index (Direction 8 signature)
| Note | Headline |
|---|---|
| [Adiprasito-Huh-Katz-2018-Hodge-Combinatorial](Adiprasito-Huh-Katz-2018-Hodge-Combinatorial.md) | Attack angle 4.A: a Hodge-Riemann signature on a matroid Chow ring with NO underlying variety. Precedent against the no-variety obstruction; the signature (not Lefschetz) is the content. |
| [Hartshorne-Algebraic-Geometry](Hartshorne-Algebraic-Geometry.md) | Role-note: Ch V.1 (the symmetric intersection pairing + Hodge index, signature (1, rho-1)); Ex V.1.4.3 (P1xP1) = the baby C x C / 2G template; App C = the function-field RH being lifted. |
| [Voisin-Hodge-Theory-I](Voisin-Hodge-Theory-I.md) | Role-note (FRONT MATTER ONLY in the repo PDF): the relevant sections are 6.3 (Hodge index), 6.1-6.2 (Lefschetz decomposition), 7.1-7.2 (polarisation / Hodge-Riemann), 11.3/12.2 (correspondences = where Gamma_S lives classically). |

### 07 Elliptic-curve heights (single-surface computational; 2I/2L/2O/2P)
| Note | Headline |
|---|---|
| [Cohen-1993-Computational-ANT-GTM138](Cohen-1993-Computational-ANT-GTM138.md) | Role-note: Alg 7.5.6 (finite case-split) + Alg 7.5.7 (theta/AGM archimedean series), implemented verbatim in 2P; regulator positive-definiteness framing. |
| [Silverman-1994-Advanced-Topics-GTM151](Silverman-1994-Advanced-Topics-GTM151.md) | Role-note: Neron local heights (VI.1-VI.4), the sigma-function archimedean formula (lambda_inf of 2I, Delta^{1/12} of 2L); the quasi-parallelogram law = the A_arch bilinear form. |
| [Silverman-1988-Computing-Heights](Silverman-1988-Computing-Heights.md) | The original Tate switch-series (the beta-switch in 2P), the finite case-split, and the factor-of-2 normalization Remark that 2I hit empirically. |
| [Silverman-1997-Computing-Canonical-Heights](Silverman-1997-Computing-Canonical-Heights.md) | The decomposition formula; names Cohen 7.5.7 as the fast archimedean route; factorization-free method. |
| [Cremona-Algorithms-Modular-Elliptic-Curves-Ch3](Cremona-Algorithms-Modular-Elliptic-Curves-Ch3.md) | Prop 3.4.1 + finite-prime pseudocode (transcribed into 2P); the "double those in [Silverman 1988]" note that settles the factor-of-2. |

### 08 Misc
| Note | Headline |
|---|---|
| [Gerasimov-Lebedev-Oblezin-Archimedean-L-factors-TFT](Gerasimov-Lebedev-Oblezin-Archimedean-L-factors-TFT.md) | Archimedean L-factor as a topological field theory partition function; the q=0 (Frobenius trace) to q->1 (Gamma-factor) deformation, a lens on the A_arch place (2I) and 2Q's two-clock question. |

## Method note

The four highest-priority sources (Deninger I/II, Leichtnam 2006) were read in the main
session; the remaining 23 were read in parallel by subagents, each given this project
context and the note format, then integrated here. Depths are stated honestly per note
(papers: intro + main results; large textbooks: TOC + relevant chapters as role-notes).
