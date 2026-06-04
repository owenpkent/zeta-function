# Reading notes: Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time* (arXiv:2602.04022v1, 3 Feb 2026)

> Section-by-section notes on Connes' Feb-2026 commissioned RH survey and its research kernel (the
> "Letter to Riemann": a constructive reframing of Weil positivity via the minimal eigenvector of the
> truncated Weil quadratic form). These notes are the "what the paper says" companion to the project's
> ASSESSMENT [`connes_2602_letter_to_riemann.md`](../connes_2602_letter_to_riemann.md) ("how it lands
> on the project: Theorem 6.1 is zeta-blind, the content is the unproven RH-equivalent convergence").
> Distinct from the 1998 NCG paper [`Connes-1998-Trace-Formula-NCG-Zeros.md`](Connes-1998-Trace-Formula-NCG-Zeros.md):
> 1998 = zeros as an absorption spectrum + the global trace formula <=> RH; 2026 = a CONSTRUCTIVE
> extremal route (extremize the Weil form) plus the information-theory (Slepian/Shannon) bridge and a
> UV spectral model. Mapped to the four-level framing (RH = Level 4 positivity), the Davenport-
> Heilbronn discipline, the marginal-positivity thesis (e3v: the margin is e^{-4 pi x}), and the
> project experiments e3s/e3t/e3u/e3v that instrument it. Page refs are to the 42-page arXiv PDF.

## One-line takeaway

The survey's research kernel is a single constructive move: restrict the Weil quadratic form $QW_\lambda$
to test functions supported in $[\lambda^{-1},\lambda]$ (only primes $\le x=\lambda^2$ enter), take its
minimal eigenvector $\eta_x$, and **Theorem 6.1 (Connes-van Suijlekom)** proves the Fourier transform
$\hat\eta_x$ has all zeros real (on the critical line) for each finite cutoff. With primes $\le 13$ this
recovers the first 50 zeta zeros to accuracies $2.6\times10^{-55}$ down to $10^{-3}$. RH would follow IF
$\hat\eta_x \to \Xi$ (Riemann's $\Xi$) as $x\to\infty$ (then Hurwitz). That convergence is the one
unproven step; Connes states it plainly ("not proved"). The rest is a survey plus a new
information-theory reading (the explicit-formula machinery = Shannon/Slepian time-/band-limiting) and a
UV spectral model (the prolate operator's self-adjoint extension reproduces the large-zero asymptotics).

## Technical content (section by section)

**Abstract + §1 Introduction (pp.1-6).** Commissioned survey; "a new perspective emerged during its
preparation." The centerpiece is a three-page letter to Riemann using only mathematics available in
1859 plus modern computers. Roadmap of the survey: classical analytic NT; entire-function theory;
Weil's Rosetta stone (Riemann surfaces / curves over $\mathbb{F}_q$ / arithmetic $\mathrm{Spec}\,\mathbb{Z}$,
unified as regular dimension-one schemes); automorphic/Langlands; RMT/quantum chaos and the missing
"ultraviolet model" (flagged for §7.6); Connes' own 1998 trace formula (zeros as absorption spectrum
on the adele class space); equivalent formulations and the Godel/Chaitin angle. The semilocal adele
class space $Y_S = \prod_{v\in S}\mathbb{Q}_v / \Gamma$, $\Gamma=\{\pm\prod p^{n_v}\}$, is previewed:
its multiplicative and additive Haar measures are no longer mutually singular (a measure-theoretic
advantage over the full adele class space), and each prime $p\in S$ gives a periodic orbit of length
$\log p$. The Moscovici joint work [27] is previewed: the self-adjoint extension of the prolate
operator reproduces the UV behavior of the squares of zeta zeros.

**§2 Encounter with the Riemann zeta function (pp.6-12).**
- *2.1 Classical analytic NT.* Chebyshev 1852 bounds; $\vartheta,\psi$; $\psi(x/n)$ sum = $\log(x!)$
  + Stirling. PNT $\Leftrightarrow \vartheta(x)\sim x$; Hadamard / de la Vallee Poussin prove
  $\zeta(1+it)\ne0$ via the $(-1)^2=1$ phase argument (if $\zeta(1+it)=0$ then $p^{-2it}\to1$ forces a
  pole at $1+2it$). Landau Tauberian -> Wiener-Ikehara -> Newman. Selberg-Erdos elementary PNT (1949)
  and the Selberg symmetry formula $\sum_{p\le x}\log^2 p + \sum_{pq\le x}\log p\log q = 2x\log x+O(x)$.
  Riemann's $f(x)=\mathrm{Li}(x)-\sum_\alpha(\mathrm{Li}(x^{1/2+\alpha i})+\dots)$ (eq.1), with the
  CAREFUL branch handling (von Mangoldt's $\mathrm{Li}(e^w)$ = Ei). Littlewood: $\pi(x)-\mathrm{Li}(x)$
  changes sign infinitely often. Hardy (infinitude on the line), Selberg 1942 (positive proportion),
  modern proportions; zero-free regions, Lindelof.
- *2.2 Entire/meromorphic function theory.* Hadamard factorization; Nevanlinna; Borchsenius-Jessen /
  Bohr-Landau almost-periodic program; average of $\log|\zeta|$ and zeros of $\zeta(s)-x$. *Voronin
  universality* (the "chameleon"): in $1/2<\mathrm{Re}(s)<1$, vertical translates of $\zeta$ approximate
  any continuous nonvanishing holomorphic target on a compact simply-connected set.

**§3 A century and a half of theory building (pp.13-20).**
- *3.1 Harmonic/functional analysis* (Hilbert spaces, scattering/spectral interpretation).
- *3.2 Algebraic/arithmetic geometry:* Weil's $\mathbb{F}_q$ proof; Grothendieck schemes + etale
  cohomology; motives. The Rosetta-stone three texts as dimension-one regular schemes.
- *3.3 Automorphic/representation theory:* adeles/ideles (Weil, *Basic Number Theory*); Langlands
  (motivic L = automorphic L => GRH would give RH for all motivic L); modular forms, Ramanujan-Petersson
  (Deligne) $|a_p|\le 2p^{(k-1)/2}$ = RH at the Euler-factor level; **Selberg trace formula** and the
  Selberg zeta $Z_\Gamma(s)=\prod_p\prod_k(1-e^{-(s+k)\ell(p)})$ -- note the explicit-formula-like
  $\sum \Lambda(n)/\sqrt n\, g(\dots)$ terms appear with the OPPOSITE (positive) sign vs the explicit
  formula's minus sign (the minus-sign discussion of [59] §12, extended to semiclassics in [3]).
- *3.4 RMT / quantum chaos:* Montgomery pair correlation $1-(\sin\pi u/\pi u)^2$ = GUE (Dyson);
  Odlyzko's numerics near the $10^{20}$-th zero; the local rescaling by $\log(T/2\pi)$ needed to compare
  with GUE -- "any correspondence must be inherently local and cannot arise from a simple fixed spectral
  operator" (THE gap addressed in §7.6); Berry-Tabor / quantum chaos; Katz-Sarnak density (U/O/Sp
  symmetry types, proven over $\mathbb{F}_q$ via Deligne equidistribution); Keating-Snaith moments
  $c_k=a_k f_k$, $f_k$ = RMT $k$-th moment of $|\det(I-U)|^2$, $a_k$ = arithmetic Euler factor.
- *3.5 NCG:* Connes' 1998 trace formula on $\mathbb{A}/\mathbb{Q}^*$, zeros as absorption spectrum;
  knots/primes (Mazur-Mumford): each prime $\to$ periodic orbit $C_p$ of length $\log p$, $\pi^{-1}(C_p)$
  = mapping torus of $r^*_{\mathrm{Frob}_p}$ on $\pi_1^{et}(\mathrm{Spec}\,\mathbb{Z}_{(p)})^{ab}$; the
  scaling site / characteristic-one structure sheaf. A recent result [13]: the $C^*$-algebra encoding
  is faithful (non-isomorphic number fields => non-isomorphic $C^*$-algebras).
- *3.6 p-adic/motivic:* Kubota-Leopoldt $\zeta_p$, Iwasawa main conjecture (Mazur-Wiles), no $p$-adic RH;
  Bloch-Kato / BSD / Beilinson.
- *3.7 Computational:* the verification history (Riemann ... Platt 2021 up to height $3\times10^{12}$);
  Riemann-Siegel + Turing's method; Odlyzko-Schonhage.

**§4 Equivalent formulations (pp.20-23).**
- *4.1 Weil positivity.* The explicit formula in $\mathbb{R}^*_+$/$\mathbb{R}$ Fourier form:
  $\hat f(i/2)-\sum_{1/2+is\in Z}\hat f(s)+\hat f(-i/2)=\sum_v W_v(f)$, with local terms
  $W_p(f)=(\log p)\sum_m p^{-m/2}(f(p^m)+f(p^{-m}))$ (eq.9) and the archimedean $W_\mathbb{R}$ (eq.10).
  **Weil's equivalence:** RH $\Leftrightarrow \sum_v W_v(g\ast g^*)\le0$ for all $g$ with
  $\hat g(\pm i/2)=0$. KEY: $W_p$ vanishes on functions supported in $[p^{-1},p]$, so the criterion
  involves only FINITELY many primes at a time. Yoshida's theorem [111]: $W_\infty(f)\ge0$ for positive-
  definite $f$ supported in $(1/2,2)$ with $\hat f(\pm i/2)=0$ -- but by numerical analysis of the
  functional, "no conceptual reason that would continue to hold when primes are involved."
- *4.2 Beurling-Nyman* ($L^2(0,1)$ density of $\{\theta/x\}$ combinations).
- *4.3 Li's criterion* $\lambda_n=\sum_\rho(1-(1-1/\rho)^n)\ge0$.
- *4.4 Robin / Lagarias* ($\sigma(n)<e^\gamma n\log\log n$ for $n>5040$; $\sigma(n)<H_n+e^{H_n}\log H_n$).
  The logical-status discussion: these put RH in the "provable-if-true" class Hilbert hoped for, which
  Godel/Chaitin show need not be provable; algorithmic-complexity barriers to direct arithmetic checking.

**§5 A Letter to Professor Bernhard Riemann (pp.23-25).** Written after a pilgrimage to Selasca
(where Riemann died, 1866). Two parts:
- *Preliminary remark:* the middle term of Riemann's formula is mis-written in textbooks (Edwards) as
  $\sum\mathrm{Li}(x^\rho)$ -- nonsensical because $x^\rho$ is unchanged under $\rho\mapsto\rho+2\pi i
  n/\log x$, so the sum has infinitely many repeated terms; von Mangoldt's $\mathrm{Ei}(\rho\log x)$ of
  the correct variable $\rho\log x$ is the right object.
- *The new content:* with primes $\{2,3,5,7,11,13\}$ only, fabricate the quadratic form $Q(\varphi)$ on
  functions $\varphi$ supported in $[1,13]$, $Q(\varphi)=$ explicit formula applied to
  $\psi(v)=\int\varphi(u)\varphi(uv)\,du/u$ (so $\psi$ supported in $[1/13,13]$, only prime powers
  $\le 13$ used -- the analogue of Riemann's Dirichlet-principle quadratic form in the conformal-mapping
  proof). Let $\eta$ minimize $Q$ with $\int\varphi^2 du/u=1$ (existence as in Hilbert 1900 "Uber das
  Dirichletsche Prinzip"). Take the Mellin transform of $\eta$; its zeros are PROVABLY on the critical
  line (§6.1), modulo uniqueness of the minimum (a Caratheodory-Fejer / Toeplitz theorem from 1911:
  assume the lowest eigenvalue is simple and even). **The amazing fact:** the first 50 zeros of
  $\hat\eta$ match the zeta zeros -- 54 decimals on the first zero, decreasing slowly. The reported
  DIFFERENCES (primes $\le 13$): first zero $2.6\times10^{-55}$ ... 50th $\approx 2\times10^{-3}$. Chance
  probability $\approx 10^{-1235}$ ($\sim$ guessing 4000 coin tosses). What is NOT known: that as the
  cutoff $x\to\infty$ the zeros converge to zeta's. The hoped-for route: $\eta_x\to$ (the function whose
  Mellin transform is $\Xi$), then Hurwitz (a uniform limit of functions with zeros on a fixed line has
  zeros on that line) gives RH.

**§6 The strategy and the next small steps (pp.26-30).**
- *6.1 (PROVEN) Theorem 6.1 (Connes-van Suijlekom, [32] "Quadratic Forms, Real Zeros and Echoes of the
  Spectral Action").* For $L>0$, a real distribution $D$ on $[0,L]$, even extension $\tilde D$ on
  $[-L,L]$: if the form with Schwartz kernel $\tilde D(x-y)$ is a lower-bounded self-adjoint operator on
  $L^2([-L/2,L/2])$ whose spectral minimum is a simple isolated eigenvalue with EVEN eigenfunction
  $\eta$, then ALL zeros of the entire function $\hat\eta(z)$ are real. Proof: the special (Toeplitz)
  form of the matrix in the trigonometric basis + a finite-matrix self-adjoint construction + Hurwitz.
  Finite truncations let one approximate $\hat\eta$'s zeros by the spectrum of a rank-one perturbation
  of the periodic Dirac operator (Dirichlet kernel); used at $N=100$ in the letter's computation.
- *6.2 (PROVEN) Fact 6.2.* $\Xi(t)$ is the Fourier transform of $k=E(h)$, where $E(f)(u)=u^{1/2}\sum_n
  f(nu)$ and $h$ is (up to scalar) the unique vanishing-integral combination of the Hermite functions
  $h_0,h_4$ (eigenfunctions of the harmonic oscillator $H=-f''+4\pi^2u^2 f$, even for $n$ even, FT-
  invariant for $n\equiv0\bmod4$). $k(u)=u^{1/2}\frac{\pi}{2}\sum n^2u^2(2\pi n^2u^2-3)e^{-\pi n^2u^2}$.
- *6.3 (PROVEN, classical) Fact 6.3 -- prolate spheroidal wave functions.* Slepian-Pollak-Landau (Bell
  Labs, Shannon's band/time-limiting question $N\simeq 2TW$). $P_\lambda$ = multiplication by
  $1_{[-\lambda,\lambda]}$, $\hat P_\lambda=F P_\lambda F^{-1}$; $P_\lambda F P_\lambda$ commutes with the
  prolate operator $PW_\lambda=-\partial_x[(\lambda^2-x^2)\partial_x]+(2\pi\lambda x)^2$ (eq.15, a
  confluent Heun operator). Eigenvalues $\nu_n(\lambda)$ simple, decreasing to 0, $\sim4\lambda^2$
  nonzero ones; eigenfunctions = prolate $h_{n,\lambda}$; $F(h_{2m,\lambda})=\chi_m h_{2m,\lambda}$,
  $\chi_m^2=\nu_m$, $\mathrm{sign}\,\chi_m=(-1)^m$; $1-\chi_0,1-\chi_2 \to0$ exponentially in $x=\lambda^2$.
- *6.4 The prolate ansatz $k_\lambda$.* $QW_\lambda$ = Weil form restricted to support $[\lambda^{-1},
  \lambda]$; positivity for all $\lambda$ $\Leftrightarrow$ RH; proved for small $\lambda$ ([111],[24]).
  There is a lower-bounded self-adjoint $A_\lambda$ with compact resolvent, $QW_\lambda(f,f)=\langle
  A_\lambda f|f\rangle$ (eq.16); its smallest eigenvalue $\epsilon(\lambda)$ goes to 0 exponentially in
  $\mu=\lambda^2$, and **Figure 1** shows $\epsilon(\sqrt x)$ tracks $1-\chi_2(\sqrt x)$, with the
  exp-of-exp law $1-\chi_2\sim\frac{2^{14}}{3}\sqrt{2\pi^5}\,e^{-4\pi e^L}\cdot L^{9/2}$ ($L=2\log\lambda$).
  The ansatz: $k_\lambda=E(h_\lambda)$, $h_\lambda$ = vanishing-integral combination of the localized
  $h_{0,\lambda},h_{4,\lambda}$. Conceptual justification via the Poisson formula: $E(\hat f)(x)=E(f)
  (x^{-1})$ on $S_0^{ev}$ (eq.18, $f(0)=\hat f(0)=0$); the obstruction to $E(f)$ being in the radical is
  $P_\lambda\cap\hat P_\lambda=\{0\}$, but these projections NEARLY intersect, so $k_\lambda$ is a
  "near-radical" element on which $QW_\lambda$ is tiny -- an educated guess for the minimal eigenvector.
- *6.5 (PROVEN) Fact 6.4.* $\hat k_\lambda\to\Xi$ uniformly on closed substrips of $|\mathrm{Im}\,z|<1/2$,
  via classical prolate-to-Hermite-Weber estimates; error $\le c\lambda^{-1/2-\alpha}(1-2\alpha)^{-1}$
  on $\mathrm{Im}\,z=\alpha$.
- *6.6 Remaining steps (THE GAP).* To apply Theorem 6.1 one must show the smallest eigenvalue of
  $QW_\lambda$ is simple with even eigenvector (known for the prolate analogue, not for $QW_\lambda$);
  AND "it still remains to show that $k_\lambda$ is a sufficiently good approximation of $\theta_x$,
  $\lambda=\sqrt x$" (where $\theta_x(u)=\eta_x(x^{1/2}u)$ is the recentered minimal eigenvector).

**§7 Geometric perspectives (pp.30-34).**
- *7.1 Archimedean trace formula.* Rewrite the 1998 archimedean trace formula with TWO independent
  parameters = Shannon time-limit $T$ ($P_T$) and band-limit $W$ ($\hat P_W$):
  $W_\infty(f)=\log(TW)f(1)+\mathrm{Tr}(\vartheta(f)(1-P_T-\hat P_W))$ (eq.19), $\vartheta$ the scaling
  action. A bridge from the explicit formula to information theory.
- *7.2 (PROVEN) Theorem 7.1 -- archimedean Weil positivity via the Sonin space.* For $g$ supported in
  $[2^{-1/2},2^{1/2}]$ with $\hat g(i/2)=\hat g(0)=0$: $W_\infty(g\ast g^*)\ge\mathrm{Tr}(\vartheta(g)S
  \vartheta(g)^*)$, $S$ = projection onto the Sonin space $S_1$ (Burnol; even $L^2$ functions vanishing
  with their FT on $[-\lambda,\lambda]$ = orthocomplement of $\mathrm{ran}\,P_\lambda+\mathrm{ran}\,\hat
  P_\lambda$). The Sonin space is "the main source of positivity" at the archimedean place.
- *7.3 The semilocal adele class space.* $Y_S=\mathbb{A}_S/\Gamma_S$, $\mathbb{A}_S=\prod_{v\in S}
  \mathbb{Q}_v$, $\Gamma_S=\{\pm p_1^{n_1}\cdots p_k^{n_k}\}\subset\mathbb{Q}^*$. Encoded by the
  cross-product algebras $S(\mathbb{A}_S)\rtimes\Gamma_S$, forming a sheaf over $\mathrm{Spec}\,\mathbb{Z}$.
  *Theorem 7.2:* $O\rtimes\mathbb{G}_m$ is a sheaf of algebras on $\mathrm{Spec}\,\mathbb{Z}$ with
  $(O\rtimes\mathbb{G}_m)(S^c)=S(\mathbb{A}_S)\rtimes\mathbb{Z}_S^\times$, generic-point stalk $S(\mathbb{A}
  _\mathbb{Q})\rtimes\mathbb{Q}^*$, global sections $S(\mathbb{R})\rtimes\{\pm1\}$.
- *7.4 The semilocal trace formula.* $-\sum_{v\in S}W_v(f)=\log(TW)f(1)+\mathrm{Tr}(\vartheta(f)(1-P_T^S-
  \hat P_W^S))$ (eq.22) -- eq.19 plus the contribution of the primes $p\in S$ via the module.
- *7.5 IR and UV regimes.* In a spectral triple $(\mathcal A,\mathcal H,D)$: UV = high-energy spectrum
  (local geometry, heat kernel, spectral action); IR = low-lying spectrum (global/topological). IR
  construction [30]: self-adjoint $D_{\log}^{(\lambda,N)}$ = rank-one perturbations of the scaling
  spectral triple on $[\lambda^{-1},\lambda]$, spectrum = the stunning low-zero approximation; their
  regularized determinants $\det_{reg}(D_{\log}-z)$ conjecturally $\to\Xi$. UV: §7.6. *Theorem 7.3*
  (CONDITIONAL on RH, [28]): for $D$ with spectrum = imaginary parts of zeta zeros, the small-$t$
  heat expansion $\mathrm{Tr}(e^{-tD^2})\sim \frac{\log(1/t)}{4\sqrt\pi\sqrt t}-\frac{\log4\pi+\gamma/2}
  {2\sqrt\pi\sqrt t}+2e^{t/4}+\sum a_n t^{n/2}$ (eq.23), $a_0=-1/4$, coefficients in Bernoulli/Euler
  numbers; the series is divergent ($a_n\sim$ factorial). [The project verified this numerically against
  the actual zeros to $\sim10^{-5}$, e3u/#51.]
- *7.6 The prolate wave operator (the UV model, with Moscovici [27]).* The natural self-adjoint extension
  of $PW_\lambda$ to $L^2(\mathbb{R})$, restricted to the Sonin space, has discrete spectrum; its negative
  eigenvalues $\nu_k$ give $2\sqrt{\nu_k}$ (for $\lambda=\sqrt2$) the SAME ultraviolet behavior as
  $\rho-1/2$; positive spectrum $\leftrightarrow$ trivial zeros. A Darboux-constructed Dirac square root
  $D$ of $PW_\lambda$ matches the UV behavior of the zeros (**Figure 2**). This is the long-missing
  "ultraviolet model" flagged in §3.4. The Dirac-square-root ambiguity is tied to the differential
  Galois theory of the prolate equation (Ramis et al. [45,89]).

**§8 Conclusion (pp.34-35).** RH catalyzed vast mathematics; the new contribution = a large class of
functions with provably-on-line zeros (Theorem 6.1) tied to the Weil form, plus the extraordinary
truncated-Euler-product numerics; the geometric route = prove the approximating zeros converge to zeta's.
To be continued with Consani and Moscovici.

## Project mapping (verdict lives in the assessment dossier)

- **What is proven (unconditional):** Theorem 6.1 (on-line zeros for each finite cutoff); Facts
  6.2/6.3/6.4 ($\Xi=$FT of $E(h)$; prolate commutation; $\hat k_\lambda\to\Xi$); Theorem 7.1 (Sonin
  archimedean positivity); Theorem 7.2 (sheaf). Conditional-on-RH: Theorem 7.3. Asymptotic only:
  the Moscovici UV match ($\lambda=1,\sqrt2$).
- **The gap (= RH):** $\hat\eta_x\to\Xi$ (§6.6), equivalently global Weil positivity (Bombieri-Weil).
  Theorem 6.1 manufactures on-line zeros for ANY admissible even-kernel form, so it is **zeta-blind**;
  the discrimination from Davenport-Heilbronn lives only in this unproven convergence (provably false
  for D-H, since $\Xi_{DH}$ has off-line zeros and a uniform limit of real-zero functions cannot have a
  complex zero). See [`connes_2602_letter_to_riemann.md`](../connes_2602_letter_to_riemann.md).
- **Instrumented by the project:** e3s (the eta_x classifier: identical machine reproduces D-H on-line
  zeros; Caratheodory-Fejer is input-agnostic); e3t (the prolate ansatz is archimedean-dominated);
  e3u (Theorem 7.3 heat trace verified; the Hilbert-Polya operator is beta-blind); e3v (the
  $\epsilon(\lambda)\sim e^{-4\pi x}$ marginal wall = Figure 1 from first principles via Slepian
  eigenvalues); e3y (the input-side stealth window = a $\sim370\times$ cancellation residue).
- **Landscape placement:** another "trace/realization without polarization" instance, now with a
  sharper realization half (the finite-cutoff on-line property is a theorem). Column (iii) of the
  [spec_z scorecard](../spec_z_cohomology_landscape.md) still absent. C-longshot in the
  [accident dossier](../rh_solved_by_accident.md): the proven fragments (Sonin positivity, prolate
  convergence, the UV model) are exactly the archimedean, D-H-shared, RH-agnostic half.

## References (paper-internal, to chase)

[32] Connes-van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* (Theorem 6.1).
[27] Connes-Moscovici (the prolate self-adjoint extension / UV model). [28] (the Theorem 7.3 heat
expansion). [24],[25],[30],[31] (the $QW_\lambda$ operator, IR Dirac operators, numerics). [111] Yoshida
(small-$\lambda$ archimedean positivity). [9-11] Burnol (Sonin space). [101] Slepian-Pollak. [26] (knots/
primes, $\pi^{-1}(C_p)$ = mapping torus). [19,20] (scaling site / Theorem 7.2). [45,89] Ramis et al.
(differential Galois of the prolate equation).
