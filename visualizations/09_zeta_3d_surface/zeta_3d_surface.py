"""
Zeta3DSurface
=============
Visualizes |ζ(s)| as a 3D surface over the complex plane.
Zeros appear as points where the surface touches the floor.
The critical line is highlighted as a ridge/valley path.
"""

from manim import *
import numpy as np


def eta_approx(s, N=80):
    """Dirichlet eta function approximation (converges for Re(s) > 0)."""
    total = complex(0, 0)
    for n in range(1, N + 1):
        total += ((-1) ** (n + 1)) / (n ** s)
    return total


def zeta_approx(s, N=80):
    """Approximate ζ(s) via η(s) / (1 - 2^{1-s})."""
    if abs(s - 1) < 0.05:
        return complex(10, 0)  # pole
    eta = eta_approx(s, N)
    denom = 1 - 2 ** (1 - s)
    if abs(denom) < 1e-10:
        return complex(10, 0)
    return eta / denom


class Zeta3DSurface(ThreeDScene):
    def construct(self):
        # ── Title (2D overlay) ─────────────────────────────────────────────
        title = Title(r"$|\zeta(s)|$ as a 3D Surface")
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.remove(title)

        # ── Set up 3D camera ──────────────────────────────────────────────
        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.7,
        )

        # ── 3D Axes ───────────────────────────────────────────────────────
        axes = ThreeDAxes(
            x_range=[-0.5, 1.5, 0.5],
            y_range=[0, 35, 5],
            z_range=[0, 4, 1],
            x_length=6,
            y_length=8,
            z_length=4,
        )

        x_label = axes.get_x_axis_label(r"\sigma")
        y_label = axes.get_y_axis_label(r"t")
        z_label = axes.get_z_axis_label(r"|\zeta|")

        self.play(Create(axes), Write(x_label), Write(y_label), Write(z_label))

        # ── Build the surface ──────────────────────────────────────────────
        # σ from -0.3 to 1.4, t from 1 to 34
        sigma_range = np.linspace(-0.3, 1.4, 60)
        t_range = np.linspace(1, 34, 100)

        def zeta_magnitude(sigma, t):
            s = complex(sigma, t)
            try:
                val = abs(zeta_approx(s, N=60))
                return min(val, 4.0)  # cap for visualization
            except Exception:
                return 0

        surface = Surface(
            lambda u, v: axes.c2p(u, v, zeta_magnitude(u, v)),
            u_range=[-0.3, 1.4],
            v_range=[1, 34],
            resolution=(50, 80),
            fill_opacity=0.7,
        )

        # Color by height
        surface.set_fill_by_value(
            axes=axes,
            colorscale=[
                (BLUE_E, 0),
                (BLUE, 0.5),
                (TEAL, 1.0),
                (GREEN, 1.5),
                (YELLOW, 2.5),
                (RED, 4.0),
            ],
            axis=2,
        )

        self.play(Create(surface), run_time=3)
        self.wait(1)

        # ── Highlight the critical line σ = 1/2 ───────────────────────────
        crit_t_vals = np.linspace(1, 34, 200)
        crit_pts = []
        for t in crit_t_vals:
            z = zeta_magnitude(0.5, t)
            crit_pts.append(axes.c2p(0.5, t, z))

        crit_curve = VMobject(color=YELLOW, stroke_width=4)
        crit_curve.set_points_smoothly(crit_pts)

        self.play(Create(crit_curve), run_time=2)

        # ── Label zeros (dips to floor) ────────────────────────────────────
        known_zeros_t = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]
        zero_dots = VGroup()
        for t0 in known_zeros_t:
            d = Dot3D(axes.c2p(0.5, t0, 0), color=RED, radius=0.08)
            zero_dots.add(d)

        self.play(LaggedStartMap(FadeIn, zero_dots, lag_ratio=0.2))

        # ── Annotation (fixed in frame) ────────────────────────────────────
        note = VGroup(
            Text("Zeros = where surface", font_size=18, color=RED),
            Text("touches the floor", font_size=18, color=RED),
            Text("along σ = ½", font_size=18, color=YELLOW),
        ).arrange(DOWN, buff=0.08).to_corner(UL, buff=0.5)
        self.add_fixed_in_frame_mobjects(note)
        self.play(Write(note))

        # ── Rotate camera for dramatic effect ──────────────────────────────
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(6)
        self.stop_ambient_camera_rotation()

        # Zoom into the critical line
        self.move_camera(phi=75 * DEGREES, theta=-30 * DEGREES, zoom=0.9, run_time=2)
        self.wait(2)

        # Side view
        self.move_camera(phi=5 * DEGREES, theta=-90 * DEGREES, zoom=0.8, run_time=2)
        self.wait(2)

        # Back to 3/4 view
        self.move_camera(phi=60 * DEGREES, theta=-50 * DEGREES, zoom=0.7, run_time=2)
        self.wait(2)
