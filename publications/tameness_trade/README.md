# Tameness trade (expository structural-obstruction note)

A focused note locating, from the model theory of additive prime structures, where the Weil explicit
formula's prime side $S(f) = \sum_n \Lambda(n)\, f(\log n)$ can and cannot be assembled inside a
first-order structure. The finding: assembling it is a tame/wild fault-line phenomenon, and the fault
line is the archimedean **order** coupled to $+$ and the primes, not tameness and not the bare prime set.

## Status

- **Tier:** DRAFT, expository structural-obstruction note. Not a proof; no new theorem about RH.
- **Type:** synthesis / methodology (assembles a published but scattered corpus around one functional).
- **Target venue class:** arXiv math.LO / math.NT expository slot (or a section folded into the
  obstruction-map survey).
- **Relation to the registry:** definability-side detail behind
  [`../obstruction_map/obstruction_map.md`](../obstruction_map/obstruction_map.md) Section 6.2 (the
  Davenport-Heilbronn / archimedean-order firewall). Source dossier:
  [`../../docs/03_research/tameness_trade.md`](../../docs/03_research/tameness_trade.md); LEARNINGS #157;
  [`../../docs/03_research/model_theoretic_frobenius.md`](../../docs/03_research/model_theoretic_frobenius.md)
  #156.

## What it argues (CORRECTED tier, no restored overclaim)

$S(f)$ couples addition (the $\{\log p\}$ lattice) and multiplication (prime factorization) in one
functional. The question "can a tame structure carry it internally" splits into two logically independent
legs: **Leg A** (saturation, PROVEN but orthogonal to the RH engine, Lemma P3) and **Leg B** (the
tameness claim, REFUTED as stated by Kaplan-Shelah; the real invariant is the archimedean order). The
unconditional keystone (does the ordered prime structure force $\times$ without Dickson) is OPEN. The
RH-engine reading (C3, MECHANISM/HEURISTIC) is that any engine reaching $S(f)$ injects it archimedeanly,
which is why the CCM Section-7 = M4 wall is archimedean by necessity.

## Honesty contract

- The model-theoretic core is **published** (Kaplan-Shelah, BJW, Boffa, Poizat, Palacin-Sklinos, Bes,
  Korec, Green-Tao); the note's residue is the **synthesis packaging**, not any theorem.
- Every result is tagged PROVEN / KNOWN / CONDITIONAL / REFUTED / MECHANISM / HEURISTIC / OPEN; every
  force-$\times$ statement is labeled Dickson-conditional; the keystone is flagged OPEN.
- The withdrawn first-draft overclaim ("no tame counting engine carries the summed explicit formula") is
  **not** restored; it is recorded as withdrawn with the citation-inversion process learning.
- Two repo corrections carried on record: the IP result is Kaplan-Shelah **Proposition 3.6** (not "Thm
  3.7"); [PS14] is **Palacin-Sklinos** (not "Point-Schmidt").

## Open review items (must clear before any "ready")

1. **Source-verify at length.** Re-confirm BJW93 (JSL 58(2), 1993) and Boffa (JSL 63(1), 1998) abstracts
   and the Poizat "Supergenerix" Theorem 25 statement independently; Bes [Bes01] and Korec [Kor01] full
   text were not fetched this pass (TLS/403 errors) and are cited at bibliographic level.
2. **Model-theory referee.** The neostability claims (supersimple, dp-minimal, SOP/IP thresholds, U-rank)
   want a referee-grade reader before circulation.
3. **Novelty of the packaging.** Lit-check that no existing survey already organizes the explicit
   formula's prime side against the additive-prime-structure tame/wild map with the keystone flagged.
4. **Decide standalone vs fold** into the obstruction-map survey (its Section 6.2).

## Files

- `tameness_trade_note.md`: the draft (this directory's deliverable).
- `README.md`: this file.
