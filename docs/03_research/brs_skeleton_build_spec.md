# BRS skeleton build spec: does the functional equation buy any conditioned economy at $\{k\log p\}$?

**Date**: 2026-08-18. **Status**: SPEC, to be executed as `experiments/spectral/e1aa_brs_skeleton.py`.
**Precedent**: [`theta_s4_build_spec.md`](theta_s4_build_spec.md) (spec-then-build, the form-side pivot rung).
**Sources**: [`reading_notes/viazovska_s4_sweep.md`](reading_notes/viazovska_s4_sweep.md) §5 (the handoff), [`../../experiments/spectral/e1o_s4_carrier.md`](../../experiments/spectral/e1o_s4_carrier.md) (the instrument), [`trojan_horse_m4.md`](trojan_horse_m4.md) (the conservation law this tests).

## 0. Why this spec exists

LEARNINGS #173's T1 sweep found the Viazovska corpus FITS-IN-PART and handed
forward one executable: the corpus's own log-node object is
**Bondarenko-Radchenko-Seip** (arXiv:2005.02996), whose Theorem 1.1 pairs the
nodes $\{\log n/(4\pi)\}$ with the zeta zero multiset, exactly critically, with
Riemann-Weil recovered as a consequence. T1 argued on paper that transferring
this to $\{k\log p\}$ costs the Euler product for the node restriction and M4
for the one-sided use. **This spec turns that argument into a measurement.**

The question, stated so it can come out either way:

> Does the functional equation buy any *conditioned economy* at the prime
> sublattice $\{k\log p\}$ beyond what the all-$n$ comb $\{\log n\}$ already
> gives, without evaluating the zero side?

An economy would be an S4-class finding and would matter. The pre-registered
expectation is that it does not, and that whatever economy appears is the
known parity factor of 2 rather than the $o(M)$ the S4 spec needs.

## 1. The instrument, reused verbatim

e1o's `cheapness(logs, L, N, K)`: build the evaluation matrix of the decimated
space $V_K = \mathrm{span}\{e^{2\pi i (Km)u/L}\}$ at the comb, and report

$$\text{cost ratio} = \frac{\mathrm{rank}(A_{\text{ev}})}{\#\text{conditions}}$$

alongside the smallest retained singular value, so that a lenient-rank
"economy" with terrible conditioning is visible as the superresolution mirage
it would be rather than a mechanism. Ratio $1.0$ = full price, no economy;
ratio $< 1$ = each condition is buying more than one.

Established baselines this must reproduce (e1o T4c/T4d): ratio $= 1.0$ exactly
at $\{\log p\}$ for every $(K, \lambda)$; ratio $< 0.75$ at a commensurate AP
comb; ratio $\le 0.21$ on the single circle $\mathbb{R}/(\log p)\mathbb{Z}$
where $\{k\log p\}$ *is* the AP.

## 2. What "the FE" is, concretely, on this skeleton

BRS's functional equation is $s \mapsto 1-s$. On the log-circle coordinate it
acts as the reflection $u \mapsto -u$, so the FE-respecting subspace is the
**even** subspace $V_K^+ = \{f \in V_K : f(-u) = f(u)\}$, of dimension
$\lceil \dim V_K/2\rceil$ rather than $\dim V_K$.

That is the entire FE content available without touching the zero side. The
*other* half of BRS's mechanism, the pairing of the node comb against its dual
(the zeros), is precisely what K1 forbids evaluating, and is carried
symbolically throughout: the probe never reads a zero, and a guard on
`mp.zetazero` and the D-H scanner enforces it.

## 3. The four cells

| | comb | space | what it isolates |
|---|---|---|---|
| B1 | $\{\log n/(4\pi)\}_{n \le N}$ | $V_K$ | the all-$n$ baseline, BRS's own node set |
| B2 | $\{k\log p\}$ | $V_K$ | the prime sublattice, no FE |
| B3 | $\{\log n/(4\pi)\}_{n \le N}$ | $V_K^+$ | all-$n$ with the FE |
| B4 | $\{k\log p\}$ | $V_K^+$ | the sublattice with the FE: the cell the question is about |

The measurement is the pair $(\text{ratio}(B4), \text{ratio}(B2))$ against
$(\text{ratio}(B3), \text{ratio}(B1))$. An FE economy specific to the primes
would show as $B4/B2 < B3/B1$, i.e. the FE helping *more* at the sublattice
than at the full comb.

## 4. Controls, all mandatory

- **Beurling twin** ([`../../experiments/_shared/beurling.py`](../../experiments/_shared/beurling.py)): a
  density-matched generalized-prime comb with an Euler product and **no**
  additive lattice, hence no FE. Any economy the FE is credited with must be
  ABSENT here. If B4 and its Beurling counterpart agree, the economy is not
  the FE's.
- **Parity control**: a non-arithmetic comb (equally spaced, or the all-$n$
  comb) run through the same even-subspace restriction. Parity is not
  arithmetic, so the factor it buys must be identical there. This is what
  separates "the FE bought something" from "halving a dimension bought
  something".
- **Conditioning**: the smallest retained singular value reported in every
  cell, per e1o's own guard.
- **D-H**: not applicable to the comb geometry (D-H has no Euler product, so
  no prime sublattice); noted rather than faked.

## 5. Pre-registered expectation and exits

**Expectation.** $B3/B1 = B4/B2 \approx 1/2$, the trivial parity economy, with
the ratio at $\{k\log p\}$ in the full space staying pinned at $1.0$; the
Beurling twin reproducing the parity factor exactly, since parity is not
arithmetic. Net: the FE buys parity and nothing else, and the economy the S4
spec needs would have to come from the zero side, which is M4.

**Exit if that is what happens.** The corpus's wall is identified with #171's
chain wall as provably the same joint, and the BRS route is recorded as a
restatement of M4 rather than a detour around it. Frontier UNMOVED, one more
route priced.

**Exit if it does not.** Any cell with $B4/B2$ materially below $B3/B1$, with
good conditioning, and ABSENT in the Beurling twin, is an S4-class finding:
the FE buying prime-specific economy without the zero side. That would reopen
the corridor's central question and takes priority over everything else on the
board. The conditioning number is the first thing to check, because the
superresolution mirage is the expected way for this to look true and be false.

## 6. What this cannot do

It cannot prove BRS's mechanism does not transfer; it can only measure whether
the FE-available part of it buys anything at the prime sublattice on this
finite skeleton. The zero side is symbolic by construction, so the probe is
blind to exactly the half that BRS actually uses, which is the point: that
half is M4, and a probe that could see it would be a probe that had already
solved the problem.
