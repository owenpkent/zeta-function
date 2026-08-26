# The Alpöge-Furman Lean repository, skimmed at source (zeta-23-lean, tag v1.0)

> VERIFIER skim note, 2026-08-26. Frame session F2a, executing the audit checklist minted
> by the F1 at-source verification
> ([`af_funding_inputs_verification.md`](af_funding_inputs_verification.md) Section 5) after
> the #202 confabulation was corrected on the record (LEARNINGS #208(ii)): the paper's
> Appendix A SELF-REPORT claims full coverage ("their types carry no hypotheses... the
> analytic inputs of §2 appear in the repository as theorems in their own right... no
> `axiom` declarations beyond Mathlib's... only the three standard axioms... with no
> `sorry`"), and until this session the project had verified only that claim, not the
> repository. Checklist: (a) main theorem types carry no analytic hypotheses; (b) the
> analytic inputs are theorems in their own right; (c) no sorry; (d) axioms exactly the
> three standard ones; (e) the EnclOK externality confined to the bandwidth-one ceiling
> certificate. Tier: STRUCTURAL INSPECTION (statements read, whole tree grepped, no build);
> grades are VERIFIED-BY-INSPECTION / CONTRADICTED / NOT-DETERMINABLE-WITHOUT-BUILD.
> Companion deep read: [`alpoge_furman_two_thirds.md`](alpoge_furman_two_thirds.md). No em
> dashes anywhere.

## 0. Repository identity (re-verified at source, then cloned)

Before trusting the F1 note's fetched identifiers, this skim re-extracted them
independently from the paper's LaTeX e-print (`arxiv.org/e-print/2608.13637`, file
`paper-v5-draft18.tex`, fetched 2026-08-26). All four match the F1 note exactly:

- URL, in the source: `The repository is available at \url{https://github.com/anthropics/zeta-23-lean}` (Appendix A, source line 621).
- Release identifiers, defined as macros at source lines 17-19: toolchain `v4.33.0-rc2`,
  Mathlib revision `51e6992efd06`, repository tag `v1.0` (the comment above them: "the
  only values to substitute at repository seeding").

Clone (2026-08-26, `git clone --depth 1 --branch v1.0`):

- **Tag v1.0 = commit `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`** (merge of PR #3
  "xiprime-pairceiling", dated 2026-08-10), i.e. the tag postdates the arXiv v1
  (2026-08-13) by minus three days and the formalization predates both.
- `lean-toolchain`: `leanprover/lean4:v4.33.0-rc2`. `lakefile.toml` pins Mathlib at git rev
  `51e6992efd06126df61a496bebf8f49482a4e129`; `lake-manifest.json` agrees and lists only
  the standard Mathlib dependency closure (batteries, aesop, Qq, proofwidgets, Cli,
  importGraph, LeanSearchClient, plausible). Both identifiers match the paper.
- Tree: **329 `.lean` files, about 103k lines**. `Zeta23/` 316 files / 102,265 lines, of
  which `Zeta23/FromPNTPlus/` (ported from PrimeNumberTheoremAnd, with attribution
  headers) is 16 files / 11,098 lines; `comparator/` 12 files / 784 lines. Root carries
  `README.md`, `AUDIT.md` (the "audit documentation" the paper cites), `LICENSE`/`NOTICE`
  (Apache 2.0, "Copyright (c) 2026 Anthropic, PBC"), and the lake files.
- Layout (top of `README.md`): `comparator/` = trusted statements ("START HERE");
  `Statement.lean` the counting functions; `Unconditional/Final/FinalMult` Theorems A-C;
  `ThmD/` (Montgomery-Taylor window), `ThmE/` + `ThmDE/` (Dirichlet); `LinAlg/` (§3,
  namespace `RHLinalg`); `WeilEF/`, `RvM/`, `GammaFacts/`, `Chebyshev.lean`, `MV/` (the
  analytic inputs, proved); `PrimeSideA/B`, `ZeroSide/`, `Tail/`, `Assembly/`;
  `XiPrime/` (zeros of $\xi'$) and `PairCeiling/` (the bandwidth-one ceiling), both added
  by the v1.0 amendment recorded in `AUDIT.md`.

The repository is real, substantial, self-describing, and matches the paper's Appendix A
on every identifier this skim could check without a kernel.

## 1. The checklist verdicts

### (a) Main theorem types carry no analytic hypotheses: VERIFIED-BY-INSPECTION

`Zeta23/Unconditional.lean` (billed in its header as "auditor's entry point... ONE
theorem, NO hypotheses") line 31:

```lean
theorem two_thirds_on_critical_line :
    ∀ ε > 0, ∃ T₀ : ℝ, ∀ T ≥ T₀, (2 / 3 - ε) * (Ncount T (2 * T) : ℝ) ≤ N0star T (2 * T) :=
  thmA₀
```

and likewise `two_thirds_on_critical_line_cumulative`, `half_simple_on_critical_line`,
`three_quarters_distinct`. `Zeta23/FinalMult.lean` lines 350-372: `thmB₀_mult` ($2/3$
simple and on-line), `thmC₀_mult` ($5/6$ distinct), and their `_cumulative` forms, all
with the identical quantifier-only shape. `Zeta23/ThmD/Mult.lean` line 435:
`thmD₀_simple_mult` with constant `HD 1` ($= 2 - 1/c_1^* = 0.67250...$), no hypotheses.
The types match the paper's Appendix A listing character for character (diffed against the
fetched LaTeX). The Dirichlet declarations (`ThmE/Mult.lean` lines 324/333,
`thmE_B₀_mult`, `thmE_C₀_mult`) carry `(hq : 1 < q) (hprim : χ.IsPrimitive)`: that is the
theorem's quantification over which L-function ("every primitive $\chi$ mod $q > 1$", as
stated in the paper), not an analytic input; graded conforming. The counting functions are
defined in `Zeta23/Statement.lean` directly against Mathlib's `riemannZeta` and
`analyticOrderAt` exactly as reproduced in the paper (`IsNontrivialZero`, `zeroMult`,
`zerosIn`, `Ncount`, `Ndist`, `N0`, `N0star`, `N0simple`, `Nsimple`: verbatim match), with
two proved sanity anchors tying them to Mathlib's `RiemannHypothesis`
(`RH_implies_all_on_line`) and the trivial chain.

### (b) The analytic inputs are theorems in their own right: VERIFIED-BY-INSPECTION

The architecture is a quarantine-plus-discharge ladder, and the discharge is complete:

- `Zeta23/Hypotheses.lean` defines the Prop-valued bundle `PaperInputs Z` with exactly
  five fields, each docstringed with the paper label and verbatim paper statement: `EF`
  (Weil explicit formula, [prop:EF]), `RvM` (Riemann-von Mangoldt + local count), `cheb`
  (Chebyshev-Mertens, six inequalities), `MV` ($\exists C > 0$, `MVHilbert C`), `Gamma`
  (Stirling facts for $\mu$). Its header states the principle: "There are NO Lean axiom
  declarations anywhere in this project: hypotheses are fields of the Prop-valued
  structure PaperInputs... so #print axioms stays at {propext, Classical.choice,
  Quot.sound} and the trust boundary is exactly this file."
- `Zeta23/Final.lean` then discharges the hypotheses one section at a time (four
  hypotheses, then two, then one, then none), each rung a proved theorem:
  `riemannVonMangoldt_zeta` (line 235, from the `RvM/` development: argument principle,
  Backlund via Jensen, proved Γ-facts), `gammaFacts` (`GammaFacts/Complete.lean`),
  `Cheb.chebyshevMertens` (`Chebyshev.lean`), `MV.mvDiag_thirteen : MVDiag 13`
  (`MV/Final.lean` line 27: the Montgomery-Vaughan weighted Hilbert inequality is PROVED
  in-repo with explicit constant 13 via an eigenvalue bound plus duality/polarization, not
  imported; the paper's $3\pi/2$ replaced per the stated "any absolute constant would
  suffice"), and finally `zetaEF : EF.EF_lit zetaZeroConfig` (line 288, re-exporting
  `WeilEF.EF_lit_zetaZeroConfig`, "proved from Mathlib's functional equation by contour
  integration"). Line 291: `theorem paperInputs_zeta : PaperInputs zetaZeroConfig`.
  The unconditional section header: "These are the headline statements of the
  formalization: no hypotheses at all."
- The F1 finding that AF's budget needs no zero-free region is visible here too: the
  discharge chain contains no Korobov-Vinogradov module; the prime side runs on
  Chebyshev-Mertens + MV separation, as §1.1 of the paper claims.
- `FromPNTPlus/` files carry attribution headers (upstream file, commit, license,
  modifications), matching the paper's "several are ported, with attribution, from the
  PrimeNumberTheoremAnd project".

### (c) No sorry anywhere: VERIFIED-BY-INSPECTION, with the comparator scope stated

Whole-tree grep (`grep -rn -w sorry`, all 329 files): **zero `sorry` tokens under
`Zeta23/` outside comments** (three comment-line mentions describe sorry-free porting
boundaries), and **33 `sorry` tokens, all inside the three `comparator/Challenge*` files**
(`Challenge.lean` 15, `Challenge/Multiplicity.lean` 12, `Challenge/XiPrime.lean` 6).
These are the DELIBERATE statement-only trusted files of the `leanprover/comparator`
format ("The `sorry`s are deliberate (challenge side)"): the challenge file states each
theorem with a placeholder proof, and the tool checks that the untrusted `Solution`
modules (which import `Zeta23` and contain no sorry) prove exactly those statements. The
counts match `AUDIT.md`'s recorded amendment figure (33) exactly, file by file. The
paper's "no sorry" claim is scoped to the proofs audited by `#print axioms`, which run
against the Solution side; as scoped, nothing contradicts it.

### (d) Axioms exactly the three standard ones: declaration level VERIFIED-BY-INSPECTION; kernel level NOT-DETERMINABLE-WITHOUT-BUILD

- **Declaration level (this skim's own evidence).** `grep -rn "^axiom\|axiom "` over the
  tree finds exactly two `axiom` lines, `Zeta23/FromPNTPlus/Tactic/AdditiveCombination.lean`
  183-184 (`axiom qc : ℚ`, `axiom hqc : qc = 2*qc`), and both sit INSIDE the docstring
  block of the `additive_combination` syntax declaration (block opens line 131 `/--`,
  closes line 189 `-/`; confirmed by delimiter inspection): they declare nothing.
  `AUDIT.md` says the same ("only inside a commented-out upstream test block... it
  declares nothing"). Soundness escape hatches: **no `native_decide`, no `@[extern]`, no
  `implemented_by`, no `unsafe` anywhere in the tree**; the only kernel-adjacent device is
  `decide +kernel`, used exactly twice, both in `PairCeiling`
  (`LawN256.lean:288 LawN256_check`, `Signed.lean:90 LawN256_edge`), which is
  kernel evaluation, not native code.
- **Kernel level (recorded, not re-executed).** `AUDIT.md` records verbatim
  `#print axioms` output for 27 comparator statements, 28 `Zeta23` library theorems
  (including `Zeta23.thmA₀`, `thmB₀_mult`, `thmC₀_mult`, the ThmD/ThmE/ThmDE families,
  and `lemmaR_tight`), the six $\xi'$ statements and the eleven ceiling theorems: every
  line `[propext, Classical.choice, Quot.sound]` except the two kernel checks
  (`LawN256_check` depends on `[propext]`, `LawN256_edge` on none), plus three full
  comparator runs with the independent `nanoda` kernel enabled ("Your solution is okay!",
  343/335/345 s). This skim did not re-run any of it (Section 3), so at kernel tier the
  claim's status here is: internally consistent, independently reproducible by the
  recorded commands, unverified by this project.
- One naming imprecision, for the record: the paper says `#print axioms` was run "on each
  of `Zeta23.two_thirds_on_critical_line`, `Zeta23.thmB₀_mult`, `Zeta23.thmC₀_mult`" and
  the corresponding MT/Theorem-L declarations. The audit's recorded lists contain the
  comparator-namespace `two_thirds_on_critical_line` and the library names `Zeta23.thmA₀`
  / `Zeta23.thmB₀_mult` / `Zeta23.thmC₀_mult`, but not the literal string
  `Zeta23.two_thirds_on_critical_line` (which is the one-line delegation `:= thmA₀` in
  `Unconditional.lean`, so its axiom set is necessarily identical). Substance intact;
  letter off by one delegation.

### (e) The EnclOK externality confined to the bandwidth-one ceiling: VERIFIED-BY-INSPECTION

- Definition: `Zeta23/PairCeiling/NumericCert.lean:72`,
  `def EnclOK (K : ℕ) (S : ℕ → ℝ) : ℕ → List (ℤ × ℤ) → Prop`: the list of integer
  intervals encloses $K \cdot S(j)$ in order. It is a Prop, not an axiom.
- Usage: `grep -rn EnclOK` hits ONLY `Zeta23/PairCeiling/{NumericCert, RowCert,
  CeilingLaw256, LawN256, Bridge, Signed}.lean` and
  `comparator/PrintAxioms/PairCeiling.lean`. Nothing else.
- It enters as a displayed hypothesis of the ceiling theorems, exactly as the paper says
  (`CeilingLaw256.lean:38`):

```lean
theorem ceiling_law256 (S : ℕ → ℝ) (hS : EnclOK LawN256.K S 0 LawN256.encl)
    ... (hvalid : c₀ + ∑ j ∈ Finset.Icc 1 256, massOf S 256 j * r ((j:ℝ)/256) ≤ p) :
    c₀ + ∫ x in (0:ℝ)..1, r x * x ≤ p + (82395317 : ℝ) / 10 ^ 8 * |r 1| + ...
```

  matching the paper's "under two hypotheses: hvalid... and EnclOK". The `NumericCert.lean`
  header states the externality in the repository's own words: "for a concrete law those
  [enclosures] come from an interval-arithmetic computation outside Lean and are a
  displayed hypothesis of the final statement"; the README pins the external
  exact-rational certificate by sha256. Everything downstream of the enclosures (the 255
  near-CUE row inequalities, the edge bound, the stability inequality) is kernel-checked
  via the integer checker and `decide +kernel`, "no native_decide, no extra axioms".
- Independence of the main theorems: no file outside `PairCeiling/` imports
  `Zeta23.PairCeiling.*` except the root aggregator `Zeta23.lean` (a build target list,
  not a dependency of any theorem) and the PairCeiling PrintAxioms file. In particular the
  import cones of `Unconditional.lean`, `Final.lean`, `FinalMult.lean`, `ThmD/`, `ThmE/`,
  `ThmDE/` contain no EnclOK, confirming "the formalisation of Theorems A and B is
  independent of it".

## 2. Beyond the checklist (found in the skim, consistent with the amendment)

- The repository contains MORE than Appendix A names: `Zeta23/XiPrime/` (six comparator
  statements: unconditionally at least $0.85838$ of the zeros of $\xi'$ simple and on the
  line, $0.92919$ distinct, all $\xi'$ zeros in the open strip,
  $\mathrm{Re}\,\xi'/\xi > 0$ on $\mathrm{Re}\,s \ge 1$) and the tightness theorem
  `Zeta23.ZeroSide.TightMult.lemmaR_tight` (the rank-trace certificate cannot be improved
  from its own quantities). Both arrived with the v1.0 amendment recorded in `AUDIT.md`
  (which also re-ran all checks: "lake build... 9010 jobs; no errors and no sorry
  warnings").
- The comparator trust architecture is itself a datum: trusted base =
  `ChallengeDeps.lean` (118 lines with comments, "≈60 lines of mathematics": the counting
  functions and the closed-form Montgomery-Taylor constant
  `cMT := √2·tan(1/√2)/(1 + (1/√2)·tan(1/√2))`, imported from Mathlib alone) plus the
  statement files; the README's sentence "Nothing under `Zeta23/` needs to be read to know
  *what* is proved" is accurate by the import graph.
- The paper's Mathlib-contribution sentence checks out at source: `Zeta23/LinAlg/` (von
  Neumann trace inequality, both directions of Sylvester, rank-trace, Weyl) is a
  self-contained `RHLinalg` development, "no upstream outside this project".
- `PrimeSideTemp.lean`, despite the name, is not a leftover: it is the [thm:traces]
  statement-packaging module (`TracesBounds`/`ThmTracesHyp`, Section 3 pattern P3).

## 3. Build decision: NOT ATTEMPTED, priced out

Per the skim's optional clause, a build was considered and declined: this host's elan has
toolchains v4.30.0 / v4.34.0-rc1 / v4.34.0-rc2 but NOT the pinned v4.33.0-rc2, so an
attempt would need a toolchain download, a `lake exe cache get` of the Mathlib closure
(multiple GB), and then a from-source build of the 316-module `Zeta23` cone itself
(103k lines; `AUDIT.md` records 9010 jobs; single files like `FromPNTPlus/MediumPNT.lean`
run 3.7k lines of contour analysis). That is hours, not the ~15-minute envelope; the skim
did not become a build session. Consequence, stated plainly: every kernel-tier claim in
this note (the `#print axioms` outputs, the comparator/nanoda replays, "no sorry warnings"
in the build log) is the repository's own recorded evidence, reproducible by the commands
in `AUDIT.md`, and remains unexecuted by this project.

## 4. The pattern library (for SPInterface work on finite compressions)

Six reusable statement patterns, quoted from source, chosen against the repo's own style
(`lean/ZetaRH/SPInterface.lean` packs interface + instance + refusals into one structure;
`lean/ZetaRH/S4Carrier.lean` carries a classical input as a per-theorem hypothesis).
zeta-23-lean's versions of both moves are more scalable:

**P1. The abstract-configuration seam (how the FE pairing enters).**
`Zeta23/Defs.lean:108,120`:

```lean
def reflect (ρ : ℂ) : ℂ := 1 - (starRingEnd ℂ) ρ

structure ZeroConfig where
  carrier : Set ℂ
  mult : ℂ → ℕ
  one_le_mult : ∀ ρ ∈ carrier, 1 ≤ mult ρ
  strip : ∀ ρ ∈ carrier, 0 ≤ ρ.re ∧ ρ.re ≤ 1
  reflect_mem : ∀ ρ ∈ carrier, reflect ρ ∈ carrier
  mult_reflect : ∀ ρ ∈ carrier, mult (reflect ρ) = mult ρ
  finite_window : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite
```

The functional-equation pairing $\rho \mapsto 1 - \bar\rho$ is a structure FIELD of an
abstract, arithmetic-free configuration ("they contain no arithmetic", quoting the paper's
§4 in the docstring); the whole zero side is proved at this level and instantiated twice
(ζ via `ZetaSeam`/`zetaZeros` in `Statement.lean`, Dirichlet via `LSeam`/`LZeros` in
`ThmE/Statement.lean`). For the SP interface: this is the D-H-facing move done right, the
zero-side bookkeeping poses abstractly and the instantiation carries the L-function
specifics (the F1/#208 D-H verdict lives at the instantiation, not the structure).

**P2. The hypothesis-quarantine bundle plus discharge ladder (how analytic inputs are
quarantined).** `Zeta23/Hypotheses.lean:147`:

```lean
structure PaperInputs (Z : ZeroConfig) : Prop where
  EF    : ExplicitFormulaPaper Z
  RvM   : RiemannVonMangoldt Z
  cheb  : ChebyshevMertens
  MV    : ∃ C : ℝ, 0 < C ∧ MVHilbert C
  Gamma : GammaFacts
```

One Prop structure = the entire trust boundary, each field docstringed with the paper
label, verbatim statement, literature source, and any deviation in shape; then
`Final.lean` discharges the fields one per section, ending at
`theorem paperInputs_zeta : PaperInputs zetaZeroConfig` and hypothesis-free headline
forms. The upgrade over our `S4Carrier` style (Chebyshev as a per-theorem hypothesis,
#S4C-2): the bundle names the boundary once, the ladder makes the boundary's shrinkage a
sequence of theorems, and `#print axioms` certifies the endpoint.

**P3. Conclusions-as-structure at the two-sided joint (how the trace formula is
represented).** `Zeta23/PrimeSideTemp.lean:81`:

```lean
structure TracesBounds (P : Params) (aT trG trG2 Ncnt : ℝ → ℝ) : Prop where
  tr1  : EvBound (fun T => trG T - aT T * P.L T * Ncnt T) (fun T => P.L T * Real.sqrt (P.X T))
  tr1' : EvBound (fun T => trG T - P.L T * Ncnt T) (fun T => P.calE T * (P.L T * Ncnt T))
  tr2  : EvBound (fun T => trG2 T - P.mainTr2 T) (fun T => P.calE T * P.mainTr2 T)
  ratio : EvBound ...

def ThmTracesHyp (P : Params) (Z : ZeroConfig) : Prop :=
  TracesBounds P P.a P.trGtilde P.trGtildeSq (fun T => (Z.N T (2 * T) : ℝ))
```

The trace-formula CONCLUSIONS ([eq:tr1]/[eq:tr2]/[eq:ratio]) are one Prop structure;
"`Assembly` consumes `(hTr : ThmTracesHyp P Z)`; `PrimeSideB` proves it from
`PaperInputs`". This is an SP4-shaped seam stated once and funded from one side while the
other side spends it: the exact shape a future SPInterface finite-compression module needs
for the C1 = SP2$\wedge$SP3 joint.

**P4. The finite-compression inertia core (rank-trace-index bookkeeping).**
`Zeta23/LinAlg/Inertia.lean:51` and `RankTrace.lean:163,260` (namespace `RHLinalg`,
self-contained over `ℝ` or `ℂ`):

```lean
theorem posIndex_conj_le {Q : Matrix m m 𝕜} (hQ : Q.IsHermitian) (B : Matrix m d 𝕜) :
    posIndex (isHermitian_conjTranspose_mul_mul B hQ) ≤ posIndex hQ

theorem rank_trace_ineq {P Q : Matrix n n 𝕜} (hP : P.PosSemidef) (hQ : Q.IsHermitian)
    {r b : ℕ} (hr : P.rank ≤ r) (hb : posIndex hQ ≤ b) {c : ℝ} (hc : 0 < c) :
    c * rtrace P - c ^ 2 / 4 * r + 2 * c * rtrace Q - c ^ 2 * b ≤ frobSq (P + Q)
```

Every off-line pair pays one unit of `posIndex` through pull-back (the #202 mechanism
datum, as Lean text); the same `rank_trace_ineq` instance at $c = 2$ and $c = 3$ yields
simple-zeros and distinct-zeros constants (per the README, the repo's $5/6$ route). The
`ZeroSide/` block structure is again ζ-free. Mathlib-gap note for our VerifierQueue: von
Neumann's trace inequality and two-directional Sylvester are here, new, and upstreamable;
if they land in Mathlib our `ArithmeticPolarization`/inertia lemmas should cite them
rather than re-prove.

**P5. The statement-vs-proof trust split (the comparator layer).** Trusted:
`ChallengeDeps.lean` (definitions from Mathlib alone, no `Zeta23` import) +
`Challenge*.lean` (statements with deliberate `sorry`). Untrusted: `Solution*.lean`
(one-line delegations into the library). An external tool re-checks statement equality,
axiom audit, and kernel replay (optionally in a second, independent kernel). For this
repo's publications gate: a P-item's citable surface could be exactly such a
statement-only trusted file, with our library as the untrusted side; it converts "read
103k lines" into "read 118".

**P6. The external-numerics quarantine (EnclOK).** Numerical certification enters as (i)
a Prop hypothesis over EXACT integer data (`EnclOK`, interval lists), (ii) a
kernel-decidable integer checker (`decide +kernel`, no native code), (iii) a sha256-pinned
external artifact for the enclosures, and (iv) zero import-path contact with the
unconditional theorems. If the xi-arc/P12 line ever needs a certified numeric enclosure in
Lean, this is the template.

## 5. Honest limits

- **No kernel-checked claim is made by this skim.** Structural inspection reads statement
  text and greps tokens; it does not replay proofs. Checklist items (c) and (d) at kernel
  tier rest on `AUDIT.md`'s recorded outputs (which this note quotes but did not execute);
  a future session on a machine with the toolchain can discharge them by exactly the five
  commands in `AUDIT.md`'s "How to reproduce".
- **Statement fidelity was checked where it is load-bearing, not everywhere.** The files
  read in full at the statement layer: `Statement.lean`, `Unconditional.lean`,
  `FinalMult.lean` (whole), `Hypotheses.lean` (whole), `ChallengeDeps`/README/AUDIT,
  plus targeted reads in `Final.lean`, `ThmD/ThmE` Mult, `PairCeiling`, `LinAlg`,
  `Defs.lean`, `PrimeSideTemp.lean`. The other roughly 100k lines are proof text this
  skim did not read; a malicious or accidental vacuity in a DEFINITION outside the read
  set would evade this note (mitigated, not eliminated, by the comparator design: the
  trusted statement files import nothing from `Zeta23/`).
- **Upstream trust**: Mathlib at the pinned commit, the Lean 4 release-candidate
  toolchain, the comparator tool's own assumptions, and the fidelity of the
  `FromPNTPlus/` port headers (not diffed against upstream here).
- **Provenance linkage**: the clone is whatever GitHub served for tag `v1.0` on
  2026-08-26; tags are movable. The note's hash pins what was inspected; the
  paper-to-commit linkage is the tag name plus full agreement of toolchain, Mathlib rev,
  and reproduced declaration texts.
- The external interval-arithmetic certificate behind `EnclOK` (sha256
  `cc3de991...`, "available from the authors") was not fetched; its absence is by design
  the ceiling theorems' displayed hypothesis, not a gap in Theorems A-E.

## 6. Verdict against the paper's Appendix A self-report

The self-report survives the skim intact, and the one prior repo-side doubt is now
resolved in the paper's favor at the tier a skim can reach. All five checklist items came
back VERIFIED-BY-INSPECTION at the structural tier (with (c)/(d)'s kernel halves
explicitly deferred to a build this skim deliberately did not run): the headline types for
Theorems A/B/C and the Montgomery-Taylor and Dirichlet families carry no analytic
hypotheses and match the paper's reproduced listings verbatim; the five analytic inputs
are a named Prop bundle discharged field by field into proved theorems, ending at
`paperInputs_zeta`, with Montgomery-Vaughan proved rather than imported and no zero-free
region anywhere in the chain (the F1 finding, visible in the import graph); the tree's
only `sorry` tokens are the 33 deliberate comparator-challenge placeholders; the only
`axiom` strings sit inside a ported docstring and declare nothing, with no
native_decide/extern/unsafe anywhere; and `EnclOK` is a displayed hypothesis confined to
`PairCeiling/` with no import path into the main theorems. The repository moreover
exceeds its own Appendix A (XiPrime, `lemmaR_tight`) and ships an audit file whose counts
this skim reproduced exactly where it could (33/15/12/6; the comment-only axiom;
the confinement claims). What the project has now verified: the paper's claim about its
repository AND the repository's source-level conformance to that claim. What it still has
not: a kernel replay under this project's own hands. LEARNINGS #202/#208's renamed
surface ("the paper's self-report vs the unaudited repository") should be re-renamed
accordingly: the repository is now audited at skim tier, and the residual is exactly one
`lake build` plus five `#print axioms` commands on a machine willing to pay for the
toolchain.
