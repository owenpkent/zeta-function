# MANIM SCENE SPEC: The Three-Stage RH Visual

Animates the approved three-stage RH visual (RH from scratch, the all-roads
convergence, the M4 signature gap) as one running "hall of machines" image.
Grounded in the repo's existing manim conventions (scenes 07 and 09) and audited
for manim feasibility. No em dashes or en dashes appear anywhere in this spec or
in any caption.

## 1. FILE HEADER

**Target path (one directory, one module file):**
```
visualizations/11_three_stage_rh/three_stage_rh.py
```
Author all four Scene classes in the single module file (matches the repo's one-file-per-directory convention; scenes 01-10 each have one `.py`). Render each Scene separately and concatenate in post.

**Manim flavor + import line (stock ManimCE, exactly as scenes 07/09):**
```python
from manim import *
import numpy as np
```

**Scene classes (one per stage):**
- `class StageA_WaterThenBeads(ThreeDScene)` (begins 3D, flattens to 2D)
- `class StageB_Watershed(Scene)` (pure 2D)
- `class StageC_EmptySocket(ThreeDScene)` (mostly 2D, one 3D saddle insert)
- `class Close_MasterImage(Scene)` (pure 2D assembly)

**Exact render commands (PowerShell, single line each, from repo root):**
```powershell
manim -qm visualizations/11_three_stage_rh/three_stage_rh.py StageA_WaterThenBeads
manim -qm visualizations/11_three_stage_rh/three_stage_rh.py StageB_Watershed
manim -qm visualizations/11_three_stage_rh/three_stage_rh.py StageC_EmptySocket
manim -qm visualizations/11_three_stage_rh/three_stage_rh.py Close_MasterImage
```
Use `-qm` (medium 720p30) for iteration, `-qh` for final. To render all four at once, append the four class names to one `manim -qm <file>` invocation.

**Total runtime estimate (sum of the four clips):**
- Stage A: ~75 s
- Stage B: ~70 s
- Stage C: ~95 s
- Close: ~35 s
- Total: about 4 min 35 s.

**Module docstring (top of file):**
```python
"""
ThreeStageRH
============
The three-stage RH picture as one hall of machines. Stage A builds RH from the
zeta terrain down to beads on the critical line. Stage B funnels four proof roads
into one neck (realization is free, the signature is the open half). Stage C opens
the one empty socket: the missing global indefinite (1, n-1) polarization over
Spec(Z) (M4, the arithmetic Hodge standard conjecture). Supplying it is RH.
Render each Scene separately and concatenate. ThreeDScene only for the terrain
(Stage A) and the saddle (Stage C); everything else is 2D VMobjects.

Faithfulness note: zeta_approx and eta_approx (copied from scene 09) drive the
Stage A terrain HEIGHT only. The pole at s = 1 is finite-capped in those helpers
(complex(10, 0)) and the visual is capped at min(val, 4.0). The explicit-formula
wave curve in A6 does NOT call those helpers; it is a precomputed schematic sum.
Trivial zeros at -2, -4, -6 are intentionally out of frame: the story lives in
the critical strip, so no viewer expects them.
"""
```

---

## 2. GLOBAL DESIGN

### Color legend (assign once at module top as constants, reuse everywhere)

```python
# Semantic palette (single source of truth for the whole piece)
C_VISIBLE      = WHITE      # solid, on-screen, "what you can see"
C_INVISIBLE    = GREY_B     # ghost / fogged / the one missing object
C_REALIZATION  = GREEN      # realization half, free, perfect pairing, on-line
C_SIGNATURE    = RED        # signature half, open, off-line, alarm, the saddle "down"
C_CRITLINE     = YELLOW     # critical line, the FE mirror, the neck
C_LEVEL3       = BLUE       # Level 3, the realization-half, the bowl reject
C_DH           = "#C2185B"  # Davenport-Heilbronn red (distinct magenta-red so it
                            # never reads as a generic alarm; the impostor color)
C_POLE         = ORANGE     # the s=1 pole spike (residue 1)
C_UP_AXIS      = GREEN      # the single ample / up direction of the saddle
C_DOWN_AXIS    = RED        # the orthogonal down directions of the saddle
C_FOG          = GREY       # open/unknown overlay fill
```

Concrete meaning bindings:
- VISIBLE / solid: `C_VISIBLE` (white) stroke, `fill_opacity` >= 0.7.
- INVISIBLE / ghost: `C_INVISIBLE` (GREY_B), `stroke_opacity ~ 0.35`, dashed where it is a line (`DashedLine`).
- Up-axis (one ample direction): `C_UP_AXIS` (green). Down-axes (the many): `C_DOWN_AXIS` (red).
- The empty socket: drawn as an `Annulus` with `C_INVISIBLE` stroke and NO fill (the hole shows the background); never filled until the Close, where it is only annotated, never plugged.
- D-H red: `C_DH` (#C2185B), used only for Davenport-Heilbronn objects.
- Critical line / FE mirror / neck: `C_CRITLINE` (yellow).

### Persistent on-screen elements

(P1) The running master image (thumbnail, top-right corner). A small `VGroup` `master_thumb` assembled by `make_master_thumb()`: a row of 3 tiny machine glyphs, a tiny funnel, and a tiny empty annulus socket, scaled to about 1.6 units wide, `to_corner(UR, buff=0.25)`, `set_opacity(0.5)`. It is `add`ed at the start of every stage and stays. In Stage A only the machines glow; in B only the funnel; in C only the socket (use `.set_opacity` per-part to highlight the active stage). In a `ThreeDScene` add it via `add_fixed_in_frame_mobjects(master_thumb)`.

(P2) The two-column tracker (VISIBLE | INVISIBLE), bottom-left, screen-locked. A `VGroup` `tracker` from `make_tracker()`: two stacked `Text` headers `"WHAT YOU CAN SEE"` (`C_VISIBLE`) and `"THE ONE INVISIBLE THING"` (`C_INVISIBLE`), each over an empty `VGroup` column that grows. A helper `add_to_visible(label)` / `add_to_invisible(label)` appends a small (`font_size=14`) `Text` bullet under the right header with a 0.4 s `FadeIn`. Position `to_corner(DL, buff=0.3)`, scale so it occupies the left ~3 units. In any `ThreeDScene` register via `add_fixed_in_frame_mobjects`. The INVISIBLE column carries the SAME single object in all three stages, phrased per stage: "zeros sit EXACTLY on the line (a knife-edge)" in A, "the SIGNATURE half, open over Z" in B, "the missing polarization over Spec(Z)" in C. State in the Close that all three were the one object.

### Camera plan

- Stage A: start `set_camera_orientation(phi=65*DEGREES, theta=-45*DEGREES, zoom=0.7)` (copy scene 09 exactly). One slow `begin_ambient_camera_rotation(rate=0.12)` over the terrain beat. Then the load-bearing move: `move_camera(phi=0, theta=-90*DEGREES, run_time=2)` to flatten top-down before the bead collapse, then `FadeOut(surface)` and hand off to 2D logic (the flatten-then-handoff recipe). Do NOT run 2D Transforms while the live Surface is on screen.
- Stage B: pure 2D, static camera. No moves.
- Stage C: pure 2D for the matrix/transparency/Rosetta/hall beats. ONE 3D insert for the saddle: render the saddle as its own short `move_camera` sequence (`phi=70*DEGREES, theta=-45*DEGREES`), then flatten (`phi=0`) and `FadeOut` before continuing 2D. Keep `add_fixed_in_frame_mobjects` for all captions while 3D is live.
- Close: pure 2D, static.

### Pacing rules (apply uniformly)

- Surfaces: `Create` over 2.5 to 3 s. Road/funnel builds: 1.5 to 2 s. `LaggedStartMap` reveals: `lag_ratio=0.3` to `0.5`. Hold 1.5 to 2 s after each conceptual beat. Caption `Write`: 1 s. Bar / ValueTracker dips: 1.5 s. `FadeOut`-clear between sub-beats: 0.5 s.
- Cap any |zeta| height at `min(val, 4.0)` (scene 09 convention). Cap Surface `resolution=(50, 80)`; never animate resolution.
- Every on-screen caption obeys the NO em dash / en dash rule: only periods, colons, commas, parentheses, hyphens.

---

## 3. SCENE-BY-SCENE

> Reused helpers (defined in section 4): `zeta_approx`, `eta_approx` (copy verbatim from scene 09; terrain height only), `KNOWN_ZEROS_T` (copy from scene 07; 10 entries), `make_master_thumb`, `make_tracker`, `add_to_visible`, `add_to_invisible`, `make_bead_wire`, `make_machine_icon`, `make_gear_socket`, `make_road`.

---

### STAGE A: RH from scratch (water then beads). Class: StageA_WaterThenBeads(ThreeDScene)

Beat A1. Title and persistent frame.
- (a) Open frame.
- (b) Mobjects: `Title(r"Stage A: From the Zeta Terrain to the Beads")`; `master_thumb` (machines highlighted); `tracker`.
- (c) `add_fixed_in_frame_mobjects(title, master_thumb, tracker)`; `Write(title)`; `FadeIn(master_thumb)`; `FadeIn(tracker)`; then `FadeOut(title)`.
- (d) 4 s.
- (e) Caption: none beyond the title text above.
- (f) Column: persistent frame, no new entry.

Beat A2. The terrain (drain-holes and capped pole).
- (a) Zeta terrain.
- (b) `ThreeDAxes` (x_range `[-0.5,1.5,0.5]`, y_range `[0,35,5]`, z_range `[0,4,1]`, lengths 6/8/4, as scene 09); `Surface` of `zeta_magnitude` (`resolution=(50,80)`, `set_fill_by_value` with the scene-09 colorscale); `crit_curve` (`VMobject`, `C_CRITLINE`) along sigma=0.5; `zero_dots` = `Dot3D` at `c2p(0.5, t0, 0)` for the first five `KNOWN_ZEROS_T` (`C_SIGNATURE`); `pole` = thin `Cylinder` (small radius, so it does not occlude the front drain-holes) at `c2p(1, 0, ...)` rising to the capped top, `C_POLE`, with a fixed-frame `MathTex(r"\text{pole at } s=1, \text{ residue } 1")` placed in a clear corner so it does not overlap the axis labels.
- (c) `set_camera_orientation(phi=65*DEGREES, theta=-45*DEGREES, zoom=0.7)`; `Create(axes)` plus axis labels; `Create(surface, run_time=3)`; `Create(crit_curve, run_time=2)`; `LaggedStartMap(FadeIn, zero_dots, lag_ratio=0.2)`; `Create(pole)` plus `Write` its label (fixed in frame); `begin_ambient_camera_rotation(rate=0.12)`, `wait(5)`, `stop_ambient_camera_rotation()`.
- (d) about 16 s.
- (e) Caption (fixed in frame, three short `Text` lines): "Height is the size of zeta." / "Zeros are drain-holes (height 0) on sigma = 1/2." / "The pole at s = 1 is one spike (capped here so it does not flatten the rest)."
- (f) Column VISIBLE: "the terrain, the zeros, the pole".

Beat A3. Why zeta is special (Euler product).
- (a) Euler-product caption over the terrain.
- (b) `MathTex(r"\zeta(s)=\sum_{n\ge 1} n^{-s}=\prod_p (1-p^{-s})^{-1}\quad(\sigma>1)")` and a second `MathTex(r"\text{equal by unique factorization}")` (both fixed in frame, `.scale(0.6)`).
- (c) `add_fixed_in_frame_mobjects(...)`; `Write` both; hold; `FadeOut`.
- (d) 5 s.
- (e) Caption: "The series and the Euler product agree for sigma greater than 1. That equality (unique factorization) is what fakes lack."
- (f) Column VISIBLE: "the Euler product (unique factorization)".

Beat A4. Three compounding symmetries and the off-line quartet.
- (a) Flatten to 2D, then symmetries.
- (b) After `move_camera(phi=0, theta=-90*DEGREES, run_time=2)` and `FadeOut(surface, pole, crit_curve, zero_dots)`, switch to a 2D `Axes` overlay (re-created as a flat `Axes`, x_range `[-0.3,1.3]`, y_range scaled around `[-90,90]`, mirror at sigma=0.5). Mobjects: `mirror` = `Line` at sigma=0.5 (`C_CRITLINE`) plus glow line (reuse the scene-07 pattern); `conj_axis` = horizontal `Line` at t=0 (`C_CRITLINE`, dashed); four `Dot`s of the quartet at `(beta,t),(1-beta,t),(beta,-t),(1-beta,-t)` with `beta=0.7, t=20` (`C_SIGNATURE`); a `DashedLine` rectangle connecting them; `MathTex(r"\rho \to 1-\rho")`, `MathTex(r"\rho \to \bar\rho")`, `MathTex(r"\text{RH: they coincide on } \sigma=\tfrac12")`.
- (c) `move_camera` flatten; `FadeOut` the 3D mobjects; `Create(mirror_glow), Create(mirror)`; `Create(conj_axis)`; `LaggedStartMap(FadeIn, quartet, lag_ratio=0.3)`; `Create(dashed_rect)`; then `Transform` the four quartet dots inward to two coincident dots on sigma=0.5 to show the on-line collapse; `Write` the three symmetry labels in sequence.
- (d) about 14 s.
- (e) Caption: "Three symmetries compound. The functional equation (rho to 1 minus rho), conjugation (rho to conjugate rho), and RH, which says they coincide on the line. A single off-line zero is forced into a quartet of four. Zeta is nonzero on sigma = 1 (the prime number theorem, 1896)."
- (f) Column VISIBLE: "the three symmetries, the quartet".

Beat A5. Collapse to beads on a wire.
- (a) 2D landscape to 1D beads.
- (b) `wire` = vertical `Line` at sigma=0.5 (`C_CRITLINE`); `beads` = `VGroup` of `Dot` (`C_REALIZATION`) at heights `KNOWN_ZEROS_T` via `make_bead_wire`; `density_label` = `MathTex(r"\text{density near } T:\ \tfrac{1}{2\pi}\log\!\big(\tfrac{T}{2\pi}\big)")`.
- (c) `ReplacementTransform(flat_axes, wire)`; `Transform` each remaining on-line dot into its bead position (per-bead lag via `AnimationGroup`); `LaggedStartMap(FadeIn, extra_beads, lag_ratio=0.25)` for the rest of the list; `Write(density_label)`.
- (d) about 10 s.
- (e) Caption: "Redraw the zeros as beads on one wire at sigma = 1/2, at heights 14.13, 21.02, 25.01, 30.42, 32.94, and on. That promotion (every bead exactly on the wire) is the hypothesis."
- (f) Column VISIBLE: "the beads on the wire".

Beat A6. The explicit formula (schematic wave sum).
- (a) Waves correcting the prime staircase.
- (b) New small `Axes` (x = count up to about 30, lower third); `staircase` = `VMobject` polyline stepping at primes 2,3,5,7,11, ... (the prime-counting staircase); three precomputed partial-sum curves `psum_1, psum_2, psum_3`, where `psum_k` is `axes.plot` (or a `VMobject` from a numpy sample array) of the schematic envelope `sum_{j<=k} x**0.5 * cos(t_j * log(x))` over the first three `KNOWN_ZEROS_T` heights `t_1, t_2, t_3`. `n_terms` is an integer index 0..3 only; there is NO `always_redraw` (it conflicts with Transform). `MathTex(r"\pi(x)=\mathrm{Li}(x)-\sum_\rho \mathrm{Li}(x^\rho)-\cdots")` fixed at top.
- (c) `Create(staircase)`; `FadeIn(psum_1)`; `ReplacementTransform(psum_1, psum_2)`; `ReplacementTransform(psum_2, psum_3)`, so the running approximation visibly tightens toward the staircase as terms are added. All curves are precomputed numpy sample arrays outside any updater (the avoid-list rule). The displayed formula stays exact; the curve is illustrative, and it does NOT call `zeta_approx`/`eta_approx`.
- (d) about 12 s.
- (e) Caption: "Each zero is a wave correcting the prime staircase. Height t is the frequency, the real part sigma is the amplitude (x to the sigma). At sigma = 1/2 every wave is balanced at the square root of x."
- (f) Column VISIBLE: "the explicit-formula waves". Column INVISIBLE (the single recurring entry, A form): "zeros sit EXACTLY on the line (not 0.5000001), a knife-edge".

---

### STAGE B: All roads converge (watershed funnel). Class: StageB_Watershed(Scene)

Beat B1. Title and frame (funnel highlighted in thumb).
- (a) Open.
- (b) `Title("Stage B: Four Roads, One Neck")`; re-`add` `master_thumb` (funnel part highlighted via `.set_opacity`) and `tracker`.
- (c) `Write(title)`; `FadeIn(master_thumb, tracker)`; `FadeOut(title)`.
- (d) 3 s.
- (e) Caption: none beyond title.
- (f) Persistent frame.

Beat B2. Four roads converging to the neck.
- (a) The watershed.
- (b) Four `make_road(...)` outputs (thick `VMobject` CubicBezier paths, tapering) from four left-edge start heights to a common `neck` `Dot` at right-center (`C_CRITLINE`); each labeled by a `Text`: "1 Spectral (Hilbert-Polya)", "2 Arithmetic-geometric (Deninger / F_1)", "3 Direct positivity (Weil / Li)", "4 Analytic (zero-free)". Each road is split along its length into a LEFT half (`C_REALIZATION` green) and a RIGHT half (`C_SIGNATURE` red) by `make_road` returning a two-segment group.
- (c) `LaggedStartMap(Create, roads, lag_ratio=0.4)`; `Write` the four labels; `FadeIn(neck)`.
- (d) about 10 s.
- (e) Caption: "Four roads. Each splits into a left half (REALIZATION: zeta as a trace or determinant, often a theorem) and a right half (the SIGNATURE: one positivity statement, the same object every road, open over Z)."
- (f) Column VISIBLE: "the four roads, the realization halves". Column INVISIBLE: "the SIGNATURE half, open over Z" (the single recurring entry, B form).

Beat B3. The neck: right halves collapse to one point.
- (a) Convergence.
- (b) The four red right-half segments; the `neck` dot.
- (c) `ReplacementTransform` the four red halves so they merge into the single `neck` dot; `Flash(neck, color=C_SIGNATURE)`; `Write(MathTex(r"\text{one positivity, every road}"))`.
- (d) about 6 s.
- (e) Caption: "The right halves are one statement. They collapse to a single neck."
- (f) Column INVISIBLE: reinforce the existing entry (no new bullet; `Indicate` the existing one).

Beat B4. The Davenport-Heilbronn tollgate.
- (a) D-H discipline.
- (b) `tollgate` = two `Line` posts across roads 1, 3, 4 (`C_DH`); road 2 re-routed around the gate (an arc `VMobject` that bypasses it); `barrier` on road 4 stopping it short of the neck, labeled `MathTex(r"\text{capped at } 2/3")`; per-road verdict `Text`s: "1: trace, not signature", "2: unique escape (a polarization, not a circular trace identity)", "3: marginal positivity", "4: capped at 2/3 (Vinogradov-Korobov)".
- (c) `Create(tollgate)`; animate roads 1/3/4 passing through it, road 2 detouring around; `Create(barrier)` on road 4; `Write` verdicts with `LaggedStart`.
- (d) about 14 s.
- (e) Caption: "Roads 1, 3, 4 must pass the Davenport-Heilbronn tollgate (D-H has the functional equation but no Euler product, and off-line zeros near 0.8085 plus 85.7 i). Road 2 routes around it: it needs the Euler product that D-H lacks. Road 4 only grazes the neck, capped at 2/3."
- (f) Column VISIBLE: "the D-H tollgate, the road-2 escape".

Beat B5. The Level 3 vs Level 4 altitude cut.
- (a) Altitude line and alarm.
- (b) Two horizontal reference `Line`s labeled `Text("Level 3")` (`C_LEVEL3`) and `Text("Level 4")` (`C_SIGNATURE`); a row of eigenvalue bars via `BarChart` (or a `VGroup` of `Rectangle`s); a `zero_baseline` `Line`; one bar driven by a `ValueTracker` dipping below zero; `alarm_text` = `Text("ALARM", color=C_SIGNATURE)`; a `SurroundingRectangle` on the rogue bar.
- (c) First pass at Level 3: drive the bar below baseline, NO alarm (caption: tolerated). Second pass at Level 4: the same dip fires the alarm: `Flash` plus `Indicate(rogue_bar, color=C_SIGNATURE)` plus a toggling-opacity `SurroundingRectangle` plus `Write(alarm_text)`.
- (d) about 12 s.
- (e) Caption: "Level 3 (Selberg central limit, GUE spacing, log-correlated) tolerates a rogue zero at beta = 0.51 as a local ripple. Level 4 (positivity) forbids it: an eigenvalue dips below 0 and the alarm fires. Note: Level 4 equals positivity is a finding (about 80/20), not a theorem."
- (f) Column VISIBLE: "the altitude cut, the alarm".

---

### STAGE C: The empty socket (the saddle and the missing gear). Class: StageC_EmptySocket(ThreeDScene)

Beat C1. Title and frame (socket highlighted in thumb).
- (a) Open.
- (b) `Title("Stage C: The One Empty Socket")`; `master_thumb` (socket highlighted); `tracker`. All via `add_fixed_in_frame_mobjects`.
- (c) `Write(title)`; `FadeIn`; `FadeOut(title)`.
- (d) 3 s.
- (e) Caption: none beyond title.
- (f) Persistent frame.

Beat C2. Perfect pairing for free, then the demand.
- (a) The pairing and the RH demand.
- (b) `MathTex(r"\rho \to 1-\rho \quad \text{(perfect, non-degenerate, free from the FE)}")`; then `MathTex(r"\text{RH: demand } 1-\rho=\bar\rho \iff \mathrm{Re}=\tfrac12")`; an arrow from the first to the second.
- (c) `Write` first (`C_REALIZATION`); `Write` second (`C_SIGNATURE`); `Create(arrow)`.
- (d) about 7 s.
- (e) Caption: "The pairing rho to 1 minus rho is perfect for free (the functional equation gives it, even D-H has it). RH demands that this pairing equal conjugation: 1 minus rho equals conjugate rho exactly when the real part is 1/2. That demand is a polarization (a positivity)."
- (f) Column VISIBLE: "the perfect pairing (free)".

Beat C3. The saddle (1, n-1) versus the rejected bowl (3D insert).
- (a) Signature as a saddle.
- (b) `ThreeDAxes`; `bowl` `Surface` `z=x^2+y^2` (all-positive, `C_LEVEL3`); `saddle` `Surface` `z=x^2-y^2` with `set_fill_by_value` diverging (`C_LEVEL3` for negative z to `C_SIGNATURE` for positive z, keyed on z-sign); `up_arrow` = `Arrow3D` up the positive eigendirection (`C_UP_AXIS`); several `down_arrows` along the negative directions (`C_DOWN_AXIS`); `MathTex(r"(1,\,n-1)")` fixed in frame.
- (c) `move_camera(phi=70*DEGREES, theta=-45*DEGREES)`; `Create(bowl)`; hold; `ReplacementTransform(bowl, saddle)` (the Lee-Yang reject becomes the real object); `Create(up_arrow)`, `LaggedStartMap(Create, down_arrows)`; `Write` the `(1,n-1)` label; then `move_camera(phi=0)` and `FadeOut(saddle, arrows)` to hand back to 2D.
- (d) about 16 s.
- (e) Caption: "The signature is a saddle, not an all-positive bowl. The target is the indefinite Hodge-index signature (1, n-1): one up-axis (the ample, Euler-pole class), every orthogonal axis down. All-positive (Lee-Yang) is the wrong object, a dead branch. Infinite-dimensional, one direction per zero (drawn here as a finite schematic). The (1, n-1) count across all truncations pins every zero to the line."
- (f) Column VISIBLE: "the saddle, the one up-axis". Column INVISIBLE: "the missing polarization over Spec(Z)" (the single recurring entry, C form, the master entry).

Beat C4. Two transparencies over the pairing matrix.
- (a) Perfectness opaque, positivity fogged.
- (b) `matrix_grid` = `Matrix` (or `VGroup` of `Square`s); a bottom overlay `Rectangle` `perfect` (full-opacity, `C_REALIZATION`) with a check and tag `MathTex(r"\text{Mathlib: riemannZeta\_one\_sub}")`; a top overlay `Rectangle` `positivity` (`fill_opacity=0.4`, `C_FOG`) with a big `MathTex(r"?")` and label `MathTex(r"\text{arithmetic Hodge standard conjecture}=M4=\text{open}")`; a thin frontier `Line` between the layers. (Use flat stacked rectangles with explicit add-order, NOT overlapping 3D fills, per the avoid-list.)
- (c) `Create(matrix_grid)`; `FadeIn(perfect)` (opaque) then `FadeIn(positivity)` (fogged); `Create(frontier_line)`; `Write` both tags.
- (d) about 10 s.
- (e) Caption: "Two layers over one pairing matrix. The bottom is PERFECTNESS (solid, free, even D-H has it, and it is in Mathlib as riemannZeta one sub). The top is the POSITIVITY sign-pattern (fogged: the arithmetic Hodge standard conjecture, M4, open). The boundary is the frontier."
- (f) Column VISIBLE: "perfectness (Mathlib)". Column INVISIBLE: reinforce the master entry (`Indicate`).

Beat C5. The function-field Rosetta: circle straightens into the line.
- (a) The shadow where the move is a theorem.
- (b) `circle` = `Circle(radius=r)` at origin with `Dot`s on it (eigenvalues `|alpha|=sqrt(q)`); target `line` = a vertical `Line` at sigma=0.5 with beads; `ghost_polarization` = `DashedLine` (`C_INVISIBLE`, low opacity); `MathTex(r"\text{genus 1 Gram } \begin{pmatrix}2 & t\\ t & 2q\end{pmatrix} \text{ PD} \iff |t|<2\sqrt{q}")`.
- (c) `Create(circle)` plus dots; then unroll the circle into the line with a `Homotopy` (or `UpdateFromAlphaFunc` on a `ParametricFunction` whose parametrization interpolates from a circle to a vertical segment over the run), so each point traces a path and the curve opens rather than tearing. The dots ride along via the same alpha. If a clean Homotopy proves fiddly, fall back to `ReplacementTransform(circle, line)` with the dots `ReplacementTransform`-ed in parallel and a caption that says the circle straightens. Do NOT use `ApplyPointwiseFunction` (a single fixed point-to-point map cannot open a closed curve into an open segment). Then `Create(ghost_polarization)` and fade it to low opacity over the "Spec(Z)" side; `Write` the Gram-matrix label.
- (d) about 13 s.
- (e) Caption: "Over a curve mod q the Weil-Rosati polarization (degree at least 0, Hodge index on C times C) forces the size of alpha to equal the square root of q. The zeros sit on a circle. The genus-1 Gram matrix [[2, t], [t, 2q]] is positive definite exactly when the absolute value of t is below 2 root q. Over Spec(Z) the circle straightens into the line Re = 1/2, and the polarization becomes a dashed ghost (no usable Spec(Z) times Spec(Z), no carrier variety). Faithful at genus 1, it dissolves over Z."
- (f) Column VISIBLE: "the function-field circle (a theorem)". Column INVISIBLE: "the carrier over Spec(Z) (dashed ghost)".

Beat C6. The D-H impostor: one bead leaves the line, one eigenvalue flips.
- (a) The load-bearing counterexample.
- (b) Reuse `make_bead_wire`: most beads on sigma=0.5 (`C_REALIZATION`); one D-H bead moves to `c2p(0.8085, 85.699_scaled)` (`C_DH`) with its partner at sigma `0.1915`; a `Brace`/`Line` labeled `MathTex(r"|1-2\beta|=0.617")` (consistent: beta = 0.8085 gives 0.617, partner 0.1915); one eigenvalue `Bar` (from B5's pattern) flipping below-to-above zero (`C_REALIZATION` to `C_DH`, via `.animate.set_color` plus a height change); a connecting `Arrow` tying the move to the flip; the stealth caption.
- (c) Place the on-line beads; `dot.animate.move_to(...)` for the impostor plus partner; `Create(brace)` plus label; simultaneous `bar.animate` flip; `Create(connector_arrow)` so the move and the flip read as one event.
- (d) about 12 s.
- (e) Caption: "Zeta zeros all sit on the line. D-H has the same free pairing but an off-line zero at 0.8085 plus 85.7 i (partner 0.1915 plus 85.7 i), displaced by the absolute value of 1 minus 2 beta, which is 0.617. That displacement is one eigenvalue flipping from below 0 to above 0: the signature is broken. Stealth window: the defect is about 2.6 percent of the spectrum and surfaces only at astronomical resolution (height 85.7 needs primes up to e to the 85.7, about 1.6 times 10 to the 37), so soft and numerical methods are blind."
- (f) Column VISIBLE: "the D-H impostor (off-line zero)".

Beat C7. The marginal-positivity razor.
- (a) No slack.
- (b) Three short `MathTex`/`Text` lines; a thin `NumberLine` near zero with a tick at `Lambda=0`.
- (c) `Write` each line in sequence; `Indicate` the `Lambda=0` tick.
- (d) about 8 s.
- (e) Caption: "Weil cancellation leaves a residue about 1 in 1000 of two huge opposing terms. D-H fails Weil positivity by about 78.7 percent per off-line direction, and unconditional bounds are 30 to 120 times too wide. de Bruijn-Newman: Lambda at most 0 is equivalent to RH, and Rodgers-Tao (2018) proved Lambda at least 0, so RH sits on the knife edge Lambda equals 0, with no slack. A compass, not a wall."
- (f) Column VISIBLE: "the marginal-positivity razor".

Beat C8. The hall of machines and the three near-miss gears.
- (a) The hall.
- (b) `make_machine_icon()` copied 7 times in a row, labeled "Deninger", "Connes-Consani", "prismatic / WCart", "Hesselholt THH/TC", "Arakelov / Faltings-Hriljac", "F_1", "AHK"; each emits the same vertical strip of zero-dots and carries the IDENTICAL `make_gear_socket()` empty `Annulus`; three near-miss gears beside one socket: `gear_FH`, `gear_AHK`, `gear_deBranges`, each attempting to seat and bouncing back, marked with a red `Cross` sized to the gear (`Cross(gear, stroke_color=RED)` or `Cross().scale_to_fit_width(gear.width)`, not a bare unit `Cross`).
- (c) `LaggedStartMap(FadeIn, machines, lag_ratio=0.3)`; `Indicate` all the empty sockets together (they are the same); `Transform` each near-miss gear toward a socket then `.animate` it back out (a bounce) with a `Cross` plus a verdict label.
- (d) about 16 s.
- (e) Caption: "A hall of machines (Deninger, Connes-Consani, prismatic / WCart, Hesselholt THH/TC, Arakelov / Faltings-Hriljac, F_1, AHK). All emit the same zeros. All have the identical empty socket. Three proven near-miss gears bracket the gap: Faltings-Hriljac (too local), AHK (too blind, trace-free), de Branges (too strong, it implies GRH and is refuted at the 34th zero)."
- (f) Column INVISIBLE: "the one missing polarization (global, indefinite (1, n-1), arithmetic-trace-carrying, RH-equivalent, non-circular)".

---

### CLOSE: collapse to the master image. Class: Close_MasterImage(Scene)

Beat D1. Assemble the three stage end-states.
- (a) The final master image.
- (b) Reduced reusable `VGroup`s: `hall_small` (from a `make_machine_icon` row), `funnel_small` (from `make_road`/neck), `socket_big` (from `make_gear_socket`); a small saddle thumbnail or just `MathTex(r"(1,\,n-1)")` stamped into the socket; the full `tracker` brought to center.
- (c) `ReplacementTransform` the three stage end-states into their slots on one frame; an `AnimationGroup` with lag to assemble; `Write` the `(1,n-1)` stamp INTO the socket (the socket stays an empty annulus, only annotated); hold.
- (d) about 14 s.
- (e) Caption: "One hall. One funnel-neck. One empty gear-shaped socket, stamped with the (1, n-1) saddle signature."
- (f) Both columns brought to center, side by side.

Beat D2. The single invisible object.
- (a) The unifying line.
- (b) `Text` lines.
- (c) `Write` in sequence; `Indicate` the three INVISIBLE-column entries from A, B, C together to show they were one object.
- (d) about 12 s.
- (e) Caption: "All three stages share one invisible object: the missing polarization over Spec(Z) (M4, the arithmetic Hodge standard conjecture). Every candidate cohomology supplies the trace and the free pairing. None supplies this. Supplying it is RH."
- (f) Column INVISIBLE: collapse the A, B, C entries into the single master entry.

Beat D3. Closing stance (directional, not fatalistic).
- (a) Close.
- (b) `Text("A compass, not a wall.", color=C_CRITLINE)`; `Text("Each dead branch is a coordinate. The target is narrowed, not abandoned.", color=C_VISIBLE)`.
- (c) `Write` both; hold 3 s; `FadeOut` all.
- (d) about 6 s.
- (e) Caption (the two lines above are the caption): "A compass, not a wall." / "Each dead branch is a coordinate. The target is narrowed, not abandoned."
- (f) Final hold.

---

## 4. REUSE NOTES

### Helper functions to extract (module top, above the Scene classes)

| Helper | Signature | Returns | Used by |
|---|---|---|---|
| `eta_approx(s, N=80)` | copy verbatim from scene 09 | `complex` | terrain height only (A2) |
| `zeta_approx(s, N=80)` | copy verbatim from scene 09 (pole-capped at complex(10,0)) | `complex` | terrain height only (A2) |
| `KNOWN_ZEROS_T` | copy verbatim from scene 07 (list of 10) | `list[float]` | A2, A5, A6 (heights), C6 |
| `make_master_thumb(highlight)` | `highlight in {"machines","funnel","socket"}` | `VGroup` (P1) | every stage |
| `make_tracker()` | none | `VGroup` (two columns plus headers) (P2) | every stage |
| `add_to_visible(scene, tracker, text)` / `add_to_invisible(scene, tracker, text)` | append plus `FadeIn` a bullet | `None` | every beat |
| `make_bead_wire(axes, heights, color, sigma=0.5)` | wire `Line` plus `VGroup` of bead `Dot`s | `(Line, VGroup)` | A5, C6 |
| `make_machine_icon(label)` | `RoundedRectangle` body plus prime-feed plus emitted zero strip plus `make_gear_socket()` | `VGroup` | C8, Close |
| `make_gear_socket(color=C_INVISIBLE)` | empty `Annulus` (cheap gear stand-in, NOT involute teeth) | `Mobject` | C8, Close |
| `make_road(start, neck, label, ...)` | tapering two-segment `VMobject` (green left half, red right half) | `VGroup` | B2, B3, Close |

`make_machine_icon` should build the template ONCE and `.copy()` across the seven labels (per the global tip on pre-rendering and copying heavy Mobjects). `make_gear_socket` returns an `Annulus` (or an 8-to-12-notch polygon at most), never a true involute gear (avoid-list).

The A6 wave curve is NOT a helper that calls `zeta_approx`/`eta_approx`. It precomputes, on a numpy array `x`, the schematic envelope `sum_{j} np.sqrt(x) * np.cos(t_j * np.log(x))` for the first three heights `t_1, t_2, t_3` from `KNOWN_ZEROS_T`, and builds three static `VMobject` curves outside any updater. The displayed formula `\pi(x)=\mathrm{Li}(x)-\sum_\rho \mathrm{Li}(x^\rho)-\cdots` stays exact; the curve is illustrative.

### Beats that are good standalone Scenes for quick iteration

Author each as a tiny throwaway `Scene` subclass during development so the choreography-sensitive beats can be rendered in isolation without the full multi-minute clip:

- A4 (quartet plus on-line collapse) and A5 (bead collapse): the 3D-to-2D handoff and the per-bead `Transform` are the choreography-sensitive parts (rated medium). Render alone first.
- A6 (explicit-formula wave sum): the staged `ReplacementTransform` between three precomputed partial-sum curves needs visual tuning (medium); iterate standalone with the precomputed sample arrays.
- B2 plus B3 (road build plus neck merge): the convergence choreography and the left/right split are the main authoring effort (medium); iterate standalone.
- B5 (Level 3 vs Level 4 alarm): stock `BarChart` plus `ValueTracker` plus `Flash` (easy), but worth a standalone to tune the alarm timing.
- C3 (saddle vs bowl, 3D insert): the only 3D in Stage C; render standalone to set the `move_camera` angles before integrating.
- C5 (circle-to-line unroll): the `Homotopy` (medium) needs tuning so it unrolls rather than tears; iterate standalone, and keep the `ReplacementTransform` fallback ready.
- C8 (hall plus near-miss gears): the gear-bounce `Transform` (medium); iterate standalone, then it feeds straight into the Close.

### Substitutions made (feasibility-driven)

- Pole (avoid an uncapped spike): rendered as a separate capped `Cylinder` labeled "residue 1". `zeta_magnitude` is capped at `min(val, 4.0)` and `zeta_approx` already returns a finite complex(10, 0) at the pole, so the real spike never drives `z_range`. The Cylinder is thin so it does not occlude the front drain-holes, and its fixed-frame label sits in a clear corner.
- Gear socket (avoid involute teeth): substituted a plain `Annulus` (or an 8-to-12-notch polygon at most) as the gear-shaped socket. Far cheaper and reads correctly.
- (1, n-1) signature (cannot render infinite-dim): substituted the 3D saddle `z=x^2-y^2` as an honest schematic ("one up, rest down" arrow gloss) plus the literal `(1, n-1)` label. Stated as a deliberate finite abstraction in the caption.
- Explicit-formula sum (avoid live mpmath in updaters and avoid the always_redraw/Transform conflict): substituted three precomputed `np.sqrt(x) * np.cos(t * np.log(x))` partial-sum curves advanced by `ReplacementTransform`, with no `always_redraw`. The displayed formula stays exact; the curve is illustrative.
- Circle-to-line unroll (avoid ApplyPointwiseFunction tearing a closed curve): substituted a `Homotopy` (or `UpdateFromAlphaFunc` on a parametrization that interpolates circle to segment), with a `ReplacementTransform(circle, line)` fallback.
- Transparency layers (avoid 3D z-fighting): substituted flat stacked `Rectangle`s with explicit add-order, not overlapping 3D fills.
- 3D-to-2D handoffs: substituted the flatten-then-handoff recipe (`move_camera(phi=0)`, `FadeOut(Surface)`, then 2D logic). No live 3D Surface coexists with 2D Transforms.

All numerics that must be faithful use the catalogued values, kept internally consistent: bead heights `14.13, 21.02, 25.01, 30.42, 32.94, ...`; D-H off-line zero `0.8085 + 85.699 i` (displayed height rounded to 85.7) with partner `0.1915 + 85.699 i` and displacement `|1 - 2 beta| = 0.617`; e to the 85.7 is about 1.66 times 10 to the 37; density `log(T / 2 pi) / (2 pi)`; Gram `[[2, t], [t, 2q]]` PD iff `|t| < 2 sqrt(q)`; de Bruijn-Newman `Lambda = 0` (Rodgers-Tao 2018 proved Lambda at least 0). Schematic-only by design: the wave sum and the down-axis count. "Level 4 equals positivity" is captioned as a finding (about 80/20), not a theorem. Trivial zeros at -2, -4, -6 are out of frame by choice.
