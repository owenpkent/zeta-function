# LaTeX conversion note: draft.md v0.3 to draft.tex (P12)

Date: 2026-08-26. Scope: faithful format conversion only. No wording changed, no claims added or dropped; the acknowledgments paragraph is byte-identical to draft.md (diff-verified). Compiled to draft.pdf (17 pages) with tectonic 0.15.0 (no pdflatex on this machine); the .tex uses only standard packages (amsmath, amssymb, graphicx, booktabs, hyperref) and is pdflatex-compatible for arXiv.

## Judgment calls made in conversion

1. Class and layout: article, 10pt, default margins. `\emergencystretch 3em` added to absorb long inline math and tt paths (final compile has zero visible overfull lines). The draft's stated 6-10 pp target assumed a denser layout; at default article margins the note runs 17 pp. If Owen wants it tighter, adding `\usepackage[margin=1in]{geometry}` is the one-line fix (kept out for now to stay within the agreed standard-package list).
2. Section numbering: `\setcounter{section}{-1}` so sections run 0-8 exactly as in the draft. Every internal "Section N" mention became a live `\ref`; rendered numbers are identical to the draft's.
3. Display math: all `$$...$$` blocks became `\[...\]`. No equation numbers introduced: the only numbered-equation mentions ((1.2), (7.5)-(7.6), (1.12)) refer to other papers' numbering and stay literal text. Formulas transcribed exactly.
4. Title-block metadata: the italic status line under the title in draft.md is workflow metadata, not paper content; it is carried verbatim as a preamble comment, with `\date{Draft v0.3, 2026-08-25}`. arXiv categories (math.NT primary, math.CA cross-list) are recorded as a comment at the top of the .tex; they are entered in the submission form, not in the source.
5. Figures: the PDF versions (figures/f1.pdf .. f4.pdf) are used per the draft's own "PDF for LaTeX" note (PNGs remain as previews). Figure environments sit in an unnumbered Figures section at the draft's position, with `\clearpage` after so all four land before the acknowledgments. Captions are verbatim including the F1-F4 markers, so each prints as "Figure n: Fn (Section ...)"; the LaTeX figure numbers coincide with the F-numbers. The heading's parenthetical "(generated: make_figures.py; PDF for LaTeX and PNG preview in figures/)" moved to an italic line under the heading (tt text inside a hyperref bookmark is avoided).
6. Citations: bracket citations in the body ([CCM, Section 3], [Su, ...], [C26, ...], [G26a], [G26b, Thm 3.2], [G26a, C26]) became `\cite[...]{...}`; the draft's alphabetic labels are preserved via `\bibitem[label]{key}` in thebibliography. Bracket mentions inside bibliography annotations ("[B] and [Su]") stay literal text. [CvS] is never bracket-cited in the body (matching the draft) and still prints in the reference list. arXiv identifiers kept exactly as written, as plain text.
7. Table (Section 7.3): booktabs tabular, non-floating (center environment, as in the draft's flow), `\small` with 4.5pt column separation so the eight columns fit the text width; the empty cells in the "sharp" row stay empty.
8. Characters: straight double quotes (three quoted phrases) became LaTeX backtick/quote pairs. All hyphens stay hyphens; no en or em dashes introduced anywhere (house rule). Source is pure ASCII; no encoding fixes were needed.
9. Markdown structure: bold run-in leads (Measurement., The refuted pre-registration., etc.) became `\textbf` run-ins; bullet and numbered lists became itemize/enumerate; ALL-CAPS emphasis kept verbatim; the `**Abstract.**` lead is supplied by the abstract environment; the `---` separators of the markdown header have no LaTeX counterpart and are dropped.
10. Code spans and paths: backtick spans became `\texttt` with escaped underscores; the three long repository paths use `\path` (from the url machinery hyperref loads) so they break across lines; the repository URL uses `\url`. The evidence-trail paragraph stays after the bibliography, as in the draft.
11. amsthm omitted: the note defines no theorem environments, so the package would be dead weight; trivially added if a revision needs it.
12. Build hygiene: tectonic leaves no .aux/.log/.out files; the directory carries only draft.tex and draft.pdf beside the markdown sources.

## Remaining for Owen

- [ ] arXiv posting: upload draft.tex plus the four figures/f1.pdf..f4.pdf (the .png previews are not needed in the submission); set math.NT primary, math.CA cross-list in the form. Consider whether `\date` should read "Draft v0.3, 2026-08-25" or be cleared at posting.
- [ ] Optional density pass: add geometry (1in margins) if 17 pp should compress toward the 6-10 pp target.
- [ ] On posting day: send the three staged courtesy emails (CCM, Suzuki, Groskin) per `courtesy_emails.md`.
