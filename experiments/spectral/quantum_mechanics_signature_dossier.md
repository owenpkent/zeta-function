# The quantum-mechanics / spectral approach to RH: does it reach the signature?

> Overnight multi-agent run, 2026-06-23. Architecture 1 (spectral / Hilbert-Polya), pursued
> through the *quantum mechanics* literature specifically. Four agents (SURVEYOR, two BUILDERs,
> ADVERSARY) brought the literature current, stress-tested the one open construction question
> (does modular/KMS positivity reach the RH signature?), ran the one buildable experiment the
> project had skipped, and adversarially verified every load-bearing claim before it landed here.
>
> Raw agent artifacts: `scratchpad/overnight_qm/{01_surveyor,02_builder_modular_positivity,03_experiment_results,04_adversary_killtest}.md`.

## Bottom line (read this first)

**Everything in the QM/spectral corpus realizes zeta but does not deliver the signature**, and the
corpus splits exactly along the project's K2 firewall. This is the **sixth independent all-roads
confirmation**, now from the operator-algebra / quantum-mechanics direction. It is a confirmation of
the realization-vs-signature thesis, not a refutation, and it sharpens *where* the wall is without
moving it.

Three things are genuinely new from this run (the rest confirms and sharpens existing `#99`-`#104`):

1. **Literature currency.** The repo's Connes review predated the entire Connes-Consani prolate /
   semilocal program (2019-2025) and never recorded Bender-Brody-Muller (2017). Both are now surveyed
   and scored. The single most important datum: Connes-Consani have **published a theorem** proving a
   Weil-positivity fragment, but **only at the archimedean place** (arXiv:2006.13771, Selecta Math.) -
   the Gamma-factor half that **D-H shares and is therefore RH-agnostic**. The literature has caught
   up to the project's K2 prediction with a published theorem: the one provable positivity sits
   exactly on the K2-blind half.
2. **Bender-Brody-Muller is a textbook K1/R3.5 wall**, proved two independent ways (quasi-Hermiticity
   equivalence + Bellissard's operator-existence obstruction). New: the repo never had a BBM entry.
3. **The skipped experiment ran (`e1d`) and returned an honest NULL**: injecting arithmetic content
   `{log p}` as an *additive* potential/kernel does NOT break the zeta-vs-D-H symmetry that 1A/1B/1C
   could not break. Arithmetic must enter the **geometry** (per-prime Q_p structure), not as a
   perturbation of the dilation generator.

The one live thread worth tracking: the **2024 semilocal prolate operator** (Connes-Consani-Moscovici,
arXiv:2310.18423). It is the only QM object that injects Euler-product content on the **Frobenius
side** and writes down an explicit positivity *strategy*. Its positivity is **a program, not a
theorem**, with a standing K1 risk - but the door is genuinely **ajar** (R3.5 leaves
intersection-theoretic positivity open by construction), not closed.

> **Dug into (2026-06-24); see the dedicated dossier [`../../docs/03_research/ccm_semilocal_prolate.md`](../../docs/03_research/ccm_semilocal_prolate.md) and LEARNINGS #114.** Refined verdict: the terminal object is M4, but the operator-algebra framing **factors** the road through a genuinely-different, separately-attackable sub-problem (construct the deferred self-adjoint operator $W_{\lambda,S}$; identify its negative eigenspace = the Sonin space) before reaching the M4 core (the $S\to\infty$ uniform domination). R3.5 status sharpens from "K1 risk" to **conditionally escaping**: the archimedean fragment *proves* the sign can be geometric (the $\rho{=}1$ jump + Sonin projection, not zeros), so escape-vs-K1 turns on one bit -- whether $W_{\lambda,S}$ admits a **zero-free** construction. A cheap density surrogate ([`e1f`](e1f_ccm_semilocal_prolate.py)) reproduces the archimedean sign-source faithfully but *cannot* settle the semilocal question (its projection isn't idempotent, so its eigenvalues aren't spectral invariants); the BUILDER target is a *faithful* operator from the proven Hardy-Titchmarsh form, not a surrogate.

---

## 1. The consolidated scorecard

Legend: (R) realizes zeta; (S) signature/positivity (Level 4); (K1) **xx = key claim is circular**;
(K2) checkmark = injects Euler/Frobenius arithmetic that could discriminate zeta from Davenport-Heilbronn.

| Construction | (R) | (S) | (K1 circular?) | (K2 arithmetic?) | One-line open step |
|---|:--:|:--:|:--:|:--:|---|
| Berry-Keating `xp` (repo 1A) | avg | no | n/a | no | density log-wrong on fixed domain |
| Sierra-Townsend mod-BK (repo 1B) | avg | no | n/a | no | inject any L-dependence |
| **Bender-Brody-Muller 2017** (1608.03679) | formal | no | **xx canonical** | no | prove H self-adjoint = RH; blocked at operator existence (Bellissard) |
| **Sierra Rindler-Dirac** (1404.4252) | resonances | no | **xx** (tune `theta = arg zeta`) | yes (orbits = log p) | get zeros without inputting arg zeta |
| Quantum graphs (1307.6055) | density | no | n/a | no | Level-3 only; no individual zeros |
| SUSY-QM / Witten index | by constr. | no | xx (reverse-eng.) | no | Witten index is a count, not a polarization sign |
| PT / pseudo-Hermitian (general) | partial | no | **xx** (metric <=> RH) | no | construct metric independent of RH |
| Connes 1999 adele trace formula | yes | no | xx (R3.5) | yes | global Weil positivity as a theorem |
| **Connes-Moscovici prolate** (2112.05500) | UV | no | not yet | no (archimedean) | prove spec = {gamma_n^2} exactly |
| **Connes-Consani arch. positivity** (2006.13771) | yes | **proven LOCAL** | not (for the fragment) | **no - K2-blind, = D-H** | extend positivity to semilocal (primes) |
| **CCM semilocal prolate** (2310.18423) | yes | no (**strategy only**) | risk (trace-side) | **yes - Euler measure** | *prove* semilocal Weil positivity w/o zeta-input |
| Bost-Connes / KMS | yes | no | xx (carrier at Re>1) | yes | reach the `1/2<Re(s)<1` obstruction; type III_1 has no trace |
| Chiral adelic Dirac (2511.18309, 2025) | yes | no | risk (unassessed) | yes (Hecke) | a non-circular positivity; peer review |

**Reading the table.** The (S) column is almost entirely "no". The single "proven LOCAL" is
Connes-Consani's archimedean positivity, whose (K2) is "no" (D-H-shared). The single "yes-yes" on the
arithmetic (K2) side that is also live on positivity is the CCM semilocal prolate operator, whose (S)
is "strategy, not theorem" with a standing K1 risk. **There is no row with (S) proven on the
arithmetic (K2) side.** That empty cell is RH.

---

## 2. The Connes-Consani prolate / semilocal program (the serious frontier)

This lineage supersedes the repo's older `1d_connes_adele_literature.md` (built on Connes 1995/1999).
The structural verdict is unchanged (realization yes, positivity K1-blocked); the new papers should be
cited because they (a) resolve the 1A density-mismatch from the inside and (b) move the *proven*
positivity from "none" to "archimedean-only".

- **Connes-Moscovici, prolate spheroidal operator** (arXiv:2112.05500, PNAS 2022). A genuine
  self-adjoint operator `W_sa` (the unique Fourier-commuting, Sonin-boundary self-adjoint extension of
  the prolate Sturm-Liouville operator) whose negative eigenvalues reproduce the **UV behavior of the
  squares of the zeta zeros**, with a Dirac square root `2D` whose counting function is the
  Riemann-von Mangoldt count `N(E) ~ (E/2pi)(log(E/2pi) - 1)`. This is the first operator whose
  *intrinsic* density matches the zeros' log-density - it dissolves the 1A density obstruction from
  the inside. **But:** the spectral identification is an asymptotic + numerical UV match, *not* an
  equality `spec(W_sa) = {gamma_n^2}`, and it lives at the **single archimedean place** (K2-blind).

- **Connes-Consani, Weil positivity at the archimedean place** (arXiv:2006.13771, Selecta Math. 2021).
  The one place in the entire QM literature where a Weil-positivity fragment is a **theorem, not a
  program**. The positivity comes from the geometry of the scaling representation (not from the
  zeros), so the fragment is not circular. **But it is the archimedean place only** - the Gamma-factor
  half, which D-H shares by construction (same functional equation, same Gamma-factor). It is
  RH-agnostic in exactly the project's technical sense. The literature has now confirmed, with a
  published theorem, the project's flag that the one provable positivity is on the K2-blind half.

- **Connes-Consani-Moscovici, semilocal prolate operator** (arXiv:2310.18423, Ann. Funct. Anal. 2024)
  - **the key paper.** This is the one that crosses onto the Euler-product / Frobenius side. It builds
  the semilocal adele class space `X_S = A_S / Gamma` over a finite set of places `S` containing the
  primes; the Hilbert-space **measure itself** carries the Euler factors, `dm_S(s) = |prod_{v in S}
  L_v(1/2 - is)|^2 ds`; and the semilocal prolate operator `W_{lambda,S}` has an `S`-dependent
  Jacobi-matrix representation, so the operator genuinely *sees* the primes. This is structurally
  **unbuildable for D-H** (no Euler factors => no `L_p` => different measure => different operator).
  What is **proven**: stability of the semilocal Sonin space, the canonical Hardy-Titchmarsh form.
  What is **not proven** (the authors' own words): positivity is "a tantalizing program... we
  expect"; the plan is to realize the Weil form `Q_n` as an automatically-positive self-adjoint trace,
  then *condition* by the radical of the Weil form. The word is **strategy / expect**, never "we
  prove". Per R3.5, a trace-side positivity in this framework is K1-equivalent to RH unless the
  radical-conditioning supplies a genuinely independent geometric / intersection-theoretic input.
  **This is the single piece of the QM literature to track**, and it maps directly onto M4 / the
  arithmetic Hodge standard conjecture, now wearing operator-algebra clothes.

---

## 3. Does modular / KMS (Bost-Connes) positivity reach the signature?

This was the sharp open question. **It largely re-derives and sharpens the project's prior modular
work** (`#99`-`#104`, MC.1-MC.4, experiments `e2oo`-`e2tt`, `modular_polarization_carrier.md`). The
verdict is unchanged from `#103`: **modular/KMS positivity is the easy half.** The genuinely new
contributions are the four-positivity classification and a sharper localization of the boundary.

**Why the K2 firewall pointed here.** The polarization that proves RH must ride the Frobenius /
Euler-product direction (`{log p}`), because the archimedean half is D-H-shared. Bost-Connes is the
quantum statistical system whose dynamics live on exactly that side: its Hamiltonian has energy levels
`{log n}`, its partition function is `Z(beta) = zeta(beta)`, its symmetry group is `Gal(Q^ab/Q)`, and
its phase transition is at the pole `s = 1`. The Generative Engine's transfer-search independently
re-discovered Bost-Connes at rank 7 near the M4 residual. The natural von Neumann algebra is type
III_1, so it has **no faithful normal trace** (`#99`): any positivity it carries must be *modular*
(Tomita-Takesaki), not tracial.

**The four positivities Tomita-Takesaki / KMS gives for free, and their type.** Each is genuine; none
is the signature.

| Positivity | Type | Easy (passive) / Hard (signature) | Carries the Frobenius trace t? | Indefinite? |
|---|---|---|:--:|:--:|
| Modular operator `Delta >= 0` | operator (spectral) | passive realization ("spectrum is real") | no | no |
| KMS passivity | state / comb | passive realization (= Euler product) | no (comb = Lambda(n), not t) | no |
| Araki relative entropy `>= 0` | divergence | neither; a metric | no | no |
| Falcone-Takesaki natural cone | self-dual cone | definite "polarization" | no | no (self-dual, not (1,n-1)) |

Every modular positivity is **definite** and **trace-blind**. The RH signature must be **indefinite**
`(1, n-1)` and **trace-carrying**. The modular structure also supplies the duality `J Delta J =
Delta^{-1}` (= the functional equation, verified to 4.4e-16 in `e2pp`). So it delivers realization +
duality - the easy two-thirds - for free.

**Where it stops short (three nested statements of one wall).**
- **(J carries duality, not sign.)** `J` is antilinear with `J^2 = +1`; the polarization needs a
  complex structure `C_E` with `C_E^2 = -1` (the Weil operator). `(Delta, J)` does **not determine**
  the polarization sign `C_E`; the sign is independent data the modular structure does not contain
  (`e2qq`/`#101`). [An indefinite J-twisted form is not *impossible* - the Krein/Pontryagin
  indefinite-modular construction exists in the literature - but it requires a *non-positive*
  functional, which a genuine KMS state does not provide, so it is scoped out for the BC structure as
  given, not refuted in general.]
- **(`log Delta` is trace-blind.)** The modular weight spectrum is a function of `(prime set, beta)`
  alone, independent of the trace assignment `t` (`e2ss`/`#103`: 529 weights, identical for every
  `t`). The modular structure cannot *source* the constraint `|t_p| < 2 sqrt(p)` that is local RH.
- **(The boundary is `Re(s) = 1`, as a REPRESENTATION statement - corrected.)** The
  **rigorous, formalizable kernel** is the local-factor proposition (VT-MOD-1): for the genus-1 local
  factor `L_p(s) = 1 - t p^{-s} + p^{1-2s}` **with `t` in the Hasse range `|t| <= p+1`**, the zeros
  sit on `Re(s)=1/2` iff `t^2 <= 4p`, otherwise strictly inside `1/2 < Re(s) < 1`, touching `Re(s)=1`
  only at the extreme `|t| = p+1`. (The Hasse restriction is load-bearing: without it, `p=2, t=4`
  gives a zero at `Re(s) = 1.77`.) The convergent Gibbs-sum representation of the BC carrier, and
  every operation internal to a fixed `KMS_beta` state, live at `Re(s) = beta > 1` and are therefore
  **strip-blind**.

  **Honest correction (adversary).** The headline "the carrier is blind to the off-line obstruction
  *by domain*" is an overclaim as a global impossibility statement. The partition function **is**
  zeta, whose analytic continuation *does* reach and vanish at the strip zeros (`|zeta(1/2 + 14.13i)|
  ~ 1e-7`). And the genus-1 block with variable `t` is the **function-field shadow**, not zeta's true
  local factor `(1 - p^{-s})^{-1}` (which has no zeros): strip-confinement is proven for the shadow
  and transported to zeta by analogy. Whether **any** analytic continuation of the finite-prime
  modular data reaches the critical strip is **OPEN** (the NP-1 probe below). So the modular structure
  *stops short of the signature*, but we do **not** dress that stop as a proven impossibility.

**Why this is K1 circular.** Assemble the smallest case `M = (+)_p p^{-beta} Q_p` with `Q_p` the
`C_E`-twisted genus-1 block (positive-definite iff `|t_p| < 2 sqrt(p)`). "M positive on the primitive
part" = "every `|t_p| < 2 sqrt(p)`" = local RH at every prime. The modular carrier contributes only
the `t`-independent weights and ladder; all `t`-content sits in `C_E`, which is not modular. Asserting
the positivity asserts the conclusion. This is the R3.5 no-shortcut wall (`lean/ZetaRH/R3_5.lean`).

**The D-H asymmetry is real but necessary-not-sufficient.** Bost-Connes is genuinely **unbuildable for
D-H** (no Euler product => no Hecke pair; D-H's von Mangoldt comb goes negative at `n=3` => no Gibbs
state), so it passes K2 **by type** - rare and clean among realization structures. But unbuildability
certifies the *domain* of the construction, not its *output*: it does not produce the indefinite
`t`-carrying form even for zeta. And the D-H exclusion happens at `Re(s) > 1` ("you cannot form my
Gibbs state"), while an off-line zero would have to be detected at `Re(s) = 1/2` - a region the
carrier never enters. Two different mechanisms; the second never fires.

**NP-1 (the one cheap, falsifiable probe this surfaces).** Does the type-III_1-ness at the phase
transition `beta = 1` encode any constraint that survives analytic continuation past `Re(s) = 1` into
the strip - a finite-prime "spectral shadow" of `log Delta` valid at `Re(s)` slightly below 1 that is
**not** shared with D-H? Prediction (from the firewall): no, which would upgrade the K2 split from a
qualitative statement into a convergence theorem. A surprise yes is the one crack worth chasing. This
is a question about analytic continuation of local KMS data, not a construction; either outcome is a
coordinate.

**NP-1 RESOLVED (2026-06-24, NO; LEARNINGS #112, [`e2vv_np1_modular_continuation.py`](../arithmetic_geometric/e2vv_np1_modular_continuation.py)).** The prediction holds, but it does **not** upgrade the firewall to a convergence theorem. The off-line obstruction is a $t_p$-phenomenon, and $t_p$ acts on the $C_E$ polarization phase (which flips PD$\to$indefinite exactly at $|t_p| = 2\sqrt p$, a genuine $t_p$-dependent computation), **not** on the modular carrier (a pure function of $(S, \beta, t_{\text{flow}})$ with no $t_p$ slot, `#101`). Every finite-prime Euler product is zero-free in the strip ($\min|Z_S| \in [0.124, 0.397]$ across $\tfrac12 < \mathrm{Re}(s) < 1$), so reaching the obstruction requires the infinite-prime limit $S \to$ all primes -- which **is** the M4 coupling (`#104`). So "does the finite-prime carrier continue into the strip as a $t_p$-detecting positivity" = "does the M4 coupling exist" = `#104`, restated from the continuation side. Both loopholes close on this analytic argument: the relative modular operator / Connes cocycle moves genuinely under state and $t_{\text{flow}}$ but those axes are orthogonal to $t_p$ (no $t_p$-bearing modular object exists), and the $\beta=1$ boundary leaves no finite-carrier strip shadow (the only singularity is the infinite limit). **The increment over `#104` is one sentence of sharper framing, not a new theorem.** (Honesty note: the first numerical pass dressed a no-op as a "measured" witness; the adversary caught it, and the experiment was rebuilt so the numerics genuinely support -- not "measure" -- the analytic verdict.)

---

## 4. Bender-Brody-Muller (2017) is a textbook K1/R3.5 wall

The most-cited recent "physics" attempt; the repo never recorded it. Two independent fatal problems,
both verified by the adversary from scratch.

- **Quasi-Hermiticity circularity (the K1 wall).** BBM define a non-Hermitian `H` (a similarity
  transform of `xp + px`) whose eigenfunctions are Hurwitz-zeta functions and whose eigenvalues track
  the zeros, then conjecture a metric making `H` Hermitian. By the quasi-Hermiticity theorem
  (Scholtz-Geyer-Hahne 1992, Mostafazadeh 2002), a diagonalizable operator admits a positive metric
  making it self-adjoint **iff its spectrum is real**. By BBM's own spectral identification, the
  spectrum is real **iff RH**. So "H is Hermitian in the conjectured metric" `<=>` "spectrum real"
  `<=>` RH: naming the metric **asserts** RH rather than deriving it. This is `r3_5_no_shortcut_theorem`
  in its purest spectral form.
- **Bellissard's operator-existence obstruction** (arXiv:1704.02644), re-derived: the momentum `p =
  -i d/dx` on `L^2(0, infty)` has deficiency indices `(n_+, n_-) = (1, 0)` (`e^{-x} in L^2`, `e^{+x}
  not in L^2`), so by von Neumann **no self-adjoint extension exists at all** - the premise "assume p
  is Hermitian" is false. And the eigenfunction `psi_z` is not in `L^2` at `Re(z) = 1/2` (the case
  that matters); the weighted-space fix that restores it shifts the critical line off `Re = 1/2`. A
  rigged Hilbert space can host `psi_z` distributionally but supplies neither self-adjointness nor a
  real spectrum, so the "=> RH" arrow still has no proven premise.

BBM is also Euler-blind (built from `xp`, no Euler product), so it fails K2: it cannot distinguish
zeta from D-H. It belongs on the same wall as Connes 1999 and the Lagarias-Connes Herglotz criterion -
realization plus a reversible positivity.

---

## 5. The experiment: arithmetic input as an additive potential (e1d) - honest NULL

[`e1d_arithmetic_spectral_dh.py`](e1d_arithmetic_spectral_dh.py). The closed experiments 1A/1B used
operators with no arithmetic input, so they could not distinguish zeta from D-H. The open question:
does a spectral construction *with* arithmetic input behave differently under the D-H discipline?

**The operator.** `H = H_0 + g V_arith` on `L^2(R, du)`, `u = log x`. `H_0 = -i d/du` is the scaling
(Berry-Keating) generator, exactly Hermitian. `V_arith` is a Hermitian multiplicative-convolution
kernel from the L-function's explicit-formula comb: for zeta, nodes at `u = k log p` with von-Mangoldt
weights (prime powers = Euler product); for D-H, nodes at `u = log n` with its period-5 Dirichlet
coefficients (all integers = no Euler product, the honest D-H analogue). A well-defined proxy for the
Connes adele-class-space operator; reduces to bare Berry-Keating at `g = 0`. Methodology reuses
`e1c`'s best-affine + discrimination-ratio `r = RMS_zeta / RMS_DH`.

**The numbers, and why the apparent signal is noise.** Bare `H_0`: `RMS_zeta 3.21, r 0.71`. ZETA comb
at `g=4`: `RMS_zeta` drops to **1.87**, `r` to **0.34** - which *looks* like discrimination. It is
not: three controls killed it.
- **(C1)** A **random** comb of the same richness lowers `RMS_zeta` just as much (`1.85 +/- 0.33`
  over 20 trials, re-verified by the adversary under a stricter density-matched metric - the random
  comb slightly *beats* the real one). The gain is generic perturbation richness, not arithmetic.
- **(C2)** Scrambling the von-Mangoldt weights barely moves it (`2.07`): Euler-product weights carry
  no signal.
- **(C3, the smoking gun)** The D-H-built operator still prefers zeta (`3.23 < 4.41`): neither
  operator carries L-function identity.

**Verdict: NULL.** Arithmetic input as an additive potential/kernel does **not** break the
zeta-vs-D-H symmetry; it must enter the **geometry** (per-prime Q_p structure), not as a perturbation
of the dilation generator. The null is scoped to the *additive* route (the experiment does not test,
and does not claim to kill, the geometric route). The verdict logic is falsifiable, not rigged: a
perfect spectrum would trip the escalate branch. No false positive was manufactured - the honesty
discipline held. This sharpens 1A/1B/1C by showing *where* arithmetic has to live.

---

## 6. Adversary verdicts and the corrections applied

| # | Claim | Verdict |
|---|---|---|
| 1 | Modular "convergence-domain theorem" (carrier blind by domain) | **WOUNDED** - local math survives; global framing softened (see Section 3) |
| 2 | Modular positivity is definite, never indefinite (1,n-1) | **SURVIVES** - phrasing corrected to "(Delta,J) does not determine the sign", Krein loophole scoped |
| 3 | BBM operator-existence kill (Bellissard deficiency (1,0)) | **SURVIVES** - re-derived from scratch, correct, not a strawman |
| 4 | Experiment NULL, three controls sufficient | **SURVIVES** - re-verified under stricter metric + 20 trials; no false positive |
| 5 | "No QM construction touches the signature; semilocal = strategy + K1 risk" | **SURVIVES** - guardrail: do NOT upgrade "K1 risk" to "K1 wall / killed"; the door is ajar |

All five corrections are incorporated above. The load-bearing one: the modular boundary at `Re(s)=1`
is a **representation statement plus an open continuation question (NP-1)**, not a proven
impossibility; only the local-factor proposition (with the Hasse restriction) is publishable-rigorous.
And the CCM semilocal status stays at **"strategy / K1 risk, door ajar"**, never "closed".

---

## 7. Lean handoff (VERIFIER targets)

- **VT-MOD-1** (the rigorous kernel). For `L_p(s) = 1 - t p^{-s} + p^{1-2s}`, real `t`, `p >= 2`,
  **with `|t| <= p+1`**: (a) all zeros have `Re(s)=1/2` iff `t^2 <= 4p`; (b) `L_p(s) != 0` for
  `Re(s) > 1`; (c) max real part of a zero is `< 1` for `|t| < p+1`, `= 1` at `|t| = p+1`. Extends
  `HodgeIndex.negDef_iff_hasseWeil` / `FunctionFieldRH.eigenvalue_modulus`.
- **VT-MOD-3** (BBM circularity). Formalize the quasi-Hermiticity equivalence in the R3.5 schema:
  the BBM operator is a `TraceFormulaNCG` with `Positivity F self_adjoint <-> RiemannHypothesis`,
  via the lemma "quasi-Hermitian iff real spectrum". Register as `#R35-OP-BBM`.
- **VT-MOD-4** (J carries duality, not sign). For a finite model: `J^2 = +1`, `J Delta J = Delta^{-1}`,
  but two `J`-compatible bilinear forms of opposite signature exist on a fixed primitive block - the
  modular data does not pin the polarization sign.

---

## 8. What this means for the program

The QM/spectral architecture has been brought current and the verdict is a **confirmation of the
realization-vs-signature thesis from a new corpus**, the sixth all-roads convergence. Concretely:

- **Do not build new L-function-agnostic spectral operators.** The 1A-1C / BBM / quantum-graph /
  SUSY-QM / PT family is closed (seven dead variants now, with BBM). The `e1d` null adds: even
  arithmetic-loaded *additive* operators stay Level-3.
- **The one live QM thread is the CCM semilocal prolate operator** (2310.18423): the radical-conditioning
  step of its trace-positivity strategy is the exact open crux. Whether it injects an independent
  geometric input (escapes R3.5) or is a pure trace rearrangement (K1) is the question. This *is* M4 /
  the arithmetic Hodge index in operator-algebra clothing.
- **The signature remains the one missing object**, identical across all six roads: a non-circular,
  global, trace-carrying, indefinite `(1, n-1)` polarization on the Frobenius side of `Spec(Z)`. The
  modular carrier is the most arithmetically honest *realization* of everything except that coupling,
  and the coupling is the whole signature.

Recommended integrations (done in this run): refresh pointer from `1d_connes_adele_literature.md` to
this dossier; add the `e1d` experiment and a BBM note to the spectral README; `LEARNINGS` entry #111.

---

## Provenance

Overnight run 2026-06-23, four agents. SURVEYOR (literature, web-sourced, primary sources read at
theorem-statement level). BUILDER-1 (modular/KMS positivity + BBM circularity). BUILDER-2 (the `e1d`
experiment, run in a repo `.venv`). ADVERSARY (D-H smoke test 9/9 live, every load-bearing computation
re-derived in `.venv`, steelman of the opposite verdict). Nothing here is a proof of RH; the output is
the exact shape of the gap and an up-to-date map of where the QM frontier has reached it. Honesty
discipline: the modular half consolidates prior `#99`-`#104` work and is labeled as such; the global
"blind by domain" claim was softened on adversary review; the CCM semilocal door is recorded as ajar,
not closed.
