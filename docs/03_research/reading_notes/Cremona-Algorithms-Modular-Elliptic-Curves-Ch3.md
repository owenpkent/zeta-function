# Reading notes: Cremona, *Algorithms for Modular Elliptic Curves*, Chapter III

> Computational-source note, §3.4 read IN FULL. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md). One chapter
> (42 PDF pages, book pp. 62-103). Read the §3 section structure (§3.1 notation, §3.2
> Kraus-Laska-Connell + Tate, §3.3 torsion / Mordell-Weil I, §3.4 heights, §3.5 Mordell-Weil
> II) and §3.4 (Heights and the height pairing) in full -- the section the project uses. The
> §3.4 algorithms are implemented verbatim in experiment 2P. Pages refer to the BOOK page
> numbers printed on each page.
> Read: §3 headers (pp. 62-64, 70-71, 75) + §3.4 in full (book pp. 71-75, the height
> pairing, the BSD normalization footnote, Prop. 3.4.1, the finite-prime pseudocode, the
> archimedean switch-series pseudocode + error bound).

## One-line takeaway

Cremona Chapter III §3.4 is the implementation-ready statement of the canonical-height
decomposition: the global identity (3.4.2) h-hat(P) = h_inf(P) + 2 log(c) + sum_{p | Delta,
p does not divide c} h_p(P) (BSD normalization, double Silverman 1988's); Proposition 3.4.1
as the finite local-height case-split (A, B, C, N, M); explicit pseudocode for "Silverman's
algorithm for local heights: finite primes" and "real component"; and the archimedean
h_inf via Silverman's x <-> x+1 switch-series with the N-term error bound. This is the
section the 2P script transcribes verbatim in its docstring.

## Technical content (section by section)

**§3 structure (book pp. 62-101).** §3.1 Terminology: the Weierstrass b_i, c_4, c_6,
Delta = -b2^2 b8 - 8b4^3 - 27b6^2 + 9b2b4b6, j = c4^3/Delta, the transformation law (3.1.3)
under T(r,s,t,u), reduced minimal models, Kraus's conditions (Prop 3.1.1). §3.2 the
Laska-Kraus-Connell minimal-model algorithm (factor gcd(c6^2, Delta) to find the scaling
u) and Tate's algorithm. §3.3 finding all torsion points (and Mordell-Weil basis search,
part I). §3.4 Heights and the height pairing. §3.5-3.6 Mordell-Weil basis / saturation via
the height-pairing regulator. §3.7 period lattice (AGM). §3.8-3.9 isogenies, twists, CM.

**The height pairing and regulator (§3.4, book p. 71).** h-hat(P, Q) = (1/2)(h-hat(P+Q) -
h-hat(P) - h-hat(Q)); "the canonical height h-hat is a real-valued quadratic form on
E(Q)"; the regulator R(E) = |det(h-hat(P_i, P_j))|, used in §3.5 to find dependence
relations among points of infinite order. The naive height is h(P) = log max(|a|, c^2) for
P = (a/c^2, b/c^3). Cremona states "the height algorithms in this section are taken from
Silverman's paper [59]" (= Silverman 1988).

**The BSD normalization footnote (§3.4, book p. 72).** The famous footnote: "I am grateful
to Gross for explaining this to me, after I found that apparently the two sides of the
Birch-Swinnerton-Dyer conjecture disagreed by a factor of 2^r!" The body: "there are two
normalizations used, one of which is double the other and is the one appropriate for the
Birch-Swinnerton-Dyer conjecture (resulting in a regulator 2^r times as large). In
Silverman's paper he uses the other (smaller) normalization. Thus all the formulae here are
double those in the paper [59]."

**Proposition 3.4.1: the finite case-split (book p. 72).** For E/Q minimal at p,
P = (x, y), psi_2 = 2y + a1 x + a3, psi_3 = 3x^4 + b2 x^3 + 3 b4 x^2 + 3 b6 x + b8:
- (a) if ord_p(3x^2 + 2a2 x + a4 - a1 y) <= 0 OR ord_p(psi_2) <= 0, then
  h_p(P) = max(0, -ord_p(x)) log p  [good / nonsingular reduction];
- (b) else if ord_p(c4) = 0, set N = ord_p(Delta), M = min(ord_p(psi_2), N/2), then
  h_p(P) = (M(M-N)/N) log p  [multiplicative, type I_m];
- (c) else if ord_p(psi_3) >= 3 ord_p(psi_2), then h_p(P) = -(2/3) ord_p(psi_2) log p
  [additive IV / IV*];
- (d) otherwise h_p(P) = -(1/4) ord_p(psi_3) log p  [additive III / III* / I_m*].
This is Silverman 1988 Theorem 5.2 specialized to Q, in the doubled BSD normalization. The
total over primes dividing c is 2 log(c), giving (3.4.2)
h-hat(P) = h_inf(P) + 2 log(c) + sum_{p | Delta, p does not divide c} h_p(P) (this formula
"appears in [62]," = Silverman 1997).

**Finite-prime pseudocode (book p. 73).** "Silverman's algorithm for local heights: finite
primes": compute b/c invariants, N = ord(p, Delta), A = ord(p, 3x^2+2a2x+a4-a1y),
B = ord(p, 2y+a1x+a3), C = ord(p, 3x^4+b2x^3+3b4x^2+3b6x+b8), M = min(B, N/2); IF A <= 0 OR
B <= 0 THEN L = max(0, -ord(p, x)) ELSE IF ord(p, c4) = 0 THEN L = M(M-N)/N ELSE IF
C >= 3B THEN L = -2B/3 ELSE L = -C/4; RETURN L log(p).

**Archimedean switch-series (book pp. 73-74).** h_inf(P) = log|x| + (1/4) sum_{n>=0} 4^-n
c_n (Tate, amended by Silverman to switch between x and x' = x+1 when |x| or |x'| < 1/2,
and to apply over C). Error < (1/2) 10^-d for N >= (5/3)d + 1/2 + (3/4) log(7 + (4/3) log H
+ (1/3) log max(1, |Delta|^-1)) terms, H = max(4, |b2|, 2|b4|, 2|b6|, |b8|) (last term
vanishes for Z-curves). Pseudocode "real component": b2' = b2-12, b4' = b4-b2+6,
b6' = b6-2b4+b2-4, b8' = b8-3b6+3b4-b2+3; IF |x| < 0.5 THEN t = 1/(x+1); beta = 0 ELSE
t = 1/x; beta = 1; loop computing w, z (or primed), switching when |w| > 2|z|.

**Global pseudocode (book p. 75).** "Algorithm for computing global canonical heights":
h = real_height(P) + log(d); for p | Delta with p not dividing d, h += local_height(p, P).

## Points mapped to the project

1. **§3.4 is the literal source of the 2P algorithm.** The finite-prime pseudocode and the
   archimedean "real component" pseudocode (including the b' formulas, the |x| < 0.5 switch,
   and the N-term formula N = ceil((5/3)d + 1/2 + (3/4) log(7 + (4/3) log H))) are copied
   into the
   [`e2p_silverman_local_heights.py`](../../../experiments/arithmetic_geometric/e2p_silverman_local_heights.py)
   docstring and implementation verbatim. ->

2. **The height pairing is the Gram matrix of 2H/2M/2I.** Cremona's "h-hat is a real-valued
   quadratic form" and R(E) = |det(h-hat(P_i, P_j))| is the Faltings-Hriljac
   positive-definiteness 2H/2M validated against LMFDB regulators; 2I decomposes it by
   place. The §3.5 saturation use (finding dependence via det = 0) is the computational
   meaning of the signature. ->

3. **The Gross footnote SETTLES the factor-of-2.** Cremona's "all the formulae here are
   double those in the paper [59]" is the clearest statement of the BSD convention the
   project uses. 2I's empirical "the bare ansatz reconstructed h-hat/2" is exactly this
   factor; 2P's docstring confirms the x2 normalization. The footnote even records that BSD
   itself was off by 2^r until this was pinned -- the same normalization care the project's
   regulator positivity depends on. ->

4. **Prop 3.4.1 is the single most directly-used result in the 07 folder.** The four cases
   labeled good / multiplicative (I_m) / additive (IV, IV*) / additive (III, III*, I_m*)
   are the Kodaira-type meaning of the bad-prime contributions. 2P's corrected I_2-curve
   attribution (the -0.347 from p=2) is case (b) applied prime by prime; 2O's period-2 I_n
   behavior is case (b)'s M(M-N)/N over the component group. ->

5. **(3.4.2) with the 2 log(c) term is the decomposition 2P validated.** This is Silverman
   1997's Eq. (3) in the doubled normalization; 2P's h_inf + sum_p h_p = h-hat is exactly
   this identity, validated to ~1e-8. ->

## What this changes for the program

- **2P is a faithful transcription of Cremona §3.4.** The finite case-split (Prop. 3.4.1),
  both pseudocodes, and the N-term formula are all here in the BSD normalization; the
  program cites Cremona §3.4 as the reference implementation behind the validated
  decomposition.
- **The normalization question is settled.** The Gross footnote is the clearest statement
  of the BSD convention; it closes the factor-of-2 that 2I rediscovered empirically.
- **The Kodaira-type meaning of the four cases is spelled out.** Cremona labels case (b)
  multiplicative (I_m) and (c)/(d) additive, the link from the local-height algorithm to
  the I_n component-group structure 2O validated. Bad-prime contributions read as
  component-group data, not just numbers.

## Status

- **Honest depth:** read the §3 section headers and §3.4 in full (book pp. 71-75): the
  pairing/regulator definitions, the Gross normalization footnote, Prop. 3.4.1, both
  pseudocodes (finite primes, real component), the global-height pseudocode, and the
  N-term error bound. Skimmed §3.1 (the b/c invariant formulas, which match the project's)
  and §3.7 (period lattice / AGM). Did not read §3.2-3.3, §3.5-3.6, §3.8-3.9 (Mordell-Weil
  computation, saturation, isogenies), which the project gets from LMFDB.
- **Used by:** experiment 2P (the §3.4 algorithms transcribed verbatim in the docstring and
  implemented), and the normalization footnote is the resolution of the 2I/2P factor-of-2.
- **Direction 8 bearing:** §3.4 is the implementation of the per-place height decomposition
  on a single arithmetic surface: h_inf (the A_arch archimedean diagonal) + 2 log(c) + the
  finite bad-prime case-split, summing to the canonical height whose positive-definite
  pairing is the validated single-surface signature.
