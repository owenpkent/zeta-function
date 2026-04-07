"""
FunctionalEquationMirror
========================
Visualizes the functional equation ξ(s) = ξ(1-s) as a mirror symmetry.
Shows how zeros either sit ON the mirror (critical line) or come in
reflected pairs — and why RH says they all choose the mirror.
"""

from manim import *
import numpy as np


KNOWN_ZEROS_T = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
]


class FunctionalEquationMirror(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────────────────
        title = Title(r"The Functional Equation: $\xi(s) = \xi(1-s)$")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # ── Part 1: The mirror ─────────────────────────────────────────────
        plane = Axes(
            x_range=[-0.3, 1.3, 0.5],
            y_range=[-5, 55, 10],
            x_length=7,
            y_length=7,
            axis_config={"stroke_width": 1.5, "include_numbers": True},
            x_axis_config={"numbers_to_include": [0, 0.5, 1]},
            y_axis_config={"numbers_to_include": [0, 10, 20, 30, 40, 50]},
        ).shift(LEFT * 0.8)

        x_label = MathTex(r"\sigma = \text{Re}(s)").scale(0.45).next_to(plane.x_axis, DOWN, buff=0.35)
        y_label = MathTex(r"t = \text{Im}(s)").scale(0.45).next_to(plane.y_axis, UP, buff=0.1)

        self.play(Create(plane), Write(x_label), Write(y_label))

        # The mirror line
        mirror = Line(
            plane.c2p(0.5, -5), plane.c2p(0.5, 55),
            color=YELLOW, stroke_width=4, stroke_opacity=0.8,
        )
        # Glow effect
        mirror_glow = Line(
            plane.c2p(0.5, -5), plane.c2p(0.5, 55),
            color=YELLOW, stroke_width=12, stroke_opacity=0.15,
        )
        mirror_label = MathTex(
            r"\text{Mirror: } \sigma = \tfrac{1}{2}", color=YELLOW
        ).scale(0.55).next_to(plane.c2p(0.5, 55), UR, buff=0.1)

        self.play(Create(mirror_glow), Create(mirror), Write(mirror_label))
        self.wait(0.5)

        # ── Part 2: What the functional equation means ─────────────────────
        eq_box = VGroup(
            MathTex(r"\xi(s) = \xi(1-s)").scale(0.8),
            Text("If ξ vanishes at s, it must also vanish at 1−s", font_size=18),
        ).arrange(DOWN, buff=0.15).to_corner(UR, buff=0.4)
        box_rect = SurroundingRectangle(eq_box, color=ORANGE, buff=0.15, corner_radius=0.1)
        self.play(Write(eq_box), Create(box_rect))
        self.wait(1)

        # ── Part 3: Show a hypothetical OFF-mirror pair ────────────────────
        hypo_label = Text("Hypothetical: a zero OFF the mirror", font_size=20, color=RED)
        hypo_label.to_edge(DOWN, buff=0.3)
        self.play(Write(hypo_label))

        # A zero at σ=0.7, t=20 and its mirror at σ=0.3, t=20
        dot_s = Dot(plane.c2p(0.7, 20), color=RED, radius=0.12)
        dot_mirror = Dot(plane.c2p(0.3, 20), color=RED, radius=0.12)
        label_s = MathTex(r"s", color=RED).scale(0.5).next_to(dot_s, RIGHT, buff=0.1)
        label_1ms = MathTex(r"1\!-\!\bar{s}", color=RED).scale(0.5).next_to(dot_mirror, LEFT, buff=0.1)

        self.play(FadeIn(dot_s), Write(label_s))
        self.wait(0.5)

        # Animate the reflection
        reflect_arrow = Arrow(
            dot_s.get_center(), dot_mirror.get_center(),
            color=ORANGE, stroke_width=2, tip_length=0.15, buff=0.15,
        )
        self.play(Create(reflect_arrow))
        self.play(FadeIn(dot_mirror), Write(label_1ms))
        self.wait(1)

        # Show they come in pairs
        pair_brace = Brace(
            VGroup(dot_s, dot_mirror), DOWN, color=RED, buff=0.15,
        )
        pair_text = Text("Must come as a pair", font_size=16, color=RED)
        pair_text.next_to(pair_brace, DOWN, buff=0.08)
        self.play(Create(pair_brace), Write(pair_text))
        self.wait(1.5)

        # Remove hypothetical
        self.play(
            FadeOut(dot_s), FadeOut(dot_mirror), FadeOut(label_s),
            FadeOut(label_1ms), FadeOut(reflect_arrow), FadeOut(pair_brace),
            FadeOut(pair_text), FadeOut(hypo_label),
        )

        # ── Part 4: Show actual zeros ON the mirror ────────────────────────
        on_label = Text("Reality: all known zeros sit ON the mirror", font_size=20, color=GREEN)
        on_label.to_edge(DOWN, buff=0.3)
        self.play(Write(on_label))

        zero_dots = VGroup()
        for t in KNOWN_ZEROS_T:
            d = Dot(plane.c2p(0.5, t), color=GREEN, radius=0.1)
            zero_dots.add(d)

        self.play(LaggedStartMap(FadeIn, zero_dots, lag_ratio=0.15), run_time=2)
        self.wait(1)

        # Each zero is its own mirror image
        self_mirror_label = VGroup(
            MathTex(r"s = \tfrac{1}{2} + it", color=GREEN).scale(0.55),
            MathTex(r"1 - s = \tfrac{1}{2} - it", color=GREEN).scale(0.55),
            Text("Same point (conjugate pair)!", font_size=16, color=GREEN_B),
        ).arrange(DOWN, buff=0.1).to_corner(DL, buff=0.5)
        self.play(Write(self_mirror_label))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Part 5: The deep question ──────────────────────────────────────
        q1 = Text("The mirror exists because of the functional equation.", font_size=24)
        q2 = Text("But WHY do all zeros choose to sit on it?", font_size=24, color=YELLOW)
        q3 = Text("Why no off-mirror pairs?", font_size=24, color=YELLOW)
        q4 = Text("", font_size=12)
        q5 = Text("That is the Riemann Hypothesis.", font_size=28, color=RED)

        questions = VGroup(q1, q2, q3, q4, q5).arrange(DOWN, buff=0.3)

        for q in questions:
            self.play(Write(q), run_time=1)
            self.wait(0.5)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Part 6: The analogy ────────────────────────────────────────────
        analogy_title = Text("Why this should feel familiar", font_size=26, color=BLUE)
        analogy_title.to_edge(UP, buff=0.5)
        self.play(Write(analogy_title))

        col1 = VGroup(
            Text("Real symmetric matrix", font_size=20, color=BLUE_B),
            Text("─────────────────────", font_size=14, color=GREY),
            Text("Eigenvalues are real", font_size=18),
            Text("", font_size=6),
            Text("WHY? Self-adjointness", font_size=18, color=GREEN),
            Text("forces them onto the", font_size=18, color=GREEN),
            Text("real line. Structural.", font_size=18, color=GREEN),
        ).arrange(DOWN, buff=0.08)

        col2 = VGroup(
            Text("Riemann zeta function", font_size=20, color=YELLOW),
            Text("─────────────────────", font_size=14, color=GREY),
            Text("Zeros are on Re = ½?", font_size=18),
            Text("", font_size=6),
            Text("WHY? Some unknown", font_size=18, color=RED),
            Text("structural property", font_size=18, color=RED),
            Text("forces them there. ???", font_size=18, color=RED),
        ).arrange(DOWN, buff=0.08)

        cols = VGroup(col1, col2).arrange(RIGHT, buff=1.5).next_to(analogy_title, DOWN, buff=0.5)
        self.play(Write(col1), run_time=1.5)
        self.play(Write(col2), run_time=1.5)

        arrow = Arrow(col1.get_right(), col2.get_left(), color=ORANGE, buff=0.3)
        arrow_label = Text("same pattern?", font_size=16, color=ORANGE)
        arrow_label.next_to(arrow, UP, buff=0.08)
        self.play(Create(arrow), Write(arrow_label))

        conclusion = Text(
            "Finding the structural reason = proving RH",
            font_size=24, color=YELLOW,
        ).next_to(cols, DOWN, buff=0.6)
        self.play(Write(conclusion))
        self.wait(3)
