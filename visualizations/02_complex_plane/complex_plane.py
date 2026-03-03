"""
ZetaComplexPlane
================
Shows the Riemann zeta function as a mapping on the complex plane.
Uses domain coloring: hue = argument of zeta(s), brightness = |zeta(s)|.
Also animates the image of a vertical line as it sweeps across the complex plane.
"""

from manim import *
import numpy as np
from scipy.special import zeta as scipy_zeta


def zeta_approx(s, terms=200):
    """Approximate zeta via Dirichlet series (only valid for Re(s) > 1)."""
    result = sum(1 / n**s for n in range(1, terms + 1))
    return result


def zeta_eta(s, terms=500):
    """Eta function: eta(s) = sum (-1)^(n+1) / n^s, valid for Re(s) > 0."""
    result = sum(((-1) ** (n + 1)) / n**s for n in range(1, terms + 1))
    return result


def zeta_continued(s, terms=500):
    """
    Approximate zeta via eta function:
    zeta(s) = eta(s) / (1 - 2^(1-s))  for Re(s) > 0, s != 1
    """
    if abs(s - 1) < 0.01:
        return complex(1e10)  # pole
    eta = zeta_eta(s, terms)
    factor = 1 - 2 ** (1 - s)
    if abs(factor) < 1e-10:
        return complex(1e10)
    return eta / factor


def arg_to_hue(theta):
    """Map argument in (-pi, pi] to hue in [0, 1]."""
    return (theta / (2 * np.pi)) % 1.0


def hue_to_rgb(h):
    """Simple HSV -> RGB with S=V=1."""
    h = h % 1.0
    i = int(h * 6)
    f = h * 6 - i
    p, q, t_ = 0, 1 - f, f
    opts = [
        (1, t_, p), (q, 1, p), (p, 1, t_),
        (p, q, 1), (t_, p, 1), (1, p, q),
    ]
    r, g, b = opts[i % 6]
    return r, g, b


class ZetaComplexPlane(Scene):
    def construct(self):
        title = Title(r"$\zeta(s)$ on the Complex Plane")
        self.play(Write(title))
        self.wait(1)

        # --- Explain the domain ---
        plane_intro = VGroup(
            MathTex(r"s = \sigma + it \in \mathbb{C}"),
            MathTex(r"\text{Re}(s) = \sigma \quad \text{(horizontal)}"),
            MathTex(r"\text{Im}(s) = t \quad \text{(vertical)}"),
        ).arrange(DOWN, buff=0.4).scale(0.85)
        self.play(Write(plane_intro))
        self.wait(2)
        self.play(FadeOut(plane_intro), FadeOut(title))

        # --- Draw the complex plane ---
        plane = ComplexPlane(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 1],
            x_length=5,
            y_length=6,
            background_line_style={"stroke_opacity": 0.3},
        ).shift(LEFT * 2.5)
        plane_label = Text("s-plane (input)", font_size=22).next_to(plane, UP, buff=0.2)

        output_plane = ComplexPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=5,
            y_length=6,
            background_line_style={"stroke_opacity": 0.3},
        ).shift(RIGHT * 2.8)
        output_label = Text(r"ζ(s)-plane (output)", font_size=22).next_to(output_plane, UP, buff=0.2)

        arrow_label = MathTex(r"\zeta").scale(1.2).move_to(ORIGIN)

        self.play(Create(plane), Write(plane_label), Create(output_plane), Write(output_label))
        self.play(Write(arrow_label))

        # --- Mark the critical line Re(s) = 1/2 ---
        crit_line = DashedLine(
            plane.n2p(0.5 - 4j),
            plane.n2p(0.5 + 4j),
            color=YELLOW, stroke_width=2.5, dash_length=0.15
        )
        crit_label = MathTex(r"\text{Re}(s)=\tfrac{1}{2}", color=YELLOW).scale(0.5)
        crit_label.next_to(plane.n2p(0.5 + 4j), UP, buff=0.1)

        self.play(Create(crit_line), Write(crit_label))
        self.wait(1)

        # --- Animate vertical line sweeping and its image ---
        sigma_tracker = ValueTracker(2.0)

        def get_input_line():
            sigma = sigma_tracker.get_value()
            return Line(
                plane.n2p(complex(sigma, -3.8)),
                plane.n2p(complex(sigma, 3.8)),
                color=BLUE, stroke_width=2
            )

        def get_output_curve():
            sigma = sigma_tracker.get_value()
            ts = np.linspace(-3.8, 3.8, 80)
            points = []
            for t in ts:
                s = complex(sigma, t)
                try:
                    w = zeta_continued(s, terms=300)
                    if abs(w) < 10:
                        points.append(output_plane.n2p(w))
                except Exception:
                    pass
            if len(points) < 2:
                return VMobject()
            curve = VMobject(color=BLUE, stroke_width=2)
            curve.set_points_smoothly(points)
            return curve

        input_line = always_redraw(get_input_line)
        output_curve = always_redraw(get_output_curve)

        sigma_label = always_redraw(
            lambda: MathTex(
                rf"\sigma = {sigma_tracker.get_value():.2f}",
                color=BLUE
            ).scale(0.6).to_corner(DL, buff=0.4)
        )

        self.play(Create(input_line), Create(output_curve), Write(sigma_label))
        self.wait(0.5)

        # Sweep sigma from 2 down to 0.5
        self.play(sigma_tracker.animate.set_value(0.5), run_time=5, rate_func=linear)
        self.wait(1)

        # Highlight that at sigma=0.5, curve passes through origin (at zeros)
        note = Text("Curve passes through 0 at zeros!", font_size=22, color=YELLOW)
        note.to_edge(DOWN, buff=0.3)
        self.play(Write(note))
        self.wait(2)

        self.play(FadeOut(note))

        # Sweep from 0.5 to -0.5 to show continuation
        self.play(sigma_tracker.animate.set_value(-0.5), run_time=3, rate_func=linear)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # --- Final summary ---
        summary = VGroup(
            MathTex(r"\zeta(s) \text{ maps the complex plane to the complex plane}").scale(0.8),
            MathTex(r"\text{Zeros} \leftrightarrow \text{where the image passes through } 0").scale(0.8),
            MathTex(r"\text{All known zeros: } \text{Re}(s) = \tfrac{1}{2}").scale(0.8).set_color(YELLOW),
        ).arrange(DOWN, buff=0.5)
        for line in summary:
            self.play(Write(line), run_time=1)
            self.wait(0.5)
        self.wait(2)
