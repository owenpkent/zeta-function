# Parity versus polarization: is the sieve parity barrier the M4 wall in another language?

> A SURVEYOR frame-audit dossier (2026-07-01), angle B of the two-dossier regime-two probe flagged as the
> breadth program's unspent axis ([`breadth_program.md`](breadth_program.md) Pillar 5 / LEARNINGS #133's
> frame-audit residue). Question audited: is sieve theory's **parity barrier** (Selberg 1949) the same
> obstruction as the project's **M4 polarization gap**, expressed in a different language? Hypothesis as
> posed: both say that beyond density information, the missing resource is a two-variable pairing exhibiting
> square-root cancellation.
>
> Reading depth, stated honestly: Sawin-Shusterman arXiv:1808.04001v2 read (introduction + keyword-verified
> body); Friedlander-Iwaniec and Bombieri verified through abstracts, Tao's expository notes, and secondary
> sources; Zhang's Type I/II/III structure verified through the Polymath record and Kowalski's notes. No
> full proof of any cited paper was checked line-by-line. Claims below are flagged where depth is survey-only.

## 1. The parity barrier, precisely

**Selberg 1949.** Selberg (*On elementary methods in prime-number theory and their limitations*, Proc. 11th
Scand. Congress, Trondheim 1949) observed that the axioms a sieve consumes (congruence-density data: for each
squarefree $d$, $|A_d| = g(d)X + r_d$ with $g$ multiplicative and $r_d$ small on average) are **invariant
under flipping the sign of the Liouville function**. His examples: the set of integers with an odd number of
prime factors and the set with an even number satisfy identical sieve axioms, yet one contains all the primes
and the other none. Consequence (the standard formulation, [Wikipedia: parity problem](https://en.wikipedia.org/wiki/Parity_problem_(sieve_theory)); Tao 2007 blog): on a set whose elements all have an odd (or all even)
number of prime factors, sieve theory alone gives **no nontrivial lower bound**, and its upper bounds are off
by a **factor of at least 2**.

**Bombieri 1976.** Bombieri (*The asymptotic sieve*, Mem. Accad. Naz. dei XL, 1976) made the phenomenon a
theorem-shaped statement. Even granting the **Elliott-Halberstam conjecture** (level of distribution $\theta = 1$,
read as every $\theta < 1$: the literal endpoint, moduli up to $x/(\log x)^A$, is **false** by
Friedlander-Granville 1989, so "level 1" always means $\theta = 1 - \epsilon$; still the strongest density
input conceivable. ADVERSARY caution added 2026-07-02), the asymptotic sieve delivers the expected asymptotics for the
generalized von Mangoldt functions $\Lambda_k$ for **every $k \ge 2$** (almost-primes), and fails exactly at
$k = 1$ (primes). Tao's exposition (*Notes on the Bombieri asymptotic sieve*, 2016) isolates the failure as a
single unknown scalar $\delta_x \in [0,2]$: primes require $\delta_x = 1 + o(1)$, and no density hypothesis
pins it. The two extreme values $\delta_x \in \{0, 2\}$ correspond to the two sign-flipped measures
$(1 \pm \lambda(n))\,dn$, which are indistinguishable by every sieve axiom.

**What the axioms see and cannot see.** Sieve axioms are **one-variable, positive-cone data**: densities of
$A$ along congruence classes, plus nonnegative weights (Brun's combinatorial weights; Selberg's $\Lambda^2$
weights, which are literally sums of squares). The invisible degree of freedom is the **sign** $\mu(n)$ /
$\lambda(n)$: a rank-one indefinite direction orthogonal to the entire positive cone. The parity barrier is
the statement that no amount of one-variable density information determines that sign.

## 2. The known parity-breakers and where their cancellation comes from

Every historical crossing of the barrier injects a **bilinear (two-variable) estimate** or automorphic input.
The ledger, with the ultimate source of the square-root cancellation in each:

| Breaker | Mechanism | Where the square-root cancellation comes from |
|---|---|---|
| Vinogradov 1937 (ternary Goldbach / three primes) | decompose $\Lambda$ into Type I (linear) + Type II (bilinear) sums; cancellation in $\sum_m \sum_n a_m b_n e(\alpha mn)$ | Cauchy-Schwarz on the bilinear structure itself (off-diagonal counting); no algebraic geometry needed at this depth |
| Vaughan 1977 / Heath-Brown 1982 identities | clean combinatorial decompositions of $\Lambda$, $\mu$ into Type I/II pieces | bookkeeping only; they expose where bilinear input is needed, they do not supply it |
| Linnik's dispersion method (1961 monograph) | second-moment (variance) treatment of remainders in a bilinear family | completed exponential sums over $\mathbb{F}_p$, i.e. the Weil bound |
| Bombieri-Vinogradov 1965 ("GRH on average", $\theta = 1/2$) | large sieve + bilinear decomposition of $\Lambda$ | the large-sieve duality (an $L^2$ almost-orthogonality); notably **zero** algebraic geometry and **zero** zero-location input in the modern proof |
| Deshouillers-Iwaniec 1982 (Kloostermania; Inventiones 70) | sums of Kloosterman sums via the Kuznetsov formula; spectral theory of $GL(2)$ Maass forms | two sources: the **Weil bound** $|S(a,b;p)| \le 2\sqrt p$ for completed Kloosterman sums (RH for the Artin-Schreier curve, Weil 1948), and the **spectral gap** for Maass forms (Selberg $3/16$, now Kim-Sarnak $7/64$) |
| Bombieri-Friedlander-Iwaniec 1986 (progressions beyond $\theta = 1/2$, fixed residue) | dispersion + Kloostermania | as above: Weil bound + spectral input |
| Friedlander-Iwaniec 1998 (*Asymptotic sieve for primes* + *The polynomial $X^2+Y^4$ captures its primes*, Ann. Math. 148) | the classical axioms **plus one new axiom**: a bilinear-form bound on the remainder with $\mu$-type coefficients, $\sum_m \big|\sum_{N<n\le 2N} \beta(n)\, a_{mn}\big|$ small, needed in a **narrow range of $N$ just below $\sqrt x$** (the range has the shape $\Delta^{-1}\sqrt{D} < N < \delta^{-1}\sqrt x$) | for $a^2 + b^4$: the arithmetic of $\mathbb{Z}[i]$ plus estimates on complete character/exponential sums over finite fields, i.e. Weil-strength input |
| Heath-Brown 2001 ($x^3 + 2y^3$, Acta Math. 186) | same sieve frame, bilinear axiom verified in $\mathbb{Z}[\theta]$ | Weil-strength complete-sum estimates (survey-depth claim) |
| Zhang 2013 (bounded gaps, Ann. Math. 179) | Type I/II via dispersion; **Type III requires the Birch-Bombieri bound** on a three-variable exponential sum | the Birch-Bombieri bound is a corollary of **Deligne's proof of RH over finite fields** (Weil II); the Type I/II ranges use the Weil bound for incomplete Kloosterman sums (verified via the Polymath8 record and Kowalski's 2013 notes) |
| Matomäki-Radziwill 2016 (Ann. Math. 183) + Tao 2016 (log-averaged 2-point Chowla) + Tao-Teräväinen (odd cases) | multiplicative-function averaging in short intervals; entropy decrement | **none**: the cancellation is qualitative ($o(1)$), not power-saving; no variety, no zeros. The one genuinely geometry-free tier of parity-breaking |

**The recursive irony, explicitly.** The deep Type II/III estimates (Deshouillers-Iwaniec, Friedlander-Iwaniec,
Zhang) bottom out in **completed exponential sums over finite fields bounded by Weil 1948 or Deligne 1974/1980**.
That is: parity over $\mathbb{Z}$ is broken, where it is broken with power savings, by importing the
function-field RH, which is precisely the polarization theorem (Castelnuovo-Severi / Hodge index on $C \times C$,
Weil's own route) that M4 is trying to transfer to $\mathrm{Spec}(\mathbb{Z})$. Sieve theory's parity-breaking
successes are **downstream consumers of the proven polarization**, applied fiberwise over the finite-field
fibers living inside an integer problem.

**How it is consumed (load-bearing detail; corrected by the 2026-07-02 ADVERSARY pass).** The import enters
only through **sign-free corollaries**, in two tiers. Tier 1 (moduli): $|S| \le 2\sqrt p$,
$|\alpha| \le q^{i/2}$, used termwise (Deshouillers-Iwaniec, Zhang's Type I/II completions, Birch-Bombieri
in Type III). Tier 2 (angle/monodromy statistics): weights in all cohomological degrees, monodromy-group
classifications, and their equidistribution corollaries (vertical Sato-Tate for Kloosterman angles, the
Fouvry-Kowalski-Michel trace-function machinery, Sawin-Shusterman's vanishing-cycles input). The original
phrasing here ("the import always enters as a modulus bound") was too narrow: tier-2 consumers exist inside
this ledger itself. What no tier ever consumes is the **signature** (S5) content of the underlying
polarization: which class pairs positively, the $(1, n-1)$ structure, the direction of the
Castelnuovo-Severi / Hodge-index inequality. Both tiers are invariant under replacing the polarizing form
$Q$ by $-Q$ (no imported statement mentions the sign of any self-pairing), and the border crossing
transports **numbers** (moduli, angles, dimensions), never the geometric **carrier** (the cycle lattice plus
ample cone) on which a signature could even be stated. Sieve theory consumes **purity and its sign-free
refinements** (facet A of the universal gap in [`sourcing_gap_r1.md`](sourcing_gap_r1.md)), never
**polarization** (the sign structure, facet B). Two disambiguations that make this falsifiable:
Kloostermania's celebrated exploitation of **sign changes** of Kloosterman sums sources those signs
**spectrally** (Kuznetsov / Petersson orthogonality, i.e. self-adjointness, the #143 operator branch), not
from the geometric import; and eigenvalue **phases** (Gauss's sign of the quadratic Gauss sum, root numbers
of functional equations) are S3/realization data, computable from traces alone and present for D-H too, not
S5 signature data.

## 3. Directional data, both ways

### 3a. Polarization implies parity-breaking (verified)

**Sawin-Shusterman** (*On the Chowla and twin primes conjectures over $\mathbb{F}_q[T]$*, Ann. Math. 196
(2022); arXiv:1808.04001, introduction read directly). They prove, for an odd prime $p$ and $q = p^m$:

- **Twin primes, quantitative** (Thm 1.1): for $q > 685090\,p^2$, the Hardy-Littlewood 2-point asymptotic
  holds in $\mathbb{F}_q[T]$, with a power saving.
- **Chowla $k$-point** (Thm 1.3): for $q > p^2 k^2 e^2$, $\sum_{|f| \le X} \mu(f+h_1)\cdots\mu(f+h_k) = o(X)$,
  with power saving. Their own words: "the main ingredient in the proof of Theorem 1.1 is the removal of the
  'parity barrier'."

The dependence on the Weil/Deligne polarization is explicit in the text (verified by keyword extraction from
the paper body): "By Deligne's theorem, the absolute values of the eigenvalues of Frobenius on the $i$-th
cohomology group are at most $q^{i/2}$"; the Kloosterman sheaf $\mathrm{Kl}_2$ "pure of weight 1" (Katz);
vanishing-cycles theory (SGA 7) following the Katz appendix to Hooley; a Weil bound of $2\sqrt{|P|}$ for the
relevant complete exponential sums; and a function-field variant of Fouvry-Michel. So over $\mathbb{F}_q[T]$:
**Deligne purity (= the polarization's modulus corollary) + geometry $\Rightarrow$ parity broken**, wholesale.

**The honest caveat on 3a.** The proof does not run on purity alone. It also uses an **exact characteristic-$p$
linearization of the parity object itself**: for $f = r + s^p$, the sign of Frobenius on the roots of $f$ is
the quadratic character of $\mathrm{disc}(f) = \mathrm{Res}(f, f')$, and $f' = r'$ is **constant in $s$**, so
$\mu(r + s^p)$ becomes a shifted quadratic **Dirichlet character** in $s$ (their Section 1.2, building on
Conrad-Conrad-Gross and classically on Pellet's formula). Over $\mathbb{Z}$ there is no derivative that dies,
no discriminant formula for $\mu(n)$, and hence no linearization. The parity-breaking over $\mathbb{F}_q[T]$
is purity **plus** an algebraic identity with no integer analogue. Direction (a) is real but weaker than
"RH $\Rightarrow$ parity-breaking": it is "RH-over-$\mathbb{F}_q$ + char-$p$ structure $\Rightarrow$ parity-breaking".

### 3b. Parity-breaking implies nothing about zeros (the absent converse)

- **Bombieri-Vinogradov** is exactly "GRH on average" in its **applications**, yet its proof and statement
  carry **zero information about the location of any zero** of any $L$-function. It is a theorem in every
  world, including a world with a zero at $\beta = 0.51$. Its bilinear/dispersion engine cannot even see such
  a zero.
- **Friedlander-Iwaniec** ($a^2+b^4$) and **Zhang** (bounded gaps) broke parity in their respective senses;
  neither produced any new zero-free region, any Li-coefficient inequality, or any one-sided positivity for
  $\zeta$. No such corollary is claimed anywhere in that literature (survey-depth, but the absence is
  well-known and structural, not an oversight).
- **Vinogradov-Korobov** (the $2/3$ zero-free exponent, the project's Architecture 4 ceiling) does **not**
  come from parity-breaking bilinear structure: it comes from Vinogradov's mean-value theorem for **one-variable
  Weyl sums** $\sum_n n^{it}$ (moment technology). The bilinear world and the zero-free-region world touch
  only in the shallow sense already recorded in LEARNINGS #133: Weil-II-powered positivity saturates the same
  $2/3$ ceiling ("too shallow" bracket).
- **No theorem runs parity-breaking $\Rightarrow$ zero-free region or $\Rightarrow$ positivity.** The absence
  of any reverse-direction theorem, across 80 years of a heavily-worked field, is itself a coordinate.
- Sharper still: **RH's sieve-visible content does not break parity.** Bombieri's asymptotic sieve fails at
  $k=1$ *even under Elliott-Halberstam* (every $\theta < 1$), which is stronger in the level aspect than GRH
  supplies (GRH gives $\theta = 1/2$, no more in the level aspect than Bombieri-Vinogradov already provides
  unconditionally). Scope kept honest (2026-07-02 ADVERSARY correction): this is a theorem about density
  inputs, not a non-implication theorem about RH itself. Chowla-type correlations are **not known** to be
  consequences of RH (no derivation exists; no independence proof exists either, and none is available by
  current methods). So the parity wall stands on both sides of RH in the known-implication sense: no route
  from RH to parity's resolution is known, and its instance-wise resolutions imply no RH-type statement. The
  two walls are **incomparable at the level of known implications**, with the density-input direction
  provably dead (Bombieri), not separated by a proven formal independence.

## 4. The identification test: the M4 fingerprint mapped onto the parity frame

The M4 polarity fingerprint ([`breadth_program.md`](breadth_program.md) Section 4; LEARNINGS #120/#121):
a transfer candidate must be **contingent + complex-root + line-axis + output-indefinite-with-the-sign-flipping
+ prohibitive-on-a-fixed-locus**. Mapping each axis onto the parity obstruction:

| Fingerprint axis | Parity-frame image | Holds? |
|---|---|---|
| Contingent (flips iff a zero leaves the line) | the parity obstruction does **not** flip on zero locations: it persists under EH/GRH (Bombieri's $\delta_x$ survives level 1), and its instance-wise resolutions leave the zeros untouched | **NO** |
| Complex-root ($t^2 - 4q < 0$ side) | the *imported* Weil bounds live on the complex-root side ($|\alpha| = \sqrt q$ pairs); but the sieve's own engine (Brun/Selberg $\Lambda^2$ weights) is a **sum-of-squares positive cone**, the real-rooted/SOS side the project's 4E.3/4E.8 wall already maps | inherited only; the frame itself is on the wrong half |
| Line-axis (Re $= 1/2$) | the frame's native axis is the **level of distribution** $\theta \in [1/2, 1]$ (an averaged modulus-range statement) plus the large-sieve $\sqrt x$ barrier on the **modulus** axis; a fourth shadow axis, joining spacing / central-rank / strip-width from screen #8 | **NO** (wrong axis, new flavor) |
| Output-indefinite with the sign flipping | the obstruction **is** literally a sign ($\mu = \pm 1$), a rank-one indefinite direction invisible to the positive cone; this is the one genuine rhyme. But the sign lives on the **input/weight side** (which measure $(1 \pm \lambda)\,dn$ you are sieving), not as the signature of an output form on the zeros | **PARTIAL** (right shape, wrong side of the #120 input/output split) |
| Prohibitive on a fixed locus | each parity-break finds its own Type II range per problem (FI's narrow window below $\sqrt x$, Zhang's ranges); the locus is **solved-for**, per sequence, i.e. curative in the #120 sense | **NO** |

Score: one partial hit out of five, plus one inherited property. By the battery's own arithmetic, the parity
barrier is **not** the M4 polarization wearing sieve clothing.

**Disqualifier screens run against "bilinear-form technology as an M4 source":**

- **Level-4 screen.** Bilinear/dispersion estimates are density/average statements (Levels 2-3 of the
  four-level framing). Bombieri-Vinogradov and Zhang are theorems compatible with a zero at $\beta = 0.51$.
  FAIL: not Level 4, cannot close RH by itself.
- **D-H screen.** See Section 5: exempt by type, not passing.
- **Discriminant screen (#119).** The technology's engine is SOS / positive-cone (real-root half); its deep
  inputs are complex-root but consumed as moduli. FAIL as a source; the complex-root content is borrowed.
- **Input/output split (#120).** The parity sign is an input-measure ambiguity, not an output signature.
  FAIL.
- **Curative-flip (#120).** Type II ranges are solved-for. FAIL.

One candidate **new screen** for the battery falls out of the audit: the **modulus-only-consumer screen**
(name kept for continuity; the precise antecedent, corrected by the 2026-07-02 ADVERSARY pass, is
**sign-free consumption**). If a technology consumes a polarization theorem only through **sign-free
corollaries**, the absolute-value tier ($|S| \le 2\sqrt p$, $|\alpha| \le q^{i/2}$) or the angle/monodromy
tier (weights in all degrees, monodromy classifications, equidistribution laws), then every imported
statement is invariant under flipping the polarizing form $Q \mapsto -Q$ and no geometric carrier crosses
the border: the signature never enters, so the technology cannot re-emit one, and it can never be an M4
**source** no matter how deep its imports. Scope rider: it stays available as an ingredient in an assembly
whose sign is sourced elsewhere (an operator per #143, or a genuine arithmetic polarization = M4 itself).
Operational test, per proof: list every statement imported from the algebro-geometric black box and check
whether any asserts the sign of a self-pairing or the signature of a form on cycles. Falsifier: an analytic
argument that imports the Hodge-index / Castelnuovo-Severi inequality itself (e.g. a sieve weight justified
by the positivity of a self-intersection on a specific correspondence) would break the screen; none is known
(2026-07-02). This retires generically the family "analytic imports of Weil/Deligne bounds" (Kloostermania,
exponential-sum technology, trace-function machinery) as polarization sources, while leaving them fully
alive as purity consumers. The #148 audit closes the loop from the producer side: purity is *produced*
(Weil I/II) without any polarization ever being produced (the Hodge standard conjecture stays open over
$\mathbb{F}_q$), so the consumed corollary is not even downstream of a polarization theorem in the modern
proof graph; a fortiori no sign is transported.

## 5. The Davenport-Heilbronn note

D-H has no Euler product, hence no multiplicative structure, hence no underlying sequence being sieved: sieve
axioms and the parity question **cannot even be stated** for D-H. This is the Architecture-2-style situation
(the frame requires the Euler product as a structural precondition), not a MIRROR failure: the frame is
**natively separating by type**, like the Frobenius/surface constructions, and unlike the stealth-window
mirrors (Lee-Yang #95, de Bruijn kernel #38, NB-Baez-Duarte #133). The honest rider: exemption is not a pass.
It means the D-H control has no traction inside this frame, so the frame supplies no discrimination leverage,
and the wrong-approach detector must be applied to whatever object a transfer would *produce*, not to the
sieve machinery itself.

## 6. Verdict: PARTIAL IDENTIFICATION. Same universal gap, other facet, one level downstream

**Not the same wall.** Four of five fingerprint axes fail; parity is logically incomparable with RH (neither
implies the other); and the walls are separated by actual theorems: parity has been crossed unconditionally in
specific integer sequences (FI 1998, Heath-Brown 2001, Zhang 2013) with zero movement on M4, and it has been
crossed wholesale over $\mathbb{F}_q[T]$ (Sawin-Shusterman) by *consuming* the proven polarization, not by
reproving it.

**But not unrelated either.** The precise relation, and the audit's yield:

1. **Parity maps to facet A (R1, sourcing/purity), not facet B (M4, polarization), of the one universal gap**
   ([`sourcing_gap_r1.md`](sourcing_gap_r1.md)). Every power-saving parity-break consumes $\sqrt q$-purity
   moduli; none consumes or produces a signature. The hypothesis "parity = polarization" is exactly the
   **genus-1 collapse** the #122 caveat warns about: in genus 1, $|\alpha| = \sqrt q \iff$ the primitive form
   is negative-definite, so purity and polarization are the same inequality there, and any frame that
   equates them silently is reading the genus-1 shadow.
2. **The sieve world independently reproduces R1's two-tier split.** Qualitative parity-breaking ($o(1)$
   cancellation: Matomäki-Radziwill, Tao's entropy decrement, Tao-Teräväinen) is achievable with **no variety
   and no zeros**; power-saving / square-root-strength parity-breaking is known **only** via Weil/Deligne
   (function-field, or fiberwise inside integer problems). Shape sourceable, $\sqrt q$-strength variety-gated:
   the same split #130 verified for Galois representations, now visible in a fully independent corpus. This is
   a genuine convergence datum, and it sharpens the R1 WATCH trigger (see Section 7).
3. **The two-variable rhyme is real but lives one level down.** What breaks parity is access to a genuine
   product structure (Type II sums live on a product of two ranges); what proves the function-field
   polarization is the surface $C \times C$; what the Arakelov face lacks (#131) is exactly
   $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ + $\Gamma_S$. The hypothesis's instinct
   ("the missing resource is a two-variable pairing with square-root cancellation") is the right shape but
   attaches to the **realization/sourcing** side: the sieve consumes the pairing's modulus, and RH needs the
   pairing's **sign**. Coordinate, framed positively: analytic number theory's own wall-map (parity vs
   zero-location, two walls its practitioners have always kept distinct) matches the project's two-facet gap
   (R1 vs M4), from a corpus the breadth battery had never screened.

**What it buys either way.** Different-walls is the finding, and it is a compression: "bilinear-form
technology" can be struck from the M4-source search space (the modulus-only-consumer screen does it in one
line), while the sieve corpus is promoted to a second independent witness for the R1 two-tier structure. The
single most promising object surfaced, correctly aimed at **R1 rather than M4**: the **Friedlander-Iwaniec
bilinear hypothesis for $\mu$** (Ann. Math. 148 (1998), the added axiom), as a *reformulation target* for the
variety-free-purity watch item. Any unconditional power-saving verification of a $\mu$-bilinear form in the
critical narrow range below $\sqrt x$, for a non-algebraic sequence, without finite-field geometry, would be
the sieve-side signature of a variety-free purity mechanism, exactly the #130 WATCH trigger, now with a
concrete analytic shape. The entropy-decrement tier shows the qualitative version is already crossed, so the
trigger is specifically the **exponent** (power saving), not the cancellation.

## 7. What this enables / what remains open

**Enables.**
- BUILDER / ADVERSARY: the **modulus-only-consumer screen** as a candidate battery addition (Section 4);
  cheap to apply, retires the exponential-sum-import family as M4 sources generically.
- SYNTHESIZER: the **level-of-distribution axis** as a fourth wrong-axis flavor for screen #8 (spacing /
  central-rank / strip-width / level).
- ORCHESTRATOR: sharpen the standing R1 WATCH item (#130) with the sieve-side trigger: *unconditional
  power-saving bilinear $\mu$ cancellation near $\sqrt x$ without finite-field geometry*. Watch the
  Matomäki-Radziwill / entropy-decrement school for any move from $o(1)$ to a power saving; that school is
  where a variety-free purity mechanism would first surface in analytic clothing.
- The Sawin-Shusterman char-$p$ linearization ($\mu(r+s^p)$ = shifted quadratic character via the
  discriminant) is a checkable toy-sandbox datum: the parity object *linearizes* exactly when the derivative
  collapses, an algebraic degree of freedom $\mathbb{Z}$ lacks. Candidate addition to
  [`../../experiments/toy/`](../../experiments/toy/) as a grader note, not a construction.

**Remains open.**
- ~~Whether the modulus-only-consumer screen survives an ADVERSARY pass.~~ **Resolved 2026-07-02: UPHELD
  WITH CORRECTIONS** (see the ADVERSARY-pass section at the end of this dossier). No historical case of a
  modulus import re-emitting a sign was found; two tier-2 (angle/monodromy) consumption families forced the
  antecedent correction; the screen is machine-enforced in
  [`../../experiments/lemma_db/breadth_corpus.py`](../../experiments/lemma_db/breadth_corpus.py) (23/23).
- The parity barrier's own "polarity" formalization: sharpest citable form now pinned (2026-07-02) as
  Bombieri 1976 as formalized in Tao 2016 ($\delta_x \in [0,2]$ free under all density axioms), with
  Selberg 1949's two-measure witness $(1 \pm \lambda(n))\,dn$; textbook form in Friedlander-Iwaniec,
  *Opera de Cribro* (AMS Colloq. 57, 2010), the parity-phenomenon discussion (exact section number needs
  literature verification). Sufficient to bank the screen; a Lean-shaped formalization remains open and is
  not claimed.
- Angle A of this two-dossier probe (the companion frame-audit) and the cross-check between the two.

## Discrepancy log

- The probe's hypothesis as posed ("parity = M4 in another language") is **not** upheld; the audit corrects
  it to "parity = the consumer-side shadow of R1 (facet A)". This disagrees with the hypothesis, not with any
  standing repo analysis; it *agrees* with #130's two-facet split and #122's genus-1 caveat, and extends both.
- No conflict found between the sieve literature and the repo's existing claims. One near-conflict resolved:
  "square-root cancellation of the parity object is RH" (via $M(x) = O(x^{1/2+\epsilon})$, Littlewood 1912)
  is true for the **mean** of $\mu$ but does not make the parity barrier RH-contingent, because parity
  concerns **correlations** (Chowla-type), which RH does not control. The two statements coexist; conflating
  them would repeat the genus-1-style collapse in an analytic register.

## References (all verified against source or secondary source this session; depth flagged in header)

- A. Selberg, *On elementary methods in prime-number theory and their limitations*, Proc. 11th Scand. Congress Trondheim (1949). E. Bombieri, *The asymptotic sieve*, Mem. Accad. Naz. dei XL (5) 1/2 (1976), 243-269.
- T. Tao, *Open question: the parity problem in sieve theory* (2007); *Notes on the Bombieri asymptotic sieve* (2016), terrytao.wordpress.com.
- J. Friedlander, H. Iwaniec, *Asymptotic sieve for primes*, Ann. Math. 148 (1998), 1041-1065; *The polynomial $X^2 + Y^4$ captures its primes*, Ann. Math. 148 (1998), 945-1040 (arXiv:math/9811186).
- J.-M. Deshouillers, H. Iwaniec, *Kloosterman sums and Fourier coefficients of cusp forms*, Invent. Math. 70 (1982), 219-288. E. Bombieri, J. Friedlander, H. Iwaniec, *Primes in arithmetic progressions to large moduli*, Acta Math. 156 (1986). D.R. Heath-Brown, *Primes represented by $x^3 + 2y^3$*, Acta Math. 186 (2001).
- Y. Zhang, *Bounded gaps between primes*, Ann. Math. 179 (2014), 1121-1174; the Polymath8 record (Tao's reading seminar 2013; Kowalski, *Bounded gaps between primes: some grittier details*, 2013).
- W. Sawin, M. Shusterman, *On the Chowla and twin primes conjectures over $\mathbb{F}_q[T]$*, Ann. Math. 196 (2022); arXiv:1808.04001 (read: intro, Thms 1.1/1.3/1.4; Deligne/Katz/vanishing-cycles usage verified in body).
- K. Matomäki, M. Radziwill, *Multiplicative functions in short intervals*, Ann. Math. 183 (2016); T. Tao, *The logarithmically averaged Chowla and Elliott conjectures*, Forum Math. Pi (2016); T. Tao, J. Teräväinen (odd-order log-averaged Chowla).

## Draft LEARNINGS entry (do not merge without SYNTHESIZER review)

> ### NNN. THE PARITY BARRIER IS NOT M4; IT IS THE CONSUMER-SIDE SHADOW OF R1 (frame-audit, angle B of the
> regime-two probe), 2026-07-01. The sieve parity barrier (Selberg 1949; Bombieri 1976: $\delta_x \in [0,2]$
> survives even Elliott-Halberstam) was audited against the M4 fingerprint: 1/5 axes hold (the $\mu$-sign is a
> rank-one indefinite direction, but on the INPUT/weight side per #120), 4/5 fail (not contingent on zeros:
> parity survives RH; wrong axis: level-of-distribution, a NEW fourth shadow axis for screen #8; curative Type
> II ranges; SOS/positive-cone engine). Every power-saving parity-break (Deshouillers-Iwaniec, Friedlander-
> Iwaniec $x^2{+}y^4$, Zhang Type III via Birch-Bombieri, Sawin-Shusterman over $\mathbb{F}_q[T]$, Deligne
> usage verified in-text) CONSUMES Weil/Deligne purity as a MODULUS bound and discards the sign: sieve theory
> is a purity consumer (facet A = R1), never a polarization producer (facet B = M4); "parity = polarization"
> is exactly the #122 genus-1 collapse. The sieve corpus independently reproduces R1's two-tier split
> (qualitative $o(1)$ parity-breaking is variety-free: Matomäki-Radziwill/Tao entropy decrement; power-saving
> is variety-gated), a second independent witness for #130. Yields: the modulus-only-consumer screen
> (candidate battery addition, retires exponential-sum-import technology as M4 sources); the sharpened R1
> WATCH trigger (unconditional power-saving bilinear $\mu$ cancellation near $\sqrt x$ without finite-field
> geometry = the FI bilinear hypothesis gone variety-free). Dossier:
> docs/03_research/parity_vs_polarization.md. No reverse theorem (parity-breaking $\Rightarrow$ zeros) exists;
> that absence is the coordinate.

## ADVERSARY pass (2026-07-02): resolution

**Verdict: UPHELD WITH CORRECTIONS (correct-in-place).** Full attack notes:
`scratchpad/counting_roads_followup/02_adversary_modulus_only.md` (gitignored).

**Strongest attack and how it resolved.** The screen's original antecedent ("consumes ... only through its
absolute-value corollary") was falsified by the dossier's own ledger: Fouvry-Kowalski-Michel trace-function
machinery and Sawin-Shusterman consume a second, deeper tier (weights in all degrees, monodromy
classifications, angle-equidistribution laws such as vertical Sato-Tate), not just moduli. And without a pin
on "sign structure", Kloostermania's sign-change engine looks like a counterexample. Resolution: the
antecedent is corrected to **sign-free consumption** (tier 1 moduli OR tier 2 angle/monodromy; both invariant
under $Q \mapsto -Q$; no geometric carrier crosses the border), and "sign" is pinned to the **S5 signature**
(excluding eigenvalue phases like Gauss-sum signs, S3 root numbers, and proof-internal oscillation, which is
Kuznetsov/operator-sourced per #143). Under the corrected wording every candidate counterexample examined
(DFI/Kloostermania bilinear forms, FKM trace functions, Sato-Tate inside sieves, Gauss's sign determination,
root-number arguments, large-sieve/Petersson positivity) **strengthens** the screen: each consumes more than
moduli yet never the signature, and the tier-2 consumers remain parity-limited themselves (Fouvry-Michel sign
changes land on almost-primes). The #148 producer-side finding braces it from the other side: purity is
produced (Weil I/II) with no polarization ever produced, so the consumed corollary is not even downstream of
a polarization theorem.

**Corrections applied to this dossier** (each marked in place): (1) Section 2 "How it is consumed" rewritten
with the two-tier taxonomy and the falsifiability disambiguations; (2) Section 1 EH endpoint gains the
Friedlander-Granville 1989 caution ($\theta = 1$ means every $\theta < 1$); (3) Section 3b headline scoped to
"RH's **sieve-visible** content does not break parity" and "not consequences of RH" corrected to "not
**known** to be consequences" ("logically incomparable" softened to "incomparable at the level of known
implications"); (4) Section 4 screen definition corrected (sign-free antecedent + operational $Q \mapsto -Q$
test + explicit falsifier + M4-source scope rider); (5) Section 7 open items resolved/pinned.

**Falsification condition left standing (the screen is falsifiable):** any analytic/sieve argument importing
the Hodge-index / Castelnuovo-Severi inequality itself. None found; literature watch.

**Wiring status.** Both #146 yields are now machine-enforced in
[`../../experiments/lemma_db/breadth_corpus.py`](../../experiments/lemma_db/breadth_corpus.py): a new
`weil_consumption` skeleton dimension ('sign-free' fires the #146 screen; 'signature' and 'producer' do not)
and `axis="level"` as the fourth wrong-axis flavor, plus the sieve-parity corpus row (fires #146 + level-axis
+ #120 input/output + #120 curative + #119 discriminant + Level-3, matching Section 4) and a 'sign-free' tag
on the Katz-Sarnak row. Self-consistency: the Weil/Rosati master column (tagged 'signature') keeps its
transfer candidacy (test-enforced); the Ihara/Ramanujan row stays 'na' by the documented tagging discipline
(tag the claimed route to a signature, not the historical constructions; graph-RH's sign is operator-sourced).
Test suite: 19/19 before this pass, **23/23 after** (the "16/16" previously recorded here and in
`breadth_program.md` / `breadth_corpus.md` was stale; the suite was already 19/19 after #143).
