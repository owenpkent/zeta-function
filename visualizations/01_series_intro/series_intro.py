"""
ZetaSeriesIntro
===============
Visualizes the partial sums of the Dirichlet series:
    zeta(s) = sum_{n=1}^{N} 1/n^s
for real s, showing convergence for s > 1 and divergence for s = 1.
"""

from manim import *
import numpy as np


def partial_sum(s, N):
    return sum(1 / n**s for n in range(1, N + 1))


class ZetaSeriesIntro(Scene):
    def construct(self):
        # Title
        title = Title(r"The Riemann Zeta Function: $\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$")
        self.play(Write(title))
        self.wait(1)

        # --- Part 1: Show the series definition ---
        series_def = MathTex(
            r"\zeta(s)",
            r"= \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \cdots",
        ).scale(0.9).move_to(ORIGIN)
        self.play(Write(series_def))
        self.wait(1.5)

        # Highlight special case s=2
        s2_label = MathTex(r"s = 2:").scale(0.85).shift(LEFT * 3 + DOWN * 1.5)
        s2_val = MathTex(
            r"\zeta(2) = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots = \frac{\pi^2}{6}"
        ).scale(0.8).shift(RIGHT * 0.5 + DOWN * 1.5)
        self.play(FadeIn(s2_label), Write(s2_val))
        self.wait(2)
        self.play(FadeOut(s2_label), FadeOut(s2_val), FadeOut(series_def), FadeOut(title))

        # --- Part 2: Convergence graph ---
        ax = Axes(
            x_range=[0, 50, 10],
            y_range=[0, 3, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True},
            x_axis_config={"numbers_to_include": [10, 20, 30, 40, 50]},
            y_axis_config={"numbers_to_include": [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]},
        ).shift(DOWN * 0.3)
        ax_label_x = ax.get_x_axis_label("N")
        ax_label_y = ax.get_y_axis_label(r"\text{Partial sum}")
        self.play(Create(ax), Write(ax_label_x), Write(ax_label_y))

        s_values = [
            (2, BLUE, r"s=2 \to \pi^2/6 \approx 1.645"),
            (3, GREEN, r"s=3 \approx 1.202"),
            (1.1, ORANGE, r"s=1.1 \text{ (slow convergence)}"),
            (1, RED, r"s=1 \text{ (diverges!)}"),
        ]

        curves = []
        labels_group = VGroup()
        target_vals = {2: np.pi**2 / 6, 3: 1.2020569, 1.1: None, 1: None}

        for s, color, label_str in s_values:
            Ns = list(range(1, 51))
            pts = [ax.c2p(N, partial_sum(s, N)) for N in Ns]
            curve = VMobject(color=color, stroke_width=2.5)
            curve.set_points_as_corners(pts)
            curves.append(curve)

            lbl = MathTex(label_str, color=color).scale(0.45)
            labels_group.add(lbl)

        labels_group.arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_corner(UR, buff=0.4)

        graph_title = Text("Partial sums of ζ(s)", font_size=28).next_to(ax, UP, buff=0.3)
        self.play(Write(graph_title))

        for (s, color, _), curve, lbl in zip(s_values, curves, labels_group):
            self.play(Create(curve), FadeIn(lbl), run_time=1.8)

            # Draw convergence line for s=2 and s=3
            if s in target_vals and target_vals[s]:
                h_line = DashedLine(
                    ax.c2p(0, target_vals[s]),
                    ax.c2p(50, target_vals[s]),
                    color=color, stroke_width=1.5, dash_length=0.15
                )
                self.play(Create(h_line), run_time=0.6)

        self.wait(2)

        # --- Part 3: Conclusion text ---
        self.play(*[FadeOut(m) for m in self.mobjects])

        conclusion = VGroup(
            MathTex(r"\zeta(s) \text{ converges for } \text{Re}(s) > 1").scale(0.9),
            MathTex(r"\zeta(1) = 1 + \tfrac{1}{2} + \tfrac{1}{3} + \cdots = \infty \quad \text{(diverges)}").scale(0.85).set_color(RED),
            MathTex(r"\text{But } \zeta(s) \text{ can be \textit{extended} to all } s \in \mathbb{C} \setminus \{1\}").scale(0.85).set_color(YELLOW),
            Text("→  Analytic Continuation", font_size=30).set_color(YELLOW),
        ).arrange(DOWN, buff=0.5)

        for line in conclusion:
            self.play(Write(line), run_time=1.2)
            self.wait(0.6)

        self.wait(2)
