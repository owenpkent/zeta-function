# Visualizations — manim Scenes

Built with [manim Community Edition](https://docs.manim.community/) (v0.18+).

## Setup

### Prerequisites

| Dependency | Purpose | Install |
|------------|---------|---------|
| Python 3.10+ | Runtime | python.org or system package manager |
| manim | Animation engine | `pip install manim` |
| FFmpeg | Video encoding | `winget install Gyan.FFmpeg` / `brew install ffmpeg` |
| LaTeX (MiKTeX or TeX Live) | Math typesetting | miktex.org / tug.org/texlive |
| `preview.sty` | Required LaTeX package | `mpm --install=preview` (MiKTeX) |

### Quick start

```bash
pip install manim
# If using MiKTeX and you get "preview.sty not found":
mpm --install=preview
```

## Rendering

```bash
# Low quality, fast preview (480p, 15fps)
manim -ql visualizations/<folder>/<script>.py <SceneName>

# Medium quality (720p, 30fps)
manim -qm visualizations/<folder>/<script>.py <SceneName>

# High quality (1080p, 60fps)
manim -qh visualizations/<folder>/<script>.py <SceneName>

# 4K (2160p, 60fps)
manim -qk visualizations/<folder>/<script>.py <SceneName>
```

Output lands in `media/videos/<script_name>/<quality>/`.

## Scene Index

### Foundations (Scenes 1–5)

| # | Folder | Scene Class | What It Shows |
|---|--------|-------------|---------------|
| 1 | `01_series_intro/` | `ZetaSeriesIntro` | Partial sums of ζ(s) converging for real s > 1 |
| 2 | `02_complex_plane/` | `ZetaComplexPlane` | ζ(s) as a function on the complex plane (domain coloring) |
| 3 | `03_analytic_continuation/` | `AnalyticContinuation` | Extending ζ beyond Re(s) > 1 using the eta function |
| 4 | `04_critical_strip/` | `CriticalStrip` | The critical strip, critical line, functional equation symmetry |
| 5 | `05_zeros/` | `ZerosOnCriticalLine` | First 20 non-trivial zeros plotted on the critical line |

### Research Concepts (Scenes 6–10)

| # | Folder | Scene Class | What It Shows |
|---|--------|-------------|---------------|
| 6 | `06_zero_free_region/` | `ZeroFreeRegion` | The Vinogradov–Korobov boundary, the 2/3 wall, 67 years of no progress |
| 7 | `07_functional_equation_mirror/` | `FunctionalEquationMirror` | ξ(s) = ξ(1−s) as mirror symmetry; why zeros prefer the mirror; the self-adjointness analogy |
| 8 | `08_robins_inequality/` | `RobinsInequality` | Robin's inequality (RH equivalence), σ(n)/(n ln ln n) vs e^γ, the 5040 exception, colossally abundant numbers |
| 9 | `09_zeta_3d_surface/` | `Zeta3DSurface` | \|ζ(s)\| as a 3D surface over the complex plane; zeros as dips to floor; rotating camera |
| 10 | `10_five_gaps/` | `FiveGaps` | The five fundamental obstructions (positivity, geometry, exactness, analytic ceiling, bridge) and how they converge |

### Explainer Series (Scenes 11-13)

Multi-part explainer videos. Each is a sequence of `Scene` / `ThreeDScene` classes rendered separately and concatenated with FFmpeg. Scenes 12 and 13 carry their full narration on screen as subtitles, so they play as self-contained silent videos, and each ships a `NARRATION.md` voiceover script.

| # | Folder | Scenes | What It Shows |
|---|--------|--------|---------------|
| 11 | `11_three_stage_rh/` | `StageA_WaterThenBeads`, `StageB_Watershed`, `StageC_EmptySocket`, `Close_MasterImage` | The dense three-stage arc: RH from scratch, the all-roads convergence, and the M4 polarization gap (the project's frontier). Full storyboard in `SPEC.md`. |
| 12 | `12_what_is_rh/` | `Part1_Primes`, `Part2_Machine`, `Part3_MapAndZeros`, `Part4_Hypothesis` | Zero-background explainer "What is the Riemann Hypothesis?". Every term is defined with an everyday analogy first (primes as atoms, zeta as a number machine, zeros as where it goes silent). Script in `NARRATION.md`. |
| 13 | `13_functional_equation/` | `Ep2_Part1_Destination` through `Ep2_Part5_Harvest` | Graduate course Episode 2, "The Functional Equation": a rigorous derivation of xi(s)=xi(1-s) via the theta function and Poisson summation, opening on a 3D \|zeta\| terrain. Theorem statements (T1-T12) and the 6-episode course outline live in `NARRATION.md`. |

### Applied Context (Scene 14)

A standalone chaos-theory context scene, the visual companion to [`../experiments/chaos/`](../experiments/chaos/) and [`../docs/03_research/quantum_chaos_and_the_zeros.md`](../docs/03_research/quantum_chaos_and_the_zeros.md) (the zeros carry the spectral statistics of a quantized chaotic system).

| # | Folder | Scene Classes | What It Shows |
|---|--------|---------------|---------------|
| 14 | `14_lorenz_attractor/` | `LorenzAttractor`, `ButterflyEffect` | The Lorenz strange attractor traced in 3D with an orbiting camera (`LorenzAttractor`), and two trajectories from starts one part in a million apart diverging (`ButterflyEffect`), sensitive dependence made literal. Both are `ThreeDScene`s; the trajectory is RK4-integrated in-scene. |

## Render all scenes

```bash
# Low quality batch render
manim -ql visualizations/01_series_intro/series_intro.py ZetaSeriesIntro
manim -ql visualizations/02_complex_plane/complex_plane.py ZetaComplexPlane
manim -ql visualizations/03_analytic_continuation/analytic_continuation.py AnalyticContinuation
manim -ql visualizations/04_critical_strip/critical_strip.py CriticalStrip
manim -ql visualizations/05_zeros/zeros_on_critical_line.py ZerosOnCriticalLine
manim -ql visualizations/06_zero_free_region/zero_free_region.py ZeroFreeRegion
manim -ql visualizations/07_functional_equation_mirror/functional_equation_mirror.py FunctionalEquationMirror
manim -ql visualizations/08_robins_inequality/robins_inequality.py RobinsInequality
manim -ql visualizations/09_zeta_3d_surface/zeta_3d_surface.py Zeta3DSurface
manim -ql visualizations/10_five_gaps/five_gaps.py FiveGaps
manim -ql visualizations/14_lorenz_attractor/lorenz_attractor.py LorenzAttractor
manim -ql visualizations/14_lorenz_attractor/lorenz_attractor.py ButterflyEffect
```

## Render the explainer series

Each explainer is several scenes. Render the parts (you can list them in one call), then concatenate with FFmpeg.

```bash
# Scene 12 - "What is the Riemann Hypothesis?" (beginner)
manim -qm visualizations/12_what_is_rh/what_is_rh.py Part1_Primes Part2_Machine Part3_MapAndZeros Part4_Hypothesis

# Scene 13 - "The Functional Equation" (graduate, Episode 2)
manim -qm visualizations/13_functional_equation/functional_equation.py Ep2_Part1_Destination Ep2_Part2_GammaFactor Ep2_Part3_Theta Ep2_Part4_Symmetric Ep2_Part5_Harvest
```

Then join the parts in order (example for scene 12):

```bash
# list.txt contains: file 'Part1_Primes.mp4' (one per line, in order)
ffmpeg -f concat -safe 0 -i list.txt -c copy What_Is_RH_FULL.mp4
```

## Notes

- All scenes use manim Community Edition (v0.18+)
- Scenes are self-contained — each file imports only `manim` and `numpy`
- Math is rendered via LaTeX — requires a working LaTeX installation
- Scene 9 (`Zeta3DSurface`) is a `ThreeDScene` and takes longer to render due to surface computation
- Scenes 11 and 13 also open with a `ThreeDScene` \|zeta\| terrain, so their first part renders more slowly than the 2D parts
- Scene 14 (`LorenzAttractor`, `ButterflyEffect`) is a `ThreeDScene` and needs no LaTeX beyond the title, since it draws integrated trajectories rather than typeset math
- Scenes 12 and 13 are silent but self-explanatory: the narration appears on screen as subtitles, and the full spoken script is in each folder's `NARRATION.md`
- Rendered videos are gitignored (`media/`)
