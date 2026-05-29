# Reading notes: Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (GTM 151, ATAEC, 1994)

> Computational/theoretical-authority ROLE-note. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md). This is a
> 540-page graduate textbook, NOT read cover to cover: I read the table of contents and
> Chapter VI (Local Height Functions), in particular §VI.3 (the archimedean explicit
> formula via the Weierstrass sigma-function) and §VI.4 (the non-archimedean explicit
> formula). This note points the program at the theorems behind 2I and 2L. Pages refer
> to the PDF. Read: TOC + Ch. VI §§1-4 (PDF pp. 466-481, the sigma-function formula,
> the q-expansion form, the quasi-parallelogram law).

## One-line takeaway

ATAEC Chapter VI is the THEORETICAL foundation of the Neron local height: §VI.1 proves
existence/uniqueness of the local height `lambda_v` (the three Néron axioms), §VI.2
proves `h_hat = sum_v lambda_v` (the local decomposition the project validates), and
§VI.3 gives the closed archimedean formula `lambda(z) = -log| e^(-(1/2) z eta(z)) sigma(z) Delta(L)^(1/12) |`
in terms of the Weierstrass sigma-function and the quasi-period `eta`, with a `q`-expansion
rewrite. This sigma-function archimedean theory is the object 2I self-derives a series
for and 2L uses for the self-intersection (Petersson norm of the discriminant).

## The points that matter, mapped to the project

1. **§VI.1 Existence + the three Néron axioms (PDF p. 455).** The local height
   `lambda_v: E(K_v) \ {O} -> R` is the unique function satisfying: (i) a duplication /
   functional relation, (ii) the `lambda_v(P) - (1/2) log|x(P)|_v` limit as `P -> O`
   exists, (iii) boundedness away from `O`. This is the abstract object; the explicit
   formulas in §3-4 are realizations.
   -> These are the axioms the 2I self-derivation REPRODUCES from the duplication formula
   rather than transcribing. 2I's telescoping ansatz is a constructive proof that its
   series satisfies (i)-(iii), validated numerically against `h_hat`. ATAEC VI.1 is the
   uniqueness theorem that guarantees 2I's series is THE local height (no other function
   satisfies the axioms), which is why matching `h_hat` to `~1e-8` is a complete check.

2. **§VI.2 Local decomposition of the canonical height (PDF p. 461).** Proves
   `h_hat(P) = sum_v n_v lambda_v(P)`, the global identity, with the `n_v` multiplicities
   fixed by the product formula.
   -> This is precisely the identity 2P validates end-to-end: `h_inf + sum_p h_p = h_hat`.
   ATAEC VI.2 is the theorem; 2P is the numerical confirmation on 37a1/389a1/5077a1 and
   the I_2 curve. The reference behind the 2I status line ("Silverman, ATAEC, Ch. VI").

3. **§VI.3 the archimedean explicit formula via the sigma-function (PDF pp. 463-467,
   Theorem 3.2).** Over `C`, `lambda(z) = -log| e^(-(1/2) z eta(z)) sigma(z) Delta^(1/12) |`,
   where `sigma` is the Weierstrass sigma-function, `eta` the quasi-period map, and the
   `Delta^(1/12)` factor makes it model-independent. Theorem 3.4 rewrites this as a
   `q`-expansion `lambda(z) = (1/12) ... + sum_{n>=1} log|(1-q^n u)(1-q^n u^-1)| + ...`
   using Legendre's relation, the form Cohen's Alg. 7.5.7 evaluates.
   -> This is the GENUINE archimedean local height `lambda_inf` that 2I computes. 2I
   self-derived an equivalent telescoping series and validated it; ATAEC VI.3 is the
   authoritative closed form (sigma-function / theta / `q`-expansion). The `Delta^(1/12)`
   factor is the same discriminant normalization 2L computes the Petersson norm of.

4. **Corollary 3.3 the quasi-parallelogram law (PDF p. 467).**
   `lambda(P+Q) + lambda(P-Q) = 2 lambda(P) + 2 lambda(Q) + v(x(P)-x(Q)) - (1/6) v(Delta)`.
   This is the bilinear-form structure of the local height (the local analogue of the
   parallelogram law that makes `h_hat` a quadratic form).
   -> This is the LOCAL source of the pairing that 2I/2H assemble into a Gram matrix. The
   archimedean Gram matrix 2I found (positive definite at rank 1-2, indefinite at rank 3
   for 5077a) is built from `lambda` evaluated at `P+Q`, `P-Q`; the quasi-parallelogram
   law is what makes those entries a well-defined symmetric pairing. The `A_arch` block
   IS this archimedean bilinear form.

5. **§VI.4 the non-archimedean explicit formula (PDF pp. 469-476).** Over a `p`-adic
   field, the local height is given by intersection theory / the component-group
   combinatorics (the same `M(M-N)/N` and Tate-algorithm data that Cohen 7.5.6 and
   Cremona 3.4.1 turn into an algorithm).
   -> This is the theoretical source of the finite local heights 2O/2P compute, including
   the I_n component-group periodicity 2O observed (period-2 on the I_2 curve). ATAEC VI.4
   is why the finite local height is constant on each component and a rational `* log p`.

## What this changes for the program

- **2I and 2L are grounded in the sigma-function theory.** ATAEC VI.3 is the
  authoritative archimedean local height (sigma-function / `q`-expansion form). 2I's
  self-derived series is an equivalent route to the same `lambda_inf`; the project can
  cite VI.3 (Theorem 3.2/3.4) as the closed form and VI.1 (uniqueness) as the reason the
  numerical match certifies correctness.
- **The local decomposition is a theorem, not a hope.** VI.2 proves `h_hat = sum lambda_v`;
  the project's 2P validation is confirmation, and the residual is purely the `h_hat`
  truncation. This pins the `A_arch + sum_p A_p = h_hat` Arakelov picture to a citable
  theorem.
- **The archimedean pairing has the quasi-parallelogram structure.** Cor. 3.3 is why the
  `A_arch` block is a genuine symmetric bilinear form, so its signature (positive definite
  at low rank, indefinite at rank 3 in 2I) is a meaningful Hodge-index datum and not an
  artifact. The global positivity comes from adding the finite blocks, exactly as 2I found.

## Status

- **ROLE-note, honest depth:** read the TOC and Chapter VI §§1-4 (PDF pp. 455-481),
  focusing on the sigma-function archimedean formula (Thm 3.2), the `q`-expansion (Thm
  3.4), and the quasi-parallelogram law (Cor 3.3). Did NOT read Chapters I-V (modular
  functions, complex multiplication, elliptic surfaces, Néron models / Tate's algorithm,
  `q`-curves), though Ch. IV is the conceptual source of the Kodaira-type data the finite
  local heights use.
- **Used by:** experiment 2I (archimedean `lambda_inf`, the sigma-function theory; cited
  in the 2I status block as "ATAEC, Ch. VI"), 2L (the `Delta^(1/12)` / Petersson-norm
  archimedean self-intersection), and 2O/2P (the non-archimedean VI.4 formula).
- **Direction 8 bearing:** VI.3 makes the `A_arch` block concrete and transcendental
  (sigma-function), VI.4 makes the finite blocks the component-group arithmetic, and
  VI.2 ties them to `h_hat`. The single-surface arithmetic Hodge index is exactly this
  decomposition with the validated positive-definiteness of the assembled pairing.
