# Riemann Zeta Function — Deep Study Repo

A comprehensive, multi-level exploration of the Riemann Zeta Function and the Riemann Hypothesis: from intuitive visual understanding through graduate-level analysis to the frontier of current research.

## Status

**In Development** — Building out documentation, visualizations, and PDF conversions.

## What's Here

This repo is structured so you can enter at any level and go as deep as you want.

```
zeta-function/
├── docs/                        # All written explanations
│   ├── 00_intuitive/            # No math required — visual, conceptual
│   ├── 01_undergraduate/        # Calculus, complex numbers, series
│   ├── 02_graduate/             # Analytic continuation, functional equation
│   ├── 03_research/             # Current approaches, open problems
│   ├── implications/            # Why it matters (primes, physics, crypto)
│   └── solutions/               # Known approaches to the Riemann Hypothesis
├── sources/                     # PDF → Markdown/TXT conversions
│   ├── riemann_1859_original.md # Riemann's original 1859 paper (translated)
│   └── ...
├── visualizations/              # manim animation scripts
│   ├── 01_series_intro/
│   ├── 02_complex_plane/
│   ├── 03_analytic_continuation/
│   ├── 04_critical_strip/
│   └── 05_zeros/
└── LLM_ONBOARDING.md            # AI assistant quick-reference
```

## The Question

The **Riemann Hypothesis** states:

> All non-trivial zeros of the Riemann zeta function have real part equal to 1/2.

It has been open since 1859. It is one of the Millennium Prize Problems (worth $1,000,000). It governs the distribution of prime numbers, and its implications ripple through number theory, physics, cryptography, and beyond.

## Levels

| Level | Folder | Prerequisites |
|-------|--------|---------------|
| Intuitive | `docs/00_intuitive/` | None — curiosity only |
| Undergraduate | `docs/01_undergraduate/` | Calculus, basic complex numbers |
| Graduate | `docs/02_graduate/` | Complex analysis, real analysis |
| Research | `docs/03_research/` | Graduate mathematics |

## Visualizations (manim)

Built with [manim](https://github.com/3b1b/manim) (3Blue1Brown's animation engine).

See `visualizations/README.md` for setup and how to render each scene.

## Source PDFs → Markdown

Original source documents are in the repo root as PDFs. Converted/annotated versions live in `sources/`.

## Status

| Area | Status |
|------|--------|
| Repo structure | ✅ Complete |
| PDF conversions | 🔄 In Progress |
| Intuitive docs | 🔄 In Progress |
| Undergraduate docs | 🔄 In Progress |
| Graduate docs | ⏳ Planned |
| Research docs | ⏳ Planned |
| Implications docs | ⏳ Planned |
| Solutions/approaches | ⏳ Planned |
| manim visualizations | 🔄 In Progress |

## Quick Start (manim)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install manim
manim -pql visualizations/01_series_intro/series_intro.py ZetaSeriesIntro
```
