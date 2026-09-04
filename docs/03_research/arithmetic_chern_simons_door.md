# The arithmetic Chern-Simons door: measured at its linking layer

**Status:** survey + probe, 2026-08-19. The #176 handed-forward question, executed.
**Probe:** [`experiments/arithmetic_geometric/e2am_arithmetic_chern_simons.py`](../../experiments/arithmetic_geometric/e2am_arithmetic_chern_simons.py) (20/20).
**Papers:** 9 arXiv texts in `references/05_arithmetic_topology/` + the two ACS papers in `references/09_quantum_gravity/` (gitignored per tier; index in [`references/README.md`](../../references/README.md) section 05).
**Parent:** [`local_quantum_gravity_and_primes.md`](local_quantum_gravity_and_primes.md) section 3.4 and section 7, [LEARNINGS #176-#177](../../experiments/LEARNINGS.md).

The question this door was opened on (#176, section 7): the arithmetic Chern-Simons
carrier has the right *shape* for Direction 8 (a 3-manifold-like object with a TQFT,
hence a natural pairing on a middle cohomology). Can its linking form be made
**indefinite with a sign**, i.e. can this carrier host M4's polarization?

The answer, measured rather than argued: **the question dissolves at this layer.**
The linking layer is torsion-valued, so "indefinite" is a type error for it. What a
torsion linking form knows about *any* real symmetric form bounding it is exactly the
signature **mod 8** (Gauss-Milgram), and in arithmetic that mod-8 shadow is Gauss-sum
phase = root-number = functional-equation-side data, which [#176](local_quantum_gravity_and_primes.md)
proved is the RH-blind half. The sign M4 needs is an exact integer, it lives one
dimension up in a bounding object with a real-valued intersection form, and *that
object is the missing carrier itself* (SP1). The tariff is paid at the carrier joint,
where the conservation law ([`trojan_horse_m4.md`](trojan_horse_m4.md)) said it must be.

The positive product is that the dictionary below the question is **real arithmetic,
not analogy**, and the probe measures it: the mod-2 linking form of the arithmetic
3-manifold (the Rédei matrix) *computes the 4-rank of the class group*, verified
across every fundamental discriminant $-5000 < D < 0$ against an independent
genus-theory computation.

---

## 1. What arithmetic Chern-Simons is

Kim's construction (arXiv:1510.05818, "for simplicity of exposition" over totally
imaginary $F$ with $\mu_n \subset F$; Lee-Park 1905.13610 lift the imaginary
restriction via compactly-supported cohomology). $X = \operatorname{Spec}(\mathcal{O}_F)$,
$\pi = \pi_1^{\text{ét}}(X)$ the unramified Galois group, $A$ a finite gauge group,
$c \in H^3(A, \mathbb{Z}/n)$ a 3-cocycle. The Chern-Simons functional is

$$CS_c : \mathcal{M}(A) \to \tfrac1n\mathbb{Z}/\mathbb{Z}, \qquad [\rho] \mapsto \mathrm{inv}(\rho^*(c)),$$

where $\mathcal{M}(A) = \mathrm{Hom}_{\text{cont}}(\pi, A)/A$ is the space of Galois
representations and $\mathrm{inv}$ is the fundamental-class isomorphism
$H^3(X, \mathbb{Z}/n) \simeq \tfrac1n\mathbb{Z}/\mathbb{Z}$ supplied by Artin-Verdier
duality ($\mathrm{inv}: H^3(X, \mathbb{G}_m) \simeq \mathbb{Q}/\mathbb{Z}$,
"reminiscent of the fundamental class of a compact oriented three manifold... noted
by Mazur around 50 years ago"). This is the exact sense in which
$\operatorname{Spec}(\mathcal{O}_F)$ is a 3-manifold and the theory is a
Dijkgraaf-Witten TQFT on it: the DW partition function (Hirano-Kim-Morishita
2106.02308) is the finite path integral
$Z(X) = \frac{1}{\#G}\sum_{\rho} \zeta_N^{\,CS(\rho)}$.

The decomposition formula (ACS II Thm 1.1; Lee-Park Thm 3.1) writes
$CS_c([\rho]) = \sum_{v \in S}(\beta_v) - CS_c([\rho \circ \kappa_S])$, a sum of
local boundary-torus terms over a **finite set of primes** $S$, never over all
places. Where the real places went is section 3.

## 2. The corpus, paper by paper

Nine papers read (full list section 7; per-paper roles in
[`references/README.md`](../../references/README.md) section 05). The theorems that
exist, versus the program:

- **ACS I (1510.05818):** the construction; no arithmetic theorem in the body.
  Kim's own abstract calls the idea of using CS theory to construct L-functions
  "far-fetched". One non-torsion object appears: the inverse limit
  $\mathrm{inv}: H^3(X, \mathbb{Z}_p(1)) \simeq \mathbb{Z}_p$, which is $p$-adic
  (see section 3, it matters).
- **ACS II (1609.03012):** the decomposition formula; explicit $CS_c$ values from
  prime-splitting counts (Thms 5.8/5.13); non-existence results for Galois
  embedding problems (Props 6.2/6.4). "Signature" occurs only as a
  $\mathbb{Z}/2$ sign character.
- **Abelian ACS + linking (1706.03336):** defines
  $\mathrm{lk}_n(P,Q) := \langle d^{-1}[P],[Q]\rangle$ via
  $H^1(X,\mathbb{Z}/n) \times \mathrm{Ext}^2(\mathbb{Z}/n,\mathbb{G}_m) \to \tfrac1n\mathbb{Z}/\mathbb{Z}$
  with $\mathrm{Ext}^2 \simeq \mathrm{Cl}(X)/n$ (Artin-Verdier), for
  $n$-homologically-trivial primes; proves the pairing symmetric (Lemma 2.2); main
  theorem is "a precise analogue of the Gaussian path integral": the partition sum
  equals $p^{(a+b)/2}$ times an exponential in pairwise linking numbers. **No
  numeric examples anywhere in the paper** (confirmed by exhaustive search); the
  probe's T2 supplies the adjacent computable layer.
- **Real places (1905.13610):** the archimedean place enters as Tate cohomology of
  $\mathrm{Gal}(\mathbb{C}/\mathbb{R}) \cong \mathbb{Z}/2$ (not an orbifold; the
  word never occurs). Thm 4.22: infinitely many totally imaginary $F$ with
  $CS_c \neq 0$.
- **Arithmetic DW (2106.02308):** TQFT axioms, gluing; $Z$ trivially counts
  homomorphisms; calls its invariants "variants of (non-abelian) Gaussian sums"
  informally, but actual Gauss sums never appear.
- **Mod-2 DW, real quadratic (1911.12964):** the corpus's computed examples. For
  $K = \mathbb{Q}(\sqrt{p_1\cdots p_r})$, $p_i \equiv 1 \bmod 4$:
  $(-1)^{CS_c(\rho)} = \prod_{i<j,\ \rho(e_{ij})=-1} (p_j|p_i)$, pure
  Legendre-symbol (= linking-matrix) data; e.g. $Z_c = 0$ for
  $\mathbb{Q}(\sqrt{5\cdot29\cdot37})$ vs $Z_c = 4$ for
  $\mathbb{Q}(\sqrt{5\cdot13\cdot73})$. A genuine mod-2 reciprocity law (Thm 4.2.2).
  **The corpus's own computable content at this layer is the linking matrix**, the
  same object the probe measures.
- **Entanglement entropies (2312.17138):** the one real-valued export; section 5.
- **Pro-p duality (2504.19078, the 2025 state):** relative Poincare duality for
  pro-p group pairs as a cobordism category; everything actually classified is
  $(1{+}1)$-dimensional ("(1+1) pro-p TQFTs at p... in bijective correspondence
  with... Aut(Zp)-extended R-Frobenius algebras"); dimension 3 aspirational; the
  one arithmetic payoff re-derives Yamagishi's 1995 counting formula, self-flagged
  as not new.
- **Program manifesto (1712.07602):** self-assessment quoted for the record: "the
  arithmetic E-L equations obtained thus far have not been entirely canonical...
  an Euler-Lagrange equation without an action"; "the reader should beware the
  lack of rigorous foundations at the moment".

## 3. The screens: value groups, L-functions, real places

Run against all nine papers (exhaustive keyword search plus close read):

**Value groups.** Every constructed invariant lands in $\tfrac1n\mathbb{Z}/\mathbb{Z}$,
$\mathbb{Q}/\mathbb{Z}$, $\mathbb{Z}/N$, or (one case, ACS I's inverse limit over
$n = p^i$) $\mathbb{Z}_p$. No real-valued invariant is constructed anywhere; "eta"
and "definite" have zero hits corpus-wide; "signature" occurs once, meaning a
$\mathbb{Z}/2$ character. The sharpest way to say what this means: **the two
completions the theory's value group reaches, $\mathbb{Q}/\mathbb{Z}$ and
$\mathbb{Z}_p$, are both unorderable fields/groups; the unique orderable completion
of $\mathbb{Q}$ is $\mathbb{R}$, the archimedean one; and the archimedean place is
precisely what the corpus itself identifies as the obstruction** (next paragraph).
A signature is an order-theoretic quantity. The value group avoids the archimedean
completion for the same structural reason the base does.

**Real places.** Lee-Park, causally: "Because $H^3(\pi_T,\mathbb{Z}/n) \neq 0$ when
$X_\infty$ is not empty (i.e. there is a real place in $F$), the arithmetic CS
action with boundary does not seem to extend": a real place is what obstructs a
closed invariant, and it is patched in via Tate cohomology of
$\mathrm{Gal}(\mathbb{C}/\mathbb{R}) \cong \mathbb{Z}/2$, contributing individually
vanishing summands to the decomposition. The repo's "archimedean place is the hard
joint" holds in this corpus at the level of the action itself.

**L-functions.** Zero appearances as input or output of any computed invariant, in
any of the nine papers; zero hits corpus-wide for "Riemann hypothesis",
"Hilbert-Polya", "spectral interpretation". The connection is invoked only as
motivation, and the corpus's own words grade it: "far-fetched" (ACS I abstract),
"in a way that remains mysterious" (1712.07602). This is what "mechanism 2 eats
neither half" looks like from inside the corpus.

---

## 4. What got measured (the probe, 20/20)

[`e2am_arithmetic_chern_simons.py`](../../experiments/arithmetic_geometric/e2am_arithmetic_chern_simons.py),
pure Python + sympy/numpy, no external data.

### 4.1 The linking dictionary is exact, and its symmetry defect is the real place

For odd primes, $\mathrm{lk}_2(q,p)$ is defined by $(q|p) = (-1)^{\mathrm{lk}}$. Over
all 990 pairs of odd primes below 200:

- the symmetry defect $\mathrm{lk}(p,q) \oplus \mathrm{lk}(q,p)$ equals
  $[p \equiv 3][q \equiv 3] \bmod 4$ **pair for pair** (this is quadratic reciprocity,
  read as a statement about where linking symmetry fails), and
- the defect count is exactly $\binom{n_3}{2}$ (276 of 990; both counts measured).

Reading: linking of knots in an oriented 3-manifold is symmetric. The arithmetic
linking of two primes is symmetric *exactly when at least one of them is split in*
$\mathbb{Q}(i)$, i.e. trivial around the real place. The entire failure of symmetry
is an archimedean term. This is the repo's "the archimedean place is the hard joint"
appearing already at the mod-2 boundary layer, and it propagates: since
$K(p^*, r) = (r|p)$ (verified in T0 including at $r = 2$), the Rédei matrix entries
are $R_{ij} = \mathrm{bit}((p_j|p_i))$, so the **asymmetry of the class-group linking
form is the same real-place defect**, inherited entry by entry.

No conflict with 1706.03336's Lemma 2.2 (the pairing there is proved symmetric):
that pairing is defined only on $n$-homologically-trivial primes, the arithmetic
analogue of null-homologous knots, where linking is symmetric in topology too. The
probe measures arbitrary pairs and finds the failure localized at the real place;
the corpus works where the failure vanishes. The two statements compose: symmetry
holds exactly on the locus where the archimedean term is trivial.

### 4.2 The linking form computes the class group (Rédei 1934, verified)

For a fundamental discriminant $D < 0$ with $t$ prime-discriminant factors
$D = d_1 \cdots d_t$, the **Rédei matrix** $R \in M_t(\mathbb{F}_2)$ is built from
linking data only: $R_{ij} = \mathrm{bit}\,K(d_i, p_j)$ for $i \neq j$, diagonal
$R_{ii} = \mathrm{bit}\,K(D/d_i, p_i)$ (column sums then vanish, checked at every $D$).
Rédei's theorem: the 4-rank of the class group is $e_4 = t - 1 - \mathrm{rank}_{\mathbb{F}_2} R$.

The probe verifies this across **all 1524 fundamental discriminants in $(-5000, 0)$**
against a computation sharing no code and no objects with the linking side:

- $h(D)$ by direct enumeration of reduced binary quadratic forms agrees with
  Dirichlet's exact finite-sum class number formula at every $|D| \le 1200$ (364 cases);
- the number of ambiguous reduced forms is $2^{t-1}$ at every $D$ (Gauss: 2-rank $= t-1$);
- $e_4$ computed by **genus characters on the ambiguous forms** (principal genus =
  squares, with each character the one-liner $\chi_{d_i}(f) = K(d_i, r)$ on a
  represented value) equals $t - 1 - \mathrm{rank}(R)$ at **every one of the 1524**
  discriminants. Histogram: $e_4 = 0$: 972, $e_4 = 1$: 550, $e_4 = 2$: 2.

The two $e_4 = 2$ cases are worth naming: $D = -2379 = (-3)(13)(61)$ and
$D = -4895 = (5)(-11)(89)$, both with **Rédei rank 0**: all pairwise linkings vanish.
These are precisely the "pairwise unlinked" configurations where the next invariant
is the **Rédei triple symbol** = the arithmetic Milnor triple linking number
(Morishita), i.e. the arithmetic Borromean configuration. The 2024 density result for
Borromean primes (Ishida-Kuramoto-Zheng, arXiv:2403.17957) lives exactly here.

A worked example for the record: $D = -260 = (-4)(5)(13)$, $t = 3$, $h = 8$,
Rédei matrix rows $\{(1,1,1), (1,1,1), (0,0,0)\}$, rank 1, so $e_4 = 3 - 1 - 1 = 1$;
the genus side finds ambiguous forms $(1,0,65), (2,2,33), (5,0,13), (9,8,9)$ of which
exactly $(1,0,65)$ and $(9,8,9)$ lie in the principal genus: $2^{e_4} = 2$. Both
routes: $\mathrm{Cl}(-260) \cong \mathbb{Z}/4 \times \mathbb{Z}/2$.

This is the strongest checkable content of "primes link like knots": the linking
form is not a metaphor, it is an exact instrument for a nontrivial arithmetic
invariant, verified 1524 for 1524.

### 4.3 Gauss-Milgram: what the boundary knows of the bulk

The classical fact that decides the M4 question. For an even lattice $L$ with
discriminant form $q$ on $G = L^*/L$, Milgram's formula:

$$\sum_{x \in G} e^{\pi i q(x)} = \sqrt{|G|}\; e^{2\pi i\, \sigma(L)/8}.$$

The boundary (torsion) data $q$ determines the bulk signature **mod 8 and nothing more**.
Measured:

- Milgram verified on the catalog $A_1, U, D_4, E_8, A_1{+}E_8$, with each
  discriminant form computed exactly (rational arithmetic) from the Gram matrix.
- **The cap, pair 1:** $U$ (hyperbolic, indefinite, $\sigma = 0$) and $E_8$ (definite,
  $\sigma = 8$) have *identical* (trivial) discriminant forms. The boundary cannot
  even see definite vs indefinite, which is the exact distinction M4's polarization
  is made of.
- **The cap, pair 2:** $A_1$ and $A_1 \oplus E_8$ have identical *nontrivial*
  discriminant forms and signatures 1 vs 9.
- **The mod-8 datum is root-number data:** the quadratic Gauss phases
  $g(1,p) = p^{-1/2}\sum_x e(x^2/p)$ are 1 or $i$ by $p \bmod 4$ (Gauss's sign
  theorem, verified to $10^{-9}$ for all $p < 200$), equal the normalized Gauss sum
  of $\chi_{p^*}$, i.e. the **local root number** (verified), and their CRT cocycle
  is the reciprocity sign (verified). Landsberg-Schaar reciprocity holds on the full
  $12 \times 12$ grid to $2.5 \times 10^{-13}$ (the metaplectic/Weil-index face;
  cross-ref [`e1i_metaplectic_weil_index`](../../experiments/spectral/e1i_metaplectic_weil_index.py)).

So arithmetic's version of "the signature mod 8 that a torsion boundary can carry"
is *already occupied*, and it is occupied by the $\varepsilon$-factors: the local
constants whose product is the sign of the functional equation. That is the half of
the adelic package that Davenport-Heilbronn also possesses, the half #176 proved
carries zero bits about zero location.

### 4.4 The disciplines cannot even be posed

No L-function is consumed anywhere in the probe: the inputs are primes, discriminants
and lattices. D-H and Beurling are **unposable** at this layer, a type refusal in the
sense of e1t's Euler gate, and this is the precise content of "mechanism 2 eats
neither half" in the #176 five-mechanism table.

---

## 5. The verdict

**The handed-forward question dissolves.** "Can the arithmetic linking form be made
indefinite with a sign" presupposes a real-valued form; the linking layer is torsion
($\mathbb{Z}/2$ here, $\mathbb{Z}/n$ for the CS functional, $\mathbb{Q}/\mathbb{Z}$
in the Artin-Verdier limit), and the corpus's one non-torsion completion is
$\mathbb{Z}_p$, which like $\mathbb{Q}/\mathbb{Z}$ admits no order: a signature is
an order-theoretic quantity, the unique orderable completion of $\mathbb{Q}$ is the
archimedean one, and the archimedean place is exactly what the corpus identifies as
the obstruction to a closed action (section 3). The correct completion of the
question, and its answer:

1. **What signature content does the layer carry?** Exactly $\sigma \bmod 8$
   (Gauss-Milgram, measured on the catalog), realized arithmetically as Gauss-sum
   phases = root numbers = FE-side data. By #176's unitarity kill, that content is
   RH-blind.
2. **Can the layer be lifted to a real-valued form?** Only by choosing a bounding
   object: a "4-dimensional" bulk whose intersection form reduces to the linking
   form on the boundary. The lift is wildly non-unique ($U$ vs $E_8$: same boundary
   data, different definiteness, signatures 8 apart), so the sign is **not a
   boundary observable at all**. Choosing the bounding object with the right
   positivity *is* supplying M4's carrier (SP1) with its polarization (SP5), i.e.
   the lift is not a route to the missing object, it is the missing object.
3. **Conservation law check** ([`trojan_horse_m4.md`](trojan_horse_m4.md)): the
   tariff is paid at the **carrier joint**. Arithmetic CS consumes the étale
   fundamental group of $\mathrm{Spec}(\mathcal{O}_K)$ (pre-zeta structure) and
   neither the Euler product nor the additive lattice ever enters; accordingly no
   L-function appears in the corpus as input or output, and the disciplines are
   unposable rather than passed. The door does not smuggle the sign; it relocates
   the wall, which is what every measured costume has done (#160, #171, #172).

**A new named coordinate for the wall:** *the sign lives in the bulk.* Any
boundary/torsion route (linking forms, class-group pairings, CS functionals valued
in finite groups, root numbers) determines a signature at most mod 8; M4 needs the
exact integer. This is a reusable disqualifier for the breadth battery
([`breadth_program.md`](breadth_program.md)): a candidate whose value group is
torsion, or whose real-valued exports are entropic (nonnegative by construction),
caps at $\sigma \bmod 8$ and cannot carry the polarization. Proposed here
2026-08-19; BANKED 2026-09-04 as screen 14 (the `export_type` dimension of
`breadth_corpus.py`, suite 26/26; LEARNINGS #218) after the density-matrix costume
measured the entropic half on the controls
([`e3ac_entropic_exports.md`](../../experiments/positivity/e3ac_entropic_exports.md)).

**The entanglement caveat, stated honestly.** The corpus's one real-valued export
(Chung-Kim-Kim-Park-Yoo 2023, arXiv:2312.17138) is the von Neumann entanglement
entropy of the arithmetic CS state for gauge group $\mathbb{Z}/p$:

$$\mathrm{Ent}(Z_{X_{S_1},S_2}) = \big(\dim \mathcal{F}_{X_S} - \dim(\mathrm{Ker\,loc}_{S_1} + \mathrm{Ker\,loc}_{S_2})\big)\,\log p,$$

a nonnegative integer multiple of $\log p$ built from ranks of Poitou-Tate
localization maps. Real-valued, yes; but entropic, hence nonnegative by construction,
hence structurally incapable of the indefinite signature, the exact twin of the
Bost-Connes kill (the strictly positive modular operator,
[`building_the_missing_positivity.md`](building_the_missing_positivity.md) Mechanism 2).
The authors' own framing: "It should be admitted that the results of this paper do
not yet make clear that the notion of entanglement is useful for number theory."
Their named future direction, "path integrals of L-function type", is the point at
which this program would first touch the objects this repo cares about, and the
place to re-check.

**Signature defects, the adjacent proven bridge, and why it does not help.** In
topology the lift from linking to signature is governed by eta invariants
(Atiyah-Patodi-Singer), and the one *proven* arithmetic instance is
Atiyah-Donnelly-Singer 1983: the Hirzebruch signature defect of a Hilbert modular
cusp equals a special value of a Shimizu L-function. Native output: an L-*value*
identity. By the #113 discriminator (any route whose native output is a central
L-value/L-derivative is BSD/Gross-Zagier regime, not RH), this lands in the
special-value regime, not the all-zeros-positivity regime. An "arithmetic eta
invariant" for $\mathrm{Spec}(\mathcal{O}_K)$ itself (spectral asymmetry of a
self-adjoint operator, varying locally, with the zeros in its spectrum) does not
exist in the literature searched; constructing one would be Deninger-adjacent and
is the only shape of reopening this door that would carry sign data (see section 6).

---

## 6. What would reopen the door

Three specific triggers, in decreasing order of force:

1. **A real-valued, sign-carrying lift with a canonical bounding object.** Any
   arithmetic construction that picks out, functorially, a "4-dimensional bulk" for
   $\mathrm{Spec}(\mathcal{O}_K)$ with a real-valued intersection form reducing to
   the Artin-Verdier linking form on the boundary. This is M4-hard by section 5.2,
   so a claim of it should be treated as a claim of the missing object.
2. **An arithmetic eta invariant.** A self-adjoint operator attached to
   $\mathrm{Spec}(\mathbb{Z})$ whose spectral asymmetry is defined, real-valued, and
   computes CS phases; the APS variation formula would then be a local sign law.
   Nothing in the searched literature constructs one.
   **DISCHARGED 2026-08-19** ([`arithmetic_eta.md`](arithmetic_eta.md) +
   [`e1ac`](../../experiments/spectral/e1ac_arithmetic_eta.py), 18/18, LEARNINGS #178):
   the invariant EXISTS for the abelian flat connections (complex Dirichlet
   characters), $\eta(\chi) = -(2/\pi)\arg_c L(1/2,\chi)$, mod-2 shadow = the
   root-number phase (this dossier's layer), variation prime-local with zero
   archimedean term. And it is EXACTLY RH-blind: the invariant never references
   $\beta$, and the D-H off-line quadruple cancels identically in every odd test
   function. The odd sector is exactly solvable and exactly RH-blind; RH is
   even-sector. Built, measured, typed: not the missing object.
3. **The ACS program reaching L-functions.** The corpus's own named next steps
   (path integrals of L-function type, entanglement for BF theories and general
   gauge groups). If a *positivity* statement, not a special-value identity, ever
   appears there, it re-enters this repo's M4 screens and should be run through the
   disciplines then.

---

## 7. Sources

Filed in `references/05_arithmetic_topology/` (plus the two ACS papers in
`references/09_quantum_gravity/`); tracked index in
[`references/README.md`](../../references/README.md) section 05. Full list: Kim
arXiv:1510.05818 (ACS I); Chung-Kim-Kim-Park-Pappas-Yoo arXiv:1609.03012 (ACS II);
arXiv:1706.03336 (abelian ACS and arithmetic linking numbers); Lee-Park
arXiv:1905.13610 (real places); Hirano-Kim-Morishita arXiv:2106.02308 (arithmetic
DW); Hirano arXiv:1911.12964 (mod 2 DW, real quadratic); Chung-Kim-Kim-Park-Yoo
arXiv:2312.17138 (entanglement entropies); Ben-Bassat - Gropper arXiv:2504.19078
(pro-p duality, 2025); Kim arXiv:1712.07602 (arithmetic gauge theory intro).
Adjacent: Ishida-Kuramoto-Zheng arXiv:2403.17957 (density of Borromean primes);
Atiyah-Donnelly-Singer 1983 (signature defect = Shimizu L-value).
