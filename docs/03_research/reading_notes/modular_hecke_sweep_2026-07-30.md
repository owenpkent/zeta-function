> SALVAGED from PR #7 (branch overnight-wave-172-173, 2026-07-31) on 2026-08-26. SUPERSEDED AS
> VERDICT by main's #173 (the modular/Hecke rung: T1/T2/e1w) and #175(vi)(3); KEPT as the tracked
> evidence source for the Kurasov-Sarnak/Alon-Cohen-Vinzant D1 correction (LEARNINGS #210) and
> for its citation riders. The entry numbers cited inside this note are the BRANCH's numbering
> (its #172/#173), not main's.

# The modular/Hecke corpus sweep against the S4 spec

> SURVEYOR dossier, 2026-07-30 (overnight, unattended). Executes item (a) of "NEXT PIVOT RUNGS"
> in [`../../../TODO.md`](../../../TODO.md) and step 1 of "Next steps" in
> [`../../../PHASE_STATE.md`](../../../PHASE_STATE.md): the Cohn-Elkies / Viazovska /
> Radchenko-Viazovska corpus and the surrounding modular-forms-as-extremal-machinery
> literature, swept against the banked S4 spec.
>
> Provenance: the gap was named by the frame audit
> ([`../ccm_corridor_frame_audit.md`](../ccm_corridor_frame_audit.md) Section 2, "Absence claims
> verified in corridor vocabulary only": the corpus had ZERO repo mentions and is "precisely the
> mechanism class of the banked S4 spec"), then named again from BOTH pivot walls: e2al
> (LEARNINGS #166) found the index-only $F/V$ layer Beurling-blind with arithmetic size entering
> only at the truncation boundary, and e1q (LEARNINGS #167) found the additive lattice ALONE
> gives only conditioning mirages. Both walls point at the same missing tie: the additive lattice
> BOUND TO the multiplicative structure. That tie is what a Hecke eigenform is.
>
> Method discipline (#157): every load-bearing statement tagged [FETCHED] (read at source this
> session), [SECONDARY] (via a citing source or a search snippet), [UNVERIFIED-MEMORY] (model
> memory, not pinned this session), [REPO] (carried by an existing repo artifact), or flagged as
> this survey's own derivation. No claim is promoted across tiers. No em dashes anywhere.
>
> **This dossier proves nothing about RH.** It is a map plus a verdict.

---

## 0. PRE-REGISTERED CRITERIA (written before any search was run)

These were fixed in advance, per the tasking, so the verdict cannot drift to fit what turned up.
The target is the banked S4 spec, quoted verbatim from
[`../../../experiments/spectral/e1o_s4_carrier.md`](../../../experiments/spectral/e1o_s4_carrier.md)
Q4 (also reproduced in [`../s4_carrier_audit.md`](../s4_carrier_audit.md) Section 4 item 5):

> Produce, for each lambda, a nonzero functional device $F_\lambda$ on the carrier's log-circle
> (dim budget $\le 4\lambda^2$) with: (1) ONE-SIDEDNESS: $F_\lambda \ge \chi_{[0,L]}$ on the comb
> support; (2) CHEAP MULTIPLICITY: the vanishing/interpolation conditions at $\{k\log p\}$ of
> total order $M$ cost $o(M)$ dimensions, lambda-uniformly, well-conditioned; (3) UNIFORMITY: the
> constants in (1)-(2) independent of lambda; (4) LATTICE CLAUSE: the mechanism must nameably
> consume the additive lattice, sourced by an identity that FAILS for perturbed logs.

### 0.1 What counts as a HIT

A mechanism in the swept corpus is a HIT if it is **transferable in mechanism class**, meaning all
of the following can be asserted about it with a specific theorem citation:

- **H1 (cheap multiplicity, S4 condition 2).** The mechanism produces a SINGLE function (or an
  $o(M)$-dimensional family) satisfying $\Omega(M)$ independent-looking vanishing or interpolation
  conditions at a prescribed node set. Rank-DEFICIENCY, not a frame. (The #168 KNS finding fixes
  the polarity test: "one function per node" is the structural OPPOSITE and grades MISS.)
- **H2 (one-sidedness, S4 condition 1).** The mechanism is or contains a genuinely one-sided
  (majorant/minorant, or sign-condition-in-both-domains) extremal statement, not merely a
  two-sided interpolation identity.
- **H3 (node-set portability).** The node set is not forced to be the length spectrum of a lattice
  or a fixed arithmetic progression: either the theorem is stated for a class of node sets that
  can contain $\{k\log p\}$, or a named deformation/transfer principle exists that reaches a
  $\mathbb{Q}$-linearly independent set.
- **H4 (the tie).** The mechanism consumes BOTH the additive lattice (Poisson/theta/modular
  transformation) AND the multiplicative structure (Euler product / Hecke eigenvalue
  multiplicativity) at the SAME joint. Consuming only one is the conservation-law tariff the repo
  has now measured four times (#152, #160, #166, #167).
- **H5 (uniformity, S4 condition 3).** The mechanism comes in a family indexed by a parameter with
  constants controlled uniformly, or the literature contains the uniform version.

A **partial HIT** is H1 + H2 + H4 with H3 or H5 open. That is the tier the tasking cares about
most: a mechanism whose class is right and whose transfer is the open question.

### 0.2 What counts as a MISS

- **M1.** The mechanism is a frame / full-rank / one-function-per-node interpolation basis
  (anti-S4 polarity, the #168 verdict class).
- **M2.** The mechanism consumes only modularity/FE and never multiplicativity, so it is available
  to a non-Euler object. This is the D-H gate, below.
- **M3.** The mechanism consumes only density/counting data, so it is available to a Beurling
  system. This is the Beurling gate, below, and is pre-killed by the DMV screen
  ([`../s4_carrier_audit.md`](../s4_carrier_audit.md) Section 3).
- **M4.** The mechanism is bulk-asymptotic / statistical (Level 3 in the four-level framing), so
  it is compatible with worlds where some zero has $\beta = 0.51$ and cannot close RH by itself.
- **M5.** Already swept: the item is inside the #164 Q2 or #168 KNS sweeps with a verdict on
  record and this pass adds nothing. (Recorded, not re-litigated.)

### 0.3 What counts as a STRUCTURAL OBSTRUCTION

Strictly stronger than a MISS: a theorem (not an absence-at-search-depth) whose hypotheses or
conclusion PROVE that the mechanism class cannot be posed at $\{k\log p\}$. Acceptable shapes:

- **O1.** A rigidity theorem forcing the support of any summation-formula-type identity to be
  lattice-commensurate or to have a counting function $\{k \log p\}$ demonstrably does not have.
- **O2.** A proven density/growth constraint on admissible node sets which $\{k\log p\}$
  (counting $N(x) = \pi(e^x)(1+o(1)) \sim e^x/x$, gaps $\to 0$) violates.
- **O3.** A proven equivalence "cheap multiplicity at $\Lambda$ $\Leftrightarrow$ $\Lambda$
  commensurate", i.e. the $\mathbb{F}_q$ Frobenius avatar of e1o T4c promoted to a theorem in this
  corpus.

An obstruction is a coordinate, not a wall: per the project stance, an O-verdict tells BUILDER
which clause a candidate must break and where the escape has to live. It must be reported with
its exact hypotheses so the escape route is visible.

### 0.4 The hard gates (non-optional, from CLAUDE.md)

- **D-H gate.** A candidate mechanism must be able to FAIL for Davenport-Heilbronn (functional
  equation, no Euler product; coefficients periodic mod 5, $(1, \kappa, -\kappa, -1, 0)$,
  $\kappa \approx 0.28408$) for a nameable reason. Note in advance, so this cannot drift: D-H's
  comb is PERIODIC, hence lattice-carried, so Poisson summation and a theta transformation are
  available to it. A mechanism whose only arithmetic input is modularity/FE therefore fails this
  gate by construction.
- **Beurling gate.** A counting-side mechanism must FAIL for the density-matched Beurling control
  (Euler product, no additive lattice) for a nameable reason.
- **Four-level gate.** A mechanism that lives only at Level 3 (bulk asymptotics, statistics,
  universality) cannot close RH; if that is what a candidate is, say so explicitly.

### 0.5 Scope declared in advance

In scope: Cohn-Elkies LP bounds; Viazovska and CKMRV magic functions (dims 8, 24); universal
optimality and its interpolation formulas; Radchenko-Viazovska Fourier interpolation and its
perturbations; the sign-uncertainty corpus; dual-LP/modular-form certificate machinery;
Bondarenko-Radchenko-Seip; the crystalline-measure / Fourier-quasicrystal corpus (the natural home
of "which node sets admit a Poisson-type identity"); and the Hecke-operator question (does ANY
extremal machinery consume multiplicativity rather than modularity).

Out of scope, declared: the Fourier-optimization school applied to zeta (Carneiro-Chirre-Milinovich
and relatives) which the repo already swept at [`../s4_carrier_audit.md`](../s4_carrier_audit.md)
Section 2.4 with verdict "consumes RH BEFORE the positivity fires"; and the Christoffel /
orthogonal-polynomial corpus, which is the SIBLING rung (TODO, from #171) and is not this sweep.

---

(Sections 1 onward were written after the search; the criteria above were not edited afterwards.)

## 1. Headline verdict, stated first

**MISS on the S4 spec, with two named STRUCTURAL OBSTRUCTIONS and one repo-sentence correction.**

The one-line answer to the tasking's question ("does the modular corpus supply the additive lattice BOUND TO the multiplicative structure?"): **no, and the corpus splits along exactly the repo's two controls.** Every mechanism in it consumes either the additive lattice (Poisson / modular transformation) or a finitely generated multiplicative semigroup, never both at the same joint. The lattice branch (Cohn-Elkies, Viazovska, CKMRV, Radchenko-Viazovska, Bondarenko-Radchenko-Seip, Alfes-Kiefer-Mazac) passes the Beurling gate and FAILS the D-H gate. The multiplicative branch (Kurasov-Sarnak, Olevskii-Ulanovskii, Alon-Cohen-Vinzant) passes the D-H gate and FAILS the Beurling gate. The intersection is empty in print.

Three findings carry the weight, in order of how much they change what BUILDER should do next:

**(1) Going modular costs one of e1q's two D-H exemption legs, and only Hecke replaces it.** e1q's D-H unposability rested on two independent arguments [REPO, [`theta_s4_build_spec.md`](../theta_s4_build_spec.md) Section (c)]: **(i) AX-FORM**, the node set $\{k\log p\}$ exists as a privileged locus only because zeta has an Euler product, and **(ii) TYPE EXCLUSION**, the kernel is built around the conductor-1, trivial-character theta sum, and e1m's T2 measured that D-H's own FE is exact (defect $1.7\times10^{-30}$) while a Riemann-type conductor-1 reconstruction fails at $O(1)$ (defect $1.72$).

Leg (ii) does not survive the move to genuine modular forms. The corpus is level-flexible by construction: Radchenko-Viazovska works on the Hecke theta group $\Gamma_\theta$ (index 3 in $\mathrm{SL}_2(\mathbb Z)$, level 2) [FETCHED, arXiv:1701.00265], Cohn-Triantafillou and Zhou use $\Gamma_0(2)$ [FETCHED, arXiv:1909.04772, arXiv:2604.10914], Alfes-Kiefer-Mazac use the metaplectic group and Hilbert modular forms [FETCHED, arXiv:2405.15620]. D-H's coefficient comb is periodic mod 5, so it carries its own theta transformation at conductor 5, and a level-flexible modular mechanism has no type reason to refuse it.

Leg (i) survives, but it is an INPUT-level exemption, not a mechanism-level one: it says the builder chose prime-power nodes, not that the machinery refuses a non-Euler object. That is exactly the failure mode e2al measured on the other side of the pivot, where arithmetic size entered "ONLY through the truncation boundary, never through the operators themselves" (LEARNINGS #166). The repo's gate asks a mechanism to NAME the clause that fails for D-H; "I picked the primes" is not such a clause.

**What D-H provably lacks, and the modular corpus provably has available, is multiplicativity.** With $\kappa = 0.2840790438$: $c_2 c_3 = -0.08070090315$ against $c_6 = c_1 = 1$; $c_2 c_7 = +0.0807$ against $c_{14} = c_4 = -1$; $c_3 c_7 = -0.0807$ against $c_{21} = c_1 = 1$ (computed this session from [`../../../experiments/_shared/davenport_heilbronn.py`](../../../experiments/_shared/davenport_heilbronn.py)'s own constants; the failure is at the FIRST coprime pair, the same signature as e2al's $f_{TC}$ failure at $(2,3)$; some pairs agree by accident, e.g. $c_3c_4 = c_{12} = \kappa$). Structurally: $c$ is supported on residues coprime to 5 and is odd there, so it is a combination of the two ODD characters mod 5, $\chi$ (with $\chi(2) = i$) and $\bar\chi$; solving $a\chi + b\bar\chi = c$ gives $a = (1 - i\kappa)/2$, $b = \bar a$, so $f_{DH}(s) = a\,L(s,\chi) + \bar a\,L(s,\bar\chi)$, a non-eigen combination of two degree-1 Euler products with the same conductor 5 and the same odd gamma factor $\Gamma((s+1)/2)$ (hand-verified this session; standard, but not fetched at source, so [SECONDARY]). In modular language D-H is a non-eigenform in a two-dimensional span of eigen-objects. **Therefore: the next rung must be a HECKE rung, not merely a modular one.** A construction that consumes only modularity carries no mechanism-level D-H exclusion at all.

**(2) The corpus's own theorems say the S4 conjunction is NON-UNIFORM in the family parameter.** S4 condition (3) asks for constants uniform in $\lambda$. The modular corpus contains two independent theorems that the analogous conjunction fails as its parameter grows. Mallows-Odlyzko-Sloane 1975: the unique modular form with the prescribed vanishing (the hypothetical extremal theta series) acquires a NEGATIVE coefficient once the weight is large enough, so extremal lattices do not exist in large dimensions [SECONDARY, J. Algebra 36 (1975) 68-76, via multiple citing sources; original not fetched]. Zhou 2026: the first of three independent necessary conditions for Cohn-Elkies LP sharpness is $\dim S_{d/2}(\mathrm{SL}_2(\mathbb Z)) \le 1$, which "rules out all $d \ge 48$", with a $\Gamma_0(2)$ cusp-form obstruction killing $d = 16, 32$ [FETCHED abstract, arXiv:2604.10914, preprint tier]. Read together: cheap multiplicity (condition 2) is purchased by RIGIDITY of the modular space, one-sidedness (condition 1) is purchased separately, and their conjunction survives at exactly two parameter values above dimension 2. The corpus's mechanism is not a family; it is a coincidence at two points, and the corpus knows it.

**(3) A repo sentence needs correcting: the additive lattice is NOT the only known glue across incommensurable circles.** [`e1o_s4_carrier.md`](../../../experiments/spectral/e1o_s4_carrier.md) Q3 (and #153, #162, and the S4 spec's clause 4) state that "the only KNOWN structure that ties incommensurable circles together is the additive lattice (integer counting $x + O(1)$ / Poisson)". Kurasov-Sarnak (J. Math. Phys. 61 (2020) 083501, arXiv:2004.05678) construct, for ARBITRARY real $b_1, \dots, b_n > 1$ (no integrality, no commensurability), a positive Fourier quasicrystal whose spectrum is $L_+ = \{m_1\xi_1 + \cdots + m_n\xi_n\} \setminus \{0\}$ with $\xi_j = \ln b_j$, and whose support is $\{\gamma : F(i\gamma) = 0\}$ for $F(s) = P(b_1^{-s},\dots,b_n^{-s})$ [FETCHED, ar5iv]. That is a genuine node-tied summation identity at a $\mathbb{Q}$-linearly independent frequency set, sourced by Lee-Yang stability of $P$, not by any lattice. **The verdict survives; the stated reason does not.** The correct sentence is: there are exactly TWO known glues, the additive lattice and Lee-Yang stability of a multivariate polynomial, and the second one is Beurling-generic by its own hypotheses (Section 7), which is why it cannot be the S4 mechanism. This also partially falsifies the #164 Q2 claim that "every explicit, named-author interpolation or summation identity found is lattice-, modular-, or functional-equation-tied": true of the interpolation corpus that survey searched, false of the crystalline-measure corpus it did not. Logged as Discrepancy D1 (Section 10).

## 2. What was already on record (this is not a re-litigation)

The frame audit's "ZERO repo mentions" claim was true when made and is now partly stale. State of prior coverage before this sweep, so nothing here is double-counted:

| Prior artifact | What it already covered | What it left open |
|---|---|---|
| [`../s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Q2 (LEARNINGS #164) | Radchenko-Viazovska, Cohn-Elkies, Viazovska, CKMRV, Ramos-Sousa, Bondarenko-Radchenko-Seip, Kulikov-Nazarov-Sodin, at abstract/theorem-hypothesis tier. Verdict MIXED: all lattice/modular/FE-tied; KNS the one density-only escape | The MECHANISM level (what the magic function actually does), the crystalline-measure corpus, the Hecke question, the D-H gate applied to this corpus |
| [`kns_log_growth_pin.md`](kns_log_growth_pin.md) (LEARNINGS #168) | KNS pinned: supercritical density genuinely met by $\{k\log p\}$, but the output is a full-rank FRAME, the structural opposite of collapse; DMV-pre-killed as density-only | Everything modular |
| [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md) (LEARNINGS #168) | The admissible-majorant lineage; Kaltenback-Woracek keeps $E$ entire | The de Branges classification of summation formulas (Goncalves 2023, Section 6 here) |
| [`../lateral_imports_2026_06.md`](../lateral_imports_2026_06.md) row "Fourier quasicrystals" | Kurasov-Sarnak and Alon-Cohen-Vinzant NAMED, at WATCH tier, as "the discrete-side boundary of the #80 obstruction" | Never posed against the S4 spec or against $\{k\log p\}$; the Beurling gate never applied to it |
| LEARNINGS #96 | Screened "Dyson quasicrystal" and graded it K-LEVEL4 (Level 3: moving one zero off-line leaves the pure-point diffraction support unchanged) | The Kurasov-Sarnak mechanism specifically, where crystallinity of the SPECIFIC measure is equivalent to all-zeros-real (Section 9, flagged as an observation-tier tension, not resolved here) |
| [`../../../experiments/arithmetic_geometric/e2ll_ff_crystal_cone.py`](../../../experiments/arithmetic_geometric/e2ll_ff_crystal_cone.py) header, [`../first_principles_conjecture_program.md`](../first_principles_conjecture_program.md) | "The Olevskii-Ulanovskii / BRS uniqueness technology covers uniformly-discrete spectra; the pole-sourced non-uniformly-discrete case here is outside it and needs a transfer theorem" | Goncalves arXiv:2312.11185 (Dec 2023) classifies Fourier summation formulas and its Remark 7 exhibits non-uniformly-dense spectral behaviour; this is a live update to that open core (Discrepancy D2) |

Genuinely zero prior repo mentions, confirmed by ripgrep this session: Viazovska, Cohn-Elkies, Radchenko-Viazovska (outside the four post-frame-audit dossiers and TODO/PHASE_STATE), sphere packing, Mallows-Odlyzko-Sloane, Guinand's concordance paper, Alfes-Kiefer-Mazac, Goncalves's classification, Arias de Reyna's quasicrystal note, Feigenbaum-Grabner-Hardin.

## 3. Sources, with tiers

Fetch caveat applying to the whole table: every WebFetch in this session is mediated by a summarizing model. Statements marked [FETCHED] were returned by a fetch of the named source; where the fetch returned material in quotation marks I have preserved the quotation marks, and where it paraphrased I say so. Where two fetches of the same source disagreed, I say so (BRS, Section 5).

| Source | ID | Tier | What it supplies here |
|---|---|---|---|
| Cohn, Elkies, "New upper bounds on sphere packings I", Ann. of Math. 157 (2003) 689-714 | arXiv:math/0110009 | FETCHED (ar5iv, Theorem 3.1 + proof mechanism) | The LP bound and its Poisson-summation engine |
| Viazovska, "The sphere packing problem in dimension 8", Ann. of Math. 185 (2017) 991-1015 | arXiv:1603.04246 | FETCHED (ar5iv, Theorem 1 + Theorem 3 + construction) | The magic function: sign conditions plus double zeros at $\sqrt{2n}$ |
| Cohn, Kumar, Miller, Radchenko, Viazovska, "Universal optimality of the $E_8$ and Leech lattices and interpolation formulas" | arXiv:1902.05438 | FETCHED (abstract verbatim) | The interpolation theorem at radii $\sqrt{2n}$, values AND radial derivatives |
| Radchenko, Viazovska, "Fourier interpolation on the real line", Publ. IHES 129 (2019) 51-81 | arXiv:1701.00265 | FETCHED (ar5iv, Theorem 1 + basis property) | $a_n(\sqrt m) = \delta_{nm}$: free interpolation, one function per node |
| Cohn, "From sphere packing to Fourier interpolation", Bull. AMS 61 (2024) 3-22 | arXiv:2407.14999 | FETCHED (arXiv HTML) | The conceptual account: sharp iff all omitted Poisson terms vanish; no Hecke/Euler content anywhere in the survey |
| Cohn, Goncalves, "An optimal uncertainty principle in twelve dimensions via modular forms" | arXiv:1712.04438 | FETCHED (abstract) | The $+1$ sign-uncertainty extremal problem, solved by modular forms; $r_1 r_2 \ge 2$ |
| Cohn, Triantafillou, "Dual linear programming bounds for sphere packing via modular forms" | arXiv:1909.04772 | FETCHED (abstract) | Modular forms produce DUAL feasible points; LP is NOT sharp in dims 12, 16, 20, 28, 32 |
| Zhou, "Cusp form dimensions, lattice uniqueness, and LP sharpness for sphere packing in dimensions 8 and 24" | arXiv:2604.10914 | FETCHED (abstract), PREPRINT tier | Three independent necessary conditions for LP sharpness; $\dim S_{d/2}(\mathrm{SL}_2(\mathbb Z)) \le 1$ rules out $d \ge 48$ |
| Feigenbaum, Grabner, Hardin, "Eigenfunctions of the Fourier transform with specified zeros" | arXiv:1907.08558 | FETCHED (abstract) | "We show that necessarily modular forms have to be used to obtain these results" |
| Bondarenko, Radchenko, Seip, "Fourier interpolation with zeros of zeta and $L$-functions", Constr. Approx. 57 (2023) 405-461 | arXiv:2005.02996 | FETCHED (ar5iv, two passes; one pass reported Section 5.3.2, a second targeted pass could NOT confirm the subsection: see Section 5) | Nodes $\{(4\pi)^{-1}\log n\}$, dual $\{i(\rho - 1/2)\}$; the additive-vs-multiplicative duality quote |
| Alfes, Kiefer, Mazac, "Measures, modular forms, and summation formulas of Poisson type", Comm. Math. Phys. 406 (2025) 137 | arXiv:2405.15620 | FETCHED (abstract) | $k$-spherical Fourier eigenmeasures CORRESPOND to modular-type transformation behaviour for the metaplectic group |
| Kurasov, Sarnak, "Stable polynomials and crystalline measures", J. Math. Phys. 61 (2020) 083501 | arXiv:2004.05678 | FETCHED (ar5iv; the raw PDF fetch failed as binary) | Positive FQ from stable pairs, arbitrary $b_j > 1$, spectrum $L_+$; the Guinand Example 4 remark |
| Olevskii, Ulanovskii, "Fourier quasicrystals with unit masses", C. R. Acad. Sci. 358 (2020) 1207-1211 | numdam 10.5802/crmath.142 | FETCHED (main theorem sentence) | Unit-mass FQ $\iff$ $\Lambda$ is the zero set of an exponential polynomial with imaginary frequencies |
| Alon, Cohen, Vinzant, "Every real-rooted exponential polynomial is the restriction of a Lee-Yang polynomial" | arXiv:2303.03201 | FETCHED (ar5iv, abstract + Corollary 1.4 verbatim) | The COMPLETE classification of $\mathbb N$-valued FQs = exactly the Kurasov-Sarnak construction |
| Lev, Olevskii, "Quasicrystals and Poisson's summation formula", Invent. Math. 200 (2015) 585-606 | arXiv:1312.6884 | FETCHED (ar5iv, Theorems 1-3) | Uniformly discrete support AND spectrum $\Rightarrow$ support inside a finite union of lattice translates |
| Goncalves, "A classification of Fourier summation formulas and crystalline measures" | arXiv:2312.11185 | FETCHED (arXiv HTML; Theorem 3 and Remark 7 summarizer-mediated) | FS-pairs classified via Hermite-Biehler $E = A - iB$ with $A/B$ almost periodic |
| Arias de Reyna, "Explicit formula and quasicrystal definition" | arXiv:2402.10604 | FETCHED (two passes, consistent), PREPRINT tier | RH $\iff$ the signed prime-comb-minus-$2\cosh(x/2)$ measure is tempered; $|\mu|([-x,x]) \sim 4e^{x/2}$; "among these Fourier quasi-crystals there are none corresponding to the zeros of the zeta function" |
| Guinand, "Concordance and the harmonic analysis of sequences", Acta Math. 101 (1959) 235-271 | (pre-arXiv) | SECONDARY (via Kurasov-Sarnak ar5iv + independent search) | Example 4, p. 264: the explicit-formula measure is crystalline but NOT a Fourier quasicrystal, even under RH |
| Mallows, Odlyzko, Sloane, "Upper bounds for modular forms, lattices and codes", J. Algebra 36 (1975) 68-76 | (pre-arXiv, not fetched) | SECONDARY (multiple citing sources) | The prescribed-vanishing modular form develops a NEGATIVE coefficient at large weight |
| Favorov, "Fourier quasicrystals and distributions with spectrum of bounded density" | arXiv:2203.06733 | SECONDARY (PDF fetch failed as binary; statement via search snippet) | Lev-Olevskii rigidity extends to relatively dense sets of BOUNDED DENSITY (not only uniformly discrete) |
| "Analogues of Fourier quasicrystals for a strip" | arXiv:2408.09563 | FETCHED (summarizer-mediated; second pin attempt failed) | The zero set of an exponential polynomial is almost periodic, in a strip, with $n(x) = cx + O(1)$ |
| Mazac, Richard, Strungaru, "On almost periodicity in crystalline measures" | arXiv:2605.23884 | FETCHED (abstract), PREPRINT tier (May 2026) | Currency check: counterexamples to Meyer/Favorov almost-periodicity conjectures; no density constraint added |
| Hariharan, Birkbeck, Lee, Ma, Mehta, Poiroux, Viazovska, "Progress in formalizing sphere packing in dimension 8" | arXiv:2604.23468 | FETCHED (abstract), PREPRINT tier | Lean formalization of the dim-8 result completed Feb 2026 (VERIFIER-relevant) |
| Shaughnessy, "Quasicrystal scattering and the Riemann hypothesis" | arXiv:2410.03673v12 | FETCHED (HTML), CLAIMED-PROOF tier | An in-corpus claimed RH proof whose load-bearing "Guess A.2" is exactly what the classification theorems exclude (Section 9.3) |

Not reached at source, and flagged as such: Meyer's PNAS 2016 "Measures with locally finite support and spectrum" (HTTP 403); Cohn's Viazovska laudatio arXiv:2207.06913 (PDF returned binary); Mallows-Odlyzko-Sloane 1975 (pre-arXiv); Nesterenko's multiplicity estimates (search snippets only, Section 8.3); Guinand 1959 (pre-arXiv, statement carried through Kurasov-Sarnak).

## 4. The mechanism inventory

Eleven distinguishable mechanisms, not eleven papers. Each is scored in Section 5.

**M-A. Cohn-Elkies LP duality.** An admissible $f: \mathbb R^n \to \mathbb R$ with $f(x) \le 0$ for $|x| \ge 1$ and $\hat f(t) \ge 0$ for all $t$ bounds the center density by $f(0)/(2^n \hat f(0))$ [FETCHED, arXiv:math/0110009 Theorem 3.1]. Engine: Poisson summation over a lattice $\Lambda$, $\sum_{x \in \Lambda} f(x + v) = |\Lambda|^{-1}\sum_{t \in \Lambda^*} e^{-2\pi i \langle v, t\rangle}\hat f(t)$, plus the reduction "periodic packings come arbitrarily close to the greatest packing density" [FETCHED, same]. This is a genuinely ONE-SIDED extremal problem closed by a lattice-consuming identity: the frame audit's characterization is accurate.

**M-B. The Viazovska magic function.** [FETCHED, arXiv:1603.04246 Theorem 3, ar5iv] a radial Schwartz $g$ on $\mathbb R^8$ with $g(x) \le 0$ for $\|x\| \ge \sqrt2$, $\hat g \ge 0$ everywhere, $g(0) = \hat g(0) = 1$, and double zeros at all $\|x\|^2 = 2n$, $n \ge 1$ (simple at $\sqrt 2$). Built from weakly holomorphic modular forms of weight $-2$ and $-4$ plus a quasimodular $\phi_0$ involving $j$, $E_2$, $E_4$, $E_6$, combined by a Laplace-type transform $a(x) = \int \phi_0(\cdot)\, e^{\pi i \|x\|^2 z}\,dz$. **This is the corpus's one genuine cheap-multiplicity object**: ONE function meeting infinitely many double-vanishing conditions. The node set is not chosen: Cohn's survey states the sharpness criterion as "we obtain a sharp bound if and only if all these omitted terms vanish", i.e. $f$ must vanish at every nonzero vector length of $\Lambda$ and $\hat f$ at every nonzero length of $\Lambda^*$ [FETCHED, arXiv:2407.14999].

**M-C. Radchenko-Viazovska free interpolation.** Even Schwartz $f$ on $\mathbb R$ satisfies $f(x) = \sum_{n\ge0} a_n(x) f(\sqrt n) + \sum_{n\ge0}\hat a_n(x)\hat f(\sqrt n)$, with $a_n(\sqrt m) = \delta_{nm}$ for $n \ge 1$; the $a_n$ come from weakly holomorphic modular forms of weight $3/2$ for the Hecke theta group $\Gamma_\theta$ [FETCHED, arXiv:1701.00265, Theorem 1 and the basis property]. CKMRV extends this to values and radial derivatives at $\sqrt{2n}$ in $\mathbb R^8$/$\mathbb R^{24}$ [FETCHED abstract, arXiv:1902.05438].

**M-D. Bondarenko-Radchenko-Seip zeta-zero interpolation.** Nodes $\Lambda = \{(4\pi)^{-1}\log n : n \in \mathbb N\}$ and dual $M = \{i(\rho - 1/2)\}$ over the nontrivial zeros [SECONDARY, via search; FETCHED for the formula shape via ar5iv]. Load-bearing input: the functional equation, explicitly not the Euler product, in the authors' own words (Section 5).

**M-E. Alfes-Kiefer-Mazac correspondence.** "Fourier eigenmeasures supported on spheres with radii given by a locally finite sequence, which we call $k$-spherical measures, correspond to Fourier series exhibiting a modular-type transformation behaviour with respect to the metaplectic group" [FETCHED abstract, arXiv:2405.15620]. Recovers Cohn-Goncalves, Lev-Reti and Meyer formulas; extends via Hilbert modular forms. This is the corpus's own statement that Poisson-type summation formulas on a radius sequence and metaplectic modularity are THE SAME THING.

**M-F. The sign-uncertainty family.** Bourgain-Clozel-Kahane $+1$ uncertainty, optimal in dim 12 via Viazovska-type modular forms and the existence of $E_6$; $r_1 r_2 \ge 2$ [FETCHED abstract, arXiv:1712.04438]. Same engine as M-B, different functional.

**M-G. Extremal modular forms (Mallows-Odlyzko-Sloane).** Prescribe vanishing of the first $\lfloor n/24 \rfloor$ nontrivial coefficients of a weight-$n/2$ form; the space has dimension $\lfloor k/12\rfloor + 1$, so the form is unique and computable; MOS show that for $n$ large it has a NEGATIVE coefficient, so no extremal lattice exists [SECONDARY]. **This is the corpus's closest structural cousin of Stepanov**: a dimension budget bought against a vanishing order, with the arithmetic conclusion read off the residual coefficient.

**M-H. Dual-LP obstructions (Cohn-Triantafillou; Zhou).** Modular forms produce DUAL feasible points, proving LP is NOT sharp in dims 12, 16, 20, 28, 32 [FETCHED abstract, arXiv:1909.04772]; Zhou packages three necessary conditions, the first being $\dim S_{d/2}(\mathrm{SL}_2(\mathbb Z)) \le 1$ [FETCHED abstract, arXiv:2604.10914]. The obstruction side of the same machinery.

**M-I. Kurasov-Sarnak stable-polynomial Fourier quasicrystals.** For a stable pair $(P, Q)$ with $Q(z) = \eta z_1^{\ell_1}\cdots z_n^{\ell_n} P^\iota(z)$ and arbitrary reals $b_1, \dots, b_n > 1$, set $F(s) = P(b_1^{-s}, \dots, b_n^{-s})$; then $\mu$ supported on $\Lambda_P = \{\gamma : F(i\gamma) = 0\}$ is a positive crystalline measure, a Fourier quasicrystal, and almost periodic, with $\mathrm{spec}(\hat\mu) \subseteq L_+ \cup -L_+ \cup \{0\}$, $L_+ = \{m_1\xi_1 + \cdots + m_n\xi_n\}\setminus\{0\}$, $\xi_j = \ln b_j$ [FETCHED, ar5iv arXiv:2004.05678, Theorem 1]. Note the shape: a self-inversive (functional-equation-like) condition on $P$, a finitely generated multiplicative semigroup of "primes" $b_j$, and a stability (Lee-Yang) condition that puts every zero of $F$ on the line $\mathrm{Re}(s) = 0$.

**M-J. The FQ classification (Olevskii-Ulanovskii; Alon-Cohen-Vinzant; Lev-Olevskii).** Unit-mass FQ $\iff$ $\Lambda$ is the zero set of an exponential polynomial with imaginary frequencies [FETCHED, numdam]. ACV Corollary 1.4 verbatim: "A measure $\mu$ on $\mathbb R$ is an $\mathbb N$-valued Fourier quasicrystal if and only if $\mu = \mu_{p,\ell}$, for some Lee-Yang polynomial $p(z_1,\dots,z_n)$ and positive frequencies $\ell \in \mathbb R_+^n$" [FETCHED, ar5iv arXiv:2303.03201]. Lev-Olevskii Theorem 1: uniformly discrete support with all atoms nonzero and uniformly discrete spectrum forces the support into a finite union of lattice translates [FETCHED, ar5iv arXiv:1312.6884].

**M-K. The Hermite-Biehler classification of summation formulas (Goncalves).** "We completely classify Fourier summation formulas, and in particular, all crystalline measures with quadratic decay", using "almost periodic functions, Hermite-Biehler functions, de Branges spaces and Poisson representation" [FETCHED abstract, arXiv:2312.11185]. Theorem 3 (summarizer-mediated): a real-antipodal FS-pair with $\mu \ge 0$ and locally finite support arises from a Hermite-Biehler $E = A - iB$ with $A/B$ almost periodic, with $\mu = 2\pi\sum_{\phi_E(\gamma)\equiv 0\ (\mathrm{mod}\ \pi)}\phi_E'(\gamma)^{-1}\delta_\gamma$.

## 5. The mechanism scorecard against the S4 spec

H1 = cheap multiplicity (rank deficiency, not a frame). H2 = one-sidedness. H3 = node-set portability to a $\mathbb{Q}$-linearly independent set. H4 = the tie (lattice AND multiplicative structure at the same joint). H5 = uniformity in a family parameter. Y / N / partial, with the reason.

| Mechanism | H1 cheap mult. | H2 one-sided | H3 node portability | H4 the tie | H5 uniformity | Verdict |
|---|---|---|---|---|---|---|
| M-A Cohn-Elkies LP | N (a bound, not a vanishing budget) | **Y** | N (Poisson needs a lattice) | N (lattice only) | Y in $n$, but the bound is not sharp | MISS |
| M-B Viazovska magic function | **Y** (one function, all double zeros) | **Y** | N (nodes = $\Lambda$'s own length spectrum, forced by the sharpness criterion) | N (Cohn's survey: no Euler/Hecke content) | **N** (Zhou: $\dim S_{d/2}\le1$; only $d = 8, 24$) | MISS, closest class match |
| M-C RV / CKMRV interpolation | **N** (anti-polarity: $a_n(\sqrt m) = \delta_{nm}$, one function per node) | N (an identity, no sign condition) | N ($\sqrt n$ from $q$-expansion exponents) | N | partial | MISS (M1, the #168 class) |
| M-D BRS zeta interpolation | N (free interpolation basis) | N | partial (nodes are $\log n$, the right SHAPE) | **N**, authors' own words: additive duality, FE only | not addressed | MISS, and FAILS the D-H gate |
| M-E Alfes-Kiefer-Mazac | n/a (an equivalence, not a device) | n/a | **N by theorem**: radii sequence $\leftrightarrow$ metaplectic modularity | N | n/a | OBSTRUCTION (Section 8.1) |
| M-F sign uncertainty | Y (same as M-B) | **Y** | N | N | **N** (dim 12 only) | MISS |
| M-G MOS extremal forms | **Y** (vanishing bought by dimension count) | **Y** (nonneg theta coefficients) | N (coefficients indexed by $\mathbb{Z}_{\ge0}$) | partial (theta coefficients ARE multiplicative for eigenforms, but the argument never uses it) | **N by theorem** (negative coefficient at large weight) | MISS, sharpest S4 cousin |
| M-H dual LP obstructions | n/a (obstruction side) | n/a | n/a | N | **N by theorem** | OBSTRUCTION (Section 8.2) |
| M-I Kurasov-Sarnak FQ | partial (an identity at incommensurate frequencies) | **Y** (positive measure; stability = the sign input) | **Y** ($b_j > 1$ arbitrary) | **N**: multiplicative semigroup only, no lattice | N (finite $n$; a horizoned object) | PARTIAL HIT on the identity clause, FAILS the Beurling gate |
| M-J FQ classification | n/a | n/a | n/a | n/a | n/a | OBSTRUCTION (Section 8.3) |
| M-K Goncalves FS classification | n/a | n/a | n/a | n/a | n/a | OBSTRUCTION + a live update (Section 8.4, D2) |

On the 17-constraint framework: it is the Architecture-2 candidate-cohomology instrument ([`../../../experiments/arithmetic_geometric/2A_candidate_evaluation.md`](../../../experiments/arithmetic_geometric/2A_candidate_evaluation.md)) and none of the objects here is a candidate cohomology for $\mathrm{Spec}(\mathbb Z)$; scoring them against it would be a category error. The applicable instrument is the S4 spec's four conditions plus the two controls, which is what the recent S4 dossiers ([`../s4_carrier_audit.md`](../s4_carrier_audit.md), [`kns_log_growth_pin.md`](kns_log_growth_pin.md)) use, and is what is used above. Stated so the omission is visible rather than silent.

### 5.1 The BRS quote, and one honesty flag

The load-bearing sentence, as returned verbatim by an ar5iv fetch of arXiv:2005.02996:

> "Both (1.1) and (1.2) rely crucially on the functional equation ... but a principal distinction between them is that the deduction of the Riemann-Weil formula starts from the Euler product representation of $\zeta(s)$, while formula (1.2) is tied to the Dirichlet series representation of $\zeta(s)$. Hence we may think of the two formulas as expressing respectively a multiplicative and an additive duality relation between the zeta zeros and a distinguished sequence of integers."

That is the corpus saying, in its own words at its closest approach to zeta, that its interpolation formula is the ADDITIVE dual and the Riemann-Weil explicit formula is the MULTIPLICATIVE one. The repo's pivot question is precisely whether a single object can be both; BRS's own framing separates them.

**Honesty flag.** A first fetch of the same paper reported that "Section 5.3.2 explicitly addresses 'Dirichlet series without Euler products'" and that the method extends to Dedekind zeta functions and other Dirichlet series with an FE of the form $Q^{-s}\Gamma(s/2)F(s) = \overline{Q^{-(1-s)}\Gamma((1-s)/2)F(1-\bar s)}$. A second, targeted fetch could NOT confirm the subsection number or its wording. I therefore carry "BRS extends to Euler-free Dirichlet series with an FE" at [SECONDARY] tier, not [FETCHED], and the D-H gate verdict for M-D in Section 6 is stated with that dependence named. It does not change the verdict, because the verbatim quote above already establishes that the FE, not the Euler product, is the load-bearing input.

## 6. The D-H gate

The rule: a candidate must be able to FAIL for Davenport-Heilbronn (FE, no Euler product) for a nameable reason.

**6.1 The measured fact about D-H that decides this section.** D-H's coefficients are periodic mod 5 with one period $(1, \kappa, -\kappa, -1, 0)$, $\kappa = (\sqrt{10 - 2\sqrt5} - 2)/(\sqrt5 - 1) = 0.2840790438$ [REPO, [`davenport_heilbronn.py`](../../../experiments/_shared/davenport_heilbronn.py) docstring]. Two consequences, both this survey's own computation from those constants:

- **Lattice-carried.** Periodicity mod 5 means the comb lives on $\mathbb Z$; Poisson summation applies verbatim, and the associated theta series has a transformation law at conductor 5 (this is exactly the content of D-H's own FE, measured exact at defect $1.7\times10^{-30}$ in e1m T2 [REPO]).
- **Not multiplicative.** $c_2 c_3 = -0.08070090315$ vs $c_6 = 1$; $c_2 c_7 = +0.08070090315$ vs $c_{14} = -1$; $c_3 c_7 = -0.08070090315$ vs $c_{21} = 1$. Failure at the first coprime pair. (Some pairs agree by accident, e.g. $c_3 c_4 = c_{12} = \kappa$; multiplicativity fails, it does not fail everywhere.) Structurally, $f_{DH}(s) = a L(s,\chi) + \bar a L(s,\bar\chi)$ with $\chi$ the odd quartic character mod 5 and $a = (1 - i\kappa)/2$ (Section 1, finding 1; hand-verified, [SECONDARY]).

**6.2 Results.**

| Mechanism | D-H gate | Nameable reason |
|---|---|---|
| M-A, M-B, M-C, M-E, M-F (the modular branch) | **FAIL as a class, at mechanism level** | Their arithmetic input is a modular transformation law at SOME level. D-H has one (conductor 5). Nothing in these mechanisms refuses a level-5 object. Radchenko-Viazovska already works at level 2 ($\Gamma_\theta$), Cohn-Triantafillou and Zhou at $\Gamma_0(2)$, Alfes-Kiefer-Mazac metaplectically: the corpus is level-flexible by design. The AX-FORM leg (prime-power nodes need an Euler product) still excludes D-H at INPUT level, which is why the verdict is "fails at mechanism level" and not "runs identically for D-H" |
| M-D BRS | **FAIL** | Verbatim: the load-bearing input is the FE, "tied to the Dirichlet series representation", not the Euler product. D-H is a Dirichlet series with an FE. [The extension to Euler-free series carried at SECONDARY, Section 5.1] |
| M-G MOS | FAIL (as stated) | The argument is a dimension count in a space of modular forms; nothing in it distinguishes eigenforms |
| M-I Kurasov-Sarnak | **PASS** | D-H is not of the form $P(b_1^{-s},\dots,b_n^{-s})$ for a finite stable $P$ (it is not a finite Dirichlet polynomial), so the construction does not start. This is a type refusal, in the same class as e1q's, and it is honest but weak: it excludes D-H by shape, not by an arithmetic property D-H lacks |
| M-J, M-K | n/a (classification theorems, not devices) | |

**6.3 The consequence, stated as the sweep's main operational output.** e1q's type-exclusion leg does not survive the move to genuine modular forms (Section 1, finding 1); its AX-FORM leg survives but is input-level, and the repo has already ruled once (LEARNINGS #166) that arithmetic entering only at the input/truncation boundary is a diagnosis, not a mechanism. The only property in this whole corpus that D-H provably lacks is HECKE EIGENFORM MULTIPLICATIVITY. So any BUILDER rung drawn from the modular corpus must consume Hecke eigenvalues, not merely modularity, or its D-H exclusion will be carried entirely by the node-set choice. This is a sharpening of the gate, not a weakening: the pivot's own slogan ("the additive lattice bound to the multiplicative structure") is now pinned to a specific, checkable object (an eigenform) and a specific, checkable failure (D-H's non-multiplicativity at $(2,3)$, exhibited numerically in Section 6.1).

## 7. The Beurling gate

The rule: a counting-side mechanism must FAIL for the density-matched Beurling control (Euler product, no additive lattice) for a nameable reason.

| Mechanism | Beurling gate | Nameable reason |
|---|---|---|
| M-A through M-H (the modular branch) | **PASS** | Poisson summation over a lattice / a modular transformation law is unbuildable on a Beurling system: no $\mathbb Z$, no theta FE. This is exactly what e1q measured (the fake's dual identity breaks at defect $0.368$, reproducing e1m's T5 $0.37$) [REPO, LEARNINGS #167] |
| M-I Kurasov-Sarnak | **FAIL, by the theorem's own hypotheses** | The $b_j$ are arbitrary reals $> 1$. Nothing requires integrality, commensurability, or a lattice. A Beurling system with finitely many generalized primes $b_1, \dots, b_n$ is literally the theorem's input. The multiplicative semigroup $\{b_1^{m_1}\cdots b_n^{m_n}\}$ IS the generalized-integer semigroup, and $L_+ = \{\sum m_j \log b_j\}$ IS the log-generalized-integer set. The mechanism is Beurling-generic by construction |
| M-J, M-K | FAIL (they classify, and their classes contain Beurling-generic members: ACV's $\ell \in \mathbb R_+^n$ is arbitrary) | Same reason |

**7.1 The structural reading.** The corpus splits exactly along the repo's bracket. Nothing in it consumes both the lattice and the multiplicative structure at the same joint. That is the fourth independent measurement of the conservation law ([`../trojan_horse_m4.md`](../trojan_horse_m4.md): the tariff is the Euler product AND the additive lattice at the same joint), now from the extremal/interpolation side, and it is the direct answer to the question the pivot walls posed.

**7.2 The correction the Beurling gate forces on M-I's value.** M-I is a genuine, in-print, node-tied summation identity at a $\mathbb{Q}$-linearly independent frequency set. That is exactly the object [`e1o_s4_carrier.md`](../../../experiments/spectral/e1o_s4_carrier.md) Q3 says does not exist ("the only KNOWN structure that ties incommensurable circles together is the additive lattice"). It exists. It is also, for precisely the same reason it exists (it needs no lattice), pre-killed by the DMV screen ([`../s4_carrier_audit.md`](../s4_carrier_audit.md) Section 3): a mechanism whose inputs an Axiom-A($\theta > 1/2$) Beurling system possesses cannot reach any exponent below 1. So the S4 spec's clause 4 (the lattice clause is MANDATORY) is CONFIRMED, and its stated justification ("the lattice is the only glue") is REPLACED by a better one: there is a second glue, and the DMV screen kills it by name.

## 8. The structural obstructions

Four, in increasing order of how much they constrain the S4 spec.

**8.1 O-A (M-E): summation formulas on a radius sequence ARE modular transformation behaviour.** Alfes-Kiefer-Mazac's correspondence [FETCHED abstract, arXiv:2405.15620] states the equivalence, and Feigenbaum-Grabner-Hardin's abstract states the necessity directly: "We show that necessarily modular forms have to be used to obtain these results" [FETCHED, arXiv:1907.08558]. Consequence for S4: the identity clause cannot be filled by "some clever kernel"; on this side of the corpus, the identity IS a modular form, so the S4 node set must be the exponent set of a $q$-expansion transported by the relevant kernel. Under the Gaussian $e^{i\pi\tau x^2}$ that gives $\sqrt n$; under a Mellin kernel it gives $\log n$ (which is BRS). It does not give $\{k \log p\}$, because the prime powers are not the exponent set of any $q$-expansion (a $q$-expansion's exponents are an additive semigroup in $(1/N)\mathbb Z_{\ge0}$; $\{k\log p\}$ is a multiplicatively-selected SUBSET of the additive semigroup $\{\log n\}$, and selecting it is exactly what the Euler product does and modularity does not).

**8.2 O-B (M-G, M-H): the S4 conjunction is non-uniform, by two independent theorems.** MOS: the prescribed-vanishing form develops a negative coefficient at large weight [SECONDARY]. Zhou: $\dim S_{d/2}(\mathrm{SL}_2(\mathbb Z)) \le 1$ is necessary for LP sharpness and rules out all $d \ge 48$, with a $\Gamma_0(2)$ cusp-form obstruction killing $d = 16, 32$ [FETCHED abstract, preprint tier]; Cohn-Triantafillou independently prove LP is not sharp in dims 12, 16, 20, 28, 32 [FETCHED abstract]. Read against S4 condition (3): the corpus's own theorems say that cheap multiplicity and one-sidedness coexist only where the modular space is rigid, and that rigidity is a small-parameter accident. **This is the sharpest S4-specific coordinate the sweep produces**: it is not that the transfer to $\{k\log p\}$ is hard, it is that the mechanism is not lambda-uniform even in its home setting.

**8.3 O-C (M-J): the classification regime excludes $\{k\log p\}$ on the density side.** Chain of pinned facts:

1. Unit-mass FQ $\iff$ $\Lambda$ = zero set of an exponential polynomial with imaginary frequencies [FETCHED, Olevskii-Ulanovskii]; equivalently, ACV Cor. 1.4: $\mathbb N$-valued FQ $\iff$ Kurasov-Sarnak's $\mu_{p,\ell}$ [FETCHED].
2. Zero sets of exponential polynomials are almost periodic, lie in a horizontal strip, and have $n(x) = cx + O(1)$ [FETCHED via arXiv:2408.09563, summarizer-mediated, second pin failed; the underlying fact is classical (Levin, distribution of zeros of exponential sums) but is carried here at SECONDARY tier].
3. $\{k\log p\}$ has $N(x) = \pi(e^x)(1 + o(1)) \sim e^x/x$: $29.7$ at $x = 5$, $2.2\times10^3$ at $x=10$, $2.4\times10^7$ at $x=20$ (computed this session). Its gaps shrink to zero, so it is not uniformly discrete either, in the too-dense direction.
4. Lev-Olevskii's rigidity needs uniformly discrete support and spectrum [FETCHED], and extends to relatively dense sets of BOUNDED DENSITY [SECONDARY, via Favorov arXiv:2203.06733 search snippet; the PDF fetch failed].
5. The weighted prime comb has $|\mu|([-x,x]) \sim 4e^{x/2}$, so $|\mu|$ is not tempered and $\mu$ is not a Fourier quasicrystal [FETCHED, arXiv:2402.10604, preprint tier]. Kurasov-Sarnak's own remark, independently: Guinand's Example 4 (Acta Math. 101 (1959) p. 264), the explicit-formula measure, "does not give a Fourier quasicrystal, even assuming the Riemann hypothesis" [FETCHED, ar5iv arXiv:2004.05678]. Arias de Reyna: "Among these Fourier quasi-crystals there are none corresponding to the zeros of the zeta function" [FETCHED].
6. Recent work in the same corpus imposes polynomial density constraints on spectra explicitly ($\#(\Gamma \cap B(0,r)) = O(r^\rho)$), which exponential growth violates [FETCHED, arXiv:2503.19567, summarizer-mediated].

**The honest form of the obstruction.** This is NOT "a theorem proves the S4 identity cannot exist at $\{k\log p\}$." It is: **every classification theorem in the corpus has a bounded-or-polynomial-density hypothesis, and $\{k\log p\}$ violates it by an exponential margin, so the corpus contains no theorem about it, positive or negative.** The prime comb sits outside the classified regime in the too-dense direction. The one in-print object that does live there (Guinand's Example 4) is a crystalline measure but not a Fourier quasicrystal, and that distinction is where the RH content lives (Section 9.1).

**8.4 O-D (M-K): the de Branges classification of summation formulas, and a live repo update.** Goncalves classifies Fourier summation formulas via Hermite-Biehler functions, with the positive/locally-finite branch reconstructed from $E = A - iB$ with $A/B$ ALMOST PERIODIC [FETCHED, summarizer-mediated]. Two readings, both load-bearing:

- Against the corridor: this is the same $H(E)$ / Hermite-Biehler language falsifier 2 lives in (#164), and it says that the objects that produce summation formulas are governed by almost periodicity of $A/B$. Almost periodicity is a rigidity that a set with $e^x/x$ counting does not exhibit. It is the third independent arrival at the same diagnosis (#164 Section 3 already noted two: the de Branges axiom structure and the Fourier-uniqueness-pair literature).
- Against the repo's LCC open core: [`e2ll_ff_crystal_cone.py`](../../../experiments/arithmetic_geometric/e2ll_ff_crystal_cone.py) records that "the Olevskii-Ulanovskii / BRS uniqueness technology covers uniformly-discrete spectra; the pole-sourced non-uniformly-discrete case here is outside it and needs a transfer theorem". Goncalves's Remark 7 constructs an FS-pair with non-uniformly-dense spectral behaviour [FETCHED, summarizer-mediated]. That is a partial answer to a repo open core that was recorded as needing a transfer theorem. Logged as Discrepancy D2 and handed to ADVERSARY for adjudication, not resolved here.

## 9. Where the RH content actually sits in this corpus, and the four-level gate

**9.1 The crystalline / quasicrystal gap IS the RH content.** Arias de Reyna's Theorem 3: RH $\iff$ the measure $\mu = -\sum_n \frac{\Lambda(n)}{\sqrt n}(\delta_{\log n} + \delta_{-\log n}) + 2\cosh(x/2)\,dx$ is a tempered distribution [FETCHED, arXiv:2402.10604, preprint tier]. Its content is the von Koch equivalence (the signed cancellation between the prime comb and the archimedean density is $O(\sqrt x)$ iff RH) restated in distributional language; it is a translation, not a new lever, and this survey grades it as such. But the translation is informative in exactly the way the repo cares about: $|\mu|$ has mass $\sim 4e^{x/2}$ REGARDLESS of RH, so the Fourier-quasicrystal condition ($|\mu|$ tempered) is RH-BLIND, while the crystalline condition ($\mu$ tempered) is RH-EQUIVALENT. **The RH content sits precisely in the gap between $\mu$ tempered and $|\mu|$ tempered, i.e. entirely in the cancellation and not at all in the support geometry.** This is the same finding the repo has now measured three times in different clothes (#158's information-free finite reality; #170's "compactness is free exactly where it is information-free"; #171's "the density+gate-purchasable part is exactly the weightless part"), and it is a fourth independent instance from a corpus that never talks to those.

**9.2 The four-level gate.** The support-geometry half of this corpus is Level 3 by the repo's own screen: LEARNINGS #96 graded the quasicrystal/diffraction route K-LEVEL4 because the pure-point diffraction support is unchanged when one zero moves off-line. Section 9.1 sharpens WHY: the diffraction data is $|\mu|$-data, which is exactly the RH-blind half. **Stated explicitly, as the tasking requires: the Fourier-quasicrystal / diffraction reading of the primes and zeros lives at Level 3 and cannot close RH.** The Level-4 statement in the same corpus is the temperedness of the SIGNED measure, which is von Koch, which is where we already are.

**9.3 One observation-tier tension, flagged not resolved.** For a FIXED stable $P$, Kurasov-Sarnak's measure is supported on the real zeros of $F$, and stability of $P$ is EQUIVALENT to all those zeros being real. So for that mechanism, crystallinity of the specific measure is not robust to moving a zero off the line, unlike the diffraction reading #96 screened. This may mean the Kurasov-Sarnak corner is Level-4-shaped in a way the #96 screen was not testing. Against that: the repo has a standing polarity verdict retiring the entire real-stability / Lee-Yang / Lorentzian / log-concave family as wrong polarity (the M4 target is indefinite $(1, n-1)$, not all-positive; [`../breadth_program.md`](../breadth_program.md), [`../exploration_sweep_2026-06.md`](../exploration_sweep_2026-06.md), LEARNINGS #95/#76). Kurasov-Sarnak reaches "all zeros on a line" through exactly such an all-positive condition. **SURVEYOR does not adjudicate this.** It is logged as Discrepancy D3 for ADVERSARY: either the polarity verdict needs a carve-out for the $b^{-s}$ / torus-restriction setting, or the Kurasov-Sarnak corner needs the Level-3 grade the diffraction reading got, and the two cannot both stand unexamined.

## 10. Discrepancy log

**D1 (with #164 Q2 and with e1o Q3 / the S4 spec clause 4).** #164 Q2 concluded that every explicit named-author interpolation or summation identity found is lattice-, modular-, or FE-tied, and the repo repeatedly states that the additive lattice is the ONLY known glue across incommensurable circles ([`e1o_s4_carrier.md`](../../../experiments/spectral/e1o_s4_carrier.md) Q3; #153; #162). Kurasov-Sarnak (J. Math. Phys. 2020) plus the Olevskii-Ulanovskii/ACV classification give explicit, named-author, in-print summation identities at arbitrary $\mathbb{Q}$-linearly independent frequency sets, sourced by Lee-Yang stability and not by any lattice. **The verdicts built on that sentence survive** (the second glue is Beurling-generic and therefore DMV-killed, Section 7.2), **but the sentence itself is false as written and should be amended** wherever it appears. Flagged, not edited: SURVEYOR does not rewrite other dossiers' load-bearing sentences.

**D2 (with the LCC open core in [`e2ll_ff_crystal_cone.py`](../../../experiments/arithmetic_geometric/e2ll_ff_crystal_cone.py) and [`../first_principles_conjecture_program.md`](../first_principles_conjecture_program.md)).** Those record that the Olevskii-Ulanovskii / BRS uniqueness technology covers only uniformly-discrete spectra and that the non-uniformly-discrete case "needs a transfer theorem". Goncalves arXiv:2312.11185 (Dec 2023) classifies Fourier summation formulas in Hermite-Biehler / de Branges language and its Remark 7 exhibits non-uniformly-dense spectral behaviour inside the classification. Whether this is the transfer theorem the LCC core wanted, or merely an example outside the uniformly-discrete case that still does not reach the archimedean continuous part, is an ADVERSARY/BUILDER question at paper-reading depth. Not resolved here.

**D3 (internal to the repo, surfaced by this corpus).** The Kurasov-Sarnak polarity tension of Section 9.3.

**D4 (a stale-claim correction, minor).** The frame audit's "a repo-wide grep returns ZERO mentions of Cohn-Elkies, Viazovska, or sphere packing" was accurate on 2026-07-17 for those three strings, but the adjacent crystalline-measure corner was NOT at zero: [`../lateral_imports_2026_06.md`](../lateral_imports_2026_06.md) (2026-06-10) already named Kurasov-Sarnak and Alon-Cohen-Vinzant at WATCH tier, and LEARNINGS #96 had screened the quasicrystal route. The audit's conclusion (the mechanism class was never swept against S4) stands; its absence claim was vocabulary-scoped in exactly the way it accused the corridor of being.

**D5 (a claimed proof in the swept corpus).** arXiv:2410.03673v12 (Shaughnessy, "Quasicrystal scattering and the Riemann hypothesis") claims RH from the assumption ("Guess A.2") that the log-prime comb is a Fourier quasicrystal [FETCHED, HTML]. That assumption is exactly what Guinand's Example 4, Kurasov-Sarnak's own remark, and Arias de Reyna's mass computation exclude (Section 8.3). Recorded so the repo does not later encounter it as a novel claim; graded CLAIMED-PROOF, load-bearing hypothesis refuted in the same corpus. Not adjudicated further.

## 11. Verdict

**Overall: MISS, with obstructions O-A through O-D and one PARTIAL HIT (M-I) that fails the Beurling gate.**

The tasking's question was whether the modular/Hecke corpus supplies the tie both pivot walls named. It does not, and the reason is structural rather than accidental: the corpus is two disjoint branches, one lattice-only (D-H-available) and one multiplicative-semigroup-only (Beurling-available), and the object the repo needs would have to be in an intersection that is empty in print. The one mechanism whose SHAPE matches S4 condition (2) exactly (Viazovska's magic function: one function, prescribed double zeros at a whole node set, sourced by an identity that fails for perturbed nodes) is provably non-uniform in its family parameter by the corpus's own theorems, and its node set is forced by the sharpness criterion to be the lattice's own length spectrum.

Framed as coordinates, per the project stance, the sweep narrows the search in four ways:

1. **The next rung must consume Hecke eigenvalues, not modularity.** Going modular without going Hecke costs e1q's type-exclusion D-H leg and leaves the exclusion resting entirely on the node-set choice, which the repo has already graded (LEARNINGS #166) as arithmetic entering at the boundary rather than through the mechanism. The checkable target is now concrete: D-H is a non-eigenform, failing multiplicativity at $(2,3)$.
2. **Lambda-uniformity is the binding clause, not node-set transfer.** Both of the corpus's obstruction theorems (MOS; Zhou/Cohn-Triantafillou) are non-uniformity statements. Any S4 candidate should be attacked at condition (3) FIRST, in its own home setting, before anyone asks about $\{k\log p\}$.
3. **The lattice clause is confirmed with a better reason.** Not "the lattice is the only glue" (false), but "the second glue is Beurling-generic and the DMV screen kills it by name".
4. **Support geometry is the RH-blind half.** The FQ condition is $|\mu|$-tempered (RH-blind); the crystalline condition is $\mu$-tempered (RH-equivalent, = von Koch). Anything in this corpus that reasons about supports, diffraction, or gap distributions is Level 3.

## 12. What this enables / what remains open

**For BUILDER.**

- **The named next rung is a HECKE rung, and it is now specifiable.** The S4-shaped question in Hecke language: does multiplicativity of eigenvalues make evaluation conditions at composite indices REDUNDANT relative to conditions at prime indices, i.e. is the evaluation map "$f \mapsto (a_f(n))_{n \le X}$" on a space of Hecke eigenforms rank-deficient relative to $\{a_f(p)\}_{p \le X}$ at cost $\pi(X) = o(X)$? Note in advance the two known counterweights: the Sturm bound says a form is determined by its coefficients up to $O(kN)$, and the eigenforms are a finite set rather than a subspace, so "rank deficiency of a linear map" may be the wrong formalization. This is exactly the formalization question e1o's Q1 flagged for the majorant skeleton, and it should be settled before code is written.
- **The M-G transplant (the sharpest Stepanov cousin).** MOS's mechanism is: a small-dimensional space, vanishing bought by dimension count, and the arithmetic conclusion read off the residual coefficient's SIGN. That is a two-sided play of exactly the Stepanov type, in the archimedean/modular world, and the repo's Stepanov audit ([`../stepanov_engine_audit.md`](../stepanov_engine_audit.md)) never met it. Worth one BUILDER read before any build.
- Do NOT build a bare-theta rung again: e1q already measured that corner and this sweep explains why it walled (a bare theta consumes the lattice only, which is the D-H-available half).

**For ADVERSARY.**

- Adjudicate D3 (the Kurasov-Sarnak vs Lee-Yang-polarity tension). This is the sharpest internal tension the sweep surfaced.
- Adjudicate D2 (does Goncalves's classification move the LCC open core?).
- Attack the D-H gate claim of Section 6.2 for the modular branch: the claim is that level-flexibility removes e1q's type exclusion. The strongest counter would be a modular mechanism that is provably conductor-1-only. If one exists, the gate verdict softens.
- Screen any future S4 candidate against condition (3) in its home setting first, per Section 11 item 2.

**For SURVEYOR (residuals this sweep could not close).**

- Meyer's PNAS 2016 "Measures with locally finite support and spectrum" (HTTP 403 this session) and Guinand's Acta Math. 1959 Example 4 at source. The Example 4 statement is currently carried through Kurasov-Sarnak.
- Mallows-Odlyzko-Sloane 1975 at source (J. Algebra 36, 68-76). The whole M-G row rests on secondary reports.
- The $n(x) = cx + O(1)$ fact for exponential-polynomial zero sets: one pin only, summarizer-mediated. It is classical, but the sweep's O-C chain uses it, so it deserves a hard citation (Levin's book, or the relevant theorem in arXiv:2408.09563 / arXiv:2307.13498).
- Nesterenko-type multiplicity estimates for modular functions: named in Section 8 as the natural "non-vanishing" half of a modular Stepanov argument, but reached only through search snippets. If the M-G transplant is pursued, this is the companion read.
- BRS Section 5.3.2 verbatim (Section 5.1's honesty flag).

**For VERIFIER.** The dimension-8 sphere-packing theorem was formalized in Lean and verified in February 2026 [FETCHED abstract, arXiv:2604.23468, authors including Viazovska]. Whatever Poisson-summation, modular-form, and LP-certificate infrastructure that project produced is the nearest existing formal substrate to anything the modular branch would need, and is worth a look before the repo builds its own.

**What remains open, stated plainly.** The pivot's forcing question is unchanged and unmoved: no object in print binds the additive lattice to the multiplicative structure at one joint in a way that yields a lambda-uniform, well-conditioned, one-sided cheap-multiplicity device at $\{k\log p\}$. This sweep did not find one, and it explains the absence better than the previous surveys did: the two halves of the tie live in two branches of the same literature, each killed by exactly one of the repo's two controls, and the corpus's own obstruction theorems say its cheap-multiplicity mechanism is not uniform even at home. **Frontier: UNMOVED.** Nothing here touches M4 or BRIDGE-H.

## 13. Cross-reference: the sibling rung landed the same night

[`christoffel_corpus_sweep_2026-07-30.md`](christoffel_corpus_sweep_2026-07-30.md) (PHASE_STATE "Next steps" item 2, the sibling named by #171) was executed by a parallel SURVEYOR in the same overnight run and reports **NO HIT, three near-misses, four obstructions**, with the structural diagnosis that every uniformity theorem in the Christoffel corpus is conditioned on the spectrum being THICK while the chain's spectrum is discrete and Lebesgue-null. Read together with this sweep, the two rungs report the same SHAPE of negative result from opposite corners: in each corpus the working theorems have a regularity/density hypothesis (thickness there, bounded-or-polynomial density here) that the arithmetic object violates on the far side, and in each corpus the arithmetic input enters at a layer below where the discrimination lives (the prefactor/Widom layer there, the node-set choice / truncation boundary here). That is a third and fourth independent arrival at the #166 diagnosis. Both cross-references are stated as observation, not as a joint claim; whether they are one phenomenon is a SYNTHESIZER question.

