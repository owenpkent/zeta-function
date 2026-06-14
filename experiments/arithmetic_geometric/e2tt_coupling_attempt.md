# 2TT: the coupling cannot be sourced from the modular carrier (AT-1 closed); the four faces of the coupling

> Experiment [`e2tt_coupling_attempt.py`](e2tt_coupling_attempt.py). Executes the adversary test AT-1 from the MC.4 attempt (e2ss, #103). Result recorded as LEARNINGS #104. This works on the coupling = M4; it sharpens and unifies, it does not solve.

## The question (AT-1)

MC.4 = M4 needs the **coupling** between the per-prime twisted blocks that *forces* $|t_p|<2\sqrt p$ from the modular flow itself, rather than asserting it block by block (the decoupled carrier is K1-circular because $\log\Delta$ is t-blind, #103). AT-1 asks: is there a coupling sourced **only** from the modular/KMS data ($\beta>1$) that constrains the traces?

## The result: AT-1 closed in the negative

Three facts (each asserted, with numbers):

1. **The carrier data is t-independent.** The BC modular weight spectrum $\{\log n-\log m\}$ (81 weights), the Gibbs weights $\{n^{-\beta}\}$, and any representative carrier-derived coupling such as $(pq)^{-\beta}I$ are all functions of (the prime set, $\beta$) alone. The carrier never takes a trace as input; $t$ enters only through $C_E$ (MC.2/#101).
2. **The constraint lives in $C_E$, not the carrier.** $C_E$ and the cup block $B_E(p,t)$ depend on $t$ (they carry the constraint); the carrier coupling does not. A t-independent operator cannot encode the t-dependent constraint $|t_p|<2\sqrt p$. **So no coupling sourced from the modular carrier can force the bound.**
3. **The coupling that works (FF template) is t-carrying.** In the function field the cup / intersection block $B_E=-G_{\mathrm{prim}}$ is positive-definite (the Hodge index, a theorem) exactly on $|t|<2\sqrt q$, and it carries $t$ ($t=0,2,4$ in-window PD; $t=5$ off-window not). That is the target shape: a t-carrying global cup, not a t-independent carrier coupling.

So the coupling cannot be sourced from the carrier; it must be a **t-carrying coupling of the $C_E$ polarization phases = the global cup product**, which the carrier does not supply. The carrier gives only the t-independent scaffolding (the weight ladder + the FE duality, MC.1).

## The four faces of the coupling (the synthesis)

The coupling is one object with four presentations, all open over $\mathrm{Spec}(\mathbb{Z})$ and all equal to M4:

| Face | What it is | Status |
|---|---|---|
| modular (here) | a t-carrying coupling of the $C_E$ polarization phases | open; not carrier-sourceable (this result) |
| function-field template | the cup product $H^1\times H^1\to H^2$, negative-definite primitive part (Castelnuovo-Severi / 2G) | a **theorem** over $\mathbb{F}_q$ |
| AHK side (09A) | the t-carrying submodular Lefschetz + indefinite primitive form on the arithmetic prime-lattice | open ([`09A_ahk_arithmetic_lattice.md`](../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md)) |
| Arakelov side | the Faltings-Hriljac product pairing + the $\Gamma_S$ archimedean place | open (2H is the single-surface theorem) |

Building any one of them is M4. This consolidates the modular thread with the AHK and product-surface threads: they are not separate attacks, they are four windows onto the same missing coupling.

## Honest verdict

AT-1 closed in the negative: the coupling is **irreducible to the carrier**. This is a sharp negative coordinate (it rules out the "maybe a clever KMS coupling helps" hope) plus a unification (the four faces). It does **not** solve M4, and nothing cheap can: the coupling must carry $t$, and the only available t-carrying data is the zeros (circular) or a genuinely new global object. The next move on this front is construction-grade: build one of the four faces (the AHK lattice 09A is the most explicitly scoped), or formalize the function-field cup in Lean (lever B's #FF-geom) so the target is machine-checked.

## Cross-refs

LEARNINGS #104 (this), #103 (MC.4, the residual this closes AT-1 on), #101 (C_E carries t, log Delta does not), #100/#102 (the modular scaffolding + euler-gating), #97 (sourced-not-propagated), #70 (C_E), #42 (the continuation/global-assembly gap), #68 (the form is transport). Docs: [`../../docs/03_research/modular_polarization_carrier.md`](../../docs/03_research/modular_polarization_carrier.md), [`../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md`](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md), 2G ([`e2g_intersection_signature.md`](e2g_intersection_signature.md)).
