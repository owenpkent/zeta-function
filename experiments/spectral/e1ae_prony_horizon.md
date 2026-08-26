# E1AE: the Prony horizon probe: the birthday scale is a Szego-register artifact, and audit falsifier 4 fires on the atom clause

**Date**: 2026-08-25. **Status**: BUILDER round (e1ad adversary case 3 executed as a build; audit falsifier 4's decision instrument; session 5 of the #201 order); final run 6/7 with the one FAIL being P2's pre-registered kill firing, which is the finding. **Code**: [`e1ae_prony_horizon.py`](e1ae_prony_horizon.py). **Data**: `e1ae_prony_horizon.npz` (tracked). **Provenance**: [`e1ad_sum_rules.md`](e1ad_sum_rules.md) handed-forward item 1 / adversarial case 3; [`sp_backlog_frame_audit.md`](../../docs/03_research/sp_backlog_frame_audit.md) falsifier 4.

## 0. The result

**The #188 birthday-scale horizon is register-relative, and it falls hard.** The annihilating-polynomial (Prony) register, consuming the SAME moment data as the Szego functional, detects membership in the scale-$D$ lattice at

$$M = 78 \text{ atoms}, \quad n = M+1 = 79 \text{ moments}, \quad \mathrm{dps}^* = 14 \text{ digits},$$

for $D = 10^4$ AND $D = 10^6$: at $D = 10^6$ the Szego register is provably blind (zero collisions; its horizon is $\sqrt{2D} = 1414$ atoms). Controls are clean at the same precision (TRUE $0.224$, matched jitter $0.219$, wrong modulus $0.21$-$0.28$, against SNAP's median site distance $\le 0.0054$; the compatible modulus $2D$ detects with the exact site-unit doubling). Pre-registration P1 FIRED, P3 FIRED, and **P2's kill FIRED as registered** (flat-in-$D$ at the ladder's granularity): per the pre-registered escalation clause and the audit's falsifier 4, **the #188 atom-currency ceiling is a family artifact of the Szego register**, and the correct response is a new instrument frame, exactly as the audit's falsifier language says.

## 1. The mechanism, and why the median makes it cheap

For an $M$-atom circle measure the first $M+1$ moments determine everything: $\Phi_M(z) = \prod_j (z - z_j)$ solves an $M \times M$ Toeplitz system on the moment data, and its roots are the atoms. At dps 14 the ill-conditioned tail of the roots is garbage (max recovery error $\sim 0.07$ turns, off-circle up to $10^{-1}$), but root sensitivity is wildly nonuniform, and the MEDIAN root is recovered to $\sim 5 \times 10^{-9}$ turns: far below one site of the $D = 10^6$ lattice. The median lattice statistic therefore reads the well-conditioned half of the spectrum and sees the lattice, while the same statistic on TRUE/jitter reads uniform. The Szego rate $S$ is the LOG-CONDITIONING of this recovery in aggregate ($\kappa(T_M) \sim e^S$); the rate functional pays it globally, the median recovery only pays the median root's share. That asymmetry is the whole result.

## 2. What survives, what dies, what is re-scoped

- **DIES: the quantitative birthday pricing** ("certifying non-lattice-ness at scale $D$ costs $\sim \sqrt{2DL}$ atoms", #188 R4's totalized reading). It is a property of Szego-type rate functionals, not of moment data. e1ad's own scope note (limit 4) anticipated exactly this; the totalization in later citations is what falls.
- **SURVIVES: the $D \to \infty$ obstruction.** Fixed instrument $(M, \mathrm{dps})$ resolves lattices only to $D^* \sim 10^{\mathrm{dps}}/\kappa_{\mathrm{med}}$; genuine $\mathbb{Q}$-linear independence is the $D \to \infty$ limit and still costs unbounded digits. #172's pointwise continuity argument is untouched. The obstruction survives as a two-currency statement with a dramatically better exchange rate than #188 implied: digits buy EXPONENTIAL $D$-reach.
- **RE-SCOPED, honestly**: (a) the growth clause dps$^*(D)$ is UNRESOLVED below the ladder floor (both rungs detected at the lowest rung, 14; the predicted growth over $10^4 \to 10^6$ is $\sim 2$ digits and the ladder starts at 14: flatness at this granularity fired P2's registered kill but may hide sub-floor growth); (b) the conditioning meter failed at dps 14 (Cholesky nan), so the cond-side bound was unevaluable: both recorded as residues; (c) what is measured is SEPARATION (SNAP vs TRUE/JIT); certifying either membership direction with INTERNAL error bars (the e2bg data-halving idiom) is the successor instrument's build, not this probe's claim.

## 3. Falsifier 4 disposition (the audit clause this executes)

The audit: "if a super-resolution register beats the birthday/precision scales, the ceiling theorems are family artifacts, 'priced, not inhabited' is wrong, and the correct response is a new instrument frame, not this one." Verdict: **the atom clause fires** (birthday beaten by 18x at $D = 10^6$, at 14 digits); the precision clause is partially resolved (no growth visible at ladder granularity; the information-theoretic $D \to \infty$ floor stands). Consequences for the record: #188's horizon LAW is re-scoped to its register (its termination mechanism and measurements stand); the #191/#195/#200 horizon results are UNAFFECTED (different instruments, different objects: their ceilings were proven about their own families, and #200's necessity was always measured-not-proven); and the successor-frame deliberation now has a measured candidate: **the recovery register on the counting side** (super-resolution reading of lattice structure at exponential $D$-reach per digit), which is exactly the instrument class the R1/S4 questions (#162/#169/#172) were priced as needing.

## 4. Honest limits

One size ($M = 78$), one gauge ($L = 1$), two $D$ rungs, known-$D$ membership testing (the detector takes $D$ as input, as e1ad's did); the $D = 10^4$ rung carries one collision (near-horizon, recorded; the headline rung $D = 10^6$ is collision-free); recovery diagnostics compare to the config's own angles (oracle-free); no zeta data anywhere. The register was run to SEPARATE, not to certify; error-bar instrumentation is future work. The #201 derivability check: "the birthday horizon is register-relative" is NOT derivable from #172/#188's entries (both priced the wall inside one register class; #188's limit-4 scope note flagged the question and this build answers it): it stands as a measured re-scoping, not a new coordinate claim.

## 5. Handed forward

To the successor-frame deliberation (now due): the recovery register as the counting-side instrument candidate (with internal error bars via data/precision halving; the certified-vector discipline from e2bf mandatory); the sub-floor dps ladder (dps 8-13) if the growth clause is ever worth pinning; the median-vs-max sensitivity asymmetry as a general lesson for every spectral-recovery instrument in the repo.
