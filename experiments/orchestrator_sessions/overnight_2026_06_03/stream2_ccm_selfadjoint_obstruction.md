# Stream 2 build -- 2CCM.1: the self-adjointness obstruction of the CCM determinant

> STAGED overnight 2026-06-03. NOT committed. For morning review by Owen + main-agent
> verification. Every number below is from `stream2_ccm_selfadjoint_obstruction.py` run
> from the repo root; the main agent must independently re-derive before anything is
> recorded in `LEARNINGS.md`. Distinguishes PROVED / CITED / STRUCTURAL-READING throughout.

## The claim (one line)

The Connes-Consani-Moscovici 2025 "det -> Xi" route (arXiv:2511.22755) is RH-equivalent,
not RH-reducing, and the precise mechanism is SELF-ADJOINTNESS: a self-adjoint generator
forces every determinant zero onto Re(s)=1/2, so "det -> Xi" for a self-adjoint H IS the
Hilbert-Polya statement of RH. The content that actually carries RH is the DEFINITENESS of
the metric (the polarization, 08A M4), demonstrated computationally by the Krein-space probe.

## Why this is NEW vs LEARNINGS #40-#44

- #44 (2PR.1): a regularized det is a class function of the eigenvalue MULTISET, hence
  "blind to the signature." TRUE but incomplete: it explains why the det cannot SEE the
  signature, not why "det -> Xi" cannot be a shortcut.
- This coordinate names the mechanism #44 omitted: the det's zeros sit at the eigenvalues,
  and self-adjointness makes those REAL, so the route to the zeros (det -> Xi) already
  asserts RH by asserting self-adjointness. The signature is not absent from the det; it is
  PRESUPPOSED in the choice of a self-adjoint H on a definite Hilbert space.
- #43 (2DB.1) is the pairing-side mirror (the de Branges pairing sees the zeros with the
  wrong, too-strong positivity). This is the determinant-side mirror: the determinant sees
  the zeros only with the RH-built-in positivity (self-adjointness = a definite metric).

## What is computed (numbers from the script; re-derive before recording)

- PART 1 (PROVED, linear algebra). 200 random self-adjoint A (8x8), H = 1/2 + iA: max
  |Im(eig A)| = 8.2e-16, max |Re(zero of det) - 1/2| = 8.3e-16. All on-line. The executable
  Hilbert-Polya tautology.
- PART 2 (PROVED, arithmetic). To host D-H's off-line zero 0.8085 + 85.699i a generator A
  needs eigenvalue 85.699 - 0.3085i (non-real), so A is non-self-adjoint; minimal anti-self-
  adjoint part ||A - A^*|| = 2|Re(rho) - 1/2| = 0.617.
- PART 5 (PROVED, the punchline). Same H = 1/2 + iA but A J-self-adjoint for an INDEFINITE
  metric J = diag(+1,+1,+1,+1,-1,-1,-1,-1): max |Re(zero) - 1/2| = 3.67 (OFF the line),
  84.1% of eigenvalues go complex; the definite control (J=I) stays on-line to 6.7e-16. Off-
  line zeros appear EXACTLY when the metric loses definiteness => the signature = metric
  definiteness = the polarization (08A M4). Determinant-side statement of #30.
- PART 3 (PROVED, classical). CCM prime data {log p : p<=x}: the oscillatory critical-line
  prime sum at t=14.1347 gives -4.01, -4.78, -7.00, -3.86, +0.31 for x = 50..20000 -- no
  limit. The zeros live in the continuation; "det -> Xi" is genuinely the open content
  (reproduces #42).
- PART 4 (PROVED, reproduces #20/#41/#43). D-H off-line zero refined to 0.8085172 +
  85.6993i (|f| = 6.9e-40); D-H von Mangoldt leaks off prime powers (n=6: 1.94, n=14: 2.85,
  ...), so no Euler product => CCM operator UNBUILDABLE. K2 is stacked: categorical (no Euler
  product, no operator) AND spectral (self-adjoint H cannot host an off-line zero).

## Honest scope

- CITED, NOT verified in-file: that CCM's H is self-adjoint and that their det -> Xi. From
  the abstract only. The self-adjointness is the LOAD-BEARING import (VERIFIER target V1). If
  the actual operator is non-self-adjoint (e.g. a Pollicott-Ruelle transfer operator), this
  coordinate FALSIFIES and reduces to #44.
- STRUCTURAL READING (mine): pinning CCM's 2025 claim to the Hilbert-Polya tautology is a
  reading, not a theorem about their paper. It neither proves nor disproves their
  convergence; it explains why that convergence is not a shortcut.
- This is a NEGATIVE / no-shortcut coordinate. It does NOT construct the Weil cohomology,
  does NOT prove RH, does NOT advance M3/M4. It sharpens #44 and gives a categorical+spectral
  K2 of the newest frontier construction, and locates the gap precisely: a non-circular
  PROOF that the natural global generator is self-adjoint (metric definite) IS the arithmetic
  Rosati positivity. The signature is the self-adjointness.

## Falsifiable prediction

If VERIFIER confirms H is self-adjoint in arXiv:2511.22755: (i) any honest "det -> Xi" proof
is RH-equivalent (no shortcut); (ii) the D-H analogue is unbuildable (no Euler product) AND
spectrally forbidden (self-adjoint H cannot have an off-line determinant zero). If H is found
non-self-adjoint, the coordinate is FALSIFIED to #44.

## VERIFIER targets

- V1. Confirm self-adjointness of H_{N,lambda} in arXiv:2511.22755 (load-bearing).
- V2 (Lean). A = A^* => spectrum(A) subset R => zeros of det(s - (1/2 + iA)) have Re(s)=1/2.
- V3. State "det -> Xi for self-adjoint H => RH" as the no-shortcut lemma (R3.5 family).

## ADVERSARY tests

- A1. Is CCM's perturbation genuinely self-adjoint or a similarity to one (no real-spectrum
  guarantee)? Check the inner product / J-symmetry.
- A2/A3. A J-self-adjoint (Krein-space, indefinite J) H carries off-line zeros (PART 5
  confirms), so PART 1's tautology needs the metric to be DEFINITE. The definiteness is the
  polarization. ADVERSARY should check whether CCM's metric could be secretly indefinite
  (it should not be, for a genuine Hilbert space spectral triple).
