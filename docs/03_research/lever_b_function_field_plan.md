# Lever B: a plan to formalize function-field RH (discharge #FF-geom) in Lean

> Posted 2026-06-14. The roadmap to turn the function-field RH chain ([`../../lean/ZetaRH/FunctionFieldRH.lean`](../../lean/ZetaRH/FunctionFieldRH.lean)) from a sorry-free **conditional** theorem (given Castelnuovo-Severi) into an **unconditional** machine-checked theorem for elliptic curves. Companion to [`optimizing_rh_for_ai.md`](optimizing_rh_for_ai.md) (lever B) and the VERIFIER table in [`../../lean/README.md`](../../lean/README.md) (#FF-1, #FF-geom).

## The goal

Discharge **#FF-geom**: prove the Hasse bound $t^2 < 4q$ (equivalently $|t|\le 2\sqrt q$) for a genuine elliptic curve $E/\mathbb{F}_q$, so that an `EllipticFrobeniusData` instance can be **constructed from a real curve** rather than assumed. That makes `functionfield_RH_elliptic` unconditional: a complete, machine-checked function-field Riemann Hypothesis for elliptic curves. This is the non-circular ground truth a verifier-trained loop (lever 5) grows the $\mathrm{Spec}(\mathbb{Z})$ lift against.

**Status (2026-06-14).** The keystone #2G-1, the eigenvalue extraction #FF-1, and now the **whole
algebraic core (M-1, #FF-M1)** are proved sorry-free: given that the Frobenius *degree* form is
non-negative on the endomorphism lattice, the Hasse bound, the strict prime boundary, and
$|\alpha|^2=p$ all follow (see `IsogenyDegree.lean`, `functionfield_RH_elliptic_of_degree`). The
Hasse bound is therefore **no longer the input** -- it is derived. The *one* remaining input is the
geometric hypothesis `hdeg`: that $\deg$ really is this non-negative quadratic form for a real curve.
How to discharge it is the subject of the section ["Discharging `hdeg`"](#discharging-hdeg-making-deg-a-non-negative-quadratic-form-for-a-real-curve) below.

## The route: elementary Hasse (degree is a positive-definite quadratic form)

Do **not** route through full surface intersection theory (the $C\times C$ / Hodge-index path is general-genus but far from Mathlib). For genus 1, the shortest path is the classical elementary proof of Hasse:

> For the Frobenius endomorphism $\varphi$ of $E/\mathbb{F}_q$, every isogeny has non-negative degree, so $\deg(m + n\varphi) = m^2 + mn\,t + n^2 q \ge 0$ for all integers $m,n$ (with $t = q+1-\#E(\mathbb{F}_q)$). A positive-semidefinite binary form has non-positive discriminant: $t^2 - 4q \le 0$.

This mirrors the keystone #2G-1 exactly (completing the square on a binary quadratic form), and reduces #FF-geom to a small, well-understood arithmetic-geometry package. References: the elementary degree-form proof ([arXiv:1212.2535](https://arxiv.org/pdf/1212.2535); Oxford W5 Hasse notes; MIT 18.783 Lecture 7).

## Mathlib audit (re-run 2026-06-14, Lean v4.30.0)

A direct probe of the pinned Mathlib (`.lake/packages/mathlib`) found MORE present than the
original audit assumed, which changes the strategy: the M-2 trace data is already there.

- **HAS (group law + arithmetic):** `WeierstrassCurve` / `EllipticCurve` with the **group law in
  any characteristic** (ITP 2023); affine / projective / Jacobian point groups; schemes; Dedekind
  domains and function fields.
- **HAS (the M-2 data, this is the key find):** `WeierstrassCurve.localPolynomial`
  (`Mathlib/AlgebraicGeometry/EllipticCurve/LFunction.lean`, T. Browning 2026) is, for good
  reduction, exactly $1 - a\,T + q\,T^2$ with $q = \#\kappa$ (residue field) and
  $a = q + 1 - \#W(\kappa)$ via `Nat.card (W'.reduction R).toAffine.Point`. So the **Frobenius
  trace $t=a$ and the point count $\#E$ are already defined in Mathlib.** The elliptic-curve
  `LFunction` is built on top. What is NOT proved there is any bound on the roots: `localPolynomial`
  is defined, but $a^2 \le 4q$ (RH for the local factor) is absent. **That absent bound is our gap.**
- **HAS (multiplication-by-$n$ degree, at the polynomial level):** the division polynomials
  $\psi_n,\ \Psi^{\mathrm{Sq}}_n,\ \Phi_n$ with their degrees
  (`DivisionPolynomial/Degree.lean`, D. Angdinata): $\Phi_n$ has degree $n^2$,
  $\Psi^{\mathrm{Sq}}_n$ degree $n^2-1$. The $x$-coordinate of $[n]P$ is $\Phi_n/\Psi^{\mathrm{Sq}}_n$,
  so $\deg[n]=n^2$ is implicit here, but as a polynomial degree, not yet as an isogeny-degree map.
- **HAS:** reduction mod $\mathfrak p$ (`Reduction.lean`): good / multiplicative / additive reduction.
- **LACKS (the residual, confirmed by grep, zero hits):** isogenies $E\to E$ as a structured
  object; $\mathrm{End}(E)$ as a ring; the **degree map** $\deg:\mathrm{End}(E)\to\mathbb Z$; the
  **dual isogeny** and its **additivity** $(\varphi+\psi)^\vee=\hat\varphi+\hat\psi$; the **Weil
  pairing**; the **Tate module** $T_\ell E$ and the torsion structure $E[n]\cong(\mathbb Z/n)^2$;
  the Frobenius as an endomorphism over $\mathbb F_q$; the Hasse bound. The **FLT project is not a
  dependency** of this repo's Mathlib pin, so none of its isogeny/Galois machinery is reachable
  here yet (it remains the place to coordinate / lift from when it matures).

Connection point: the cleanest upstreamable target is **"the roots of
`WeierstrassCurve.localPolynomial` (good reduction) have absolute value $\sqrt q$", i.e.
$a^2 \le 4q$ for $1 - aT + qT^2$** -- stated on the object Mathlib already has, with $a,q$ supplied
by Mathlib. `functionfield_RH_elliptic_of_degree` is that statement modulo the `hdeg` input.

## Milestones

- **M-0 (DONE, 2026-06-14): the discriminant bridge lemma.** A real binary form $Q(m,n)=m^2 + t\,mn + q\,n^2$ with $Q(m,n)\ge 0$ for all $(m,n)$ has $t^2\le 4q$; positive-definite ($>0$ off the origin) gives the strict $t^2<4q$. Proved sorry-free in [`../../lean/ZetaRH/FunctionFieldRH.lean`](../../lean/ZetaRH/FunctionFieldRH.lean) as `disc_nonpos_of_posSemidef` and `disc_neg_of_posDef` (evaluate at $(-t/2, 1)$; the positive mirror of #2G-1's `negDef_of_hasseWeil`). Build green. This is the bridge from "$\deg\ge 0$" to "$t^2\le 4q$"; the remaining glue (the form is $\ge 0$ for all *real* m,n, from integers by homogeneity + density) belongs to M-3.
- **M-1: the isogeny + degree API. ALGEBRAIC CORE DONE (2026-06-14); scheme-theoretic part is the residual critical path.** The deliverable splits into two layers.
  - *Algebraic layer (DONE, sorry-free, axiom-clean).* [`../../lean/ZetaRH/IsogenyDegree.lean`](../../lean/ZetaRH/IsogenyDegree.lean) defines the degree form `degForm t q m n = m^2 + t*m*n + q*n^2` and proves the **Hasse bridge** `disc_nonpos_of_int_nonneg`: if the form is non-negative on the lattice $\mathbb{Z}\cdot 1 \oplus \mathbb{Z}\cdot\varphi$ (the geometric content "every isogeny has non-negative degree"), then $t^2\le 4q$. The proof passes integer$\to$rational by homogeneity and rational$\to$real by density (`disc_nonpos_of_rat_nonneg`, via `exists_rat_btwn` + a completed square), so the **M-3 integer$\to$real glue is absorbed here**. Wired in [`../../lean/ZetaRH/FunctionFieldRH.lean`](../../lean/ZetaRH/FunctionFieldRH.lean) by the constructor `EllipticFrobeniusData.ofDegreeNonneg` and the endpoint `functionfield_RH_elliptic_of_degree`: over a prime field, `deg ≥ 0` on the lattice $\Rightarrow |\alpha|^2=p$. So the Hasse bound is now a THEOREM downstream of degree-positivity, not an assumed numeric field.
  - *Scheme-theoretic layer (the residual, still ~months).* Define isogenies of $E/k$, the degree $\deg:\mathrm{End}(E)\to\mathbb{Z}$, its additivity on the binary quadratic form, $\deg(\psi)\ge 0$, and $\deg(\psi)=0\iff\psi=0$. This is the bulk and a major Mathlib contribution in its own right; coordinate with the FLT project. It is exactly the hypothesis `hdeg` of `functionfield_RH_elliptic_of_degree`: discharging it makes the endpoint unconditional.
- **M-2 (hard): Frobenius and its characteristic polynomial.** The Frobenius endomorphism $\varphi_q$ over $\mathbb{F}_q$, $\deg(\varphi)=q$, $\deg(1-\varphi)=\#E(\mathbb{F}_q)$, and hence $\deg(m+n\varphi)=m^2+mn\,t+n^2 q$ with $t=q+1-\#E(\mathbb{F}_q)$. This is what supplies `hdeg` with concrete $q=\deg\varphi$ and $t=q+1-\#E$. ~weeks-months given M-1.
- **M-3 (assemble): Hasse. DONE as a conditional bridge.** $\deg$ positive-semidefinite on the lattice $\Rightarrow$ (Hasse bridge, incl. the integer$\to$real density glue) $\Rightarrow t^2\le 4q$. Proved sorry-free in `disc_nonpos_of_int_nonneg`; what remains is feeding it the M-1/M-2 scheme-theoretic `hdeg`.
- **M-4 (wire + boundary): discharge #FF-geom.** Construct `EllipticFrobeniusData` from $E/\mathbb{F}_q$ and make `functionfield_RH_elliptic` unconditional. **Prime-field boundary DONE:** `hasse_strict_of_prime` upgrades $t^2\le 4q$ to the strict $t^2<4q$ the eigenvalue chain needs, via `four_mul_prime_not_isSquare` ($4p$ is never a perfect square for prime $p$). The general prime-power boundary $t^2=4q$ (supersingular, real roots $\pm\sqrt q$) is the one remaining wire. ~days.

## Discharging `hdeg`: making `deg` a non-negative quadratic form for a real curve

The single remaining hypothesis is `hdeg : ∀ m n : ℤ, 0 ≤ degForm t q m n`, i.e. the Frobenius
degree form is non-negative on the lattice $\mathbb Z\cdot 1 \oplus \mathbb Z\cdot\varphi$. It
decomposes into four obligations, and only **one** of them is deep.

### The four obligations

- **O1 (the objects).** $\mathrm{End}(E)$ as a ring; the degree map $\deg:\mathrm{End}(E)\to
  \mathbb Z_{\ge 0}$ with $\deg(0)=0$, $\deg(\psi)>0$ for $\psi\ne 0$, and multiplicativity
  $\deg(\varphi\psi)=\deg\varphi\cdot\deg\psi$.
- **O2 (additivity = the quadratic-form property).** $\deg$ is a **quadratic form**: the polar
  $B(\varphi,\psi)=\deg(\varphi+\psi)-\deg\varphi-\deg\psi$ is $\mathbb Z$-bilinear. THIS IS THE
  CRUX.
- **O3 (the two values + the trace).** $\deg(1)=1$, $\deg(\varphi_{\mathrm{Frob}})=q$, and
  $t=B(1,\varphi)=q+1-\#E(\mathbb F_q)$.
- **O4 (non-negativity).** $\deg\ge 0$, immediate from O1.

Given O2, $\deg(m\cdot1+n\varphi)=m^2\deg(1)+mn\,B(1,\varphi)+n^2\deg(\varphi)=m^2+t\,mn+q\,n^2$
is **forced** (a quadratic form is determined by its values on a basis and the polar). So
`hdeg` $=$ O2 $+$ O3 $+$ O4, and the algebraic layer already proved here finishes the rest
($t^2\le 4q$, strict over a prime field, $|\alpha|^2=p$). **O3 is largely already in Mathlib**:
the trace $t=a$ and $\#E$ are exactly `WeierstrassCurve.localPolynomial`'s data. So the real
work is **O1 + O2**.

### Why O2 (additivity) is the heart

The dual isogeny $\hat\varphi$ satisfies $\hat\varphi\varphi=[\deg\varphi]$. Then
$$[\deg(\varphi+\psi)]=(\varphi+\psi)^\vee(\varphi+\psi)=(\hat\varphi+\hat\psi)(\varphi+\psi)
=[\deg\varphi]+[\deg\psi]+(\hat\varphi\psi+\hat\psi\varphi),$$
so $B(\varphi,\psi)\cdot[1]=\hat\varphi\psi+\hat\psi\varphi$, which is bilinear **iff the dual is
additive**, $(\varphi+\psi)^\vee=\hat\varphi+\hat\psi$ (Silverman *AEC* III.6.2-6.3). In one line:
**"$\deg$ is a quadratic form" $\iff$ "the dual isogeny is additive"**, and that is the single
hard theorem behind the Hasse bound.

### Three routes to O1 + O2

- **Route A (elementary, reuses Mathlib's division polynomials; PARTIAL).** $\deg[n]=n^2$ is
  essentially present ($\Phi_n$ has degree $n^2$). Over $\mathbb F_q$, Frobenius
  $\varphi:(x,y)\mapsto(x^q,y^q)$ is explicit and purely inseparable of degree $q$, and $1-\varphi$
  is separable with $\ker(1-\varphi)=E(\mathbb F_q)$, so $\deg(1-\varphi)=\#E(\mathbb F_q)$ -- which
  Mathlib HAS. This pins the specific values (O3) and is a good cross-check, but it does NOT give the
  general quadratic-form property (O2). Use it to validate O3, not to close O2.
- **Route A′ (dual isogeny, Silverman III.6 -- minimal self-contained surface).** Define $\deg$ via
  the function-field extension degree (Mathlib has finite-extension degrees / morphism degree), build
  the dual via $\mathrm{Pic}^0(E)\cong E$ (autoduality), then prove additivity of the dual via the
  **theorem of the cube / seesaw** on $E\times E$. Bottleneck: $\mathrm{Pic}^0$ autoduality + the
  theorem of the cube, both absent and both substantial. Smallest mathematical surface, but the
  theorem of the cube is itself a serious formalization.
- **Route B (Tate-module determinant -- conceptually cleanest, heaviest deps, FLT-aligned).** For
  $\ell\ne\mathrm{char}$, $T_\ell E\cong\mathbb Z_\ell^2$, $\mathrm{End}(E)$ acts, and
  $\deg=\det$, $\mathrm{tr}=\mathrm{trace}$ on $T_\ell$ (Silverman III.8.6, via the Weil pairing
  $e_\ell(\varphi x,\varphi y)=e_\ell(x,y)^{\deg\varphi}$). Then O2 is **free**: $\det$ on a rank-2
  module is *literally* a quadratic form (the reduced norm), so no theorem of the cube is needed.
  Positive-definiteness: $\deg\varphi=0\Rightarrow\varphi$ kills all $\ell$-power torsion
  $\Rightarrow\varphi=0$. Dependencies: $E[\ell^n]\cong(\mathbb Z/\ell^n)^2$ (torsion structure
  theorem), the Weil pairing, the $\ell$-adic representation -- all absent here, but all are FLT
  targets.

**Recommendation.** For the function-field wedge in isolation, Route A′ is the minimal build, but
the theorem of the cube is a real cost. **For the program as a whole, prefer Route B**: it makes O2
free ($\det$ is a quadratic form), it is exactly what the FLT project is building, and it is the
literal finite-field rehearsal of the M4 target -- "$\deg=\det/\text{norm}$ on $H^1$ is a quadratic
form whose positivity is RH" is the Spec($\mathbb Z$) shape (08A's M4). Track FLT; when $T_\ell$ and
the Weil pairing land, Route B closes O1+O2 fast. In the meantime, do the immediate Lean step below,
which is independent of which route lands.

### The immediate Lean step (M-1.5): reduce `hdeg` to a typed quadratic-form contract -- DONE (2026-06-14)

Before any scheme theory, the hypothesis is sharpened from "the *explicit* form is non-negative" to
the honest minimal statement "**$\deg$ is ANY non-negative quadratic form with $\deg(1)=1$,
$\deg(\varphi)=q$**". This is now proved sorry-free in `IsogenyDegree.lean` over Mathlib's
`QuadraticForm`, modelling the rank-2 lattice $\mathbb Z\cdot1\oplus\mathbb Z\cdot\varphi$ as
$\mathbb Z\times\mathbb Z$ ($1\mapsto(1,0)$, $\varphi\mapsto(0,1)$):

- `quadratic_eq_basis (Q : QuadraticForm ℤ (ℤ×ℤ)) (m n) : Q (m,n) = m²·Q(1,0) + (polar Q (1,0)(0,1))·m·n + n²·Q(0,1)`
  -- **the explicit form is FORCED** by the quadratic-form structure (via `map_smul` + `polar_smul_left/right`).
- `hasse_of_quadratic (Q) (h1 : Q(1,0)=1) (hnn : ∀ v, 0 ≤ Q v) : (polar Q (1,0)(0,1) : ℝ)² ≤ 4·(Q(0,1):ℝ)`
  -- **the Hasse bound from the contract** (`quadratic_eq_basis` then the Hasse bridge).

Both are axiom-clean (`quadratic_eq_basis` does not even need `Classical.choice`). Consequence: the
geometry owes only O2 (it is a quadratic form) + O3 (two values, mostly in Mathlib) + O4 (non-negative),
**never the explicit polynomial**. This is the precise contract the scheme-theoretic work (Route A′ or
B) must instantiate: produce `End(E)` with a degree `QuadraticForm` that is non-negative on the
lattice, with `deg 1 = 1` and `deg φ_Frob = q`.

### Dependency-ordered task list

1. **M-1.5 (DONE 2026-06-14):** the `QuadraticForm` contract lemmas `quadratic_eq_basis` +
   `hasse_of_quadratic` in `IsogenyDegree.lean`, sorry-free and axiom-clean. The obligation is now
   reduced to O2+O3+O4.
2. **O3 wiring (DONE 2026-06-14):** `LocalFactor.lean` connects the chain to Mathlib's
   `WeierstrassCurve.localPolynomial`. `localFactor_root_normSq` (RH for the abstract local factor
   `1-aT+qT²`: `a²<4q ⟹` roots have `|·|²=1/q`, via the reciprocal `α=β⁻¹` and the eigenvalue
   extraction); `localPolynomial_eq_of_goodReduction` (unfolds `W.localPolynomial` to `1-C a·X+C q·X²`
   with `a=q+1-#W(κ)`, `q=#κ` -- the trace/count now Mathlib-native); `localPolynomial_root_normSq`
   (the roots of Mathlib's `localPolynomial` have `|·|²=1/q`, given the Hasse bound). Sorry-free,
   axiom-clean. The Hasse bound is the only open input.
3. **O1 (route choice):** `End(E)` + `deg`. Route A′: morphism/field-extension degree. Route B: the
   $T_\ell$ action. Coordinate with FLT for B.
4. **O2 (the crux):** additivity of the dual (Route A′, theorem of the cube) OR $\deg=\det$ on $T_\ell$
   (Route B, Weil pairing). This is the multi-month piece and the genuine Mathlib contribution.
5. **Wire:** instantiate the M-1.5 contract from O1+O2+O3, discharge `hdeg`, make
   `functionfield_RH_elliptic_of_degree` unconditional, and state it as the Hasse bound for
   `WeierstrassCurve.localPolynomial` (the upstreamable form).

## A correctness subtlety to flag (boundary case)

The current chain routes through `eigenvalue_modulus`, which needs the Frobenius roots to be **non-real** (`root_nonreal` requires the strict $t^2<4q$). The Hasse bound gives $t^2\le 4q$. The boundary $t^2=4q$ (supersingular, real eigenvalues $\pm\sqrt q$) occurs only for prime-power $q$ that is a perfect square; **for $q$ prime it never occurs** ($4q$ is not a perfect square, so $t^2<4q$ is automatic). So:
- For $q$ prime (the case `FunctionFieldRH`'s `b_e(p,t)` uses), Hasse already gives the strict $t^2<4q$ the chain needs.
- For general prime-power $q$, add a one-line boundary case to `FunctionFieldRH.lean`: when $t^2=4q$ the roots are real and equal $\pm\sqrt q$, so $|\alpha|^2=q$ directly. Small, do it in M-4.

## Effort, risk, upstreaming

- **Done:** M-0 (the real-form discriminant bridge), **M-1 algebraic core** (#FF-M1: the lattice
  Hasse bridge, the strict prime boundary, the RH endpoint), **M-1.5** (the `QuadraticForm`
  contract: `quadratic_eq_basis` + `hasse_of_quadratic`), and **O3 wiring** (#FF-O3: `LocalFactor.lean`
  connects the chain to Mathlib's `WeierstrassCurve.localPolynomial`) -- all sorry-free and axiom-clean.
- **Next:** O1+O2 (the scheme-theoretic `deg`), the critical path, via route A′ or B.
- **Critical path (O1+O2, several expert-months):** the isogeny/degree API and the additivity of the
  dual (or $\deg=\det$ on $T_\ell$). This is the flagship Mathlib contribution; the whole package
  (isogenies, degree, dual / Weil pairing, Hasse) is something Mathlib wants, and it overlaps the FLT
  project. Note O3 (the trace and point count) is **already in Mathlib** (`localPolynomial`), so the
  remaining work is O1+O2, not the trace data.
- **Risk:** O2 is the genuine theorem (additivity of the dual = theorem of the cube, Route A′; or the
  Weil-pairing/$T_\ell$ comparison, Route B). Route B's deps (Tate module, Weil pairing) are larger
  but FLT-aligned and make O2 free; Route A′ is self-contained but the theorem of the cube is costly.

## Genus-$g$ generalization (out of scope here, noted)

Full Weil RH for genus $g$ goes through the Jacobian (an abelian variety) and the **Rosati involution positive-definiteness** (the general form of "$\deg$ is positive-definite"), the same structural argument scaled up, but requiring abelian varieties and Néron-Tate in Mathlib. The elliptic plan is the wedge; it also exercises exactly the positive-definite-quadratic-form pattern that the genus-$g$ Rosati form (08A's M1) and the Spec($\mathbb{Z}$) target (M4) need.

## Interface to the existing scaffold

The deliverable is a theorem of the shape
```
theorem hasse_bound {q : ℕ} (hq : q.Prime) (E : EllipticCurve (ZMod q)) :
    (trace_frobenius E) ^ 2 < 4 * q
```
(strict for $q$ prime; $\le$ in general, with the boundary handled in M-4), feeding `EllipticFrobeniusData`. Then `functionfield_RH_elliptic` becomes unconditional, and lever B has a complete, non-circular, machine-checked function-field RH for elliptic curves: the value-function floor the rest of the program (the $\mathrm{Spec}(\mathbb{Z})$ lift, M4) is transported against.

The upstreamable form of the same theorem is stated directly on Mathlib's existing object: **for
`W : WeierstrassCurve` of good reduction, the roots of `W.localPolynomial` ($= 1-aT+qT^2$) have
absolute value $\sqrt q$, equivalently $a^2 \le 4q$.** Mathlib already supplies $a$ (the trace) and
$q$ (the residue-field cardinality) there; our `disc_nonpos_of_int_nonneg` supplies the bound once
$\deg$-positivity (O1+O2) is in place. This is the clean PR target.

## References

- Elementary Hasse via the degree quadratic form: [arXiv:1212.2535](https://arxiv.org/pdf/1212.2535) ("Hasse theorem -- an elementary approach"); MIT 18.783 Elliptic Curves, Lecture 7 (point counting); Oxford W5 Hasse notes.
- Silverman, *The Arithmetic of Elliptic Curves* (2009): III.6 (the dual isogeny + additivity = "$\deg$ is a quadratic form", Route A′); III.8.6 ($\deg=\det$ on the Tate module, Route B); V.1.1 (Hasse).
- Mathlib pieces present (Lean v4.30.0): `Mathlib/AlgebraicGeometry/EllipticCurve/LFunction.lean` (`WeierstrassCurve.localPolynomial` $=1-aT+qT^2$, the trace + point count, T. Browning 2026); `DivisionPolynomial/Degree.lean` ($\Phi_n$ degree $n^2$, D. Angdinata); `Reduction.lean`; the ITP-2023 group law. Absent: isogeny/`End`/`deg`, the dual + additivity, the Weil pairing, the Tate module.
- The FLT formalization project (Buzzard et al.), for adjacent arithmetic-geometry machinery (Tate modules / Galois representations -- the Route B dependencies). Not currently a dependency of this repo's Mathlib pin.
- Project: [`optimizing_rh_for_ai.md`](optimizing_rh_for_ai.md) (lever B), [`../../lean/ZetaRH/FunctionFieldRH.lean`](../../lean/ZetaRH/FunctionFieldRH.lean) (the conditional chain this completes), [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) (the genus-$g$ / Spec($\mathbb{Z}$) Rosati generalization).
