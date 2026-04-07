# Manim Reference Guide

> Quick reference for [manim Community Edition](https://docs.manim.community/) v0.18+.
> Covers the API surface most relevant to this project.

---

## Table of Contents

1. [Setup & Rendering](#1-setup--rendering)
2. [Scene Structure](#2-scene-structure)
3. [Mobjects (Displayable Objects)](#3-mobjects)
4. [Text & Math](#4-text--math)
5. [Coordinate Systems & Graphing](#5-coordinate-systems--graphing)
6. [Animations](#6-animations)
7. [Transforms](#7-transforms)
8. [ValueTracker & Updaters](#8-valuetracker--updaters)
9. [3D Scenes & Objects](#9-3d-scenes--objects)
10. [Vector Fields](#10-vector-fields)
11. [Colors & Styling](#11-colors--styling)
12. [Layout & Positioning](#12-layout--positioning)
13. [Common Patterns](#13-common-patterns)

---

## 1. Setup & Rendering

### Prerequisites

| Dependency | Install |
|------------|---------|
| Python 3.10+ | python.org |
| manim | `pip install manim` |
| FFmpeg | `winget install Gyan.FFmpeg` / `brew install ffmpeg` |
| LaTeX (MiKTeX or TeX Live) | miktex.org / tug.org/texlive |
| `preview.sty` | `mpm --install=preview` (MiKTeX only) |

### Render commands

```bash
manim -ql  script.py SceneName    # 480p  15fps  (fast preview)
manim -qm  script.py SceneName    # 720p  30fps
manim -qh  script.py SceneName    # 1080p 60fps
manim -qk  script.py SceneName    # 2160p 60fps  (4K)

manim -pql script.py SceneName    # -p = auto-open after render
manim --disable_caching ...       # skip cache (useful for debugging)
```

Output goes to `media/videos/<script>/<quality>/`.

### Minimal scene

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        self.play(Create(circle))
        self.wait(1)
```

---

## 2. Scene Structure

### Scene base methods

```python
self.play(*animations, run_time=1)     # play animations
self.wait(duration=1)                   # pause
self.add(*mobjects)                     # add without animation
self.remove(*mobjects)                  # remove without animation
self.bring_to_front(*mobjects)          # z-ordering
self.bring_to_back(*mobjects)
self.next_section("name")              # mark section boundary
```

### Scene types

| Class | Use |
|-------|-----|
| `Scene` | Standard 2D scene |
| `ThreeDScene` | 3D camera, surfaces, rotation |
| `MovingCameraScene` | Camera zoom/pan in 2D |
| `ZoomedScene` | Split-screen zoom lens |

---

## 3. Mobjects

### Geometry primitives

```python
# Circles & dots
Circle(radius=1, color=RED)
Dot(point=ORIGIN, radius=0.08, color=WHITE)
Dot3D(point=ORIGIN, radius=0.08, color=WHITE)
Ellipse(width=2, height=1)
Annulus(inner_radius=1, outer_radius=2)
Arc(radius=1, start_angle=0, angle=PI/2)

# Lines & arrows
Line(start=LEFT, end=RIGHT, color=WHITE)
DashedLine(start=LEFT, end=RIGHT, dash_length=0.05)
Arrow(start=LEFT, end=RIGHT, buff=0.25, stroke_width=6)
DoubleArrow(start=LEFT, end=RIGHT)
Vector(direction=RIGHT)
CurvedArrow(start_point=LEFT, end_point=RIGHT)

# Polygons
Rectangle(width=4, height=2, color=WHITE)
Square(side_length=2)
RoundedRectangle(width=4, height=2, corner_radius=0.5)
Polygon(*vertices)
Triangle()
RegularPolygon(n=6)
Star(n=5, outer_radius=1)

# Annotations
Brace(mobject, direction=DOWN, buff=0.2)
SurroundingRectangle(mobject, color=YELLOW, buff=0.1, corner_radius=0.1)
BackgroundRectangle(mobject, color=BLACK, fill_opacity=0.75)
Cross(mobject, stroke_color=RED)
Underline(mobject)
```

### Grouping

```python
VGroup(*mobjects)                          # group VMobjects
Group(*mobjects)                           # group any mobjects

group = VGroup(circle, square, triangle)
group.arrange(RIGHT, buff=0.5)             # lay out horizontally
group.arrange(DOWN, aligned_edge=LEFT)     # vertically, left-aligned
group.arrange_in_grid(rows=2, buff=0.3)    # grid layout
```

### Tables

```python
table = MobjectTable(
    [[Text("A"), Text("B")],
     [Text("1"), Text("2")]],
    include_outer_lines=True,
).scale(0.75)

# or
table = Table(
    [["A", "B"], ["1", "2"]],
    col_labels=[Text("X"), Text("Y")],
)
```

---

## 4. Text & Math

### LaTeX math

```python
MathTex(r"\int_0^1 f(x)\,dx")                           # single expression
MathTex(r"a^2", "+", r"b^2", "=", r"c^2")               # isolate parts
MathTex(r"E = mc^2", tex_to_color_map={"E": YELLOW})     # auto-color

tex = MathTex(r"a^2", "+", r"b^2")
tex.get_part_by_tex("a^2").set_color(RED)                 # color specific part
tex.set_color_by_tex("b^2", BLUE)
```

### Text

```python
Text("Hello", font_size=36, color=WHITE)
Text("Hello", font="Courier New", slant=ITALIC, weight=BOLD)

# Multi-line
Text("Line 1\nLine 2", line_spacing=1.2)
```

### Titles & lists

```python
Title(r"My Title with $\LaTeX$")
Title("Plain Title", include_underline=True)

BulletedList("Item 1", "Item 2", "Item 3", buff=0.4)
```

### Key `MathTex` / `Tex` params

| Param | Default | Purpose |
|-------|---------|---------|
| `font_size` | `48` | Font size |
| `color` | `WHITE` | Text color |
| `tex_to_color_map` | `{}` | Auto-color specific substrings |
| `tex_environment` | `"align*"` / `"center"` | LaTeX environment wrapper |
| `substrings_to_isolate` | `None` | Force splitting at given strings |

---

## 5. Coordinate Systems & Graphing

### Axes (2D)

```python
axes = Axes(
    x_range=[-3, 3, 1],          # [min, max, step]
    y_range=[-2, 2, 0.5],
    x_length=8,                   # screen units
    y_length=5,
    axis_config={"include_numbers": True, "stroke_width": 1.5},
    x_axis_config={"numbers_to_include": [-2, 0, 2]},
    tips=True,                    # arrow tips
)

# Plot a function
graph = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[-3, 3])
label = axes.get_graph_label(graph, label="\\sin(x)", x_val=2)

# Axes labels
x_label = axes.get_x_axis_label("x")
y_label = axes.get_y_axis_label("f(x)")

# Coordinate conversion
point = axes.c2p(1, 2)           # coords → screen position
x, y = axes.p2c(point)           # screen position → coords

# Useful extras
area = axes.get_area(graph, x_range=[0, 2], color=BLUE, opacity=0.3)
v_line = axes.get_vertical_line(axes.c2p(1, np.sin(1)))
h_line = axes.get_horizontal_line(axes.c2p(1, np.sin(1)))
riemann = axes.get_riemann_rectangles(graph, x_range=[0, 2], dx=0.2)
```

### NumberPlane

```python
plane = NumberPlane(
    x_range=[-5, 5, 1],
    y_range=[-3, 3, 1],
    background_line_style={"stroke_color": BLUE_D, "stroke_opacity": 0.5},
)
```

### ComplexPlane

```python
plane = ComplexPlane(
    x_range=[-3, 3, 1],
    y_range=[-3, 3, 1],
)
point = plane.n2p(complex(1, 2))    # complex number → screen position
z = plane.p2n(point)                 # screen position → complex number
plane.add_coordinates()              # show coordinate labels
```

### ParametricFunction

```python
# 2D parametric curve
curve = ParametricFunction(
    lambda t: np.array([np.cos(t), np.sin(t), 0]),
    t_range=[0, TAU],
    color=YELLOW,
)

# In axes coordinates
curve = axes.plot_parametric_curve(
    lambda t: [np.cos(t), np.sin(t)],
    t_range=[0, TAU],
)
```

### PolarPlane

```python
polar = PolarPlane(radius_max=3, azimuth_step=12)
graph = polar.plot(lambda theta: 1 + np.cos(theta), color=BLUE)
```

---

## 6. Animations

### Creating / removing objects

```python
self.play(Create(mobject))                   # draw incrementally
self.play(Uncreate(mobject))                 # reverse of Create
self.play(Write(tex))                        # hand-writing effect
self.play(Unwrite(tex))                      # erase
self.play(DrawBorderThenFill(mobject))       # outline then fill
self.play(FadeIn(mobject))                   # fade in
self.play(FadeIn(mobject, shift=UP))         # fade in from below
self.play(FadeOut(mobject))                  # fade out
self.play(GrowFromCenter(mobject))           # grow from center
self.play(GrowArrow(arrow))                 # grow arrow tip-ward
self.play(SpinInFromNothing(mobject))        # spin + grow
self.play(SpiralIn(group))                   # spiral trajectory

# Letter by letter
self.play(AddTextLetterByLetter(text, time_per_char=0.05))
```

### Sequencing

```python
# Simultaneous
self.play(Create(a), Write(b), FadeIn(c))

# Staggered
self.play(LaggedStartMap(FadeIn, group, lag_ratio=0.15), run_time=2)
self.play(LaggedStart(*[Write(m) for m in group], lag_ratio=0.2))

# Sequential within one play call
self.play(Succession(Create(a), Write(b), FadeIn(c)))
self.play(AnimationGroup(Create(a), Write(b), lag_ratio=0.5))
```

### Indicating

```python
self.play(Indicate(mobject, scale_factor=1.2, color=YELLOW))
self.play(Circumscribe(mobject, color=RED))
self.play(Flash(point, color=YELLOW))
self.play(FocusOn(point))
self.play(ApplyWave(mobject))
self.play(Wiggle(mobject))
self.play(ShowPassingFlash(mobject.copy(), time_width=0.3))
```

### Movement

```python
self.play(MoveAlongPath(dot, curve), run_time=3)
```

### Animation parameters

```python
self.play(
    Create(circle),
    run_time=2,                     # duration in seconds
    rate_func=smooth,               # easing function
)
```

**Rate functions:** `linear`, `smooth`, `rush_into`, `rush_from`,
`slow_into`, `there_and_back`, `there_and_back_with_pause`,
`wiggle`, `double_smooth`, `ease_in_sine`, `ease_out_sine`, etc.

---

## 7. Transforms

### Morphing one object into another

```python
# Transform: source becomes target (source stays in scene, changes appearance)
self.play(Transform(source, target))

# ReplacementTransform: source is removed, target is added
self.play(ReplacementTransform(source, target))

# TransformFromCopy: source stays unchanged, a copy becomes target
self.play(TransformFromCopy(source, target))

# FadeTransform: cross-fade between two mobjects
self.play(FadeTransform(old, new))

# FadeTransformPieces: cross-fade submobjects piecewise
self.play(FadeTransformPieces(old_group, new_group))
```

### Applying functions

```python
self.play(ApplyFunction(lambda m: m.scale(2).rotate(PI/4), mobject))
self.play(ApplyMatrix([[2, 1], [0, 1]], mobject))
self.play(ApplyComplexFunction(lambda z: z**2, plane))
self.play(ApplyPointwiseFunction(lambda p: [p[0]**2, p[1], 0], mobject))
```

### The `.animate` syntax

```python
# Any mobject method can be animated:
self.play(circle.animate.shift(RIGHT * 2))
self.play(circle.animate.set_color(RED).scale(2))
self.play(circle.animate.move_to(UP * 2).rotate(PI/4))

# Chaining works:
self.play(
    square.animate.shift(LEFT).set_color(BLUE),
    circle.animate.shift(RIGHT).scale(0.5),
)
```

### Save / restore

```python
mobject.save_state()
self.play(mobject.animate.shift(UP).set_color(RED))
self.wait(1)
self.play(Restore(mobject))    # back to saved state
```

---

## 8. ValueTracker & Updaters

### ValueTracker

A non-visible mobject that holds a number. Animate it to drive other objects.

```python
t = ValueTracker(0)

# Create a dot that follows the tracker
dot = always_redraw(
    lambda: Dot(axes.c2p(t.get_value(), np.sin(t.get_value())), color=RED)
)
self.add(dot)
self.play(t.animate.set_value(2 * PI), run_time=4)
```

### ComplexValueTracker

```python
z = ComplexValueTracker(complex(1, 0))
self.play(z.animate.set_value(complex(0, 1)), run_time=2)
```

### Updaters

```python
# Lambda updater: called every frame
mob.add_updater(lambda m: m.next_to(other_mob, RIGHT))

# always_redraw: recreate the mobject every frame
label = always_redraw(
    lambda: MathTex(f"x = {t.get_value():.2f}").next_to(dot, UP)
)
self.add(label)

# Remove updater
mob.clear_updaters()
mob.remove_updater(specific_func)

# Temporarily suspend
mob.suspend_updating()
mob.resume_updating()
```

### DecimalNumber (live-updating number display)

```python
num = DecimalNumber(0, num_decimal_places=2, font_size=36)
num.add_updater(lambda m: m.set_value(t.get_value()))
self.add(num)
self.play(t.animate.set_value(10), run_time=3)
```

---

## 9. 3D Scenes & Objects

### ThreeDScene

```python
class My3D(ThreeDScene):
    def construct(self):
        # Camera setup
        self.set_camera_orientation(
            phi=75 * DEGREES,     # vertical angle (0=top-down, 90=side)
            theta=-45 * DEGREES,  # horizontal angle
            zoom=0.8,
        )

        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-2, 2, 1],
        )
        self.add(axes)

        # Move camera
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=2)

        # Auto-rotate
        self.begin_ambient_camera_rotation(rate=0.1)   # radians/sec
        self.wait(5)
        self.stop_ambient_camera_rotation()

        # Fixed-in-frame overlays (2D text on top of 3D)
        label = Text("Hello").to_corner(UL)
        self.add_fixed_in_frame_mobjects(label)
```

### 3D objects

```python
# Surfaces
surface = Surface(
    lambda u, v: axes.c2p(u, v, np.sin(u) * np.cos(v)),
    u_range=[-PI, PI],
    v_range=[-PI, PI],
    resolution=(30, 30),        # (u_steps, v_steps)
    fill_opacity=0.7,
)
surface.set_fill_by_value(
    axes=axes,
    colorscale=[(BLUE, -1), (GREEN, 0), (RED, 1)],
    axis=2,    # color by z-value
)

# Primitives
Sphere(radius=1, resolution=(20, 20))
Cube(side_length=2)
Cylinder(radius=1, height=2, direction=OUT)
Cone(base_radius=1, height=2)
Torus(major_radius=2, minor_radius=0.5)
Prism(dimensions=[3, 2, 1])
Line3D(start=ORIGIN, end=[1, 1, 1], thickness=0.02)
Arrow3D(start=ORIGIN, end=[1, 1, 1])
Dot3D(point=ORIGIN, radius=0.08)
```

---

## 10. Vector Fields

### Static arrow field

```python
field = ArrowVectorField(
    lambda p: np.array([-p[1], p[0], 0]),     # rotation field
    x_range=[-3, 3],
    y_range=[-3, 3],
    length_func=lambda norm: 0.4 * sigmoid(norm),
)
self.add(field)
```

### Animated stream lines

```python
stream = StreamLines(
    lambda p: np.array([-p[1], p[0], 0]),
    x_range=[-3, 3],
    y_range=[-3, 3],
    stroke_width=2,
    virtual_time=3,
    max_anchors_per_line=100,
)
self.add(stream)
stream.start_animation(warm_up=True, flow_speed=1.5)
self.wait(4)
stream.end_animation()
```

### 3D vector fields

```python
field = ArrowVectorField(
    lambda p: np.array([p[1], -p[0], p[2]]),
    three_dimensions=True,
    x_range=[-2, 2, 1],
    y_range=[-2, 2, 1],
    z_range=[-2, 2, 1],
)
```

---

## 11. Colors & Styling

### Built-in colors

```
WHITE  GREY_A  GREY_B  GREY_C  GREY_D  GREY_E  BLACK
RED    RED_A   RED_B   RED_C   RED_D   RED_E
BLUE   BLUE_A  BLUE_B  BLUE_C  BLUE_D  BLUE_E
GREEN  GREEN_A GREEN_B GREEN_C GREEN_D GREEN_E
YELLOW GOLD    ORANGE  PINK    PURPLE  TEAL    MAROON
```

### Styling VMobjects

```python
mob.set_color(RED)
mob.set_fill(BLUE, opacity=0.5)
mob.set_stroke(WHITE, width=2, opacity=1)

# Gradient
mob.set_color_by_gradient(RED, YELLOW, GREEN)

# Per-submobject coloring
mob.set_submobject_colors_by_gradient(BLUE, RED)
```

---

## 12. Layout & Positioning

### Directions

```
UL  UP  UR          np.array([-1, 1, 0]) etc.
LEFT ORIGIN RIGHT
DL DOWN DR
```

### Positioning methods

```python
mob.move_to(ORIGIN)                          # center at point
mob.move_to(other_mob)                       # center at other's center
mob.next_to(other, RIGHT, buff=0.25)         # place adjacent
mob.to_edge(UP, buff=0.5)                    # against screen edge
mob.to_corner(UR, buff=0.5)                  # against screen corner
mob.align_to(other, UP)                      # align tops
mob.shift(RIGHT * 2 + UP * 0.5)             # relative shift
mob.center()                                 # center on screen
```

### Arrangement

```python
group.arrange(RIGHT, buff=0.5)                        # horizontal
group.arrange(DOWN, buff=0.3, aligned_edge=LEFT)       # vertical, left-aligned
group.arrange_in_grid(rows=2, cols=3, buff=0.5)        # grid
group.arrange_submobjects(RIGHT)                       # just submobjects
```

### Bounding box queries

```python
mob.get_center()
mob.get_top()    mob.get_bottom()
mob.get_left()   mob.get_right()
mob.get_corner(UR)
mob.get_width()  mob.get_height()
```

---

## 13. Common Patterns

### Fade out everything

```python
self.play(*[FadeOut(m) for m in self.mobjects])
```

### Live-updating graph point

```python
t = ValueTracker(0)
axes = Axes(x_range=[0, 5], y_range=[-1, 1])
graph = axes.plot(np.sin, color=BLUE)
dot = always_redraw(lambda: Dot(
    axes.c2p(t.get_value(), np.sin(t.get_value())), color=RED
))
v_line = always_redraw(lambda: axes.get_vertical_line(
    axes.c2p(t.get_value(), np.sin(t.get_value())), color=YELLOW
))
self.add(axes, graph, dot, v_line)
self.play(t.animate.set_value(5), run_time=4)
```

### Build up an equation step by step

```python
eq1 = MathTex(r"e^{i\pi}")
eq2 = MathTex(r"e^{i\pi}", "=", "-1")
eq3 = MathTex(r"e^{i\pi}", "+", "1", "=", "0")

self.play(Write(eq1))
self.play(TransformMatchingTex(eq1, eq2))
self.play(TransformMatchingTex(eq2, eq3))
```

### Animated counter

```python
counter = Integer(0, font_size=72)
self.play(ChangeDecimalToValue(counter, 100), run_time=3)
```

### Camera zoom (MovingCameraScene)

```python
class ZoomScene(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=4).move_to(target))
        self.wait()
        self.play(Restore(self.camera.frame))
```

### Successive transforms on a single object

```python
# IMPORTANT: after Transform(a, b), reference `a` — not `b`
self.play(Transform(a, b))    # a now looks like b
self.play(Transform(a, c))    # a now looks like c
# `b` and `c` are never added to the scene
```

---

## Further Reading

- [Full API reference](https://docs.manim.community/en/stable/reference.html)
- [Tutorials](https://docs.manim.community/en/stable/tutorials.html)
- [Example gallery](https://docs.manim.community/en/stable/examples.html)
- [FAQ](https://docs.manim.community/en/stable/faq.html)
