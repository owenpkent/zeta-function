# e3ac: entropic exports (the density-matrix costume, executed)

**Status: BUILDER probe + ADVERSARY pass applied (PASS_WITH_FIXES, report tracked at [`_e3ac_adversary.md`](_e3ac_adversary.md); every FIX item applied, the rank-one costume and the fold ported as gates), 2026-09-04, Owen-directed ("what if we used a density matrix to address this problem, like quantum entropy"). 14/14 gates full ($N = 10^5$, 13 s) and quick ($N = 10^4$, 2 s). LEARNINGS #218; ledger section 11 of [`trojan_horse_m4.md`](../../docs/03_research/trojan_horse_m4.md); screen 14 of the breadth battery. Falsification instrument: nothing here is evidence for RH, and the frontier is UNMOVED by design.**

## 1. The question, and what was already on file

The proposal was to attack RH through a density matrix and its quantum entropy. Three things were on file. The trojan-horse ledger's costume 1 (state / GNS): every state on a $*$-algebra gives a positive form for free, and the cargo reappears at the identification joint. LEARNINGS #111: Araki relative entropy is one of four positivities Tomita-Takesaki gives away, all definite and $t$-blind. LEARNINGS #177: the entanglement entropy of the arithmetic Chern-Simons state is "nonnegative by construction, structurally incapable of an indefinite signature," with a disqualifier proposed but not banked. And e3z had measured the pointwise multiplicativity defect $a_{mn} - a_m a_n$ and read it as "D-H has no equilibrium product state."

What was NOT on file: the literal objects, built for every control in one code path, with the repaired Epstein control (LEARNINGS #217: the principal forms of $d = -15$ and $d = -47$ are RH-false) in the table. Post-#217 the repo held, unrecorded, a certified counterexample to the simplest form of the costume: a perfectly good density matrix, with a perfectly good entropy, whose zeros are off the line. The adversary added the second object, the rank-one state, which is the one that reaches the strip.

## 2. The two costumes

**Gibbs.** For a Dirichlet series with $a_n \ge 0$ and $\beta > 1$,
$$\rho_\beta = \sum_{n \ge 1} p(n)\,|n\rangle\langle n|, \qquad p(n) = \frac{a_n n^{-\beta}}{L(\beta)},$$
a density matrix on $\ell^2(\mathbb{N})$ whose partition function is $L(\beta)$. Unique factorization identifies $\ell^2(\mathbb{N})$ with $\bigotimes_p \ell^2(\mathbb{N}_0)$, one bosonic mode per prime (the Bost-Connes Fock picture), and $\rho_\beta$ is a product state over the modes exactly when $a_n$ is multiplicative, i.e. exactly when $L$ has an Euler product (multiplicative, not completely multiplicative, is the right condition; at $\lambda = -1$ below the state has $p(1) = 0$ and the identification still works because only the exponent-vector distribution is used).

1. **The state is diagonal** in the number basis. Its von Neumann entropy is the Shannon entropy of $p(n)$, and every diagonal state on a tensor product is separable. Nothing quantum does any work inside it (gate G1).
2. **Its one quantum-information invariant** is the total correlation across the prime modes, $C = \sum_p H(v_p) - H(n)$, which equals $D(p \,\|\, \bigotimes_p \mathrm{marg}_p)$ and, by the Pythagorean identity $D(p\|q) = C + \sum_p D(\mathrm{marg}_p \| q_p)$ for every product $q$, is the minimum of $D(p\|q)$ over product states: the relative-entropy distance from $p$ to the Euler-product manifold (the I-projection theorem; gates G11 and G12 are consistency checks of the two identities, not findings). $C = 0$ exactly for an Euler product, which is the identity $S = \sum_p S_p$ with $S = \log\zeta(\beta) - \beta\,\zeta'(\beta)/\zeta(\beta)$ (gate G2).
3. **$C$ is entropic**, nonnegative by construction: a disqualifier-grade detector, not a polarization.

**Rank-one (the adversary's addition).** $|\psi_s\rangle = \sum_n a_n n^{-s}|n\rangle$ with $s = \sigma + it$ exists for $\sigma > 1/2$ for every control, signed coefficients included: $\|\psi\|^2 = \sum_n |a_n|^2 n^{-2\sigma}$, which for $\zeta$ is $\zeta(2\sigma)$, so the critical line is exactly its normalizability boundary (the Hardy-space $H^2$ frame of Nyman-Beurling). Its reduced density matrix on a prime mode is not diagonal (off-diagonal entries 0.2 to 0.4 on mode 2). This is the costume that reaches the strip. Two facts: its entanglement across any prime-mode bipartition again reads the Euler axis only (a product vector iff $a_n$ multiplicative), and it is exactly $t$-blind, because $n^{-it} = \prod_p (p^{-it})^{v_p(n)}$ is a product of local unitaries, so every entanglement measure of $\psi_s$ is a function of $\sigma$ alone. The state can sit at $s = \rho$ on top of a zero and cannot tell (gates G13, G14).

## 3. Results

**(a) The identity, to the tail.** At $\beta = 3$ with primes to $10^5$: $S_\infty = 0.678502221866$ from mpmath; the mode sum $\sum_p S_p$ is $1.5\times10^{-10}$ below it and the truncated Shannon entropy $1.5\times10^{-9}$ below it. Both deficits are the exact tails: $\sum_{p > N} p^{-3}(1 + 3\log p) \approx 3/(2N^2)$ for the modes, and $-T + m(S - 1)$ with $T = \sum_{n > N} p\log(1/p) \approx 3\log N/(2N^2\zeta(3))$ for the truncated state.

**(b) The control cube.** $\beta = 2$, total correlation $C$ in nats:

| control | Euler | $a_n \ge 0$ | RH | $C(N{=}10^3)$ | $C(N{=}10^4)$ | $C(N{=}10^5)$ |
|---|---|---|---|---|---|---|
| $\zeta$ | yes | yes | numerically | $4.4\times10^{-4}$ | $4.9\times10^{-5}$ | $5.1\times10^{-6}$ |
| $A = \zeta L(\chi_{-15})$ | yes | yes | numerically (+GRH) | $5.6\times10^{-4}$ | $6.2\times10^{-5}$ | $6.5\times10^{-6}$ |
| Beurling fake | yes | yes | not posable (no FE) | $5.6\times10^{-4}$ | $6.0\times10^{-5}$ | $5.3\times10^{-6}$ |
| Epstein $Q_0$, $d=-15$ | no | yes | FALSE, $T^* = 12.04$ | $0.261$ | $0.261$ | $0.261$ |
| Epstein $Q_1$, $d=-15$ | no | yes | FALSE, $T^* = 24.48$ | $0.579$ | $0.579$ | $0.579$ |
| Epstein principal, $d=-47$ | no | yes | FALSE, $T^* = 24.66$ | $0.134$ | $0.135$ | $0.135$ |
| Epstein non-principal, $d=-47$ | no | yes | FALSE, $T^* = 32.05$ | $0.357$ | $0.356$ | $0.356$ |
| $B = L(\chi_{-3})L(\chi_5)$ | yes | **signed** | under GRH | undefined | | |
| Davenport-Heilbronn | no | **signed** | FALSE, $T^* = 85.70$ | undefined | | |

For the product states $C$ is the truncation artifact, decaying like $N^{-(\beta - 1)}$ (measured slopes 0.44 / 0.96 / 1.98 at $\beta = 1.5 / 2 / 3$); for the Epstein states it plateaus (converged to three digits at $N = 10^4$ for $\beta = 2$; at $\beta = 1.5$ the third digit still moves, $Q_1$: $0.667 \to 0.663$). Separation at $\beta = 2$, $N = 10^5$: 20,790x. The Beurling row is a product state by construction, so its zero is a vacuous pass of that discipline, which is the right outcome for a detector that claims no RH leverage. The two "undefined" rows are the signed corner: D-H's period-5 coefficients are $(1, \kappa, -\kappa, -1, 0)$ with $\kappa = 0.2841$, and $a_B(2) = -2$ (minimum $-36$ below $10^5$).

**(c) The sign pattern and the pencil's state window.** $f_\lambda = A + \lambda B$ (LEARNINGS #217; [`e_euler_pencil.md`](../criticality/e_euler_pencil.md)). The genus identity $r_{Q_0} = a_A + a_B$, $r_{Q_1} = a_A - a_B$ holds as exact integers for every $n \le 10^5$ (gate G3), and so does the sharper fact $|a_B(n)| = a_A(n)$ for every $n$ (forced prime by prime: for $\chi_{-15}(p) = 1$ both local factors give $k + 1$, for $\chi_{-15}(p) = -1$ both give $[k \text{ even}]$, for $p \mid 15$ both give 1). So $r_{Q_0}, r_{Q_1} \in \{0, 2a_A(n)\}$ and the Gibbs state of the pencil exists exactly for $|\lambda| \le 1$, the segment whose endpoints are the two Epstein forms of discriminant $-15$; the exits are witnessed by $r_{Q_1}(1) = 0$ (coefficient $-\epsilon$ at $\lambda = -1 - \epsilon$) and $r_{Q_0}(2) = 0$ (coefficient $-2\epsilon$ at $\lambda = 1 + \epsilon$). The census finds off-line zeros below height 200 at every grid point $|\lambda| \ge 0.01$; joint universality of the four characters mod 15 gives them at some height for every $\lambda \ne 0$; the smallest Lehmer threshold below 200 is $\lambda_c = 4.9\times10^{-4}$ (the pencil's S3 table), so for $0 < \lambda < \lambda_c$ the first off-line zero sits above 200. The density matrix is positive across the whole segment and the only Euler product on it is $\lambda = 0$.

**(d) The fold: $C$ against the census $T^*$.** $C(\lambda)$ is smooth, quadratic near 0 after subtracting the truncation floor $C(0) = 6.5\times10^{-6}$ (log-log slopes 1.99 and 2.01 on the two sides over $[0.01, 0.1]$) and monotone in $|\lambda|$ (gate G10). So within the pencil $C$ pins $|\lambda|$ and not the sign, and "$C(+\lambda) \approx C(-\lambda)$" is automatic (the measured asymmetry, 0.9 percent at $0.01$ and 1.8 percent at $0.025$, is the cubic term). The fair test is the fold: solve $C(\lambda') = C(+\lambda)$ for $\lambda' < 0$ by bisection and compare the census $T^*$ on the two sides (gate G9), $\beta = 2$, $N = 10^5$:

| $+\lambda$ | $\lambda'$ | common $C$ | $T^*(+\lambda)$ | census bracket of $\lambda'$ | $T^*$ there | ratio |
|---|---|---|---|---|---|---|
| $0.025$ | $-0.024761$ | $1.398\times10^{-4}$ | 43.384 | $[-0.025, -0.01]$ | $\le 24.952$ | 1.74 |
| $0.05$ | $-0.049128$ | $5.357\times10^{-4}$ | 43.391 | $[-0.05, -0.025]$ | $\le 13.805$ | 3.14 |
| $0.1$ | $-0.096648$ | $2.093\times10^{-3}$ | 20.737 | $[-0.1, -0.05]$ | $\le 13.799$ | 1.50 |

Equal $C$, different lowest off-line height. The converse holds too: the same pair (43.38) is $T^*$ at $\lambda = 0.01, 0.025, 0.05$ (spread $2.5\times10^{-4}$) while the floor-subtracted $C$ varies 25x (19x raw). Neither quantity determines the other. (The $T^*$ values are the pencil's, cited; the bracket convention takes the larger of the two census values around $\lambda'$.)

**(e) The geometry.** For $Q_0$: $D(p \,\|\, \text{product of marginals}) = 0.2614 = C$ to $10^{-16}$; $D(p \,\|\, \zeta\text{'s product state}) = 0.4564$ and $D(p \,\|\, A\text{'s}) = 0.4631$, with the Pythagorean residuals $D(p\|q) - C - \sum_p D(\mathrm{marg}_p\|q_p)$ at $10^{-15}$. The marginal product is the nearest Euler product by theorem; the numbers are the consistency check.

**(f) The rank-one costume.** $\sigma = 0.75$, $N = 2\times10^4$, entanglement entropy across $\{\text{mode } 2 \mid \text{odd part}\}$, at $t = 0$, $14.135$ and $85.699$:

| control | $\|\psi\|^2$ | $S_{\rm ent}$ | $t$-dependence |
|---|---|---|---|
| $\zeta$ | 2.598 | $8.83\times10^{-3}$ (floor) | none |
| $A = \zeta L(\chi_{-15})$ | 8.780 | $0.0505$ (floor) | none |
| $B = L(\chi_{-3})L(\chi_5)$ | 8.780 | $0.0505$, equal to $A$ to $10^{-12}$ | none |
| Epstein $Q_0$ / $Q_1$, $d=-15$ | 17.95 / 17.17 | $0.624$ / $0.665$ | none |
| Epstein principal / non-principal, $d=-47$ | 7.18 / 3.94 | $0.716$ / $0.662$ | none |
| Davenport-Heilbronn | 1.549 | $0.345$ | none |

Every control is a state here, D-H and $B$ included. $B$ equals $A$ because $|a_B| = a_A$ with multiplicative signs, which is a local unitary. The maximum deviation across the three $t$ values is $2.5\times10^{-15}$ (gate G14): the $t$-blindness is a theorem, verified bit for bit at the first zeta zero and at D-H's off-line height.

## 4. Reading

**Costume 1, sharpened to three statements.** (i) The Gibbs density matrix is available exactly where the Dirichlet coefficients are nonnegative, and coefficient positivity (the Gibbs convention) is neither necessary for RH ($B$, an Euler product satisfying RH under GRH, is signed) nor sufficient (every Epstein row is positive and RH-false); it is a sign convention, not a structural coordinate, since $B$'s signs are a local unitary on $A$ and under the rank-one costume every control is a state. (ii) The Gibbs state is diagonal, so the "quantum" in "quantum entropy" is inert there; the rank-one state is not diagonal, reaches $\sigma > 1/2$, and is exactly $t$-blind. (iii) In both costumes the one invariant is the distance to the Euler-product manifold, read by total correlation or by entanglement, and it reads the Euler axis of the cube and nothing else: not the additive lattice (on product states $C = 0$ whatever the prime logarithms), not the zeros (the fold).

**Two machine screens fire, and the regime observation is a third by hand.** The e3r polarity screen (#48): the positivity is unconditional. The entropic-export screen (#218, this probe): the export is nonnegative by construction, so there is no sign to flip; this is the #177 proposal, banked in [`breadth_corpus.py`](../lemma_db/breadth_corpus.py) as the `export_type` dimension (26/26). The regime is the #121 tier: the Gibbs state lives at $\beta > 1$, where an Euler product has no zeros, but the pencil's negative side has certified zeros inside the state's own half-plane (at $\lambda = -0.25$ the state exists at $\beta = 2$ while the census places a zero at $\mathrm{Re}\,s = 1.895$), and the entropy still does not see them. That sharpens the finding: the state and the zeros can share a half-plane and the export remains blind.

**Where it pays, and the representation reading.** The Gibbs state lives at $\beta > 1$ and the rank-one state at $\sigma > 1/2$; both are $t$-blind by local-unitary invariance, so neither can locate a zero even where it sits on one. The honest phrasing is representational: operations internal to the state (entropies, correlations, entanglement) are strip-blind, while the state itself carries every bit (the Gibbs weights determine $L$ and hence every zero by continuation, #111). Every density matrix is $e^{-\beta H}/Z$ for some $H$, so "the density-matrix costume is costume 2 (self-adjointness) at a temperature" is definitional rather than a discovery; the repo's KMS type III$_1$ row and #112 already say the non-diagonal thermal object is blind to the strip. What is new is the measured form: the sign-carrying structure the tariff demands (the shift $n \mapsto n + 1$, the adelic scaling flow) acts through $t$, and every entanglement measure is $t$-invariant by construction. The conservation law held without being reached.

**Correction to e3z.** e3z's Part C used "Epstein $d = -47$ principal: non-multiplicative but RH-TRUE" to show the product-state obstruction is necessary-not-sufficient. That witness is gone (#217). The reading survives on a better witness, the pencil: $f_\lambda$ is non-multiplicative for every $\lambda \ne 0$ while $T^*(\lambda)$ climbs without bound as $\lambda \to 0$, and $B$ is an Euler product with signed weights. e3z's "D-H is a statistical mixture of product states" also needs the sign: under the Gibbs convention D-H is not a state; under the rank-one costume it is one, with entanglement 0.35 on the Euler axis. Separability is automatic for every diagonal state and carries no information.

## 5. What was banked

Screen 14 (`export_type`: 'entropic' and 'torsion' fire, 'signed' does not, with the scope clause that the tag applies to the object handed to M4, not to an intermediate such as a sum rule's entropic term). Two corpus rows at the bottom of the ranking. The dated correction in e3z's docstring and runtime output. The rank-one costume and the fold as gates G9, G13, G14.

## 6. Limits

- The Gibbs state needs $\beta > 1$; the rank-one state needs $\sigma > 1/2$. Neither is defined on the line.
- Finite $N$: the product-state rows carry a truncation floor $\sim N^{-(\beta - 1)}$ (Gibbs) and a floor that grows with the coefficient size (rank-one: $\zeta$ $8.8\times10^{-3}$, $A$ $0.05$ at $N = 2\times10^4$). The plateau rows are converged to three digits at $N = 10^4$ for $\beta = 2$ only.
- The census $T^*(\lambda)$ is cited from the pencil (heights 1 to 200), not recomputed; the fold's negative-side $T^*$ is the larger census value bracketing $\lambda'$, not a value at $\lambda'$ itself.
- The Beurling fake has generalized primes to 15,000 only, so its generalized integers above 15,000 are undercounted; irrelevant to the product structure, which is what $C$ measures.
- The nearest-product comparisons restrict all product states to primes $\le N$.
- The quadratic law is fitted on $\lambda \in [0.01, 0.1]$ after floor subtraction; the $\lambda = \pm 0.001$ rows sit at the floor and are not used.

## 7. Gates

G1 diagonal state: von Neumann = Shannon ($2\times10^{-16}$). G2 the identity $S = \sum_p S_p$ against mpmath within the tail tolerance. G3 genus identity, $|a_B| = a_A$, and the endpoint witnesses, exact to $10^5$. G4 lattice enumeration equals `EpsteinZeta.dirichlet_coefficient` for both $d = -47$ forms, $n \le 60$. G5 product states decay below $2\times10^{-3}$. G6 Epstein plateaus above $0.05$, stable to 10 percent. G7 signed weights in both RH classes. G8 state window exactly $[-1, 1]$. G9 the fold (ratios 1.74, 3.14, 1.50) and its converse (one $T^*$ pair across 25x in $C$). G10 quadratic and monotone. G11 the I-projection identity to $10^{-9}$. G12 the Pythagorean identity to $10^{-9}$ for two product states. G13 every control is a rank-one state and entanglement reads the Euler axis ($B = A$ to $10^{-12}$). G14 exact $t$-blindness to $10^{-10}$.

Run: `python3 -m experiments.positivity.e3ac_entropic_exports [--quick]`. Artifact: `e3ac_entropic_exports.npz` (tables, the $\lambda$ sweep, the fold, the rank-one table, the cited $T^*$ column, provenance).
