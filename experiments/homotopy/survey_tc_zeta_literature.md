# SURVEYOR dossier: THH / TC / TP and the zeta function -- literature reconnaissance

Scope: does the literature already realize $-\zeta'/\zeta$, the von Mangoldt sum $\sum \Lambda(n) n^{-s}$, or
the Euler product as an $S^1$-equivariant invariant (trace / Euler characteristic / regularized determinant)
of $\mathrm{THH}(\mathbb{Z})$, $\mathrm{TC}(\mathbb{Z})$, or $\mathrm{TP}(\mathbb{Z})$? And specifically:
is the $i^{-s}$-weighting of Bokstedt torsion, and the THH -> TC Mobius/$1/\zeta$ reduction, a known construction?

Date: 2026-05-30. Surveyor role. Caveat: graded as far as the abstracts, introductions, and main-theorem
statements I read directly (Hesselholt and Morin PDFs read page by page; Connes-Consani and the CCM 2025
paper read at abstract/summary depth only -- flagged per row).

---

## 1. Scorecard

Q1 = expresses $-\zeta'/\zeta$ / von Mangoldt sum / Euler product as trace/Euler char/regularized det of an
$S^1$-equivariant THH/TC/TP invariant.
Q2 = attaches weight $i^{-s}$ (or scaling/$\lambda$-operation eigenvalue $i$, or Bott/periodicity grading) to
$S^1$-Tate periodicity to produce a Dirichlet series in $s$.
Q3 = relates the THH -> TC cyclotomic reduction (Nikolaus-Scholze, the $\varphi_p$ Frobenii) to Mobius
inversion / $1/\zeta$ / inclusion-exclusion over prime powers.

| Source | Q1 | Q2 | Q3 | Read depth |
|---|---|---|---|---|
| Hesselholt, *THH and the Hasse-Weil zeta function* (Contemp. Math., ~2018) | partial | partial | no | full (12 pp) |
| Morin, *THH and zeta values* (arXiv 2011.11549, 2020/2021) | partial | no | no | full intro (8 pp) |
| Connes-Consani, *Cyclic homology, Serre's local factors and $\lambda$-operations* (J. K-Theory, arXiv 1211.4239, 2014) | partial | partial | no | abstract + summary |
| Connes-Consani-Moscovici, *Zeta Spectral Triples* (arXiv 2511.22755, 2025) | no | no | no | abstract only |
| Morin (Bordeaux preprint *THH-ZetaValues.pdf*, expanded version of 2011.11549) | partial | no | no | full intro |
| Hesselholt-Nikolaus, *Topological cyclic homology* (Handbook of Homotopy Theory, 2019) | no | no | no | not read (background ref) |
| Bost-Connes / Witt-vector line (e.g. *Bost-Connes systems and periodic Witt vectors*, 2025) | no | no | partial | abstract only |

No source scored **yes** on any question. The exact construction posed in the task (Bokstedt torsion
$|\mathrm{THH}_{2i-1}(\mathbb{Z})| = i$ weighted by $i^{-s}$ assembling to $-\zeta'(s)$, then THH -> TC implementing
$1/\zeta$ Mobius) does **not** appear in the literature I found. The closest existing results all live one
step away, described below.

---

## 2. The most relevant sources

### 2.1 Hesselholt, *Topological Hochschild homology and the Hasse-Weil zeta function* (the closest single result)

Contemporary Mathematics volume (ICM-adjacent; the copy I read is the Rochester/Ravenel host PDF).
MSC 11S40, 19D55, 14F30. This is the paper that does, in spirit, exactly the "zeta as $S^1$-equivariant
invariant of TP" move -- but over a **finite field**, not over $\mathbb{Z}$, and it produces the Hasse-Weil
$\zeta(X,s)$ itself, not the von Mangoldt sum $-\zeta'/\zeta$.

Key construction. He sets $\mathrm{TP}_i(X) = \hat H^{-i}(\mathbb{T}, \mathrm{THH}(X))$, the $\mathbb{T}=S^1$-Tate cohomology of
Bokstedt's $\mathrm{THH}(X)$, and equips it with a meromorphic Frobenius $\varphi_p$ coming from the cyclotomic
structure. The headline is **Theorem A**, quoted verbatim:

> Let $k$ be a finite field of order $q=p^r$ ... If $f: X \to \mathrm{Spec}(k)$ is a smooth and proper
> morphism of schemes, then, as meromorphic functions on $\mathbb{C}$,
> $$\zeta(X,s) = \frac{\det_\infty(s\cdot\mathrm{id} - \Theta \mid \mathrm{TP}_{\mathrm{od}}(X)\otimes_{W,\iota}\mathbb{C})}{\det_\infty(s\cdot\mathrm{id} - \Theta \mid \mathrm{TP}_{\mathrm{ev}}(X)\otimes_{W,\iota}\mathbb{C})},$$
> where $\Theta$ is a $\mathbb{C}$-linear graded derivation such that $q^\Theta = \mathrm{Fr}_q^*$ and $\Theta(v) = \frac{2\pi i}{\log q}\cdot v$.

So this is a **regularized determinant** ($\det_\infty$, the Deninger-style zeta-regularized determinant of
$s\cdot\mathrm{id}-\Theta$) of an operator $\Theta$ acting on the **$S^1$-Tate periodic** invariant $\mathrm{TP}_*(X)$.
The operator $\Theta = \log_q(\mathrm{Fr}_q^*)$ is the infinitesimal generator of a "Frobenius flow," exactly the
Deninger flow the project's Arch 2 surveys care about. The periodicity element $t = c_1(\mathcal O(1)) \in
\mathrm{TP}_{-2}$ (the Bott/$S^1$-Tate periodicity class) acts with eigenvalue tied to $\frac{2\pi i}{\log q}$, which is
what makes the determinant a ratio of completed $\Gamma$-style factors and recovers the periodicity of $\zeta(X,s)$.

Grading rationale:
- Q1 = **partial**. It realizes $\zeta(X,s)$ (the full zeta of a finite-field scheme) as a regularized
  determinant of an operator on a genuinely $S^1$-equivariant THH invariant (TP = THH Tate). It does NOT
  produce $-\zeta'/\zeta$ or $\sum\Lambda(n)n^{-s}$ as such, and the base is $\mathbb{F}_q$, not $\mathbb{Z}$. The Euler
  product enters only implicitly through $\det(1 - q^{-s}\mathrm{Fr}_q^* \mid H^\bullet_{\mathrm{crys}})$, the standard
  Weil-cohomology shape, not via primes $p$ ranging over $\mathrm{Spec}\,\mathbb{Z}$.
- Q2 = **partial**. The weight here is $q^{-s}$ via $q^\Theta = \mathrm{Fr}_q^*$ (a single prime power $q$, eigenvalue
  of the geometric Frobenius), and the periodicity class $v$ carries the $\frac{2\pi i}{\log q}$ grading. This
  is the structural prototype of "attach an $s$-power to the $S^1$-Tate periodicity," but it is a
  $q^{-s}$ weight for one $q$, not the $i^{-s}$ ranging over all $i$ that the task assumes. The Dirichlet
  series the task wants ($\sum_i (\log i) i^{-s}$) is not produced.
- Q3 = **no**. The cyclotomic / $\varphi_p$ structure is used to manufacture $\Theta$, but it is never tied to
  Mobius inversion or $1/\zeta$. The reduction here is THH -> TP (Tate), not THH -> TC, and there is no
  inclusion-exclusion over prime powers.

Caveat noted in the paper itself: $\mathrm{TP}_*(X)$ "is generally not periodic" over $\mathbb{Z}$ and the construction
of $\varphi_p$ "does not always exist, and, when it does, its construction requires some work." That is precisely
the gap between his finite-field theorem and the $\mathrm{Spec}\,\mathbb{Z}$ case the project wants.

### 2.2 Morin, *Topological Hochschild homology and zeta values* (arXiv 2011.11549; expanded Bordeaux PDF)

This is the one paper in the corpus whose **base is $\mathbb{Z}$ / the sphere spectrum** and whose target is
genuinely the Dedekind/arithmetic zeta of schemes proper over $\mathrm{Spec}\,\mathbb{Z}$. It builds a motivic
filtration on $\mathrm{THH}, \mathrm{TP}, \mathrm{TC}^-$ (extending Bhatt-Morrow-Scholze and Antieau over $\mathbb{Z}$, using
Hahn-Raksit-Wilson-style even-filtration ideas), and reads off **special values** $\zeta^*(\mathcal X, n)$, not the
$\zeta$ function as a determinant. Key statements:

> **Theorem 1.8** (joint with Flach). Let $\mathcal X$ be a regular connected scheme of dimension $d$, proper over
> $\mathrm{Spec}(\mathbb{Z})$. We have $\det(\xi_{\mathcal X/\mathbb{S},n}) = \pm A(\mathcal X)^{n-d/2}\cdot \frac{\zeta^*(\mathcal X_\infty, n)}{\zeta^*(\mathcal X_\infty, d-n)}$.

> **Conjecture 1.9** (joint with Flach). $\lambda(\zeta^*(\mathcal X,n)^{-1}\cdot \mathbb{Z}) = \Delta(\mathcal X/\mathbb{S}, n)$.

The central object is $L\Omega^{<n}_{\mathcal X/\mathbb{S}} := \mathrm{gr}^n_F\,\Sigma^2 \mathrm{TC}^+(-)[-2n]$, a graded piece of a
$\mathbb{T}$-equivariant filtration on $\mathrm{THH}$ over the sphere; replacing the base $\mathbb{Z}$ by $\mathbb{S}$ is the explicit
philosophy ("provided one replaces in some sense the base ring $\mathbb{Z}$ by the sphere spectrum $\mathbb{S}$").
The motivation paragraph is striking: Morin says he "realized that this philosophy might be true when we saw
the computation of $\pi_*\mathrm{THH}(\mathcal O_F)$" -- i.e. the same Bokstedt-torsion computation the project is using
is what suggested the zeta connection to him. That is the nearest the literature comes to the project's
starting observation.

Grading:
- Q1 = **partial**. Zeta **special values** $\zeta^*(\mathcal X,n)$ are expressed via determinants of perfect
  complexes built from THH/TC$^-$/TC$^+$ filtration pieces over $\mathbb{S}$, and Corollaries 1.6-1.7 recover
  Milne's correcting factor and (finite-field case) $q^{\chi}$. But it is special values at integer $n$, not
  $-\zeta'/\zeta$ as a function of $s$, and not the von Mangoldt sum or the Euler product. The functional
  equation appears only as "a shadow" (Theorem 1.8 ratio).
- Q2 = **no**. The grading is the integer-weight motivic/Nygaard filtration index $n$ (Tate twists, weight
  $w = j+m$), used to extract values at $s=n$. There is no $i^{-s}$ Dirichlet series and no scaling action
  with eigenvalue $i$; the $S^1$ (= $\mathbb{T}$) acts but its Tate periodicity is not weighted into a Dirichlet series.
- Q3 = **no**. TC$^-$, TP, TC$^+$ all appear and the cyclotomic equalizer is in the background, but Mobius
  inversion / $1/\zeta$ / prime-power inclusion-exclusion is never invoked. The correcting factor
  $C_\infty(\mathcal X,n) = \prod_{i<n;j}(n-1-i)!^{(-1)^{i+j}\dim H^j}$ is a product of factorials, not a Mobius sum.

### 2.3 Connes-Consani, *Cyclic homology, Serre's local factors and the $\lambda$-operations* (J. K-Theory 2014, arXiv 1211.4239)

The classical (non-topological) prototype and the direct ancestor of the project's Arch 2 line. For a smooth
projective $X$ over a number field, **cyclic homology** with coefficients in the infinite adeles $A_\infty$,
acted on by the $\lambda$-operations, gives **Serre's archimedean local factors** of the Hasse-Weil $L$-function
as regularized determinants of the generator of the $\lambda$-flow. This is the $HC$ / $HP$ (periodic cyclic,
$S^1$-Tate) analogue of Hesselholt 2.1, but archimedean. From the abstract/summary:

> ... cyclic homology with coefficients in the ring of infinite adeles ... provides the right theory to
> obtain, using $\lambda$-operations, Serre's archimedean local factors ... as regularized determinants.

Grading (abstract/summary depth only; I did NOT decode the body PDF -- flagged):
- Q1 = **partial**. Archimedean Euler/$\Gamma$-factors of the $L$-function as regularized determinants on a
  periodic-cyclic ($S^1$-Tate) invariant. But this is the archimedean factor of $L$, on $HC/HP$ of a variety,
  not $-\zeta'/\zeta$ and not THH/TC over $\mathbb{S}$.
- Q2 = **partial**. The $\lambda$-operation $\lambda_k$ has eigenvalue $k^n$ on weight-$n$ pieces; the
  generator of the induced flow is the $\Theta$ whose determinant gives the $\Gamma$-factor. This is the
  "eigenvalue $i$ / scaling action" mechanism the task asks about, in its original (Connes) form. It produces
  $\Gamma$-factors, not a Dirichlet series $\sum i^{-s}$.
- Q3 = **no**. No Mobius / $1/\zeta$ / prime-power inclusion-exclusion (this is the single-archimedean-place story).

### 2.4 Connes-Consani-Moscovici, *Zeta Spectral Triples* (arXiv 2511.22755, 2025)

Most recent Connes-school zeta paper. From the abstract: self-adjoint operators as rank-one perturbations of
the spectral triple for the scaling operator on $[\lambda^{-1},\lambda]$, "only involves the Euler products over
the primes $p \le x = \lambda^2$," and computes **regularized determinants** that, normalized, converge to the
Riemann $\Xi$ function. This is the **scaling-site / spectral-triple** line, NOT a THH/TC/TP construction.

Grading (abstract only):
- Q1 = **no** (uses Euler products and regularized determinants of a scaling operator, but no THH/TC/TP and
  no von Mangoldt-as-equivariant-invariant; it is the prime-cutoff spectral-realization program).
- Q2 = **no** (scaling operator on an interval, not $S^1$-Tate periodicity of THH; the $i^{-s}$ weight is not present in this form).
- Q3 = **no**.

Relevance: it confirms the Connes school is pushing the *scaling-site / $\det \to \Xi$* angle in 2025, which is
adjacent to but disjoint from the THH route. Worth a deeper read if the project later wants the
prime-cutoff $\det \to \Xi$ machinery, but it does not answer Q1-Q3.

### 2.5 Bost-Connes / Witt-vector line (e.g. *Bost-Connes systems and periodic Witt vectors*, 2025)

The Bost-Connes system is the one place in the broader literature where $1/\zeta$, Mobius, and prime-power
inclusion-exclusion appear natively (the BC partition function is $\zeta$, the system's symmetries are the
ideles, and Witt-vector / $\lambda$-ring structure carries the Frobenii $\varphi_p$). Recent work ties BC
systems to (periodic) Witt vectors, and Witt vectors are exactly $\pi_0\mathrm{TR}/\mathrm{TP}$ in the THH world.

Grading (abstract depth only):
- Q1 = **no** (no THH/TC/TP determinant of $-\zeta'/\zeta$).
- Q2 = **no**.
- Q3 = **partial**. The BC system and Witt/$\lambda$-ring formalism is where the Frobenii $\varphi_p$ meet
  $1/\zeta$ and Mobius-type sums; this is the most promising **external** home for the project's Q3 conjecture,
  but no source connects it to the Nikolaus-Scholze THH -> TC equalizer specifically.

---

## 3. Bottom line

The THH -> von Mangoldt link as posed in the task is **not in the literature** -- not fully, and only obliquely
in pieces. No paper I found weights Bokstedt's $|\mathrm{THH}_{2i-1}(\mathbb{Z})| = i$ by $i^{-s}$ to get $-\zeta'(s)$, and
no paper identifies the Nikolaus-Scholze THH -> TC cyclotomic equalizer with Mobius inversion / multiplication
by $1/\zeta$. Both the $i^{-s}$-weighting (Q2) and the THH->TC = $1/\zeta$ claim (Q3) appear to be **original to
this project** as stated; I could not verify either anywhere.

The single closest existing result is **Hesselholt, *THH and the Hasse-Weil zeta function*, Theorem A**:
$\zeta(X,s)$ realized as a regularized determinant $\det_\infty(s\cdot\mathrm{id}-\Theta)$ of the Frobenius-flow
generator $\Theta$ acting on the $S^1$-Tate periodic invariant $\mathrm{TP}_*(X) = \hat H^{-*}(\mathbb{T},\mathrm{THH}(X))$.
It is the exact "zeta = determinant of an operator on an $S^1$-equivariant THH invariant" template the project
wants -- but it lives over $\mathbb{F}_q$ (one prime power, weight $q^{-s}$, $\zeta(X,s)$ not $-\zeta'/\zeta$), and it
uses THH -> TP (Tate), not THH -> TC. Morin's *THH and zeta values* is the closest thing **over $\mathbb{S}$/$\mathbb{Z}$**,
but it extracts integer special values, not the function $-\zeta'/\zeta$, and never touches the von Mangoldt
sum, the $i^{-s}$ weighting, or a Mobius reduction.

---

## 4. What this enables / what remains open

For BUILDER:
- The Hesselholt $\det_\infty(s - \Theta \mid \mathrm{TP}_{\mathrm{od}})/\det_\infty(s-\Theta \mid \mathrm{TP}_{\mathrm{ev}})$
  template is the object to imitate over $\mathbb{Z}$. The project's $i^{-s}$ weighting should be checked against
  whether it is secretly the $q^\Theta = \mathrm{Fr}^*$ relation summed over $\mathrm{Spec}\,\mathbb{Z}$ (i.e. is the project's
  $-\zeta'(s) = \sum_i(\log i)i^{-s}$ the $\log\det$ / trace of $\Theta$ in a global, $\mathbb{Z}$-based analogue?).
  The factor $\log i = -\partial_s i^{-s}$ matching $\Theta(v) \propto \log q \cdot$(grading) is suggestive and
  should be pinned down explicitly.
- Morin's $\mathrm{TC}^+(\mathbb{Z})$ / motivic-filtration machinery over $\mathbb{S}$ is the rigorous substrate if the project
  wants to work over $\mathbb{Z}$ rather than $\mathbb{F}_q$. His Corollary 1.4 ($F^*\mathrm{THH}(\mathcal O_F) \simeq \tau_{\ge 2*-1}\mathrm{THH}(\mathcal O_F)$)
  is the connectivity statement that makes the Bokstedt-torsion bookkeeping precise.

For ADVERSARY:
- The Q3 conjecture (THH -> TC = $1/\zeta$ Mobius) is unverified and original. Stress-test it: the
  Nikolaus-Scholze equalizer $\mathrm{TC} = \mathrm{eq}(\mathrm{TC}^- \rightrightarrows \mathrm{TP})$ is a homotopy equalizer over the
  Frobenii, and Mobius/$1/\zeta$ is an Euler-product inversion over primes. Check whether the equalizer is
  multiplicative-over-primes in the way $1/\zeta = \prod_p(1-p^{-s})$ is, or whether this is a category error
  (equalizer is additive/limit, Euler product is multiplicative). This is the load-bearing claim and the most
  likely failure point.
- D-H discipline note: Hesselholt and Morin both *require* the Euler product / crystalline-Frobenius structure
  (Arch 2 sits outside the D-H detector by design, per CLAUDE.md). A THH construction that produced
  $-\zeta'/\zeta$ should be checked to see whether it would also "work" for a Dedekind zeta without RH-relevant
  content; but since Arch 2 is exempt from D-H, the sharper test is whether the construction uses the *full*
  arithmetic of $\mathrm{Spec}\,\mathbb{Z}$ or only formal $\lambda$-ring data (cf. the project's Arch 2E Adams-spectrum
  finding that bare $\psi_p$ on concrete $\lambda$-rings has no zeta-zero spectrum).

For SYNTHESIZER:
- This sits with the existing Arch 2 dossiers (Connes-Consani arithmetic site / scaling site). The new datum
  is that the *topological* (over-$\mathbb{S}$) version of the Connes-Consani cyclic-homology determinant exists and
  is Hesselholt's, but only over $\mathbb{F}_q$; the over-$\mathbb{Z}$ version (Morin) gives special values, not the
  determinant of the flow. The project's conjecture would be the missing third corner: the over-$\mathbb{Z}$
  *determinant of the flow* yielding $-\zeta'/\zeta$.

Open / could not verify:
- I read Hesselholt and Morin in full at the intro/main-theorem level, but only the abstracts of
  Connes-Consani 1211.4239 and CCM 2511.22755 (the body PDFs did not decode through WebFetch). The
  $\lambda$-operation eigenvalue and $\Gamma$-factor determinant in 1211.4239 are stated from the abstract and
  the project's own Arch 2 notes, not from the decoded body.
- I did not find any paper using the phrase / construction "von Mangoldt as a THH invariant." Absence here is
  meaningful but not a proof of absence: a deeper search of Hesselholt's full bibliography and the
  Antieau-Krause-Nikolaus "prismatic cohomology of $\mathbb{Z}$" line (which computes $\mathrm{TC}(\mathbb{Z})$ explicitly) is the
  recommended next reconnaissance step before concluding the link is fully original.

---

## Sources

- Lars Hesselholt, *Topological Hochschild homology and the Hasse-Weil zeta function*, Contemporary Mathematics. https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/hesselholt1.pdf
- Baptiste Morin, *Topological Hochschild homology and zeta values*, arXiv:2011.11549. https://arxiv.org/pdf/2011.11549 ; expanded PDF https://www.math.u-bordeaux.fr/~bmorin/THH-ZetaValues.pdf
- Alain Connes, Caterina Consani, *Cyclic homology, Serre's local factors and the $\lambda$-operations*, J. K-Theory, arXiv:1211.4239. https://arxiv.org/abs/1211.4239
- Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755. https://arxiv.org/pdf/2511.22755
- Lars Hesselholt, Thomas Nikolaus, *Topological cyclic homology*, Handbook of Homotopy Theory (2019). https://web.math.ku.dk/~/trk734/papers/s07/handbook.pdf
- Thomas Nikolaus, Peter Scholze, *On topological cyclic homology*, arXiv:1707.01799. https://arxiv.org/pdf/1707.01799
- Marcel Bokstedt, *The topological Hochschild homology of $\mathbb{Z}$ and $\mathbb{Z}/p$* (unpublished). notes: https://pi.math.cornell.edu/~dmehrle/notes/references/bokstedt2.pdf
- *Bost-Connes systems and periodic Witt vectors* (2025). https://www.researchgate.net/publication/394174877_Bost-Connes_systems_and_periodic_Witt_vectors
