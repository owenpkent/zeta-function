"""
ZeroFreeRegion
==============
Visualizes the zero-free region of ζ(s), the Vinogradov–Korobov boundary,
and the "2/3 wall" — the analytic ceiling that has not moved since 1958.

Shows how the proven zero-free region narrows as Im(s) grows,
and how far it remains from the critical line.
"""

from manim import *
import numpy as np


class ZeroFreeRegion(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────────────────
        title = Title("The Zero-Free Region and the 2/3 Wall")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # ── Build the complex plane ────────────────────────────────────────
        plane = Axes(
            x_range=[0, 1.1, 0.25],
            y_range=[0, 200, 50],
            x_length=8,
            y_length=6.5,
            axis_config={"stroke_width": 1.5, "include_numbers": True},
            x_axis_config={"numbers_to_include": [0, 0.25, 0.5, 0.75, 1.0]},
            y_axis_config={"numbers_to_include": [0, 50, 100, 150, 200]},
        ).shift(DOWN * 0.3)

        x_label = MathTex(r"\sigma = \text{Re}(s)").scale(0.5).next_to(plane.x_axis, DOWN, buff=0.4)
        y_label = MathTex(r"t = \text{Im}(s)").scale(0.5).next_to(plane.y_axis, LEFT, buff=0.3).rotate(PI / 2)

        self.play(Create(plane), Write(x_label), Write(y_label))

        # ── Critical line at σ = 1/2 ──────────────────────────────────────
        crit_line = Line(
            plane.c2p(0.5, 0), plane.c2p(0.5, 200),
            color=YELLOW, stroke_width=2.5,
        )
        crit_label = MathTex(r"\sigma = \tfrac{1}{2}", color=YELLOW).scale(0.5)
        crit_label.next_to(plane.c2p(0.5, 200), UP, buff=0.1)
        self.play(Create(crit_line), Write(crit_label))

        # ── Line at σ = 1 ─────────────────────────────────────────────────
        line_one = DashedLine(
            plane.c2p(1.0, 0), plane.c2p(1.0, 200),
            color=GREY_B, stroke_width=1.5,
        )
        one_label = MathTex(r"\sigma = 1", color=GREY_B).scale(0.45)
        one_label.next_to(plane.c2p(1.0, 200), UP, buff=0.1)
        self.play(Create(line_one), Write(one_label))
        self.wait(0.5)

        # ── Draw the Vinogradov–Korobov zero-free boundary ─────────────────
        # σ ≥ 1 - c / (log t)^{2/3}  for large t
        # We use c = 0.05 for visual clarity
        c_vk = 0.05

        def vk_boundary(t):
            if t < 3:
                return 1.0
            return 1.0 - c_vk / (np.log(t)) ** (2 / 3)

        t_vals = np.linspace(3, 200, 300)
        sigma_vals = [vk_boundary(t) for t in t_vals]

        # Build the zero-free shaded region (from boundary to σ = 1.1)
        boundary_pts_right = [plane.c2p(1.1, t) for t in t_vals]
        boundary_pts_left = [plane.c2p(s, t) for s, t in zip(sigma_vals, t_vals)]

        # Shade zero-free region
        region_pts = (
            boundary_pts_left
            + list(reversed(boundary_pts_right))
        )
        zero_free_region = Polygon(
            *region_pts,
            fill_color=GREEN, fill_opacity=0.2, stroke_width=0,
        )

        # The boundary curve itself
        boundary_curve = VMobject(color=GREEN, stroke_width=3)
        boundary_curve.set_points_smoothly(boundary_pts_left)

        region_label = Text("Zero-free region\n(proven)", font_size=18, color=GREEN)
        region_label.move_to(plane.c2p(0.97, 100))

        self.play(FadeIn(zero_free_region), Create(boundary_curve), Write(region_label), run_time=2)
        self.wait(1)

        # ── Label the boundary formula ─────────────────────────────────────
        formula = MathTex(
            r"\sigma \geq 1 - \frac{c}{(\log t)^{2/3}}",
            color=GREEN,
        ).scale(0.6)
        formula.to_corner(UR, buff=0.5)
        formula_note = Text("Vinogradov–Korobov (1958)", font_size=16, color=GREEN_B)
        formula_note.next_to(formula, DOWN, buff=0.15)

        self.play(Write(formula), Write(formula_note))
        self.wait(1)

        # ── Show the GAP between boundary and critical line ────────────────
        gap_t = 100
        gap_left = plane.c2p(0.5, gap_t)
        gap_right = plane.c2p(vk_boundary(gap_t), gap_t)

        gap_arrow = DoubleArrow(
            gap_left, gap_right,
            color=RED, stroke_width=2.5, tip_length=0.15, buff=0,
        )
        gap_label = MathTex(r"\text{THE GAP}", color=RED).scale(0.5)
        gap_label.next_to(gap_arrow, UP, buff=0.08)

        self.play(Create(gap_arrow), Write(gap_label))
        self.wait(1)

        gap_note = Text(
            "This gap has not narrowed\nsince 1958 — 67+ years.",
            font_size=18, color=RED,
        )
        gap_note.next_to(gap_label, UP, buff=0.2)
        self.play(Write(gap_note))
        self.wait(2)

        # ── Shade the unknown region (between crit line and boundary) ──────
        unknown_pts_left = [plane.c2p(0.5, t) for t in t_vals]
        unknown_pts_right = boundary_pts_left[::-1]
        unknown_region = Polygon(
            *unknown_pts_left, *unknown_pts_right,
            fill_color=RED, fill_opacity=0.1, stroke_width=0,
        )
        unknown_label = Text("Unknown\nregion", font_size=16, color=RED_B)
        unknown_label.move_to(plane.c2p(0.72, 50))

        self.play(FadeIn(unknown_region), Write(unknown_label))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Part 2: The Wall — why 2/3 can't be improved ──────────────────
        wall_title = Text("Why the 2/3 exponent is stuck", font_size=30, color=RED)
        wall_title.to_edge(UP, buff=0.5)
        self.play(Write(wall_title))

        explanation = VGroup(
            Text("The classical proof uses trigonometric inequalities:", font_size=22),
            MathTex(r"3 + 4\cos\theta + \cos 2\theta \geq 0").scale(0.85),
            Text("", font_size=8),
            Text("This inequality is OPTIMAL — it cannot be improved.", font_size=22, color=ORANGE),
            Text("Any proof using this technique is permanently", font_size=22, color=ORANGE),
            Text("capped at the 2/3 exponent.", font_size=22, color=ORANGE),
            Text("", font_size=8),
            Text("To go further requires fundamentally new methods.", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.2).next_to(wall_title, DOWN, buff=0.5)

        for mob in explanation:
            self.play(Write(mob), run_time=0.7)
        self.wait(1)

        # Timeline
        timeline_title = Text("Progress on the zero-free exponent:", font_size=22)
        timeline_title.next_to(explanation, DOWN, buff=0.5)

        years = VGroup(
            Text("1896: exponent 1 (de la Vallée Poussin)", font_size=18),
            Text("1922: exponent ~1 improved slightly", font_size=18),
            Text("1958: exponent 2/3 (Vinogradov–Korobov)", font_size=18, color=GREEN),
            Text("1959–2026: NO IMPROVEMENT", font_size=18, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(timeline_title, DOWN, buff=0.2)

        self.play(Write(timeline_title))
        for y in years:
            self.play(Write(y), run_time=0.6)
        self.wait(3)
