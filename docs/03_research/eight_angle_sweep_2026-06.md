# Session synthesis: the eight-angle sweep (June 2026)

> Consolidation of a single research session that swept eight angles on RH and deep-dove the one live
> thread. Every angle is recorded in LEARNINGS #111-#117 with its own dossier; this doc ties them
> together. The unifying finding restates the project's thesis from eight new bases:
> **realization is everywhere, the signature (M4 = the arithmetic Hodge standard conjecture) is nowhere
> but M4.** Companion to [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md) (the standing
> convergence ledger) and [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md) (the scorecard).

## The one-paragraph finding

The session pursued the quantum-mechanics / spectral angle, the modular-continuation question (NP-1),
string theory, and cryptography, plus a three-build deep dive on the one genuinely-live thread (the
Connes-Consani-Moscovici semilocal prolate operator). Every angle reduced to the same place. The
realization half of RH (a trace, a determinant, a spectrum, an amplitude, a partition function) is
buildable in framework after framework; the signature half (an indefinite $(1,n{-}1)$ polarization on
the Frobenius side of $\mathrm{Spec}(\mathbb{Z})$, carrying the trace $t$, non-circular) is the
irreducible content and was reached by none of them. This is the marginal-positivity thesis confirmed
from eight independent bases, and it narrowed the search hard: it eliminated the cheap operator routes
to the one live thread, produced three reusable disqualifiers, and left a single un-eliminated route
(CCM's deferred metaplectic operator) plus the standing construction-grade M4 targets.

## The eight-angle ledger

| # | Angle | Verdict | Reduces to | Commit |
|---|---|---|---|---|
| 111 | QM / spectral, brought current (Connes-Consani prolate/semilocal, Bender-Brody-Muller) | realization, not signature; 6th all-roads confirmation | de Branges (#43) for reflection positivity; K1/R3.5 for BBM; the published archimedean positivity confirms the K2 firewall | `b4e0da7` |
| 111 | `e1d`: arithmetic input as an *additive* potential | NULL | additive injection does not break the $\zeta$-vs-D-H symmetry; arithmetic must enter the geometry | `b4e0da7` |
| 112 | NP-1: does the finite-prime modular carrier continue into the strip as a $t_p$-detector? | NO | the off-line obstruction is absent from every finite truncation; reaching it = the infinite limit = the M4 coupling (#104) | `76d3f79` |
| 113 | String theory ($p$-adic/adelic strings, SYK/$xp$, topological string, reflection positivity, metaplectic) | corpus closes onto existing kills | Euler-side realization (#42/#76); Level 3; de Branges (#43); the Kudla near-miss = BSD/Gross-Zagier regime | `633c3db` |
| 114 | CCM semilocal prolate: the deep-read map | ajar, factored, conditionally escaping | M4 at the terminal core, but the road factors through a separately-attackable operator construction | `cc43993` |
| 115 | `e1g`: the band-in-$s$ concentration operator (faithful, genuine projections) | signature-blind (reweighting-blind) | a diagonal-similarity triviality; L-function-blind by construction | `1c2e58a` |
| 116 | Cryptography (GRH-as-tool, Ramanujan graphs, isogeny crypto, Mobius, lattice/theta) | corpus-completing closure | RH-as-tool (inverted dependency); the function-field RH shadow (lever B); Level 3; the Epstein control | `5969faa` |
| 117 | `e1h`: the degree-domain prolate operator (faithful $W_{\lambda,S}=(H+\tfrac12)^2+\lambda^2 N_S$) | signature-blind (reads moments) | a deterministic function of the Jacobi matrix; a single prime's factor is just a frequency | `9f4ff82` |

## Three reusable disqualifiers (the session's genuine yield)

The sweep was negative on RH, but it produced three clean, reusable tools that retire whole families of
approaches by *regime* or *structure* rather than case-by-case:

1. **The L-value / L-derivative rule (#113).** Any arithmetic-intersection route whose native output is a
   central **L-value or L-derivative** is in the BSD / Gross-Zagier / Beilinson-Bloch (order-of-vanishing)
   regime, **not** the RH regime. RH needs the *signature of the pairing across all heights*, not the
   rank/derivative at the center. This retires the entire Gross-Zagier family in one line, including the
   deepest arithmetic theta lift (Kudla, Kudla-Rapoport-Yang) and the isogeny-graph near-miss
   (Codogni-Lido) the crypto survey flagged.
2. **The cheap-spectral-surrogate disqualifiers (#115, #117).** (a) An $s$-band concentration spectrum is
   **reweighting-blind**: any spectral multiplier (the Euler factors $|\prod_v L_v|^2$ a special case) is
   invisible to it by diagonal similarity, so it is L-function-blind by construction. (b) An
   orthogonal-polynomial-data spectral statistic **reads moments, not arithmetic**: a single prime's
   measure factor carries no content beyond its characteristic frequency $\log p$, which any matched
   non-arithmetic factor reproduces, and the joint multi-prime structure does not separate spectrally.
   Together: *if arithmetic enters only as a measure weight on the spectral line, no spectral statistic of
   a cutoff/Jacobi operator can decode it.* The arithmetic must live in the metaplectic sign-structure.
3. **The GRH-as-tool inverted dependency (#116).** The entire cryptography/computational-number-theory
   applications literature *consumes* RH (GRH-conditional algorithms: Bach's bound, deterministic
   Miller-Rabin; $\Pi^0_1$ verification refutes only). The dependency points away from a proof; it is
   structurally incapable of being a route.

## The CCM thread, fully mapped (the one live door)

The Connes-Consani-Moscovici semilocal prolate operator was the only QM object the sweep flagged as live
rather than closed. The deep dive (#114, #115, #117; dossier
[`ccm_semilocal_prolate.md`](ccm_semilocal_prolate.md)) mapped it precisely:

- **The factoring.** The terminal object is M4 verbatim ("the sought for Weil cohomology"), but the
  open step factors into (1) *construct* the self-adjoint $W_{\lambda,S}$ with its $S$-dependent Jacobi
  matrix (CCM defer this, via the metaplectic representation of $\widetilde{SL(2,\mathbb{A}_S)}$) and
  (2) identify its negative eigenspace = the Sonin space -- both operator-theory, *not* the arithmetic
  Hodge index, separately attackable -- around (4) the $S\to\infty$ uniform domination, which **is** M4.
- **R3.5 status = conditionally escaping.** The archimedean fragment (Connes-Consani 2006.13771) *proves*
  the positivity sign can be **geometric** (the $-2$ derivative-jump at the self-dual scale + the Sonin
  projection, never the zeros), so it walks R3.5's geometric-positivity escape clause. The semilocal
  escape-vs-K1 turns on one bit: **can $W_{\lambda,S}$ be constructed without inputting the zeros?**
- **The three cheap operator builds are all signature-blind**, by three distinct mechanisms, each fixing
  the prior's flaw and still failing: `e1f` (multiplication-by-density surrogate -- not idempotent, so
  its eigenvalues are not spectral invariants); `e1g` (the genuine band-in-$s$ concentration operator --
  reweighting-blind); `e1h` (the genuine degree-domain prolate operator -- reads moments, not arithmetic).
- **One genuine validated identity.** The archimedean Hardy-Titchmarsh scaling operator **is** the
  Meixner-Pollaczek Jacobi matrix ($\alpha_k=0$, $\beta_k^2=k(k-\tfrac12)$), exact to $5\times10^{-60}$.
- **Net.** The metaplectic operator is the un-eliminated route **by elimination** -- the cheap
  OP-data attacks are exhausted, and CCM deferred the real operator for a reason (it is research-grade
  construction work). The door stays ajar; it is now thoroughly mapped.

## The honesty engine worked (the methodological record)

Every artifact this session survived a builder -> adversary loop with a mandatory non-arithmetic / D-H
control before being recorded, and the discipline caught real errors each time:

- **NP-1's numerical witness was vacuous** (the test function ignored its $t_p$ argument; feeding NaN
  gave the same answer). The adversary killed it; the verdict was rebuilt on the analytic argument alone.
- **`e1f`'s "M4-wall degradation" was a normalization artifact** (a non-idempotent projection); demoted.
- **`e1g`'s "the primes cancel" overstated reweighting-blindness**; a random-multiplier control corrected
  it to the right, more general statement.
- **`e1h`'s sign caveat was mis-framed on both sides**, and the adversary **killed its own $z=+2.29$
  false positive** when steelmanning the positive case (the inverse risk -- was a real signal under-read?).
- **The "Nth independent all-roads confirmation" framing was an overclaim twice** (string, crypto); both
  downgraded to "corpus-closes" -- the positivity-bearing rows re-cite existing kills.

The lesson the session keeps re-teaching: a soft realization positivity, a normalization-dependent
eigenvalue, or a measure-weight spectral shift can *look* like arithmetic content; the non-arithmetic
control is what separates a signal from decoration, and it almost always says decoration.

## Where the front stands

The cheap routes across QM, modular continuation, string theory, cryptography, and the CCM operator
constructions are exhausted, and all eight reduce to the same M4 signature. The genuinely-open frontier is
unchanged in location but sharper in description:

- **CCM's deferred metaplectic operator** -- the one un-eliminated route, research-grade, the place a
  zero-free construction would decide R3.5-escape vs K1 (#114, #117).
- **The standing construction-grade M4 targets**, all four faces of the same coupling: the AHK arithmetic
  lattice ([`research_directions/09A_ahk_arithmetic_lattice.md`](research_directions/09A_ahk_arithmetic_lattice.md)),
  the Faltings-Hriljac product + $\Gamma_S$, the function-field lever B $\mathrm{Spec}(\mathbb{Z})$ lift
  ([`lever_b_function_field_plan.md`](lever_b_function_field_plan.md)), and the modular $C_E$-cup (#104).

Nothing here lowered the difficulty of M4. What the sweep did was confirm, from eight independent
directions, that M4 *is* the difficulty -- and hand back three disqualifiers that keep future search off
the dead branches.

## Provenance

Single session, 2026-06-24/25. Eight angles, seven commits (`b4e0da7`, `76d3f79`, `633c3db`, `cc43993`,
`1c2e58a`, `5969faa`, `9f4ff82`), LEARNINGS #111-#117. Dossiers:
[`quantum_mechanics_signature_dossier.md`](../../experiments/spectral/quantum_mechanics_signature_dossier.md),
[`string_theory_rh.md`](string_theory_rh.md), [`ccm_semilocal_prolate.md`](ccm_semilocal_prolate.md),
[`cryptography_rh.md`](cryptography_rh.md). Experiments: `e1d`, `e1f`, `e1g`, `e1h`
([`experiments/spectral/`](../../experiments/spectral/)), `e2vv`
([`experiments/arithmetic_geometric/`](../../experiments/arithmetic_geometric/)). Each angle was
builder/surveyor -> adversary verified; the D-H control (`experiments/_shared/davenport_heilbronn.py`)
held 9/9 throughout.
