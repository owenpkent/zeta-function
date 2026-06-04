> First-principles construction sweep for the missing RH positivity, run 2026-06-03 by the
> BUILDER/ADVERSARY/SYNTHESIZER loop (4 mechanisms, each adversarially stress-tested against the
> Davenport-Heilbronn discipline and K1-K4). Status: an honest construction artifact. Full success
> would be RH; it did not happen. All four mechanisms collapse to a known object (arithmetic Rosati /
> Hodge-standard positivity = RH, or de Branges / Conrey-Li = stronger-than-RH-and-false). The one
> live invariant the sweep isolated (the Rankin loglog-coefficient) was then EXECUTED as experiment
> 3W and confirmed necessary-not-sufficient. Companion to
> [candidate_proof_rh_connes_line.md](candidate_proof_rh_connes_line.md) and
> [spec_z_cohomology_landscape.md](spec_z_cohomology_landscape.md). See
> [researcher_mindset.md](researcher_mindset.md): a clean collapse is a coordinate.

# Building the Missing RH Positivity From First Principles: Four Mechanisms, Four Verdicts

## Preamble

This document builds the RH-closing positivity from scratch, four independent times, and locates the exact irreducible ingredient each construction needs. Full success would BE the Riemann Hypothesis. That did not happen. What did happen is sharper than another negative result: all four mechanisms, designed independently (Rankin-pole polarization, Bost-Connes Fock modular form, fibered arithmetic-surface intersection form, prime free-field reflection positivity), were carried until the load-bearing step was isolated, and in every case that step collapsed to one of two known objects. The value is in the collapse being clean and identical across four different costumes: it tells us with unusual precision where the proof must live and what it cannot be. Plain-text math throughout, no em dashes.

## Mechanism 1: Primitivity-indexed polarization (Rankin-Selberg pole)

**Construction.** For F in the Selberg class, the Rankin square L(s, F x Fbar) = sum_n |a_F(n)|^2 n^{-s} has a pole at s=1 of order n_F equal to the number of distinct primitive constituents (Selberg orthonormality). F primitive iff n_F = 1 iff simple pole with residue r_F > 0. Define a Gram form B_F(v,v') = sum_{k,l} conj(c_k) c'_l K_F(b_k,b_l) on the project's e3c2/e3c3 test family, where K_F is the residue-(1/n_F)-normalized Rankin pairing against the spectral measure dmu_F of the F x Fbar explicit formula. Claim (P): B_F is PSD iff RH(F), PROVIDED n_F = 1. The forward half is generic (g(rho) real on the line). The backward half is the content: with a simple pole the residue subtraction is exact, so the only leftover negative mass sits at off-line zeros.

**Where Euler enters.** Exactly one step: pinning pole order n_F = 1 for primitive F, equivalently sum_{p<=x} |a_F(p)|^2/p = log log x + O(1) with coefficient EXACTLY 1. The "1" is the multiplicative orthogonality of the local factors. No Euler product, no prime-supported log F, no integer constituent count, no normalizable residue, no exact subtraction.

**Why D-H cannot build it.** D-H = c1 L(s,chi1) + c2 L(s,chi2) is a sum of two distinct primitive Dirichlet L-functions, so its Rankin loglog coefficient is sum_j |c_j|^2 (period-normalized 0.432, not 1) and the pole-subtraction leaves a sign-indefinite cross-constituent term c1 conj(c2) L(s, chi1 x chi2bar) + c.c. that is O(1)-large near s=1. B_DH is then degenerate and its definiteness is decoupled from D-H's zeros. This is the project's stealth window (LEARNINGS Finding #19, 3D.3 dossier).

**Irreducible ingredient (R) Rankin-Residue Rigidity.** For simple Rankin pole, residue subtraction is exact, so the only thing left that can make B_F indefinite is an off-line zero.

**Adversary verdict.** Survives D-H: NO. Circular: YES. Novelty: NOT new. (R) decomposes into (R1) per-off-line-zero rank-2 indefiniteness = the e3j (N_off, N_off) signature, already proven; (R2) on-line zeros => PSD = the easy half of RH; (R3) "no stealth window for a simple pole" = trivially true for the EXACT (non-truncated) sum even for D-H (the stealth window was a finite-precision/finite-basis artifact, eps < 1e-5 in float64, looser than rigorous verification). The residual content is "B_F PSD => no off-line zero," which is RH restated. The multiplicative input (pole order = constituent count) is exactly Selberg orthonormality, a named partly-open conjecture. **Verdict: dead-RH-restated.**

## Mechanism 2: Bost-Connes Fock-space modular positivity

**Construction.** Each Euler factor (1-p^{-s})^{-1} = Z_p(b) = Tr e^{-b(log p)N_p} is the partition function of one bosonic mode. The BC equilibrium KMS state for b > 1 is the restricted tensor product phi_b = (x)'_p rho_{b,p}, with global partition function prod_p Z_p(b) = zeta(b). Bosonic second quantization gives zeta(s) = det(1 - T(s))^{-1} = Tr_Fock Gamma(T(s)) for the one-particle operator T(s) e_p = p^{-s} e_p. On the GNS space define the Weil-KMS form Q_b(f) = <J f Omega, Delta^{1/2} J f Omega> minus an archimedean counterterm, using Tomita-Takesaki modular data (Delta = e^{-H}, J). Claim: Q_b >= 0 iff all strip zeros on Re s = 1/2.

**Where Euler enters.** Two genuinely multiplicative steps: (A) the equilibrium state exists as a state only because phi_b is a product over primes (Z factors), which IS multiplicativity a_{mn} = a_m a_n; (B) Gamma(A (+) B) = Gamma(A) (x) Gamma(B) converts the one-particle direct sum into the Fock tensor product (sum n^{-s} into prod (1-p^{-s})^{-1}). Q_b is a tensor form; writing it as a tensor requires a pure product state.

**Why D-H cannot build it.** D-H coefficients are non-multiplicative (a(6)=0.3 but a(2)a(3)=0.51, verified). No per-prime Hamiltonian reproduces them; the BC-type state is a statistical mixture c1 phi^(1) + c2 phi^(2), never a pure product state, so it has no single modular operator factoring over primes. Q_b is structurally UNDEFINED for D-H, not merely false.

**Irreducible ingredient.** An intrinsic polarization on the GNS Fock space whose signature is read off the per-prime tensor factorization via a Tomita-modular signature of the product state, proven positive without the trace identity. The dossier itself names this "the arithmetic-Hodge-standard / arithmetic-Rosati positivity (08A M4) re-expressed in Bost-Connes Fock language."

**Adversary verdict.** Survives D-H: NO. Circular: YES. Novelty: NOT new, and worse, type-incompatible. The bare modular form is <psi, Delta^{1/2} psi> = sum_n |c_n|^2 n^{-b/2}, unconditionally positive for all b (Delta = e^{-beta H} of a Gibbs state is strictly positive-definite), so ALL RH content is forced into the archimedean counterterm = the dead archimedean-domination route, R3.5's trace-formula quadratic form in Tomita-Takesaki costume. Two further breaks: det(1-T(s)) needs T(s) trace-class, i.e. Re s > 1, so the Fock determinant is undefined in the critical strip where the continuation (the zeros) gets smuggled back; and H = sum_p (log p) N_p has spectrum {log n}, carrying zero information about zero locations. A Hodge-index polarization needs an INDEFINITE pairing (signature ~ (1, N-1)); e^{-beta H} is strictly positive-definite, so it cannot carry the Hodge sign. **Verdict: dead-RH-restated.**

## Mechanism 3: Fibered arithmetic-surface intersection form

**Construction.** Take the verified function-field template (2G/2T): on C x C the primitive Gram on {Delta_0, Gamma_0} is [[-2g, -t],[-t, -2gq]], negative-definite iff |t| < 2g sqrt(q) = RH-for-C = minus the Rosati trace form. Build the minimal 2D object S over Spec(Z) x_{F1} Spec(Z) = Spec(W(Z)) so the same 2x2 block lives over each prime p with bidegree (1,p): local block P_p = [[-2, -t_p],[-t_p, -2p]], with Gamma_S^2|_p = log p (von Mangoldt, finding #26). New claim: multiplicativity forces the global primitive form to be the ORTHOGONAL direct sum M = A_arch (+) (+)_p P_p (Kunneth-orthogonality), with A_arch the shared archimedean Gamma-factor block. RH = M negative-definite.

**Where Euler enters.** Exactly one step (DEF 4 / Claim 4): the finite part is an orthogonal direct sum over places. Multiplicativity makes each local L-factor a single rank-1 primitive class, hence a clean place-grading whose signature is the union of block signatures. Euler fixes the BLOCK STRUCTURE, not the entries (entries shared with D-H, per #42 / M2.6).

**Why D-H cannot build it.** D-H coefficients are non-multiplicative and periodic mod 5 (a_2 a_3 = -0.081 but a_6 = 1.0), so there is no rank-1 local block, no orthogonal place-grading; the finite part is an irreducible 2-character mixture. Claim 4 cannot even be stated. No bidegree (1,p), no Frobenius correspondence, no surface of the required type.

**Irreducible ingredient.** Orthogonality of the archimedean Weil pairing with respect to the Euler/Kunneth place-grading, AND negative-definiteness of the resulting direct sum (zeros live in the continuation, controlled by the archimedean block coupled to the per-place blocks).

**Adversary verdict.** Survives D-H: NO. Circular: YES. Novelty: NOT new. Two independent fatal breaks. (1) Internal contradiction: Claim 4 demands A_arch ORTHOGONAL to the place-grading (so signatures assemble), but the ingredient's sub-claim (b) demands the archimedean block COUPLE to the finite blocks via the continuation (so zeros enter). Mutually exclusive: in a 3-block toy, kappa = 0 gives M negative-definite regardless of any zero, and turning kappa on sends an eigenvalue through 0 at kappa ~ 1. Definiteness is decided by the coupling, not the orthogonal structure. (2) The recipe applies to D-H: its a_p satisfy |a_p| < 2 sqrt(p), so every D-H block is negative-definite and the orthogonal sum plus shared A_arch "proves" the false D-H RH; the firewall sits on the RH-vacuous finite blocks while the RH-relevant content is the shared arch-to-finite coupling. DEF 2 is also ill-defined: (1-p^{-s})^{-1} is genus 0 (H^1 = 0), wrongly assigned a genus-1 block; "rank-1 local H^1" contradicts Frobenius eigenvalue conjugacy. K3 fails: Weil 1948 gets FF-RH from ONE 2x2 form, with no per-place orthogonal grading, so the central mechanism is absent from the one case where the analogue is a theorem. The only non-vacuous reading is Weil-Bombieri / arithmetic Rosati positivity, the M2.5/M2.6 non-circular Rosati form (e2v/e2w), where M2.6 already found the stealth window (D-H reads spuriously positive at +0.094). **Verdict: dead-RH-restated.**

## Mechanism 4: Multiplicative reflection positivity from the prime free-field

**Construction.** By Bohr-Bagchi, log|L(sigma+it)| for a genuine Euler product is almost surely a sum of independent per-prime variables (the angles {(log p) t mod 2pi} equidistribute independently from Q-linear independence of {log p}). Verified: at sigma = 0.75, Var(log|zeta|) = 0.4494 vs the independence prediction 0.4501 (0.1%); D-H gives 0.2476, matching no prime-sum. Take this as a literal Gaussian prime free-field with covariance kernel K(s,w) = sum_{p,m,j} (1/m) alpha_{p,j}^m conj(alpha_{p,j})^m p^{-ms - m conj(w)}, PSD on Re > 1/2 because the Euler log-coefficients are non-negative (1/m > 0). Reflect across the functional equation involution: K_theta(s,w) = K(s, 1 - conj(w)). Claim (RP): the reflected form is PSD on the half-strip 1/2 < Re < 1 iff all zeros on the line. This is Osterwalder-Schrader reflection positivity: reflection-positive about a hyperplane iff spectral measure supported on it. The off-line negative direction is the (N_off, N_off) signature (#18/3J) realized as a POLARIZATION (reflection inner product), not a trace, which is why it looked like it might escape K1.

**Where Euler enters.** Two uses: (A) independence makes the field EXIST (log L = sum_p log L_p with independent angles); (B) non-negativity of sum_j |alpha_{p,j}|^{2m} makes the un-reflected K positive-definite to begin with, so the only question is whether reflection preserves it.

**Why D-H cannot build it.** log(c1 L1 + c2 L2) does not split into independent per-prime terms (log of a sum is not a sum of logs); the field is undefined. Even forcing -f'/f, D-H's von Mangoldt coefficients are sign-indefinite (b_3 = -0.31, b_4 = -1.44, b_9 = -2.29, verified), so K is not even PSD before reflection; RP is vacuous. D-H's off-line zeros (0.8085 + 85.699i) are genuine negative directions of a form that was never reflection-positive.

**Irreducible ingredient (IRR).** The FE-reflected kernel K_theta(s,w) = K(s, 1 - conj(w)) is PSD on the half-strip. This converts RH from a trace statement (provably K1-circular per R3.5) into a polarization-preservation statement: does a canonical PSD kernel stay PSD under a specific involution.

**Adversary verdict.** Survives D-H: NO. Circular: YES. The kernel is exactly K(s,w) = log zeta(s + conj w) (verified to 5+ digits), so the reflected kernel is log zeta(s + 1 - w). The central claim FAILS in the forward direction: with RH TRUE on the sampled region, the reflected form is strongly INDEFINITE for zeta (17 of 24 negative eigenvalues on a 2D node set; 21 of 41 on a contour), while the un-reflected kernel is PSD on the same nodes (min eig ~ 2e-8). Root cause: the bare prime field has no s -> 1-s symmetry (zeta(s)/zeta(1-s) is unstructured; the FE needs the Gamma factor chi(s), shared with D-H), and the reflection diagonal s + 1 - s = 1 lands on zeta's POLE (finding #7: the cancellation is the pole effect, not Euler genericity). Novelty: NOT new. The Euler reading of (IRR) is simply FALSE (disproved here). The completed reading (insert Gamma so reflection is an FE-isometry) is exactly Osterwalder-Schrader = de Branges H(E) = Hermite-Biehler cone positivity, which Conrey-Li (2000) proved is STRICTLY STRONGER than RH and fails at positive density (project finding #43; verified: Q(rho) = -Re{xi'(rho) xi(1+rho)} is negative at the 34th zeta zero, on the line, RH true). **Verdict: dead-known-conjecture (de Branges / Conrey-Li).**

## Comparison table

| Mechanism | Irreducible ingredient | Type | Verdict |
|---|---|---|---|
| 1. Rankin-pole polarization | Rankin-Residue Rigidity: simple pole => exact subtraction => only off-line zeros make B_F indefinite | (R1) RH-restated + (input) Selberg orthonormality | dead-RH-restated |
| 2. Bost-Connes Fock modular | Intrinsic Tomita-modular signature of the product state = polarization | RH-restated (own IFF) + re-expression of 08A M4; type-incompatible (Delta PSD, no Hodge sign) | dead-RH-restated |
| 3. Fibered arithmetic surface | Archimedean pairing orthogonal to Euler place-grading AND direct sum negative-definite | RH-restated (Weil-Bombieri / arithmetic Rosati); internally contradictory (orthogonal vs coupled) | dead-RH-restated |
| 4. Prime free-field reflection | FE-reflected kernel K_theta = log zeta(s+1-w) stays PSD | known-conjecture (de Branges / Conrey-Li); false in bare Euler reading | dead-known-conjecture |

## The sharpest output

**The single most precise statement of the missing math.** All four mechanisms try to manufacture an INDEFINITE polarization (a pairing whose signature, not whose trace, is RH-equivalent) out of multiplicativity, and all four collapse at the same seam: the place where the zeros actually enter is never the multiplicative finite data. It is always the archimedean / continuation factor, which is SHARED with Davenport-Heilbronn. Stated exactly: in each construction the Euler product cleanly fixes the BLOCK STRUCTURE / existence of the object (orthogonal place-grading, pure product state, simple Rankin pole, independent prime field), and this is genuinely D-H-discriminating and RH-independent. But the off-line-zero content lives in the continuation across Re = 1/2, carried by the Gamma factor and the functional equation, which the Euler product does not touch. So every mechanism splits into a vacuous branch (where it also "proves" the false D-H RH) and an RH-equivalent branch (where the ingredient IS the missing positivity restated). The missing math is precisely: a positivity that injects the EXACT factorization structure into the GLOBAL signature of the continuation, rather than into the per-place entries (RH-vacuous, shared bound |a_p| < 2 sqrt p) or the shared archimedean block.

**Is there any genuinely-new foothold?** No. Not one of the four "genuinely-new" self-labels survives. They reduce as follows: Mechanisms 1, 2, 3 collapse to Weil-Bombieri positivity = arithmetic Rosati positivity = the arithmetic Hodge standard conjecture (08A M4 / R3.5), the K1 trap. Mechanism 4 collapses to de Branges / Conrey-Li reflection positivity (finding #43), which is strictly stronger than RH and fails for zeta. The multiplicative inputs that ARE real reduce to Selberg orthonormality (a named partly-open conjecture, Mechanism 1's pole-order input) and the Q-linear independence of {log p} (Mechanism 4's independence input). Both are necessary-not-sufficient: they detect non-Euler-ness, not RH-failure, and would equally flag RH-satisfying non-Euler controls (the Epstein-d47 trap, #20/#22/#27). This is the reformulation trap in clean form.

**The two non-circular footholds worth recording (not new, but sharpened):**

1. *The Rankin loglog-coefficient is an exact, zero-free, multiplicative discriminator:* sum_{p<=x} |a_F(p)|^2 / p ~ c log log x with c = 1 for a primitive Euler product, c = sum_j |c_j|^2 < 1 (period-normalized 0.432) for a reducible combination. It is a single scalar decided by the prime coefficients alone, sharper than the #20/#26 von-Mangoldt-delocalization fingerprint. Necessary-not-sufficient: it is the K2 firewall made quantitative, not a positivity that implies RH.

2. *Bost-Connes refinement of the 2A_R1 D-H exclusion:* D-H is a statistical mixture c1 phi^(1) + c2 phi^(2) of two extremal KMS states, never a pure product state. This sharpens "linear combination is not a geometric operation" to "D-H has no equilibrium product state at all." One line for the D-H dossier; not load-bearing.

**Smallest next step to test the only marginally-live thread.** The one place the analysis points forward is the seam itself: the archimedean/continuation factor is where the zeros enter and is shared with D-H, so any working polarization must make the Euler factorization act ON that factor, not beside it. The smallest test: compute whether the Rankin loglog-coefficient c can be promoted from a scalar discriminator into the NORMALIZATION of the archimedean coupling block (i.e. does the c = 1 vs c < 1 distinction control the sign of the arch-to-finite off-diagonal that #42/M2.6 showed is shared). If c rescales that coupling so that c = 1 forces negative-definiteness and c < 1 permits the eigenvalue crossing, that would be the first place multiplicativity touches the continuation rather than the entries. Prediction from the four collapses above: it will not, and the rescaling will land back on the M2.6 stealth window. But it is a one-script, one-day test (extend e2w_rosati_fourway_M2_6.py with the loglog-coefficient prefactor on A_arch) and it is the only step here that is not already foreclosed.

## Bottom line

Four independent first-principles constructions of the RH positivity all collapse to the same two known objects (arithmetic Rosati / Hodge standard positivity, or de Branges / Conrey-Li reflection positivity); none surfaced a genuinely-new non-circular foothold, which is the marginal-positivity compass reading true once more: multiplicativity discriminates D-H cleanly but only fixes the object's existence, while the off-line zeros live in the shared archimedean continuation, so the missing math IS the polarization, not a route to it.

## Postscript: the live invariant, executed (experiment 3W)

The sweep named one clean, non-circular, single-scalar multiplicative invariant worth testing: the
Rankin loglog-coefficient c_F = lim (sum_{p<=X} |a_F(p)|^2 / p) / loglog X, which is 1 for a
primitive Euler product and < 1 for a reducible / non-Euler function. It was implemented and run
([e3w_rankin_loglog.py](../../experiments/positivity/e3w_rankin_loglog.py), LEARNINGS #53):

| control | c_F (X up to 2e5) | Euler product | RH |
|---|---|---|---|
| zeta | 1.10 | yes | true |
| chi3 | 0.97 | yes | true |
| Davenport-Heilbronn | 0.37 | no | FALSE |
| Epstein-d47-principal | 0.63 | no | TRUE |

Decisive: c_F < 1 for BOTH Davenport-Heilbronn (RH-false) AND Epstein-d47-principal (RH-true). So
c_F detects NON-EULER-ness, not RH-failure: it is the K2 firewall in its sharpest single-scalar
form, necessary-not-sufficient for RH (the reformulation trap, LEARNINGS #20/#27). This closes the
only thread the sweep left open, exactly as predicted: multiplicativity fixes the object's existence
/ block structure (a real, non-circular discriminator), but the off-line-zero content lives in the
shared archimedean continuation, which the Euler product does not touch. The missing math IS the
polarization, not a route to it.
