# LLM Onboarding

Quick reference for AI assistants working on this repository.

---

## Project Overview

**Name:** Riemann Zeta Function — Deep Study Repo
**Purpose:** Multi-level exploration of the Riemann zeta function and Riemann Hypothesis, from intuitive to research-level, with manim visualizations.
**Status:** In Development

## About the Owner

I'm Owen — a wheelchair user with muscular dystrophy.

- **Typing is hard** — Be proactive. Make decisions. Don't ask for confirmation on small things.
- **Offer A/B/C choices** — I can type one letter instead of explaining.
- **PowerShell on Windows** — Use PowerShell syntax. Prefer single-line commands.
- **Accessibility matters** — Many of my projects are tools I actually need.

---

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview, status, structure map |
| `TODO.md` | Task tracking (`- [ ]` checkbox format) |
| `docs/` | All written explanations by level |
| `sources/` | PDF → Markdown conversions of primary sources |
| `visualizations/` | manim animation scripts |
| `LLM_ONBOARDING.md` | This file |

---

## Repo Structure

```
zeta-function/
├── docs/
│   ├── 00_intuitive/            # No math required
│   ├── 01_undergraduate/        # Calculus + complex numbers
│   ├── 02_graduate/             # Complex analysis
│   ├── 03_research/             # Frontier approaches
│   ├── implications/            # Why RH matters
│   └── solutions/               # Known proof attempts/approaches
├── sources/                     # Converted PDFs
├── visualizations/              # manim scenes
│   ├── 01_series_intro/
│   ├── 02_complex_plane/
│   ├── 03_analytic_continuation/
│   ├── 04_critical_strip/
│   └── 05_zeros/
├── README.md
├── TODO.md
└── LLM_ONBOARDING.md
```

---

## Tech Stack

- **Language:** Python
- **Visualization:** manim (3Blue1Brown) — `pip install manim`
- **Docs:** Markdown with LaTeX math (`$...$` inline, `$$...$$` block)

## Math Notation

Use standard LaTeX in Markdown:
- Inline: `$\zeta(s)$`
- Block: `$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$$`

---

## Git Commits

```powershell
git add -A; git commit -m "docs: add intuitive explanation"; git push
```

Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`

---

## Constellation

This repo is tracked by Constellation. It has `README.md` with `## Status` and `TODO.md` with checkboxes.
