# Mueller 1983: the arithmetic equivalent of essential simplicity, read for F2b

> SURVEYOR reading note, 2026-08-28. Bounded fetch riding frame session F2b, scheduled by
> [`f2a_certificate_class.md`](../f2a_certificate_class.md) Section 6, item 5 (lines
> 713-718), motivated by Section 1's C2-FUND paragraph "All three channels are
> first-class" (lines 180-193). **Nothing in the class definition depends on this note's
> outcome**: zero-side and prime-side parametrizations of $\mathcal{P}$ are already
> first-class regardless. It only checks whether a second, non-RH-priced bridge exists
> alongside the Goldston-Montgomery dictionary.
>
> **Method and tiers.** WebSearch/WebFetch across the citation graph, plus direct PDF
> reads via the Read tool when WebFetch's extraction failed on compressed streams.
> VERIFIED-AT-SOURCE = read directly, myself, not an intermediate paraphrase. TWO-ROUTE =
> two independent documents agree. SINGLE-SOURCE = read at one source, uncorroborated.
> SECONDARY = background/inference, not read at source this session.

## Q3: the citation

**Julia Mueller, "Arithmetic equivalent of essential simplicity of zeta zeros," Trans.
Amer. Math. Soc. 275, No. 1 (1983), pp. 175-183. DOI: 10.1090/S0002-9947-1983-0678343-0.**
[TWO-ROUTE, in fact three-route]: her own CV (read via the Read tool), GLSS II's
bibliography entry `[Mue83]` (arXiv:2507.06823v1, read via WebFetch), and the Crossref
API record for the DOI all agree. Semantic Scholar (CorpusId 120824272) lists 13 citing
papers. Ivić 2003 (below) renders the title "Arithmetical..." (one letter off); the other
three agree on "Arithmetic...", treated here as authoritative.

**Mueller's own paper was not reachable this session** (`ams.org` returned 403,
`degruyterbrill.com` 405, Semantic Scholar's abstract field "elided by publisher"), so
every finding below about her actual content is secondary: from papers describing her
result, not the paper itself.

## Q1: the zero-side hypothesis (recovered), the prime-side "equivalent" (not recovered)

**The zero-side object Mueller named "Essential Simplicity" is cross-confirmed by three
independent sources, all landing on the same pair of scalars.** GLSS II
[VERIFIED-AT-SOURCE, arXiv:2507.06823v1]: "Mueller [Mue83] referred to [these properties]
as 'Essential Simplicity' of the zeros $\rho$": (ES1) $N^\circledast(T) = TL + o(TL)$
(near-diagonal equal-ordinate pair count) and (ES2) $N(T,\lambda_0) = o(TL)$ as
$\lambda_0\to0$ (near-diagonal distinct-ordinate pair count vanishes). Ivić 2003
[VERIFIED-AT-SOURCE, arXiv:math/0312097 p. 12, via the Read tool] states the identical
pair, attributed to "J. Mueller [12]," as his (32) (matching ES2) and (33) (matching
ES1). Goldston 2004 [VERIFIED-AT-SOURCE, arXiv:math/0412313 Section 6] independently
names the same conjunction "the Essential Simplicity Conjecture (ESC)" (small gaps plus
simple zeros, $N^*(T):=(T\log T/2\pi)^{-1}\sum m_\rho\sim1$), though without citing
Mueller for the term (a gap, logged below). The zero-side object is settled: (ES1)+(ES2),
equivalently Ivić's (32)+(33), in every later paper's notation.

**The prime-side functional Mueller's title promises could not be pinned down.** The one
passage found anywhere that describes the *content* of Mueller's theorem, not just its
terminology, is Ivić 2003, p. 12 [SINGLE-SOURCE for the claim about Mueller;
VERIFIED-AT-SOURCE for what Ivić himself wrote, read directly from the rendered page]:

> "A discussion of the essential simplicity hypothesis is given by J. Mueller [12]. It is
> shown there that this hypothesis is, under the RH, equivalent to two other hypotheses
> involving certain integrals."

Ivić does not name the two hypotheses, say either is prime-side, or give the integrals.
Neither GLSS I nor GLSS II (both read in full earlier this project, per
[`glss_full_funding_boundary.md`](glss_full_funding_boundary.md)) uses any prime-side
content from Mueller; both cite `[Mue83]` for terminology only. Nothing sharper turned up
in a wider sweep: Goldston 2004, otherwise exhaustive here, cites only the 1978
Gallagher-Mueller paper; BGSTB (2306.04799) and arXiv:2009.05760, 2501.14545, 1206.3737,
1302.5018 all omit her. Gallagher's 1985 solo sequel (J. reine angew. Math 362), the
likeliest source for the precise content, was blocked (405) and not read.

Whether one of the "two other hypotheses" is literally a prime second-moment or
short-interval-variance statement, as this fetch's motivating hypothesis assumed, is a
plausible inference from the title ("arithmetic") and the Gallagher-Mueller 1978 toolkit,
which proves in that paper "an asymptotic formula for a weighted second moment for primes
in short intervals" (Goldston 2004 Section 7). It is **not itself verified** by any
source read this session. [SECONDARY, unverified].

## Q2: conditionality

**Per the only source found describing the theorem's content, the equivalence is stated
under RH, not unconditionally** [SINGLE-SOURCE for the claim about Mueller's paper;
sentence itself VERIFIED-AT-SOURCE]. That is the direct answer this fetch was sent to
get, and it does not support an unconditional merge.

**One honest complication, flagged and not resolved.** Gallagher-Mueller has a precedent
for exactly this kind of RH-dependency dissolving: their 1978 paper proved
"PCC $\Rightarrow$ SZC" under RH, later clarified (GLSS I, per GLSS II) as not actually
needing RH, confirmed independently by Goldston 2004 ("holds unconditionally," Section
7). Whether Mueller's 1983 solo result underwent the same RH-removal, i.e. whether RH in
Ivić's account is load-bearing or an of-its-era default, is **not addressed by any source
read this session**. No paper checked invokes an unconditional version, including the
ones with the clearest incentive (GLSS I/II, BGSTB); weak evidence against, not proof.

## Discrepancy log

1. [`glss_full_funding_boundary.md`](glss_full_funding_boundary.md) Section 1.2 attributes
   `[Mue83]` and the ESH "adapted... to the no-RH setting" gloss to "GLSS I." Direct
   re-fetch [VERIFIED-AT-SOURCE] shows both are stated in **GLSS II**; GLSS I cites only
   the 1978 Gallagher-Mueller paper and Mueller's 1976 thesis, never `[Mue83]`. Minor;
   worth a one-word fix at the source note.
2. Goldston 2004 defines "the Essential Simplicity Conjecture (ESC)" without citing
   Mueller, despite being exhaustive here; not a contradiction, just an unexplained gap.

## Consequence for the class definition

The pointer named in Section 6 item 5 does not deliver what it was hoped to. The one
source describing Mueller 1983's content states the equivalence **under RH**, not
unconditionally, landing it in the same RH-priced bracket as the Goldston-Montgomery
dictionary rather than beside it as a free second route. The two pool parametrizations of
$\mathcal{P}$ do **not** partially merge unconditionally on the strength of this pointer;
the merge remains RH-priced, and the class definition's existing choice to carry
zero-side and prime-side grants as separately first-class (Section 1, C2-FUND) is
confirmed correct, not overcautious. Door left open: Mueller's own two hypotheses were
never read, so a stronger or weaker reading than Ivić's gloss needs a VERIFIER-grade
original-source read (TAMS 275, or a MathSciNet/zbMATH review) to rule out.

## What this enables / what remains open

**Enables.** F2b can cite this for the negative half of the Mueller pointer ("if... then"
resolves to "no, at least not for free") without re-running the search; the zero-side ES
object is triple-sourced (GLSS, Goldston, Ivić) with a citable formula pair, (ES1)/(ES2).
**Open.** (a) The content of Mueller's two integral hypotheses, unread; a VERIFIER with
library/MathSciNet access could close this in one sitting. (b) Whether the RH dependency
is removable, as the 1978 one was; no evidence either way. (c) Gallagher's 1985 sequel,
likeliest to discuss Mueller directly, blocked (405); the highest-value next fetch.
