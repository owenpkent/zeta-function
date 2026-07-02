# P9: Paired-subtorus circle-rootedness (arXiv note draft)

Draft of the PUBLICATIONS.md **P9** note. Source of the mathematics:
[`../../experiments/toy/paired_subtorus.md`](../../experiments/toy/paired_subtorus.md) (proof + 12/12
numerical verification, LEARNINGS #144) and the novelty pass (LEARNINGS #144 addendum).

## Status

- `main.tex`: complete draft, ~5 pages (amsart). Statement, one-page proof (self-contained
  Lemma 2.3 via Vieta; Hinkkanen credited as the one-step alternative, Remark 2.5), three
  sharpness examples, the derandomized $2^m$ identity, the subgroup classification question.
- Attribution posture (per the novelty pass): the STATEMENT is presented as the contribution;
  the machinery (multiaffine determinantal stability, Schur-product extraction) is explicitly
  credited to GKW folklore and Hinkkanen 1997. Remark 4.2 states plainly that the result does
  NOT extend the interlacing-families selection step to the circle.

## Submission gate (open items, in order)

1. ~~Checker verdict~~ DONE (2026-07-01) and folded in: Hinkkanen's statement CONFIRMED verbatim
   (via COSW p.35; COSW Prop. 4.20 = independent published proof, now cited); arXiv:2606.15003
   CLEAN (coefficientwise q-convolution, REAL-rooted, no orbit averages); Ruelle Grace-like CLEAN
   but surfaced the key attribution: Lemma 2.3 IS the classical **Asano contraction** (Asano 1970,
   Ruelle PRL 1971; unit-bidisk form verbatim in COSW Remark after Prop. 4.19). Draft revised:
   lemma renamed and attributed, Asano/Ruelle/COSW added to references, the Lee-Yang-pattern
   framing added, novelty claim scoped to the assembled orbit-average theorem only.
2. **MathSciNet session** (HUMAN, Owen): search "expected characteristic polynomial" + unitary,
   "Schur product" + polydisk, principal minor generating polynomials of unitary matrices. The
   novelty pass was web-only.
3. **Human review pass**: verify the GKW citation author list (Grinshpan, Kaliuzhnyi-Verbovetskyi,
   Woerdeman, Complex Anal. Oper. Theory 7 (2013); the surveyor's link matched this journal/DOI but
   the author list was not independently confirmed), the Kabluchko volume/page data, and the
   Hinkkanen page range.
4. **Owen's calls**: author name as rendered; whether to add an acknowledgments line on
   computer-assisted exploration/verification (venue norms vary; nothing is claimed that depends
   on it since the proof is human-checkable line by line); whether to link the verification code
   (the repo is public: `experiments/toy/paired_subtorus.py`).
5. Compile + arXiv package (math.CV primary, cross-list math.CO, math.PR).

## Build

`pdflatex main.tex` (twice for refs). No external packages beyond amsart/geometry/hyperref.
