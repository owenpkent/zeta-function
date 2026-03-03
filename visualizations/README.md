# Visualizations — manim Scenes

Built with [manim](https://github.com/3b1b/manim) (3Blue1Brown's animation library).

## Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install manim
```

## Rendering a Scene

```powershell
# Low quality (fast preview)
manim -pql <script.py> <SceneName>

# High quality
manim -pqh <script.py> <SceneName>

# Examples
manim -pql visualizations/01_series_intro/series_intro.py ZetaSeriesIntro
manim -pql visualizations/02_complex_plane/complex_plane.py ZetaComplexPlane
manim -pql visualizations/03_analytic_continuation/analytic_continuation.py AnalyticContinuation
manim -pql visualizations/04_critical_strip/critical_strip.py CriticalStrip
manim -pql visualizations/05_zeros/zeros_on_critical_line.py ZerosOnCriticalLine
```

## Scene Index

| # | Folder | Scene | What It Shows |
|---|--------|-------|---------------|
| 1 | `01_series_intro/` | `ZetaSeriesIntro` | Partial sums of ζ(s) converging for real s > 1 |
| 2 | `02_complex_plane/` | `ZetaComplexPlane` | ζ(s) as a function on the complex plane (domain coloring) |
| 3 | `03_analytic_continuation/` | `AnalyticContinuation` | Extending ζ beyond Re(s) > 1 using the eta function |
| 4 | `04_critical_strip/` | `CriticalStrip` | The critical strip, critical line, and symmetry |
| 5 | `05_zeros/` | `ZerosOnCriticalLine` | First 20 non-trivial zeros plotted on the critical line |

## Notes

- All scenes use `manim` Community Edition (v0.18+)
- Scenes are self-contained — each file imports only `manim`
- Math is rendered via LaTeX (requires a LaTeX install, or use `--disable_caching`)
- For fast preview without LaTeX: add `tex_template=TexFontTemplates.gnu_freeserif_freesans` or use `MathTex` with simple expressions
