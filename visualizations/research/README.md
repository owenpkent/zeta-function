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
| 13 | `13_gue_agreement` | ~30k locally computed zeros vs the GUE gap law and Montgomery's sine kernel |
| 14 | `14_anim_gue_blind` (gif) | zeros pushed off the line while the statistics, recomputed live, never change (#174) |
| 15 | `15_polar_line` | the classic polar picture: zeta(1/2 + it) threading the origin vs Re = 0.75 never touching it |
| 16 | `16_anim_polar` (gif) | the polar trace live (origin-pass counter), then the real part sliding off the line |
| 17 | `17_phase_plot` | Wegert-style domain coloring: zeros as color pinwheels, the pole winding backward |
| 18 | `18_zeros_hear_primes` | INSTRUMENT: cos(t gamma) summed over 8880 zeros spikes at log(prime powers) with heights Lambda(n)/sqrt(n) |
| 19 | `19_zt_gram` | Z(t) with Gram points, plus the Lehmer pair (zeros 0.038 apart, arch +0.0039) |
| 20 | `20_ground_state` | INSTRUMENT: the Weil form's minimizer across scales (universal zero-locking to 0.004; multi-mode margin saturates in sigma; 50-digit solves past the fp floor) |

Figures 2, 5, 6, 8, 11, 12 are drawn from the e2an/e2ao builds (LEARNINGS
#179/#180); 13/14 use the primes thread's Riemann-Siegel engine (rsz.py); the
rest are the classical pictures those builds sit inside.

## Researched candidates (2026-08-20 survey of existing RH visualizations)

Tier A (high value, easy with the local stack):
- ~~Phase plot / domain coloring~~ **BUILT as 17**.
- ~~The duality spike plot~~ **BUILT as 18** (zeros -> primes direction; the
  primes -> zeros direction is figure 2).
- ~~Z(t) with Gram points and the Lehmer near-miss~~ **BUILT as 19**.
- **N(T) staircase vs Riemann-von Mangoldt + S(t)**: the zero count hugging
  the smooth law; ties to Turing's method.
- **Primes-Poisson vs zeros-GUE contrast**: unfolded prime gaps (exponential)
  next to figure 13 (GUE): the randomness/rigidity inversion in one glance.
- **pi(x) vs Li(x) vs R(x) with zero corrections**: the classical prediction
  picture at the pi(x) level.

Tier B (moderate effort):
- **De Bruijn-Newman heat flow** (Polymath15): animate the xi function's zeros
  under heat flow; RH = "we sit exactly at the boundary" (Lambda = 0 is
  Rodgers-Tao's lower bound, 0.22 the upper). Repo tie: the criticality
  thread's dBN probe. Needs H_t quadrature + root tracking; feasible locally.
- **3D |zeta| landscape** over the strip (pole spike + zero funnels).
- **Chebyshev race with the L-zero prediction** (the repo's own #174 positive;
  needs the primes-thread datasets).

Tier C (manim / later): the 3b1b-style analytic-continuation morph (already a
planned TODO scene), Voronin universality, audio of the zeros.

## Planned batches

- **Batch 2 remainder (the disciplines):** the Chebyshev race predicted from
  L-zeros before the primes were counted (the primes thread's positive); the
  S-finite Euler ladder's duality defect and the off-line rigidity curve once
  backlog items A2/A3 run. (The GUE pair, 13/14, is done.)
- **Batch 3 (the landscape):** the four-architecture map with kill status; the
  15-candidate satisfiability matrix; the M1-M5 ladder.
- **Manim versions** of 1/3/7 for smooth video, once the static set settles.

Conventions: every figure renders in both themes with a shared palette dict
(`THEMES` in make_figs.py); expensive data (mpmath strip grids, zero lists,
the lattice engine) is computed once per process and shared across themes;
figures carry their own suptitles so the PNGs are self-explanatory outside
the gallery.
