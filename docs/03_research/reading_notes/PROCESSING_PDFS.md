# Organizing and processing PDFs in this repo

> The repeatable procedure for taking a PDF (a paper dropped into the repo, or a classical
> source) and filing it, extracting it, taking notes on it, and wiring it into the program.
> Written 2026-06-04. Entry points that link here: [`references/README.md`](../../../references/README.md),
> [`sources/README.md`](../../../sources/README.md), and the [reading-notes index](README.md).
> If you just dropped a PDF at the repo root, start at section 4.

## 1. Where PDFs live (three tiers)

| Tier | Directory | What goes here | PDF in git? | Index |
|---|---|---|---|---|
| Primary sources | [`sources/`](../../../sources/) | Classical / original documents (Riemann 1859, translations, the zeta reference) and their `.txt` conversions | **Committed** (gitignore whitelist `!sources/*.pdf`) | [`sources/README.md`](../../../sources/README.md) |
| Reference library | [`references/NN_topic/`](../../../references/) | Modern papers / monographs the proof program reads | **Gitignored** (`*.pdf`); only the index is tracked | [`references/README.md`](../../../references/README.md) |
| Notes | [`docs/03_research/reading_notes/`](.) | One `Author-Year-Topic.md` note per paper, house style | n/a (markdown) | [`reading_notes/README.md`](README.md) |

Deeper artifacts a paper may also earn (only when warranted, not by default):
- an **assessment dossier** in [`docs/03_research/`](..) ("how it lands on the program": the
  Davenport-Heilbronn discipline, the K1-K4 kill criteria, the spec_z landscape, the accident dossier);
- **experiments** in [`experiments/`](../../../experiments/) that instrument the paper's claims, each
  with a `LEARNINGS.md` finding and a `TODO.md` entry.

The eight reference-library role folders (mapped to the research directions):
`01_prismatic_cohomology`, `02_deninger_program`, `03_foliated_cohomology_trace`,
`04_ncg_connes`, `05_arithmetic_topology`, `06_intersection_hodge`,
`07_elliptic_curve_heights`, `08_misc`. The reading-notes index mirrors these folders.

**A PDF at the repo root is unfiled.** Root `*.pdf` is gitignored and belongs nowhere; file it into
`sources/` (primary source) or `references/NN_topic/` (reference paper). Do not leave it at root.

## 2. .gitignore rules (already in place)

```
*.pdf                # all PDFs ignored by default (references are copyrighted)
!sources/*.pdf       # EXCEPT primary sources, which are committed
```

So: `sources/` PDFs are tracked; `references/` PDFs are not (the tracked artifact is the index entry +
the reading note). Scratch text extracts (`_name.txt`, `_proto*.py` at root) are temporary; delete them
when done (do not commit). arXiv papers are often CC-BY (the Connes 2602 paper is), so they *could* be
committed, but we keep them in `references/` (gitignored, index-only) for uniformity; the arXiv ID in
the index lets anyone re-fetch.

## 3. Naming conventions

- Reference PDF: `Author(s)-Year-Short-Title.pdf`
  (e.g. `Connes-1998-Trace-Formula-in-NCG-and-Zeros-of-Riemann-Zeta.pdf`).
- Reading note: `Author-Year-Topic.md` (e.g. `Connes-2026-RH-Past-Present-Letter.md`).
- Keep the note filename close to the PDF filename so the two are traceable to each other.

## 4. The workflow (drop -> filed -> extracted -> noted -> mapped)

**Step 0 - classify.** Primary source or reference paper? Which of the eight topic folders? (Match the
paper's role to a research direction; `08_misc` if none fits.)

**Step 1 - file the PDF.** Move it from the root into `sources/` or `references/NN_topic/` with the
naming convention. References PDFs stay gitignored; sources PDFs are committed.

**Step 2 - index it.** Add a row to the relevant table:
- `references/README.md`: `| `Author-Year-Title.pdf` | Full citation | Role in the program |`
- or `sources/README.md`: `| `File` | Description |`

**Step 3 - extract the text** (for accurate notes; pick one):
- `pypdf`: `python -c "from pypdf import PdfReader; r=PdfReader('path.pdf'); open('_x.txt','w',encoding='utf-8').write(chr(10).join(p.extract_text() for p in r.pages))"`
- `pdfminer.six` (see [`sources/README.md`](../../../sources/README.md) Option A / `sources/convert_pdfs.py`)
- or the Read tool's `pages=` to read the PDF directly (good for figures/equations).
- Write to a scratch `_name.txt` at root (gitignored); delete it in Step 7.

**Step 4 - write the reading note** in `reading_notes/` in the **house style** (see any existing note,
e.g. [`Connes-1998-...`](Connes-1998-Trace-Formula-NCG-Zeros.md) or [`Connes-2026-...`](Connes-2026-RH-Past-Present-Letter.md)):
1. Title line: full citation + arXiv ID / year.
2. Blockquote: the paper's **role** in the program, **reading depth**, cross-links (the four-level
   framing, the D-H discipline, the relevant directions), and how it differs from related notes.
3. `## One-line takeaway`.
4. `## Technical content (section by section)`: bold section headers, precise definitions and theorem
   statements, key formulas, **page references**.
5. `## Project mapping`: what is proven vs the gap; which directions / experiments / findings it touches.
6. An honest depth/`Status` line. **No em or en dashes anywhere** (project style).

**Step 5 - index the note.** Add a row to `reading_notes/README.md` under the right `NN` folder, with a
one-line headline.

**Step 6 - deeper artifacts (only if warranted).** If the paper is load-bearing for the front: write an
assessment dossier in `docs/03_research/`, and/or build experiments in `experiments/` (each with a
`LEARNINGS.md` finding number and a `TODO.md` entry). Cross-link all of them to the reading note.

**Step 7 - clean up and commit.** Delete scratch `_*.txt` / `_proto*.py`. Commit the tracked changes
(the note, the index rows, any dossier/experiments). The reference PDF itself is gitignored, so the move
is local only; the committed record is the index entry. Push per the per-action authorization policy.

## 5. Worked example: Connes, arXiv:2602.04022 (2026)

The end-to-end trail, as a template:
- **Filed:** `references/04_ncg_connes/Connes-2026-RH-Past-Present-and-a-Letter-Through-Time.pdf`
  (was loose at the repo root; gitignored).
- **Indexed:** `references/README.md`, section `04`.
- **Reading note:** [`Connes-2026-RH-Past-Present-Letter.md`](Connes-2026-RH-Past-Present-Letter.md)
  (indexed in this folder's README under `04 NCG / Connes`).
- **Assessment dossier:** [`docs/03_research/connes_2602_letter_to_riemann.md`](../connes_2602_letter_to_riemann.md).
- **Experiments:** `e3s`/`e3t`/`e3u`/`e3v`/`e3y` (LEARNINGS #50-#56), instrumenting Theorem 6.1,
  the prolate ansatz, the heat trace, the marginal wall, and the stealth window.
