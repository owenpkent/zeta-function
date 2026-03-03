"""
ZerosOnCriticalLine
===================
Visualizes the first 20 non-trivial zeros of the Riemann zeta function
on the critical line Re(s) = 1/2.

Also shows |zeta(1/2 + it)| as a function of t, with zeros marked.
"""

from manim import *
import numpy as np


# First 20 non-trivial zero imaginary parts (to 6 decimal places)
KNOWN_ZEROS_T = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
    52.970321, 56.446248, 59.347044, 60.831779, 65.112544,
    67.079811, 69.546402, 72.067158, 75.704691, 77.144840,
]


def eta_approx(s, N=500):
    return sum(((-1) ** (n + 1)) / (n**s) for n in range(1, N + 1))


def zeta_on_critical_line(t, N=500):
    """Approximate zeta(1/2 + it) using the eta function."""
    s = complex(0.5, t)
    eta = eta_approx(s, N)
    denom = 1 - 2 ** (1 - s)
    if abs(denom) < 1e-10:
        return complex(0)
    return eta / denom


class ZerosOnCriticalLine(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────────────────
        title = Title(r"Non-Trivial Zeros on the Critical Line $\text{Re}(s) = \frac{1}{2}$")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # ── Part 1: |zeta(1/2 + it)| plot ─────────────────────────────────
        ax = Axes(
            x_range=[0, 80, 10],
            y_range=[0, 4.5, 1],
            x_length=11,
            y_length=4,
            axis_config={"include_numbers": True},
            x_axis_config={"numbers_to_include": [10, 20, 30, 40, 50, 60, 70, 80]},
            y_axis_config={"numbers_to_include": [1, 2, 3, 4]},
        ).shift(UP * 0.5)

        ax_xlabel = ax.get_x_axis_label("t = \\text{Im}(s)")
        ax_ylabel = ax.get_y_axis_label(r"\left|\zeta\!\left(\tfrac{1}{2}+it\right)\right|")

        plot_title = Text("|ζ(1/2 + it)| — zeros are where this touches 0",
                          font_size=24).to_edge(UP, buff=0.3)
        self.play(Write(plot_title), Create(ax), Write(ax_xlabel), Write(ax_ylabel))

        # Compute |zeta(1/2 + it)| at dense t values
        t_vals = np.linspace(0.5, 79.5, 500)
        zeta_mags = []
        for t in t_vals:
            try:
                z = zeta_on_critical_line(t, N=300)
                zeta_mags.append(min(abs(z), 4.4))
            except Exception:
                zeta_mags.append(0)

        # Build the curve
        pts = [ax.c2p(t, v) for t, v in zip(t_vals, zeta_mags) if v is not None]
        curve = VMobject(color=BLUE, stroke_width=2)
        curve.set_points_smoothly(pts)

        self.play(Create(curve), run_time=3)

        # Mark the zeros
        zero_dots = VGroup()
        for t0 in KNOWN_ZEROS_T:
            if t0 <= 80:
                d = Dot(ax.c2p(t0, 0), color=RED, radius=0.07)
                zero_dots.add(d)

        self.play(LaggedStartMap(FadeIn, zero_dots, lag_ratio=0.08), run_time=2)

        # Label a few
        label_indices = [0, 2, 4, 9]
        for i in label_indices:
            t0 = KNOWN_ZEROS_T[i]
            if t0 <= 80:
                lbl = MathTex(rf"\rho_{{{i+1}}}", color=RED).scale(0.42)
                lbl.next_to(ax.c2p(t0, 0), DOWN, buff=0.12)
                self.play(Write(lbl), run_time=0.4)

        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Part 2: Complex plane with zeros plotted ───────────────────────
        plane = ComplexPlane(
            x_range=[-0.2, 1.2, 0.5],
            y_range=[0, 80, 10],
            x_length=5,
            y_length=7.5,
            axis_config={"stroke_width": 1.5},
            background_line_style={"stroke_opacity": 0.25},
        ).shift(LEFT * 1.5)

        re_label = MathTex(r"\text{Re}(s)").scale(0.45).next_to(plane.n2p(complex(1.2, 0)), RIGHT, buff=0.05)
        im_label = MathTex(r"\text{Im}(s)").scale(0.45).next_to(plane.n2p(complex(0, 80)), UP, buff=0.05)
        plane_title = Text("First 20 non-trivial zeros", font_size=26).to_edge(UP)

        crit_line = Line(
            plane.n2p(complex(0.5, 0)),
            plane.n2p(complex(0.5, 80)),
            color=YELLOW, stroke_width=2,
        )
        crit_lbl = MathTex(r"\tfrac{1}{2}", color=YELLOW).scale(0.45)
        crit_lbl.next_to(plane.n2p(complex(0.5, 0)), DOWN, buff=0.1)

        self.play(Write(plane_title), Create(plane), Write(re_label), Write(im_label))
        self.play(Create(crit_line), Write(crit_lbl))

        # All zeros displayed with animation
        all_zero_dots = VGroup()
        all_zero_labels = VGroup()
        for i, t0 in enumerate(KNOWN_ZEROS_T):
            d = Dot(plane.n2p(complex(0.5, t0)), color=RED, radius=0.09)
            lbl = MathTex(
                rf"t \approx {t0:.3f}", color=RED
            ).scale(0.32).next_to(d, RIGHT, buff=0.06)
            all_zero_dots.add(d)
            all_zero_labels.add(lbl)

        self.play(
            LaggedStartMap(FadeIn, all_zero_dots, lag_ratio=0.12),
            LaggedStartMap(Write, all_zero_labels, lag_ratio=0.12),
            run_time=4,
        )
        self.wait(1)

        # Sidebar: count and RH
        sidebar = VGroup(
            Text("All 20 zeros:", font_size=22, color=WHITE),
            MathTex(r"\text{Re}(\rho_n) = \tfrac{1}{2}", color=YELLOW).scale(0.75),
            Text("", font_size=14),
            Text("Verified up to:", font_size=20),
            MathTex(r"t \approx 3 \times 10^{12}", color=GREEN).scale(0.65),
            Text("zeros — all on", font_size=20),
            Text("the critical line.", font_size=20),
            Text("", font_size=14),
            Text("Still no proof", font_size=20, color=RED),
            Text("for ALL zeros.", font_size=20, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_corner(UR, buff=0.35)

        self.play(Write(sidebar))
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Part 3: Grand conclusion ───────────────────────────────────────
        conclusion = VGroup(
            Text("The Riemann Hypothesis", font_size=36, color=YELLOW),
            MathTex(r"\text{All non-trivial zeros } \rho \text{ of } \zeta(s)").scale(0.85),
            MathTex(r"\text{satisfy } \text{Re}(\rho) = \tfrac{1}{2}").scale(0.85),
            Text("", font_size=12),
            Text("Open since 1859.", font_size=28, color=RED),
            Text("$1,000,000 prize. Unsolved.", font_size=26, color=ORANGE),
        ).arrange(DOWN, buff=0.35)

        for mob in conclusion:
            self.play(Write(mob), run_time=0.9)
            self.wait(0.3)
        self.wait(3)
