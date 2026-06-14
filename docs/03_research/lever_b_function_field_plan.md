# Lever B: a plan to formalize function-field RH (discharge #FF-geom) in Lean

> Posted 2026-06-14. The roadmap to turn the function-field RH chain ([`../../lean/ZetaRH/FunctionFieldRH.lean`](../../lean/ZetaRH/FunctionFieldRH.lean)) from a sorry-free **conditional** theorem (given Castelnuovo-Severi) into an **unconditional** machine-checked theorem for elliptic curves. Companion to [`optimizing_rh_for_ai.md`](optimizing_rh_for_ai.md) (lever B) and the VERIFIER table in [`../../lean/README.md`](../../lean/README.md) (#FF-1, #FF-geom).

## The goal

Discharge **#FF-geom**: prove the Hasse bound $t^2 < 4q$ (equivalently $|t|\le 2\sqrt q$) for a genuine elliptic curve $E/\mathbb{F}_q$, so that an `EllipticFrobeniusData` instance can be **constructed from a real curve** rather than assumed. That makes `functionfield_RH_elliptic` unconditional: a complete, machine-checked function-field Riemann Hypothesis for elliptic curves. This is the non-circular ground truth a verifier-trained loop (lever 5) grows the $\mathrm{Spec}(\mathbb{Z})$ lift against, and the keystone #2G-1 + the eigenvalue extraction #FF-1 are already proved, so the Hasse bound is the **one** remaining input.

## The route: elementary Hasse (degree is a positive-definite quadratic form)

Do **not** route through full surface intersection theory (the $C\times C$ / Hodge-index path is general-genus but far from Mathlib). For genus 1, the shortest path is the classical elementary proof of Hasse:

> For the Frobenius endomorphism $\varphi$ of $E/\mathbb{F}_q$, every isogeny has non-negative degree, so $\deg(m + n\varphi) = m^2 + mn\,t + n^2 q \ge 0$ for all integers $m,n$ (with $t = q+1-\#E(\mathbb{F}_q)$). A positive-semidefinite binary form has non-positive discriminant: $t^2 - 4q \le 0$.

This mirrors the keystone #2G-1 exactly (completing the square on a binary quadratic form), and reduces #FF-geom to a small, well-understood arithmetic-geometry package. References: the elementary degree-form proof ([arXiv:1212.2535](https://arxiv.org/pdf/1212.2535); Oxford W5 Hasse notes; MIT 18.783 Lecture 7).

## Mathlib audit (June 2026)

- **HAS:** `WeierstrassCurve` / `EllipticCurve` and the **group law in any characteristic** (formalized, ITP 2023, in Mathlib); schemes; Dedekind domains and function fields; the FLT project (Buzzard et al.) is actively building adjacent arithmetic geometry.
- **LACKS:** isogenies $E\to E$ and the degree map; the Frobenius endomorphism over $\mathbb{F}_q$; positive-definiteness of $\deg$; point counting $\#E(\mathbb{F}_q)$; the Hasse bound itself.

Action item before starting: re-audit current Mathlib and the FLT project for any of the M-1/M-2 pieces (the FLT effort needs adjacent isogeny/Galois machinery and may already supply some).

## Milestones

- **M-0 (DONE, 2026-06-14): the discriminant bridge lemma.** A real binary form $Q(m,n)=m^2 + t\,mn + q\,n^2$ with $Q(m,n)\ge 0$ for all $(m,n)$ has $t^2\le 4q$; positive-definite ($>0$ off the origin) gives the strict $t^2<4q$. Proved sorry-free in [`../../lean/ZetaRH/FunctionFieldRH.lean`](../../lean/ZetaRH/FunctionFieldRH.lean) as `disc_nonpos_of_posSemidef` and `disc_neg_of_posDef` (evaluate at $(-t/2, 1)$; the positive mirror of #2G-1's `negDef_of_hasseWeil`). Build green. This is the bridge from "$\deg\ge 0$" to "$t^2\le 4q$"; the remaining glue (the form is $\ge 0$ for all *real* m,n, from integers by homogeneity + density) belongs to M-3.
- **M-1 (hard, the critical path): the isogeny + degree API.** Define isogenies of $E/k$, the degree $\deg:\mathrm{End}(E)\to\mathbb{Z}$, its additivity on the quadratic form, $\deg(\psi)\ge 0$, and $\deg(\psi)=0\iff\psi=0$ (positive-definiteness). This is the bulk and a major Mathlib contribution in its own right; coordinate with the FLT project. ~months.
- **M-2 (hard): Frobenius and its characteristic polynomial.** The Frobenius endomorphism $\varphi_q$ over $\mathbb{F}_q$, $\deg(\varphi)=q$, $\deg(1-\varphi)=\#E(\mathbb{F}_q)$, and hence $\deg(m+n\varphi)=m^2+mn\,t+n^2 q$ with $t=q+1-\#E(\mathbb{F}_q)$. ~weeks-months given M-1.
- **M-3 (assemble): Hasse.** $\deg$ positive-definite $\Rightarrow Q(m,n)=\deg(m+n\varphi)\ge 0 \Rightarrow$ (M-0) $\Rightarrow t^2\le 4q$. ~days given M-1/M-2.
- **M-4 (wire + boundary): discharge #FF-geom.** Construct `EllipticFrobeniusData` from $E/\mathbb{F}_q$ and make `functionfield_RH_elliptic` unconditional. Handle the boundary case $t^2=4q$ (below). ~days.

## A correctness subtlety to flag (boundary case)

The current chain routes through `eigenvalue_modulus`, which needs the Frobenius roots to be **non-real** (`root_nonreal` requires the strict $t^2<4q$). The Hasse bound gives $t^2\le 4q$. The boundary $t^2=4q$ (supersingular, real eigenvalues $\pm\sqrt q$) occurs only for prime-power $q$ that is a perfect square; **for $q$ prime it never occurs** ($4q$ is not a perfect square, so $t^2<4q$ is automatic). So:
- For $q$ prime (the case `FunctionFieldRH`'s `b_e(p,t)` uses), Hasse already gives the strict $t^2<4q$ the chain needs.
- For general prime-power $q$, add a one-line boundary case to `FunctionFieldRH.lean`: when $t^2=4q$ the roots are real and equal $\pm\sqrt q$, so $|\alpha|^2=q$ directly. Small, do it in M-4.

## Effort, risk, upstreaming

- **Critical path:** M-1 (the isogeny degree API). It is the largest piece, genuinely research-engineering, and a flagship Mathlib contribution; the whole package (isogenies, degree, Hasse) is something Mathlib wants. Estimate: several expert-months, partly shared with the FLT project.
- **Immediate:** M-0 is a one-day lemma that can land now and de-risks the bridge.
- **Risk:** M-1/M-2 may need scheme-theoretic isogeny machinery not yet present; the elementary route minimizes this (it works with $\mathrm{End}(E)$ and degrees, not the full $C\times C$ surface), but still needs a real isogeny/degree development.

## Genus-$g$ generalization (out of scope here, noted)

Full Weil RH for genus $g$ goes through the Jacobian (an abelian variety) and the **Rosati involution positive-definiteness** (the general form of "$\deg$ is positive-definite"), the same structural argument scaled up, but requiring abelian varieties and Néron-Tate in Mathlib. The elliptic plan is the wedge; it also exercises exactly the positive-definite-quadratic-form pattern that the genus-$g$ Rosati form (08A's M1) and the Spec($\mathbb{Z}$) target (M4) need.

## Interface to the existing scaffold

The deliverable is a theorem of the shape
```
theorem hasse_bound {q : ℕ} (hq : q.Prime) (E : EllipticCurve (ZMod q)) :
    (trace_frobenius E) ^ 2 < 4 * q
```
(strict for $q$ prime; $\le$ in general, with the boundary handled in M-4), feeding `EllipticFrobeniusData`. Then `functionfield_RH_elliptic` becomes unconditional, and lever B has a complete, non-circular, machine-checked function-field RH for elliptic curves: the value-function floor the rest of the program (the $\mathrm{Spec}(\mathbb{Z})$ lift, M4) is transported against.

## References

- Elementary Hasse via the degree quadratic form: [arXiv:1212.2535](https://arxiv.org/pdf/1212.2535) ("Hasse theorem -- an elementary approach"); MIT 18.783 Elliptic Curves, Lecture 7 (point counting); Oxford W5 Hasse notes.
- The Lean group law on Weierstrass curves (any characteristic): ITP 2023 ([Dagstuhl LIPIcs.ITP.2023.6](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITP.2023.6)), in Mathlib.
- The FLT formalization project (Buzzard et al.), for adjacent arithmetic-geometry machinery.
- Project: [`optimizing_rh_for_ai.md`](optimizing_rh_for_ai.md) (lever B), [`../../lean/ZetaRH/FunctionFieldRH.lean`](../../lean/ZetaRH/FunctionFieldRH.lean) (the conditional chain this completes), [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) (the genus-$g$ / Spec($\mathbb{Z}$) Rosati generalization).
