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
```

## Notes

- All scenes use manim Community Edition (v0.18+)
- Scenes are self-contained — each file imports only `manim` and `numpy`
- Math is rendered via LaTeX — requires a working LaTeX installation
- Scene 9 (`Zeta3DSurface`) is a `ThreeDScene` and takes longer to render due to surface computation
- Rendered videos are gitignored (`media/`)
