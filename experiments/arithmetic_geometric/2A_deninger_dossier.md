# 2A Candidate Dossier: Deninger's conjectural foliated-space program

> A deeper look at Christopher Deninger's program (1992-present) of constructing a "dynamical cohomology" for $\mathrm{Spec}(\mathbb{Z})$ via a conjectural foliated space whose flow's periodic orbits encode the primes. Companion to [2A_candidate_evaluation.md](2A_candidate_evaluation.md), [2A_R1_DH_exclusion.md](2A_R1_DH_exclusion.md), [2A_borger_dossier.md](2A_borger_dossier.md), [2A_lorscheid_dossier.md](2A_lorscheid_dossier.md), [2A_connes_dossier.md](2A_connes_dossier.md).
>
> Deninger's program is the most explicitly geometric of the Arch 2 candidates — it proposes building the very surface that Weil's proof would need. This dossier covers: the program's origin in the function-field analogy, the proposed foliated space, the conjectural cohomology and flow, where the program has progressed concretely vs where it remains entirely conjectural, and its scorecard against the 17-constraint framework.
>
> **Caveats upfront**: Deninger's program is famously the *most conjectural* of the major Arch 2 candidates — its central object (the foliated space) has never been constructed. I have partial familiarity with the Deninger 1991-2010 papers and the Leichtnam-Deninger collaborations; the post-2010 work is less covered.

## 1. Historical origin: lifting Weil's function-field proof

Deninger's program (Deninger 1991, 1994, 1998, 2002) starts from a precise structural analysis of Weil's RH proof for curves $C / \mathbb{F}_q$:

**Weil's proof uses**:
1. **Étale cohomology** $H^*(C, \mathbb{Q}_\ell)$, a finite-dimensional $\mathbb{Q}_\ell$-vector space.
2. **Geometric Frobenius** $F: C \to C$, acting on $H^*$.
3. **Lefschetz fixed-point formula**: $\#C(\mathbb{F}_{q^n}) = \sum_i (-1)^i \mathrm{Tr}(F^n | H^i)$.
4. **Poincaré duality** + **Hodge index theorem** on the surface $C \times C$ to force $|\alpha_i| = \sqrt q$.

**Deninger's question**: what kind of geometric object, sitting "above" $\mathrm{Spec}(\mathbb{Z})$, would support each of these structures?

**Deninger's proposal** (refined over several papers):
- The object is a **foliated dynamical system** $(X, \mathcal{F}, \Phi_t)$ where:
  - $X$ is a topological / smooth space (an "$\infty$-dimensional manifold").
  - $\mathcal{F}$ is a 1-dimensional foliation.
  - $\Phi_t: X \to X$ is a flow (the "Frobenius substitute") whose periodic orbits correspond to primes.
- The **cohomology** $H^*_{\mathcal{F}}(X)$ (foliated / "leafwise" cohomology) is the analog of étale cohomology.
- The flow $\Phi_t$ acts on this cohomology. Its eigenvalues are conjectured to be the imaginary parts of zeta zeros.
- **Periodic orbits** of $\Phi_t$ correspond to primes: an orbit of period $\log p$ for each prime $p$.

This is the most explicitly geometric Arch 2 candidate: it asks for a specific geometric object (foliated space), not just an algebraic framework.

## 2. The conjectural foliated space, in detail

**What Deninger imagines $X$ to look like**:
- $X$ should be a 3-dimensional "object" (in some generalized sense), with $\dim_{\mathbb{R}} X = 3$ giving room for:
  - A 1-dimensional "$\mathbb{R}_+^*$-flow direction" (the Frobenius substitute).
  - A 2-dimensional "transverse direction" that plays the role of $\mathrm{Spec}(\mathbb{Z})$.
- The foliation $\mathcal{F}$ is by 1-dimensional leaves (orbits of $\Phi_t$).
- The leafwise cohomology is what plays the role of étale cohomology.

**The dictionary** (Deninger 1998 makes this precise):

| Function field $C / \mathbb{F}_q$ | Number field $\mathrm{Spec}(\mathbb{Z})$ (Deninger's program) |
|---|---|
| $C(\overline{\mathbb{F}}_q)$ as a set | $X$ as a foliated space |
| Closed points $x \in C$ | Periodic orbits of $\Phi_t$ on $X$ |
| $\deg(x) = n$ for $x \in C(\mathbb{F}_{q^n})$ | Period of orbit = $\log p$ for prime $p$ |
| Geometric Frobenius $F$ | The flow $\Phi_t$ (continuous version of $F^t$) |
| $H^i(C, \mathbb{Q}_\ell)$ for $i = 0, 1, 2$ | $H^i_\mathcal{F}(X)$, infinite-dim but trace-class for $\Phi_t$ |
| Frobenius eigenvalues on $H^1$ | $\Phi_t$-eigenvalues on $H^1_\mathcal{F}$ at $t \to s$ |
| $C \times C$ surface (Hodge index) | $X \times X$ (foliated; Hodge index conjectural) |

**The Lefschetz trace formula on this space**:
$$\zeta(s) = \prod_{i=0}^{2} \det(s \cdot \mathrm{id} - \Phi^* | H^i_\mathcal{F}(X))^{(-1)^{i+1}}$$
in the "regularized determinant" sense. The zeros of $\zeta$ become the eigenvalues of $\Phi^*$ on $H^1_\mathcal{F}$.

## 3. What has been constructed (vs what is conjectural)

**Constructed pieces** (rigorous mathematics, not conjectures):

- **Foliated cohomology of foliated manifolds**: well-developed theory (Connes, Moore-Schochet, Heitsch-Lazarov, etc.). Applies to actual foliated manifolds but not to Deninger's hypothetical $X$.
- **Trace formulas for foliated flows**: Guillemin-Sternberg, Atiyah-Bott, Connes-Marcolli have versions. Connect to RH via Connes' approach.
- **Bost-Connes systems** (Bost-Connes 1995): QSM systems with $\zeta$-like partition functions. Closely related to Deninger's spirit but constructed via NCG, not foliated geometry.
- **Patterson-Sullivan / Selberg trace formulas**: well-developed for hyperbolic surfaces. Analog of Deninger's program for function field of an algebraic curve, NOT for $\mathrm{Spec}(\mathbb{Z})$.

**Conjectural pieces** (Deninger's actual program):

- **The foliated space $X$ itself**: never constructed. Deninger has discussed candidates (foliations on $\mathrm{Spec}(\mathbb{Z})$-like spaces, Arakelov-style models) but no candidate has been built rigorously.
- **The flow $\Phi_t$**: never constructed (depends on $X$).
- **The leafwise cohomology $H^i_\mathcal{F}(X)$**: depends on the construction of $X$ and the foliation.
- **The Lefschetz trace formula for $\Phi_t$**: depends on all of the above.
- **The Hodge index theorem on $X \times X$**: would depend on a satisfactory $X$.

**My honest assessment**: Deninger's program is more accurately a *vision* than a *theory*. It articulates what would be needed to lift Weil's proof to $\mathrm{Spec}(\mathbb{Z})$, but the central object remains conjectural after 30+ years.

## 4. Deninger's interpretation of $\mathbb{F}_1$

Unlike Borger, Lorscheid, or Deitmar, Deninger does NOT explicitly construct $\mathbb{F}_1$. Instead:

- **The "base"** in Deninger's program is implicit in the foliated structure. The flow $\Phi_t$ acts as if on an "$\mathbb{F}_1$-like" base, with the primes being periodic orbits.
- **Connection to $\mathbb{F}_1$ programs**: Deninger's foliated space could in principle be the "$\mathbb{F}_1$-scheme" in some sense — Connes-Consani's arithmetic site has been compared to it.

**Where Deninger differs from other Arch 2 candidates**:

| Candidate | Approach to $\mathbb{F}_1$ |
|---|---|
| Deitmar | Monoid schemes; $\mathbb{F}_1 = \{0, 1\}$ as a multiplicative monoid |
| Lorscheid | Blueprints; $\mathbb{F}_1$ is a blueprint with no addition relations |
| Borger | $\Lambda$-rings; $\mathbb{F}_1$ structure = Adams operations |
| Connes-Consani | Arithmetic site; $\mathbb{F}_1$ = topos with hyperring sheaves |
| **Deninger** | **No explicit $\mathbb{F}_1$**; the foliated space is the geometric base directly |

Deninger's framework is the most "geometry-forward": it tries to build the surface directly rather than first constructing a base scheme $\mathbb{F}_1$ and then a fiber product.

## 5. The "arithmetic surface" in Deninger

The surface analog $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ in Deninger's framework would be $X \times X$ (or some variant), the product of the foliated space with itself.

**Required structures on $X \times X$**:
1. A product foliation $\mathcal{F} \times \mathcal{F}$.
2. The flow $\Phi_t \times \Phi_s$ acting on $X \times X$ with two-parameter time.
3. Intersection theory on the leaf space.
4. **The Hodge index theorem**: the central open problem.

**The Hodge index theorem on $X \times X$** (Deninger's central open conjecture):
For a "divisor" $D$ on the foliated space $X \times X$, the self-intersection $D \cdot D$ has the right signature (negative for divisors not equivalent to the trivial one). This would force the Frobenius eigenvalues on $H^1_\mathcal{F}$ to lie on $|\alpha| = q^{1/2}$ in the spirit of Weil's proof.

**Status**: open. The intersection theory on Deninger's $X \times X$ doesn't exist because $X$ doesn't exist. The conjectured Hodge index would be the analog of the Castelnuovo-Severi inequality on $C \times C$ in Weil's proof.

## 6. What Deninger's program predicts about $\zeta$

**Lefschetz fixed-point formula** (constraint ix): the periodic orbits of $\Phi_t$ encode primes; the Lefschetz trace formula relates the flow's "fixed-point density" to the zeros of $\zeta$. **Structural prediction**: $\zeta(s)$ factors as a regularized determinant over the foliated cohomology, with poles / zeros corresponding to $\Phi_t$ eigenvalues.

**Frobenius substitute** (constraint viii): the flow $\Phi_t$ is the substitute. Its spectrum (acting on $H^1_\mathcal{F}$) should consist of the imaginary parts of zeta zeros. **Status**: conjectural; depends on existence of $X$.

**Per-prime Euler factors** (constraint x): each periodic orbit of period $\log p$ contributes a local factor $(1 - p^{-s})^{-1}$ in the regularized determinant.

**Positivity** (constraints xi-xiii): via Hodge index theorem on $X \times X$. **Status**: open. This is the central open problem.

## 7. Strengths of Deninger's framework

1. **Most explicitly geometric**: directly proposes a geometric surface (foliated space) on which intersection theory and Hodge index could in principle live. This is closer to Weil's actual proof structure than the other candidates.

2. **Clean structural dictionary**: the function-field-to-number-field translation is most transparent in Deninger's program. Each ingredient of Weil's proof has an explicit (if conjectural) counterpart.

3. **Sidesteps the $\mathbb{F}_1$ debate**: no need to construct a "base scheme below $\mathbb{Z}$" if you can construct the foliated space directly.

4. **Compatibility with NCG**: foliated cohomology (Connes' machinery) provides technical tools that Deninger can use. Connection to Bost-Connes systems is natural.

5. **Connects to dynamical systems**: brings in deep machinery from dynamical-systems trace formulas (Atiyah-Bott, Guillemin-Sternberg, Patterson-Sullivan), which is otherwise foreign to Arch 2.

6. **Cross-architecture appeal**: many researchers find the dynamical / foliated picture compelling because of the clean Lefschetz analogy.

## 8. Limitations of Deninger's framework

1. **The central object doesn't exist**: $X$, the foliated space, has not been constructed in 30+ years. Until $X$ is constructed, the program is a roadmap, not a theory.

2. **No partial implementations**: unlike Borger ($\mathrm{Spec}(W(\mathbb{Z}))$ explicitly), Lorscheid (blueprints explicitly), or Connes ($S_\mathbb{Q}$ explicitly), Deninger's $X$ has no concrete candidate that can be analyzed.

3. **Intersection theory blocked by $X$'s non-existence**: constraint (vi) is doubly open — no $X$, no intersection theory.

4. **Hodge index theorem doubly open**: (xi) requires both intersection theory AND positivity argument. Both are conjectural.

5. **Cohomology theory uncertain**: even if $X$ is constructed, which "foliated cohomology" to use is non-trivial. Leafwise de Rham? Connes' cyclic? Heitsch-Lazarov? Each has different properties.

6. **No published K1 analysis**: I'm not aware of a published analysis of whether Deninger's positivity (if formalized) would fall under R3.5's no-shortcut theorem. By analogy with Connes (R3.5 applies), it likely does — but if the Hodge index theorem can be proven by INTERSECTION-THEORETIC means (signature of intersection form), it escapes R3.5's trace-formula hypothesis. This is the central question.

## 9. Active research questions specific to Deninger (as of ~2025)

- **Constructing $X$**: the central problem. Several candidates have been proposed (foliated Arakelov spaces, Berkovich analytifications, $p$-adic dynamical systems) but none has been pinned down.
- **Bost-Connes-style models**: can the foliated space be replaced by a Bost-Connes QSM system, with the partition function playing the role of $\zeta$? This is a NCG version of Deninger, more tractable but losing the explicit geometric structure.
- **Foliated cohomology on conjectural $X$**: even if $X$ is constructed, the choice of cohomology and its formal properties are open.
- **Trace formula on the foliated space**: even if $X$ and its cohomology are constructed, the trace formula's rigorous formulation requires technical work.
- **Bridge to Bhatt-Morrow-Scholze prismatic cohomology (R5)**: could the prismatic site provide the right cohomology for a foliated version of $\mathrm{Spec}(W(\mathbb{Z}))$? Unclear; the foliation and the prismatic structure are different mathematical objects.

## 10. Combinability with other candidates

**With Borger**: Borger's $\mathrm{Spec}(W(\mathbb{Z}))$ could serve as a candidate for Deninger's $X$ — the foliation would come from the $\Lambda$-structure (with $\Phi_t = \prod_p \psi_p^{t/\log p}$, mimicking R4's bridge). This is the most promising Deninger-realization direction. The foliated cohomology would be $H^*_\Lambda(\mathrm{Spec}(W(\mathbb{Z})))$, possibly via prismatic cohomology (R5).

**With Connes**: Connes' $S_\mathbb{Q}$ is the natural NCG-style version of Deninger's $X$. The $\mathbb{R}_+^*$-action on $S_\mathbb{Q}$ matches Deninger's flow $\Phi_t$. R4 (Borger + Connes hybrid) is essentially a hybrid Deninger candidate: $X = \mathrm{Spec}(W(\mathbb{Z}))$ with $\Phi_t$ from Connes' action on $S_\mathbb{Q}$.

**With Lorscheid**: blueprints don't naturally support flows; Deninger + Lorscheid is awkward.

**With Deitmar**: monoid schemes are too simple to support dynamical structure.

**With Connes-Consani arithmetic site**: the arithmetic site $\mathcal{A}$ has a Frobenius-like endomorphism $\mathrm{Frob}_\mathrm{ar}$; this could be related to Deninger's $\Phi_t$ via discretization. Connes-Consani's topos-theoretic machinery could provide the categorical setting for Deninger's $X$.

**Most promising hybrid**: Deninger + (Borger + Connes + prismatic) — use Borger's $\mathrm{Spec}(W(\mathbb{Z}))$ as the foliated space, Connes' $\mathbb{R}_+^*$-action as the flow, and prismatic cohomology as the leafwise cohomology. This is essentially "Architecture 2 fully assembled" if it works.

## 11. Open scorecard for Deninger (post-R1)

The Deninger scorecard is largely identical to Connes' on the K1 side (R3.5 applies to trace-formula positivity), but differs on the geometric / cohomology side because Deninger's $X$ is conjectural:

| Constraint | Status | What's needed to close |
|---|---|---|
| (i) | ⏳ | No explicit base scheme; the foliated space $X$ plays the role implicitly. |
| (ii) | ⏳ | $X \times X$ as "arithmetic surface" — but $X$ doesn't exist. |
| (iii) | ⏳ | Embedding $\mathrm{Spec}(\mathbb{Z}) \to X$ would be natural but $X$ is undefined. |
| (iv) | ⏳ | Foliated cohomology of conjectural $X$. |
| (v) | ⏳ | Poincaré duality on $H^*_\mathcal{F}(X)$. |
| (vi) | ⏳ | Cycle class map + intersection theory on $X \times X$. **The central open problem.** |
| (vii) | ⏳ | Künneth for foliated cohomology of $X \times X$. |
| (viii) | 🟡 | $\Phi_t$ as flow on $X$ is the proposed substitute; structurally well-defined, but depends on $X$. |
| (ix) | 🟡 | Lefschetz trace formula in foliated form; proposed but conjectural. |
| (x) | 🟡 | Periodic orbits of period $\log p$ give Euler factors; structural prediction. |
| (xi) | ⏳ | Hodge index on $X \times X$ — depends on (vi). |
| (xii) | ⏳ | The positivity argument has to be intersection-theoretic (not trace-formula) to escape R3.5. Whether Deninger's version is escapable is the central question. |
| (xiii) | ⏳ | Castelnuovo-Severi analog. |
| (xiv) | ✅ | Deninger's framework specializes to Weil's proof for curves over $\mathbb{F}_q$ correctly (the foliated space becomes finite-dim, cohomology becomes étale). |
| (xv) | ⏳ | Twists not addressed in the conjectural framework. |
| (xvi) | ⏳ | Selberg class not the explicit target. |
| (xvii) | ✅ | R1 confirms D-H is excluded: linear combinations of Dirichlet series are not foliated-space constructions. |

Two ✅, three 🟡, twelve ⏳, no ❌.

**Decisive blocker**: (i)-(vii) ALL ⏳ because the central object $X$ has not been constructed. Once $X$ is constructed, several constraints could be closed at once — but constructing $X$ is the central 30-year open problem.

**Comparison to Borger**: Borger has 4 ✅ items (explicit construction of $\mathrm{Spec}(W(\mathbb{Z}))$, explicit Frobenius substitute, explicit D-H exclusion, Weil specialization). Deninger has only 2 ✅. The gap reflects the difference: Borger constructs the candidate; Deninger proposes its existence.

**Comparison to Connes**: Connes has 3 ✅ items (Frobenius substitute, Weil specialization, D-H exclusion). Deninger has 2 ✅. Connes' framework is more developed than Deninger's because Connes' $S_\mathbb{Q}$ is an explicit (if noncommutative) object, while Deninger's $X$ is purely conjectural.

## 12. Bottom line on Deninger

**Best aspect**: the structural dictionary is the cleanest among the candidates. Deninger explicitly articulates each Weil-proof ingredient and its conjectural counterpart over $\mathrm{Spec}(\mathbb{Z})$. The framework is the most "natural" lift of Weil's proof.

**Worst aspect**: the framework is the most conjectural. The central object $X$ has not been constructed after 30+ years of attempts. Until $X$ exists, the program cannot make concrete progress on (vi), (xi), or the central Hodge index question.

**Most likely path forward**: hybrid with Borger and/or Connes — use $\mathrm{Spec}(W(\mathbb{Z}))$ (Borger) as the foliated space, Connes' $\mathbb{R}_+^*$-action as the flow, and prismatic cohomology (R5) as the leafwise cohomology. R4 ([2A_R4_borger_connes_hybrid.md](2A_R4_borger_connes_hybrid.md)) is essentially this Deninger realization. This is the most promising direction for Arch 2 overall per [2A_path_forward.md](2A_path_forward.md).

**On R3.5's applicability**: it's plausible (but unverified) that Deninger's positivity formulation falls under R3.5's hypothesis — the trace formula structure of $\Phi_t$ on $H^1_\mathcal{F}$ would make the positivity P ⟺ RH. **However**, if the Hodge index theorem can be proven INTERSECTION-THEORETICALLY (via signature of an intersection pairing), it escapes R3.5 because intersection-theoretic positivity is structurally different from trace-formula positivity. Deninger's program is uniquely positioned to seek the intersection-theoretic version, which is why it remains the most-watched Arch 2 direction despite its conjectural status.

**Cross-cut to LEARNINGS finding #11 (2E)**: 2E showed that bare Adams operations $\psi_p$ on concrete $\Lambda$-rings have no zeta-zero spectrum — cohomology must do the lifting. The same principle applies to Deninger: the bare flow $\Phi_t$ on a "naive" foliated space wouldn't carry zeta information; the leafwise cohomology of a carefully-constructed $X$ would. The 2E lesson sharpens what Deninger's program would need to deliver beyond the bare flow.

## References (Deninger-specific)

- Deninger, C. (1991). *On the $\Gamma$-factors attached to motives*. Invent. Math. 104, 245–261. Initial framing of the analogy.
- Deninger, C. (1994). *Motivic L-functions and regularized determinants*. Proc. Sympos. Pure Math. 55(1), 707–743. The regularized determinant viewpoint.
- Deninger, C. (1998). *Some analogies between number theory and dynamical systems on foliated spaces*. Doc. Math. Extra Vol. ICM Berlin 1998, I, 163–186. The most complete statement of the program.
- Deninger, C. (2002). *A note on arithmetic topology and dynamical systems*. Algebraic Number Theory and Algebraic Geometry, Contemp. Math. 300, 99–114. Refinements.
- Deninger, C. (2008). *Analogies between analysis on foliated spaces and arithmetic geometry*. Groups and Analysis, London Math. Soc. Lecture Note Ser. 354, 174–190. Later survey.
- Leichtnam, E. (2005). *Scaling group flow and Lefschetz trace formula for laminated spaces*. Bull. Sci. Math. 129, 99–116. Technical foundations for foliated trace formulas.
- Leichtnam, E. (2014). *An invitation to Deninger's work on arithmetic zeta functions*. Geometry, Spectral Theory, Groups, and Dynamics, Contemp. Math. 387, 201–236. Pedagogical survey.
- Bost, J.-B.; Connes, A. (1995). *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*. Selecta Math. 1, 411–457. NCG-side parallel to Deninger.
- Connes, A.; Marcolli, M. (2005). *Quantum statistical mechanics over number fields and the Tomita-Takesaki theorem*. Selecta Math. 11(3), 325–347. Bridge between Deninger spirit and NCG.
- Manin, Yu. I. (2007). *Cyclotomy and analytic geometry over $\mathbb{F}_1$*. Quanta of Maths, 385–409. Conceptual connections.
