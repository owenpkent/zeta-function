"""
Lorenz Attractor
================
The canonical strange attractor, rendered in 3D. Two scenes:

  LorenzAttractor : the butterfly traced out as a single colored trajectory,
                    with an ambient camera orbit (the hero shot).
  ButterflyEffect : two trajectories from almost-identical starts, drawn
                    together so their exponential divergence is visible. This
                    is sensitive dependence on initial conditions made literal.

The Lorenz system (1963), from truncated Rayleigh-Benard convection:

    dx/dt = sigma (y - x)
    dy/dt = x (rho - z) - y
    dz/dt = x y - beta z

with the classic parameters sigma = 10, rho = 28, beta = 8/3, which sit
firmly in the chaotic regime (largest Lyapunov exponent ~ 0.906).

Render:
    manim -pqh lorenz_attractor.py LorenzAttractor
    manim -pqh lorenz_attractor.py ButterflyEffect
"""

from manim import *
import numpy as np


# --- Lorenz vector field and integrator --------------------------------------

SIGMA, RHO, BETA = 10.0, 28.0, 8.0 / 3.0


def lorenz_deriv(state):
    x, y, z = state
    return np.array([
        SIGMA * (y - x),
        x * (RHO - z) - y,
        x * y - BETA * z,
    ])


def integrate_lorenz(start, dt=0.005, steps=6000):
    """RK4 integration of the Lorenz system, returns an (steps+1, 3) array."""
    pts = np.empty((steps + 1, 3))
    pts[0] = start
    s = np.array(start, dtype=float)
    for i in range(steps):
        k1 = lorenz_deriv(s)
        k2 = lorenz_deriv(s + 0.5 * dt * k1)
        k3 = lorenz_deriv(s + 0.5 * dt * k2)
        k4 = lorenz_deriv(s + dt * k3)
        s = s + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        pts[i + 1] = s
    return pts


def make_axes():
    """Axes sized to hold the classic attractor (x,y in +/-30, z in [0,55])."""
    return ThreeDAxes(
        x_range=[-30, 30, 10],
        y_range=[-30, 30, 10],
        z_range=[0, 55, 10],
        x_length=7,
        y_length=7,
        z_length=5,
    )


class LorenzAttractor(ThreeDScene):
    def construct(self):
        title = Title(r"The Lorenz Attractor")
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))
        self.remove(title)

        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES, zoom=0.75)

        axes = make_axes()
        x_label = axes.get_x_axis_label(r"x")
        y_label = axes.get_y_axis_label(r"y")
        z_label = axes.get_z_axis_label(r"z")
        self.play(Create(axes), Write(x_label), Write(y_label), Write(z_label))

        # Integrate and build the trajectory as a color-graded curve.
        pts = integrate_lorenz([1.0, 1.0, 1.0], dt=0.005, steps=6000)
        curve_pts = [axes.c2p(*p) for p in pts]

        traj = VMobject()
        traj.set_points_as_corners(curve_pts)
        traj.set_stroke(width=2.0, opacity=0.9)
        # Color by progression along the orbit: cool at the start, hot at the end.
        traj.set_color_by_gradient(BLUE_E, TEAL, GREEN, YELLOW, RED)

        # Draw it as if being traced out in real time.
        self.play(Create(traj), run_time=8, rate_func=linear)
        self.wait(0.5)

        note = VGroup(
            Text("One trajectory, never repeating.", font_size=20, color=WHITE),
            Text("Bounded, deterministic, chaotic.", font_size=20, color=YELLOW),
        ).arrange(DOWN, buff=0.12).to_corner(UL, buff=0.5)
        self.add_fixed_in_frame_mobjects(note)
        self.play(Write(note))

        # Hero orbit.
        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(9)
        self.stop_ambient_camera_rotation()

        # Look down the two lobes, then back to three-quarter.
        self.move_camera(phi=15 * DEGREES, theta=-90 * DEGREES, zoom=0.8, run_time=2)
        self.wait(1.5)
        self.move_camera(phi=70 * DEGREES, theta=-40 * DEGREES, zoom=0.75, run_time=2)
        self.wait(1.5)


class ButterflyEffect(ThreeDScene):
    def construct(self):
        title = Title(r"Sensitive Dependence: the Butterfly Effect")
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))
        self.remove(title)

        self.set_camera_orientation(phi=70 * DEGREES, theta=-55 * DEGREES, zoom=0.75)
        axes = make_axes()
        self.play(Create(axes))

        # Two starts separated by one part in a million.
        start_a = np.array([1.0, 1.0, 1.0])
        start_b = start_a + np.array([1e-6, 0.0, 0.0])
        pts_a = integrate_lorenz(start_a, dt=0.005, steps=6000)
        pts_b = integrate_lorenz(start_b, dt=0.005, steps=6000)

        curve_a = VMobject().set_points_as_corners([axes.c2p(*p) for p in pts_a])
        curve_b = VMobject().set_points_as_corners([axes.c2p(*p) for p in pts_b])
        curve_a.set_stroke(color=TEAL, width=2.0, opacity=0.9)
        curve_b.set_stroke(color=RED, width=2.0, opacity=0.9)

        caption = VGroup(
            Text("Two starts, 0.000001 apart.", font_size=20, color=WHITE),
            Text("They track together, then split.", font_size=20, color=RED),
        ).arrange(DOWN, buff=0.12).to_corner(UL, buff=0.5)
        self.add_fixed_in_frame_mobjects(caption)

        # Trace both at once so the moment of divergence reads on screen.
        self.play(Write(caption))
        self.play(Create(curve_a), Create(curve_b), run_time=9, rate_func=linear)
        self.wait(0.5)

        self.begin_ambient_camera_rotation(rate=0.16)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.wait(1)
