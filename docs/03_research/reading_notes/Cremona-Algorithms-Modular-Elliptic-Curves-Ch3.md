# Reading notes: Cremona, *Algorithms for Modular Elliptic Curves*, Chapter III

> Computational-source note. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md). This is one
> chapter (42 PDF pages); read the §3 section list and §3.4 (Heights and the height
> pairing) in full, since that is the section the project uses. The §3.4 algorithms are
> the ones implemented in experiment 2P. Pages refer to the PDF. Read: §3 headers (TOC)
> + §3.4 (PDF pp. 70-73, the height pairing, Prop. 3.4.1, the finite-prime algorithm, the
> archimedean switch-series).

## One-line takeaway

Cremona Chapter III §3.4 is the implementation-ready statement of the canonical-height
decomposition: it gives the global identity `h_hat(P) = h_inf(P) + 2 log(c) + sum_{p | Delta, p does not divide c} h_p(P)`
(BSD normalization, double Silverman 1988's), Proposition 3.4.1 as the finite local-height
case-split (`A, B, C, N, M`), an explicit pseudocode "Silverman's algorithm for local heights
at finite primes," and the archimedean `h_inf` via Silverman's `x <-> x+1` switch-series.
This is the section the 2P script transcribes verbatim in its docstring.

## The points that matter, mapped to the project

1. **Section list of Chapter III.** §3.1 Terminology and notation (Weierstrass `b_i, c_i,
   Delta, j`, transformation law, minimal models); §3.2 the Kraus conditions / Laska-Kraus
   reduction; §3.3 computing the Mordell-Weil group (point search); §3.4 Heights and the
   height pairing; §3.5-3.6 the Mordell-Weil basis / saturation; §3.7 the period lattice
   (AGM); §3.8 isogenous curves; §3.9 twists and complex multiplication.
   -> §3.4 is the relevant section. §3.7 (period lattice via AGM) is the input to the
   archimedean height when computed the theta way (Cohen 7.5.7); 2L uses the AGM
   half-periods. The rest is curve bookkeeping the project gets from LMFDB / sympy.

2. **The height pairing and regulator (§3.4, PDF p. 71).** `h_hat(P,Q) = (1/2)(h_hat(P+Q)
   - h_hat(P) - h_hat(Q))`, the canonical height "is a real-valued quadratic form on E(Q),"
   and `R(E) = det(h_hat(Pi,Pj))`. Cremona states the algorithms are "taken from Silverman's
   paper [59]" (= Silverman 1988).
   -> This is the Gram-matrix the project builds in 2H/2M and decomposes by place in 2I.
   The "quadratic form" statement is the Faltings-Hriljac positive-definiteness 2H/2M
   validated against LMFDB regulators. Cremona is the implementation form of the pairing.

3. **The BSD normalization note (§3.4, PDF p. 72).** "There are two normalizations used,
   one of which is double the other and is the one appropriate for the Birch-Swinnerton-Dyer
   conjecture... all the formulae here are double those in the paper [59]."
   -> This is the resolution of the 2I/2P factor-of-2. Cremona's `h_hat = sum_v h_v` uses
   the doubled (BSD) normalization, which is the project's convention. 2I's empirical
   discovery ("the bare ansatz reconstructed `h_hat/2`") is exactly this factor; 2P's
   docstring confirms the `x2` normalization. Cremona is the clearest statement of which
   normalization to use and why.

4. **Proposition 3.4.1: the finite local-height case-split (PDF p. 72).** For `P = (x,y)`
   on a model minimal at `p`, with `psi_2(P) = 2y+a1 x+a3`, `psi_3(P) = 3x^4+b2 x^3+3b4 x^2
   +3b6 x+b8`: (a) if `ord_p(3x^2+2a2 x+a4-a1 y) <= 0` or `ord_p(psi_2) <= 0` then
   `h_p = max(0, -ord_p(x)) log p`; (b) else if `ord_p(c4)=0`, `N=ord_p(Delta)`,
   `M=min(ord_p(psi_2), N/2)`, then `h_p = (M(M-N)/N) log p`; (c) else if `ord_p(psi_3) >=
   3 ord_p(psi_2)` then `h_p = -(2/3) ord_p(psi_2) log p`; (d) else `h_p = -(1/4) ord_p(psi_3)
   log p`. The four cases are good reduction, multiplicative, additive types III/III*/I_m,
   and additive IV/IV*.
   -> This is the finite-height algorithm transcribed VERBATIM in the 2P docstring and
   implemented in [`e2p_silverman_local_heights.py`](../../../experiments/arithmetic_geometric/e2p_silverman_local_heights.py).
   2P's corrected attribution on the I_2 curve (the `-0.347` from `p=2`) is case (b) applied
   prime by prime. 2O's period-2 I_n behavior is case (b)'s `M(M-N)/N` over the component
   group. This is the single most directly-used result in the 07 folder.

5. **The finite-prime pseudocode and the archimedean switch-series (§3.4, PDF pp. 72-73).**
   Cremona gives explicit pseudocode (`N=ord(p,Delta); A=...; B=...; C=...; M=min(B,N/2);
   IF A<=0 OR B<=0 THEN L=max(0,-ord(p,x)) ELSE IF ord(p,c4)=0 THEN L=M*(M-N)/N ...`) and
   states the archimedean `h_inf` uses Tate's series amended by Silverman: switch between
   `x` and `x' = x+1` whenever `|x|` or `|x'|` drops below `1/2`, with truncation error
   `< (1/2) 10^-d` for `N >= (5/3)d + 1/2 + (3/4) log(7 + (4/3) log H)`.
   -> The 2P docstring's finite pseudocode (`if A<=0 or B<=0: L=max(0,-ord_p(x))` etc.) and
   the term-count formula `N=ceil((5/3)d + 1/2 + (3/4)log(7+(4/3)log H))` are copied from
   exactly here. Cremona §3.4 is the literal source of the 2P algorithm, both the finite
   case-split and the archimedean switch-series with its error bound.

## What this changes for the program

- **2P is a faithful transcription of Cremona §3.4.** The finite case-split (Prop. 3.4.1),
  the pseudocode, the archimedean switch-series, and the `N`-term formula are all here in
  the BSD normalization. The project can cite Cremona, *Algorithms for Modular Elliptic
  Curves*, §3.4 as the reference implementation behind the validated decomposition.
- **The normalization question is settled.** Cremona's explicit "double those in [59]" note
  is the clearest statement of the BSD convention the project uses; it closes the
  factor-of-2 that 2I rediscovered empirically.
- **The Kodaira-type meaning of the four cases is spelled out.** Cremona labels case (b) as
  multiplicative (I_m) and (c)/(d) as additive, which is the link from the local-height
  algorithm to the I_n component-group structure 2O validated. Useful for reading bad-prime
  contributions as component-group data, not just numbers.

## Status

- **Honest depth:** read the §3 section headers and §3.4 in full (PDF pp. 70-73): the
  pairing/regulator definitions, the normalization note, Prop. 3.4.1, the finite-prime
  pseudocode, and the archimedean switch-series + error bound. Skimmed §3.1 (notation /
  `b_i, c_i` formulas, which match the project's) and §3.7 (period lattice / AGM). Did not
  read §3.2-3.3, §3.5-3.6, §3.8-3.9 (Mordell-Weil computation, saturation, isogenies),
  which the project gets from LMFDB.
- **Used by:** experiment 2P (the §3.4 algorithms transcribed verbatim in the docstring and
  implemented), and the normalization is the resolution of the 2I/2P factor-of-2. Cited in
  the 07 folder index as "the §3.4 local-height conventions used in 2P."
- **Direction 8 bearing:** §3.4 is the implementation of the per-place height decomposition
  on a single arithmetic surface: `h_inf` (the `A_arch` archimedean diagonal) + `2 log(c)`
  + the finite bad-prime case-split, summing to the canonical height whose positive-definite
  pairing is the validated single-surface signature.
