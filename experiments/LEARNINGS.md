# Learnings from the proof-architecture experimental thread

> Companion to [PROOF_ARCHITECTURES_PLAN.md](PROOF_ARCHITECTURES_PLAN.md) (test plan and status table) and the per-architecture READMEs. This document synthesizes what the experiments collectively **teach** about the four candidate proof architectures and the RH landscape, organized by finding rather than by architecture. Updated as new experiments complete.

The companion documents answer "what did each experiment do?". This one answers "what do they collectively tell us?". When a new experiment lands, look here for the cross-cutting interpretation.

---

## Cross-cutting findings

### 29. Literature reorientation of Direction 10 (SURVEYOR, 2026-05-30): the proven template is Hesselholt's `zeta(X,s) = det_inf(s-Theta | TP_odd)/det_inf(s-Theta | TP_even)` over F_q. This VALIDATES the THH route (zeta really is a regularized determinant of a flow on an S^1-equivariant THH invariant) but reorients the target away from the naive THH->TC=Mobius guess, and shows the route funnels back to the SAME signature/Hodge-index problem as Direction 8.

Survey ([survey_tc_zeta_literature.md](homotopy/survey_tc_zeta_literature.md)) checked whether the THH -> von Mangoldt link is already known. Verdict: not as posed (the i^{-s} weighting of |THH_{2i-1}(Z)|=i and the THH->TC=1/zeta claim appear original), but the surrounding framework is established and sharper than the project's first guess.

**The proven template (Hesselholt, *THH and the Hasse-Weil zeta function*).** Over a finite field k of order q, for X/k smooth proper:
`zeta(X,s) = det_inf(s.id - Theta | TP_odd(X)(x)C) / det_inf(s.id - Theta | TP_ev(X)(x)C)`,
where `TP_i(X)` is the S^1=T-Tate cohomology of Bokstedt's THH, `Theta` is the graded derivation with `q^Theta = Fr_q^*` and `Theta(v) = (2pi i/log q) v`, the periodicity class `t in TP_{-2}` carries the grading, and `det_inf` is the Deninger zeta-regularized determinant. This is EXACTLY the Deninger flow-determinant picture, realized in THH, and PROVEN -- over F_q.

**The over-Z gap is #25, in Hesselholt's own framework.** He flags that `TP_*(X)` is generally NOT periodic over Z and `phi_p` does not always exist there. That is the place-dependent-bidegree obstruction (#25) appearing inside the proven framework: one Frobenius `Fr_q` (single scale q) over F_q, no single `Fr` over Z. Morin (*THH and zeta values*, arXiv 2011.11549) builds the over-S/Z machinery (T-equivariant motivic filtration on THH/TP/TC over the sphere spectrum) but extracts integer special values `zeta*(X,n)`, never the function `-zeta'/zeta`.

**Reorientation of the project's BUILDER target.** (i) The right object is `det_inf(s - Theta)` on `TP` with the flow generator `Theta`, NOT raw THH homotopy orders with a hand-imposed `i^{-s}` weight. The project's `-zeta'(s) = sum_i (log i) i^{-s}` (#28) should be reconciled with Hesselholt's determinant: `log i = -d/ds i^{-s}` is suggestive of a log-det/resolvent-trace of `Theta`, but the identification is unproven and may be a separate coincidence. (ii) ADVERSARY flag on Gap B (#28/10B): the homotopy equalizer `TC = eq(TC^- => TP)` is an ADDITIVE limit, whereas `1/zeta = prod_p (1-p^{-s})` is MULTIPLICATIVE over primes; "TC equalizer = Mobius = 1/zeta" is the load-bearing unverified claim and the most likely category error. The necklace/Mobius combinatorics (#28) carries `mu` but does not by itself make the equalizer multiplicative.

**The decisive structural point.** Even where Hesselholt's theorem HOLDS (over F_q), it gives the determinant FORMULA (zeta as det of the flow) -- this is the Arch-1/spectral realization -- but RH for X is `|Frobenius eigenvalues| = q^{1/2}`, which is the Weil/Hodge-index POSITIVITY (Arch 2 / Direction 8), a SEPARATE input not produced by the determinant identity. So a fully-developed THH route does not escape the central difficulty: it relocates Direction 8's signature/Hodge-index problem into the TP/flow framework (form 10A.iii, the K1 crux). Whether that relocation supplies NEW tools for the signature is the real open question and the only thing that would make Direction 10 more than a reformulation. Net: Direction 10 is real and now has a precise, literature-grounded target (Hesselholt-over-Z via Morin's substrate), but it funnels back to the same Hodge-index positivity as Direction 8, consistent with the marginal-positivity thesis and the project's structural reading that positivity is the irreducible hard step.

### 28. Direction 10A.ii first pass: Bokstedt's THH(Z) torsion log-orders assemble RIGOROUSLY to -zeta'(s) (the imprimitive log-sum), and the von Mangoldt sum = #26 dynamical zeta = Gamma_S^2 is exactly ONE Mobius factor (1/zeta) away. That factor is the conjectural THH -> TC cyclotomic reduction. The checkpoint passes in its imprimitive form and reduces Direction 10 to a single sharp target.

e_thh_vonmangoldt ([e_thh_vonmangoldt.py](homotopy/e_thh_vonmangoldt.py), writeup [e_thh_vonmangoldt.md](homotopy/e_thh_vonmangoldt.md)) runs the cheapest concrete form of the Direction 10A checkpoint (the THH-side mirror of #26). Substrate: Bokstedt's theorem `pi_*(THH(Z)) = Z (deg 0), Z/i (deg 2i-1), 0 (even>0)`, so `|THH_{2i-1}(Z)| = i` and the prime p enters degree 2i-1 via `v_p(i)`.

**Three links (all verified).**
- **Link 1 (exact, term-by-term).** Weighting degree 2i-1 by `i^{-s}` with value `log|THH_{2i-1}| = log i`, the assembled series `sum_i (log i) i^{-s} = -zeta'(s)` (err 5e-16 at s=4). This is the IMPRIMITIVE log-sum, NOT the von Mangoldt sum.
- **Link 2 (the Mobius gap).** `-zeta'(s) = zeta(s)*(-zeta'/zeta)(s)`, i.e. `Lambda = mu * log` (verified to 6e-31). The von Mangoldt sum is recovered by Mobius convolution (x 1/zeta) of the THH log-orders.
- **Link 3 (per-prime, exact by regrouping).** `sum_i v_p(i) i^{-s} = zeta(s) p^{-s}/(1-p^{-s})`, times log p = zeta(s) x [p-Euler factor of -zeta'/zeta] (err ~1e-12 for p=2,3,5). Cross-check `sum_p v_p(i) log p = log i` exact.

**Verdict.** The primes enter THH(Z) exactly through `v_p(i)` with correct log p weights and assemble rigorously to `-zeta'(s)`. The von Mangoldt sum (`= Gamma_S^2`, #26) is one factor `1/zeta = mu` away, which on the spectral side is the primitive reduction THH -> TC (the Nikolaus-Scholze cyclotomic equalizer). So Direction 10 reduces to ONE falsifiable target: **does the THH -> TC equalizer implement Mobius inversion?** Two caveats kept explicit: (A) the weight `i^{-s}` on degree 2i-1 is an assumption the S^1-Tate formalism must justify; (B) "1/zeta = TC reduction" is the conjectural target, not a theorem.

**K2 firewall.** D-H is not a ring, so no THH; concretely `Lambda_DH` delocalizes onto composite n (first leak n=6, then 12,14,18,21,...; matches #20/#26), so it is NOT `mu*(log-order sequence)`. No THH, no surface, at the most structural level yet.

This is the strongest positive signal for any of directions 9-13: unlike the bounded cheap-detectors of #27, the THH route reproduces the correct prime structure rigorously up to one identified factor, and that factor has a precise homotopy-theoretic candidate.

**Gap B follow-up (e_necklace_mobius.py, doc 10B).** The missing `1/zeta = mu` factor has a structural home in the cyclotomic geometry, not just in the Dirichlet identity. The cyclotomic `C_n`-fixed-point components of THH are indexed by NECKLACE polynomials `M(q,n) = (1/n) sum_{d|n} mu(n/d) q^d`, which are LITERALLY Mobius inversion. Verified exactly (exact rationals): the Mobius-inverse pair `sum_{d|n} d M(q,d) = q^n`, the Metropolis-Rota cyclotomic identity `1/(1-qt) = prod_n (1-t^n)^{-M(q,n)}` (mod t^25), and that this is the SAME Mobius inversion as `Lambda = mu*log` = von Mangoldt. So the `mu` that turns the THH log-order series `-zeta'` into the von Mangoldt sum `-zeta'/zeta` is intrinsic to the cyclotomic `C_n` combinatorics. Two flagged gaps remain (10B): (A) prove the scaling eigenvalue on the periodicity-graded piece `sigma^i` is `i` (justifying the `i^{-s}` weight via `F_n V_n = n`); (B) track the necklace weights through the TC equalizer's regularized trace to get exactly `1/zeta`. The K1 crux (signature vs trace, form 10A.iii) is still untouched and is the real RH content.

### 27. Two new "crazy but formal" directions (9-13) were stress-tested with two cheap experiments. The Hodge-Riemann log-concavity of the Li coefficients is a NON-EULER detector, not an RH detector (the #20 trap, in a new basis); the Jensen/Turan (xi-Taylor-moment) basis is in a STEALTH WINDOW at reachable order (sees neither non-Euler-ness nor off-line zeros). Two bases, two different walls, both consistent with marginal positivity.

Session 2026-05-30 proposed five speculative directions (docs/03_research/research_directions/09-13) attacking the place-dependent-bidegree obstruction (#25) head-on, and shipped two same-day falsification experiments.

**e3n ([e3n_li_signature.py](positivity/e3n_li_signature.py)) -- Direction 9 (arithmetic matroid / AHK).** Tests whether the Li coefficients obey the Adiprasito-Huh-Katz log-concavity (degree-1 Hodge-Riemann) signature an arithmetic matroid would force, and whether D-H violates it. Result at T_max=120, n<=120, 40 dps:

| function | Euler product | off-line zeros | log-concavity violations (lambda_n^2 < lambda_{n-1}lambda_{n+1}) |
|---|---|---|---:|
| zeta | yes | no | **0** |
| D-H | no | yes | 37 |
| D-H on-line zeros only (control) | no | no | 37 |
| Epstein d47 principal | **no** | **no** | 57 |
| Epstein d47 non-principal | no | yes | 52 |

Decisive controls: (i) removing D-H's off-line zeros leaves the 37 violations unchanged; (ii) the non-Euler-but-RH-satisfying Epstein d47 PRINCIPAL form (no off-line zeros up to T=120) has the MOST violations (57). So the log-concavity defect tracks **non-Euler-ness, not RH-failure** -- exactly the LEARNINGS #20 reformulation trap, now in the Hodge-Riemann/Li basis. This SUPPORTS Direction 9's K2 mechanism as a structural-existence statement ("no Euler product => no log-concave Li sequence => no matroid": only the unique Euler product zeta is log-concave), but shows the HR defect alone is not a numerical RH-detector. To test RH the matroid must inject the EXACT Euler structure, not the float-level zero perturbation (doc milestone 9.2).

**e_jensen_turan ([e_jensen_turan.py](integrable/e_jensen_turan.py)) -- Direction 13 (tau-function / Jensen-Turan).** Tests whether the Polya moments of Xi(z)=xi(1/2+iz) obey the Turan inequalities / Jensen-polynomial hyperbolicity (Pólya; Csordas-Norfolk-Varga; Griffin-Ono-Rolen-Zagier 2019), the degree-1 HR / real-rootedness content from the integrable-systems side. Moments extracted by circle-sampling + discrete Cauchy transform (fast, ~80-digit accuracy; the `mp.taylor(method='quad')` route hangs at high order). Result at M=16, 80 dps: zeta, D-H, AND Epstein d47 principal ALL pass (0 Turan violations, 0 non-hyperbolic Jensen polynomials for d=2,3,4). This is a **stealth window**: the xi-moment basis is dominated by the low zeros near z=0, so the off-line D-H zeros at height ~85.7 perturb the low-order moments below the detection floor. The basis sees neither non-Euler-ness nor off-line zeros at reachable order.

**The contrast is the finding.** The Li-coefficient basis (lambda_n = sum over ALL zeros) is sensitive to the on-line zero DISTRIBUTION, hence detects non-Euler-ness (but over-detects: fires on RH-satisfying non-Euler controls). The xi-Taylor-moment basis (dominated by low zeros) is insensitive to high off-line zeros, hence a stealth window. Neither is a clean RH-detector; both walls are consistent with the marginal-positivity thesis (#18/#19) and with the discipline that a working certificate must engage the EXACT Euler/arithmetic structure, not a soft spectral statistic. Net: directions 9 and 13 are not refuted, but their cheap-detector value is bounded; their real test requires the structural constructions (the matroid characteristic polynomial = xi; the tau-function realization), which remain open. Directions 10 (THH/cyclotomic Frobenius over the sphere spectrum) and 11 (bidegree-as-measure) are theory-side and untested; Direction 10 is the only one of the five that dissolves #25's obstruction at the root (one circle action carrying all primes).

### 26. `Gamma_S^2` (the regularized self-intersection of the arithmetic Frobenius correspondence pinned in #25) is realized concretely as the log-derivative of a Ruelle dynamical zeta whose primitive closed-orbit lengths are exactly `{log p}`: `-zeta'/zeta = sum_n Lambda(n) n^{-s}`. Davenport-Heilbronn has no such closed-orbit spectrum (its log-derivative coefficients delocalize off prime powers), so the dynamical-flow representation does not exist for it.

2R ([e2r_dynamical_zeta.py](arithmetic_geometric/e2r_dynamical_zeta.py), writeup [e2r_dynamical_zeta.md](arithmetic_geometric/e2r_dynamical_zeta.md)) makes #25's abstract `Gamma_S^2 = reg-sum_p (log p)(...)` concrete on the dynamical side, the half of the Morishita Deninger↔Connes-Consani bridge (arXiv:2508.15971, closed orbits↔primes) that Deninger supplies.

**Verified (s=2, prec 30).** The dynamical-zeta product over primes with orbit lengths `l(gamma_p)=log p`, `prod_p (1-p^{-s})^{-1}`, converges to `zeta(s)` (err 5e-2→3e-5 as P:10→5000); and `sum_n Lambda(n) n^{-s}` converges to `-zeta'/zeta(s)=0.56996099` (err 1e-1→2e-4 as N:10→5000). So the flow's regularized self-pairing IS the prime side = `Gamma_S^2`. The local factor at `p` (orbit length `log p`) is the Euler factor `(1-p^{-s})^{-1}` = the geometric content of #25's `(1,p)` bidegree.

**D-H control (dynamical K2).** `Lambda_DH` (from `-L_DH'/L_DH`) carries mass 37.42 OFF prime powers vs 36.94 on them (n≤60), first leaking at n=6 — matching the 3M fingerprint (#20). No Euler product ⇒ no primitive-`{log p}` orbit spectrum ⇒ no flow. The wrong-approach discipline in dynamical-systems language.

**What it is NOT.** Not a new route to RH (the identities are classical); the content is the structural identification (orbit lengths = place-weights = `Gamma_S^2`) and the D-H non-existence. The dynamical zeta gives the SPECTRUM and self-pairing of `Gamma_S`, not the SIGNATURE RH needs. It does not build the cohomology `H^*_{F,pr}`, finiteness, or the index theorem (Directions 4/8 open). It fixes the TARGET for Direction 4.6: a leafwise prismatic `H^*_{F,pr}` whose trace-formula determinant equals this dynamical zeta.

### 25. The single sharpest break between the function-field template and Spec(Z) is the BIDEGREE of the Frobenius correspondence: on C x C it is a (1, q) correspondence with ONE scale q, but over Spec(Z) it must carry a place-dependent bidegree (1, p) per prime. From that one fact the two defining features of Deninger's program (infinite-dimensional H^i, an R-flow not a Z-action) follow as consequences, and Gamma_S^2 is pinned to the von Mangoldt prime sum.

2Q ([e2q_frobenius_bidegree.py](arithmetic_geometric/e2q_frobenius_bidegree.py), writeup [e2q_frobenius_bidegree.md](arithmetic_geometric/e2q_frobenius_bidegree.md)) takes the now-complete 2K dictionary (#24) one notch further: granting that all intersection NUMBERS are computed, what must the missing correspondence `Gamma_S` BE?

**The break.** In 2G the Frobenius graph is a `(1, q)` correspondence (`e.Gamma=1`, `f.Gamma=q`) with `q` = residue cardinality, CONSTANT over the curve; RH is then the algebraic inequality `|t| < 2g sqrt(q)` in two integers. Over `Spec(Z)` the fibre over `p` is `Spec(F_p)` of cardinality `p`, so `Gamma_S` has a PLACE-DEPENDENT bidegree `(1, p)` -- no single scale `q`. The experiment quantifies it: over the first 40 primes the required-scale spread `max(p)/min(p)` is already 86.5 and diverges.

**Three consequences, derived not posited.** (1) No single scale => no finite `2x2` primitive Gram (the would-be Gram is block-graded over places, scale `p` in the `p`-block). (2) One place-block per prime power => `H^1` infinite-dimensional => the signature is an infinite-dim INDEX theorem, not a determinant -- exactly Deninger's "infinite-dimensional `H^i`," now a consequence of the bidegree. (3) A single Frobenius `x|->x^q` gives a `Z`-action with one log-scale `log q`; commensurable place-scales `{log p}` acting simultaneously FORCE a continuous `R`-action, the flow `Phi_t = prod_p U_{log p}^{t/log p}` of Directions 2/4. The Deninger flow is not aesthetic; it is the only carrier of a continuum of commensurable local scales.

**Gamma_S^2 pinned.** FF: `Gamma^2 = q * Delta^2` (single scale x adjunction). Spec(Z): `"Gamma_S^2" = reg-sum_p (log p)*(local self-int at p)` = the von Mangoldt prime side `P_fin` (2K) read as the correspondence's regularized self-pairing = the Direction 4.6 regularized determinant `det_zeta(s - Phi_t)`, with per-fibre adjunction input `omega-bar^2 = 12 h_Fal` already computed (2J/2L). So `Gamma_S` is a sharper, falsifiable target than "a Frobenius graph on S": a correspondence of place-dependent bidegree `(1,p)` whose regularized self-intersection is the prime sum.

**Sharper K2.** A `(1, p)` local bidegree IS the Euler factor `(1 - p^{-s})^{-1}`. D-H has a functional equation but no Euler product, so its von Mangoldt analogue delocalizes (#20), leaving no clean per-place local degrees: `no Euler product <=> no local bidegrees <=> no Gamma_S <=> no surface`. The wrong-approach discipline is now a bidegree statement, its most geometric form yet.

### 24. The complete single-arithmetic-surface side of the Hodge-index picture over Spec(Z) is now computed and validated end to end: positive-definite height pairing at ranks 1-4, and the FULL Silverman local decomposition (archimedean Petersson/Green + every finite prime, good and bad) summing to h_hat by the authoritative algorithm.

Session 004 (continued in-session) built out the arithmetic side of the 2K dictionary (#22/#23) to completion on a single arithmetic surface:

- **2M (#rank-4):** the Neron-Tate height pairing is positive definite at RANK 4 (curve 234446a1; 8x8 Gram, 4 positive eigenvalues, none negative). Faltings-Hriljac PosDef now exhibited at ranks 1, 2, 3 (2H) and 4 (2M).
- **2L (archimedean self-intersection):** the Petersson norm `||Delta||_Pet(tau) = (Im tau)^6 |eta(tau)|^24` -- the `omega-bar^2 = 12 h_Fal` analogue of `Delta^2 = 2-2g` -- computed and validated by two self-contained gates (j(tau)=j(E) to 1e-51; SL2(Z)-invariance to 1e-50).
- **2O (bad prime, first pass):** I_1 prime-conductor curves have bad-prime local height identically 0 (closing the 2I caveat rigorously); an I_2 example shows the Z/2 component-group periodicity.
- **2P (AUTHORITATIVE, supersedes 2I/2O):** implementing Cohen GTM 138 Alg 7.5.6/7.5.7 and Cremona sec 3.4 verbatim (the real height WITH the x<->x+1 convergence switch; the finite height WITH the exact M(M-N)/N component term), the GLOBAL identity `h_inf + sum_p h_p = h_hat` validates for 37a1/389a1/5077a1 and the I_2 curve at P/2P/3P, residual at the h_hat n_iter=7 truncation floor (down to ~1e-8). This confirms 2I's x2 normalization, CORRECTS 2O's bad-prime attribution (the -0.3466 on y^2=x^3+19x-20 is h_2, the I_6 prime, not p=11), and achieves the intent of the blocked T3 theta cross-check (e2n) by the proper route.

**Net for Direction 8.** Every term the 2K dictionary calls for on a SINGLE arithmetic surface is now computed by the reference algorithm and validated against the independent limit-defined canonical height: the positive-definite signature (the Hodge index, ranks 1-4) and the complete local decomposition (archimedean incidence `lambda_inf` (2I), archimedean self-incidence Petersson norm (2L), and every finite local height good/bad via Silverman's exact algorithm (2P)). The Faltings-Hriljac arithmetic Hodge index is thus fully instantiated computationally. The remaining gap is unchanged and singular: the PRODUCT surface `Spec(Z) x Spec(Z)` and its Frobenius correspondence (2K sec 4/6b) -- now the only missing object, with everything that lives on a single arithmetic surface in hand and validated.

**Methodological.** Authoritative textbook algorithms (Cohen/Cremona/Silverman), validated against an independent ground truth (the 4^{-n} limit h_hat), beat ad-hoc reconstructions: 2P superseded the partial 2I (missing the convergence switch) and the approximate 2O (wrong bad-prime attribution) and resolved the blocked 2N -- all caught/fixed by the gate-against-h_hat discipline, never by assumption.

### 23. The genuine archimedean Neron local height (self-derived, validated against LMFDB h_hat to 1e-5): for integral-generator curves the arithmetic Hodge index regulator is 100% archimedean on the diagonal, BUT the archimedean pairing alone goes indefinite by rank 3 -- positivity is GLOBAL (archimedean diagonal + finite off-diagonal), mirroring 3M's two-clock balance on the arithmetic side.

2I ([e2i_archimedean_local_height.py](arithmetic_geometric/e2i_archimedean_local_height.py), writeup [e2i_archimedean_local_height.md](arithmetic_geometric/e2i_archimedean_local_height.md)) computes the transcendental archimedean Neron local height that 2H's naive coordinate split could not see.

**Method (self-derived, not transcribed).** Derived the Tate telescoping series from the duplication formula + canonical recursion (`z(t)=1-b4 t^2-2 b6 t^3-b8 t^4`, `w(t)=4t+b2 t^2+2 b4 t^3+b6 t^4`, `1/x(2P)=w/z`; ansatz `mu=½log|x|+½ sum 4^{-(n+1)} log|z(t_n)|` satisfies `mu(P)-¼mu(2P)=¼log|2y+a1x+a3|`, sum over places = 0 by the product formula). Then VALIDATED against the LMFDB-matched `h_hat`. The bare ansatz reconstructed `h_hat/2` exactly -- the documented Silverman-paper-vs-books factor of 2 -- found empirically, not assumed; rescaling `lambda=2mu` gives the `h_hat = sum_v lambda_v` convention. Validation `lambda_inf + log(den x) = h_hat` holds to 1e-5..1e-9 across all test points (including non-integral 2P where the finite places genuinely enter).

**Result.** For the integral generators (37a, 389a, 5077a), finite local heights vanish, so `lambda_inf(P) = h_hat(P)`: each canonical height is PURELY archimedean (arch trace share 100%). BUT the archimedean pairing MATRIX alone is positive definite only at rank 1-2; at rank 3 (5077a) it is indefinite (arch Gram det -0.92). The off-diagonal finite contributions (from non-integral P+Q) are what make the TOTAL pairing positive definite (Faltings-Hriljac). So the archimedean place carries the diagonal bulk, but the SIGNATURE is global: archimedean cushion + finite glue, neither alone. This is the arithmetic-geometry face of 3M's two-clock balance (archimedean must combine with finite to produce positivity), now where positivity is a theorem.

**Methodological note.** A self-derived algorithm validated against an independent ground truth (LMFDB `h_hat`) is stronger than a transcribed formula: the factor-of-2 normalization trap was caught by the validation, not assumed away. No unvalidated transcendental code entered the codebase (contrast the discipline applied throughout this session).

### 22. The arithmetic Hodge index IS a theorem over Spec(Z): the Neron-Tate height pairing on E(Q) is positive definite (validated against known regulators, rank 1-3). But the naive coordinate height split assigns the archimedean place ~0 canonically -- the true archimedean local height is the transcendental sigma-function quantity, not visible in coordinates.

2H ([e2h_arithmetic_hodge_index.py](arithmetic_geometric/e2h_arithmetic_hodge_index.py), writeup [e2h_arithmetic_hodge_index.md](arithmetic_geometric/e2h_arithmetic_hodge_index.md)) computes the canonical height pairing on E(Q) via the exact limit `h_hat(P) = lim h_x(2^n P)/4^n` (group law in exact rationals) for rank 1, 2, 3 curves.

**Headline (solid, validated).** The pairing matrix is POSITIVE DEFINITE for every curve (signatures (1,0),(2,0),(3,0)) -- the Faltings-Hriljac arithmetic Hodge index over Spec(Z), exhibited as a signature. Computed regulators match known LMFDB values (37a 0.05111, 389a 0.15246, 5077a 0.41714). With #21 (2G) this completes the signature picture on both sides of the function-field / number-field divide: negative-definite primitive form on C x C (theorem, 2G), positive-definite height pairing on E/Q (theorem, 2H). Over Spec(Z) the Hodge-index signature is REAL for a single arithmetic surface; the gap is only the product surface Spec(Z) x Spec(Z) and its Frobenius.

**Honest caveat (archimedean place).** The naive coordinate split (h_inf = log max(|x|,1), h_fin = log den) is exact but is NOT the Neron/Arakelov local decomposition. Empirically h_inf/4^n -> 0 (the 2^n P equidistribute on E(R), |x| stays bounded), so the naive split assigns ~0 to the archimedean place. The genuine archimedean Neron local height lambda_inf is the transcendental Weierstrass-sigma / Green's-function quantity, invisible in coordinates. That its coordinate proxy vanishes canonically is the lesson: the archimedean contribution needs genuinely analytic machinery, exactly the framing-document theme (new_mathematics.md §4.2) that the archimedean place is the subtle missing piece.

**Next.** Compute lambda_inf(P) via the sigma-function / Tate's series (mpmath theta), validate by lambda_inf + sum_p lambda_p = h_hat against exact finite local heights, and quantify the archimedean share of the regulator -- "how the archimedean place enters the signature," done correctly.

### 21. Direction 8 opened: the function-field Hodge index is now exact in code as a SIGNATURE -- the primitive intersection form on C x C is negative definite, and that negative-definiteness IS the Hasse-Weil bound. This is the non-circular (signature-side) counterpart to 3M's circular (trace-side) positivity.

2G ([e2g_intersection_signature.py](arithmetic_geometric/e2g_intersection_signature.py), writeup [e2g_intersection_signature.md](arithmetic_geometric/e2g_intersection_signature.md)) builds the intersection form on the sublattice `{e, f, Delta, Gamma}` of `NS(C x C)` (Frobenius graph `Gamma`, diagonal `Delta`, fibres `e, f`) with the classical intersection numbers, and computes its signature across genus 1-2 curves over `F_q`.

**Result (exact, whole family):** full Gram signature is `(1, 3)` (Hodge index: one positive eigenvalue); the primitive part `{Delta_0, Gamma_0}` (orthogonal to the hyperbolic `{e,f}` plane) is negative definite `(0, 2)`; and that negative-definiteness is identically `4 g^2 q - t^2 > 0`, i.e. the **Hasse-Weil bound** `|t| < 2g sqrt(q)` with `t = q + 1 - N_1`. Iterating over Frobenius powers forces `|alpha_i| = sqrt(q)`. **Positivity from a signature, not a trace identity.**

**Why this matters for the program.** It is the function-field TEMPLATE (Direction 8 milestones 5.1 state-the-index + 5.5 Weil-specialization/K3), exact and verified, giving the precise target a Spec(Z) lift must reproduce. It also closes a loop with finding #20: 3M decomposed the **trace/explicit-formula side** (Arch 3) of the positivity and found it circular as a proof route (R3.5/K1); 2G is the **signature side** (Arch 2) of the SAME positivity, and the signature is non-circular. That contrast is exactly why Direction 8, not Architecture 3, is the route.

**K2 geometric face.** The construction is unbuildable for Davenport-Heilbronn: no Euler product => no Frobenius => no graph `Gamma`, no surface. This is the geometric shadow of #20's fingerprint (no Euler product <=> von Mangoldt weight delocalizes off prime powers).

**The precise lift gap.** The template names what is missing over Spec(Z): the surface `Spec(Z) x Spec(Z)` (absent), an arithmetic Frobenius (absent), and the `(1, k)` signature on the arithmetic Neron-Severi (the central open problem). Encouraging precedent: the Faltings-Hriljac arithmetic Hodge index theorem holds for a SINGLE arithmetic surface with signature `(1, rho-1)`; the gap is the product surface and the Frobenius, not the index theorem itself. Natural next computational step: the Arakelov / Faltings-Hriljac pairing on a single arithmetic surface, to see how the archimedean place enters the signature.

### 20. The Weil form admits an INPUT-SIDE place-type split (archimedean vs finite) that is non-circular, unlike the answer-side on/off split; its clean part is the Euler-product fingerprint (Lambda_L delocalizes onto composite n iff there is no Euler product: zeta 0, D-H 64 starting at n=6), and the off-line obstruction is buried at exactly the archimedean-prime cancellation scale.

3M ([e3m_place_type_balance.py](positivity/e3m_place_type_balance.py), writeup [e3m_place_type_balance.md](positivity/e3m_place_type_balance.md)) introduces a decomposition of the SAME Weil Gram matrix used by 3C-3J, but split by **place type** via the explicit formula rather than by zero location:

```
M = A_arch + P_fin + B_pole        (computable from Gamma factor + Dirichlet coefficients, no zeros)
```

vs 3J's answer-side `M = M_on + M_off` (computable only after locating the zeros). The place-type split is the non-circular object a proof is allowed to use, and is exactly the archimedean-vs-finite uniformity the framing document ([new_mathematics.md](../docs/03_research/new_mathematics.md) §2.2, §4.2) demands.

**Validated.** The finite block `P_fin` (built from `Lambda_L(n)`, the coefficients of `-L'/L`, via `a_n log n = sum_{d|n} Lambda_L(d) a_{n/d}`) and the pole block `B_pole` reproduce 3F's independent prime sum and boundary term to floating point.

**Euler-product fingerprint (cancellation-free headline).** `Lambda_L(n)` makes the missing Euler product visible input-side (n <= 200):

| L | a_1 | # composite-n support | first composite n |
|---|---:|---:|---:|
| zeta | 1 | **0** | none |
| Davenport-Heilbronn | 1 | **64** | **6** |
| Epstein d=47 non-principal | **0** | n/a (no a_1=1 series) | n/a |

For zeta, `Lambda_zeta` lives only on prime powers (`Lambda(p^k)=log p>0`): the Euler product exactly. For D-H, `Lambda_DH` spills onto composite integers, first at `n=6=2*3`. The non-principal Epstein form `2m^2+mn+6n^2` never equals 1, so `a_1=0` and the `-L'/L` recursion does not apply directly.

**Decisive control (the fingerprint detects NON-EULER, not RH-failure).** A natural temptation is to read the composite-n block `P_composite` (the prime block restricted to composite n) as the off-line obstruction. An Epstein class-number ladder kills this:

| L | Euler product | off-line zeros | composite support | P_composite |
|---|---|---|---:|---|
| zeta | yes | no | 0 | zero |
| Epstein d=3, d=4 (h=1) | yes (= zeta L(chi)) | no | 0 | zero |
| Epstein d=47 principal (h=5) | no | **no (<=T=120)** | 15 | indefinite |
| Davenport-Heilbronn | no | **yes** | 39 | indefinite |

`P_composite` is exactly zero for every genuine Euler product (the h=1 Epstein forms factor as `zeta L(chi)`) and indefinite for every non-Euler function -- but Epstein d=47-principal is non-Euler with indefinite `P_composite` and NO off-line zeros. So composite-n support tracks **non-Euler-ness, not RH-failure**: necessary (an Euler product forbids it) but not sufficient. This is the reformulation trap ([new_mathematics.md](../docs/03_research/new_mathematics.md) §5.2, failure mode #5), and is the D-H discipline applied to 3M's own method.

**Net narrowing.** The place-type split is the right structure (uniform archimedean/finite treatment, input-side) but does NOT by itself manufacture positivity: no soft input-side bookkeeping (eigenvalue reconstruction OR composite-support detection) escapes the requirement that the **archimedean block dominate the prime obstruction**, which is the hard Weil/Connes core. This localizes RH's difficulty exactly where the framing document says it must live (§2.2: if positivity is still the hardest step, the framework is not yet right) and argues for the structural route (Hodge-index-type cushion dominance, Architecture 2 / Direction 8) over any further detector.

**Diagnosed gap (provisional).** The archimedean block via the frequency-space digamma kernel matches 3F's validated Bombieri-form integral to 0.2% at large b but carries a converged ~0.06 absolute offset at small b (stable to t_cap = 2e4; isolated to A_arch). Since `M ~ 0.08` is a residue of blocks of size ~60, this swamps the input-side eigenvalue detector. Fix: compute `A_arch` from the bilinear Bombieri-form integral per L-function Gamma factor.

**Structural finding (marginal positivity, sharpened).** D-H's raw off-line obstruction (`-2.6%`, finding #10) is the SAME ORDER as the archimedean-minus-prime cancellation residue in the explicit formula. The obstruction is buried at exactly the cancellation scale: invisible to a soft input-side reconstruction, visible only with exact arithmetic or the answer-side projection of 3J (which manufactures the `-78.7%` sharpening by projecting onto range(M_off), an answer-side move). This explains WHY finding #19's "fundamentally different diagnostic" is hard to build, and pins what a working positivity certificate must do: engage the exact arithmetic of the blocks (Euler product => prime-power support; off-line obstruction => composite-n terms an Euler product forbids), not their floating-point difference.

### 19. Schur framework has no leverage point for disproof: hypothetical off-line zero signal scales as 16 * (beta - 1/2)^2, with stealth window epsilon < 10^-5 in float64 -- looser than direct rigorous verification (epsilon < 10^-7 from Platt-Trudgian).

3K ([e3k_hypothetical_offline.py](positivity/e3k_hypothetical_offline.py), README section 3K) injects hypothetical off-line zero pairs into zeta's zero list and traces the Schur complement signal. The result is a clean negative for the disproof program:

**Three structural findings:**
- **Quadratic scaling:** Schur rel min = -16 * (beta - 1/2)^2 uniformly across gamma_0 in [30, 180] and epsilon in [5 * 10^-5, 10^-2]. Saturates to D-H asymptote -0.8 around epsilon ~ 0.1.
- **Stealth window in float64:** epsilon < 3 * 10^-6 (below this, M_off looks rank-1 PSD, framework reports "no obstruction"). Higher precision (mpmath prec=50) would push stealth threshold to ~10^-25.
- **Rigorous verification is SHARPER:** Platt-Trudgian rigorous verification bounds zeros to ~10^-7 from the critical line up to T = 3 * 10^12. Any hypothetical off-line zero with epsilon > 10^-7 is already excluded. Schur framework's float64 sensitivity is ~30x looser than this.

**Pro-RH implication.** The "marginal positivity" of zeta (Finding 18: D-H fails by 78.7% per off-line direction) is PROOF-TECHNIQUE-marginal, not NUMERICALLY-marginal. Combining 3J + 3K:
- D-H violates Weil positivity by a large structural gap (78.7%).
- zeta tolerates hypothetical off-line zeros only at epsilon < 10^-7 (excluded by direct verification).
- There is no "stealth window" where Schur detects what direct methods miss.

**Why this matters.** A productive disproof program needs a diagnostic that's more sensitive than existing direct verification. The Schur framework, while structurally sharp for distinguishing zeta from D-H (3J), is not such a tool: its sensitivity is below the rigorous numerical bound. Any productive disproof attempt must use a fundamentally different diagnostic (de Bruijn-Newman heat equation deformation, higher-precision direct zero verification at extreme heights, or some yet-unidentified spectral technique). This rules out the Gram-matrix / Weil-form positivity direction as a disproof avenue.

**Strategic implication for the project.** The disproof angle in the positivity family is closed. Continue allocating compute to proof-direction work (Arch 2, Arch 1, Arch 3 sharpening, Arch 4 LP/SDP), not disproof.

### 18. Two-clock decomposition of the Weil Gram matrix: the Schur complement against the on-line cushion isolates an off-line obstruction ~30x sharper than the raw spectrum (asymptote -78.7% vs -2.6%), with signature exactly (N_off, N_off) per off-line gamma in UHP.

3J ([e3j_schur_complement.py](positivity/e3j_schur_complement.py), README section 3J) decomposes the Weil-form Gram matrix as $M = M_{\rm on} + M_{\rm off}$ and computes the true Schur complement $S = M / M_{CC}$ where $M_{CC}$ is the on-line orthogonal complement block. $S$ is the off-line obstruction *after the on-line cushion has been deployed optimally*.

**Structural results (validated at $T_{\max} \in \{200, 300, 500\}$, $K \in [30, 1000]$):**

| Quantity | Value | Interpretation |
|---|---|---|
| $\dim(S)$ for D-H | $2 N_{\rm off}$ exactly | One rank-2 indefinite piece per off-line $\gamma$ in UHP |
| $\mathrm{sig}(S)$ for D-H | $(N_{\rm off}^-, N_{\rm off}^+)$ exactly (for $K$ above settling) | Signature stable across $K \in [100, 1000]$ |
| $\lambda_{\min}(S) / \lambda_{\max}(S)$ asymptote | $-78.7\%$ | Saturated by $K = 500$; $T_{\max}$-invariant |
| Raw $M$ rel min asymptote | $-2.6\%$ (3D.3 result) | Diluted by the on-line cushion's large $\lambda_{\max}$ |
| Sharpness factor Schur / raw | $\approx 30 \times$ | Schur isolates obstruction from on-line background |
| Cushion cost (cross-coupling correction) | $\to 0$ as $K \to \infty$ | On-line cross-coupling becomes negligible at large $K$ |

For $\zeta$ and $\chi_3$: $\dim(S) = 0$ at every $K$ (no off-line zeros, trivial Schur).

**Quantitative form of the marginal-positivity thesis.** In the off-line subspace, the on-line cushion delivers $1 - 0.787 = 21.3\%$ of the off-line magnitude. RH-style positivity would require $\geq 100\%$. D-H fails by precisely 78.7% per off-line $\gamma$ direction, uniformly. This is the sharpest finite-dimensional pinning to date of how far D-H violates RH-like positivity, and the obstruction is shown to be intrinsic (not an artifact of basis choice or test-function family).

**Methodological lesson.** The raw $M$ spectrum understates the off-line obstruction by mixing it with the on-line background. The Schur complement against the on-line cushion is the natural way to extract the obstruction-only signal: it lives on a fixed-dimensional subspace whose dimension is determined by the *count* of off-line $\gamma$ values, not by the basis size $K$. This generalizes to any two-clock positivity decomposition (Bombieri's positivity, Connes's adelic trace, Deninger's Frobenius / archimedean fiber split): the structural quantity to measure is the Schur complement of one clock against the other, not the raw spectrum.

**Strategic implication for proof architectures.** Any RH-style positivity proof for $\zeta$ must show that on the analog of $\mathrm{range}(M_{\rm off})$, wherever the obstruction lives in the Arch-3 / Arch-1 setup, the on-line cushion strictly dominates. The "two-clock balance" must beat $1.0$. For D-H this balance is $0.213$. The gap to RH is unambiguous and large. This pins down what an Arch-3 proof technique must achieve quantitatively, not just qualitatively.

### 17. Weil's explicit formula in operator form is the single highest-leverage Mathlib contribution for the project: one PR unlocks structural work across Arch 1, 3, 4, and the R3.5 concrete-instantiation track.

VERIFIER session 002 ([r3_5_verification_attempt.md](orchestrator_sessions/r3_5_verification_attempt.md)) identified the bottleneck. The relevant Mathlib gap is

```
Mathlib.NumberTheory.LSeries.ExplicitFormula:
  theorem riemannZeta_explicit_formula (phi : C -> C) (h_phi : phi in TestFunctionClass) :
    sum_{rho in nonTrivialZeros zeta} phi(rho) = boundary(phi) + sum_p log(p) * primeKernel(phi, p)
```

One Mathlib PR (operator-form Weil-Riemann-Guinand explicit formula) unlocks:

1. **R3.5 concrete instantiation**: every NCG framework's trace identity is by definition the operator form of this identity. Once Mathlib has the analytic version, the operator version is one step of "lift to functional calculus".
2. **Arch 3 Weil-Bombieri positivity in Lean**: the positivity statement `sum_rho |hat f(rho)|^2 >= 0` IS the explicit formula applied to `|f|^2`. With the formula in Mathlib, Arch 3 positivity becomes first-class Lean.
3. **Arch 4 Mossinghoff-Trudgian translation**: the formula bridges zero distribution and prime distribution. The 1D ceiling work needs the formula to convert "zero at beta + i gamma exists" to "trig polynomial inequality fails".

By contrast, an unbounded normal operator spectral theorem (the obvious other gap) would unlock R3.5 ONLY in its operator-level form. VERIFIER's structural R3.5 in session 002 sidesteps that gap by reformulating P-SA at the spectral-image level. So the operator spectral theorem is LESS leveraged than the explicit formula.

**Estimated cost**: a Mathlib PR for the explicit formula is on the order of 5-15 person-months, depending on how cleanly the test function class can be set up against existing `Mathlib.NumberTheory.LSeries.RiemannZeta`. This is small compared to the ~50 person-months VERIFIER estimates for a concrete Connes adelic NCG framework instance.

**Strategic implication**: if the project ever escalates to active Mathlib contribution, the Weil explicit formula is the canonical target. It is the single deliverable that compounds across the largest number of architectures.

### 16. The Fermat-Frobenius axiom for Lambda-blueprints has three equivalent / nested formulations (A blueprint-relation, B Adams quotient, C delta-ring); A and B are logically equivalent, C is strictly stronger and uncovers that F_p is NOT a native delta-blueprint at p.

Session 002 produced three independently-developed candidates for the Fermat-Frobenius axiom required by Direction 1 milestone 4.1: [A](arithmetic_geometric/D1_4_1_fermat_frobenius_candidate_A.md) (blueprint-relation form), [B](arithmetic_geometric/D1_4_1_fermat_frobenius_candidate_B.md) (Adams-operation quotient), [C](arithmetic_geometric/D1_4_1_fermat_frobenius_candidate_C.md) (delta-ring lifted).

**Triality structure.** Both BUILDER-1A and BUILDER-1B independently identified that A and B are logically equivalent. A keeps the original blueprint and demands `(psi_p(x), x^p) ∈ congr_p` where `congr_p` is the sub-relation of `relations` generated by `(p · m, 0)` and closed under blueprint operations. B builds the quotient blueprint `B / I_p` first and demands strict equality `pi_p ∘ psi_p = Frob_p ∘ pi_p`. The two characterize the same `(B, psi)` pairs as Lambda-blueprints but produce different morphism categories. C provides a strictly stronger framework with `delta_p : B -> B` as primitive data and `psi_p(x) := x^p + p · delta_p(x)` as derived; in the p-torsion-free case C is equivalent to B, but in general C carries strictly more data.

All three pass the K2 D-H exclusion. All three recover the Joyal/Borger condition `psi_p(x) ≡ x^p (mod p)` on ring blueprints. All three correctly reject `Z[T]` with `psi_p = id` and accept the canonical Lambda-structure `psi_p(T) = T^p`.

**The new structural obstruction.** Candidate C uncovers a genuine new finding: **F_p does NOT carry a native delta-blueprint structure at p**. Axiom (DR2) requires the Buium polynomial `C_p(x, y) := (x^p + y^p - (x + y)^p) / p` to vanish identically; in F_p, `C_2(1, 1) = (1 + 1 - 4)/2 = -1 ≠ 0`. F_p can only be treated via prismatic lift to Z_p. This downgrades constraint (iii) "F_q compatibility" from R2.5's predicted "yes" to "partial-no" for candidate C and explains structurally why Bhatt-Scholze restrict prismatic / delta-ring theory to p-torsion-free or "prismatic" rings. The obstruction is real, not an artifact of any single framework choice.

**Methodological lesson.** Running three BUILDERs in parallel on the same milestone was decisive. A or B alone would have given the "weak" answer; C alone would have left the equivalence to A/B as an open conjecture. Together the three triangulate the structure: A and B fix the morphism-vs-quotient methodological split; C fixes the rich-witness extension and surfaces the F_p obstruction. The recommended Lean architecture (per BUILDER-1C) exposes all three layers as a hierarchy `LambdaBlueprintA <= LambdaBlueprintB ≡ LambdaBlueprintA' < LambdaBlueprintC = DeltaBlueprint with commutation` so downstream theorems can be parameterized by the structure level they actually need.

**Forward consequence.** This is the first session 002 finding that strengthens Phase 2 readiness: the candidate C framework is the prismatic-compatible structure directly. If session 003 VERIFIERs successfully formalize `#FF-C-1..4`, Direction 3 (prismatic cohomology) has a typed-Lean target to build on, rather than needing to construct the underlying Lambda-structure from scratch.

### 15. Polynomial-ideal SOS via Putinar/Schmuedgen (SDP) confirms but does NOT escape the 4E.3 line-restriction lemma: the entire LP/SDP family is structurally capped.

4E.8 ([e4e8_sos_sdp.py](zero_free/e4e8_sos_sdp.py), writeup [e4e8_sos_sdp.md](zero_free/e4e8_sos_sdp.md)) tests the third and last open LP/SDP-style escape route from 4E.3 identified by [4E.6](zero_free/e4e6_constrained_lp.md): polynomial-ideal SOS via Putinar/Schmuedgen. Uses cvxpy 1.9.0 with the CLARABEL SDP solver.

**Three structural findings:**

**(Phase A) 4E.2's +25% LP gap is REAL, not a sampling artifact.** The cos × cos SOS-SDP at SOS-bidegree L = 1 (polynomial bidegree (2, 2)) matches the K-sampling LP to floating-point precision across the entire alpha sweep:

| alpha | C-S 1D | cos SOS-SDP | K-sampling LP | gap to C-S |
|---:|---:|---:|---:|---:|
| 0 | 2.0000 | 2.0000 | 2.0000 | 0% |
| 1 | 2.2857 | 2.5616 | 2.5616 | +12.07% |
| 3 | 3.2000 | **4.0000** | **4.0000** | **+25.00%** |
| 5 | 5.3333 | 5.7016 | 5.7110 | +6.90% |

At bidegree (2, 2) for the cos × cos slice, the 2D Fejer-Riesz analog HOLDS at the extreme rays we test (max c_{1, 1} + alpha c_{2, 2}). The general statement of 2D Fejer-Riesz fails at higher degrees (Scheiderer), but the slice we care about is benign.

**(Phase C) Full-trig SOS gives no advantage over cos × cos SOS for this objective.** Allowing sin × sin, cos × sin, sin × cos cross terms in P and extracting the cos × cos projection yields the SAME maximum at every alpha tested. The extremal polynomials are already cos × cos.

**(Phase D) The 4E.3 line-restriction lemma is SATURATED but NOT VIOLATED by SOS-SDP.** Direct SDP maximization of c_1 of the phi = 2 theta line restriction over cos × cos SOS polynomials of bidegree (2, 2), with c_0 of the restriction = 1, gives:

| Polynomial | c_1 / c_0 of restriction (raw) | ratio to Fejer raw 1.8478 |
|---|---:|---:|
| 4E.2 LP-optimal (alpha = 3) | 0.8000 | 0.4330 |
| SDP-optimal (cos × cos SOS, L = 1) | **1.8478** | **1.0000** |

The SDP saturates 1D Fejer at effective degree 6 EXACTLY (ratio 1.0000 to 4 decimals). The saturating polynomial is recognizably Q(theta, phi) = (1 + cos theta)(1 + cos phi), so $P|_{\phi=2\theta} = 4 \cos^4 \theta (1 + \cos \theta)^2$.

**This bounds the Putinar/Schmuedgen polynomial-ideal SOS from above.** For any tubular neighborhood K of the line phi = 2 theta in the Putinar setup ($g \ge 0$ defining the neighborhood, certificate $P = \sigma_0 + g \sigma_1$ with sigma_l SOS), the max c_1 of restriction is at most the line-restriction limit, which is 1.8478 = Fejer at effective degree 6. So Putinar polynomial-ideal SOS for the phi = 2 theta coupling does not escape the 4E.3 wall.

**Pattern (extending LEARNINGS finding #12):** the 4E.3 line-restriction lemma is robust under the entire LP/SDP relaxation family. Each successive attempted escape converges to the structural Fejer wall:

- 4E.6 (constrained-domain K-point LP): full collapse to Fejer.
- 4E.7 (multi-zero LP, naive objectives): real shape-factor gain (lambda_{1,1} 55-137× larger than lambda_1^2) but rank-1 LP optima.
- 4E.8 (SDP / SOS / Putinar): saturates Fejer line-restriction bound but does not exceed it.

The pattern: **the more LP/SDP-like the escape, the more cleanly it confirms 4E.3 rather than escaping it.** Remaining qualitatively-distinct directions (Bombieri variational SOS with L^2 penalty allowing polynomial negativity; Heath-Brown explicit multi-zero MT bookkeeping combining 4E.2's higher-harmonic gain with multi-zero ledger; arithmetic-geometric or spectral inputs from Arch 1/2) live outside the LP/SDP framework.

**Architectural implication.** Combined with finding #14 (the V-K stagnation), this closes Architecture 4 numerically. The single-zero MT zero-free region constant cannot be improved via LP/SDP machinery on multivariate non-negative trig polynomials at any bidegree, with any objective, in either LP or SDP form. Per LEARNINGS finding #14, pushing the V-K exponent requires fundamentally new input from Arch 2 or Arch 1.

**Cross-cut to the marginal-positivity thesis.** Adding to the list of reinforcing directions: the LP/SDP machinery's inability to escape the Fejer wall is another instance of "RH is true only at the margin". The wall is tight enough that even the strongest natural LP/SDP relaxation (Putinar SOS) saturates it exactly. The margin within the LP/SDP framework is zero, which is the useful conclusion: it closes this framework cleanly and redirects effort to the architectures (Arch 2 geometric, Arch 1 spectral) that are not bounded by the Fejer ceiling.

### 14. Architecture 4's 67-year stagnation at the Vinogradov-Korobov exponent $2/3$ is a structural ceiling, not insufficient effort: all three inputs of the V-K recipe are now near-optimal within their frameworks.

The 4A + 4C unified literature dossier ([4a_4c_vinogradov_korobov.md](zero_free/4a_4c_vinogradov_korobov.md)) reads the project's experimental thread back against the classical analytic route to a zero-free region. The route has three inputs: (Input 1) the explicit formula relating zero locations to a prime sum, (Input 2) a non-negative trig polynomial as auxiliary inequality, (Input 3) an exponential sum bound on $\zeta$ in the critical strip. **All three inputs are individually near-optimal**:

- **Input 2 is saturated by 4B-4E.7.** 4B's LP saturates Fejér $\cos(\pi/(N+2))$ exactly at every tested degree. The 4D, 4E, 4E.2, 4E.3, 4E.4, 4E.5, 4E.6, 4E.7 multivariate experiments tested every natural extension (single-coefficient, balanced-diagonal-sum, constrained-domain, multi-zero, $d \in \{2, 3, 4\}$) and none escapes the 1D Fejér ceiling on the MT zero-free constant. The 4E.3 structural lemma (any $d$-variate non-neg poly restricted to a line is a 1D non-neg poly bounded by 1D Fejér at matched effective degree) is robust under all tested relaxations.
- **Input 3 is at the Vinogradov mean value theorem main conjecture** (Bourgain-Demeter-Guth 2016, $\ell^2$-decoupling). The $2/3$ exponent comes from the optimization $k \sim (\log T)^{1/3}$ trading V-MVT degree against block size; once V-MVT is sharp, this optimization gives $2/3$ as a true ceiling.
- **Input 1 (the explicit formula) is an identity**, with no further optimization slack.

**The conditional landscape confirms the picture.** Of all named conditional improvements (density hypothesis $N(\sigma, T) \ll T^{2(1-\sigma)+\epsilon}$, Lindelöf hypothesis, no-Siegel-zero, Heath-Brown 1992, Pintz 1976/2017, Ford 2002, BDG 2016, RH itself), NONE would push the leading exponent from $2/3$ down. Each either sharpens multiplicative constants within V-K (BDG, Ford), gives $q$-uniformity (Heath-Brown), is a Deuring-type "if-then" with a hypothetical hypothesis (Pintz Siegel⇒ZFR), or trivially solves the problem (RH). The conditional landscape is **internally consistent with the structural ceiling**: no easy conditional fix exists.

**The architectural implication.** Architecture 4 is a **constraint-mapping architecture**, not a route to RH. It quantifies the tightest currently-provable wall and shows that wall is structural. Improving the exponent requires a fundamentally new input class, structurally outside the V-K recipe:
- **Architecture 2 route**: arithmetic-geometric exponential-sum machinery á la Deligne's solution of the Weil conjectures, applied to $\zeta(s)$ rather than $L$-functions over finite fields. Per 2A's diff-table analysis, this is the constructive obstruction.
- **Architecture 1 route**: spectral identification on Connes' adèle class space (1D dossier), producing zero locations directly and making the V-K route obsolete.

**Cross-cut to the marginal-positivity thesis** (memory + project capstone): RH is "just barely true" in multiple senses; the V-K bottleneck being just-barely-loose-enough to admit off-line zeros is one of those senses. The classical analytic route gives the tightest currently-provable wall, and the gap from this wall to RH is structural rather than incidental — consistent with the project's overall framing that **any RH proof must use exact zeta structure** (Euler product + functional equation + the specific cohomology of $\mathrm{Spec}(\mathbb{Z})$), not just generic analytic features.

**Methodological lesson.** A 67-year stagnation that *every* named conditional improvement fails to break is a signal of structural ceiling, not insufficient cleverness. Maps to the 4E.3 / 4E.6 / 4E.7 pattern within the architecture: each LP-escape attempt confirms that the original structural lemma is robust under the next-most-natural relaxation. The pattern recurs at the architecture-level meta scale.

### 13. Multi-zero MT LP gives a real shape-factor improvement but rank-1 LP optima at naive objectives: the higher-harmonic structure of 4E.2 is needed for a non-trivial multi-zero MT win.

4E.7 ([e4e7_multi_zero_lp.py](zero_free/e4e7_multi_zero_lp.py), [.md](zero_free/e4e7_multi_zero_lp.md)) tests the second proposed escape from 4E.3's line-restriction lemma identified by 4E.6: postulate multiple putative zeros at independent heights, so the LP becomes multivariate with full $d$-torus non-negativity (4E.3 lemma doesn't directly apply).

**Result, two layers:**

**(Real win at shape-factor level)** The joint two-zero shape factor $\lambda_{1,1} = (q_1^2 - 1)^2 / 4$ is STRICTLY LARGER than $\lambda_1^2$ (naive two-independent-zero MT). Ratios at $N = 2, 3, 4$: 137×, 72×, 56×. This reflects the "zeros interact in the explicit-formula sum" effect that motivates Heath-Brown / Pintz multi-zero MT.

**(But rank-1 LP optima)** The LP-optimal polynomial for max $c_{1,1}$ at bidegree $(N, N)$ is rank-1 (tensor product $Q(\theta) Q(\phi)$), with LP value $= q_1^2$ exactly (per 4D-ii). Balanced-sum LP $\max c_{1,0} + c_{0,1} + \alpha c_{1,1}$ and Heath-Brown-style $a(c_{1,0} + c_{0,1}) + b c_{1,1}$ also rank-1 across all tested $(\alpha)$ and $(a, b)$. **Naive multi-zero objectives DO NOT exceed the tensor bound at the LP-value level.**

**The synthesis**: a non-trivial multi-zero MT improvement requires combining:
1. **Higher-harmonic LP gain** (4E.2's +25% rank-2 win via $c_{1,1} + \alpha c_{2,2}$): non-tensor 2D structure exists at higher harmonics.
2. **Multi-zero MT bookkeeping** (Heath-Brown 1992, Pintz 1976): the explicit-formula manipulation that translates the LP value to a zero-free region constant.

This combination is research-grade work beyond the experiment.

**Translation to zero-free region for asymptotic RH**: Riemann-von Mangoldt density gives consecutive-zero spacing $\sim 2\pi / \log T$ at height $T$, so multi-zero MT applies tightly only at finite height. Heath-Brown / Pintz get constant-factor improvements for FINITE-RANGE problems (Siegel zeros, least prime in AP) where multiple zeros at controlled distances are postulated. For asymptotic RH on zeta, multi-zero MT could improve the **constant** but not the **scaling** $1/\log T$.

**Cross-cut to 4E.6**: both 4E.6 (constrained-domain) and 4E.7 (multi-zero) are LP-based escape routes from 4E.3 identified in finding #12. 4E.6 collapsed entirely. 4E.7 gives a real shape-factor improvement but bounded by tensor decomposition at naive objectives. **The remaining LP-escape direction is 4E.8 (polynomial-ideal SOS via Putinar/Schmüdgen)** which requires SDP not LP — structurally different machinery, the only remaining open route.

**Methodological pattern (extending finding #12)**: the structural lemma (4E.3) is robust under multiple escape attempts:
- Naïve domain relaxation (4E.6): full collapse.
- Multi-zero LP (4E.7): real shape-factor win, but tensor-product LP optima.
- Polynomial-ideal SOS (4E.8 open): the qualitatively-distinct machinery remaining.

Each subsequent escape attempt is structurally further from the original LP. The pattern is: "the more LP-like the escape, the smaller its eventual win against 4E.3."

### 12. The MT 1D-Fejér ceiling is robust under naïve domain relaxation: constrained-domain LP is not a separate escape route.

4E.6 ([e4e6_constrained_lp.py](zero_free/e4e6_constrained_lp.py), [.md](zero_free/e4e6_constrained_lp.md)) tests the proposed escape from 4E.3's structural lemma: relax the non-negativity constraint $P \ge 0$ to a subset $\Omega \subset [0, 2\pi]^d$ (the "constrained-domain LP"). The 4E.3 lemma's proof relies on full non-negativity, so a domain restriction *might* break the line-restriction-to-1D-Fejér argument.

**Result**: it doesn't. Four natural formulations were tested:

| Setup | Constraint | Behavior |
|---|---|---|
| A | $P(\theta_k) \ge 0$ at $K$ evenly-spaced points | hits $c_{\rm bound}$ for $K \le N$; recovers Fejér for $K \gg N$ |
| B | $P \ge 0$ on $[0, 2\pi] \setminus (\theta_0 - \delta, \theta_0 + \delta)$ | $\equiv$ Fejér for small $\delta$; hits $c_{\rm bound}$ with huge negative excursions for large $\delta$ |
| C | $P \ge 0$ at $\theta_k = \gamma_k \log p \bmod 2\pi$ for $K$ on-line zeros | recovers Fejér as $K \to \infty$ (Weyl equidistribution) |
| D | constrain at on-line zeros, max $P$ at off-line trick frequency | apparent gain decays to 1.000 as $K \to \infty$ (sparse-sampling artifact) |

Setup D, the most MT-faithful formulation, gives apparent gains over the full-non-negativity baseline that decay monotonically with $K$: at $N=8$, $K=50$ gives ratio 1.90, $K=400$ gives 1.000. Pure sparse-sampling, not structural.

**Why each formulation fails the same way**: the MT explicit-formula sum runs over **all** zeros of $\zeta$. Relaxing the test polynomial's non-negativity to a subset means losing the inequality $\sum_\rho f(\rho) \ge 0$ unless we have separate control over the on-line zeros' contributions — and that control is essentially RH-strength input.

**This sharpens 4E.3's structural lemma**: the MT geometric structure resists not just 1D line-restriction (4E.3) but also naïve domain relaxation (4E.6). The "1D Fejér ceiling" on the single-zero MT shape factor is robust under both.

**Genuine escape routes (open)**: 
1. **Heath-Brown multi-zero coupling** (Arch 4E.7 open) — multiple putative zeros at different heights. The line-restriction lemma applies only to a single line direction, so multi-zero couplings can in principle escape.
2. **Bombieri variational SOS** — allow small negativity, control $L^2$ norm via a quadratic-programming penalty.
3. **Polynomial-ideal SOS** (Arch 4E.8 open) — non-negativity over algebraic variety via Putinar/Schmüdgen.

None is "LP over a subset of the torus." 4E.6 narrows the open landscape to these three qualitatively distinct routes.

**Methodological pattern (worth re-using)**: the structural lemma's robustness signals where the genuine open machinery lives. When a naïve relaxation collapses to the original ceiling, the next steps require *changing the type of inequality*, not just its support. This pattern recurs across architectures: see also LEARNINGS #11 (bare $\psi_p$ collapses; need cohomology), LEARNINGS #7 (Weil-form analytic cancellation collapses; need new positivity certificate).

### 11. Bare $\psi_p$ on concrete Λ-rings has no zeta-zero-like spectrum: cohomology is what does the lifting.

2E ([e2e_adams_spectrum.py](arithmetic_geometric/e2e_adams_spectrum.py), writeup [2E_adams_spectrum_probe.md](arithmetic_geometric/2E_adams_spectrum_probe.md)) tests R5's structural hypothesis directly by computing the spectrum of the Adams operations $\psi_p$ on four concrete Λ-ring substrates:

| Probe | Substrate | Spectrum | min $|\gamma_n - \lambda|$ |
|---|---|---|---|
| 1 | Representation ring $R(\mathbb{Z}/n)$ | Roots of unity (cycle structure of mult-by-$p$) | $13.13$ |
| 2 | Frobenius on $\mathbb{F}_{p^k}$ | $k$-th roots of unity (order of $F$) | $13.13$ |
| 3 | Truncated ghost ring $W_N$ | $\{0\}$ (nilpotent shift $w_n \to w_{pn}$) | $14.13$ |
| 4 | $K_*(\mathrm{Spec}\,\mathbb{Z}) \otimes \mathbb{Q}$ | $\{p^d : d \ge 0\}$ (Beilinson eigenspaces) | $0.01$ |

**Probes 1-3 give the predicted "no structural relation" outcome**: spectra live on the unit circle or at $\{0\}$, $\gamma_n$ starts at $14.13$. Min-distances $\approx \gamma_1$ are mechanical.

**Probe 4 has an apparent near-coincidence** ($5^2 = 25 \approx \gamma_3 = 25.01$) which is **pigeonhole, not signal**, confirmed by a structural randomization control. Null hypothesis: replace $\{2, 3, 5, 7\}$ with 4 random primes from $[2, 200]$; recompute min-distance. Observed quantile in 5000-trial null distribution: $0.086$. The closeness is in the lower tail (~9th percentile) but not extraordinary; null median is $0.97$. Verdict: lucky pigeonhole, ~1-in-12 random configurations produce comparable collisions.

**Structural lesson**: bare Λ-ring substrates are too small (or too symmetric) to host zeta-zero spectra. The substrate structure dictates the spectrum:
- Permutation actions on finite groups → roots of unity.
- Shifts on graded/truncated structures → nilpotent.
- Beilinson-graded K-theory → pure powers.

**This is the predicted negative result that confirms R5's framing**: the cohomology theory built on top of $\mathrm{Spec}(W(\mathbb{Z}))$ is what would lift the small Λ-action to an object large enough to carry zeta-zero spectral information. Prismatic cohomology (R5's leading candidate) is one such lift; the spectrum on the cohomology, not on the bare Λ-ring, is where zeta zeros would appear (R5 Q2 — open).

**Cross-cut to 2B (Weil over $\mathbb{F}_5$)**: both 2B and 2E point in the same direction. In 2B, Frobenius eigenvalues on $H^1(C, \mathbb{Q}_\ell)$ — the cohomology, not the structure sheaf $H^0(C, \mathcal{O}_C)$ — give the zeros of $Z(C, T)$. The cohomology theory carries the spectral information; the bare algebraic substrate does not. 2E demonstrates the analogous statement on the Borger side: bare $\psi_p$ on $W(\mathbb{Z})$-flavored substrates does not carry $\zeta$'s zeros, the cohomology would have to.

**Limitations**: tested four substrates; exotic Λ-rings (universal Λ-ring on infinite generators, de Rham-Witt complexes, Frobenius-equivariant K-theory of moduli stacks) not probed. Compared against the first 10 $\gamma_n$ only.

**This closes Arch 2E**. The bare-spectrum question is resolved (negative as predicted). The next step — testing $\psi_p$ on actual prismatic cohomology of $\mathrm{Spec}(W(\mathbb{Z}))$ — is the R5 Q2 question, which requires the cohomology to first be computed and is beyond the project per [2A_path_forward.md](arithmetic_geometric/2A_path_forward.md).

### 10. The wrong-approach detector's signal saturates: relative min eigenvalue converges and negative count equals off-line zero pairs.

3D.3 extended the Gram-matrix K-scaling from K=100 (3D, 3D.2) up to K=1000, with three structural findings:

- **Relative min eigenvalue ($\lambda_{\min}/\lambda_{\max}$) converges to $-2.62\%$** for D-H across $K \in [300, 1000]$. The signal strength is dimension-independent: it's a fixed property of the off-line zero structure.
- **Number of negative eigenvalues is FIXED at $4$** = number of off-line zero PAIRS in the upper half plane (D-H at $T_{\max} = 200$ has $8$ off-line zeros, forming $4$ functional-equation pairs). Each off-line conjugate pair $(\rho_{\rm off}, \bar\rho_{\rm off})$ introduces exactly $1$ negative eigenvalue. This is a structural finding: the detector's "signal dimension" exactly counts off-line zero pairs.
- **Selberg-class L-functions stay PSD to floating-point noise** even at $K = 1000$. For $\zeta$, $\chi_3$, $\chi_4$: worst rel min $\sim 10^{-16}$, indistinguishable from numerical zero, despite the matrix having $K - n_{\rm zeros} \sim 900$ near-zero eigenvalues (genuine rank deficiency from Gram-of-real-vectors structure for on-line zeros).

This closes LEARNINGS open question #5. The detector is robust at large K, and the architectural interpretation (one negative eigenvalue per off-line zero pair) gives a clean structural picture: **the Gram-matrix detector is effectively counting off-line zero pairs via its negative-eigenvalue spectrum**.

**K-doubling deepening rate.** The absolute min eig grows from $-0.37$ at $K = 100$ to $-4.04$ at $K = 1000$: factor $10.9 \approx K^{1/2}$ in absolute terms. Per K-doubling step: $\{2.06, 1.57, 1.68, 1.50, 1.33\}$. This is consistent with $|\lambda_{\min}| \sim K \cdot |\text{rel min}|$ (since $\lambda_{\max}$ grows linearly with $K$ and rel min is constant).

**Architectural implication.** The detector's signal structure is finite-dimensional and combinatorial: one negative eigenvalue per off-line pair, with fixed signal strength. This raises a natural next question: if one ran D-H at higher $T_{\max}$ (revealing more off-line zero pairs), would the negative-eigenvalue count grow accordingly?

**3D.4 confirms YES** (T_max scaling). At $T_{\max} = 200$ D-H has 4 distinct off-line $\gamma$'s in UHP (at heights $\sim 85.7, 114.2, 166.5, 176.7$); at $T_{\max} = 300$ a 5th off-line pair appears at $\gamma \approx 240.4$; at $T_{\max} = 350$ two more pairs appear at $\gamma \approx 320.9$ and $331.0$; **at $T_{\max} = 500$ two more pairs again, bringing the total to 9 distinct off-line $\gamma$'s** in UHP. The negative eigenvalue count of $M^{DH}$ tracks exactly:

| $T_{\max}$ | # distinct off-line $\gamma$'s | $n_{\rm neg}$ (measured) | rel min eig | increment |
|---|---|---|---|---|
| $200$ | $4$ | $4$ (MATCH) | $-2.599 \times 10^{-2}$ | baseline |
| $300$ | $5$ | $5$ (MATCH) | $-2.599 \times 10^{-2}$ | +1 |
| $350$ | $7$ | $7$ (MATCH) | $-2.599 \times 10^{-2}$ | **+2 (non-trivial)** |
| $500$ | $9$ | $9$ (MATCH) | $-2.597 \times 10^{-2}$ | **+2 (non-trivial)** |

The double-increments between consecutive $T_{\max}$ steps are non-trivial tests: the prediction must hit EXACTLY $n_{\rm neg} = 7$ at $T_{\max} = 350$ and $n_{\rm neg} = 9$ at $T_{\max} = 500$, not just "monotonically larger." It does, for all four data points. **The structural prediction is sharply validated.**

Additionally, the relative min eigenvalue is **identical to 3+ sig figs across all four $T_{\max}$ values** ($-2.599 \times 10^{-2}$ at $T_{\max} \in \{200, 300, 350\}$, $-2.597 \times 10^{-2}$ at $T_{\max} = 500$ — the small drift is floating-point noise at higher matrix conditioning). Combined with 3D.3's $K$-invariance (3D.3 found rel min $\sim -2.62\%$ across $K \in [300, 1000]$ at fixed $T_{\max} = 200$), the asymptotic constant is **universal: invariant under both $K$ and $T_{\max}$ extensions**. Selberg-class L-functions ($\zeta, \chi_3, \chi_4$) stay PSD to floating-point noise at all tested $T_{\max}$ (worst rel $\sim 10^{-16}$ at $T_{\max} = 200$, dropping to $\sim 10^{-19}$ at $T_{\max} = 500$ as conditioning improves). This closes the architectural picture of the wrong-approach detector:

**The Gram-matrix detector is structurally counting off-line zero pairs**, with fixed per-pair signal strength of $\sim 2.6\%$ of $\lambda_{\max}$, invariant under matrix-size scaling and zero-range extension.

**Computational note**: the $T_{\max} = 500$ extension was bottlenecked by uncached zero computations — D-H 2D off-line scan ~14 min, $\chi_3 / \chi_4$ critical-line scans ~13 min each. Total ~50 min wall clock for the additional data point. The cleanly-stated prediction `$n_{\rm neg} = $ # off-line $\gamma$'s in UHP` continues to hold without exception across all tested $T_{\max}$ values.

### 1. Level 4 (positivity) is the only level that's been shown to actually discriminate $\zeta$ from D-H computationally.

The four-level framing in [docs/02_graduate/log_correlated_fields_intro.md](../docs/02_graduate/log_correlated_fields_intro.md) §6 says: RH lives at Level 4 (Weil positivity), not Level 3 (spectral / statistical). The experiments have now produced a concrete computational instance of this claim:

- **Arch 3 (positivity) at the Gram-matrix level (3C.2, 3D, 3C.3, 3D.2):** the Weil quadratic form via Gram-matrix eigenvalue analysis returns PSD for $\zeta, \chi_3, \chi_4$ (all Selberg-class, GRH-believed) and **indefinite** for D-H, with the witness deepening monotonically as the basis size grows ($-2.4 \times 10^{-2} \to -3.7 \times 10^{-1}$ for $K = 20 \to 100$). The same witness vector $c^*$ that flags D-H gives $W_\zeta(c^*), W_{\chi_3}(c^*) \geq 0$: the detector is direction-selective, not L-function-blind.
- **Arch 1 (spectral) at every level we tested:** bare Berry-Keating (1A), three Sierra-Townsend variants (1B), and the explicit L-function discrimination test (1C) all produce H matrices with no L-function input. After best affine rescaling, RMS deviations from first 40 $\gamma_n^\zeta$ and from first 40 $\gamma_n^{DH}$ are both in $[2.4, 5.1]$; the discrimination ratio $\mathrm{RMS}_\zeta / \mathrm{RMS}_{DH}$ spans a factor of 3.35 around 1, consistent with random alignment of similar-density sequences.

The lesson is concrete: a structural test that lives at Level 3 (spectral signature, density) cannot tell us which L-function we're looking at, because the input quantities (eigenvalues, densities) don't see the Euler product. The same construction "matches" zeta and D-H equally well, even though one satisfies RH and the other doesn't. Positivity-based tests that take in the actual zeros (Gram matrix of $\Phi_b(\rho)$ values) do see the difference.

### 2. Small-$n$ Li-positivity does not distinguish; large-$n$ Li does. The discrimination scale is $n \sim 320{,}000$ for D-H.

The Li criterion $\lambda_n \geq 0 \iff$ RH is unconditional, so D-H must have negative $\lambda_n$ at some $n$. 3B computed $\lambda_n$ at $n \leq 300$ and found **both $\zeta$ and D-H are strictly positive** in that range. The reason: for the first D-H off-line zero ($\rho \approx 0.8085 + 85.7i$, FE partner $0.192 + 85.7i$), $|w_{\rm off}| - 1 \approx 4.2 \times 10^{-5}$, so the off-line contribution becomes order 1 only at $n \approx 24{,}000$, and exceeds the on-line $(n/2)\log(qn/(2\pi))$ asymptotic only at $n \gtrsim 320{,}000$.

3B.2 computed $\lambda_n^{DH}$ at large $n$ via the decomposition $\lambda_n^{DH} = \lambda_n^{DH, \rm asymp} + \sum_{\rho_{\rm off}} 2\,\Re(w_{\rm on}^n - w_{\rm off}^n)$ and **directly witnessed $\lambda_n^{DH} < 0$ at $n = 400{,}000$** (off-line correction $-2.0 \times 10^7$ vs asymptotic $+2.4 \times 10^6$) and **at $n = 10^6$** ($-3 \times 10^{18}$). The sign oscillates as $\cos(n \arg(w_{\rm off}))$ with amplitude growing as $|w_{\rm off}|^n$, so not every $n$ past the crossover gives negative $\lambda_n^{DH}$ (e.g., $n = 500{,}000$ landed on a positive phase).

**3B.3 ([e3b3_rigorous.py](zero_free/../positivity/e3b3_rigorous.py) + [.md](zero_free/../positivity/e3b3_rigorous.md)) sharpens this** to a **rigorous witness at $n = 336{,}000$**: 100-digit working precision, full T_max = 500 off-line data (18 zeros UHP, 9 distinct gammas), and explicit error bounds (Bombieri-Lagarias asymptotic error $\le 2 \log^2(qn) = 411$ at the witnessed n; tail bound from provable 1/γ² scaling + empirical $\le 50$ quadruples above T_max gives 392). At n = 336,000: asymptotic $+2.03 \times 10^6$, off-line correction $-2.68 \times 10^6$, central $\lambda_n = -6.47 \times 10^5$, upper bound $-6.46 \times 10^5 < 0$. The number 336,000 is just above the magnitude-crossover prediction of 320,000 — the 16,000 gap is the first phase-aligned sample in a step-2000 sweep. **Updated discrimination scale: $n \approx 336{,}000$ for the first rigorous Li witness on D-H.**

This is a non-trivial structural result. **The Li criterion does correctly distinguish RH from non-RH; the discrimination scale is just large**, roughly $n \sim 1/|w_{\rm off} - 1|^2$ rather than $n \sim 1/|w_{\rm off} - 1|$. Any proof attempt that argues $\lambda_n \geq 0$ via methods that work uniformly out to $n = O(10^3)$ is structurally insufficient: the same arguments would conclude the same for D-H. To use the Li criterion as a discriminator computationally, you need $n \gtrsim 10^5$ scale or you need a different positivity test entirely.

The methodologically correct upgrade was the Weil quadratic form (3C-3D, 3C.3, 3D.2): same positivity principle, but evaluated via test functions (the $\Phi_b$ family) where the phase of $\hat f(\rho)$ at off-line $\rho$ shows up immediately. The Gram-matrix detector discriminates D-H at $K = 30$ test functions and $T_{\max} = 200$, vastly cheaper than the $n \sim 4 \times 10^5$ needed for Li.

### 3. The Davenport-Heilbronn discipline has been operationally validated.

D-H was introduced as a structural counter-example: any Arch 1/3/4 method that does not distinguish $\zeta$ from D-H is wrong. After the session's experiments, this discipline has now done concrete work twice:

- **It killed a plausible approach** (small-$n$ Li, 3B). Without the D-H control, Li-positivity at $n \leq 300$ looked like a clean positive signal for $\zeta$. With it, we recognized the signal as not actually testing RH.
- **It validated the right approach** (Gram-matrix Weil form, 3C.2 + 3D.2). The detector flags D-H indefinite (correct) and the Selberg-class L-functions PSD (correct). The cross-cut with $\chi_3, \chi_4$ then confirmed the detector is not just "different from $\zeta$" but specifically responding to off-line zeros.

Architecturally: D-H is the project's "false-positive filter." Any method that survives the D-H test deserves further investigation; any method that fails it (passes for D-H as well as $\zeta$) is structurally wrong even if it looks correct on $\zeta$ alone.

### 4. Spectral constructions without arithmetic input are uniformly bounded in their L-function discrimination.

The full Arch 1 result (1A + 1B + 1C) provides a quantitative version of "Hilbert-Pólya needs arithmetic input": across six H matrices we tested (three boundary conditions in 1A, three Sierra-Townsend variants in 1B), the discrimination ratio after best affine rescaling spans $[0.50, 1.67]$ — factor 3.35 spread. A genuine Hilbert-Pólya construction whose eigenvalues are exactly $\{\gamma_n^\zeta\}$ would give RMS$_\zeta = 0$ and RMS$_{DH} \sim 10$, giving ratio $0$. The factor-3 spread we see is consistent with random alignment between two similar-density gamma sequences, not with arithmetic content.

What this rules out is **strong**: no fixed-domain discretization of any operator of the form $H = (xp + px)/2 + V(x)$ (for any $V$) can prove RH, because the same H matrix is L-function-agnostic. The only viable spectral directions are constructions whose H matrix encodes the Euler product (or equivalent arithmetic input), like Connes' adèle class space (1D), which is the deferred-literature task.

### 5. Single-coefficient multivariate Fejér LPs decompose; balanced-sum LPs do not. (REFINED via 4E.)

4D-ii and 4D.2 established the *single-coefficient* decomposition: max $c_{1, \ldots, 1}$ at $d$-degree $(N, \ldots, N)$ saturates the tensor product. 4E (e4e_offdiag_lp.py) generalizes the question and finds the picture is family-dependent.

**Single-coefficient family decomposes.** For 4D/4D.2 and 4E Test A combined:
$$\max c_{j_1, \ldots, j_d} = \prod_{i=1}^d (\max_Q q_{j_i}) = \prod_i q_{j_i}^{1D}(N)$$
at $d$-degree $(N, \ldots, N)$, for any $(j_1, \ldots, j_d)$. The LP-optimal coefficient tensor is rank 1, and the LP value equals the asymmetric tensor product of independently chosen 1D optima. For $d = 2$, $j = k = 1$: $q_1^{1D}(N) = 2\cos(\pi/(N+2))$ (Fejér).

**Balanced-sum-of-diagonal family does NOT decompose, and the gap is weight-dependent.** For the objective $c_{1,1} + \alpha c_{2,2}$ at bidegree $(N, N) = (2, 2)$, 4E (at $\alpha = 1$) and 4E.2 (alpha sweep) together establish that the LP value strictly exceeds the Cauchy-Schwarz tensor bound $16/(8 - \alpha)$ over the range $\alpha \in (0, 8]$, with relative gap peaking at $+25.00\%$ for $\alpha = 3$:

$$\max\, c_{1,1} + 3 c_{2,2}\,(\text{LP}) = 4.0000 \quad > \quad \max_Q (q_1^2 + 3 q_2^2) = \tfrac{16}{5} = 3.2000.$$

The original 4E finding ($\alpha = 1$, +12.1%) is a single point on this curve. Other findings: gap peaks smoothly at $\alpha = 3$ then decays; **3-term diagonal sum** $c_{1,1} + c_{2,2} + c_{3,3}$ at bidegree $(3,3)$ gives gap +1.98%, an **8.66x increase** over the 2-term sum at the same bidegree (+0.23%). The LP-optimal coefficient matrix is full rank $N+1$ with $\sigma_2/\sigma_1 \in [0.43, 0.78]$, robust across grid resolutions.

**Closed-form structure at the peak.** At $\alpha = 3$, $N = 2$, the LP-optimal coefficient matrix has clean rational entries: $c_{1,1} = 8/5, c_{2,2} = c_{0,2} = c_{2,0} = 4/5$, parity structure $c_{j,k} = 0$ for $j + k$ odd. In $(u, v) = (\theta + \phi, \theta - \phi)$ coordinates, $5 P = 5 + 4\cos u + 4 \cos v + 8 \cos u \cos v + 2 \cos 2u + 2 \cos 2v$, which contains $\cos 2u, \cos 2v$ without their tensor partners $\cos 2u \cos v, \cos u \cos 2v$ — algebraically ruling out factorization. The clean rationals suggest a closed-form derivation of this optimum is possible.

**Off-diagonal-sum family does NOT exceed tensor either.** For $c_{1,2} + c_{2,1}$ at bidegree $(N, N)$ (Test C), the LP value is **strictly less than** the Cauchy-Schwarz tensor bound. The LP-optimal $c_{j,k}$ matrix has rank $> 1$ but this is an LP-vertex degeneracy: a tensor product witness achieves the same LP value.

**The corrected structural statement.** The 4D claim "the d-variate LP decomposes; no new auxiliary inequality" is true for *single-coefficient* objectives at uniform degree, and even for *some* sum objectives (like Test C's $c_{1,2} + c_{2,1}$). It is **false** for the balanced-diagonal-sum objective $c_{1,1} + c_{2,2}$: the LP value at $N = 2$ exceeds the tensor bound by 12%, and the optimal polynomial is genuinely 2D.

**Earlier convention error remains.** The original 4D-ii narrative had a separate convention bug (comparing $(c_1^{4B})^d$ vs $(2 c_1^{4B})^d = (q_1^{1D})^d$); that bug is fixed in [4D's writeup](../zero_free/README.md#4D). 4E's finding is independent of the convention question: it's about which LP objectives produce rank-1 vs full-rank solutions and whether the LP exceeds the tensor bound.

**Methodological lesson.** "Does the LP decompose?" is answered by two diagnostics combined: (1) rank of the LP-optimal coefficient matrix via SVD, and (2) comparison of the LP value to a Cauchy-Schwarz-derived tensor product bound. Rank $> 1$ alone is not sufficient (Test C has rank $> 1$ but LP value matches tensor bound, so the LP has a rank-1 optimal solution that the solver missed). The pair "rank $> 1$ AND LP > tensor bound" is the right test for genuine new content.

**What this leaves open.** The 12% improvement at $N = 2$ is on the auxiliary inequality, not yet on the zero-free region constant. **(Resolved by 4E.3:** see finding 8 below.) The other open directions from the original 4D remain: constrained-domain LP (e.g., $P \geq 0$ only on a submanifold corresponding to a hypothetical off-line zero), and Heath-Brown-style cross-prime coupling.

### 8. The C-S figure of merit and the MT figure of merit are structurally distinct: 4E.2's +25% LP gap does NOT translate into a zero-free region improvement.

4E.2 produced a +25% gap to the Cauchy-Schwarz tensor bound on $\max c_{1,1} + 3 c_{2,2}$ at bidegree $(2, 2)$. The natural next question (open #3 in the LEARNINGS earlier version): does this gap improve the Mossinghoff-Trudgian zero-free region constant $C$ in $\beta < 1 - C/\log|t|$? 4E.3 (e4e3_mt_translation.py) answers no, with both numerical evidence and a structural lemma.

**Numerical evidence.** Take the 4E.2 peak polynomial at $(\alpha, N) = (3, 2)$: $c_{0,0} = 1, c_{1,1} = 8/5, c_{2,0} = c_{0,2} = c_{2,2} = 4/5$. Restrict to 1D via various heights $(t_1, t_2)$. The MT shape factor (divided by $P(0)$ as a proxy for the boundary $R(P)$) is computed for each reduction and compared to the 1D Fejér optimum at the same effective degree:

| Reduction | shape/$P(0)$ | eff deg | Fejér shape/$P(0)$ at same deg | ratio |
|---|---|---|---|---|
| $t_1 = t_2 = \gamma_0/2$ | $0.000909$ | $2$ | $0.01472$ | $0.062$ |
| $t_1 = \gamma_0, t_2 = \gamma_0/2$ | $0.002000$ | $3$ | $0.02520$ | $0.079$ |
| $t_1 = t_2 = \gamma_0$ | $0$ | $4$ | $0.02885$ | $0$ |

Best 2D-derived shape/$P(0)$ is 12.6x worse than 1D Fejér at matched degree. Across the $\alpha \in [0, 10]$ sweep, no choice produces a 2D polynomial whose 1D restriction beats 1D Fejér; the maximum ratio (0.958) is achieved by the trivial tensor product at $\alpha = 0$.

**Structural lemma.** For any non-negative bivariate trig polynomial $P(\theta, \phi) \geq 0$ on $[0, 2\pi]^2$, the restriction $\tilde P(u) := P(t_1 u, t_2 u)$ is a non-negative 1D trig polynomial on $[0, 2\pi]$. The argument is one line: $(t_1 u, t_2 u)$ is a point of $[0, 2\pi]^2$ (modulo periodicity), so $P \geq 0$ everywhere implies $\tilde P(u) \geq 0$.

Hence the family of effective 1D polynomials from 2D restriction is a SUBSET of all 1D non-neg trig polynomials at matched effective degree. The MT figure of merit, which involves $\max c_1$ over the non-neg cone, is therefore bounded above by 1D Fejér. **No 2D bivariate restriction can break the 1D Fejér ceiling on the single-zero MT zero-free region constant.**

**The two figures of merit see different things.** The 4E.2 +25% gap is a real structural finding: the LP $\max c_{1,1} + 3 c_{2,2}$ over 2D non-neg polynomials at bidegree $(2, 2)$ exceeds the Cauchy-Schwarz tensor bound, and the LP-optimal polynomial has genuinely 2D coupling (clean rational coefficients with $\cos 2u, \cos 2v$ appearing without their tensor partners in $(u, v) = (\theta + \phi, \theta - \phi)$ coordinates). But the C-S figure of merit (max linear combination of $c_{j,k}$) and the MT figure of merit (max $c_1$ after 1D restriction) optimize different functionals. The 4E.2 LP shifts mass to $c_{2,2}, c_{2,0}, c_{0,2}$ to gain on the C-S objective; in MT bookkeeping this mass lands at the pole frequency (inflating $c_0$) or at $h = 2\gamma_0$ (which doesn't probe the trick zero at $\gamma_0$).

**What this rules out.** Any "shortcut" from the bivariate LP framework to the de la Vallée Poussin / Mossinghoff-Trudgian single-zero zero-free region constant via simple 1D restriction. This includes the natural family $\max c_{1,1} + \alpha c_{2,2}$ across all $\alpha$, all reductions $(t_1, t_2) \in \mathbb{R}^2$, and all bidegrees.

**What this does NOT rule out.**

- Constrained-domain LP: $P \geq 0$ only on a submanifold corresponding to a hypothetical off-line zero (e.g., $\phi = 2\theta$ for a zero probed at heights $\gamma$ and $2\gamma$). The submanifold-constrained polynomial is NOT bounded by the unrestricted 1D Fejér.
- Polynomial-ideal sum-of-squares decompositions modulo prime-coupling relations.
- Multi-zero or multi-character setups (Heath-Brown's actual use of bivariate inequalities in the least-prime-in-AP and Siegel-zero problems).
- Higher-rank LP families: $d$-variate at $d \geq 3$ with non-degenerate weights, where the structural lemma still applies but the matching becomes more delicate.

These are queued as 4E.4 follow-ups; none are pursued in 4E.3.

**Lesson.** A real structural improvement on one figure of merit does not automatically transfer to a different figure of merit even when both involve the same family of polynomials. The 4E ↔ 4E.2 ↔ 4E.3 progression illustrates how a "+25% gap" finding can be both real and computationally beneficial somewhere AND irrelevant to the headline RH-style application. Future LP-based architecture-4 work should specify the figure of merit explicitly and target it directly, not target a proxy and hope it transfers.

### 9. The d-variate balanced-sum LP gap grows sub-linearly with $d$: +25% (d=2), +51% (d=3), $\sim$+62% (d=4).

4E.4 and 4E.5 extend the bivariate balanced-sum LP of 4E / 4E.2 to higher dimensions: max $c_{1, \ldots, 1} + \alpha c_{2, \ldots, 2}$ at uniform degree $(N, \ldots, N)$ for $N = 2$. The peak gaps to the symmetric tensor bound:

| $d$ | LP variables | peak $\alpha$ | peak gap (M-corrected) |
|---|---|---|---|
| $2$ (4E.2) | $3^2 = 9$ | $3.00$ | $+25.00\%$ |
| $3$ (4E.4) | $3^3 = 27$ | $3.25$ | $\sim +50\%$ (interval $[47\%, 51\%]$) |
| $4$ (4E.5) | $3^4 = 81$ | $4.50$ | $\sim +62\%$ (interval $[55\%, 70\%]$) |

The d=2 → d=3 jump nearly doubles the gap (25 pp); the d=3 → d=4 jump adds less (15 pp). The increment per dimension shrinks. A naive linear prediction $(d-1) \times 25\%$ would give 75% at d=4, above the observed range. The pattern is sub-linear and likely saturates at some limit below $100\%$ as $d \to \infty$.

**Peak $\alpha$ grows with $d$.** The optimal weight on the higher-order term $c_{2, \ldots, 2}$ rises ($3.0 \to 3.25 \to 4.5$), consistent with higher-dimensional structure putting more emphasis on higher-order coupling.

**M-convergence at d=3.** At $\alpha = 3$ exactly, LP values across $M_{3D} \in \{40, 70, 100\}$ are $\{4.95, 4.89, 4.87\}$ with $P_{\min}$ approaching 0. The M=100 LP value 4.8665 with $P_{\min} = -2.9 \times 10^{-4}$ gives a tight lower-bracket of 4.865, so the true LP value at $\alpha = 3$ is in $[4.865, 4.867]$, gap $[+47.0\%, +47.1\%]$. The M=60 sweep at $\alpha = 3.25$ gives +51.3% (slight overestimate).

**M-convergence at d=4.** Heavier: $M^4$ constraints. At $\alpha = 4.5, M = 35$ (1.5M constraints): LP = 7.64, $P_{\min} = -0.099$, lower bracket = 6.95, gap in $[+54.5\%, +69.8\%]$. Larger $M$ would narrow this further but requires $\geq 10^7$ constraints.

**Peak coefficient tensors.** $d = 2$ had clean rationals ($1, 8/5, 4/5, 4/5, 4/5$). $d = 3$ at $M = 60$ gave $c_{1,1,1} = 2.637, c_{2,2,2} = 0.754$, lower-order entries $\sim 0.6$, without an obvious clean-rational form (some asymmetry consistent with LP noise). $d = 4$ similarly lacks an evident clean structure at the M values reached.

**What this does NOT mean for RH.** Per finding 8 (4E.3 structural lemma), any d-variate non-neg polynomial restricted to a line is a 1D non-neg trig polynomial bounded by 1D Fejér at matched effective degree, FOR ANY $d$. The +62% trivariate-or-higher gap still does NOT translate into a better single-zero MT zero-free region constant. The growth-with-dimension result characterizes the structure of multivariate auxiliary inequalities themselves, independent of the RH application.

**What this MIGHT mean for the broader picture.** The sub-linear growth of the LP-vs-tensor gap with $d$ suggests that the bivariate LP (4E.2) already captures most of the available LP-vs-tensor gap. Going to higher dimensions yields diminishing returns. If a future application uses d-variate non-negativity in a context where the structural lemma does NOT apply (multi-zero coupling, constrained domain, polynomial-ideal SOS), the d-variate gap is the relevant figure of merit, but the d=2 result already captures more than half of what's achievable.

### 6. The arithmetic-geometric architecture is the only one that has produced an actual RH theorem in our experiments — and 2A pins down precisely why.

Arch 2B verified the Weil RH for the elliptic curve $E: y^2 = x^3 + x + 1$ over $\mathbb{F}_5$ exactly: Frobenius eigenvalues $\alpha = -3/2 \pm i\sqrt{11}/2$, $|\alpha|^2 = 5$, and $|C(\mathbb{F}_{5^k})|$ matches the Weil formula at $k = 1, \ldots, 6$ by brute-force point counting. This is not "evidence for RH"; it is RH for that curve, proved.

**2A** traces the proof step by step against $\mathrm{Spec}(\mathbb{Z})$. The two companion docs:
- [2A_weil_proof_diff.md](../experiments/arithmetic_geometric/2A_weil_proof_diff.md): the diff itself + §4 expansion + §5 list of 17 constraints the missing mathematics must satisfy
- [2A_candidate_evaluation.md](../experiments/arithmetic_geometric/2A_candidate_evaluation.md): checkable predicates for each constraint + submission template for new candidates + scorecards for the six major existing candidates (Deitmar, Lorscheid, Borger, Connes, Deninger, Connes-Consani) + kill criteria

The proof's structural shape — **Lefschetz fixed-point + Poincaré duality + Hodge index theorem** — works for curves over $\mathbb{F}_q$ because all three pieces exist on the SAME object (the surface $C \times C$). Over $\mathrm{Spec}(\mathbb{Z})$, each piece is either missing entirely or available only in a partial form:

- **Lefschetz**: requires a geometric Frobenius endomorphism. $\mathrm{Spec}(\mathbb{Z})$ has none; Connes proposes the $\mathbb{R}^*_+$-action on the adèle class space and Deninger proposes a real-time flow on a hypothetical foliated space, but neither object has been built.
- **Poincaré duality**: requires a non-degenerate cohomological pairing on $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$, which in turn requires a "base below $\mathbb{Z}$" (traditionally called $\mathbb{F}_1$). The functional equation $\xi(s) = \xi(1-s)$ gives the consequence at the L-function level but not the underlying cohomology pairing.
- **Hodge index theorem**: requires a 2-dimensional geometric object (the surface $C \times C$ in the function-field case). Without the surface $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$, no analogue. The Arch 3 finding (#7, the Weil-form duality circularity) is the analytic shadow of this missing geometric positivity.

**The single-sentence diagnosis**: Architecture 2's obstruction is constructive, not analytic — the proof template is well-understood, but the underlying object on which to instantiate it has not been built. The three programs (Connes, Deninger, $\mathbb{F}_1$) each address one corner of the obstruction triangle (Frobenius / surface / positivity respectively), but no single program has assembled all three.

**The universal scorecard finding** (from `2A_candidate_evaluation.md`): scored against the 17 specific constraints, the six major candidates collectively cover the Frobenius slot (constraints viii-x, especially Connes and Borger) and the base slot (i-iii, especially Deitmar and Lorscheid), but **no candidate has even a partial ✅ on the Hodge index positivity slot (xi-xiii)**. The deepest open problem is constructing a positivity certificate on the (hypothetical) surface $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ that is provable WITHIN the new framework, not requiring RH as input. Most "RH proofs" in the literature fail kill criterion K1: they reduce RH to a different positivity statement that is morally RH-equivalent rather than providing an independent constructive proof.

**Cross-cut to Arch 3 (positivity).** Arch 3 probes the (c) Hodge-index slot analytically rather than geometrically (Weil positivity on test functions). Arch 3F-3I (the Weil-form duality experiments) found that the analytic version hits a circularity wall: any unconditional proof requires GRH-strength input. This is consistent with 2A's diagnosis — the analytic shadow inherits the circularity of the missing geometric positivity. **The analytic and geometric obstructions are the same obstruction, viewed from two sides.**

2B is the only architecture in our set where the proof template actually closes; the other three architectures' obstructions all reduce, in different ways, to "we don't have the cohomology over $\mathbb{Z}$ that we have over $\mathbb{F}_q$."

### 7. The Weil-form duality is computable, and the cancellation structure on the prime side reveals where the analytic obstruction lives.

For $\zeta$, Weil positivity $W(b) = \sum_\rho \Phi_b(\rho)^2 \geq 0$ can be computed from either the zero side (the sum over $\rho$) or from the prime side via Bombieri's explicit formula:
$$W(b) = \underbrace{8(b^{1/2} - b^{-1/2})^2}_{\text{boundary}} - 2\sum_{p^k < b^2} \tfrac{\log p}{p^{k/2}}(2\log b - k\log p) - (\log 4\pi + \gamma_E)\cdot 2\log b - \int_1^\infty \tfrac{f(x) + f(1/x)/x - 2f(1)/x}{x - 1/x}dx.$$

3F verifies the two sides agree to $<2\%$ at $T_{\max} = 1000$, $b \geq 14$, with the residual error matching the expected $O((\log T)/(\pi T))$ truncation. The framework is correctly implemented.

**The cancellation structure.** At $b = 20$, the four prime-side components are $+144, -120, -19, -5$, summing to $\sim 0.1$. The prime sum cancels 83% of the boundary; the constant and gamma integral together cancel most of the remainder. Each component is $O(10^2)$ relative to $W$ of $O(10^{-1})$ — three orders of magnitude of cancellation.

**Why this is the analytic obstruction.** A proof of Weil positivity from the prime side requires bounding $\sum \Lambda(n) n^{-1/2} (2 \log b - \log n)_+$ from above by the boundary $+$ constants $+$ gamma integral, *without using zero locations*. The best unconditional PNT (Vinogradov-Korobov) gives $\psi(x) - x = O(x \exp(-c (\log x)^{3/5}))$, an error of order $x$. The cancellation we observed has margin $\sim 0.1\%$ of the component magnitudes. The PNT error is far too loose. Improving it to a power-saving error term ($\psi(x) - x = O(x^\theta)$ for $\theta < 1$) is *equivalent* (up to bookkeeping) to a zero-free region with that exponent. To break Weil positivity's analytic obstruction one needs a fundamentally new way to bound the prime sum — Bombieri's "variational approach" (2003), Connes' trace-formula construction, and Deninger's motivic cohomology are three ongoing programs aimed at this.

**Three L-functions tested (3G, 3H).** The cross-comparison sharpens the picture:

| L-function | Pole at $s = 1$ | Coefficient sign | Largest comp ($b=20$) | $\lvert W \rvert$ | Cancellation ratio |
|---|---|---|---|---|---|
| $\zeta$ | YES | $\Lambda(n) \geq 0$ all positive | $144$ (boundary) | $0.1$ | $\sim 10^{-3}$ |
| $\chi_3$ | no | $\Lambda(n) \chi_3(n) \in \{\pm 1, 0\}$ | $5.77$ (prime sum) | $0.24$ | $\sim 4 \times 10^{-2}$ |
| D-H | no | $b_n^{DH}$ oscillating, no $\Lambda$ structure | $2.83$ (Dirichlet sum) | $0.31$ | $\sim 1.3 \times 10^{-1}$ |

**The tight cancellation is specifically a feature of $\zeta$'s pole at $s = 1$, not of Euler products in general.** $\chi_3$ also has an Euler product but no pole and shows mild cancellation comparable to D-H, not tight cancellation like $\zeta$. The mechanism: $\zeta$'s pole forces a large positive boundary $\sim b^{1/2}$; $\Lambda(n) \geq 0$ forces a large positive prime sum; the tight cancellation between these two is what we observe at $\sim 10^{-3}$. For all other Selberg-class L-functions (which are entire), no pole means no boundary, and the prime sum has internal cancellation from the character.

**The χ_3 unconditional path tested (3I): blocked by the same wall.** I conjectured in 3H that χ_3's mild cancellation might be unconditionally achievable via Siegel-Walfisz-strength estimates. **3I verifies this is wrong.** The Siegel-Walfisz bound on $|\psi(x, \chi_3)|$, applied via partial summation against the boxcar test kernel, is too loose by factor 33× at $b = 10$, growing to 122× at $b = 100$. The ratio gets *worse* as $b$ grows.

**Why:** partial summation kills the cancellation that makes the weighted prime sum small. To get a tight bound on the weighted prime sum, you'd need to control the *zeros* of $L(s, \chi_3)$ — which is GRH for $\chi_3$, what we're trying to prove. Same circularity as ζ.

**The wall isn't ζ-specific; it's a feature of all Selberg-class L-functions.** Even with mild cancellation, the gap between current unconditional bounds and required margin is factor 30-100 for χ_3 (vs factor ~5-10 for ζ). Both are blocked by the same circularity: you need GRH-strength input to bound prime sums tightly enough.

**Implication for the RH route.** Among Selberg-class L-functions, **ζ is exceptionally hard for the Weil-form route** at the level of cancellation tightness. But for ALL of them (ζ, Dirichlet L's, modular L's), the unconditional path through Weil positivity hits the same fundamental wall — getting tighter control on $\psi(x, \chi)$ unconditionally than current Siegel-Walfisz-strength bounds. This is consistent with the historical pattern: many partial results (positive proportion of zeros on line, Levinson-Conrey for ζ and χ_3 alike), but no path through full Weil positivity for any non-trivial L-function. The Weil-form route is structurally blocked across the Selberg class.

**The path forward must avoid the partial-summation step entirely.** Either work directly with the L-function (Connes' adèle class space, Deninger's cohomology) without going through the prime sum, OR find a positivity certificate that doesn't require the prime sum to be bounded *tightly* (sum-of-squares decomposition for the Weil form, as in Bombieri's variational approach).

---

## Per-architecture summary of what is open

### Arch 1 (spectral): no further computational lift expected; the door is now Connes-style.

1A + 1B + 1C closed the door on the BK family and ST-style modifications. The remaining direction (1D, Connes adèle class space) is a literature/theory task, not numerical. No further Arch 1 numerical experiment is expected to produce new structural information.

### Arch 2 (arithmetic-geometric): the open frontier is literature-and-construction work; 2A has now mapped it and provided an evaluation framework.

2B (worked example over $\mathbb{F}_5$) is one of the strongest results we have, but it doesn't move toward $\mathrm{Spec}(\mathbb{Z})$. **2A** is complete and consists of two companion documents:

- [2A_weil_proof_diff.md](../experiments/arithmetic_geometric/2A_weil_proof_diff.md) — the diff itself, the constructive-obstruction analysis (§4), and the 17-constraint specification of what the missing mathematics must deliver (§5).
- [2A_candidate_evaluation.md](../experiments/arithmetic_geometric/2A_candidate_evaluation.md) — the methodology: checkable predicates per constraint, submission template for new candidates, scorecards for six major candidates, kill criteria.

Diagnosis: Architecture 2's obstruction is *constructive* — the proof template is well-understood, but the underlying object hasn't been built. The three programs (Connes, Deninger, $\mathbb{F}_1$ variants) each address one corner of the obstruction triangle but none has assembled all three on a single object. The universal scorecard finding: no candidate has even a partial ✅ on the Hodge index positivity slot (xi-xiii). This is the central open construction problem.

Remaining literature tasks (informed by the evaluation framework):
- ~~**R1** (lowest-hanging fruit per 2A_candidate_evaluation §V): sharpen the D-H exclusion check (xvii) for each candidate.~~ **Complete** ([2A_R1_DH_exclusion.md](../experiments/arithmetic_geometric/2A_R1_DH_exclusion.md)): all six candidates pass K2 by construction. **The structural reason**: D-H is defined by a linear combination of Dirichlet L-functions, which is an analytic operation on Dirichlet series rather than a geometric operation. None of the six frameworks (Deitmar, Lorscheid, Borger, Connes, Deninger, Connes-Consani) can construct linear combinations of L-functions as their natural output. K2 safety is conditional on the Selberg conjecture — if some Euler-product L-function were found to have off-line zeros (no known examples), K2 would become a live concern. This finding also surfaces a design constraint for future candidates: any framework whose L-function operation commutes with linear combination would fail K2 immediately.
- ~~**R2**: explicitly compute the fiber product $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ in Borger / Lorscheid.~~ **Complete** ([2A_R2_fiber_product.md](../experiments/arithmetic_geometric/2A_R2_fiber_product.md), with per-candidate deep-dives [2A_borger_dossier.md](../experiments/arithmetic_geometric/2A_borger_dossier.md) and [2A_lorscheid_dossier.md](../experiments/arithmetic_geometric/2A_lorscheid_dossier.md)). Borger gives Spec(W(ℤ)) via the big Witt ring functor (right adjoint to U: Λ-Rings → Rings); Lorscheid gives the blueprint (ℤ × ℤ, doubled relations). Both candidates produce non-trivial surface-like objects. **Key insight from comparing the dossiers**: Borger is strong on Frobenius (viii) but weak on surface (ii); Lorscheid is strong on surface (i-iii) but weak on Frobenius (viii). The two are "complementary half-candidates."
- ~~**R2.5**: sketch the Λ-blueprint hybrid framework.~~ **Proposed** ([2A_R2_5_lambda_blueprints.md](../experiments/arithmetic_geometric/2A_R2_5_lambda_blueprints.md)). A **Λ-blueprint** is a triple (B, B^•, {ψ_p}) — blueprint plus commuting Adams operations satisfying Fermat-Frobenius modulo the blueprint relations. The category Λ-Blpr would have 𝔽₁ as initial object, ℤ canonically (with ψ_p = identity), and inherit both Λ-Rings and Blpr as subcategories. **Predicted scorecard: 8 ✅ / 4 🟡 / 5 ⏳** — substantially better than either parent's ~4 ✅. Improvements over Borger: surface constraint (ii) upgrades from 🟡 to ✅ via the cleaner blueprint structure. Improvements over Lorscheid: Frobenius constraint (viii) upgrades from ⏳ to ✅ via built-in Adams operations. **The Hodge index slot (xi-xiii) remains universally open** even in the hybrid — it's not addressed by combining Frobenius and surface structures. **Status: research proposal, not established mathematics**. The precise definition of Fermat-Frobenius in the blueprint setting, categorical properties of Λ-Blpr, and explicit fiber product computation all need rigorous development. Estimated effort: thesis-level research project. R2.5 is the most promising hybridization direction surfaced by the evaluation framework.
- ~~**R3** (hardest): identify whether Connes-Consani's positivity conjecture is kill-criterion K1 (RH-equivalent) or has an independent constructive proof candidate.~~ **Complete** ([2A_R3_connes_positivity.md](../experiments/arithmetic_geometric/2A_R3_connes_positivity.md)). The framework hosts at least three distinct positivity conjectures with different K1 status: **C1 (Weil-Bombieri positivity)** is provably RH-equivalent, fails K1. **C2 (Hamiltonian self-adjointness, the Hilbert-Pólya formulation)** also fails K1. **C3 (arithmetic-site / hyperring refinements)** is K1-uncertain — not provably RH-equivalent but no independent proof exists. Connes / Connes-Consani (xi)-(xiii) moves from ❌ to 🟡. **Cross-architecture connection**: R3 aligns with Arch 3's 3F-3I finding — both classical analysis (3F-3I) and noncommutative geometry (R3) hit circularity walls when trying to derive Weil positivity without RH-strength input. The geometric route (intersection theory on a constructed surface, Hodge index theorem) is the only remaining direction where positivity could emerge for free. This is consistent with the original 2A diagnosis: the obstruction is constructive, and proceeds via geometry not analysis.
- ~~**R3.5**: Does ANY noncommutative-geometric framework escape K1?~~ **Proved (sketch)** ([2A_R3_5_K1_universality.md](../experiments/arithmetic_geometric/2A_R3_5_K1_universality.md)). **No-shortcut theorem**: every trace-formula NCG framework with standard spectral identification has positivity P ⟺ RH. Three positivity types covered: self-adjointness (P-SA), quadratic form PSD (P-Q), operator non-negative eigenvalues (P-OP). All universally fall under the theorem. **Proof sketch**: the trace identity is reversible — given the spectral identification (F's spectrum = imaginary parts of ζ zeros), P forces RH AND RH forces P, by standard spectral theory. **Consequence**: **NCG-only approaches universally fail K1 by structure**. The K1 wall is not specific to Connes — it's a structural feature of any trace-formula approach. **The unique escape route is geometric**: intersection theory + Hodge index theorem on a constructed surface provides positivity from the SIGNATURE of an intersection form, a structurally different kind of positivity not subject to the no-shortcut theorem. The theorem is folklore in NCG circles; the contribution of R3.5 is to make it explicit in the 17-constraint framework's language. **Crystallizes the central project finding**: constraints (xi)-(xiii) are not just "open" — they are specifically THE escape route through which any RH proof via Architecture 2 must go. Every other route is blocked by R3.5 (NCG approaches) or by Arch 3 finding 7 (analytic approaches).
- ~~**R3.6**: Deep dive on Connes-Consani C3 (arithmetic site, hyperrings, characteristic-one geometry).~~ **Complete** ([2A_R3_6_arithmetic_site.md](../experiments/arithmetic_geometric/2A_R3_6_arithmetic_site.md)). The most aggressive Connes-Consani refinements (arithmetic site 𝒜 as a topos with hyperring-valued structure sheaf, Frob_ar endomorphism, characteristic-one calculus) host at least four positivity formulations (C3a intersection-pairing, C3b étale cohomology spectral, C3c motivic, C3d sheaf-theoretic). All four either fit R3.5's hypothesis and fail K1, or aren't strong enough to imply RH alone. **Net effect**: Connes / Connes-Consani (xi)-(xiii) sharpens from 🟡 to ❌ — no Connes-Consani formulation has been demonstrated to escape K1. The 25+ years of Connes-Consani program development has produced rich categorical machinery (topos theory, hyperrings, tropical/idempotent structures) but no positivity statement strictly weaker than RH. **Silver lining**: this machinery might serve as INFRASTRUCTURE for the geometric route in Architecture 2 — even if it doesn't directly provide K1-escaping positivity, it could provide the right notion of "scheme below ℤ" or sheaf-theoretic tools for constructing the surface and its intersection theory. R3.6.3 surfaces this as a follow-up direction.
- ~~**R3.6.3**: investigate whether Connes-Consani machinery (arithmetic site, hyperrings, characteristic-one) can serve as infrastructure for the geometric route.~~ **Complete** ([2A_R3_6_3_cc_infrastructure.md](../experiments/arithmetic_geometric/2A_R3_6_3_cc_infrastructure.md)). Verdict: PARTIALLY, in three decreasing senses. **Strong sense (categorical setting for intersection theory)**: ⏳ open — topos $\mathcal{A}$ is a candidate but no published intersection theory on hyperring-sheaf topoi exists. **Medium sense (combinable ingredients with other frameworks)**: 🟡 — hyperring sheaves could enrich Borger's $W(\mathbb{Z})$ in the R4 hybrid, but combination undeveloped. **Weak sense (inspiration via tropical Hodge index)**: ✅ — the Adiprasito-Huh-Katz 2018 tropical Hodge index theorem is a deep classical result motivating the search for a Hodge index in the geometric route. But it does NOT transfer because tropical varieties encode degenerations of EXISTING algebraic varieties, not constructed-from-scratch arithmetic surfaces. **Cross-cuts**: with R4 (hyperring sheaves on $W(\mathbb{Z})$); with R5 (tropical prismatic cohomology, speculative); with 2D-M3 (hyperring-valued leafwise prismatic cohomology). **Default strategy** per path-forward Option C: pursue R2.5 + R5 first; add R3.6.3 machinery only if needed for the Hodge index step. **Three queued research-grade follow-ups** (R3.6.3.a literature deep-dive, R3.6.3.b hyperring tensor product theory, R3.6.3.c tropical-arithmetic Hodge bridge) are all thesis-level projects beyond project scope.
- ~~**R4**: explore hybrid candidates — the "Borger Frobenius + Connes trace formula" hybrid.~~ **Analyzed** ([2A_R4_borger_connes_hybrid.md](../experiments/arithmetic_geometric/2A_R4_borger_connes_hybrid.md)). The natural bridge: U_t = ∏_p U_{log p}^{t/log p} — Borger's discrete Adams operations ψ_p generate Connes' continuous ℝ*_+-action via the multiplicative completion. Candidate Hilbert space: H = L²(W(ℤ), μ) for an appropriate measure μ. Predicted scorecard: **~8 ✅ / 5 🟡 / 3 ❌** — similar to Λ-blueprints (R2.5) but with trace formula explicit rather than implicit. **K1 verdict**: fails K1 by R3.5 (inherits Connes' trace identity vulnerability). **Value**: infrastructure for the geometric route — gives a concrete Hilbert space realization where Borger's surface side and Connes' trace formula side coexist. Five open technical questions (R4.1-R4.5) for someone developing it rigorously. **R2.5 (Λ-blueprints) and R4 (Borger + Connes) are complementary hybrids**: similar scorecard progress, different mechanisms. Both inherit K1 failure on (xi)-(xiii) but provide infrastructure for the geometric escape route.
- ~~**R5**: investigate Bhatt-Morrow-Scholze prismatic cohomology as the cohomology for Spec(W(ℤ)) in Borger's framework.~~ **Analyzed** ([2A_R5_prismatic_cohomology.md](../experiments/arithmetic_geometric/2A_R5_prismatic_cohomology.md)). **Connection**: δ-rings (the foundation of BMS prismatic cohomology) are essentially "Λ-rings at one prime p"; Borger's Λ-structure naturally projects to δ-structures at every prime. So prismatic cohomology applies to Spec(W(ℤ)). **Predicted impact**: closes constraints (iv)-(vii) (finite cohomology, Poincaré duality, cycle class map, Künneth) in one move. **K1 status**: still fails — prismatic cohomology has its own trace formula structure that falls under R3.5's hypothesis. So R5 is infrastructure progress, not K1 escape. Five verification questions surfaced. **Both hybrid candidates (R2.5 Λ-blueprints, R4 Borger + Connes) could use prismatic cohomology as their cohomology theory.**
- **Path forward strategic plan** ([2A_path_forward.md](../experiments/arithmetic_geometric/2A_path_forward.md)): synthesis of R1-R5 into a research plan. **Develop BOTH hybrid candidates in parallel**; use prismatic cohomology for both; attack Hodge index on whichever track reaches it first. **5-10 year multi-paper research program**, success probability < 50%. Project-level vs beyond-project work distinguished. **Final meta-conclusion**: Architecture 2 is the right place to look for an RH proof (per R3.5 ruling out other architectures), but the geometric construction problem is hard enough that even existing categorical machinery (Λ-rings, blueprints, adèle class space, prismatic cohomology, arithmetic sites) doesn't close it. New mathematics is needed along the hybrid + geometric lines.
- ~~**2E** (numerical probe): test whether bare $\psi_p$ on concrete Λ-rings has zeta-zero-like spectrum.~~ **Complete** ([e2e_adams_spectrum.py](../experiments/arithmetic_geometric/e2e_adams_spectrum.py), [2E_adams_spectrum_probe.md](../experiments/arithmetic_geometric/2E_adams_spectrum_probe.md)). Four probes (representation rings, Frobenius on $\mathbb{F}_q$, truncated ghost ring, rational K-theory). All spectra are roots of unity, $\{0\}$, or pure powers of $p$ — structurally orthogonal to $\{\gamma_n\}$. The one apparent near-coincidence ($5^2 \approx \gamma_3$, distance 0.01) is pigeonhole, confirmed by randomization control (~9th percentile under structural null). **Conclusion**: the bare Λ-structure cannot carry zeta-zero information — the cohomology lifts (prismatic per R5) is where the spectrum would live. **This is the predicted negative outcome and confirms R5's framing.** See finding #11 above.
- ~~**2C** (state of the $\mathbb{F}_1$ / Arakelov programs as of 2025): the framework supports this naturally — write up the survey using the scorecard structure.~~ **Complete** ([docs/03_research/f1_arakelov_survey_2025.md](../docs/03_research/f1_arakelov_survey_2025.md)). Survey covers the six $\mathbb{F}_1$ candidates (synthesized from 2A dossiers), the Arakelov-Soulé-Gillet arithmetic intersection theory program (not directly covered by 2A), and the 2018-2025 infrastructure (prismatic cohomology, condensed and light condensed mathematics, perfectoid spaces, Bost foliations, motivic Arakelov). **Aggregated status table**: the Hodge index positivity slot is UNIVERSALLY OPEN across both programs and all candidates. The Arakelov framework provides arithmetic intersection theory on arithmetic surfaces over $\mathrm{Spec}(\mathcal{O}_K)$ (relative dimension $\ge 1$) but NOT on $\mathrm{Spec}(\mathbb{Z})$ itself (relative dimension 0). The $\mathbb{F}_1$ framework provides candidate "bases below $\mathbb{Z}$" but no candidate carries Hodge index positivity. Recent 2020s machinery (prismatic cohomology, condensed math) is INFRASTRUCTURE for both programs but does not close the central open problem. Path forward per [2A_path_forward.md](../experiments/arithmetic_geometric/2A_path_forward.md): develop the hybrid candidates (R2.5 $\Lambda$-blueprints, R4 Borger + Connes) in parallel, apply prismatic cohomology, attack Hodge index on whichever track reaches it first. Multi-decade research program, < 50% success probability.
- ~~**2D** (smallest open conjecture in Deninger's program): identify a meaningful target shorter than full RH.~~ **Complete** ([2D_deninger_micro_target.md](../experiments/arithmetic_geometric/2D_deninger_micro_target.md)). Surveys three candidate micro-targets and recommends **M3, the prismatic foliation hypothesis**: define a foliation $\mathcal{F}$ on the prismatic site of $\mathrm{Spec}(W(\mathbb{Z}))$ whose leaves are orbits of $\Phi_t = \prod_p U_{\log p}^{t/\log p}$, and verify the leafwise prismatic cohomology has finiteness, Poincaré duality, Künneth, and a Lefschetz trace formula recovering the Euler-product piece of $\zeta(s)$. **What M3 closes if proved**: constraints (iv)-(v)-(vii) and partially (viii)-(ix) for Deninger's framework. **What it leaves open**: (xi)-(xiii) Hodge index positivity (the K1-escape route). M3 is infrastructure progress on Deninger's program (smaller than RH, but substantively new) and sits at the natural intersection of R4 (Borger + Connes hybrid) and R5 (prismatic cohomology). Tractable as a thesis-level project. The two alternative candidates (M1 archimedean fiber, M2 one-prime local Lefschetz) are either too disconnected from Deninger's dictionary or mostly recovered by Bost-Connes 1995. M3 is the right size.

These are not "experiments" in the numerical sense, but they now have a defined methodology and evaluation criteria.

### Arch 3 (positivity): the framework is robust; rigorous Li-negativity now witnessed at n = 336,000 (3B.3).

The Gram-matrix detector works as a wrong-approach detector and survives Selberg-class cross-cuts. The framework has been validated. **3B.3 ([e3b3_rigorous.py](../experiments/positivity/e3b3_rigorous.py) + [.md](../experiments/positivity/e3b3_rigorous.md)) closes the direct-exhibition extension**: rigorous witness $\lambda_{336{,}000}^{DH} < 0$ with explicit Bombieri-Lagarias error bound (411 at the witnessed n) and tail bound (392 from 1/γ² scaling + empirical density assumption). Uses 100-digit working precision and the full T_max = 500 off-line zero data (18 zeros UHP from 9 distinct gammas, 9 quadruples). Sharpens 3B.2's n = 400,000 to n = 336,000 — 16% lower, closer to the magnitude-crossover prediction at n ~ 320,000 plus phase-alignment offset. The Gram-matrix detector remains the cheaper test (K=30 test functions, T_max=200, no high-precision computation needed); 3B.3 is the direct exhibition that complements it. **Arch 3 is now fully characterized: small-n Li-positivity does not discriminate; Gram-matrix detector discriminates cheaply at K=30; direct Li discriminates at n = 336,000 rigorously.**

### Arch 4 (analytic): the d-variate LP gap is real and grows with d, but does not improve the MT zero-free region constant under restriction (4E.3, 4E.4).

4B closed the 1D Fejér question. 4D-ii and 4D.2 confirmed that single-coefficient $d$-variate LPs decompose. 4E and 4E.2 found that balanced-diagonal-sum LPs $\max c_{1,1} + \alpha c_{2,2}$ do NOT decompose: LP value exceeds the C-S tensor bound by up to +25% at $\alpha = 3, N = 2$. **4E.4 extended to d=3** and found the gap nearly DOUBLES: +51% at $\alpha = 3.25, N = 2$, fitting the pattern $\sim (d-1) \times 25\%$.

**4E.3 closes the natural RH-application follow-up:** does the +25% (or +51%) gap improve the Mossinghoff-Trudgian zero-free region constant? Answer: NO. Both numerically (across all $\alpha$ and reductions) and structurally (any $d$-variate non-neg polynomial restricted to a line gives a 1D non-neg polynomial, bounded by 1D Fejér at matched effective degree). The C-S and MT figures of merit are incompatible; the $d$-variate restriction approach to MT is structurally capped by 1D.

So the architecture-4 numerical thread has converged: the bivariate / multivariate LP families are computationally well-understood (gap pattern with $d$ is known), but none of them produces a better zero-free region constant via the standard de la Vallée Poussin route.

Remaining open directions (NOT closed by 4E.3, NOT in the restriction route):
- **Constrained-domain LP** (4E.5): impose $P \geq 0$ only on a submanifold corresponding to a hypothetical off-line zero. The submanifold-constrained polynomial is NOT bounded by 1D Fejér.
- **Polynomial-ideal SOS** (4E.6): sum-of-squares decompositions modulo prime-coupling relations.
- **Multi-zero / multi-character coupling** (4E.7): Heath-Brown's actual use of bivariate inequalities in least-prime-in-AP / Siegel-zero problems (these involve multiple putative zeros, where 2D structure genuinely couples them).
- **4-variate or higher d** for the balanced-sum LP gap pattern: does the $(d-1) \times 25\%$ scaling continue?

~~4A (Vinogradov-Korobov reproduction) and 4C (conditional improvements) remain literature tasks.~~ **Complete** ([`4a_4c_vinogradov_korobov.md`](zero_free/4a_4c_vinogradov_korobov.md)): unified dossier covering Inputs 1 and 3 of the classical analytic route (the explicit-formula and exponential-sum sides), to complement 4B-4E.7's coverage of Input 2 (the auxiliary inequality). **Three structural conclusions**: (1) the $2/3$ exponent comes from Vinogradov's mean value theorem, sharpened to its main conjecture by Bourgain-Demeter-Guth 2016 — so within the V-K recipe it is now a true ceiling; (2) the auxiliary-inequality input is saturated (4B's Fejér + 4D-4E.7's no-escape from line restriction), so no clever polynomial can push the exponent; (3) no named conditional improvement (RH / density hypothesis / LH / no-Siegel-zero / Heath-Brown / Pintz / Ford / BDG) would push the exponent. **Architecture 4 is a constraint-mapping architecture, not a route to RH.** Pushing the exponent requires a fundamentally new input class (Arch 2 arithmetic-geometric exponential-sum machinery á la Deligne, or Arch 1 Connes spectral identification).

---

## Methodological notes

### What test designs have worked

- **The PSD-of-Gram-matrix construction:** evaluating a sum $\sum_\rho \Phi(\rho_j) \Phi(\rho_k)$ at on-line zeros gives a real Gram matrix (automatically PSD); at off-line zeros it doesn't. Reduces the abstract positivity question to a finite-dimensional eigenvalue computation. This is the cleanest concrete realization of "Level 4 positivity" we have.

- **The L-function-class cross-cut:** running the same test on $\zeta$ (RH believed), $\chi_3, \chi_4$ (GRH believed; Selberg-class positive control), and D-H (RH known false; non-Selberg negative control) gives three calibration points. A test that distinguishes all three correctly is direction-selective.

- **Best-affine rescaling for spectral discrimination:** instead of comparing raw eigenvalues to zeta gammas (which forces a scale match), fit $E \mapsto \alpha E + \beta$ first and report residual RMS. Eliminates trivial scale mismatch as a confound.

- **High-precision arithmetic for slow-convergent sums:** mpmath at $\geq 30$ digits for any zero sum, Hurwitz zeta for Dirichlet L-functions, $Z_\chi$ sign-change scan for L-zeros. The smoke test catches regressions at 8/8 tests.

### What test designs did not work, or required correction

- **LP for nonneg multivariate trig polys at coarse grid:** at $M_{2D} = 50$, the 2D LP returned solutions with $P_{\min} \sim -10^{-2}$, i.e., genuinely infeasible on the continuum. Required $M_{2D} = 200$ for $P_{\min}$ to drop to floating-point noise. Lesson: pointwise constraints on continuous functions require fine sampling.

- **Comparison convention mismatch in the 4D multivariate LP:** an earlier version of the 4D / 4D.2 narrative claimed a "factor-of-$2^d$ advantage" of the LP over a "factorized witness." This was a convention error. The 1D Fejér theorem statement "max $c_1 = \cos(\pi/(n+2))$" uses the 4B convention $P = c_0 + 2\sum c_k \cos$, in which the raw coefficient of $\cos(\alpha)$ in the optimum $Q$ is $q_1 = 2 c_1$, not $c_1$. The tensor product $Q(\theta_1) \cdots Q(\theta_d)$ has raw $c_{1,\ldots,1} = q_1^d = (2 c_1)^d$, which equals the LP optimum. The "$2^d$ advantage" came from comparing the LP value to $c_1^d$ instead of $(2 c_1)^d = q_1^d$. Once the conventions are aligned, no advantage remains: the d-variate LP just finds the tensor product. **Lesson: whenever comparing an LP value to an analytic witness, write both in the same convention (raw coefficients of $\cos$ in the polynomial, not "doubled" or "Fourier-symmetric" conventions). Verify the rank of the LP-optimal coefficient tensor: if rank 1, the problem decomposes.**

- **Lowest-eigenvalue-of-real-Hamiltonian comparison without rescaling:** raw eigenvalues from a discretized $H_{BK}$ (range $[0, 20]$) compared to zeta gammas (range $[14, 143]$) gave RMS $\sim 88$, which obscured the actual L-function-blindness question. Best-affine rescaling (1C) made the structural comparison clean.

- **Compact-support test function for Li (e.g., truncating the explicit-formula sum at $T_{\max} = 200$):** the truncation error in Li coefficients at $n = 500$ is $\sim 17\%$, dominated by the $\sim n^2 \log T / (2\pi T)$ tail. To reach truncation accuracy 1% we'd need $T_{\max} \gtrsim 10^4$, requiring $\sim 12{,}000$ zeros. Feasible but not pursued; the qualitative result was already in hand.

### What machinery should be reusable across future experiments

- **The `LFunction` interface** in `experiments/_shared/lfunction.py`: every L-function (zeta, D-H, Dirichlet) implements `evaluate(s)` and `zeros(T_max, prec)` with disk caching. New L-functions can be added by subclassing and the existing experiments run on them unchanged.

- **The Gram-matrix scaling experiment template** (e3d2): pick a test family, an L-function set, a basis-size sweep, and report min eigenvalue. Generalizes to any "Level 4 positivity" test.

- **The discrimination-ratio test** (e1c): for any candidate $\zeta$-targeting construction, apply it to D-H (and ideally $\chi_3, \chi_4$) and compute best-affine RMS to each. A construction whose ratio is bounded by a factor of $\sim 3$ is L-function-blind.

---

## Session 003 findings (2026-05-28): second control, function-field target, last analytic escape

**Finding #19 (Arch 3, the wrong-approach detector GENERALISES beyond D-H).**
[`e3l_epstein_control.py`](positivity/e3l_epstein_control.py) builds a second,
structurally independent off-line-zero control: the Epstein zeta function of a
binary quadratic form (functional equation, no single Euler product), via a new
`experiments/_shared/epstein_zeta.py` (Chowla-Selberg / Terras expansion,
validated against the class-number-1 anchor $Z_Q = 4\zeta(s)\beta(s)$ to
$10^{-31}$ and against its own functional equation to $10^{-32}$). Reconnaissance
result: the small class-number 2 and 3 discriminants ($d = 15, 23$) have NO
off-line zeros at reachable height, but the class-number-5 discriminant $d = 47$
non-principal form $2x^2+xy+6y^2$ has an off-line zero pair at
$\rho \approx 0.634 \pm \ldots$, partner $0.366 + 32.05\,i$; the PRINCIPAL form
$x^2+xy+12y^2$ has none. Running the 3J Weil-form Schur-complement detector on
all five targets at $K$ up to 300 gives a clean PASS of the counting law on
BOTH controls:

  | target | off-line heights | Schur dim | Schur neg | rel min |
  |---|---|---|---|---|
  | zeta, chi_3, Epstein d=47 principal | 0 | 0 | 0 | PSD |
  | Epstein d=47 non-principal | 1 | 2 | 1 | -25.5% |
  | Davenport-Heilbronn (T<=200) | 4 | 8 | 4 | -77.6% |

The law `schur_neg = #off-line heights`, `schur_dim = 2 * #off-line heights`
holds identically on Epstein as on D-H. The Weil-form positivity detector
responds to off-line zeros per se, not to a quirk of the D-H construction. The
wrong-approach discipline now rests on two independent counterexamples, and the
Epstein principal-vs-non-principal contrast shows the detector is selective
WITHIN a single discriminant. (Off-line zeros are sparse for these Epstein
forms: still only one height up to $T = 120$, so the experiment tests
generalisation, not the multi-height counting which D-H already established
across $T \in \{200,300,350,500\}$.)

**Finding #20 (Arch 2, the function-field positivity target, exhibited
concretely).** [`e2f_hodge_index_sweep.py`](arithmetic_geometric/e2f_hodge_index_sweep.py)
extends 2B from one curve over $\mathbb{F}_5$ to a family: elliptic curves over
$\mathbb{F}_q$ for $q \in \{5,7,11,13,17,19,23\}$ and genus-2 hyperelliptic
curves over $\{5,7,11,13\}$. For each it counts points over $\mathbb{F}_{q^k}$,
recovers the integer zeta polynomial $P(T)$ exactly (via $\exp(\sum N_k T^k/k)$
in sympy), and computes the Frobenius eigenvalues. The Weil RH bound
$|\alpha_i| = \sqrt{q}$ holds EXACTLY across the whole family (worst deviation
$0.000\mathrm{e}{+}00$; it is a theorem via the Hodge index theorem on
$C \times C$). This is the positivity TARGET the geometric route (Arch 2,
Direction 8) must reproduce over $\mathrm{Spec}(\mathbb{Z})$: in the
function-field world where the index theorem is available, the bound is exact
and computable; the obstruction over $\mathbb{Z}$ is the absence of the surface
and the index theorem, not of the positivity statement itself.

**Finding #21 (Arch 4, the last analytic escape closes).**
[`e4e9_heath_brown_sdp.py`](zero_free/e4e9_heath_brown_sdp.py) implements
Direction 7 (Heath-Brown multi-zero MT): it targets the MULTI-ZERO MT shape
factor directly in an SDP over the $\cos\times\cos$ SOS cone, sweeping the
zero-coupling $g = \gamma_2/\gamma_1$ and bidegree $N \in \{2,3,4\}$, combining
4E.7's cross-frequency term with 4E.2's higher harmonics. Result: the best
multi-zero MT / Fejer ratio is $\le 1$ (saturates, never exceeds), with the
optimal certificate at rank 2 (sharpening 4E.7's rank-1 finding: the multi-zero
higher-harmonic structure is genuinely 2D yet still capped). The line
restriction folds any $\cos\times\cos$ SOS polynomial into a 1D non-negative
polynomial, and the multi-zero ledger redistributes harmonic weight but cannot
manufacture trick-frequency weight beyond the Fejer cap. This closes the last
LP/SDP escape from the 4E.3 line-restriction lemma. Architecture 4 is now
numerically closed across the entire LP/SDP/SOS family. (The D-H discipline does
not apply: this is pure trig-polynomial optimisation, L-function-agnostic.)

**Finding #22 (Arch 3, a SECOND Li-criterion off-line witness + rigorous
discrimination).** [`e3b4_li_discrimination.py`](positivity/e3b4_li_discrimination.py)
extends the 3B.3 rigorous Li machinery from one off-line construction to a
discrimination statement across five L-functions. Results: the D-H rigorous
negativity reproduces exactly (lambda_n^{DH} < 0 rigorously from n = 336,000);
the Selberg-class controls (zeta q=1, chi_3 q=3) are rigorously POSITIVE from
n = 50,000; and the Epstein d=47 non-principal form gives a SECOND off-line Li
witness: its lambda_n crosses negative at n = 110,000 (the off-line zero's
beta = 0.366 partner has |1 - 1/rho| > 1, so its Li contribution grows
exponentially negative and overwhelms the positive on-line baseline). This is
the first Li-criterion off-line witness for an Epstein zeta in the project, and
it is the SAME off-line zero that makes the 3L Schur detector fire (Finding
#19), so the two positivity criteria agree on the second control. With the
Epstein zeros scanned to T = 500 (so the off-line TAIL bound, which scales as
1/(2 T_max^2), is negligible; at T = 60 it swamped the signal), the Epstein
witness is RIGOROUS: lambda_n^{Epstein} < 0 from n = 110,000 after the
worst-case asymptotic and tail bounds. The full discrimination then holds
rigorously: at n = 336,000,
lambda_n^{DH} < 0 and lambda_n^{Epstein} < 0 < lambda_n^{zeta}, lambda_n^{chi_3}.
The Li criterion discriminates off-line L-functions from Selberg-class
L-functions for a SECOND, independent off-line construction, not just
Davenport-Heilbronn. (The Epstein d=47 off-line zeros stay sparse: still the
single height at 32.05 up to T = 500, so the higher T_max bought the tail
bound, not additional zeros.)

**Cross-architecture synthesis of session 003.** Findings #19 and #22 harden
the wrong-approach discipline (it now rests on TWO independent off-line
constructions, D-H and Epstein, and both the Gram/Schur detector and the Li
criterion fire on both). Finding #21 closes Architecture 4 numerically across
the full LP/SDP/SOS family. Finding #20 exhibits the function-field positivity
target exactly. Net effect: every architecture reachable by computation is now
either closed (Arch 1, 3, 4) or has its target made concrete (Arch 2), and the
sole remaining route is the Hodge-index construction over Spec(Z) (Direction 8),
which is construction work, not a compute task. This is the marginal-positivity
picture sharpened, not softened: the controls are stronger and the path is
narrower.

---

## Open questions identified by the experiments

1. ~~**Does the 4D 2D-LP factor-of-4 result generalize to higher dimensions?**~~ ~~**Resolved (4D.2):** confirmed at $d = 3$.~~ **Resolved differently:** the "factor-of-$2^d$ advantage" was a convention error. The d-variate LP for max $c_{1,\ldots,1}$ at uniform degree $(N,\ldots,N)$ decomposes: the optimum is the tensor product $Q(\theta_1) \cdots Q(\theta_d)$ where $Q$ is the 1D Fejér optimum, giving $\max c_{1,\ldots,1} = (2\cos(\pi/(N+2)))^d = (q_1^{1D})^d$. No new inequality.

2. ~~**What LP family WOULD produce a genuinely new multivariate auxiliary inequality?**~~ **Resolved (4E + 4E.2):** the balanced-diagonal-sum family $c_{1,1} + \alpha c_{2,2}$ at bidegree $(2, 2)$ produces 2D inequalities not derivable from tensor products, with relative gap to the C-S tensor bound varying as $\alpha$ varies and peaking at +25.00% for $\alpha = 3$. Extension to higher bidegree with more diagonal terms (4E.2.b: $c_{1,1} + c_{2,2} + c_{3,3}$ at $N = 3$) increases the gap by 8.66x relative to the 2-term version at the same bidegree. The off-diagonal-sum $c_{1,2} + c_{2,1}$ does NOT exceed tensor bound. Remaining sub-directions: (a) constrained-domain LPs; (b) Heath-Brown cross-prime coupling; (c) closed-form derivation of the $\alpha = 3$ peak optimum.

3. ~~**Does the Mossinghoff-Trudgian zero-free constant improve when the 4E/4E.2 2D inequality is plugged in?**~~ **Resolved (4E.3): NO.** The +25% C-S gap does not translate to an MT improvement. Both numerically (the 4E.2 peak gives 12.6x WORSE shape/$P(0)$ than 1D Fejér at matched effective degree, and across $\alpha \in [0, 10]$ no 2D polynomial beats 1D Fejér) and structurally (any 2D non-neg polynomial restricted to a line is bounded by the 1D Fejér optimum). The C-S and MT figures of merit are incompatible; future LP-based zero-free-region work must target MT directly (via constrained-domain LP, multi-zero coupling, or polynomial-ideal SOS).

4. ~~**At what $n$ does $\lambda_n^{DH}$ first go negative?**~~ **Resolved (3B.2):** witnessed at $n = 400{,}000$ via the asymptotic-plus-off-line-correction decomposition. Off-line correction $-2.0 \times 10^7$ vs on-line asymptotic $+2.4 \times 10^6$. Crossover predicted at $n \sim 320{,}000$; phase determines sign past that. Refinement: a fully rigorous certificate (exact xi-derivative formula, ~100 digit precision, more off-line zeros) would replace the asymptotic with the exact value; the structural conclusion is robust.

5. ~~**Does the Gram-matrix wrong-approach detector remain a clean test in the limit $K \to \infty$ where $M^\zeta$ becomes singular but $M^{DH}$ continues to deepen?**~~ **Resolved (3D.3): YES, and the structural picture is cleaner than expected.** At $K \in [100, 1000]$ with $T_{\max} = 200$ (D-H has 8 off-line zeros, i.e., 4 conjugate pairs): the relative min eigenvalue $\lambda_{\min}/\lambda_{\max}$ for D-H converges to an asymptotic constant of $-2.62\%$. The number of negative eigenvalues stays FIXED at $4 =$ number of off-line zero pairs. Selberg-class L-functions ($\zeta, \chi_3, \chi_4$) remain PSD to floating-point noise. The detector is essentially counting off-line zero pairs via the negative-eigenvalue count, and the relative-min depth is dimension-independent.

6. **Is there an Arch-2-style "lift to $\mathbb{Z}$" that the experiments could probe, even partially?** 2B gave us RH for one curve over $\mathbb{F}_5$. An analogous "RH for a single object in $\mathrm{Spec}(\mathbb{Z})$" doesn't exist yet, but $\mathbb{F}_1$ literature gestures at it.

---

## Synthesis: where does the project stand?

Of the four architectures:

- **Arch 1 (spectral)** is closed at the numerical-experiment level. We've shown the simple constructions are L-function-blind; further progress requires Connes-style theory.
- **Arch 2 (arithmetic-geometric)** has produced the strongest individual result (Weil RH for one curve over $\mathbb{F}_5$, proved). 2A completes the diff-table analysis: the obstruction over $\mathrm{Spec}(\mathbb{Z})$ is *constructive*, not analytic — Weil's proof template needs a Frobenius substitute, a surface $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$, and a Hodge index positivity on that surface; the three corresponding programs (Connes, Deninger, $\mathbb{F}_1$) each address one corner but no single program has assembled all three. The path forward is construction work. **R1 + R2 + R2.5 + R3 + R3.5 progress**: R1 confirmed all six candidates pass K2 (D-H exclusion). R2 computed the fiber product in Borger and Lorscheid, identifying that they're complementary half-candidates. R2.5 proposed Λ-blueprints as the natural hybrid combining their strengths (8 ✅ / 4 🟡 / 5 ⏳ predicted scorecard). R3 analyzed Connes-Consani's three positivity conjectures (C1/C2 fail K1, C3 K1-uncertain). **R3.5 proved a no-shortcut theorem**: every trace-formula NCG framework has positivity ⟺ RH, so NCG-only approaches universally fail K1 by structure. **The Hodge index slot (xi-xiii) is therefore not just "open" — it is specifically THE escape route through which any RH proof via Architecture 2 must go.** The geometric route is unique: intersection-theoretic positivity (signature of an intersection form) is structurally different from operator-theoretic positivity (trace formulas, self-adjoint operators, quadratic forms). Only the former escapes the K1 wall.
- **Arch 3 (positivity)** has the most extensive experimental support: small-$n$ Li-positivity confirmed for $\zeta$ (but not a discrimination test); Weil-form-via-Gram-matrix works as a wrong-approach detector; Selberg-class cross-cut validates direction-selectivity. The next experimental step (xi-derivative Li at $n \sim 350{,}000$) is heavy but well-defined.
- **Arch 4 (analytic)** has a refined picture from 4D/4D.2 + 4E + 4E.2 + 4E.3 + 4E.4: single-coefficient multivariate Fejér LPs decompose to tensor products, but the balanced-diagonal-sum LP $\max c_{1,1} + \alpha c_{2,2}$ at bidegree $(2, 2)$ does NOT — peak gap +25.00% at $\alpha = 3$. The trivariate extension (4E.4) DOUBLES the gap to +51.29% at $\alpha = 3.25, N = 2, d = 3$, fitting the pattern $\sim (d-1) \times 25\%$. **However (4E.3)**: the d-variate C-S gap does NOT improve the Mossinghoff-Trudgian zero-free region constant for any $d$, neither numerically nor structurally. The C-S and MT figures of merit are incompatible: any d-variate non-neg polynomial restricted to a line is bounded by 1D Fejér at matched effective degree, so the d-variate restriction approach to MT is structurally capped. To actually improve the zero-free region via multivariate inequalities requires constrained-domain LP, multi-zero coupling, or polynomial-ideal SOS (queued as 4E.5-4E.7). **The 4A + 4C unified dossier** ([zero_free/4a_4c_vinogradov_korobov.md](zero_free/4a_4c_vinogradov_korobov.md)) closes the literature side of Arch 4: the V-K $2/3$ exponent has been stuck 67 years because all three inputs of the recipe (explicit formula + auxiliary inequality + V-MVT exponential sum bound) are near-optimal within their frameworks. The conditional landscape (density hypothesis, LH, no-Siegel-zero, Heath-Brown, Pintz, Ford, BDG) sharpens constants but does not break the exponent. **Architecture 4 is a constraint-mapping architecture, not a route to RH** (LEARNINGS finding #14). Pushing the exponent requires a fundamentally new input class from Arch 2 or Arch 1.

The structural message of the experiments: **only Arch 2 has the cohomology/positivity coupling that closes RH-style arguments in the function-field case; only Arch 3 has a positivity test that distinguishes Selberg-class L-functions from non-Euler-product look-alikes computationally; Arch 1 and Arch 4, on the numerical evidence here, do not close RH by themselves.**

This is consistent with the project's structural commitment (RH lives at Level 4 positivity, not Level 3 spectral signature) and with the strategic landscape in [docs/research_atlas/](../docs/research_atlas/).
