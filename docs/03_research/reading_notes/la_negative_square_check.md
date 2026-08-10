# Does Burnol's $L_a$ satisfy the negative-square condition? A candidate Krein-Langer $N_\kappa$ realization check

> SURVEYOR/BUILDER dossier, 2026-07-18 (overnight). Attempts the residual named twice in the same
> day's prior work: [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md) Section 4 ("Whether
> the translation would even succeed (does $L_a$'s pole data satisfy the negative-square condition
> required to be a bona fide $q\in N_\kappa$ for finite $\kappa$?) is consequently an open computation
> nobody has attempted, not a settled fact in either direction") and Section 7, residual 3 ("Whether
> $L_a$'s pole data actually satisfies the negative-square condition needed to realize it as a
> generalized Nevanlinna function... has never been checked by anyone, in either direction"). Both are
> restatements of [`PHASE_STATE.md`](../../../PHASE_STATE.md)'s #164 reopen condition (i). This note is
> a direct attempt at that open computation, not a survey of whether one exists.
>
> **STATUS.** Date 2026-07-18. Verdict tier: **REALIZABLE-CANDIDATE** ($\kappa = 1$, computed via a
> mirror-pole Cauchy-kernel local model derived in Section 5 below and checked numerically in Section 6;
> **not a proof for the true, global $L_a$**, see Section 7 for exactly what is missing). This is
> sharper than the prompt's own prior guess of $\kappa\le 2$ (matching $\dim(L_a/K_a)=2$): the two pole
> directions turn out to be a *mirror pair* relative to Burnol's own real axis (the critical line
> $\mathrm{Re}(s)=1/2$), not two independent one-sided negative directions, and a mirror pair costs
> exactly one negative square, robustly, independent of the unknown coupling strength. **Consequence
> for #164 (Section 9): does not reopen the closure** (the majorant/extremal-theorem absence found by
> the same-day BBH dossier is untouched by this note), but it answers, at candidate tier, the specific
> sub-question that dossier left as "unattempted," and it sharpens the remaining question from "does
> $L_a$ instantiate the Kaltenbäck-Woracek framework at all" to "does an extremal/majorant theorem exist
> for the specific class $HB_1$."
>
> Method discipline: every load-bearing claim is tagged [FETCHED] (read at source this session),
> [SECONDARY] (via a citing source, search snippet, or converged-but-unpinned restatement), or flagged
> explicitly as this note's own derivation. No claim is promoted across tiers. No em dashes.

## 1. The question, restated precisely

Does the pole data of Burnol's extended Sonine space $L_a$ (simple poles of the completed Mellin
transform at $s=0$ and $s=1$, Burnol arXiv:math/0203120 Prop. 2.2; $\dim(L_a/K_a)=2$, Prop. 4.5) satisfy
the negative-square condition needed to realize $L_a$'s structure data as a generalized Nevanlinna
function $q$ in the Krein-Langer class $N_\kappa$, i.e. can $L_a$ be realized inside the
Kaltenbäck-Woracek indefinite de Branges (dB-Pontryagin) framework with finite negative index $\kappa$?
If so, what is the smallest such $\kappa$, and by what computation?

## 2. Sources

| Source | Tier | What it gives |
|---|---|---|
| Burnol, "Two complete and minimal systems associated with the zeros of the Riemann zeta function," arXiv:math/0203120 (the JTNB paper) | [FETCHED], two independent passes: (1) ar5iv HTML, three targeted extraction passes; (2) **the raw local `pdftotext` conversion of the actual JTNB PDF** (`burnol_jtnb.txt`), found already sitting in this session's shared scratchpad from earlier same-day work on [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md), read directly and used to correct/upgrade several items past pass (1)'s summarized quotes. Also cross-checked against the verbatim quotes already banked in [`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md), which independently pins the same Prop. 2.2 / Thm. 2.1 / Prop. 4.5 text today | Prop. 2.2 (poles at $s=0,1$, and the exact $Y^a_{w,k}$ evaluator-vector definition), Thm. 2.1 ($K_a$ entire, satisfies "all axioms of de Branges' general theory"), Prop. 4.5 ($\dim(L_a/K_a)=2$, quoted with its proof); the real axis = critical line confirmation ("*Some slight change of variable is necessary to recover the original de Branges formulation, as he ascribes to the real axis the rôle played here by the critical line*"); Burnol's own stated reason for the bilinear (not sesquilinear) pairing, quoted exactly in Section 4 |
| Kaltenbäck, Woracek, "Pontryagin spaces of entire functions I," Integral Equations Operator Theory 33 (1999) 34-97 | [FETCHED] (PDF obtained from the author's own homepage listing, `haraldworacek.github.io/homepage/Downloads/JournalPapers/1999/17.pdf`, downloaded and converted to text locally with `pdftotext -layout`, read directly; a WebFetch attempt on the Springer page redirected to an auth wall and a direct WebFetch of the raw PDF could not parse the compressed stream, so the local conversion was necessary and is the actual source read) | Definition 2.1 (the Nevanlinna class $N_\kappa$, defined directly via $\kappa$ negative squares of the Nevanlinna kernel), Definition 3.1 (the dB-Pontryagin space axioms), Section 5 Definition 5.1 ($S_\kappa$, the indefinite Schur class, and $HB_\kappa$, the indefinite Hermite-Biehler class), **Theorem 5.3** (the entry theorem: a dB-Pontryagin space of negative index $\kappa$ corresponds exactly to an entire $E\in HB_\kappa$, and conversely, with no extra hypotheses beyond $E\in HB_\kappa$ itself) |
| Woracek, "Existence of zerofree functions $N$-associated to a de Branges Pontryagin space," Monatsh. Math. 162 (2011) 453-506 | [FETCHED], inherited from [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md) Section 4 (itself sourced at primary-text level the same day; not independently re-fetched tonight) | The Nevanlinna kernel formula $K_q(w,z)=\frac{q(z)-\overline{q(w)}}{z-\bar w}$; confirms Definition 6.6 / Prop. 6.8's admissible-majorant criterion is stated only for the classical subclass $E\in HB_0$, never for $E\in HB_{<\infty}$ |
| Kulikov, Nazarov, Sodin school papers on generalized Nevanlinna functions (arXiv:1011.2081, arXiv:1306.1117) and general web search on "$\kappa$ negative squares" | [SECONDARY] (multiple independent search/fetch passes converge on the same elementary characterization, but no single verbatim primary-source quote with equation number was obtained; Kaltenbäck-Woracek Part I itself treats this elementary definition as known background, citing Iokhvidov-Krein-Langer and Alpay-Dijksma-Rovnyak-de Snoo, not restating it) | The finite-point characterization: a Hermitian kernel $K$ has $\kappa$ negative squares if, for every finite set of points $z_1,\dots,z_n$ in the domain, the Hermitian matrix $(K(z_i,z_j))_{i,j=1}^n$ has at most $\kappa$ negative eigenvalues, and $\kappa$ is the smallest integer with this property over all finite configurations |
| This note's own derivation (Section 5) and script (Section 6) | Own work, this session | The rank-2 mirror-pole kernel algebra; the numerical signature computation |
| Attempted but not reached: direct PDF text of arXiv:1011.2081 (compressed stream unparseable by WebFetch); Springer abstract page for K-W Part I (redirects to an auth wall, unreachable anonymously) | **UNREACHED** | No claim made about content beyond what the ar5iv/search-snippet passes on these same sources already gave (tabulated above under "SECONDARY") |

## 3. Definitions pinned

**The Nevanlinna class $N_\kappa$ [FETCHED, Kaltenbäck-Woracek Part I, Definition 2.1].** Quoted, with
the paper's own conjugation notation $F^\#(z):=\overline{F(\bar z)}$ (a function is "real" iff
$F=F^\#$) reconstructed from a locally-corrupted OCR extraction: the downloaded PDF's overline
diacritics did not survive `pdftotext` cleanly and are restored below (confirmed by repeated pattern,
e.g. "$z,\bar z\in O$" printed with the bar silently dropped in multiple places across the document,
not a one-off). The reconstruction matches the paper's own stated formula pattern exactly, cross-checked
against the parallel formula (5.1) in Theorem 5.3 and against the standard form of this definition
appearing consistently across every [SECONDARY] source found. (Neither the raw extraction of Definition
2.1 nor of formula (5.1) in Theorem 5.3 shows a $\pi$ normalization constant; Theorem 5.3's formula
below restores one by analogy with the standard classical de Branges reproducing-kernel formula
[UNVERIFIED-MEMORY, general knowledge of the classical theory, not confirmed against this specific
extraction], since the same diacritic-loss pattern that is confirmed for overline bars could plausibly
also have dropped a $\pi$; this specific symbol's presence in the original is not independently
confirmed either way.)

> An $n\times n$-matrix valued function $Q$, analytic in an open, reflection-symmetric set
> $O=\overline O^\#$, is said to be an element of the Nevanlinna class $N_\kappa^{n\times n}$ if
> $Q(z)^\# = Q(\bar z)$ whenever $z,\bar z\in O$, and if the kernel
> $$N_Q(z,w) = \frac{Q(z)-Q(w)^\#}{z-\bar w}, \qquad z,w\in O,$$
> has $\kappa$ negative squares. [$N_\kappa$ abbreviates $N_\kappa^{1\times1}$.] "The reproducing kernel
> Pontryagin space generated by the kernel $N_Q$ for a Nevanlinna function $Q$... is denoted..."
> [FETCHED, Part I, immediately following Definition 2.1; the space's own name is truncated by the OCR
> extraction at this point, but the sentence's content, that $N_Q$ directly generates a reproducing
> kernel Pontryagin space, is intact and is standard].

**Negative squares, the elementary form [SECONDARY, converged across multiple independent sources; not
independently pinned to one verbatim primary quote tonight].** For a Hermitian kernel $K(z,w)$ on a set
$\Omega$: $K$ has $\kappa$ negative squares if, for every finite $z_1,\dots,z_n\in\Omega$, the Hermitian
matrix $\big(K(z_i,z_j)\big)_{i,j=1}^n$ has at most $\kappa$ negative eigenvalues, and $\kappa$ is
minimal with this property (i.e. some finite configuration actually achieves $\kappa$ negative
eigenvalues). This is the definition used throughout Section 6's numerical work.

**The dB-Pontryagin space axioms [FETCHED, Kaltenbäck-Woracek Part I, Definition 3.1]**, the "entry
condition" the task asked to pin, and the answer to "which Part of the series states the axioms": Part
I, not a later part. Given a space $P$ of entire functions with an indefinite inner product
$[F,G]=(GF,\cdot)$ built from a bounded self-adjoint $G$:

> $\langle P,[.,.]\rangle$ is called a de Branges inner product space (dB-space) if:
> (i) $F\in P \Rightarrow F^\#\in P$, with $[F^\#,G^\#]=[G,F]$;
> (ii) for $w\in\mathbb C\setminus\mathbb R$ and $F\in P$ with $F(w)=0$, the function
> $\frac{z-\bar w}{z-w}F(z)$ is again in $P$, with $\big[\frac{z-\bar w}{z-w}F(z),G(z)\big] =
> \big[F(z),\frac{z-\bar w}{z-w}G(z)\big]$.
> If $\kappa(G)<\infty$ ($\kappa(G)=\kappa$) we call $\langle P,[.,.]\rangle$ a dB-Pontryagin
> (dB-Hilbert, if $\kappa=0$) space.

**The indefinite Hermite-Biehler class and the entry theorem [FETCHED, Part I, Definition 5.1 and
Theorem 5.3].** $S_\kappa$ is the set of functions $Q$ meromorphic in $\mathbb C^+$ such that the
Schur-type kernel $S_Q(z,w) := \frac{i(1-Q(z)\overline{Q(w)})}{z-\bar w}$ has $\kappa$ negative squares;
$HB_\kappa$ is the set of entire $E$ with $E^{-1}E^\#\in S_\kappa$, $E,E^\#$ sharing no non-real zero,
and $E/E^\#$ non-constant. Then, verbatim in content (formula reconstructed from corrupted OCR to its
standard classical form, $E=A-iB$ with $A,B$ real entire, cf. the formula already independently
reconstructed the same way by [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md) Section 4
from the parallel formula in Woracek 2011):

> **Theorem 5.3.** Let $\langle P,[.,.]\rangle$ be a dB-Pontryagin space with reproducing kernel
> $K(w,z)$. Then $K(w,z) = \dfrac{B(z)\overline{A(w)}-A(z)\overline{B(w)}}{\pi(z-\bar w)}$ for some real
> entire $A,B$, and $E:=A-iB\in HB_\kappa$ where $\kappa:=\mathrm{Ind}_-P$ (the negative index of $P$).
> **Conversely**, if $E\in HB_\kappa$ is given, $E=A-iB$, and $K(w,z)$ is defined by this same formula,
> then the reproducing kernel Pontryagin space $P(E)$ with kernel $K(w,z)$ is a dB-Pontryagin space
> [with negative index $\kappa$].

This is the precise theorem that would need to be invoked once (if ever) $L_a$'s data is packaged as a
genuine $E\in HB_\kappa$: **the converse direction of Theorem 5.3 has no hypothesis beyond
$E\in HB_\kappa$ itself.** This directly answers the task's request to name which K-W theorem is the
relevant entry point: it is Theorem 5.3 of Part I, not a result in a later part of the series.

**Bonus finding, extending the same-day BBH dossier's own residual list.** Having downloaded and
grepped the complete text of Part I (3527 lines after `pdftotext` conversion) for this note,
[`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md) Section 7's residual 1 ("Kaltenbäck-Woracek
Parts I, II, III, V, and VI were not read in full... a majorant theorem stated literally for
$E\in HB_{<\infty}$ could in principle live in one of the unread parts") is now **partially discharged**:
a direct grep of Part I's full text for "majorant," "admissible," and "extremal" returns **zero hits**
[FETCHED]. Part I contains no majorant or extremal theorem of any kind. Parts II, III, V, VI remain
unread and are still open per that dossier's own residual list; only Part I is newly closed here.

## 4. $L_a$'s concrete data, and the mirror-pair structure

From Burnol arXiv:math/0203120 [FETCHED: first via ar5iv HTML, then **cross-verified directly against a
raw local `pdftotext` conversion of the JTNB PDF** (`burnol_jtnb.txt`) already sitting in this session's
shared scratchpad from earlier same-day work on [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md);
the passages below are read from that raw text, not a web-fetch summary, upgrading several items past
what the first pass alone would have supported]:

- **Theorem 2.1.** For $f\in K_a$, the completed right Mellin transform
  $M(f)(s)=\pi^{-s/2}\Gamma(s/2)\hat f(s)$ is entire, and $K_a$ (as a space of such transforms)
  "satisfies all axioms of [de Branges'] general theory of Hilbert spaces of entire functions."
- **Proposition 2.2.** For $f\in L_a\supset K_a$, $M(f)(s)$ is meromorphic with at most simple poles
  at $s=0$ and $s=1$. Quoted directly from the raw conversion: "*The evaluations $f\mapsto M(f)^{(k)}(w)$
  for $w\ne0, w\ne1$, or $f\mapsto\mathrm{Res}_{s=0}(M(f))$, $f\mapsto\mathrm{Res}_{s=1}(M(f))$ are
  continuous linear forms on $L_a$. One has the functional equation $M(\mathcal F_+(f))(s)=M(f)(1-s)$.*"
  Burnol then names the vector $Y^a_{w,k}\in L_a$ representing each such evaluator: for $w\ne0,1$,
  $\int_0^\infty f(t)\,Y^a_{w,k}(t)\,dt = M(f)^{(k)}(w)$ for all $f\in L_a$; $Y_0^a$ and $Y_1^a$ denote
  the (limiting, $k=0$) evaluators computing the residues at $0$ and $1$ respectively.
- **The bilinear, not sesquilinear, pairing [FETCHED, upgraded from the earlier session's SECONDARY
  paraphrase-risk flag to a direct quote].** "*We are using the bilinear forms
  $[f,g]=\int_0^\infty f(t)g(t)\,dt$ and not the Hermitian scalar product
  $(f,g)=\int_0^\infty f(t)\overline{g(t)}\,dt$ in order to ensure that the dependency of $Y^a_{w,k}$
  with respect to $w$ is analytic and not anti-analytic.*" This is Burnol's own stated reason, and it
  is the standard reason for this device in reproducing-kernel theory (to keep the evaluator family
  jointly holomorphic rather than holomorphic in one variable and antiholomorphic in the other). It
  meaningfully de-risks Section 7's gap 4 below: the passage to the standard sesquilinear
  reproducing-kernel convention used throughout Kaltenbäck-Woracek is the routine one (post-compose
  with conjugation in the evaluation parameter), though it was not carried out explicitly in Section
  5's algebra.
- **Proposition 4.5, quoted directly.** "*One has $\dim(L_a/K_a)=2$*." Proof (quoted): "*equivalent to
  the fact that the residue-evaluators $Y_0^a$ and $Y_1^a$*" are linearly independent; $K_a$ itself
  "*is defined by two linear conditions*" inside $L_a$ (vanishing, rather than merely finite, at each
  pole).
- **The real-axis convention, confirmed at source, now twice.** "*Some slight change of variable is
  necessary to recover the original de Branges formulation, as he ascribes to the real axis the rôle
  played here by the critical line.*" ("he" = de Branges; this sentence sits directly under Theorem 2.1
  in the raw text, i.e. it is stated for $K_a$, and by Burnol's own consistent notation and the shared
  $s\leftrightarrow1-s$ functional equation, it governs $L_a$ identically.) $L_a$ itself is defined as
  functions merely *constant* (not vanishing) on $(0,a)$ together with a constant cosine transform on
  $(0,a)$, the weaker condition that is the source of the extra pole data relative to $K_a$'s vanishing
  condition.

**The mirror-pair observation (this note's own reading of the above, not stated by Burnol).** $s=0$
and $s=1$ are both *real numbers* in the ordinary sense, but relative to the dB space's own intrinsic
structural axis (the critical line), neither sits on that axis, and they are exact mirror images of
each other under the space's own reflection $s\leftrightarrow1-s$ (their average is exactly $1/2$).
This is precisely the situation a de Branges-Pontryagin space calls a conjugate pair of non-real poles,
even though $0$ and $1$ are literally real: "real" and "non-real" in this theory are always relative to
the structural axis in force, not the literal number line. This distinction is the entire content of
Section 5 below.

**Two elementary residues that seed the model [FETCHED, standard classical facts, confirmed to 30
digits with mpmath in Section 6's script].** $\Gamma(s/2)\sim 2/s$ as $s\to0$ (so
$\pi^{-s/2}\Gamma(s/2)$ has residue exactly $2$ at $s=0$, an archimedean/Gamma-factor fact, unrelated to
zeta); $\zeta(s)\sim\frac1{s-1}+\gamma_E$ as $s\to1$ (residue exactly $1$ at $s=1$, the arithmetic pole).
Burnol's own multiplier $\chi(s)=\zeta(s)/\zeta(1-s)$ was checked directly (this note's own small
calculation, elementary Laurent expansion, not sourced) to have a *zero*, not a pole, at $s=0$
(since $\zeta(1-s)\to\infty$ there) and a simple pole of residue $-2$ at $s=1$; this shows the two poles
of $M(f)(s)$ for $f\in L_a$ are not both coming from $\chi$ alone, consistent with one pole being the
archimedean Gamma-factor singularity and the other the arithmetic zeta singularity, entering by
different mechanisms of Burnol's construction.

**What was not extracted, even after the raw-text cross-check.** The evaluators $Y_0^a,Y_1^a$ are named
and their defining pairing is now pinned exactly (above), but no explicit closed-form relation between
$Y_0^a$ and $Y_1^a$ themselves (e.g. a formula giving one as a fixed multiple or transform of the other
via the $s\leftrightarrow1-s$ functional equation) was found near Prop. 4.5 or its proof in the raw
text; a further, wider search of the same source (beyond the sections read this session) might locate
one, but that search was not carried out tonight. This remains the single largest concrete gap between
this note's model and a literal computation on Burnol's actual construction: it is the coupling
constant $\rho(a)$ itself (Section 5), and no source found tonight supplies it in closed form. See
Section 7.

## 5. The kernel-modification algebra (this note's own derivation)

**Setup.** Model the rank-2 correction as a genuine generalized-Nevanlinna singular part added to
$K_a$'s own (positive, classical) reproducing kernel: $K_L = K_a + K_{\text{sing}}$, where
$K_{\text{sing}}$ is built purely from the two pole directions. This additive ansatz is the natural,
standard shape of a finite-rank Pontryagin-space extension (matching how Theorem 5.3's machinery is
used throughout the K-W series), **but it has not been verified against Burnol's own literal formulas**;
it is a candidate, clearly flagged.

**Step 1: change coordinates to Burnol's own real axis.** Let $\tau := i(s-\tfrac12)$, i.e.
$s=\tfrac12-i\tau$. Then $\mathrm{Re}(s)>\tfrac12 \Leftrightarrow \mathrm{Im}(\tau)>0$: this sends
Burnol's own "upper half-plane" to the standard one. Under this map, $s=1\mapsto\tau_1=i/2\in\mathbb
C^+$, and $s=0\mapsto\tau_0=-i/2=\overline{\tau_1}\in\mathbb C^-$: a genuine, exact conjugate pair.

**Step 2: the candidate singular part.** Take the minimal real-symmetric (i.e.
$Q(\bar\tau)=\overline{Q(\tau)}$) meromorphic function with simple poles exactly at $\tau_1,\tau_0$:
$$Q_{\text{sing}}(\tau) = \frac{\rho}{\tau-\tau_1} + \frac{\bar\rho}{\tau-\tau_0}, \qquad \rho\in\mathbb C
\text{ an unknown coupling constant}.$$
(Reality check, direct computation: $\overline{Q_{\text{sing}}(\tau)} = \frac{\bar\rho}{\bar\tau-\tau_0}
+\frac{\rho}{\bar\tau-\tau_1} = Q_{\text{sing}}(\bar\tau)$, using $\bar\tau_1=\tau_0$. Confirmed.)

**Step 3: the Nevanlinna kernel of the singular part, in closed form.** Writing $u_1(\tau):=
\frac1{\tau-\tau_1}$, $u_0(\tau):=\frac1{\tau-\tau_0}$, direct algebra (telescoping the difference
$Q_{\text{sing}}(\tau)-\overline{Q_{\text{sing}}(w)}$ over the common factor $\tau-\bar w$; carried out
by hand and independently checked against a direct numerical evaluation in Section 6, agreement to
floating-point precision) gives:
$$K_{\text{sing}}(w,\tau) := \frac{Q_{\text{sing}}(\tau)-\overline{Q_{\text{sing}}(w)}}{\tau-\bar w}
= -\rho\, u_1(\tau)\,\overline{u_0(w)} \;-\; \bar\rho\, u_0(\tau)\,\overline{u_1(w)}.$$
This is **purely off-diagonal** in the $(u_0,u_1)$ basis: writing
$K_{\text{sing}}(w,\tau)=\sum_{i,j\in\{0,1\}} C_{ij}\,u_i(\tau)\overline{u_j(w)}$, the coefficient block
is
$$C = \begin{pmatrix} 0 & -\rho \\ -\bar\rho & 0\end{pmatrix}, \qquad \text{Hermitian, } C_{00}=C_{11}=0.$$

**Step 4: the signature.** The eigenvalues of $\begin{pmatrix}0&x\\\bar x&0\end{pmatrix}$ are exactly
$\pm|x|$ for any $x\in\mathbb C$ (characteristic polynomial $\lambda^2-|x|^2=0$). So for **any**
$\rho\ne0$, $C$ has eigenvalues $\{+|\rho|,-|\rho|\}$: signature $(1,1)$, i.e. **exactly one negative
eigenvalue, regardless of the magnitude or phase of $\rho$.** Translating back: $u_1(\tau(s))\propto
\frac1{s-1}$ and $u_0(\tau(s))\propto\frac1s$ (direct substitution, up to an overall constant factor
$-i$ that does not affect signature), matching the task prompt's own suggested Cauchy-kernel vectors
$\frac1s,\frac1{s-1}$ exactly.

**Why the diagonal vanishes, and why this matters.** The vanishing of $C_{00},C_{11}$ is not an
assumption; it falls out of the telescoping algebra in Step 3. Isolating the $\tau_1$-pole's own
contribution to $Q_{\text{sing}}(\tau)-\overline{Q_{\text{sing}}(w)}$ and telescoping over
$\tau-\bar w$ leaves the factor $\frac1{\bar w-\tau_1}$ attached to $u_1(\tau)$; the identity
$\bar\tau_1=\tau_0$ (the two poles are conjugates of *each other*, by construction) turns that factor
into $\overline{u_0(w)}$, not $\overline{u_1(w)}$: $\frac1{\bar w-\tau_1} =
\overline{1/(w-\bar\tau_1)} = \overline{1/(w-\tau_0)} = \overline{u_0(w)}$. So the $\tau_1$-pole's own
term always lands on the *off*-diagonal $(1,0)$ slot, never on its own diagonal slot, and symmetrically
for $\tau_0$; this is exactly why the closed form in Step 3 has no $u_1(\tau)\overline{u_1(w)}$ or
$u_0(\tau)\overline{u_0(w)}$ term. This is the precise mechanism by which a mirror pair differs from two
independent one-sided negative directions (which would instead give a *diagonal* block
$\mathrm{diag}(-|\gamma_0|,-|\gamma_1|)$, signature $(0,2)$, i.e. $\kappa=2$): **a genuine mirror pair
costs exactly one negative square, not two, and this is a structural fact about the pole locations
(each pole is the conjugate of the other, not a fixed point of conjugation), not a numerical
coincidence dependent on the unknown coupling.**

## 6. THE COMPUTATION: numerical signature check

Script: `la_negative_square_numerics.py`, session scratchpad
(`C:\Users\owenp\AppData\Local\Temp\claude\c--Users-owenp-dev-zeta-function\5708f836-0dc9-46e9-96bd-2a1caa68d9b0\scratchpad\la_negative_square_numerics.py`;
not a tracked repo experiment, a one-off check for this note). [SUPERSEDED 2026-08-09: the
scratchpad path above is machine-local and the script is unrecoverable (evidence-rule
violation, flagged by [`_modular_rung_adversary.md`](_modular_rung_adversary.md) B5). The
computation is superseded at source tier by the tracked
[`e1w_burnol_bilinear.py`](../../../experiments/spectral/e1w_burnol_bilinear.py), which
computes Burnol's LITERAL bilinear extension and finds signature $(2,0)$, $\kappa(L_a) = 0$:
this note's $\kappa = 1$ was the negative-square count of the $\mathcal{F}_+$-twisted pairing,
not of the space. See [`e1w_burnol_bilinear.md`](../../../experiments/spectral/e1w_burnol_bilinear.md)
Sections 5-6 and LEARNINGS #173.] `mpmath` at 30 digits seeds the two
elementary residues; `numpy` computes eigenvalues of the resulting small Hermitian matrices. Full output
transcribed below in summary form.

**Part 1 (sanity check).** $s\cdot\Gamma(s/2)\to 2$ and $(s-1)\cdot\zeta(s)\to1$, confirmed to 9-10
correct digits at $s=10^{-9}$ (e.g. $1.99999999942\ldots$ and $1.00000000058\ldots$).

**Part 2 (toy $N_1$ mechanism check, independent of the $L_a$ model).** $q(z)=1/(z-i)$, tested on
random finite point sets of size $n=2$ to $6$ drawn from $\mathbb C^+$, 8 trials: **every trial found
exactly one negative eigenvalue**, e.g. (trial 0, $n=6$) eigenvalues
$[-3.003, 0.001, 0.027, 0.107, 1.519, 12.72]$, negative count 1; (trial 3, the minimal $n=2$ case)
eigenvalues $[-0.468, 0.094]$, negative count 1. Confirms the basic mechanism (a pole in the "wrong"
half-plane costs exactly one negative square) robustly, not just in the specific $L_a$-shaped
construction below.

**Part 3 (the closed-form check, then the actual block).** Closed-form vs. direct numerical evaluation
of $K_{\text{sing}}$ agreed over 20 random $(\rho,w,\tau)$ triples to $6\times10^{-16}$ (floating-point
noise; confirms the Step 3 algebra is correct, not just plausible). The 2×2 block was then evaluated at
$a\in\{0.1,0.5,1,2,5,10\}$ under four illustrative placeholder models for the unknown $a$-dependence of
$\rho(a)$ (`const`, `exp`, `power`, `phased`, spanning constant/decaying/oscillating-phase choices, all
seeded from the two residues $2$ and $1$ from Part 1) purely to test robustness, **not** as a claim
about Burnol's true formula:

| $a$ | model | $\rho(a)$ | eigenvalues | negative count |
|---|---|---|---|---|
| 0.1 | const | $2$ | $-2.000,\ 2.000$ | 1 |
| 0.1 | exp | $1.810$ | $-1.810,\ 1.810$ | 1 |
| 1.0 | power | $1$ | $-1.000,\ 1.000$ | 1 |
| 1.0 | phased | $0.398+0.619i$ | $-0.736,\ 0.736$ | 1 |
| 5.0 | exp | $0.0135$ | $-0.0135,\ 0.0135$ | 1 |
| 10.0 | phased | $-0.00008-0.00005i$ | $-0.0001,\ 0.0001$ | 1 |

All 24 cells (6 values of $a$ times 4 models) gave negative count exactly 1. (Full table in the script
output.) As Section 5 shows algebraically, this robustness is guaranteed for any nonzero $\rho$, so the
table is a confirmation, not a discovery, but it is a genuine numerical check of the hand-derived
algebra, not an assumption.

**Part 4 (rank/signature at $n>2$ generic points).** Because $K_{\text{sing}}$ has rank $\le2$
everywhere (an outer-product structure, immediate from Step 3's closed form), the prediction at $n>2$
test points is: exactly 1 negative, 1 positive, and $n-2$ numerically-zero eigenvalues. Checked at
random $n=3$ to $7$ point configurations, 5 trials, all consistent, e.g. ($n=7$, trial 0):
eigenvalues $[-1.096, {\sim}0,{\sim}0,{\sim}0,{\sim}0,{\sim}0, 0.039]$, neg $=1$, pos $=1$, zero $=5$;
($n=5$, trial 1): $[-1.563,{\sim}0,{\sim}0,{\sim}0, 1.519]$, neg $=1$, pos $=1$, zero $=3$. This is a
falsifiable prediction of the rank-2 structure that was checked, not assumed.

## 7. What is established, and what is not

**Established by this note (own derivation + numerical check, Sections 5-6).** If $L_a$'s pole
correction to $K_a$'s kernel is modeled as an additive rank-2 term built from the two elementary Cauchy
kernels at the mirror-pole locations $s=0,1$ (reflections of each other across Burnol's own real axis,
the critical line), **that local correction has negative index exactly 1, for any nonzero coupling
strength.** This is a clean, checkable, from-scratch piece of mathematics (Definition 2.1's kernel
formula, applied to an explicit rational $Q_{\text{sing}}$, verified twice: once by hand-algebra, once
numerically).

**Not established.**
1. **The additive ansatz $K_L=K_a+K_{\text{sing}}$ itself.** Burnol's own construction of $L_a$'s inner
   product (a bilinear, not sesquilinear, $L^2(0,\infty)$ pairing extended to the pole-carrying
   functions) was not translated into this reproducing-kernel language this session; the ansatz is
   structurally natural (it is exactly the shape Theorem 5.3-type constructions take throughout the K-W
   series) but unverified against Burnol's literal formulas. This is the translation step both this note
   and [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md) flag as the standing gap.
2. **Global vs. local $\kappa$.** Adding a positive-semidefinite kernel ($K_a$'s own, since $K_a$ is a
   classical, entire, positive-definite dB space by Theorem 2.1) to a rank-2 kernel with 1 negative
   square can only *decrease or preserve* the negative count relative to the perturbation alone
   (standard monotonicity of negative squares under a positive-semidefinite sum, [SECONDARY, standard
   Pontryagin-space fact traceable to Alpay-Dijksma-Rovnyak-de Snoo's reproducing-kernel-Pontryagin-space
   book, cited as [ADSR1] inside Kaltenbäck-Woracek Part I itself; not independently re-fetched
   tonight]). So $\kappa(K_L)\le 1$ follows if the ansatz holds; genericity (no exact cancellation
   between the singular part's negative direction and $K_a$'s positive background) would give equality,
   $\kappa(K_L)=1$, but this is not proven, only argued as the expected generic case.
3. **$\rho(a)\ne0$ for every $a$.** $\dim(L_a/K_a)=2$ for every $a\in(0,\infty)$ [FETCHED, Prop. 4.5,
   stated generally] shows the two evaluators are always linearly independent *as a vector space fact*,
   but this does not, by itself, rule out an isolated $a$ where the associated coupling degenerates as a
   *form* (an isotropic-vector or Jordan-block scenario). Not excluded by this note.
4. **The bilinear-vs-sesquilinear reconciliation.** Burnol's own reason for the bilinear pairing
   (Section 4, now [FETCHED] with the exact quote) is exactly the standard reason this device is used in
   reproducing-kernel theory (holomorphic, not antiholomorphic, dependence on the evaluation parameter),
   which de-risks this gap: the passage to Definition 2.1/3.1/5.1's sesquilinear convention is expected
   to be the routine one (conjugate the evaluation parameter). But the explicit substitution was not
   carried out this session; "expected to be routine" is not the same as "checked."
5. **Kaltenbäck-Woracek Parts II, III, V, VI** remain unread (only Part I was fetched and read in full
   this session); a majorant/extremal theorem specifically for small $\kappa$ (e.g. $\kappa=1$) could in
   principle live there. Part I itself, now fully read, contains none (Section 3, bonus finding).

**Grading.** Per the task's own tier vocabulary, this is **REALIZABLE-CANDIDATE, $\kappa=1$**, computed
via the mirror-pole model of Section 5, numerically confirmed in Section 6, with the five gaps above
named exactly rather than glossed over.

## 8. Verdict

**REALIZABLE-CANDIDATE ($\kappa=1$).** This is the first computation, in either direction, attempted
against the question named as open by [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md).
It supplies a small, clean, structurally-motivated candidate value, sharper than the $\kappa\le2$ prior
guess (because the two pole directions are a genuine mirror pair, not two independent negative
directions), with the derivation and numerics shown in full rather than asserted. It is explicitly
**not** a proof that Burnol's actual $L_a$, with its own literal inner product, has negative index 1;
Section 7 names exactly what more would be needed.

## 9. Consequence for the #164 closure

[`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md)'s own nearest-miss-2 finding (Section 4 of
that dossier) named **two** independent gaps standing between $L_a$ and a working
Kaltenbäck-Woracek-based repair of the #164 majorant question: (a) whether $L_a$ even instantiates the
generalized-Nevanlinna-function framework at all (an "unattempted open computation"), and (b) whether an
admissible-majorant or extremal theorem exists *anywhere* for the genuinely indefinite class
$HB_{<\infty}$ (searched directly in that dossier; not found, including in the one paper, Woracek 2011
Section 6.2, that gets closest, whose own majorant criterion is stated only for the classical subclass
$HB_0$).

**This note answers half of that, at candidate tier.** Gap (a) moves from "unattempted" to
"CANDIDATE-COMPUTED, $\kappa=1$": there is now a concrete, small, structurally-derived candidate
realization, not just an open question. Gap (b) is untouched: no majorant or extremal theorem was found
today either (Part I, now read in full, adds a confirmed zero-hit to the same search, Section 3's bonus
finding). **Per PHASE_STATE.md's own falsifiability language ("reopen conditions are exactly those
residuals resolving in the machinery's favor"), #164's closure is NOT reopened**, because reopening
needs *both* gaps resolved in the machinery's favor, and gap (b) remains firmly closed.

**What this does change:** the target for whoever next searches Kaltenbäck-Woracek Parts II, III, V,
VI (residual 1 of the BBH dossier, still open) is now sharper. The question is no longer the broad "is
there a majorant/extremal theorem anywhere for the indefinite class," but specifically: **does any
extremal or admissible-majorant theorem exist, in this series or elsewhere, posed for
$E\in HB_1$ specifically** (the smallest genuinely indefinite class, one step past the classical
$HB_0$ that Woracek 2011's own Proposition 6.8 already covers)? If Parts II/III/V/VI (or a different
paper) supply such a theorem at $\kappa=1$, it would apply directly to this note's candidate
realization, via Theorem 5.3's converse (no extra hypotheses beyond $E\in HB_1$), and #164's reopen
condition (i) would then genuinely fire. If they do not (matching the pattern found in every source
checked so far: the indefinite machinery is consistently a computational tool for classical-space
answers, never host to its own extremal theorem), the closure hardens further, now with the translation
step itself supplied and still leading nowhere.

## 10. Publications-gate note

Per the task's instruction, flagged **PUBLICATIONS-gate-candidate** with explicit caveats, not a claim
of having cleared the gate ([`PUBLICATIONS.md`](../../../PUBLICATIONS.md) Evaluation gate items 2-3):
the mirror-pole-pair mechanism (Section 5) is, as far as this session's searches found, a genuinely
computed, not-surveyed result (no source found anywhere in tonight's search, nor in the same-day BBH
dossier's own dedicated grep of Burnol's papers for "Pontryagin," "Krein-Langer," or "negative square,"
connects Burnol's Sonine-space pole data to generalized Nevanlinna theory in either direction). Against
the gate: item 2 (verification status) is **conjectural / local-model**, not "rigorous" or "numerically
validated" against the true object, per Section 7's five named gaps; item 3 (novelty) is supported by
today's searches but not by an independent, dedicated literature pass built solely to find prior art on
this exact question. **Not ready for the registry as stated; flagged so a future SURVEYOR pass knows to
run the full gate once the Section 7 gaps are narrowed, particularly gap 1 (the additive-ansatz
translation from Burnol's own bilinear pairing).**

## Handoff

1. **The precise next SURVEYOR-cheap step:** search Kaltenbäck-Woracek Parts II, III, V, VI
   specifically for a $\kappa=1$ (or any small, explicit finite $\kappa$) extremal/majorant/admissible
   theorem, now that Part I is confirmed to have none. This is residual 1 of
   [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md), narrowed by this note from "any
   indefinite class" to "specifically $HB_1$."
2. **The precise next BUILDER-depth step, if pursued:** translate Burnol's literal $L_a$ inner-product
   extension (Section 4's residue evaluators, in his own bilinear pairing) into the sesquilinear
   generalized-Nevanlinna-function language of Definition 2.1, replacing this note's additive-ansatz
   model with the real thing, and re-run Section 5's algebra against the actual coupling constant rather
   than the four illustrative placeholders in Section 6. This is the single highest-value gap to close
   (Section 7, gap 1); it would upgrade this note's candidate $\kappa=1$ toward an actual computed value
   for Burnol's true space.
3. **Do not read this note as reopening #164.** It sharpens one of the two named gaps in the corridor's
   own nearest-miss-2 finding; the other gap (no majorant theorem for any indefinite class, anywhere
   found) is independently confirmed once more here (Part I, zero hits) and remains the harder,
   load-bearing obstruction.
4. **The mirror-pair mechanism itself (Section 5) is reusable** beyond $L_a$: any construction in this
   project that produces a finite-rank pole correction to a classical dB space, where the poles are
   mirror images across the space's own structural axis (not necessarily the literal real line), can be
   checked the same way: change coordinates to put the axis at $\mathrm{Im}=0$, write the minimal
   real-symmetric singular part, and read the negative index off the resulting block's diagonal
   structure (zero diagonal, from a genuine mirror pair, means one negative square per pair; a nonzero
   diagonal, from independent same-sign-anomalous real poles, would cost one negative square *per
   anomalous pole*, i.e. more). This is a cheap, general-purpose screening tool for any future indefinite
   candidate in the project's corpus.
