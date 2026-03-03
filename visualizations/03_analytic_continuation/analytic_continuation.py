"""
AnalyticContinuation
====================
Visualizes how the zeta function is extended beyond Re(s) > 1
using the eta function / alternating series relationship:
    zeta(s) = eta(s) / (1 - 2^(1-s))
    eta(s)  = 1 - 1/2^s + 1/3^s - 1/4^s + ...  (converges for Re(s) > 0)
"""

from manim import *
import numpy as np


def eta_partial(s, N=300):
    return sum(((-1) ** (n + 1)) / (n**s) for n in range(1, N + 1))


def zeta_from_eta(s, N=300):
    if abs(s - 1) < 0.05:
        return float("inf")
    eta = eta_partial(s, N)
    denom = 1 - 2 ** (1 - s)
    if abs(denom) < 1e-10:
        return float("inf")
    return eta / denom


class AnalyticContinuation(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────────────────
        title = Title("Analytic Continuation of $\\zeta(s)$")
        self.play(Write(title))
        self.wait(1)

        # ── Step 1: The problem ────────────────────────────────────────────
        problem = VGroup(
            MathTex(r"\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}").scale(0.9),
            MathTex(r"\text{converges only for } \text{Re}(s) > 1").scale(0.85).set_color(RED),
            MathTex(r"\text{But we want } \zeta(s) \text{ for ALL } s \in \mathbb{C}").scale(0.85).set_color(YELLOW),
        ).arrange(DOWN, buff=0.45)
        for mob in problem:
            self.play(Write(mob), run_time=1)
            self.wait(0.5)
        self.wait(1)
        self.play(FadeOut(problem), FadeOut(title))

        # ── Step 2: Introduce the eta function ─────────────────────────────
        eta_title = Text("Step 1: The Alternating Series (Eta Function)", font_size=30)
        eta_title.to_edge(UP)
        self.play(Write(eta_title))

        eta_def = MathTex(
            r"\eta(s)",
            r"= 1 - \frac{1}{2^s} + \frac{1}{3^s} - \frac{1}{4^s} + \cdots",
            r"= \sum_{n=1}^\infty \frac{(-1)^{n+1}}{n^s}",
        ).scale(0.85).shift(UP * 0.5)
        eta_conv = MathTex(
            r"\text{Converges for } \text{Re}(s) > 0",
        ).scale(0.85).set_color(GREEN).shift(DOWN * 0.3)
        self.play(Write(eta_def))
        self.wait(1)
        self.play(Write(eta_conv))
        self.wait(1.5)

        # ── Step 3: Relationship between eta and zeta ──────────────────────
        relation_label = Text("Step 2: Link eta to zeta", font_size=30).to_edge(UP)
        self.play(ReplacementTransform(eta_title, relation_label))

        relation = MathTex(
            r"\eta(s) = \left(1 - 2^{1-s}\right) \zeta(s)",
        ).scale(0.9).shift(UP * 0.8)
        therefore = MathTex(
            r"\therefore \quad \zeta(s) = \frac{\eta(s)}{1 - 2^{1-s}}",
        ).scale(1.0).set_color(YELLOW)
        domain = MathTex(
            r"\text{valid for } \text{Re}(s) > 0,\; s \neq 1",
        ).scale(0.8).shift(DOWN * 1.0)

        self.play(FadeOut(eta_def), FadeOut(eta_conv))
        self.play(Write(relation))
        self.wait(1)
        self.play(Write(therefore))
        self.wait(1)
        self.play(Write(domain))
        self.wait(2)
        self.play(FadeOut(relation), FadeOut(therefore), FadeOut(domain), FadeOut(relation_label))

        # ── Step 4: Visualize — partial sums converge in extended region ───
        ax_title = Text("Partial sums of ζ(s) via eta — real axis", font_size=26).to_edge(UP)
        self.play(Write(ax_title))

        ax = Axes(
            x_range=[-2, 3, 1],
            y_range=[-3, 5, 1],
            x_length=9,
            y_length=5.5,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.3)
        ax_xlabel = ax.get_x_axis_label("s \\text{ (real)}")
        ax_ylabel = ax.get_y_axis_label("\\zeta(s)")
        self.play(Create(ax), Write(ax_xlabel), Write(ax_ylabel))

        # Shade the "original" region Re(s) > 1
        region_gt1 = ax.get_area(
            ax.plot(lambda x: 5, x_range=[1, 3]),
            x_range=[1, 3],
            color=BLUE,
            opacity=0.12,
        )
        region_label1 = MathTex(r"\text{Series converges}", color=BLUE).scale(0.5)
        region_label1.next_to(ax.c2p(2, 4.5), ORIGIN)

        # Shade the "extended" region 0 < Re(s) < 1
        region_01 = ax.get_area(
            ax.plot(lambda x: 5, x_range=[0.05, 1]),
            x_range=[0.05, 1],
            color=GREEN,
            opacity=0.12,
        )
        region_label2 = MathTex(r"\text{Continuation}", color=GREEN).scale(0.5)
        region_label2.next_to(ax.c2p(0.5, 4.5), ORIGIN)

        self.play(FadeIn(region_gt1), Write(region_label1))
        self.play(FadeIn(region_01), Write(region_label2))

        # Plot zeta(s) using eta method for s in (-1.8, 3), s != 1
        s_vals_left = np.linspace(-1.8, 0.95, 120)
        s_vals_right = np.linspace(1.05, 2.9, 80)

        def safe_zeta(s):
            try:
                v = zeta_from_eta(complex(s), N=500)
                if isinstance(v, float) and (v == float("inf") or np.isnan(v)):
                    return None
                v = float(v.real) if hasattr(v, "real") else float(v)
                if abs(v) > 5:
                    return None
                return v
            except Exception:
                return None

        pts_left = [(s, safe_zeta(s)) for s in s_vals_left]
        pts_right = [(s, safe_zeta(s)) for s in s_vals_right]

        def make_curve(pts, color):
            valid = [(s, v) for s, v in pts if v is not None]
            if len(valid) < 2:
                return VMobject()
            path = VMobject(color=color, stroke_width=2.5)
            path.set_points_smoothly([ax.c2p(s, v) for s, v in valid])
            return path

        curve_right = make_curve(pts_right, BLUE)
        curve_left = make_curve(pts_left, GREEN)

        self.play(Create(curve_right), run_time=1.5)
        self.play(Create(curve_left), run_time=2)

        # Mark the trivial zeros at s = -2, -4
        for zero_s in [-2]:
            dot = Dot(ax.c2p(zero_s, 0), color=RED, radius=0.08)
            zlabel = MathTex(rf"s={zero_s}", color=RED).scale(0.45).next_to(dot, DOWN, buff=0.1)
            self.play(FadeIn(dot), Write(zlabel))

        # Mark the pole at s=1
        pole_line = DashedLine(ax.c2p(1, -3), ax.c2p(1, 5), color=RED, stroke_width=1.5)
        pole_label = MathTex(r"\text{pole}", color=RED).scale(0.5).next_to(ax.c2p(1, 4.5), RIGHT, buff=0.05)
        self.play(Create(pole_line), Write(pole_label))

        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Summary ────────────────────────────────────────────────────────
        summary = VGroup(
            MathTex(r"\zeta(s) \text{ is defined for all } s \in \mathbb{C} \setminus \{1\}").scale(0.85),
            MathTex(r"\text{Simple pole at } s = 1 \text{ with residue } 1").scale(0.8).set_color(RED),
            MathTex(r"\text{Trivial zeros at } s = -2, -4, -6, \ldots").scale(0.8).set_color(YELLOW),
            MathTex(r"\text{Non-trivial zeros in the critical strip } 0 < \text{Re}(s) < 1").scale(0.8).set_color(GREEN),
        ).arrange(DOWN, buff=0.45)
        for line in summary:
            self.play(Write(line), run_time=1)
            self.wait(0.4)
        self.wait(2)
