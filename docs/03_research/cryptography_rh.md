# The cryptography / computational-number-theory angle on RH

> Survey + adversarial verification, 2026-06-24 (SURVEYOR -> ADVERSARY). Scope: every serious
> cryptography / computational-number-theory connection to $\zeta$ and the Riemann Hypothesis, scored
> against the project's realization-vs-signature framework and cross-referenced to the existing kills.
> Raw artifacts: `scratchpad/crypto/{01_surveyor,02_adversary}.md`.

## Bottom line

**No cryptographic structure offers a route to the arithmetic M4 signature.** Cryptography touches RH
in exactly two ways, both already in the project's record: it **uses RH as a tool** (GRH-conditional
algorithms — the dependency is *inverted*, RH is an input), and where it touches positivity it is the
**proven function-field RH** (Hasse-Weil = ECC; Ramanujan = expanders/isogeny graphs), the project's
lever B. Möbius pseudorandomness is Level 3; lattice/theta crypto reduces to the Epstein zeta, the
project's existing non-Euler RH-false control.

**Honest framing (adversary-corrected):** this is a **corpus-completing closure that re-cites lever B
plus the Epstein control**, *not* a new independent "eighth all-roads coordinate." The
signature-adjacent rows (Ramanujan graphs, isogeny crypto, Epstein) all re-cite existing kills, exactly
as the string-theory survey's positivity rows did (`#113` set the precedent: "seventh independent" was
downgraded to "corpus-closes"). The only genuinely-new content is (a) the GRH-as-tool catalog (the
dependency points *away* from proving RH) and (b) the Ihara-zeta graph-RH as a crisp finite restatement
of "realization is free, the proven-case signature is the content."

## Scorecard

| Thread | Reduces to | Direction |
|---|---|---|
| 1. GRH as algorithmic tool (Bach's $2(\log n)^2$, deterministic Miller-Rabin, class/unit-group computation) | **RH-as-tool** | RH is an INPUT (inverted) |
| 2. Ramanujan graphs / expanders / Ihara-zeta graph-RH (LPS, Pizer, Sunada) | **function-field RH shadow** (lever B), graph clothing | realization (proven case) |
| 3. Isogeny crypto / supersingular / Deuring / Eichler-Selberg (Brandt = Hecke $T_\ell$) | **lever B + `#113`** (BSD/Gross-Zagier regime) | realization + wrong invariant |
| 4. Möbius / Sarnak disjointness ($\mathrm{RH} \iff M(N)=O(N^{1/2+\epsilon})$) | **Level 3** pseudorandomness | compatible with $\beta=0.51$ |
| 5. Lattice crypto / theta / Epstein zeta | **the Epstein D-H control** (re-verified) | known RH-false non-Euler control |
| 6. Computational / $\Pi^0_1$ / verification heights (Platt-Trudgian) | **verification** (refute-only) | RH is the target, refutable only |

## The threads, grouped by failure mode

**RH-as-a-tool (threads 1, 6) — the dependency is inverted.** GRH is an *assumed input* that buys
algorithmic results: Bach's bound ($2(\log n)^2$) gives deterministic Miller-Rabin primality and
class-group / unit-group generation under GRH; recent isogeny work proves graph mixing *under* GRH
("removing a heuristic"); $\Pi^0_1$ verification (Platt-Trudgian) can only ever *refute* RH at a finite
height, never prove it. In every case RH points the wrong way — it is the hypothesis the algorithm
consumes, not a theorem the cryptography produces. This is the firmest part of the survey and is a
genuinely useful catalog: it documents that the entire "RH and cryptography" applications literature is
on the *consuming* side of RH, with no inferential path back to a proof.

**The proven function-field RH shadow (threads 2, 3).** This is where crypto touches positivity, and it
is the project's own lever B in disguise. The Ramanujan/expander spectral gap $|\lambda| \le 2\sqrt{k-1}$
*is* the Ramanujan-Petersson bound = Deligne's RH for varieties over $\mathbb{F}_q$ = the Hasse-Weil
bound the repo formalizes (`lean/ZetaRH/FunctionFieldRH.lean`, `TateModule.lean`, `IsogenyDegree.lean`).
Pizer's supersingular isogeny graphs are Ramanujan via Deligne; the Ihara-zeta graph-RH (Sunada:
Ramanujan $\iff$ graph-RH) is that proven case made finite and decidable. The **isogeny-graph near-miss**
(Codogni-Lido Hodge structure on graph homology; the Brandt matrix = Hecke $T_\ell$ on weight-2 forms;
Eichler-Selberg trace giving $a_p$ = the Frobenius trace $t$) is the *most* signature-adjacent point in
the whole crypto corpus — it carries three M4 conjuncts in one finite package. It is **killed as a
route** three ways, the third decisive: (a) the pairing's positivity *is* the proven Deligne bound =
lever B (not an independent input); (b) it is single-prime with no archimedean place; (c) by the repo's
own `#113` retirement rule, its native invariant is a central L-value / order-of-vanishing = the
**BSD / Gross-Zagier regime**, not the all-heights signature RH needs. Its shared open step is
*identical* to lever B's: the $\mathrm{Spec}(\mathbb{Z})$ lift = M4. It adds no new handle on the open
half. (Caveat: "Ramanujan gap = lever B object" is best stated as *same positivity source, poorer
carrier* — finite, single-prime, archimedean-free.)

**Level 3 (thread 4).** Möbius randomness: $\mathrm{RH} \iff M(N) = O(N^{1/2+\epsilon})$, but Sarnak's
disjointness / Chowla cancellation are statements compatible with a $\beta = 0.51$ world (the standard
Level-3 ceiling). Cross-ref `research_directions/10B_thh_weight_and_mobius.md`.

**The known control (thread 5), re-verified.** Lattice-crypto Gaussian/theta sums analytically continue
to the **Epstein zeta function** — the project's existing non-Euler, RH-false control. The adversary
independently re-confirmed it: $\text{EpsteinZeta}$ at $d=47$ (class number 5, non-principal form) has a
functional equation (residual $\sim 5\times10^{-51}$), no Euler product, and a genuine **off-line zero
at $\mathrm{Re} = 0.634$** ($\approx 0.634 + 32.05i$) — Davenport-Heilbronn's own 1936 phenomenon. So
lattice $\to$ theta $\to$ Epstein $\to$ D-H-control is a real structural identification, not an analogy:
the one place cryptography's analytic object naturally lands is the project's K2 wrong-approach detector.

## Crank filter

Serious work kept and scored: Bach (GRH algorithmics), Sarnak (Möbius disjointness), Lubotzky-Phillips-
Sarnak / Margulis / Pizer (Ramanujan graphs), the isogeny-crypto literature (SIDH/CSIDH/SQIsign,
Codogni-Lido), Platt-Trudgian (verification). Discounted as numerology / no-venue: "factoring breaks
RH," "a quantum computer finding the zeros proves RH," "RH solved via blockchain/lattice." No serious
result discounted, no crank admitted.

## What this contributes

A negative coordinate plus two small genuine yields. The crypto/computational corpus closes onto the
existing kills, confirming the realization-vs-signature thesis from the applied/computational side: it
lands on the realization side (or the *consuming* side, for RH-as-tool), and the signature stays the
lone island. The two record-worthy yields: (1) the **GRH-as-tool catalog** — the entire crypto
applications literature consumes RH, with the dependency inverted, so it is structurally incapable of
being a route; (2) the **Ihara-zeta graph-RH** as a crisp, finite, citable mirror of "realization is
free, the proven-case signature is the content," and the **lattice-crypto = Epstein-zeta** real-world
appearance of the project's D-H control. Cross-refs: `lever_b_function_field_plan.md` and
`lean/ZetaRH/{FunctionFieldRH,TateModule,IsogenyDegree}.lean` (the function-field RH = ECC shadow);
`#113` (the BSD/Gross-Zagier L-value retirement rule the isogeny near-miss obeys); `#97`/`#98`/`#111`
(the prior convergences this completes); `research_directions/10B_thh_weight_and_mobius.md` (Möbius);
the Epstein-zeta K2 control; `all_roads_to_the_signature.md`.
