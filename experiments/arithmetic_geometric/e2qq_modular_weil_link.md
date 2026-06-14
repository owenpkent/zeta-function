# 2QQ: the modular-Weil link (milestone MC.2)

> Experiment [`e2qq_modular_weil_link.py`](e2qq_modular_weil_link.py). Milestone MC.2 of [`../../docs/03_research/modular_polarization_carrier.md`](../../docs/03_research/modular_polarization_carrier.md). Result recorded as LEARNINGS #101. Follows the modular-carrier PoC (e2pp, #100) and the von Neumann probe (e2oo, #99).

## The question

The modular PoC (#100, e2pp) showed the type III modular structure supplies, for free, the weight grading $\log\Delta$ and the FE/Poincare duality $J\Delta J=\Delta^{-1}$ that a trace lacks. MC.2 asks how that meets the actual polarization data the project already built: the Weil operator $C_E$ (#70, e2lo) and the Sen/Frobenius generator $\Theta$ (#41), on the finite Euler-Sen model. Does the modular conjugation $J$ equal $C_E$? Does $\log\Delta$ equal $\Theta$? And does the modular-phase route reproduce the $t$-carrying 2G polarization that the trace (#99) could not?

## The result: three honest gaps that say exactly what is still M4

Running the experiment establishes three structural facts (each asserted):

1. **$\Theta$ is non-semisimple, so it is not $\log\Delta$.** The Sen generator $\Theta=-\tfrac12 I+N$ has a nonzero monodromy nilpotent $N$ ($N^2=0$, $N\neq0$), so $\Theta$ is not self-adjoint; the modular Hamiltonian $\log\Delta$ is self-adjoint, hence can match only the **semisimple part** of $\Theta$ (the weight, $-\tfrac12$ here). The monodromy $N$ is invisible to the modular Hamiltonian. This is the Petrov non-semisimplicity again (#69): the weight filtration is modular, the monodromy is extra.

2. **The Weil operator $C_E$ is a complex structure, not the modular conjugation $J$.** $C_E^2=-I$ (complex-linear), whereas $J^2=+I$ (antilinear involution, e2pp). The naive identification $J=C_E$ is a category error: $J$ is the real-structure conjugation, $C_E$ is the polarization phase. $C_E$ is extra data beyond $J$.

3. **The $C_E$-twisted polarization carries $t$; the modular weight data does not.** $B_E(q,t)=\begin{psmallmatrix}2&t\\t&2q\end{psmallmatrix}$ differs for $t=1$ vs $t=3$ and is positive-definite iff $t^2<4q$ (Hasse-Weil); at an off-line trace $t=5$ ($t^2>4q$) the Weil operator is not real and there is no polarization. The Frobenius trace $t$ is injected by $C_E$, not by $\log\Delta$ (which is $t$-independent, as is any GNS trace form).

## Reading

The modular structure (e2pp) supplies the **$t$-independent scaffolding**: the weight grading $\log\Delta$ and the FE duality $J\Delta J=\Delta^{-1}$. The **$t$-carrying polarization** needs two things the modular Hamiltonian does not contain: the complex structure $C_E$ (the phase, $C_E^2=-I$, distinct from the antilinear $J$) which injects $t$, and the monodromy $N$ (distinct from $\log\Delta$, #69). M4 is proving the assembled $C_E$-twisted form positive without RH input. So MC.2 does not collapse the gap; it **factors** it cleanly: modular scaffolding (free) + the phase $C_E$ + the monodromy $N$, with positivity the open kernel.

**Refinement of #99/e2oo.** Both the GNS trace form and the polarization $B_E$ are positive-definite. The genuine discriminator is therefore not "definite vs indefinite" but **carries-$t$ vs $t$-blind**: $B_E$ depends on $t$ (and is PD iff Hasse-Weil), the trace form does not. The indefinite object is the cup form $\Omega$ / $G_{\mathrm{prim}}$, which $C_E$ converts into the positive $t$-carrying polarization. This sharpens the e2oo phrasing without changing its verdict (the trace route is still wrong, now precisely because it is $t$-blind and structureless, not merely definite).

## Cross-refs

- LEARNINGS #101 (this), #100 (the modular PoC), #99 (the trace route closed), #70 (e2lo, $C_E$), #69 (the monodromy $N$ / Petrov non-semisimplicity), #41 (the flow $\Theta$), #68 (the form is transport, the $C_E$-twist must source the indefinite $B$), #40 (the $t$-blindness this refines).
- Docs: [`../../docs/03_research/modular_polarization_carrier.md`](../../docs/03_research/modular_polarization_carrier.md) (MC.2 milestone), [`../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md`](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md).
