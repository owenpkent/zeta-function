# Reading notes: Deninger, *Number Theory and Dynamical Systems on Foliated Spaces* (Liege 2001 / arXiv math.NT/0204110, 2002)

> Reference-library read-through ([`README.md`](README.md)). The sequel to the 1998
> ICM ([`Deninger-1998-ICM-Analogies-Foliated.md`](Deninger-1998-ICM-Analogies-Foliated.md)),
> written deliberately without motives. This is where the conjectural 1998 picture
> first meets a real theorem on the dynamical side: the Alvarez Lopez-Kordyukov trace
> formula (Thm 3.3, "[AK2]") for flows transversal to a one-codimensional foliation,
> and the resulting Corollary 3.5 (`Re = α/2` from `Θ = α/2 + S`, `S` skew-adjoint).
> It states sharply why the manifold setting forces `α = 0` and forbids fixed points,
> hence why laminated spaces / generalized solenoids (and ultimately the fixed-point
> trace formula of ALK 2017) are needed for number theory. It also gives a fully
> worked number-theoretic example: a CM lift of an ordinary elliptic curve over `F_p`
> realizes the construction and yields a dynamical proof of RH for `ζ_E(s)` (Thm 5.9
> + the elliptic-curve example, pp.28-29). Pages refer to the PDF in
> `references/02_deninger_program/`. Read in full: pp.1-29 (the entire body) plus the
> reference list (pp.30-32).

## One-line takeaway

For a Riemannian foliation `F` on a compact manifold with an `F`-compatible flow that
is everywhere transversal (no fixed points), Alvarez Lopez-Kordyukov prove a genuine
Lefschetz trace formula: the operator `A_φ = ∫ φ(t) φ^{t*} dt` on reduced leafwise
cohomology is trace class, and the resulting trace reproduces the closed-orbit side of
the explicit formula. The infinitesimal generator splits `Θ = α/2 + S` (`S`
skew-adjoint, `α` the conformal weight of the flow), so the `H^1`-spectrum sits on
`Re = α/2`. The catch: in the manifold setting `α = 0` (isometric flow), the wrong
weight for number fields (which need `α = 1`), and the flow has no fixed points (number
fields need `p = ∞` as a fixed point with `k ≤ -1` coefficients `Np^k`, not `±1`). That
double mismatch is the explicit motivation for laminated spaces and for ALK 2017, and
the elliptic-curve example shows that when both are supplied (a solenoid over a CM
lift, `α = 1`), the dynamical RH proof actually goes through.

## Technical content (section by section)

**Sect. 2 (pp.2-9): foliations, leafwise cohomology, and the leafwise Hodge package.**
A `d`-dimensional foliation `F` on a smooth `a`-manifold `X` (locally `R^d × R^{a-d}`),
example: irrational-slope lines on `T^2` (dense leaves). Leafwise forms
`A^n_F(X) = Γ(X, Λ^n T^*F)`, leafwise differential `d_F`, leafwise cohomology
`H^n_F = ker d_F^n / im d_F^{n-1}`, and (for the program) the **reduced** leafwise
cohomology `H-bar^n_F(X) = ker d_F^n / closure(im d_F^{n-1})` -- a nuclear Frechet
space, infinite-dimensional already for `H-bar^1` even with dense leaves. The Poincare
lemma gives `H^n_F(X) = H^n(X, R)` for the sheaf `R` of leafwise-locally-constant
functions; `H-bar^0_F = H^0(X,R) = R` for a dense leaf; `H^n_F = 0` for `n > d`. Cup
product makes `H-bar^*_F` a graded-commutative `H-bar^0_F`-algebra. A flow `φ^t` is
`F`-compatible if `φ^t` maps leaves into leaves, inducing `φ^{t*}` on `H-bar^n_F` with
generator `Θ = lim_{t→0} (φ^{t*} - 1)/t`, an `R`-linear derivation (`Θ(h1 ∪ h2) =
Θh1 ∪ h2 + h1 ∪ Θh2`, formula (1)).
- **The leafwise Hodge theorem (Property (2), p.5).** For a Riemannian `F` (bundle-like
  metric `g`) with oriented `TF`, the inner product `(α,β) = ∫_X <α,β>_F vol`, the
  leafwise Laplacian `Δ_F = d_F d_F^* + d_F^* d_F` (whose restriction to a leaf is the
  leaf Laplacian, [AKI] Lemma 3.2), and the Hodge `*_F: Λ^n T^*F → Λ^{d-n} T^*F` give a
  topological isomorphism `ker Δ_F^n ≅ H-bar^n_F(X)` (inverse `H`). **This is deep:**
  `Δ_F` is only elliptic ALONG the leaves, so ordinary elliptic regularity fails; for
  non-Riemannian `F` the isomorphism fails. From it: `*_F: H-bar^n_F ≅ H-bar^{d-n}_F`
  (3); a trace `tr: H-bar^d_F → R`, `tr(h) = ∫_X *_F(H(h)) vol`, well-defined on
  any representative; a non-degenerate cup pairing (5) `H-bar^n_F × H-bar^{d-n}_F → R`;
  a scalar product (4) `(h,h') = tr(h ∪ *_F h') = ∫_X <H(h),H(h')>_F vol`; the Kunneth
  iso (6) `H-bar^n_{F_X}(X) ⊗-hat H-bar^m_{F_Y}(Y) ≅ H-bar^{n+m}_{F_{X×Y}}(X×Y)` (the
  nuclear-Frechet tensor product is unambiguous); and (Kahler foliation case, (7)-(8))
  an `H^{pq}`-decomposition `H-bar^n_F ⊗ C = ⊕_{p+q=n} H^{pq}`, hard-Lefschetz isos
  `L_F^i: H-bar^{d-i}_F ≅ H-bar^{d+i}_F`, and a polarizable ind-`R`-Hodge structure of
  weight `n` on primitive classes.
- **Theorem 2.1 (`Θ = α/2 + S`, the conditional `Re = α/2`).** Let `X` be a compact
  3-manifold, `F` a Riemannian surface foliation with a dense leaf, `φ^t` an
  `F`-compatible flow conformal on `TF`: `g(T_x φ^t v, T_x φ^t w) = e^{αt} g(v,w)`
  (formula (9)). Then `Θ = 0` on `H-bar^0_F = R`, `Θ = α` on `H-bar^2_F ≅ R`, and on
  `H-bar^1_F` `Θ = α/2 + S` with `S` skew-symmetric for `(,)`. **Proof:** dense leaf ⇒
  `H-bar^0_F` = constants ⇒ `Θ = 0`; conformality + `*_F: R = H-bar^0_F ≅ H-bar^2_F`,
  `φ^{t*}(*_F 1) = e^{αt}(*_F 1)` ⇒ `Θ = α` on `H-bar^2`; on `H-bar^1`, `α(h1∪h2) =
  Θ(h1∪h2) = Θh1∪h2 + h1∪Θh2` (formula (10)), and `φ^{t*}` commuting with `*_F`
  (differentiate) plus `(h,h') = tr(h ∪ *_F h')` gives `α(h,h') = (Θh,h') + (h,Θh')`,
  forcing `Θ = α/2 + S`, `S` skew.

**Sect. 3 (pp.9-14): the dynamical Lefschetz trace formulas.**
- **Conjecture 3.1 (the general foliated trace formula).** For `X` compact, `F`
  codimension-one, `φ` `F`-compatible, with non-degenerate fixed points (`T_x φ^t`
  without eigenvalue `1` for `t ≠ 0`) and non-degenerate closed orbits (`T_x φ^{kl(γ)}`
  has eigenvalue `1` with multiplicity one): with `ε_x = sgn det(1 - T_x φ^t | T_x F)`,
  `ε_γ(k) = sgn det(1 - T_x φ^{kl(γ)} | T_x X / R Y_{φ,x}) = sgn det(1 - T_x φ^{kl(γ)} |
  T_x F)`, and `κ_x` defined by `T_x φ^t` acting as `e^{κ_x t}` on `T_x X / T_x F`,
  there is a `D'(R^{>0})`-valued trace of `φ^*` on `H-bar^*_F(X)` with (formula (11)):
  `Σ_n (-1)^n Tr(φ^* | H-bar^n_F(X)) = Σ_γ l(γ) Σ_{k≥1} ε_γ(k) δ_{kl(γ)} +
  Σ_x ε_x |1 - e^{κ_x t}|^{-1}`. Unknown if `φ` has fixed points (except `dim X = 1`).
  "The analytic difficulty in the presence of fixed points lies in the fact that
  `Δ_F` cannot be transversally elliptic to the `R`-action by the flow, so transverse
  index theory does not apply directly."
- **Theorem 3.3 ([AK2], the proved non-singular trace formula).** Under (3.2) (`X`
  compact oriented, `F` codimension-one, `φ` everywhere transversal to `F`, hence `F`
  Riemannian with a bundle-like `g`, no fixed points, non-degenerate periodic orbits):
  for `φ ∈ D(R)`, the operator `A_φ = ∫_R φ(t) φ^{t*} dt` on the Hilbert completion
  `H-hat^n_F(X)` is **trace class**, `Tr(φ^*|H-bar^n_F)(φ) := tr A_φ` defines a
  distribution, and (formula (12)):
  `Σ_n (-1)^n Tr(φ^* | H-bar^n_F(X)) = χ_Co(F,μ) δ_0 + Σ_γ l(γ) Σ_{k∈Z\0} ε_γ(k)
  δ_{kl(γ)}` in `D'(R)`, where `χ_Co(F,μ)` is Connes' Euler characteristic of `F` for
  the transverse measure `μ` corresponding to `*_⊥(1)`. If the RHS is non-zero, some
  `H-bar^n_F` is infinite-dimensional (else the alternating trace would be smooth).
- **Theorem 3.4 (spectral form).** For Riemannian `F`, bundle-like `g`, `F`-compatible
  `φ`: the `φ^{t*}` form a strongly continuous group on `H-hat^n_F`; `Θ` is closed
  densely defined, agreeing with the Frechet generator; `sp(Θ) ⊂ {-ω ≤ Re ≤ ω}`; if
  `φ^{t*}` is orthogonal then `T = -iΘ` is self-adjoint and `φ^{t*} = exp(itT)`.
- **Corollary 3.5 (the conditional `Re = α/2`, formula (13)).** `X` compact 3-manifold,
  `F` surface foliation with dense leaf, `φ` non-degenerate everywhere-transversal
  conformal (9). Then `Θ` has pure point spectrum `Sp^1(Θ)`, discrete in `R`, with
  `1 - Σ_{ρ∈Sp^1(Θ)} e^{tρ} + e^{tα} = χ_Co(F,μ) δ_0 + Σ_γ l(γ) Σ_{k∈Z\0} ε_γ(k)
  δ_{kl(γ)}`, and **all `ρ` have `Re ρ = α/2`**. Proof: `(φ^{t*}h, φ^{t*}h') =
  e^{αt}(h,h')`, so `e^{-αt/2} φ^{t*}` is orthogonal; by Stone `T = -iS` self-adjoint
  with `Θ = α/2 + S`; alternatively `-(Θ - α/2)^2 = Δ^1 |_{ker Δ^1_F}` ([DS2] proof of
  2.6). **Remark 2 (the crux):** "actually the conditions of the corollary force
  `α = 0`, i.e. the flow must be isometric." The continuous-spectrum case (Remark, p.14)
  gives a contour `Σ_{point} Φ(ρ) + ∫_{α/2-i∞}^{α/2+i∞} Φ(λ) m(λ) dλ`, `m(λ) ≥ 0`.

**Sect. 4 (pp.14-18): explicit-formula comparison and the `α=0` / no-fixed-point
obstruction.**
- **Theorem 4.1 (Dedekind explicit formula).** For `K/Q`, `φ ∈ D(R)`,
  `Φ(s) = ∫ e^{ts} φ(t) dt` (formula (17)):
  `Φ(0) - Σ_ρ Φ(ρ) + Φ(1) = -log|d_{K/Q}| φ(0) + Σ_{p∤∞} log Np (Σ_{k≥1} φ(k log Np) +
  Σ_{k≤-1} Np^k φ(k log Np)) + Σ_{p|∞} W_p(φ)`, where for `p|∞` the `Γ`-factor
  distribution is `W_p(φ) = ∫ φ(t)/(1 - e^{κ_p t}) dt` on `R^{>0}` (`κ_p = -1` complex,
  `κ_p = -2` real) and `∫ φ(t) e^t / (1 - e^{κ_p |t|}) dt` on `R^{<0}`.
- **Distributional form (formula (19)).** `1 - Σ_ρ e^{tρ} + e^t = -log|d_{K/Q}| δ_0 +
  Σ_{p∤∞} log Np (Σ_{k≥1} δ_{k log Np} + Σ_{k≤-1} Np^k δ_{k log Np}) + Σ_{p|∞} W_p`.
- **The dictionary (p.16).** `spec o_K ∪ {p|∞}` ↔ 3-dim `(X, φ^t, F)` of Conj 3.1;
  finite place `p` ↔ closed orbit `γ_p` not in a leaf, `l(γ_p) = log Np`, `ε_{γ_p}(k) =
  1`; infinite place `p` ↔ fixed point `x_p` with `κ_{x_p} = κ_p`, `ε_{x_p} = 1`.
- **The two mismatches (p.18).** Comparing (13) with (19): (a) `χ_Co(F,μ) ↔
  -log|d_{K/Q}|` (formula (20)); **Fact 4.2** confirms the sign: non-compact leaves are
  complete ⇒ `β_0(F,μ) = 0` ⇒ `χ_Co = -β_1 ≤ 0`, matching `-log|d| ≤ 0`; refined via
  Connes' Riemann-Roch `χ_Co(F,O,μ) = (1/2) χ_Co(F,μ)` to the Arakelov Euler
  characteristic `χ_Ar(O_{spec o_K bar}) = -log√|d_{K/Q}|` (formula (21)). (b) **Number
  theory needs `α = 1`** (the `e^t` term and `φ^{t*}` scaling `H-bar^2` by `e^t`, hence
  conformal factor `e^t`, formula (22)), impossible for manifolds where Cor 3.5 forces
  `α = 0`; and (c) **the `k ≤ -1` coefficients** are `ε_γ(k) = ±1` for manifolds but
  `Np^k = e^{k log Np}` for number fields. "Thus it becomes vital to find phase spaces
  `X` more general than manifolds."

**Sect. 5 (pp.18-29): laminated spaces, the working hypothesis, the elliptic-curve
example.**
- **Laminated spaces / generalized solenoids (5.1-5.2).** An `a`-dim laminated space is
  locally `(open in R^a) × (totally disconnected)`, transition maps
  `(F_1(x,y), F_2(y))` (continuous maps from connected sets to totally disconnected are
  constant); leaves are the path components, `a`-dim manifolds. Classical solenoid
  `S^1_p = R ×_Z Z_p = lim(... → R/Z →^p R/Z)`. `C^{∞,0}` and Sullivan's stronger
  `C^{∞,∞}` / `TLC` structures (transition maps `(F_1(x), F_2(y))`). Foliations `F` of
  laminated spaces by `d`-dim laminated subspaces; three foliated structures `L, F, FL`
  with `FL` foliating `X` by the `d`-manifolds occurring as path components of the
  `F`-leaves; reduced leafwise cohomology `H-bar^*_{FL}(X)`.
- **Working hypothesis 5.6 (formula (26)).** For `X` a compact `C^{∞,0}`-laminated space
  with codimension-one `F` and `F`-compatible `φ`, non-degenerate fixed points and
  periodic orbits, there is a `D'(R*)`-valued trace with
  `Σ_n (-1)^n Tr(φ^* | H-bar^n_{FL}(X)) = Σ_γ l(γ)(Σ_{k≥1} ε_γ(k) δ_{kl(γ)} +
  Σ_{k≤-1} ε_γ(|k|) det(-T_x φ^{kl(γ)}|T_xF) δ_{kl(γ)}) + Σ_x W_x`, with the two-sided
  fixed-point distributions `W_x|_{R^{>0}} = ε_x |1 - e^{κ_x t}|^{-1}` and
  `W_x|_{R^{<0}} = ε_x det(-T_x φ^t|T_xF) |1 - e^{κ_x|t|}|^{-1}`. Remark 5.7 records the
  uniform coefficient formula (27) `det(1 - T_xφ^{kl}|T_xF)/|det(1 - T_xφ^{|k|l}|T_xF)|`,
  the manifold-case `|det(T_xφ^{kl}|T_xF)| = 1`, and the conformal-case (4)
  `|det(T_xφ^{kl(γ)}|T_xF)| = e^{kl(γ)}`, giving formula (29) which "fits perfectly with
  the explicit formula (19) if all `ε_{γ_p}(k) = 1` and `ε_{x_p} = 1`", since then
  `e^{kl(γ_p)} = Np^k` and `W_{x_p} = W_p`. The fixed-point structure forces (Fact,
  p.25) `T_x φ^{kl(γ)} = e^{(k/2)l(γ)} O_k`, `O_k ∈ SO(T_x F)`: the number-theoretic
  eigenvalues of `T_x φ^{log Np}` would be complex conjugates of absolute value
  `Np^{1/2}`, "Weil numbers of weight 1," possibly an elliptic curve over `o_K/p` via
  Tate-Honda.
- **Theorem 5.9 + the elliptic-curve example (5.8, pp.26-29).** Take an unramified cover
  `f: M → M` of a compact oriented `d`-manifold, `M-bar = lim(M →^f M →^f ...)` a
  `C^{∞,∞}`-laminated space with shift `f-bar`; suspend `X = M-bar ×_Λ R` (`Λ = lZ`),
  giving a `(d+1)`-dim laminated space with codimension-one `F`, `F`-compatible flow
  `φ^t[m,t'] = [m,t+t']` everywhere transversal, NO fixed points; closed orbits ↔ finite
  `f`-orbits, `l(γ) = |γ_M| l`. **Theorem 5.9** then proves the working hypothesis in
  this fixed-point-free case (`H-bar^n_{FL}` replaced by `H^n_F`):
  `Σ_n (-1)^n Tr(φ^*|H^n_F) = χ_Co(FL,μ) δ_0 + Σ_γ l(γ)(Σ_{k≥1} ε_γ(k) δ_{kl(γ)} +
  Σ_{k≤-1} ε_γ(|k|) det(-T_xφ^{kl(γ)}|T_xF) δ_{kl(γ)})`, with `χ_Co(FL,μ) = χ(M) l`.
  **The arithmetic instance:** `E/F_p` ordinary, `C/Γ` a CM lift with `End = o_K`,
  Frobenius ↔ a split prime `π` (`π π-bar = p`). Set `M = C/Γ`, `f = π`; then
  `X = (C ×_Γ T_π Γ) ×_Λ R` where `T_π Γ = lim Γ/π^i Γ ≅ Z_p` is the `π`-adic Tate
  module ≅ the `p`-adic Tate module of `E`. With `l = log p`, multiplicative time gives
  `X ≅ (C ×_Γ T_π Γ) ×_{p^Z} R*_+`. The RHS of the Thm 5.9 trace formula EQUALS the RHS
  of the explicit formula for `ζ_E(s)`; the metric `g_{[z,y,t]}(ξ,η) = e^t Re(ξ η-bar)`
  is conformal (9) with `α = 1`; the proof of Thm 2.1 adapts to give `Θ = 1/2 + S` on
  `H-bar^1_{FL}(X)`, `S` skew, **a dynamical proof of the Riemann hypotheses for
  `ζ_E(s)` "along the lines that we hope for in the case of `ζ(s)`."** Deninger cautions
  this is "misleading": a variety almost never lifts to characteristic zero together
  with its Frobenius, and for ordinary elliptic curves RH is already Hasse's theorem via
  Hodge cohomology of the lift. The "present dream" (p.29): attach to `X/Z` an
  infinite-dimensional dissipative dynamical system (perhaps via `GL_∞`), then pass to
  its finite-dimensional compact global attractor.

## Points mapped to the project

1. **Reduced leafwise cohomology + the leafwise Hodge theorem (Property (2)).**
   `H-bar^n_F(X) = ker d_F / closure(im d_F)`, nuclear Frechet, infinite-dimensional;
   `ker Δ_F ≅ H-bar^n_F` (deep -- `Δ_F` only leafwise elliptic); Hodge `*_F`, trace
   `tr: H-bar^d_F → R`, non-degenerate cup pairing, Kunneth, and (Kahler case)
   `H^{pq}` + hard-Lefschetz + polarization.
   -> The analytic substrate Direction 4.3 (finiteness/Hodge) needs and the `H^1` of
   Direction 4.6 is modeled on. The Kunneth iso (6) `H-bar^*_{X×Y}` is the foliated
   analogue of the 2K product structure: the product / `×` works at the
   leafwise-cohomology level once you have the spaces. The polarized `H-bar^1_prim` is
   the natural home of a Direction-8 signature theorem.

2. **The RH mechanism `Θ = α/2 + S` (Thm 2.1, Cor 3.5).** Conformality (factor
   `e^{αt}`) + Hodge `*_F` forces `Θ = α/2 + S`, `S` skew, hence `sp(Θ) ⊂ {Re = α/2}`,
   pure point and discrete.
   -> This is the **proved, conditional** version of the 1998 `Θ = 1/2 + A` RH argument
   (the Direction 8 step). RH is the `α = 1` instance. The skew part `S` carries the
   zeros; `Re = α/2` is forced by Hodge-`*` positivity + conformality, exactly the
   marginal-positivity content. The gap between "have it" and "RH" is purely: get a
   phase space where `α = 1`.

3. **The Alvarez Lopez-Kordyukov trace-class theorem (Thm 3.3, "[AK2]").**
   `A_φ = ∫ φ(t) φ^{t*} dt` is trace class on transversal Riemannian foliations; the
   distributional trace gives `χ_Co(F,μ) δ_0 + Σ_γ l(γ) Σ_k ε_γ(k) δ_{kl(γ)}`.
   -> This is the cited "[AK2]" theorem at the heart of Leichtnam 2006 and the subject
   of the ALK 2017 note. The trace-class mechanism (`A_φ` smooths because integrating
   the flow against a test function regularizes; `φ^{t*}` alone is not trace class) is
   the concrete answer to Direction 4.3 (finiteness) in the no-fixed-point regime. The
   `χ_Co(F,μ) δ_0` term is the `s = 0,1` polar contribution, identified with
   `-log|d_{K/Q}|`.

4. **The strong spectral statement (Thm 3.4) + continuous-spectrum form.** Orthogonal
   `φ^{t*}` ⇒ `T = -iΘ` self-adjoint, `φ^{t*} = exp(itT)`, pure point spectrum in a
   strip; or a contour `∫_{α/2-i∞}^{α/2+i∞} Φ(λ) m(λ) dλ`, `m ≥ 0`.
   -> The contour form is exactly the shape needed if the zeros were a continuous
   spectrum. For the arithmetic case (discrete zeros) the pure-point statement is the
   target; the machinery handles both.

5. **The explicit-formula comparison and the `α=0` / `Np^k`-vs-`±1` obstruction
   (sect.4).** Term-by-term match of (19) against (13): finite `p` ↔ transversal orbit
   `l(γ) = log Np`; infinite `p` ↔ fixed point `κ = κ_p`; `-log|d_{K/Q}| ↔ χ_Co(F,μ)`
   (Fact 4.2: `χ_Co ≤ 0` matches `-log|d| ≤ 0`). The match **fails** on two counts:
   (a) number theory needs `α = 1` (the `e^t` factor), impossible for manifolds; (b) the
   `k ≤ -1` coefficients are `±1` for manifolds but `Np^k` for number fields.
   -> This is the precise statement of why the foliated picture is not yet the
   arithmetic one, and it IS the 2K gap in flow language. The fix requires phase spaces
   more general than manifolds (laminated spaces) AND fixed points (the archimedean
   place) -- exactly what ALK 2017 supplies. The `χ_Co = -log|d_{K/Q}|` / Arakelov
   bookkeeping (20)-(21) is clean 2I-flavored archimedean accounting: the discriminant
   is the foliated Euler characteristic.

6. **Laminated spaces / the working hypothesis 5.6 / the elliptic-curve proof.**
   Solenoids `S^1_p = R ×_Z Z_p`; the totally-disconnected transversal carries the `Z_p`
   factor; formula (26) extends the trace formula to `D'(R*)` with `α ≠ 0` and a
   two-sided fixed-point `W_x`; Thm 5.9 + the CM-lift example realize `α = 1` and give a
   dynamical RH proof for `ζ_E(s)`.
   -> The totally-disconnected transversal is the `Z_p` that Leichtnam 2006 makes the
   "p-adic transversal" and the prismatic direction realizes: number theory enters
   through the totally-disconnected (p-adic / adelic) transversal. **The elliptic-curve
   example is the existence proof that the whole machine works when the space exists**:
   a solenoid with `α = 1` gives `Θ = 1/2 + S`, RH for `ζ_E`. D-H discipline: such a
   space carries a genuine `{log Np}` closed-orbit spectrum; Davenport-Heilbronn has no
   Euler product, hence no orbit spectrum, so this construction is on the right side of
   the wrong-approach detector (consistent with 2R).

## What this changes for the program

- **The `Re = α/2` theorem is real, conditional, and exactly the Direction-8 step in
  flow form.** Cor 3.5 proves `sp(Θ) ⊂ {Re = α/2}` from Hodge-`*` + conformality; RH is
  the `α = 1` instance. The whole gap between "have it" and "RH" is: get a phase space
  with `α = 1` and fixed points allowed. Thm 5.9 shows it is not vacuous -- it works for
  `ζ_E(s)`.
- **The trace-class question (Direction 4.3) is solved in the non-singular case.** Thm
  3.3 (ALK 2002) is the existence proof: `A_φ = ∫ φ φ^{t*} dt` is trace class for
  transversal flows. The remaining difficulty is fixed points, where `Δ_F` is no longer
  transversally elliptic to the `R`-action. This is the exact boundary ALK 2017 pushes.
- **The 2K product-surface gap has a flow-language twin.** "Manifolds force `α = 0` and
  forbid fixed points; number theory needs `α = 1` and a fixed point at `∞` with `Np^k`
  coefficients" is the same obstruction as "no absolute base point / no
  `Spec(Z) × Spec(Z)`." The Arakelov bookkeeping `χ_Co = -log|d_{K/Q}|` shows the
  archimedean / global accounting already works; what is missing is the space.
- **The totally-disconnected transversal is where arithmetic enters.** Sect. 5 makes
  explicit that the move from manifolds to laminated spaces (solenoids with `Z_p`
  factors) supplies `α = 1`. Direct support for Direction-3 (p-adic/prismatic) +
  Direction-4 (foliation), consistent with the Leichtnam 2006 "p-adic transversal makes
  the trace class" finding. The CM-lift example is the worked proof of concept.

## Actionable

- Treat Cor 3.5 / Thm 2.1 (`Θ = α/2 + S`) as the canonical conditional `Re = 1/2`
  statement on the flow side, and the `α=0`-vs-`α=1` plus `±1`-vs-`Np^k` mismatch
  (p.18) as the precise specification of what a number-theoretic phase space must fix.
- Working hypothesis 5.6 formula (26), with its two-sided `W_x` fixed-point
  distributions, is the target ALK 2017's general-case trace formula aims to prove.
  Read alongside ALK 2017's "term supported on `M^0`" slides.
- The elliptic-curve example (pp.28-29) is the strongest existing evidence that the
  program is internally consistent: a solenoid over a CM lift, `α = 1`, gives
  `Θ = 1/2 + S` and RH for `ζ_E`. The honest caveat (no Frobenius-compatible lift in
  general; RH for ordinary `E` already known) is why this is a model, not the theorem.
- No new computation. The structural takeaway feeds the trace ↔ signature thread: 2R
  gives the orbit spectrum, Cor 3.5 gives `Re = α/2` from `*`-positivity, Direction 8 is
  the `α = 1` Hodge-`*` realization, and Thm 5.9 is the proof that all three close once
  the space exists.

## Status

Read pp.1-29 of 29 (the full body) plus references (pp.30-32): sect.1 intro (and the
contrast with Connes' adelic non-commutative approach); sect.2 foliation cohomology +
leafwise Hodge package (Property (2)-(8)) + Theorem 2.1; sect.3 Conjecture 3.1, the ALK
trace formula (Thm 3.3 / [AK2]), spectral theorem (Thm 3.4), and Corollary 3.5
(`Re = α/2`); sect.4 the Dedekind explicit formula (Thm 4.1), its distributional form
(19), the dictionary, Fact 4.2, and the `α=0` / `±1`-vs-`Np^k` obstructions; sect.5
laminated spaces, working hypothesis 5.6 (formula (26)), Theorem 5.9, and the
elliptic-curve example (the CM-lift solenoid giving a dynamical proof of RH for
`ζ_E(s)`). Honest depth: the leafwise Hodge theorem (Property (2)) and the ALK
trace-class theorem (Thm 3.3) are read as cited black boxes ([AKI]/[AK2], i.e. the
ALK 2001/2002 papers and ALK 2017); the construction of `χ_Co` and the proof of Thm 5.9
are stated with their structure but "given elsewhere."
