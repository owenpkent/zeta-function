# Adversary report on `docs/03_research/negative_proof.md` (2026-09-01)

> Same-session hostile-referee pass (ADVERSARY role, opus) on the first draft of Sections 0-5 and 7 of the negative-proof document, before the pencil probe had run. Tracked here under the evidence rule (CLAUDE.md Conventions) because the document cites it as load-bearing. Disposition: all five blocking findings and all weakening findings were applied to the document the same day; the cosmetic findings were applied where they changed a statement. The one place the document departs from the report is finding 9: the Rodgers-Tao gloss was rewritten to say that the assumption $\Lambda < 0$ implies RH and so makes RH-conditional inputs available, which is how the argument obtains its contradiction, rather than dropping the mechanism sentence. Finding 1 (dangling probe citations) was resolved by the probe and dossier landing later the same session.

## Verified against

`experiments/LEARNINGS.md`, `experiments/primes/PRIME_PATTERNS.md`, `experiments/positivity/e3l_epstein_control.py`, `experiments/_shared/epstein_zeta.py`, `docs/03_research/rh_logical_status.md`, plus independent recomputation (genus decomposition to n = 200, Eisenstein dimension, Hecke-group covolume, Lehmer/dBN algebra, Li onset arithmetic).

## BLOCKS THE ARGUMENT

1. Header cited `e_euler_pencil.py`, `e_euler_pencil.md`, LEARNINGS #217: none existed at review time. Resolved by the probe landing.
2. P1 claimed $f_{\pm1}$ (Epstein $d = -15$) have off-line zeros below height 200. WRONG and already falsified in-repo: `e3l` records that $d = 15, 23$ have NO off-line zeros at reachable height. The stated warrant was wrong twice: $h(-47) = 5$, not 2, and the $d = -47$ witness is the NON-principal form, whose class group $C_5$ (one genus) admits no two-Euler-product decomposition. Applied: P1 rewritten as the opposite prediction; the $d = -47$ description corrected (three Euler products: $\zeta_K$ and two dihedral cusp-form $L$-functions).
3. "LEARNINGS #19 / #22" for the Gram-matrix detector and Epstein Li coefficients: WRONG citation. LEARNINGS line 1440 carries an explicit note that the Session-003 "Finding #19-#22" labels are session-local, not the canonical `### 19.` / `### 22.` headers; cite by experiment ID (`e3l`, `e3b4`). Content error: D-H has 4 negative Schur eigenvalues (one per off-line height below 200), Epstein non-principal $d = -47$ has 1, not "one each." Applied.
4. "A perturbative argument can never certify a boundary point's membership in the closed set either. So the proof, like the disproof, must be non-perturbative": WRONG and self-refuting. Hurwitz's theorem is itself a route to a closed condition by approximation from inside the closed set (Pólya / Laguerre-Pólya / Lee-Yang / de Bruijn-Newman at large $t$). Correct: an open-condition (stability) certificate cannot certify a boundary point; approximation from inside can. Applied to Section 7 item 4.
5. Closing paragraph "it broke where a disproof of a true $\Pi^0_1$ sentence has to break": question-begging (presupposes RH). Applied: rewritten.

## WEAKENS

6. Guth-Maynard exponent $30(1-\sigma)/13$ holds only for $3/4 \le \sigma \le 1$; near $1/2$ the binding bound is Carlson's, mid-strip Ingham's $3(1-\sigma)/(2-\sigma)$. Applied.
7. Bombieri-Hejhal 1995 is conditional (GRH for constituents plus a zero-spacing hypothesis). Applied.
8. "Rodgers-Tao: the infimum of collision times over all pairs is 0": WRONG. Unnormalized, trivial from Riemann-von Mangoldt; normalized, $\liminf$ of normalized gaps $= 0$ is open. Rodgers-Tao is a global ensemble statement. Applied: gloss removed, two-zero model labeled a caricature.
9. "against Montgomery's pair-correlation lower bounds": questioned as needing an unconditional input. Document response: under the contradiction hypothesis $\Lambda < 0$, RH holds and conditional inputs are available. Rewritten in that form.
10. "universality is the only mechanism that has ever produced an off-line zero": WRONG historically; Potter-Titchmarsh 1935 and Davenport-Heilbronn 1936 used Bohr almost-periodicity. Applied: "the Bohr / universality family."
11. "There is no non-constructive disproof of a $\Pi^0_1$ sentence": OVERSTATED. A disproof can be non-constructive with no witness bound; what holds is effectivizability by unbounded search. Name $\Sigma_1$-soundness. Applied.
12. "certifiable by a finite computation": the repo's `rh_logical_status.md` records the reverse-math calibration of the argument-principle counting step as open. Applied: qualified.
13. Hiding law "$x \sim 10^{150}$" is for $\beta = 0.6$; $\beta = 0.9$ needs only $x \gtrsim 10^{31}$. Applied.
14. $\delta^2$ log-log slope: prefactor $Z_0''/Z_B$ is pair-dependent; test the model ratio, not a raw slope. Applied to P3.
15. "In the pencil the same infimum statement is Voronin's": non sequitur (Voronin says nothing about which pairs collide or that off-line zeros continue on-line zeros of $A$). Applied: removed; P4 restated with the exit-through-the-top alternative.
16. Hurwitz paragraph: "can never make their sum vanish" is circular (it is RH); also $\sum_{a=1}^{q}$ vs $\sum_{(a,q)=1}$ conflated. Applied: reframed as a hypothesis of the tool; sums distinguished.
17. Hamburger hypotheses understated (finite order load-bearing; second series allowed on the mirror side); unify with the Hecke-group criterion at $\lambda = 1$. Applied.
18. Kaczorowski-Perelli: the D-H function lives in $\mathcal{S}^\#$, whose degree-1 classification gives linear combinations; "the FE alone" was used in two senses. Applied.
19. "every density estimate is a mean-value statement": Ingham fourth moment, Huxley/Heath-Brown large values, Guth-Maynard Fourier/large values. Applied: "mean-value or large-value."
20. "positive proportion" for $\gg T$ zeros: density-zero proportion of all zeros; say "positive lower density in $T$." Applied.

## COSMETIC

21. Polymath 15 bound is $0.22$, not $0.2$. Applied.
22. Voronin cite: pin to Voronin 1976 (Trudy MIAN 142) for Epstein; Karatsuba-Voronin chapter for the linear-combination result. Applied as stated.
23. "the pencil is the full Eisenstein space": the span is; the pencil is an affine line. Applied.
24. Weil converse theorem: twists over infinitely many moduli, Gauss-sum root numbers, vertical-strip boundedness, pole-allowing version (every pencil member has the pole at 1). Applied.
25. Landau oscillation: equivalence at the level of $\Theta = \sup\beta$. Applied.
26. Hurwitz's theorem needs "limit not identically zero." Applied.
27. Euler-product convergence $\iff$ RH needs locally uniform convergence for the reverse direction. Applied.
28. "provably / conjecturally zero-free" and "complement of two points": state that the strip zero-freeness is RH. Applied.
29. Section 2b's product remark is vacuous where it matters (tail convergence is RH). Applied: said so.

## CHECKED AND CLEAN

30. Hurwitz algebra ($\zeta = q^{-s}\sum_{a=1}^q \zeta(s,a/q)$; DFT formula for coprime $a$; the $q = 3$ identity). D-H 1936 for rational $a \ne 1/2, 1$; Cassels 1961.
31. $r_{Q_0}(n) = a_A(n) + a_B(n)$ and $r_{Q_1}(n) = a_A(n) - a_B(n)$ verified for all $n \le 200$ with zero mismatches.
32. Completed factor $15^{s/2}(2\pi)^{-s}\Gamma(s)$ with root number $+1$ for both $A$ and $B$; $Z_\lambda$ real; off-line zeros in pairs $(\rho, 1 - \bar\rho)$.
33. Hecke group $\langle z \mapsto z + 1, z \mapsto -1/(15z)\rangle \cong G(\sqrt{15})$, $\sqrt{15} > 2$, Fuchsian of the second kind, infinite covolume; level 5 likewise.
34. $\dim E_1(\Gamma_0(15), \chi_{-15}) = 2$; $S_1(\Gamma_1(N)) = 0$ for $N \le 22$; $\chi_{-15}$ odd.
35. Voronin joint universality statement; the tuple $(\zeta, L(\chi_{-15}), L(\chi_{-3}), L(\chi_5))$ is covered.
36. The Rouché construction with $h_2 = -\tfrac{c_1}{c_2}h_1(1 - \epsilon(s - s_0))$.
37. Carlson exponent $4\sigma(1-\sigma) < 1$ for $\sigma > 1/2$; Bohr-Landau $O(T)$ insufficient: correct.
38. Lehmer model: signs and prefactor exactly right.
39. dBN flow: $\partial_t H = -\partial_z^2 H$, collision at $t = -\delta^2/8$; RH $\iff \Lambda = 0$ given Rodgers-Tao.
40. Li onset $n \gtrsim \gamma^2/(\beta - 1/2)$; $n > 10^{25}$ at $\gamma > 3\times10^{12}$.
41. Platt-Trudgian $3\times10^{12}$ and 118,488,122 zeros to $5\times10^7$ match PRIME_PATTERNS; all six linked files exist; #174 and #201 correctly located, but #174 is the axiom census, not the GUE-blindness result (that is PRIME_PATTERNS Sections 5c-5d). Applied.
42. No em dashes; tone compliant except finding 5.

## Same-day CORRECTION by the adversary (after independent computation)

R1. Finding 2 RETRACTED. An argument-principle computation (discs of radius 0.05, 240-point contour, mpmath dps 25, $A + B$ evaluated through Hurwitz-zeta Dirichlet $L$-functions independently of `epstein_zeta.py`) gives winding number exactly 1 at $0.80001 + 12.0386i$ ($|F| = 4.2\times10^{-6}$ at the grid center) and at $0.92746 + 15.4966i$ ($1.1\times10^{-5}$), and winding number 0 at the module-reported $0.70074 + 84.76354i$ ($|F| = 1.155$). So $f_{+1}$ (principal form, $d = -15$) HAS off-line zeros below height 16; the doc's original P1 was right for the $+1$ endpoint. What survives of finding 2: the warrant was still wrong ($h(-47) = 5$; the $d = -47$ witness is the non-principal form). Severity: cosmetic.

R2. NEW, against the repo: the Session-003 Finding #19 sentence "the small class-number 2 and 3 discriminants ($d = 15, 23$) have NO off-line zeros at reachable height" (also in the `e3l` docstring) is false for the principal form of $d = -15$. (Resolution this session: the probe had tested the non-principal form `epstein_d15`; the sentence is corrected in place with a dated note.)

R3. NEW, against the repo: `epstein_zeta.py::zeros()` emitted a spurious root ($0.700741 + 84.76354i$, winding 0). Its positives need certification and its negatives are untrusted, including the $d = -47$ reconnaissance that feeds the Schur-counting law. (Resolution this session: a winding-number certification filter added to `zeros()`, and the $d = -47$, $-23$, $-15$ lists re-certified; see the dossier.)

R4. P1 half-refuted as originally written: $f_{-1} = A - B$ shows no off-line zeros below 200 in either scan. RETRACTED in the second correction below.

## Second correction (the completed census)

The adversary's first fast evaluator failed its own gate (a sign error on the Euler-Maclaurin half-term, diagnosed by the error scaling as $N^{-\sigma}$); its first census was withdrawn. The gated evaluator, with winding-number bisection and mpmath re-certification at 30 digits, gives for $0 < t < 40$, $\sigma > 0.502$:

| form | off-line zeros | mpmath $|Z_Q(\rho)|$ |
|---|---|---|
| $Q_0 = A + B$ (principal, $x^2 + xy + 4y^2$) | $0.8000108763 + 12.0385983586i$; $0.9274609514 + 15.4966339469i$; $0.6955863811 + 20.3459677100i$; $0.7402568735 + 33.7568500638i$ | $7.3\times10^{-7}$, $3.9\times10^{-7}$, $3.9\times10^{-7}$, $3.9\times10^{-7}$ |
| $Q_1 = A - B$ (non-principal, $2x^2 + xy + 2y^2$) | $0.7580708612 + 24.4828215241i$ | $2.6\times10^{-7}$ |

R4 RETRACTED: both endpoints have off-line zeros far below 200; P1 as first written is fully correct. R3 upgraded: against this truth the module's $T_{\max} = 200$ scan reported for $Q_0$ three zeros (12.04, 15.50, and a spurious 84.76) and missed 20.35 and 33.76; for $Q_1$ it reported none and missed 24.48. Both failure modes in one module. R2 sharpened: the Finding #19 sentence is false for both classes of $d = -15$, first zero at height 12.04. Scripts archived in `negative_proof_adversary_scripts/` (chk.py genus check; verify.py, w.py radius-0.05 certification; diag.py the sign-error diagnosis; fast2.py gated evaluator + census; loc.py bisection localization + mpmath certification).

Amended verdict: FAIL on the first draft for the bibliographic and rhetorical findings 1, 3, 4, 5 (all applied); the document's one testable prediction was right where the tracked ledger said it would be wrong.

## Verdict at review time

FAIL on the first draft (five blocking defects). The checked-and-clean core (items 30-41) is substantial. All blocking and weakening findings applied the same day; see the document header.
