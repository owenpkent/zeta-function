# Pinning the canonical-system pillar: Remling Section 5.2 at source, and Suzuki's zeta chain read properly

> SURVEYOR hardening note, 2026-07-22, feeding the running e1u build (the trace-normed
> canonical-system rung of LEARNINGS #170). Two tasks: (1) put the compactness pillar
> (trace-normed Hamiltonians compact; $H \mapsto m$ a homeomorphism) on a primary source,
> currently carried by Hur arXiv:1501.01268 plus a Forester-Remling citation to Remling's book
> (Spectral Theory of Canonical Systems, de Gruyter 2018, Section 5.2 / Corollary 5.8) that
> nobody had read; (2) read Suzuki arXiv:1204.1827 at source and place his canonical system
> relative to the e1u encoding.
>
> Method discipline (#157 process flag): **[FETCH-VERIFIED]** = read at source this session
> (arXiv abstract page, ar5iv HTML, or full text extracted locally from the arXiv PDF);
> **[SECONDARY]** = search-snippet or unpinned; **[SURVEYOR-INFERENCE]** = my structural
> translation, not in any print source. Discrepancies logged in Section 5, not resolved.
> No em dashes.

## 0. Verdicts up front

1. **Task 1, the Remling pillar: RESOLVED BY SUBSTITUTION (2026-07-22).** The printed book
   pages remain unread: de Gruyter and Google Books previews are paywalled/unrenderable, and
   Remling's own OU pages carry no draft (the only online full copy found is an unauthorized
   upload at dokumen.pub, not used, on legitimacy grounds). But the entire load the book
   citation carried is now pinned at source in three open documents, two authored by Remling
   himself: (i) Hur arXiv:1501.01268 **full text** (extracted and read this session): complete
   definitions, the metric, the compactness argument, and the homeomorphism (Proposition 5.1)
   with its proof (Appendix A); (ii) Remling-Scarbrough arXiv:1811.07067 **full text**: the
   author's own restatement with the exact book numbering (Theorem 5.1 = bijection; Section 5.2
   = the metric; Theorem 5.7(b) + Corollary 5.8 = metric convergence iff locally uniform
   $m$-convergence), plus an in-print instance of the exact indivisible-tail embedding e1u
   needs; (iii) Remling arXiv:0710.4128 Section 2: the origin of the compactness mechanism
   (the same test-function metric, Banach-Alaoglu + diagonal). Nothing in the survey's
   Section 1.3 changes; three refinements are logged in Section 3 below.
2. **Task 2, Suzuki 1204.1827: read at source (full text). Verdict on the e1u relationship:
   a DIFFERENT OBJECT on a TRANSVERSE deformation axis, not the infinite-$\lambda$ limit
   object of e1u's chains and not a gauge of it.** Suzuki holds the full arithmetic kernel
   and deforms the shift parameter $\omega$ (zero-free-region calibrated, RH = the
   $\omega \to 0$ family statement); e1u holds the line ($\omega = 0$ target) and deforms the
   cutoff $\lambda$. His Hamiltonians are diagonal, determinant-one (NOT trace-normed;
   trace-normalizable by reparametrization, [SURVEYOR-INFERENCE], Section 2.4). His finite-$a$
   objects are exact chain elements of zeta's own $\omega$-space; positivity/extension is his
   open load. e1u's finite objects are positive for free; exactness (identification) is the
   open load. The two programs split the same conservation law on opposite sides.
3. **The companion-series find (the strongest new fact for the e1u adversary):** Suzuki's
   JFA 2021 paper (arXiv:1606.05726 v3) already carries an in-print GRH-equivalent shaped
   like e1u's clause (a)+(b) split: **Theorem 2.4** = GRH iff along a sequence
   $\omega_n \downarrow 0$ the determinant coordinate never degenerates
   ($\det(1 \pm K[t]) \ne 0$ for ALL $t \ge 0$: no finite-time collapse of the Hamiltonian)
   AND the far-end reproducing kernel decays ($J(t;z,z) \to 0$ as $t \to \infty$: no mass
   left at the singular end). His Theorem 2.3 PROVES the far-end decay necessary (given HB
   membership). No compactness leg, no subsequential-limit argument in any text of the series
   read or scanned (1204.1827 and 1606.05726 at full text; 2206.03682 and 2012.11121 at
   full-text keyword level per the adversary spot-check; the companions listed in Section 2.3
   remain unread), so the #170 novelty claim for the composite move stands within that scope,
   but any e1u claim of a "newly
   isolated non-degeneracy clause" must now cite Suzuki Thm 2.4 (3)-(4) as the nearest
   in-print cousin, in a different gauge.

---

## 1. Task 1: the compactness pillar at source

### 1.1 Access attempts (honest record)

- Remling's homepage (math.ou.edu/~cremling) and lecture-notes page: fetched; no canonical
  systems notes, no book draft [FETCH-VERIFIED, both pages].
- de Gruyter document pages (both the 2018 ISBN and the bound ISBN): HTTP 405 to fetches.
- Google Books (id io1uDwAAQBAJ): preview exists but does not render through the fetch tool;
  only front matter references visible. TOC recovered from retail listings [SECONDARY]:
  chapters are 1 Basic Definitions, 2 Symmetric and Self-Adjoint Relations, 3 Spectral
  Representation, 4 Transfer Matrices and de Branges Spaces, **5 Inverse Spectral Theory**,
  6 Some Applications, 7 The Absolutely Continuous Spectrum. So Section 5.2 / Corollary 5.8
  sit inside the inverse-spectral-theory chapter, consistent with both citing papers.
- No second edition exists as of this search (2026-07-22): all listings are the 2018 volume
  (de Gruyter Studies in Mathematics 70), so the Forester-Remling numbering has no
  edition-drift risk [SECONDARY, converged retail/publisher listings].
- dokumen.pub hosts what appears to be a full copy; unauthorized upload; **not used**.

### 1.2 The pinned statement set

**(A) Hur, arXiv:1501.01268, "Density of Schrodinger Weyl-Titchmarsh m functions on Herglotz
functions" [FETCH-VERIFIED, full text extracted from the arXiv PDF and read; Sections 2.2, 5,
6 and the references].** The exact setup and statements:

- **Space:** half-line canonical systems $Ju' = zHu$ on $x \in (0,\infty)$, $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$,
  "$H$ is a positive semidefinite $2\times2$ matrix whose entries are real-valued, locally
  integrable functions"; trace-normed means "$\mathrm{Tr}\,H(x) = 1$ for almost all $x$";
  boundary condition always "$u_1(0,z) = 0$". $V_+$ = the trace-normed ones.
- **Limit point for free:** "a half-line trace-normed canonical system is always in a limit
  point case at $\infty$", so the $m$-function $m_H(z) = \tilde u_2(0)/\tilde u_1(0)$ from the
  (unique up to constant) $H$-integrable solution is well-defined; no hidden boundary choice
  at infinity. (Credited to de Branges [7] with an alternative proof by Acharya [1].)
- **Bijection:** "De Branges [10] and Winkler [37] then showed that, for a given Herglotz
  function, there exists a unique half-line trace-normed canonical system with (11), such
  that its m function $m_H$ is the given Herglotz function." ([10] = de Branges 1968 book;
  [37] = Winkler, "The inverse spectral problem for canonical systems", Int. Eq. Op. Theory
  22 (1995) 360-374.)
- **The metric and the topology:** pick a countable $\|\cdot\|_\infty$-dense set $\{f_n\}$ of
  continuous compactly supported functions, $d_n(H_1,H_2) := \big| \int_{(0,\infty)} f_n^*(x)\,(H_1-H_2)(x)\,f_n(x)\,dx \big|$,
  $d := \sum_n 2^{-n} d_n/(1+d_n)$. "Clearly, $d(H_n,H)\to0$ if and only if $H_n$ converges
  to $H$ weak-$*$." So the topology on $V_+$ is the weak-$*$ topology on the matrix measures
  $H(x)dx$, metrized by test-function quadratic forms.
- **Compactness:** "By the similar argument in section 2 of [30], it is briefly shown that
  $V_+$ is a compact metric space." The argument, given in the paper: Banach-Alaoglu on
  finite intervals $[0,L]$ plus a diagonal process gives a weak-$*$ convergent subsequence
  of the measures $H_{n_j}(t)dt$; "the trace-normed condition, $\mathrm{Tr}\,H(x) = 1$, is
  preserved in the limiting process, which implies that the limit measure $d\mu$ is
  absolutely continuous with respect to the Lebesgue measure and it can be expressed by
  $H(t)dt$ for some $H$ in $V_+$." This is the precise sense in which trace-norming closes
  the class: the normalization forbids the limit measure from developing a singular part.
- **The homeomorphism, verbatim:** "**Proposition 5.1.** The map from $V_+$ to
  $\overline{\mathcal H}$, defined by $H \mapsto m_H$, is a homeomorphism, where
  $\mathcal H$ is the set of all (genuine) Herglotz functions and
  $\overline{\mathcal H} = \mathcal H \cup \mathbb R \cup \{\infty\}$." Target topology:
  uniform convergence on compact subsets of $\mathbb C^+$ (for the extended target the
  spherical/chordal metric is the right reading; Forester-Remling state it that way
  explicitly). Proof shape: bijection (de Branges + Winkler) + $V_+$ compact + continuity
  (proved in Hur's Appendix A) + compact-to-Hausdorff, hence homeomorphism. The degenerate
  elements $\mathbb R \cup \{\infty\}$ (constant $m$) are genuinely IN the target, i.e. the
  compact space contains the degenerate limits.
- **The equivalent coordinate (load-bearing for e1u):** de Branges' convergence form,
  recalled by Hur: $m_{H_n}(z) \to m_H(z)$ locally uniformly iff
  $\int_0^x H_n(t)\,dt \to \int_0^x H(t)\,dt$ **locally uniformly** in $x$ (see also
  Langer-Winkler [20], Prop. 3.2); "due to the trace-normed condition, the weak-$*$
  convergence in (26) implies the local uniform convergence in (27), which reveals that two
  convergences are equivalent." So on $V_+$: metric convergence = weak-$*$ = locally uniform
  convergence of the integrated Hamiltonians $M(x) = \int_0^x H$ = locally uniform
  $m$-convergence. Four faces of one topology.

**(B) Remling-Scarbrough, arXiv:1811.07067, "Oscillation theory and semibounded canonical
systems" [FETCH-VERIFIED, full text extracted and the relevant passages read].** The
author's own restatement of the book's content, with the book numbering:

- "A fundamental result from the inverse spectral theory of canonical systems
  [11, **Theorem 5.1**] says that every generalized Herglotz function is the m function of a
  unique canonical system." (Generalized Herglotz = Herglotz $\cup$ the constants
  $m \equiv a \in \mathbb R_\infty$; the constants correspond to $H \equiv P_\alpha$, a
  single singular interval, with spectral measure $\rho = 0$.) [11] = Remling, Spectral
  Theory of Canonical Systems, de Gruyter Studies in Mathematics 70, 2018.
- "These modified canonical systems ... converge to $H$ as $n \to \infty$ with respect to
  the metric discussed in [11, **Section 5.2**]. Moreover, in general, convergence in this
  metric is equivalent to the locally uniform (on $\mathbb C^+$) convergence of the
  associated m functions [11, **Theorem 5.7(b), Corollary 5.8**], and this in turn implies
  that the spectral measures $\rho_n$ converge to $\rho$ in weak $*$ sense."
- **The indivisible-tail precedent (e1u's named must-fix, in print):** the sentence above is
  about exactly the e1u embedding move. Verbatim: "The boundary condition $\beta_n$ can be
  implemented by a singular half line $(L_n, \infty)$ of type $\beta_n + \pi/2$," with
  $H_n(x) = H(x)$ for $x < L_n$ and $H_n(x) = P_{\beta_n + \pi/2}$ for $x > L_n$, and these
  converge to $H$ in the Section 5.2 metric. So: a finite chain on $[0,L]$ with boundary
  condition $\beta$ IS embedded in the compact space by the projection-valued tail, the tail
  angle encodes the boundary condition, and the tail's influence dies in the limit. This is
  the standard tool, used by Remling himself.
- **Trace-norming as reparametrization (in print):** their Section 4 Schrödinger-to-canonical
  translation produces $H_0 = \begin{pmatrix} p^2 & pq \\ pq & q^2 \end{pmatrix}$, "not yet
  trace normed; to do this, we need to pass to the new variable
  $X = \int_0^x (p^2(t) + q^2(t))\,dt$." Confirms the survey's "normalization is a
  reparametrization of the independent variable, not a growth bound" at source.

**(C) Remling, arXiv:0710.4128, "The absolutely continuous spectrum of one-dimensional
Schrödinger operators" (= Math. Phys. Anal. Geom. 10 (2007) 359-373, Hur's [30])
[FETCH-VERIFIED, Section 2 via ar5iv].** The origin of the compactness mechanism: the same
metric construction ($d(\mu,\nu) = \sum 2^{-n}\rho_n/(1+\rho_n)$ with $\rho_n$ built from a
countable dense set of continuous compactly supported test functions), the compactness claim
"$(\mathcal V^C, d)$ is a compact space" via Banach-Alaoglu on $M([-R,R])$ plus a diagonal
argument, and the continuity statement (Lemma 4.2 there): $d(\mu_n,\mu)\to0$ implies
$m_\pm(x,z;\mu_n) \to m_\pm(x,z;\mu)$ uniformly on compact subsets of $\mathbb C^+$. Hur's
"similar argument" credit is thus pinned end to end: mechanism in 0710.4128 for measure
spaces of potentials, adaptation to $V_+$ in Hur with the trace-norm-closure observation,
full treatment in the book per the author's own citations.

**(D) Forester-Remling, arXiv:2409.04862** [FETCH-VERIFIED in the #170 round, unchanged]:
the two survey-quoted sentences (compactness of trace-normed systems, the $H \mapsto m$
homeomorphism with the spherical metric on the disk $|z - 2i| \le 1$) remain as recorded;
their citations (Section 5.2 for compactness discussion, Corollary 5.8 for the
homeomorphism) are consistent with (B).

### 1.3 The four pin questions, answered

1. **Which topology on Hamiltonians?** Weak-$*$ on the matrix measures $H(x)dx$, metrized by
   countable test-function quadratic forms; equivalently (on the trace-normed class only)
   locally uniform convergence of $M(x) = \int_0^x H$. [Hur at source; book Section 5.2 per
   Remling-Scarbrough.]
2. **Which normalization?** $\mathrm{Tr}\,H = 1$ a.e. on $(0,\infty)$, boundary condition
   $u_1(0) = 0$, limit point at $\infty$ automatic. The normalization is exactly what closes
   the class under weak-$*$ limits (no singular part can form). [Hur at source.]
3. **How are degenerate/indivisible limits handled?** They are inside the space, not
   excluded: $H \equiv P_\alpha$ on singular (indivisible) intervals is a legal element, the
   constant $m$-functions $\mathbb R \cup \{\infty\}$ are in the homeomorphism target, and a
   projection-valued tail is the standard embedding of a finite chain with a boundary
   condition. Degeneration is a location in the compact space, not a failure of it. [Hur
   Prop. 5.1; Remling-Scarbrough at source.]
4. **The exact homeomorphism statement?** Hur Prop. 5.1 as quoted above (bijection by
   de Branges + Winkler; homeomorphism by compactness + continuity); the book's form is
   Theorem 5.7(b) + Corollary 5.8 per the author's own citation, stating the convergence
   equivalence (metric iff locally uniform $m$-convergence). Which precise sentence in the
   book is labeled "Corollary 5.8" remains unverified at page level; both author citations
   agree on what it carries.

### 1.4 Delta list versus the survey note (`compact_class_determinacy_survey.md` Section 1.3)

- **No statement changes.** Everything the survey's Section 1.3 and adversary addendum
  assert about the compact space survives the source read unchanged.
- **Refinement 1 (new, useful):** the topology has a fourth equivalent face, locally uniform
  convergence of integrated Hamiltonians $M(x)$ (de Branges' form, upgraded from weak-$*$ by
  trace-norming). This hands e1u a concrete working coordinate: local convergence
  certificates are free; ALL escape routes live in the $x \to \infty$ tail and the
  identification. The survey stated this qualitatively; it is now a pinned equivalence.
- **Refinement 2 (new, useful):** the indivisible-tail embedding of a finite chain is not
  merely "a normalization the BUILDER rung must fix and report" (survey Section 1.3(iv)); it
  is a standard in-print move with the exact convergence statement e1u needs
  (Remling-Scarbrough), including the fact that the tail angle is the boundary condition.
- **Refinement 3 (provenance):** Hur's [30] is now identified precisely (MPAG 10 (2007)
  359-373 = arXiv:0710.4128) and its Section 2 read; the survey's "argument credited to
  Remling 2007, Section 2" gloss was correct, with the nuance that 0710.4128's compactness
  is for potential/measure spaces and Hur ADAPTS it to $V_+$ (his own sketch carries the
  trace-norm-closure step).
- **Residual (honest):** the book's printed Section 5.2 / Corollary 5.8 pages remain unread.
  The only content that still rests on the author's citations rather than a read text is
  the internal labeling (which sentence is 5.7(b), which is 5.8), not any mathematical
  statement. Priced at zero for e1u purposes.

---

## 2. Task 2: Suzuki's canonical system from zeta, read at source

**Source: arXiv:1204.1827 v2, "A canonical system of differential equations arising from the
Riemann zeta-function" (RIMS Kokyuroku Bessatsu B34 (2012) 397-435) [FETCH-VERIFIED, full
text extracted from the arXiv PDF; abstract page also fetched].**

### 2.1 The object

- The family $\Theta_\omega(z) = \xi(\tfrac12 - \omega - iz)/\xi(\tfrac12 + \omega - iz)$,
  $\omega > 0$; $E^\omega(z) := \xi(\tfrac12 + \omega - iz)$;
  $A^\omega = \tfrac12(\xi(s+\omega) + \xi(s-\omega))$,
  $B^\omega = \tfrac{i}{2}(\xi(s+\omega) - \xi(s-\omega))$ at $s = \tfrac12 - iz$.
- **Proposition 1.1 (verbatim):** "RH holds if and only if RH($A^\omega$) holds for all
  $\omega > 0$." (RH($A^\omega$) = all zeros of $A^\omega$ real; known unconditionally for
  $\omega \ge 1/2$ by Lagarias, and for $0 < \omega < 1/2$ under RH.)
- **Proposition 1.2 (verbatim):** "Let $\omega_0 \ge 0$. Then the following are equivalent:
  (1) $\zeta(s) \ne 0$ for $\Re(s) > \tfrac12 + \omega_0$, (2) $\Theta_\omega(z)$ is a
  meromorphic inner function in $\mathbb C^+$ for every $\omega > \omega_0$." So the
  $\omega$-family is a nested family of zero-free-region statements; RH is the
  $\omega_0 = 0$ member. This is the calibration that makes the axis transverse to e1u's
  (Section 2.6).
- Hermite-Biehler membership of $E^\omega$: holds unconditionally for $\omega \ge 1/2$
  (trivial zero-free region), under RH for $0 < \omega < 1/2$; at $\omega = 0$ the family
  degenerates ($\Theta_0 \equiv 1$), so the RH-critical content is the small-$\omega$ end,
  not a limit object at $\omega = 0$.

### 2.2 The construction (what is actually built, and how)

- An arithmetic Hankel-type kernel: $h_\omega$ built from Jordan's totient
  $J_{2\omega}(n) = n^\omega c_\omega(n)$ and a beta/gamma-type special function $g_\omega$
  (Burnol's method for the gamma function, applied to $\xi$); $h_\omega$ vanishes on
  $(0,1)$, supported in $[1,\infty)$. Innerness of $\Theta_\omega$ is characterized through
  $h_\omega$ (Theorem 2.2).
- The operator $(\mathsf H_\omega f)(x) = \int_0^\infty h_\omega(xy) f(y)\,dy$ on
  $L^2(0,\infty)$ and its multiplicative truncations
  $\mathsf H_{\omega,a} = P_a \mathsf H_\omega P_a$ on $L^2(0,a)$.
- **Theorem 2.3 (main construction, $\omega > 1$ unconditional, verbatim core):**
  $\mathsf H_{\omega,a}$ is Hilbert-Schmidt self-adjoint with continuous kernel for $a > 1$,
  zero for $a \le 1$; $1 \pm \mathsf H_{\omega,a}$ invertible for every $a > 0$; define
  $m(a) = \det(1 + \mathsf H_{\omega,a})/\det(1 - \mathsf H_{\omega,a})$ (Fredholm
  determinants). Then $m$ is real-valued continuous on $(0,\infty)$ and
  $$-a\,\frac{\partial}{\partial a}\begin{pmatrix} X_a \\ Y_a \end{pmatrix} = z \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} m(a)^{-2} & 0 \\ 0 & m(a)^2 \end{pmatrix}\begin{pmatrix} X_a \\ Y_a \end{pmatrix}, \quad 0 < a < \infty,$$
  with explicit solution $(A_a, B_a)$ satisfying $(A_1, B_1) = (A^\omega, B^\omega)$; plus
  the transformation to a pair of Schrödinger equations with potentials built from $m$.
- **Normalization: diagonal, determinant one.** $H_\omega(a) = \mathrm{diag}(m(a)^{-2}, m(a)^2)$,
  $\det H_\omega \equiv 1$, in the multiplicative variable $a$ (the $-a\,\partial_a$ gauge).
  NOT trace-normed. Positive semidefinite automatically WHEREVER DEFINED (it is diagonal
  with entries $m^{\mp2}$, $m$ real): in this gauge "positivity of the Hamiltonian" is
  exactly "$m(a)$ stays real, finite and nonvanishing", i.e. non-degeneration of a
  determinant-class coordinate. The RH content of "positive semidefiniteness of the family"
  is a no-blowup statement about Fredholm determinant ratios: the same residue class as
  M4's uniform determinant-class clause (#148), met here from the inverse direction.
- **Chain geometry:** $a = 1$ carries the full $(A^\omega, B^\omega)$; $\mathsf H_{\omega,a}$
  grows with $a$; the far end $a \to \infty$ is expected to be the trivial chain element.
  Verbatim, the open problem: "we emphasize that the limit behavior
  $\lim_{a\to+\infty}(A_a(z), B_a(z))$ is still open even if $\omega > 1$. The expected
  result is ... $(\xi(\tfrac12+\omega), 0)$ ... this limit behavior is related to the
  arithmetic properties of $\zeta(s)$ in more deep level, because we need information for
  all $\{c_\omega(n)\}_{n\ge1}$ to understand it differ from the situation that we need only
  finitely many $c_\omega(n)$'s to understand $\mathsf H_{\omega,a}$ for a finite range of
  $a$." So even in the unconditional range, the FAR-END identification of his chain is open
  and is priced by Suzuki himself as full-arithmetic-input. This is the (a)/(b)-shaped
  entanglement, in his gauge, stated in 2012.
- **Unconditional vs conditional:** proven unconditionally for $\omega > 1$ (kernel
  continuity needs it); "plausible ... without essential difficulties" for $\omega > 1/2$
  (distributional derivatives + L^2-kernel determinants, Section 5); for
  $0 < \omega < 1/2$ "very hard ... unconditionally," but under RH the analytic obstacles
  reduce to integral-operator theory (Section 5). The abstract's criterion (verbatim): "If
  such construction is extended to all $\omega > 0$ unconditionally, we get a criterion for
  the Riemann hypothesis in terms of a family of canonical systems parametrized by
  $\omega > 0$, which explains the validity of the Riemann hypothesis as positive
  semidefiniteness of the corresponding family of Hamiltonian matrices."
- **Direction of the equivalence:** both directions live at the family level.
  Positivity/extension of the constructed family for all $\omega > 0$ $\Rightarrow$
  $E^\omega \in HB$ for all $\omega > 0$ $\Rightarrow$ RH (Prop. 1.1/1.2). Conversely RH
  $\Rightarrow$ the de Branges spaces exist for all $\omega > 0$ (Lagarias) and the
  construction is expected to go through. At fixed $\omega > 1/2$ everything is
  unconditional and carries no RH content; the RH weight sits entirely in the
  $\omega \downarrow 0$ tail of the family.

### 2.3 The companion series (checked for degeneration / mass-escape measurements)

**arXiv:1606.05726 v3 = "Hamiltonians arising from L-functions in the Selberg class"
(J. Funct. Anal. 281 (2021) 109116) [FETCH-VERIFIED, full text extracted; Theorems quoted
from the extraction].** The zeta construction generalized to the real Selberg subclass
$S_{\mathbb R}$, with $E_L^{\omega,\nu}(z) = \xi_L(\tfrac12 + \omega - iz)^\nu$ (the extra
integer $\nu$ resolves the kernel-continuity restriction: condition (2.8) is
$\nu\omega d_L > 1$, recovering $\omega > 1$ for $L = \zeta$, $\nu = 1$). Structure:

- **Theorem 2.1:** the truncated operator $\mathsf K_L^{\omega,\nu}[t]$ on $L^2(-\infty,t)$
  (additive variable now) is Hilbert-Schmidt with continuous kernel, zero for $t \le 0$, and
  "there exists $\tau = \tau(L;\omega,\nu) > 0$ such that both $\pm1$ are not the
  eigenvalues of $\mathsf K_L^{\omega,\nu}[t]$ for every $t \in [0,\tau)$." The Hamiltonian
  on $[0,\tau)$: $H_L^{\omega,\nu}(t) = \mathrm{diag}(1/\gamma_L^{\omega,\nu}(t),\ \gamma_L^{\omega,\nu}(t))$
  with $\gamma_L^{\omega,\nu}(t) = (\det(1+\mathsf K[t])/\det(1-\mathsf K[t]))^2$. Diagonal,
  determinant one, exactly the zeta gauge.
- **Theorem 2.2:** the explicit solution solves the canonical system on $[0,\tau)$ with
  $E_L^{\omega,\nu}(z) = A(0,z) - iB(0,z)$ (full function at $t = 0$, chain running outward).
  Proved by the inverse-problem input [45, Theorem 1.1] = Suzuki, "An inverse problem for a
  class of canonical systems having Hamiltonians of determinant one," JFA 279 (2020) 108699.
- **Theorem 2.3 (the mass-escape necessity, proven):** assuming $E_L^{\omega,\nu} \in HB$
  (unconditional for $\omega > 1/2$), the Hamiltonian extends to $[0,\infty)$ (the Fredholm
  determinants never vanish, Prop. 5.1 there) and $J_L^{\omega,\nu}(t;z,w) \to 0$ as
  $t \to \infty$ for every fixed $z, w$, with $J(t;z,z) \not\equiv 0$ at any finite $t$. So
  in his gauge, "no mass left at the far end" is a THEOREM given class membership, and the
  far-end decay is necessary for GRH.
- **Theorem 2.4 (the GRH equivalence, verbatim):** "The validity of GRH($L$) for
  $L \in S_{\mathbb R}$ is equivalent to the condition that there exists a sequence
  $(\omega_n, \nu_n) \in \mathbb R_{>0} \times \mathbb Z_{>0}$, $n \ge 1$, such that
  (1) $\omega_m < \omega_n$ if $m > n$ and $\omega_n \to 0$ as $n \to \infty$,
  (2) $\nu_n \omega_n d_L > 1$,
  (3) $\det(1 \pm \mathsf K_L^{\omega_n,\nu_n}[t]) \ne 0$ for every $t \ge 0$, and
  (4) $\lim_{t\to\infty} J_L^{\omega_n,\nu_n}(t;z,z) = 0$ for every $z \in \mathbb C^+$."
  Clause (3) = no finite-time degeneration of the determinant-class coordinate (the
  Hamiltonian exists and stays positive on all of $[0,\infty)$); clause (4) = far-end
  reproducing-kernel decay (no mass stranded at the singular end). **Theorem 6.1** is the
  calibrated variant (stated for $0 < \omega_0 < 1/2$): $L(s) \ne 0$ for
  $\Re(s) > \tfrac12 + \omega_0$ iff the same clauses hold along $\omega_n \to \omega_0$. The zero-free-region reading of the family is thus
  in print, theorem-level.

**arXiv:2206.03682, "Aspects of the screw function corresponding to the Riemann
zeta-function" (J. Lond. Math. Soc. 108 (2023) 1448-1487) [FETCH-VERIFIED, ar5iv +
abstract].** The $\omega = 0$ boundary attacked through Krein's screw-function theory
instead of the $\omega$-family: $g(t) = -\Psi(t)$ with
$\Psi(t) = \sum_\gamma (1 - \cos(\gamma t))/\gamma^2$. RH-equivalents proved: $g$ is a screw
function iff RH (Thm 1.2); nonnegativity of the associated hermitian form iff RH (Thm 1.3,
the Weil-positivity analogue); NON-DEGENERACY of the form on $L^2(-a,a)$ for all $a$ iff RH
(Thm 1.4); $\Psi = O(1)$ iff RH (Thm 1.6); $\Psi \ge 0$ iff RH (Thm 1.7); Hankel-determinant
nonnegativity iff RH (Thm 1.8). Unconditional: trace-class of the operator (Thm 1.5), decay
estimate, small-$t$ nonnegativity. Section 9 connects to Kotani's "zeta string" (Krein
strings) under RH. **No explicit degeneration/mass-at-infinity statement for the associated
string was found in the fetched text**; the closest object is Thm 1.4's nondegeneracy
equivalence, which is form-level, not Hamiltonian-level.

**arXiv:2301.00421** (Weil-distribution Hilbert space; de Branges space under RH; merges the
2209.04658 screw line): abstract-level only this session, unchanged from the survey's read
[FETCH-VERIFIED abstract, prior round]. **arXiv:2012.11121** (Ann. Inst. Fourier 75 (2025)
1463-1508): the chain-construction machine from unimodular functions; abstract fetched, "a
conditional but richly general solution to the inverse problem of recovering the structure
Hamiltonian from a given de Branges space"; no compactness content in the abstract
[FETCH-VERIFIED abstract]. Not read deeper. Also in the series, not read this session:
1308.0228 (self-reciprocal polynomials; J. Anal. Math. 2018), 1907.07838 (lacunary diagonal
Hamiltonians; Tohoku 2022), 1907.07302 (survey of the integral operators), 2209.12832,
2308.11860, 2301.05779. Flagged honestly as unread.

### 2.4 Is his family trace-normed or normalizable to it?

Not trace-normed as built (diagonal, $\det H = 1$). Trace-normalizable in the standard way
[SURVEYOR-INFERENCE, using the reparametrization convention pinned in Section 1.2(B)]: in
the additive gauge, pass to $x(t) = \int_0^t (\gamma(s) + 1/\gamma(s))\,ds$ and divide $H$
by its trace; the result is a legal $V_+$ element on $[0, x(\tau))$, extendable by an
indivisible tail if $x(\tau) < \infty$. Two structural observations, both inference, both
flagged for the e1u adversary rather than asserted as print facts: (i) a blowup of
$\gamma$ at finite $\tau$ (clause (3) failing) maps in trace-normed coordinates to $H$
collapsing onto a projection $P_{0}$ or $P_{\pi/2}$, i.e. exactly the indivisible-interval
degeneration e1u's clause (b) names; (ii) since $\mathrm{Tr}\,H = \gamma + 1/\gamma \ge 2$,
the trace-normed length of Suzuki's chain up to $t$ is at least $2t$, so his $t \to \infty$
chains are genuinely infinite trace-normed chains and the far-end condition (4) lives at the
$V_+$ boundary where Hur's degenerate elements sit.

### 2.5 The relationship to e1u, exactly

**Verdict: a different object entirely, on a transverse deformation axis; adjacent in gauge
vocabulary, dual in load split.**

- **Axes.** Suzuki fixes the FULL arithmetic (exact kernel from all of $\xi$) and deforms the
  shift $\omega$; each fixed $\omega$ system is exactly zeta's, and RH is the
  $\omega_n \downarrow 0$ statement about the FAMILY (Thm 2.4), calibrated to zero-free
  regions (Prop. 1.2 / Thm 6.1). e1u fixes the line (the $\omega = 0$ target, $\Xi$ itself)
  and deforms the cutoff $\lambda$; each finite $\lambda$ object is an approximation, and
  the open content is that the subsequential limit IS zeta's object. His chains are not the
  infinite-$\lambda$ limit object of e1u's chains (that object, if identified, is the
  $\omega = 0$ boundary at which his family degenerates, $\Theta_0 \equiv 1$), and no gauge
  change maps a fixed-$\omega$ Suzuki chain to it.
- **The dual load split (the useful sentence).** Suzuki: identification FREE (his finite-$t$
  data are exact chain elements of zeta's own space, computable from finitely many
  arithmetic coefficients, as he notes), positivity/extension OPEN (clauses (3)-(4), the
  small-$\omega$ family). e1u: positivity/reality FREE (CF reality of $\hat\xi_\lambda$,
  class membership by trace-normed compactness), identification OPEN (clause (a) = the #160
  pin, entangled with (b)). The two programs sit on opposite sides of the same conservation
  law; neither consumes the other's free leg.
- **No compactness trade anywhere in the series.** Confirmed by reading: no normal-family,
  subsequential-limit, or determinacy argument appears in 1204.1827 or 1606.05726; the
  $t$-family is never compactified; limits are taken along the chain parameter of a FIXED
  system, not across a family of systems. The #170 novelty claim (the composite move is
  unposed for zeta) stands, now verified against the full texts rather than abstracts.
- **What e1u must now cite.** Any claim that clause (b) ("no chain degeneration / no mass
  escape") is newly isolated must be scoped: in Suzuki's gauge, the split
  no-finite-degeneration + far-end-decay is in print as the entire GRH content (Thm 2.4),
  with the far-end decay proven necessary (Thm 2.3). What remains genuinely new in e1u is
  the COMPACTNESS side: free subsequential limits for cutoff approximants at $\omega = 0$
  plus the (a)/(b) split of the residue in the trace-normed space. Also note his far-end
  open problem (1204, the $c_\omega(n)$ sentence): "identification at the singular end
  costs all the arithmetic" has an in-print precedent from 2012.

---

## 3. Discrepancy log (reported, not resolved)

1. **Suzuki homepage vs arXiv numbering.** Suzuki's own publication list attaches
   arXiv:1606.05726 to the det-one inverse-problem paper (JFA 2020); the arXiv entry
   1606.05726 is actually "Hamiltonians arising from L-functions in the Selberg class"
   (JFA 2021), whose v3 comment says "a part of the old version was published as the
   reference [45] of the latest version," [45] being the det-one JFA 2020 paper. So the
   2016 posting was split: inverse-problem half to JFA 2020 (no separate arXiv number
   found), application half remains as 1606.05726 v3. Cosmetic provenance wrinkle; the
   survey's Section 3.5 citation practice ("Suzuki 1204.1827 ... no compactness leg") is
   unaffected.
2. **Homeomorphism target presentation.** Forester-Remling metrize the target by the
   spherical metric on the disk $|z - 2i| \le 1$; Hur states locally uniform convergence on
   compacts of $\mathbb C^+$ with target $\mathcal H \cup \mathbb R \cup \{\infty\}$. These
   are two presentations of the same topology (a Herglotz function is determined by its
   values on any disk; the extended target needs the chordal reading). Not a discrepancy;
   recorded so nobody hunts a phantom delta.
3. **Where the $V_+$ compactness is PROVED.** The survey's tag chain implied the full proof
   sits in Remling's book Section 5.2 with Hur as corroboration. The source read refines:
   Hur gives a self-contained sketch ("it is briefly shown"), the mechanism is at source in
   0710.4128 Section 2 (for measure spaces of potentials), and the book per its author's
   citations carries the systematic treatment. No load-bearing change; the tag on the
   compactness statement can rest on Hur + 0710.4128 alone, with the book as the canonical
   reference rather than the sole carrier.
4. **1204.1827 abstract phrasing vs theorem content.** The abstract's "positive
   semidefiniteness of the corresponding family of Hamiltonian matrices" could be misread
   as an open positivity condition on a constructed matrix family. At theorem level the
   Hamiltonian is diagonal with entries $m^{\mp2}$, hence positive wherever defined; the
   criterion's content is existence/non-degeneration of the construction for all
   $\omega > 0$ (in 1606 vocabulary: clauses (3)-(4)). The survey's one-line gloss ("RH =
   Hamiltonian positive semidefiniteness") is fair but should be read as
   existence-plus-no-blowup, not as a sign condition on given data.

## 4. What this changes for e1u

Honestly: nothing in the e1u statement of work changes, and two of its inputs harden. The
compactness pillar the rung stands on is now at source end to end (definitions, metric,
compactness mechanism, homeomorphism, degenerate elements in-space), and the two facts the
builder most needs are in print with proofs: the indivisible-tail embedding of a finite
chain converges in the right metric with the tail angle playing the boundary condition
(Remling-Scarbrough), and metric convergence can be certified on the integrated Hamiltonian
$M(x) = \int_0^x H$ locally, which means every cheap certificate is local and the entire
risk is concentrated where the survey said it was: the $x \to \infty$ tail (clause (b)) and
the identification (clause (a)). What the Suzuki read adds is a scoping correction plus a
free cross-check: the (a)+(b)-shaped residue has an in-print cousin (Thm 2.4's clauses
(3)-(4)) in the transverse gauge, so e1u's novelty is the compactness trade itself, not the
clause split; and Suzuki's far-end theorem (Thm 2.3: $J(t;z,z) \to 0$ proven necessary given
HB membership) suggests a concrete adversary probe: compute the e1u analogue of
$J(t;z,z)$ on the finite chains and watch whether its decay rate is $\lambda$-uniform,
since that is exactly where his gauge says the arithmetic bill arrives.

**Must-know corrections for BUILDER/ADVERSARY, compact:**
- None to prior claims. Additions: (i) cite Suzuki Thm 2.4 (3)-(4) when describing clause
  (b) as "newly isolated" (scope it to the compactness gauge); (ii) the tail-angle =
  boundary-condition fact means the e1u must-fix (indivisible-tail normalization) is a
  CHOICE with a named in-print convention, not an invention; report the angle used;
  (iii) local certificates on $M(x)$ are free, so any measured "convergence" claim must be
  explicitly tail-scoped or it is vacuous.

## 5. Reference list with verification tags

Fetched and read at source this session:
- arXiv:1501.01268, Hur, "Density of Schrodinger Weyl-Titchmarsh m functions on Herglotz
  functions" [FETCH-VERIFIED: FULL TEXT extracted from the arXiv PDF; Sections 2.2, 3, 5, 6,
  Appendix A locations, references list].
- arXiv:1811.07067, Remling-Scarbrough, "Oscillation theory and semibounded canonical
  systems" [FETCH-VERIFIED: FULL TEXT extracted; book-numbering citations, singular-interval
  formalism, tail embedding, trace-norming reparametrization].
- arXiv:0710.4128, Remling, "The absolutely continuous spectrum of one-dimensional
  Schrödinger operators" (MPAG 10 (2007) 359-373) [FETCH-VERIFIED: Section 2 metric +
  compactness, Lemma 4.2 continuity, via ar5iv].
- arXiv:1204.1827 v2, Suzuki, zeta canonical system [FETCH-VERIFIED: FULL TEXT extracted;
  abstract page for version history].
- arXiv:1606.05726 v3, Suzuki, Selberg-class Hamiltonians (JFA 281 (2021) 109116)
  [FETCH-VERIFIED: FULL TEXT extracted; Theorems 2.1-2.4, 6.1 verbatim; abstract page for
  the version-split comment].
- arXiv:2206.03682, Suzuki, screw function for zeta (JLMS 108 (2023) 1448-1487)
  [FETCH-VERIFIED: abstract page + ar5iv theorem list. ADVERSARY 2026-07-22: full text
  extracted and keyword-scanned; zero compactness/normal-family/Helly vocabulary hits
  (one innocuous "subsequent sections"; "compact" only as compact support / compact
  subsets inside uniform-convergence statements)].
- arXiv:2012.11121, Suzuki, chains of RKHS from unimodular functions (AIF 75 (2025))
  [FETCH-VERIFIED: abstract only. ADVERSARY 2026-07-22: full text extracted and
  keyword-scanned; zero hits for normal-family/Montel/Vitali/Helly/Banach-Alaoglu/
  tightness/precompact/equicontinuity vocabulary (one innocuous "subsequent sections");
  the novelty-rider absence claim for this paper is now full-text keyword level. The
  RATE question for clause (4) remains unchecked here (a keyword scan cannot settle it)].
- Remling homepage + lecture-notes page (math.ou.edu/~cremling) [FETCH-VERIFIED: no book
  draft or canonical-systems notes exist there].

Carried from prior rounds, unchanged:
- arXiv:2409.04862, Forester-Remling [FETCH-VERIFIED, #170 round].
- arXiv:2301.00421, Suzuki [FETCH-VERIFIED abstract, #170 round].

Secondary:
- Remling, Spectral Theory of Canonical Systems, de Gruyter Studies in Mathematics 70,
  2018: TOC chapter titles [SECONDARY, retail listings]; Section 5.2 / Thm 5.1 / Thm 5.7(b) /
  Cor. 5.8 contents [pinned via the author's own citations in 1811.07067 and 2409.04862;
  printed pages UNREAD].
- Winkler IEOT 22 (1995); Langer-Winkler IEOT 30 (1998); de Branges 1968: as cited inside
  Hur [SECONDARY at their own source level].
- Suzuki 1308.0228, 1907.07838, 1907.07302, 2209.12832, 2308.11860, 2301.05779: NOT READ
  this session; listed for the record.

## 6. What this enables / what remains open

**Enables.** e1u proceeds on a fully at-source foundation: the builder can quote Hur for
every space-level fact, use the Remling-Scarbrough tail convention for the finite-chain
embedding (reporting the tail angle as the boundary-condition choice), and certify
convergence locally on $M(x)$ while stating tail-scope explicitly. The adversary gains one
new probe (the $J(t;z,z)$ decay-rate uniformity test, Section 4) and one new citation duty
(Suzuki Thm 2.4 as the in-print cousin of the clause split).

**Remains open (SURVEYOR items).** (1) The printed book pages (labeling-level residual
only). (2) Suzuki's unread companions, most relevantly 2301.00421 at full-text level (the
Weil-form de Branges space under RH) and 1907.07302 (the operator survey, which may record
progress on the $1/2 < \omega \le 1$ extension of the zeta construction); a future sweep
should check whether anyone has since proven the $\omega > 1/2$ unconditional extension
promised "without essential difficulties" in 1204.1827 Section 5. (3) Whether Suzuki's
far-end condition (4) has a quantitative (rate) form anywhere in the series; none was found
in the texts read, and a rate is exactly what a lambda-uniform e1u version would need.
