# 2SS: the MC.4 / M4 smallest-case attempt (K1-circular, the coupling is the residual)

> Experiment [`e2ss_mc4_attempt.py`](e2ss_mc4_attempt.py). A BUILDER attempt at MC.4 (the open kernel of the modular-carrier program, = M4), adversarially honest. Result recorded as LEARNINGS #103. Follows MC.1/MC.2/MC.3 (e2pp #100, e2qq #101, e2rr #102).

## The attempt

MC.4 asks: prove the C_E-twisted form on the finite-prime modular (Bost-Connes type III$_1$) carrier is positive on the primitive part, **carrying** the Frobenius trace $t$, **without RH input**. The smallest-case construction: the BC truncation on a finite prime set $P$, with the genus-1 Euler-Sen primitive block attached per prime, $Q_p=\Omega(\cdot,C_E\cdot)=B_E(p,t_p)/\sqrt{4p-t_p^2}$ (positive-definite iff $|t_p|<2\sqrt p$, the local Hasse-Weil window), assembled as the KMS-weighted block-direct-sum $M=\bigoplus_p p^{-\beta}Q_p$. "Positive on the primitive part" $=$ every $|t_p|<2\sqrt p$ $=$ local RH at every prime.

## The result: K1-circular, sharply and concretely

The disciplines run; the numbers (56-row sweeps, recorded in `e2ss_mc4_attempt.npz`):

- **fq-shadow PASSES.** The twist is positive-definite exactly on the Hasse-Weil window (0 mismatches across the sweep; e.g. $p=5$: $t=4$ PD, $t=5$ not), reproducing Weil's $|\alpha|=\sqrt q$.
- **K2 firewall PASSES by construction.** $\zeta$'s comb is non-negative (carrier forms); D-H's comb is negative at $n=3$ (no positive Gibbs state, no carrier). Inherited from MC.3.
- **K1 FAILS (circular).** The modular weight grading $\log\Delta$ is t-independent (529 weights, identical for every trace assignment), so the carrier does **not** supply $t_p$. The twist signature responds to $t$ only through $C_E$, which the modular structure does not contain. Positivity $=$ (every $|t_p|<2\sqrt p$) $=$ local RH at every $p$; asserting it asserts the conclusion.

**The mechanism (the sharp part).** The modular/KMS carrier lives at $\beta>1$, i.e. $\mathrm{Re}(s)>1$, the region of absolute convergence of the Euler product. The local GL$_2$ factor $1-t_p p^{-s}+p^{1-2s}$ has its zeros on $\mathrm{Re}(s)=1/2$ exactly at $|t_p|=2\sqrt p$, split off the line as $|t_p|$ grows, and cross into $\mathrm{Re}(s)>1$ (where a $\beta>1$ carrier could see them) only at the full Hasse bound $|t_p|=p+1$. The entire nontrivial off-line range $2\sqrt p<|t_p|<p+1$ is **invisible** to the carrier. That is precisely why $\log\Delta$ is t-blind: it is the marginal-positivity wall localized per prime, the same shape as the M2.6 stealth window.

This is the **same M4**, reduced to K1-circularity. It is not yet the #80 continuous-archimedean-spectrum wall directly (at finite truncation the block-sum is full rank, no continuous part); #80 is what the **global coupling** would hit if one tried to force $t$ intrinsically rather than assert it. The block-direct-sum has no literal numerical stealth window only because it is decoupled per prime, which is the same coin as "positive iff you assume each $t$ in-window."

## The residual (what MC.4 / M4 still needs)

Construct the **coupling** between the per-prime twisted blocks (the global Frobenius/Lefschetz signed-trace pairing, i.e. the product-surface / Poincare-duality assembly) that **forces** $|t_p|<2\sqrt p$ from the modular flow itself, rather than asserting it block by block. The decoupled carrier cannot, because $\log\Delta$ is t-blind, so $t$ must come from a coupling that lives in the critical strip the carrier never reaches. That coupling is M4 undiminished. This matches the breadth-sweep doctrine (#97): the signature must be **sourced** (from the coupling), never **propagated** (asserted per block).

## Handoff (Lean / adversary targets)

- **VT-1**: for $\Omega=[[0,1],[-1,0]]$, $B_E(p,t)=[[2,t],[t,2p]]$, the polarization $Q=\Omega A_E(-A_E^2)^{-1/2}$ is positive-definite iff $t^2<4p$ (maps to `HodgeIndex.negDef_iff_hasseWeil`; cf. the new `FunctionFieldRH.eigenvalue_modulus`).
- **VT-2**: the modular weight spectrum of the finite BC carrier is a function of the prime set alone (carries no $t$).
- **VT-3**: $1-t p^{-s}+p^{1-2s}$ is nonvanishing for $\mathrm{Re}(s)>1$, all real $t$ (the carrier-blindness lemma).
- **AT-1**: try a $\beta$-dependent off-diagonal coupling sourced only from KMS data; predicted to add no constraint on $t$ (cannot reach the critical strip).

## Cross-refs

LEARNINGS #103 (this), #102/#101/#100 (MC.3/2/1), #99 (the trace route closed), #98 (the frame-audit that predicted NONE), #97 (sourced-not-propagated), #70 (C_E, the K1 underdetermination), #80 (the continuous-spectrum wall the global coupling re-enters), #52/M2.6 (the stealth window this localizes per prime). Doc: [`../../docs/03_research/modular_polarization_carrier.md`](../../docs/03_research/modular_polarization_carrier.md) (MC.4 stays open).
