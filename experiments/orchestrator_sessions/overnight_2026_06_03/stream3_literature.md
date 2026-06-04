# Stream 3a: deep literature, the three weakest cells of the Spec(Z) cohomology landscape

> **Overnight run 2026-06-03. STAGED, NOT committed. SURVEYOR output, read-only on git.**
> Deepening of the three load-bearing cells in
> [`docs/03_research/spec_z_cohomology_landscape.md`](../../../docs/03_research/spec_z_cohomology_landscape.md):
> (1) Connes-Consani Feb-2026 "On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$" (arXiv:2602.15941),
> (2) the arithmetic standard conjectures (Gillet-Soule arithmetic Hodge index; the arithmetic analogue
> of Grothendieck's Hodge standard conjecture), (3) Yuan-Zhang adelic-line-bundle arithmetic Hodge index.
>
> **Evidence discipline.** Every claim is tagged PROVED / COMPUTED / CITED / STRUCTURAL-READING.
> The three primary sources were read at the abstract+theorem-statement level from the originals:
> arXiv:2602.15941 (Connes-Consani abstract, verbatim), arXiv:1304.3538 (Yuan-Zhang I, Theorems 1.1
> and 1.3 read from the PDF), arXiv:alg-geom/9608003 (Takeda, Conjecture 1.2 and 2.2 read from the PDF,
> which transcribes the Gillet-Soule conjecture). No new mathematics is claimed; this is a map.
> The main agent should independently re-verify the arXiv IDs and the quoted theorem statements before
> anything is recorded in LEARNINGS or the scorecard.

---

## 0. The one-line answer to "do these three cells move toward a polarization?"

| Cell | What it provides | Does it move toward the polarization (08A M4)? |
|---|---|---|
| **Connes-Consani 2026 Jacobian** | A Picard-**monoid** realization of the adele class space; the Riemann sector = metrized rank-1 groups (Arakelov line bundles); the singular strata that carry the spectral realization of L-functions | **No.** It is a deeper *realization* substrate (ingredient i, and a refined ii via the monoid/duality). The abstract states **no positivity, no polarization, no RH**. It is the 2026 confirmation of the survey's pattern: structure on the realization side, polarization deferred. |
| **Arithmetic standard conjectures (Gillet-Soule)** | The *named conjecture* whose codim-$p$ positivity is the arithmetic Hodge standard conjecture: $\mathbf{AH_p}$. Codim-1 is a **theorem** (Faltings-Hriljac $n{=}1$, Moriwaki general $n$). Codim $\ge 2$ is **wide open**. | **It literally IS 08A M4 in form, but it is NOT yet the RH-relevant instance.** 08A M4 needs $\mathbf{AH_p}$ on the *product* $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$ for the Frobenius correspondence class $\Gamma_S$, which is a higher-codimension cycle on a 2-dimensional-over-$\mathbb{Z}$ object that **does not yet exist**. The proven codim-1 case is the Faltings-Hriljac "too local" signature already in the scorecard. |
| **Yuan-Zhang adelic Hodge index** | The arithmetic Hodge index extended to **adelic** (limit-of-integral-model) metrized line bundles, on a fixed normal projective variety of any dimension $n$, with an explicit signature theorem (Thm 1.3). | **No, in the dimension-reaching sense that matters.** Its higher-dimensionality is in the *ambient variety*, not in the *codimension of the cycle*: it is still **codimension-1** (line bundles / divisors). It does NOT reach the higher-codimension Gillet-Soule conjecture, and it is on a **fixed single variety**, never a self-product carrying a Frobenius correspondence. It strengthens the "too local" bracket; it does not cross the universal gap. |

The deepening below substantiates each line with the exact theorem statements.

---

## 1. Connes-Consani, "On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$" (arXiv:2602.15941, 17 Feb 2026)

### 1.1 What the paper provides (CITED, abstract read verbatim)

The abstract (verbatim from arXiv:2602.15941, accessed 2026-06-02):

> "We interpret the structure of the adele class space of the rationals -- and specifically its Riemann
> sector -- as the natural monoidal extension of the Picard group of the arithmetic curve
> $\overline{\mathrm{Spec}\,\mathbb{Z}}$. We identify the elements of this space with torsion-free rank-1
> abelian groups $L$ endowed with rigidifying data. In the Riemann sector, this data corresponds to a
> norm, extending the classical notion of metrized line bundles in Arakelov geometry. For the full adele
> class space, we replace the norm with a group morphism to $\mathbb{R}$ and a combinatorial datum: a
> parametrization of the roots of unity associated with the character dual of $L$. We show that the
> product of adeles is represented geometrically by the tensor product of these rank-1 groups and their
> rigidifying structures. The resulting monoid space generalizes the Picard group to the full adelic
> context by incorporating the singular strata required for the spectral realization of L-functions."

Structural decoding of the abstract:

- **The Picard MONOID (not group).** The central object is a *monoid* extension $\widehat{\mathrm{Pic}}$ of the
  Picard group of $\overline{\mathrm{Spec}\,\mathbb{Z}}$. Classical Arakelov $\widehat{\mathrm{Pic}}(\overline{\mathrm{Spec}\,\mathbb{Z}})$
  is a *group* of metrized line bundles (rank-1 projective $\mathbb{Z}$-modules + a norm at $\infty$), and it
  is well known to be $\cong \mathbb{R}$ via the arithmetic degree (CITED: standard, Neukirch/Soule). The
  2026 move is to **drop invertibility**: allow rank-1 torsion-free groups $L$ that are NOT projective, with
  "rigidifying data" that degenerates. This is the **monoid** of all metrized rank-1 objects, and the
  degenerate ones are the **"singular strata."**
- **The Riemann sector = Arakelov line bundles.** On the locus where the rigidifying datum is a genuine norm,
  the objects ARE the classical metrized line bundles. So the new object *contains* Arakelov $\widehat{\mathrm{Pic}}$
  as a sub-locus and adds the singular boundary.
- **The full adele class space.** Off the Riemann sector the norm is replaced by (a) a group morphism $L\to\mathbb{R}$
  (a "degree-like" linear functional that need not be a norm) and (b) a combinatorial root-of-unity parametrization
  (the character-dual datum). This is the geometric re-encoding of the adele class space $\mathbb{A}_{\mathbb{Q}}/\mathbb{Q}^\times$
  that Connes' 1999 trace formula lives on.
- **Why "for the spectral realization of L-functions."** The point of the singular strata is that the spectral
  realization (Connes 1998 Selecta; the trace formula whose spectral side is the zeros) requires exactly the
  degenerate/boundary objects that the *group* $\widehat{\mathrm{Pic}}$ omits. The monoid supplies them
  geometrically.

### 1.2 What the paper does NOT provide (CITED: absence in the abstract; STRUCTURAL-READING for the implication)

- **No positivity.** The abstract states no quadratic form, no PSD/negative-definite signature, no Weil-positivity
  statement, no Hodge index. (CITED: verbatim abstract above contains none.)
- **No polarization.** A Picard *monoid* is a moduli/realization object. A polarization is an extra datum (an ample
  class + a positive cup form). The abstract describes the monoid and its tensor (multiplicative) structure only.
- **No RH.** No RH-equivalent statement is claimed.
- **No de Branges / no Sonin space here.** The 2021 Connes-Consani Weil-positivity-at-the-archimedean-place result
  (Sonin space, arXiv:2006.13771) is a separate paper; the 2026 Jacobian paper, per its abstract, is the
  realization/Picard-monoid construction, not the positivity.

### 1.3 Verdict for the scorecard cell (STRUCTURAL-READING)

The survey's existing cell reads: "$(i)$ $\circ\!\to\!\checkmark$, $(ii)$ $\circ$, $(iii)$ $\times$, K2 $\checkmark$ on $F$;
open step: turn the Picard/realization structure into a signed pairing (not de Branges)." **This deepening CONFIRMS that
cell verbatim and sharpens it:**

- $(i)$ Trace/realization is the *content* of the 2026 paper. Upgrade-justification confirmed: the monoid is a genuine
  geometric realization carrier (the singular strata are precisely what the spectral realization needs).
- $(ii)$ Duality: the tensor product of rank-1 objects gives the multiplicative/monoidal structure; this is the
  Picard-side shadow of duality but the paper does not (per abstract) state a Poincare-duality pairing as a theorem.
  Leave at $\circ$ (partial).
- $(iii)$ Polarization: **absent**, by the abstract. The Picard MONOID is the wrong kind of object to carry a
  polarization directly: a polarization is a map $\mathrm{Pic}\to\mathrm{NS}$ plus a positive form on $\mathrm{NS}$;
  the 2026 paper builds $\mathrm{Pic}$ (the monoid), not $\mathrm{NS}$ with a signed intersection form.
- The project's R3.5 no-shortcut theorem still applies: any *trace-formula* positivity extracted from this monoid
  would be K1-equivalent to RH. The escape (an honest intersection signature) is exactly what the monoid does not
  supply.

**The 2026 paper does NOT move toward a polarization.** It is the strongest-to-date *realization* substrate, and it
lands precisely on the survey's "all roads to the signature" pattern: the realization side moved (again), the
polarization did not.

### 1.4 One genuinely new structural angle worth flagging to BUILDER (STRUCTURAL-READING, speculative)

The Picard *monoid* (with its singular strata) is a more honest analogue of the function-field $\mathrm{Pic}^0(C)$ +
boundary than the Picard *group* alone. In Weil's proof the polarization lives on $\mathrm{Jac}(C)=\mathrm{Pic}^0(C)$
and the Rosati form is on $\mathrm{End}^0(\mathrm{Jac})$. The 2026 paper names the would-be "$\mathrm{Jac}(\overline{\mathrm{Spec}\,\mathbb{Z}})$".
**If** a Rosati-type involution and a positive trace form could be defined on the endomorphisms of this monoidal
Jacobian, that would be 08A M2/M4 in this language. The paper does not do this. But it is the first object that even
*names the Jacobian*, which is the carrier 08A's Rosati formulation wants. This is a BUILDER lead, not a result:
the open question is whether the monoid's endomorphism structure admits a positive involution, and the R3.5 caveat
warns that if positivity is read off a trace identity it is circular.

---

## 2. The arithmetic standard conjectures: Gillet-Soule, Moriwaki, and whether this is literally 08A M4

### 2.1 The classical statement being lifted (CITED: Grothendieck via Takeda Conj 1.1)

Let $X$ be smooth projective of dimension $n$ over an algebraically closed field, $A^p(X)$ the codim-$p$ cycles mod
homological equivalence, $H$ an ample line bundle, $L_H : A^p(X)\to A^{p+1}(X)$ cup with $c_1(H)$. Grothendieck's
standard conjectures (Takeda Conj 1.1, transcribed verbatim from arXiv:alg-geom/9608003 p.1), for $p\le n/2$:

- $\mathbf{A_p}(X,H)$ (Hard Lefschetz): $L_H^{n-2p}: A^p(X)\to A^{n-p}(X)$ is an isomorphism.
- $\mathbf{H_p}(X,H)$ (Hodge index / Hodge standard): for $0\ne x\in A^p(X)$ with $L_H^{n+1-2p}(x)=0$,
  $$(-1)^p\,\deg\!\big(L_H^{n-2p}(x)\cdot x\big) > 0.$$

(CITED: in characteristic 0, $\mathbf{H_p}$ is a **theorem** via Hodge theory + the Hodge-Riemann bilinear relations;
it is open in positive characteristic. This is exactly the "Hodge standard conjecture = Rosati positivity over a field"
that 08A section 3 names.)

### 2.2 The arithmetic analogue, exactly (CITED: Gillet-Soule via Takeda Conj 1.2, verbatim transcription)

Let $X$ be a regular scheme projective and flat over $\mathbb{Z}$ with smooth generic fiber $X_{\mathbb{Q}}$ (an
"arithmetic variety"), $n$ = relative dimension over $\mathbb{Z}$, $\widehat{CH}^p(X)$ the arithmetic Chow groups
(Gillet-Soule), $F_\infty$ = complex conjugation on $X(\mathbb{C})$. For an arithmetically ample Hermitian line bundle
$(H,\|\cdot\|)$, cup with the arithmetic first Chern class gives $L_{H,\|\cdot\|}:\widehat{CH}^p(X)_{\mathbb{R}}\to
\widehat{CH}^{p+1}(X)_{\mathbb{R}}$.

**Gillet-Soule arithmetic standard conjectures** (Takeda Conj 1.2, transcribed verbatim from arXiv:alg-geom/9608003 p.2;
attributed there to Gillet-Soule, *Arithmetic analogs of the standard conjectures*, in *Motives* PSPUM 55.1, AMS 1994,
pp. 129-140): there exists an $F_\infty$-invariant Hermitian metric $\|\cdot\|$ on $H_{\mathbb{C}}$ such that for
$2p\le n+1$:

- $\mathbf{AA_p}(X,H,\|\cdot\|)$ (arithmetic Hard Lefschetz): $L_{H,\|\cdot\|}^{n+1-2p}: \widehat{CH}^p(X)_{\mathbb{R}}
  \to \widehat{CH}^{n+1-p}(X)_{\mathbb{R}}$ is an isomorphism.
- $\mathbf{AH_p}(X,H,\|\cdot\|)$ (arithmetic Hodge index): for $0\ne x\in\widehat{CH}^p(X)_{\mathbb{R}}$ with
  $L_{H,\|\cdot\|}^{n+2-2p}(x)=0$,
  $$(-1)^p\,\widehat{\deg}\!\big(L_{H,\|\cdot\|}^{n+1-2p}(x)\cdot x\big) > 0.$$

This $\mathbf{AH_p}$ is **the arithmetic Hodge standard conjecture.** Note the arithmetic shift: where the geometric
Hodge index uses $L_H^{n-2p}$ and the condition $L_H^{n+1-2p}x=0$ on an $n$-dimensional variety, the arithmetic version
uses $L^{n+1-2p}$ and the condition $L^{n+2-2p}x=0$, because $\widehat{\deg}$ measures the "$+1$ arithmetic dimension"
contributed by the archimedean place. (CITED: this is exactly the "$\mathrm{Spec}(\mathbb{Z})$ adds one dimension"
phenomenon the project repeatedly hits, the two-clock / archimedean balance #18/#20/#34.)

### 2.3 What is proven vs open (CITED, precise)

- **Codimension 1 ($p=1$): PROVEN, unconditionally, in all relative dimensions.**
  - $n=1$ (arithmetic surfaces): Faltings 1984 + Hriljac 1985 (the Hodge index theorem for divisors on an arithmetic
    surface; $\mathbf{H_1}$ proven via positivity of the Neron-Tate height pairing on the Jacobian + intersection of
    cycles not meeting the generic fiber). (CITED: Takeda p.2.)
  - general $n$ (codim-1 cycles on higher-dimensional arithmetic varieties): **Moriwaki 1996**, *Hodge index theorem
    for arithmetic cycles of codimension one* (arXiv:alg-geom/9403011, abstract verbatim: "we will give a partial
    answer for arithmetic analogues of Grothendieck's standard conjectures due to H. Gillet and C. Soule"). Moriwaki
    proved $\mathbf{H_1}(X,H,\|\cdot\|)$ for any arithmetically ample $(H,\|\cdot\|)$. (CITED: Takeda p.2.)
  - Kunnemann (1995/96) reduced the conjectures to analogues for Arakelov Chow groups and proved them for projective
    spaces and (later) regular quadrics. (CITED: Takeda p.4.)
- **Codimension $\ge 2$ ($p\ge 2$): WIDE OPEN.** Yuan-Zhang's introduction states it directly (CITED, arXiv:1304.3538
  p.2, verbatim): "the high-codimensional case of the Gillet-Soule conjecture is still **wide open**."
- **Takeda's own result (CITED):** he resolves $\mathbf{AH_p}$ into (a) the *geometric* standard conjectures for the
  generic fiber $X_K$ and (b) a *height-pairing positivity* on homologically-trivial primitive arithmetic cycles
  $CH^p(X_K)^0$ (Beilinson's conjecture) plus (c) a *vertical-cycle* conjecture. So even granting Grothendieck's
  standard conjectures over the generic fiber, the arithmetic Hodge index for $p\ge2$ needs the Beilinson height
  positivity, which is itself open. (CITED: Takeda Conj 2.2 $\mathbf{FH_p}$ and the surrounding text, PDF pp.4-5:
  $(-1)^p\langle L_H^{n+1-2p}(x),x\rangle$ positive on $CH^p_{\mathrm{fin}}(X)_{\mathbb{R}}$.)

### 2.4 Is this literally 08A M4? (STRUCTURAL-READING, the central question of this cell)

**In FORM: yes, exactly.** 08A M4 is "the arithmetic Hodge standard conjecture": the positivity $\mathbf{AH_p}$ above
*is* the standard professional name for what 08A calls "arithmetic Rosati positivity = the engine of RH." The 08A
document already says this (section 3: "the positivity of the Rosati form is the Hodge standard conjecture"). So the
literature cell and 08A M4 are the **same named object**.

**In INSTANCE: no, not yet, and this is the sharp content of the deepening.** The proven cases ($p=1$, Faltings-Hriljac-
Moriwaki) are exactly the scorecard's "Faltings-Hriljac (too local)" bracket: a real, proven $\mathbf{AH_1}$ on a single
arithmetic variety. To get RH for $\zeta$ the project needs $\mathbf{AH_p}$ for the **Frobenius correspondence class
$\Gamma_S$** on the **product** $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$. Two gaps separate the proven
case from the needed case:

1. **The object does not exist.** $\mathrm{Spec}(\mathbb{Z})\times_{\mathbb{F}_1}\mathrm{Spec}(\mathbb{Z})$ is the
   missing 2-dimensional-over-$\mathbb{Z}$ arithmetic variety. Gillet-Soule's $\widehat{CH}^p$ is defined for *regular
   projective flat $X/\mathbb{Z}$ with smooth generic fiber*. The product is none of these (it has no scheme-theoretic
   existence; the $\mathbb{F}_1$ candidates that might host it -- Lorscheid blueprints, Borger $W(\mathbb{Z})$, the C-C
   monoid -- have no arithmetic intersection theory yet). So $\mathbf{AH_p}$ cannot even be *stated* for $\Gamma_S$ yet.
2. **The needed codimension is $\ge 2$, the open range.** On the (relative) 2-dimensional product, the Frobenius
   correspondence $\Gamma_S$ is a cycle whose RH-relevant primitive part sits in codimension $\ge 2$ in the arithmetic
   Chow group (the diagonal and the graph are divisors on a surface, but the *self-intersection / correspondence
   algebra* positivity that gives $|\alpha|=\sqrt q$ is the higher-codim Hodge-index instance). This is exactly the
   $p\ge 2$ range Yuan-Zhang flags as wide open.

**So: the literature has PROVEN the codim-1 arithmetic Hodge index (which is the "too local" bracket already in the
scorecard), and the RH-relevant instance is the higher-codim case on a product that does not exist. 08A M4 = the
Gillet-Soule arithmetic standard conjecture $\mathbf{AH_p}$, $p\ge 2$, instantiated on $\mathrm{Spec}(\mathbb{Z})^{\times 2}$
with the cycle $\Gamma_S$. Both the higher-codim conjecture AND the product object are open. This is the universal gap,
restated in the most professional vocabulary available.**

### 2.5 Scorecard update for the Gillet-Soule cell (STRUCTURAL-READING)

The survey cell reads "$(i)\times$, $(ii)\circ$ wrong dim, $(iii)\circ$ inherits single-surface; open step: cycle-class
for $\Gamma_S$ on the product + arithmetic standard conjecture." This deepening **confirms and refines**:

- $(iii)$ should be read as "$\circ$ = $\mathbf{AH_1}$ PROVEN (Moriwaki, all $n$), $\mathbf{AH_{p\ge2}}$ OPEN." The
  partial mark is justified: codim-1 is a theorem, the RH-relevant codim is open.
- The "single sharpest open step" is exactly right and now has a precise name: **$\mathbf{AH_p}$ for $p\ge2$ on a
  product carrying $\Gamma_S$** = the open higher-codimension Gillet-Soule conjecture + the missing product.

---

## 3. Yuan-Zhang adelic Hodge index: does its higher-dimensionality reach the product surface?

### 3.1 The classical theorem it extends (CITED: Yuan-Zhang Thm 1.1, read from arXiv:1304.3538 PDF p.3)

> **Theorem 1.1 ([Fal, Hr, Mo1]).** Let $K$ be a number field, $\pi:\mathcal{X}\to\mathrm{Spec}\,O_K$ a regular
> arithmetic variety, geometrically connected of relative dimension $n\ge1$. Let $\overline{\mathcal{M}}$ be a Hermitian
> line bundle on $\mathcal{X}$, and $\overline{\mathcal{L}}$ an ample Hermitian line bundle on $\mathcal{X}$. Assume
> $\mathcal{M}_K\cdot\mathcal{L}_K^{n-1}=0$ on the generic fiber $\mathcal{X}_K$. Then the arithmetic intersection number
> $$\overline{\mathcal{M}}^2\cdot\overline{\mathcal{L}}^{n-1}\le 0,$$
> with equality (under positivity of $\mathcal{L}$ and strict positivity of the metric) iff $\overline{\mathcal{M}}=
> \pi^*\overline{\mathcal{M}}_0$ for some $\overline{\mathcal{M}}_0$ on $\mathrm{Spec}\,O_K$.

This is the Faltings-Hriljac ($n=1$) / Moriwaki (general $n$) codim-1 arithmetic Hodge index, restated with line bundles.

### 3.2 The Yuan-Zhang main theorem (CITED: Thm 1.3, read verbatim from PDF p.4)

> **Theorem 1.3.** Let $K$ be a number field, $\pi:X\to\mathrm{Spec}\,K$ a normal and geometrically connected projective
> variety of dimension $n\ge1$. Let $\overline{M}$ be an integrable adelic line bundle on $X$, and $\overline{L}_1,
> \dots,\overline{L}_{n-1}$ be $n-1$ nef line bundles on $X$ where each $L_i$ is big on $X$. Assume $M\cdot L_1\cdots
> L_{n-1}=0$ on $X$. Then
> $$\overline{M}^2\cdot\overline{L}_1\cdots\overline{L}_{n-1}\le 0,$$
> with the stated equality characterization ($r\overline{M}=\pi^*\overline{M}_0$).

And the signature statement (PDF p.4, verbatim paraphrase): the pairing $\langle\overline{M}_1,\overline{M}_2\rangle=
\overline{M}_1\cdot\overline{M}_2\cdot\overline{L}_1\cdots\overline{L}_{n-1}$ on the space $W$ of $\overline{L}_i$-bounded
integrable adelic line bundles has $V=\pi^*\widehat{\mathrm{Pic}}(K)_{\mathbb{Q}}$ a maximal isotropic subspace,
the pairing **negative semi-definite on $V^\perp$, and negative definite on $V^\perp/V$.**

### 3.3 The two reasons this does NOT reach the product surface (STRUCTURAL-READING, anchored on the theorem)

**(A) It is codimension 1, not higher codimension.** The objects are adelic *line bundles* $\overline{M}$ (codim-1
arithmetic cycles / divisors). The "higher dimension" in Yuan-Zhang is the dimension $n$ of the *ambient variety* $X$,
NOT the codimension of the cycle. The signature theorem is the codim-1 Hodge index in disguise (one variable $\overline{M}$
squared, intersected against $n-1$ fixed nef bundles to cut down to a surface-like 2-dimensional pairing). The
introduction is explicit (CITED, PDF p.2, verbatim): "The aim of this series of two papers is to prove an *adelic version*
of the Hodge index theorem for (**still**) codimension one cycles on varieties over a finitely generated field $K$."

This is the decisive fact: **Yuan-Zhang extends the metric/coefficient theory (Hermitian -> adelic = limits of integral
models, Berkovich/non-archimedean at all places), and the ambient dimension (to any $n$), but it does NOT advance the
codimension. It remains $\mathbf{AH_1}$, the proven, "too local" range.** The RH-relevant Frobenius-correspondence
positivity is $\mathbf{AH_{p\ge2}}$, which Yuan-Zhang explicitly leaves "wide open."

**(B) It is on a fixed single variety, with no self-product and no Frobenius correspondence.** Theorem 1.3 is stated for
a single normal projective $X/K$. There is no $X\times X$, no diagonal, no graph of an endomorphism realizing a Frobenius,
and no place-graded $(1,p)$ bidegree (#25/2Q). The applications (CITED, PDF p.2: non-archimedean Calabi-Yau uniqueness;
rigidity of preperiodic points of polarizable dynamical systems) are about *one* variety and its self-maps' invariant
metrics, not about a correspondence carrying $\zeta$. The adelic generality is genuinely useful infrastructure (it is the
"limit of integral models" technology that an $\mathbb{F}_1$ product surface might eventually need), but it does not by
itself produce the product or the correspondence.

### 3.4 What Yuan-Zhang DOES strengthen in the bracket (STRUCTURAL-READING)

It sharpens the "Faltings-Hriljac too local" bracket of the scorecard's section 3 in two ways worth recording:

- **Adelic = all-places-at-once.** The pairing is genuinely adelic (archimedean Arakelov + non-archimedean Berkovich,
  glued as limits of integral models). This is the most complete codim-1 arithmetic Hodge index available, and it is the
  closest existing technology to the "global, all-places" requirement the survey's section 3 demands of the missing
  polarization. It satisfies "global" and fails only "carries the Frobenius trace $t$" and "is the higher-codim instance."
- **The negative-definiteness on $V^\perp/V$** is the literal proven signature. It confirms the project's own
  Faltings-Hriljac reproduction (2H-2P) is the right object and is now available in maximal (adelic, any-$n$, codim-1)
  generality. The gap is unchanged: it is one variety, codim-1, no correspondence.

### 3.5 Scorecard placement (STRUCTURAL-READING)

Yuan-Zhang is best recorded as the **state-of-the-art realization of the "Faltings-Hriljac (too local)" bracket**, not
as a new cell. It strengthens that bracket to (adelic, all-$n$, all-places, codim-1) but does **not** cross any of the
three sides that pin the missing object: it is global $\checkmark$ but **codim-1 not codim-$p$**, **single variety not
product**, **no Frobenius trace $t$**. It does not reach the product surface.

---

## 4. Synthesis: where the three cells leave the universal gap

All three cells reinforce the survey's central thesis (#30, "all roads to the signature") with 2026-current,
primary-source precision:

1. **Connes-Consani 2026** is the realization side moving again (now a Picard *monoid* with the singular strata for
   spectral realization). It names the "Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$" for the first time, which is
   the carrier 08A's Rosati formulation wants, but it states **no positivity**. Realization advanced; polarization
   deferred. (CITED: abstract.)
2. **The Gillet-Soule arithmetic standard conjectures** give the universal gap its exact professional name:
   $\mathbf{AH_p}$, the arithmetic Hodge standard conjecture. The codim-1 case is a **theorem** (Faltings-Hriljac-
   Moriwaki = the "too local" bracket); the RH-relevant **codim-$\ge2$ case is wide open**, AND it must be instantiated
   on a product object that does not yet exist with a Frobenius cycle class. **08A M4 = $\mathbf{AH_{p\ge2}}$ on
   $\mathrm{Spec}(\mathbb{Z})^{\times2}$ with $\Gamma_S$. The form is literally the same; the instance is doubly open
   (higher codim + missing product).**
3. **Yuan-Zhang** is the strongest existing technology *inside* the proven bracket: adelic, all-dimensions, all-places,
   but **still codimension 1** (their own word) and **on a single variety**. It does not reach the higher-codimension
   conjecture and does not build the product or the correspondence. It strengthens the "too local" side of the bracket;
   it does not cross the gap.

The net 2026 picture is unchanged from the survey's diagnosis and sharper: the missing object is the higher-codimension
arithmetic Hodge standard conjecture $\mathbf{AH_{p\ge2}}$ for the Frobenius correspondence $\Gamma_S$ on the
not-yet-constructed product $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$. Every 2017-2026 advance has been
either (a) the realization side (Connes-Consani monoid; prismatic) or (b) the codim-1, single-variety side of the
polarization (Yuan-Zhang). Nobody has touched (c) the higher-codim correspondence positivity on a product, which is
the only thing equivalent to RH.

---

## 5. Discrepancy log (where this deepening disagrees with or sharpens the existing analyses)

A SURVEYOR reports; does not resolve. Flagging for ADVERSARY / VERIFIER / the morning review:

1. **No disagreement on the Connes-Consani 2026 cell.** The survey's reading (realization structure, positivity deferred)
   is confirmed verbatim by the abstract. **Refinement, not discrepancy:** the object is a Picard *monoid* and the paper
   explicitly *names the Jacobian* of $\overline{\mathrm{Spec}\,\mathbb{Z}}$, which is a sharper statement than the
   scorecard's "Picard/realization structure." The scorecard's parenthetical "($\circ\!\to\!\checkmark$)" on ingredient
   (i) is justified.

2. **Sharpening of the Gillet-Soule cell, possible terminology drift to flag.** The survey and 08A both say "the
   arithmetic standard conjectures are themselves open." This is TRUE but should be stated more precisely to avoid
   overclaiming the gap's openness: **the codimension-1 arithmetic Hodge index is a THEOREM (Moriwaki 1996, all relative
   dimensions; Faltings-Hriljac for $n=1$), not a conjecture.** Only codim $\ge2$ is open. The scorecard's "$(iii)\circ$
   inherits single-surface" already encodes this, but any prose that says "the arithmetic Hodge index is conjectural"
   without the codim qualifier is imprecise. **Recommended correction for the morning:** in
   `spec_z_cohomology_landscape.md` section 8 ("CONJECTURAL: ... The arithmetic standard conjectures ... are themselves
   open"), append "(codimension $\ge2$; the codimension-1 case is Moriwaki's theorem)."

3. **Possible over-attribution to Yuan-Zhang in the survey.** The survey section 7 says Yuan-Zhang "extended the
   arithmetic Hodge index to adelic line bundles in higher dimension, still on a fixed scheme, never on the product." This
   is **correct** but the phrase "higher dimension" could be misread as "higher codimension." This deepening pins it:
   the higher dimension is the *ambient variety's* dimension; the *cycle codimension is still 1* (Yuan-Zhang's own word,
   PDF p.2). **Recommended clarification:** "higher-dimensional ambient variety, but still codimension-1 cycles." This
   matters because the RH-relevant instance is higher *codimension*, which Yuan-Zhang does NOT address.

4. **A precise correspondence to record (not a discrepancy).** 08A M4 is named "the arithmetic Hodge standard
   conjecture" and equated with "arithmetic Rosati positivity." This deepening confirms the identification is exact and
   supplies the formula: 08A M4 $=$ Takeda/Gillet-Soule $\mathbf{AH_p}$, $(-1)^p\widehat{\deg}(L^{n+1-2p}(x)\cdot x)>0$,
   for $p\ge2$ on $\mathrm{Spec}(\mathbb{Z})^{\times2}$. The Rosati form (08A section 1) and the cup-with-$c_1(H)$
   intersection form ($\mathbf{AH_p}$) are the two faces of the same positivity (08A already states the sign-flip
   $\mathrm{NS}(C\times C)$ intersection $= -$Rosati). **No discrepancy; this is the literature confirming 08A's framing.**

5. **No K2 movement.** None of the three cells provides any new K2 (Davenport-Heilbronn) discrimination. Connes-Consani's
   monoid is built on the adele class space which still presupposes the multiplicative/Euler structure D-H lacks (K2 holds
   on the Frobenius side as before). Yuan-Zhang and Gillet-Soule are about arithmetic varieties with genuine geometry; D-H
   is not a variety, so they are vacuous for it (consistent with the scorecard's "vacuous" K2 marks for Faltings-Hriljac
   and Gillet-Soule). No discrepancy.

---

## 6. What this enables / what remains open

**Enables (for BUILDER):**
- A precise target name and formula for 08A M4: **prove $\mathbf{AH_p}$ (the Gillet-Soule arithmetic Hodge standard
  conjecture), $(-1)^p\widehat{\deg}(L_{H}^{n+1-2p}(x)\cdot x)>0$, for $p\ge2$, on a 2-dimensional-over-$\mathbb{Z}$
  object carrying the Frobenius correspondence $\Gamma_S$.** This is the most professional statement of the goal and
  places it inside an active literature (standard conjectures, Beilinson height positivity, Arakelov intersection theory).
- A concrete decomposition of the difficulty (Takeda): even granting Grothendieck's standard conjectures on the generic
  fiber, $\mathbf{AH_{p\ge2}}$ reduces to **Beilinson's height-pairing positivity on homologically-trivial primitive
  cycles** plus a vertical-cycle conjecture. BUILDER could probe whether the Frobenius-correspondence positivity the
  project wants is a *special case* of Beilinson's height positivity on $\mathrm{Spec}(\mathbb{Z})^{\times2}$. (Lead, not
  a result.)
- The Yuan-Zhang adelic technology (limits of integral models, Berkovich at all places, $\overline{L}$-boundedness) is
  the most complete codim-1 all-places infrastructure; if a product surface is ever constructed, this is the metric
  framework its codim-1 sub-pairings would use. The Connes-Consani Picard monoid is the first object naming the
  "Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$" -- a BUILDER lead for an arithmetic Rosati involution (08A M2),
  with the R3.5 circularity caveat.

**Remains open (the universal gap, now triply precise):**
1. The **product object** $\mathrm{Spec}(\mathbb{Z})\times_{\mathbb{F}_1}\mathrm{Spec}(\mathbb{Z})$ with an arithmetic
   intersection theory (none of Lorscheid / Borger / C-C-monoid has one yet).
2. The **Frobenius cycle class** $\Gamma_S$ on it, with the $(1,p)$ bidegree (#25) and the von Mangoldt
   self-intersection (#26).
3. The **higher-codimension ($p\ge2$) arithmetic Hodge standard conjecture** $\mathbf{AH_p}$ for that class -- the
   genuinely open mathematics (Yuan-Zhang: "wide open"), even on objects that DO exist; doubly hard here because the
   object does not exist.

The three 2017-2026 advances surveyed all live on the *realization* side or the *proven codim-1* side. The
higher-codimension correspondence positivity on a product -- the only thing equivalent to RH -- has not moved.

---

## 7. References (verified against originals where read; arXiv IDs/venues confirmed)

Primary, read at theorem-statement level this session:
- **Connes, A.; Consani, C.** *On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$.* arXiv:2602.15941 (submitted 17
  Feb 2026). Abstract read verbatim. [VERIFIED arXiv ID and date.]
- **Yuan, X.; Zhang, S.-W.** *The arithmetic Hodge index theorem for adelic line bundles I: number fields.*
  arXiv:1304.3538 (v1 12 Apr 2013; the read PDF is dated 2 Nov 2018). Published (with part II, arXiv:1304.3539) in
  *Mathematische Annalen* 367 (2017), no. 3-4, 1123-1171 (DOI 10.1007/s00208-016-1414-1). Theorems 1.1 and 1.3 and the
  signature statement read from the PDF. [VERIFIED arXiv IDs; venue Math. Ann. confirmed via Springer.]
- **Takeda, Y.** *A relation between standard conjectures and their arithmetic analogues.* arXiv:alg-geom/9608003 (2 Aug
  1996). MSC 14G40. Conjectures 1.1, 1.2 (the Gillet-Soule arithmetic standard conjectures, $\mathbf{AA_p}$ /
  $\mathbf{AH_p}$), 2.1, 2.2 read verbatim from the PDF. [VERIFIED arXiv ID.]

Cited via the above (statement-level, not independently re-read this session):
- **Gillet, H.; Soule, C.** *Arithmetic analogs of the standard conjectures.* In *Motives* (Seattle, WA 1991), Proc.
  Sympos. Pure Math. 55, Part 1, AMS 1994, pp. 129-140. MR1265527. (The source of $\mathbf{AA_p}$/$\mathbf{AH_p}$;
  transcribed by Takeda.) [Venue confirmed via AMS PSPUM 55.1 listing and a publication-list cross-check.]
- **Moriwaki, A.** *Hodge index theorem for arithmetic cycles of codimension one.* arXiv:alg-geom/9403011. Abstract read
  verbatim ("a partial answer for arithmetic analogues of Grothendieck's standard conjectures due to H. Gillet and C.
  Soule"); the codim-1 result $\mathbf{H_1}$ attributed in Takeda p.2 and Yuan-Zhang p.2. [VERIFIED arXiv ID.]
- **Faltings, G.** *Calculus on arithmetic surfaces.* Ann. of Math. 119 (1984). **Hriljac, P.** *Heights and Arakelov's
  intersection theory.* Amer. J. Math. 107 (1985). (Codim-1, $n=1$; the "too local" bracket, reproduced by the project
  at 2H-2P.) [Standard; not re-read this session.]
- **Grothendieck, A.** *Standard conjectures on algebraic cycles.* (1969). (The geometric $\mathbf{H_p}$; theorem in
  char 0 via Hodge-Riemann.) [Cited via Takeda Conj 1.1.]
- **Kunnemann, K.** (1995/96) Arakelov-Chow reduction + projective spaces / quadrics. [Cited via Takeda p.4.]
- **Connes, A.** *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function.* Selecta Math.
  (1999). (The spectral realization the 2026 monoid's singular strata serve.) [Cited; in the project library.]

Project internal cross-references:
- [`docs/03_research/spec_z_cohomology_landscape.md`](../../../docs/03_research/spec_z_cohomology_landscape.md) (the
  15-candidate scorecard; the cells deepened here are rows 4, 9, 10 and section 7).
- [`docs/03_research/research_directions/08A_rosati_standard_conjecture.md`](../../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md)
  (M1-M5; M4 = the arithmetic Hodge standard conjecture, now pinned to $\mathbf{AH_{p\ge2}}$).
- [`experiments/LEARNINGS.md`](../../../experiments/LEARNINGS.md) #25/#26 ($\Gamma_S$ bidegree, von Mangoldt
  self-intersection), #34 ($A_{\mathrm{arch}}$), #40-#44 (the q-lift / Id_eps / de Branges / Sen coordinates).
- [`experiments/arithmetic_geometric/e2cc3_q_lift_attempt.md`](../../../experiments/arithmetic_geometric/e2cc3_q_lift_attempt.md),
  [`2J_arakelov_adjunction.md`](../../../experiments/arithmetic_geometric/2J_arakelov_adjunction.md).

---

## 8. Honest caveats on this deepening (partial expertise, what was and was not read)

- **Read this session at theorem-statement level:** the Connes-Consani 2026 abstract (verbatim), Yuan-Zhang I Thms 1.1
  and 1.3 + the signature paragraph (from the PDF, pp.3-4), Takeda's transcription of the Gillet-Soule conjectures
  (Conj 1.1, 1.2, 2.1, 2.2, from the PDF, pp.1-5), the Moriwaki abstract (verbatim).
- **NOT read this session (cited via the above, flagged):** the body/proofs of any of these papers; the original
  Gillet-Soule 1994 Motives article (transcribed only via Takeda); the Yuan-Zhang part II (arXiv:1304.3539);
  Kunnemann's papers; the Connes-Consani 2026 body beyond the abstract. The claim "Yuan-Zhang is codimension-1" rests
  on the authors' own introduction sentence ("still codimension one cycles"), which is decisive and direct; the claim
  "$\mathbf{AH_{p\ge2}}$ is wide open" rests on Yuan-Zhang's introduction ("wide open") and Takeda's reduction. These are
  strong primary-source statements but the morning review should still re-open the PDFs to confirm the quotes.
- **The identification "08A M4 = $\mathbf{AH_{p\ge2}}$ on the product with $\Gamma_S$" is a STRUCTURAL-READING**, built
  on the proven fact that $\mathbf{AH_p}$ is the standard name for arithmetic Rosati positivity (08A already asserts this)
  and on the project's own #25/#26 identification of $\Gamma_S$'s bidegree and self-intersection. It is a precise
  *restatement* of the gap in professional vocabulary, not a new theorem and not a step toward closing it. The codimension
  bookkeeping ("the RH-relevant primitive part is codim $\ge2$") is a structural reading of how Weil's correspondence
  positivity sits in the arithmetic Chow grading; an ADVERSARY should check whether the relevant primitive class on the
  (hypothetical) arithmetic surface is genuinely codim $\ge2$ or whether a codim-1 reformulation exists that would put it
  in Moriwaki's proven range. (If it did, that would be a major lead; the project's prior reading and the function-field
  analogy both say it is the higher-codim / correspondence-algebra positivity, i.e. genuinely open.)
- No numerics were produced in this stream; nothing here is COMPUTED. All tags are CITED or STRUCTURAL-READING.
