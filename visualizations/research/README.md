# Research-figure gallery: seeing the problem

Locally generated figures and animations for visual understanding of the RH
problem and this repo's own objects. Static matplotlib + GIF animations, no
cloud, no manim dependency; all output is regenerable and gitignored.

## Run

```
python visualizations/research/make_figs.py     # 8 static figures, light + dark themes (~4 min)
python visualizations/research/make_anims.py    # 4 animations, both themes (~2 min)
python visualizations/research/make_figs.py --only 6    # rebuild one figure
python visualizations/research/make_figs.py --html      # rebuild the page only
```

Then open `visualizations/research/_out/index.html`. The page is
self-contained: **dark mode by default** with a toggle (or press T), sidebar
navigation, click any figure for a full-screen lightbox, arrow keys to step
between figures. Captions persist in `_out/manifest.json`, so single-figure
rebuilds keep the gallery intact. Every figure exists as `<base>__dark.png`
and `<base>__light.png`; the page swaps them with the theme.

## Batch 1 (2026-08-19)

| # | base | what it shows |
|---|------|----------------|
| 1 | `01_the_problem` | zeta's strip (all zeros on the line) vs Davenport-Heilbronn (off-line pair at 85.7) |
| 2 | `02_zeros_from_integers` | the e2an multiplier from raw integer sums; dips = zeros to 1e-4, zeta never evaluated |
| 3 | `03_explicit_formula` | psi(x) rebuilt from 0 / 10 / 40 / 91 zero pairs |
| 4 | `04_error_budget` | the prime-counting error hugging sqrt(x); what one rogue zero would cost |
| 5 | `05_sp_scorecard` | the five-component scorecard (#179): zeta / D-H / Beurling per cell |
| 6 | `06_margin_law` | the margin law (#180) and the prime-side certification floor |
| 7 | `07_central_hole` | why the exponent is gamma_1^2: the worst window hides in the central hole |
| 8 | `08_carrier` | the circle carrier at L = 8 vs 16; D-H's off-line pair never dips |
| 9 | `09_anim_explicit` (gif) | the staircase assembling one zero pair at a time |
| 10 | `10_anim_offline` (gif) | dragging one zero off the line; the error envelope growing |
| 11 | `11_anim_carrier` (gif) | the carrier resolving as L slides 6 to 20; D-H star never dips |
| 12 | `12_anim_margin` (gif) | the window narrowing into the hole; the margin sliding down its law |

Figures 2, 5, 6, 8, 11, 12 are drawn from the e2an/e2ao builds (LEARNINGS
#179/#180); the rest are the classical pictures those builds sit inside.

## Planned batches

- **Batch 2 (the disciplines):** the Chebyshev race predicted from L-zeros
  before the primes were counted (the primes thread's positive); the
  GUE-blindness picture (move zeros off the line, statistics unchanged: why
  Level 3 cannot close RH); the S-finite Euler ladder's duality defect and the
  off-line rigidity curve once backlog items A2/A3 run.
- **Batch 3 (the landscape):** the four-architecture map with kill status; the
  15-candidate satisfiability matrix; the M1-M5 ladder.
- **Manim versions** of 1/3/7 for smooth video, once the static set settles.

Conventions: every figure renders in both themes with a shared palette dict
(`THEMES` in make_figs.py); expensive data (mpmath strip grids, zero lists,
the lattice engine) is computed once per process and shared across themes;
figures carry their own suptitles so the PNGs are self-explanatory outside
the gallery.
