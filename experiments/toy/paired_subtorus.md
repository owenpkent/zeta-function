# Paired-subtorus circle-rootedness: PROVEN

**Task**: H3 from LEARNINGS #143 (the adversary's A2 candidate theorem, `scratchpad/circle_interlacing/01_adversary.md`).
**Date**: 2026-07-01. **Role**: BUILDER.
**Status**: **PROVEN**, all $m$, all $U \in U(2m)$. Every lemma numerically verified in [`paired_subtorus.py`](paired_subtorus.py) (12/12, including an exact-unitary mpmath check at defect $1.3\times 10^{-51}$).

## Statement

**Theorem.** Let $U \in U(2m)$, coordinates paired $(2j-1, 2j)$, and
$D(\theta) = \mathrm{diag}(e^{i\theta_1}, e^{-i\theta_1}, \ldots, e^{i\theta_m}, e^{-i\theta_m})$
with $\theta_j$ iid uniform on $[0, 2\pi)$. Then

$$f(z) = \mathbb{E}_\theta\left[\det(zI - D(\theta)U)\right] = g(z^2), \qquad g(w) = \sum_{T \subseteq \{1..m\}} w^{m-|T|} \det U[S_T],$$

where $S_T$ is the union of the pairs indexed by $T$, and **all $2m$ roots of $f$ lie on $|z| = 1$**.

**Corollary 1 (contraction form).** If $\|V\| \le 1$ (any contraction, not necessarily unitary), all roots of $g$ lie in the closed unit disk (the expected characteristic polynomial is Schur-stable). Unitarity is exactly the boundary case that pins the roots to the circle.

**Corollary 2 (finite identity).** The continuous torus average equals the finite average $2^{-m}\sum_{\varepsilon \in \{\pm 1\}^m} \det(zI - E(\varepsilon)U)$, $E(\varepsilon) = \mathrm{diag}(\varepsilon_1, \varepsilon_1, \ldots, \varepsilon_m, \varepsilon_m)$: in both averages exactly the pair-closed principal minors survive, with coefficient $1$.

**Corollary 3 (self-inversiveness, the adversary's R3).** Jacobi's complementary-minor identity for unitary $U$ gives $c_{m-k} = \det(U)\,\overline{c_k}$ for the coefficients of $g$. The proof below does not use it; it falls out.

## Proof

Write $V$ for a contraction ($\|V\| \le 1$); the theorem uses $V = U$ unitary.

**Step S0 (polydisk nonvanishing of the generating determinant).**
$Q(y_1, \ldots, y_{2m}) = \det(I + \mathrm{diag}(y)V)$ is multiaffine in $y$ (each $y_i$ enters only through row $i$), and $Q(y) \ne 0$ whenever all $|y_i| < 1$: the spectral radius of $\mathrm{diag}(y)V$ is at most $\|\mathrm{diag}(y)V\| \le \max_i |y_i| < 1$, so $-1$ is not an eigenvalue. [Test 4]

**Step SE (Lemma E, the pair-extraction lemma).** *Let $Q(u, v) = A + B_a u + B_b v + Cuv$ be multiaffine and nonvanishing on the open bidisk. Then $|A| \ge |C|$, and hence $A + Cx \ne 0$ for $|x| < 1$.*

*Proof.* For fixed $|v| < 1$, the linear map $u \mapsto (A + B_b v) + (B_a + Cv)u$ is nonvanishing on $|u| < 1$, which forces $|A + B_b v| \ge |B_a + Cv|$ (if both sides vanished identically, $Q(\cdot, v) \equiv 0$ would vanish inside the bidisk). By continuity this holds for $|v| = 1$. Expanding $|A + B_b v|^2 - |B_a + Cv|^2 \ge 0$ on $|v| = 1$ and minimizing over the phase of $v$:

$$|A|^2 + |B_b|^2 - |B_a|^2 - |C|^2 \;\ge\; 2\,|\bar A B_b - \bar B_a C|. \tag{*}$$

Since $|\bar A B_b - \bar B_a C| \ge |B_a||C| - |A||B_b|$, $(*)$ rearranges to $(|A| + |B_b|)^2 \ge (|B_a| + |C|)^2$, i.e.

$$|A| + |B_b| \;\ge\; |B_a| + |C|. \tag{**}$$

Running the same argument with the roles of $u$ and $v$ swapped gives $|A| + |B_a| \ge |B_b| + |C|$. Adding the two: $|A| \ge |C|$. Finally $A \ne 0$ (else $Q(0,0) = 0$), so $A + Cx \ne 0$ on $|x| < 1$. $\square$ [Test 5, including the chain $(*)$, $(**)$ and a negative control: $|C| > |A|$ really admits a bidisk zero]

**Step SP (iterate over the pairs).** Group the $2m$ variables of $Q$ into the $m$ pairs. For pair $j$, freeze all other variables at arbitrary points of the open polydisk and apply Lemma E to $(u, v) = (y_{2j-1}, y_{2j})$: the *pair-even extraction* (keep the terms of joint degree $0$ or $2$ in the pair, writing $x_j$ for the monomial $y_{2j-1}y_{2j}$) is again multiaffine and nonvanishing on the open polydisk. Extraction is linear on coefficients, so it commutes with freezing the other variables. After all $m$ extractions, exactly the pair-closed subsets survive:

$$P(x_1, \ldots, x_m) = \sum_{T} \Big(\prod_{j \in T} x_j\Big) \det V[S_T] \;\ne\; 0 \quad \text{on } |x_j| < 1. \tag{Master claim}$$

[Test 6]

**Step SD (diagonal and pinning).** Restricting to the diagonal, $G(x) = P(x, \ldots, x) \ne 0$ for $|x| < 1$. Since $g(w) = w^m G(1/w)$, no root of $g$ has modulus $> 1$: all roots lie in the closed unit disk (Corollary 1). Now take $V = U$ unitary: $g$ is monic with $|g(0)| = |\det U| = 1$, and $|g(0)| = \prod_i |w_i|$ over the roots. A product of numbers each $\le 1$ equalling $1$ forces every $|w_i| = 1$. Roots of $f$ are the square roots: all on $|z| = 1$. $\blacksquare$ [Tests 7, 8, 12]

## Where the content lives (negative controls, all in Test 10)

- **Same-sign pairing** $\mathrm{diag}(e^{i\theta_j}, e^{+i\theta_j})$: every surviving minor carries $\mathbb{E}[e^{2i\theta}] = 0$; the average collapses exactly to $z^{2m}$. Conjugate pairing is what makes $g$ nontrivial.
- **Equal determinant is not enough**: $p = (z - e^{i\pi/3})^3$ and $q = (z - e^{-i\pi/3})^3$ are unitary characteristic polynomials with the same determinant, and $(p+q)/2 = z^3 - \tfrac32 z^2 - \tfrac32 z + 1$ has roots $\{-1, 2, \tfrac12\}$. So "average of same-det unitary char polys" is false in general; the paired-orbit structure is load-bearing.
- **Self-inversiveness is not enough**: the same cubic is self-inversive and off-circle (the Davenport-Heilbronn shape). The Schur-stability transport, not the functional equation, carries the theorem.
- **Unitarity is exactly the boundary**: $V = 0.8\,U$ puts every root at modulus $0.8^2$ [Test 11]; block-diagonal $U$ with $\det V_j \in \{1, -1, -1\}$ gives $g = (w+1)(w-1)^2$, an on-circle double root, the boundary contact of the reachable set [Test 9].

## Connection to #143 and MSS

This is the MSS-flavored expected-characteristic-polynomial theorem the #143 handoff asked for, over the interpolating family of subgroups: trivial subgroup $\to$ the char poly itself (circle-rooted); full diagonal torus $\to$ $z^{2m}$ (#143 collapse); **paired subtorus $\to$ nontrivial AND circle-rooted (now a theorem)**. The paired torus is the maximal torus of $Sp(m) \subset U(2m)$, so the statement reads: the weight-zero projection of $\det(zI - \cdot\,U)$ along the symplectic torus preserves the unitary root locus.

The meta-point for #143's kill: the proof **sidesteps the missing extremal-selection order entirely**. No interlacing, no "some member at least as good as the average". The mechanism is stability transport (nonvanishing on a polydisk, preserved by the pair-even extraction), the Schur/disk analogue of the Borcea-Branden half-plane calculus. This strengthens the corrected #143 reading rather than reopening it: content requires conjugate pairing (same-sign collapses), the locus requires the unitary carrier (contractions pull strictly inside), and both are presupposed inputs here. Over $\mathrm{Spec}(\mathbb{Z})$ the carrier is exactly the missing Hilbert-Polya object, so nothing here touches M4 or RH.

Route scorecard from the work plan: (A) one-pair induction: the invariant class turned out to be *polydisk-nonvanishing multiaffine polynomials*, and the one-pair step is Lemma E; this route CLOSED the problem. (B) compound-compression: the naive guess $g = \det(wI + G)$ with $G$ the pair-compound was already refuted by the adversary (probe_a2c); the weak form ("$g$ is SOME unitary char poly") is equivalent to the theorem and is now true a posteriori. (C) Schur-Cohn transport: subsumed; the certificate the proof produces (Schur stability + unimodular constant term) is the Schur-Cohn shape with the positivity replaced by nonvanishing. (D) literature round: not needed, a full proof landed first.

## Literature and novelty (honest labels)

- Lemma E is elementary; coefficient inequalities of this type for bidisk-stable polynomials are classical territory (Schur-Cohn; Rudin's polydisc theory; stable multiaffine polynomials). I could not find this exact extraction lemma stated, but it is likely known or folklore to experts.
- The theorem itself (torus-orbit average of a unitary characteristic polynomial over the symplectic maximal torus is circle-rooted): not found in the #143 survey or the adversary round; nearest neighbors are Kabluchko (Ann. Henri Lebesgue 2025, unitary Brownian motion first moments, circle-controlled but not exactly circle-rooted at finite time from Haar-type averaging) and the Borcea-Branden/MSS stability calculus (half-plane regime). Novelty is plausible but UNVERIFIED against the OPUC/finite-free-probability literature; a SURVEYOR pass before any external write-up.
- The finite identity (Corollary 2) means the theorem is a statement about $2^m$ reflections $E(\varepsilon)U$, which may connect to real-stability techniques for signings (MSS I's own hyperbolic-polynomial toolkit, transported to the disk).

## Self-assessment (K1-K4, D-H, 17-constraint frame)

- **K1 (circularity)**: clean. Finite unitary matrices only; no zeta zeros, no Euler product, neither implies nor is implied by RH.
- **D-H discipline**: not an RH method, so the detector question is about shape: the theorem's certificate is carrier unitarity, which D-H lacks; the self-inversive-but-off-circle cubic in Test 10 is the D-H shape and is correctly NOT covered by the theorem. The construction distinguishes carrier from no-carrier by design.
- **Honest scope**: this is a toy-side (proven-world) structural theorem about the expectation step of a hypothetical circle-MSS engine. It does not manufacture the carrier, the order, or the M4 polarization. Its value: (i) the #143 phenomenon is now a theorem with an elementary proof; (ii) the proof style (locus preservation via stability transport, no order needed) is a genuinely different third mechanism next to operator and positivity, worth remembering when grading future engines.

## Handoff

**Verification targets (VERIFIER, Lean-friendly, all finite-dimensional):**
- VT-PS1: Lemma E exactly as stated (four complex numbers, one inequality chain). Mathlib-native.
- VT-PS2: $\det(I + \mathrm{diag}(y)V) \ne 0$ for $\|V\| \le 1$, $\max|y_i| < 1$ (spectral radius bound).
- VT-PS3: the pinning step: monic + roots in closed disk + $|g(0)| = 1$ $\Rightarrow$ all roots on the circle.
- VT-PS4 (capstone): the $m = 2$ instance end-to-end, then general $m$ by the extraction induction.

**Adversarial test cases (ADVERSARY):**
- Attack Lemma E's equality manifold: $Q = 1 + uv$ (from an antidiagonal pair block) has $|A| = |C|$; check the extraction lands exactly on the boundary, never beyond.
- Non-uniform measures on the paired torus (the proof uses only which monomials survive; any pair-even measure with $\mathbb{E}[e^{ik\theta_j}] = 0$ for $k = \pm 1$ and $\mathbb{E}[1] = 1$ gives the same $f$; biased measures with $\mathbb{E}[e^{2i\theta}] \ne 0$ leave the theorem's scope: find the failure).
- Perturb the pairing (overlapping pairs, triples $(e^{it}, e^{it}, e^{-2it})$): det still $1$; does circle-rootedness survive? The proof's extraction needs joint-degree-$\{0, k\}$ structure; test where it breaks.
- Numerical stress: $m = 10$ random spot checks (the formula is $2^m$ dets; feasible to $m \sim 14$).

## Test table (paired_subtorus.py, 12/12)

| # | What | Result |
|---|------|--------|
| 1 | R2 minor formula = sign average (exact) = MC torus average | $3.6\times10^{-15}$ / MC $0.008$ |
| 2 | R1: realizations circle-rooted | $7.1\times10^{-15}$ |
| 3 | R3: Jacobi self-inversiveness, $m = 2..5$ | $1.8\times10^{-15}$ |
| 4 | S0: polydisk nonvanishing + spectral bound | min $|Q| = 0.137$, bound tight |
| 5 | Lemma E chain $(*), (**)$, $|A| \ge |C|$ + negative control | max $|C|-|A| = -2.9\times10^{-2}$ |
| 6 | Master claim $P \ne 0$ on polydisk + boundary contact | min $|P| = 0.243$ |
| 7 | Theorem regression, Haar $m = 1..6$ | max defect $3.0\times10^{-15}$ |
| 8 | Search $m = 5, 6, 7$ (random + Nelder-Mead + structured) | max defect $7.3\times10^{-15}$ |
| 9 | Block-diagonal boundary case, double root on circle | exact to $4.4\times10^{-16}$ |
| 10 | Controls: same-sign collapse / equal-det fails / self-inversive fails | $3.1\times10^{-16}$ / root $2.0$ / defect $1.0$ |
| 11 | Contraction corollary: roots at $0.8^2$, inside | $0.6400$ |
| 12 | mpmath 50-digit exact-unitary (Cayley) check, $m = 3$ | defect $1.3\times10^{-51}$ |
