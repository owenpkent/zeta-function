"""
FiveGaps
========
Animated diagram of the five fundamental obstructions to proving RH:
Positivity Gap, Geometry Gap, Exactness Gap, Analytic Ceiling, Bridge Gap.

Shows how each approach runs into its wall, and how the walls are all
connected — symptoms of the same missing framework.
"""

from manim import *
import numpy as np


class FiveGaps(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────────────────
        title = Title("Five Walls Between Us and a Proof")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # ── Part 1: Show each gap one at a time ───────────────────────────

        gaps = [
            {
                "name": "The Positivity Gap",
                "color": RED,
                "approach": "Spectral / Hilbert–Pólya",
                "what": "Find a self-adjoint operator whose\neigenvalues are the zeta zeros",
                "wall": "Cannot prove the operator's eigenvalues\nare real (self-adjointness unproven)",
                "needs": "A source of POSITIVITY — some geometric\nor algebraic structure forcing real spectrum",
            },
            {
                "name": "The Geometry Gap",
                "color": BLUE,
                "approach": "Arithmetic Geometry",
                "what": "Lift Weil's function-field proof\nto the integers (Spec(Z))",
                "wall": "Spec(Z) is not compact, has no\nFrobenius, lacks needed cohomology",
                "needs": "A new geometric object with the\nstructure of a smooth compact curve",
            },
            {
                "name": "The Exactness Gap",
                "color": GREEN,
                "approach": "Random Matrix Theory",
                "what": "Use GUE statistics to understand\nzero distribution",
                "wall": "Statistics describe distributions,\nnot individual zero positions",
                "needs": "A method to convert 'almost all'\ninto 'all' — algebraic structure\nbeneath the statistics",
            },
            {
                "name": "The Analytic Ceiling",
                "color": ORANGE,
                "approach": "Zero-Free Regions",
                "what": "Push the zero-free region\nto the critical line",
                "wall": "Stuck at exponent 2/3 since 1958.\nThe underlying inequalities are optimal.",
                "needs": "Fundamentally new exponential sum\ntechniques beyond Vinogradov–Korobov",
            },
            {
                "name": "The Bridge Gap",
                "color": PURPLE,
                "approach": "Connecting Worlds",
                "what": "Rigorously link spectral theory\n(operators) to arithmetic (primes)",
                "wall": "Connection is heuristic and statistical\nbut not rigorous or constructive",
                "needs": "A single mathematical object that IS\nboth arithmetic and spectral",
            },
        ]

        for gap in gaps:
            self.show_gap_card(gap)

        # ── Part 2: All five at once — the convergence ────────────────────
        overview_title = Text("Five walls — or one?", font_size=30, color=YELLOW)
        overview_title.to_edge(UP, buff=0.4)
        self.play(Write(overview_title))

        # Create compact icons for each gap
        icons = VGroup()
        for g in gaps:
            icon = VGroup(
                RoundedRectangle(
                    width=2.2, height=1.2,
                    corner_radius=0.1,
                    color=g["color"],
                    fill_color=g["color"],
                    fill_opacity=0.15,
                    stroke_width=2,
                ),
                Text(g["name"].replace("The ", ""), font_size=14, color=g["color"]),
            )
            icon[1].move_to(icon[0])
            icons.add(icon)

        icons.arrange_in_grid(rows=1, buff=0.3).next_to(overview_title, DOWN, buff=0.5)
        self.play(LaggedStartMap(FadeIn, icons, lag_ratio=0.15))
        self.wait(1)

        # Draw arrows from all to center
        center_box = RoundedRectangle(
            width=4, height=1.5,
            corner_radius=0.15,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.15,
            stroke_width=3,
        ).shift(DOWN * 1.2)
        center_text = VGroup(
            Text("Same Missing Thing:", font_size=18, color=YELLOW),
            Text("A unified framework where", font_size=16),
            Text("arithmetic IS geometry IS", font_size=16),
            Text("spectral theory", font_size=16),
        ).arrange(DOWN, buff=0.06).move_to(center_box)

        arrows = VGroup()
        for icon in icons:
            arr = Arrow(
                icon.get_bottom(), center_box.get_top(),
                color=GREY_B, stroke_width=1.5, tip_length=0.12, buff=0.1,
            )
            arrows.add(arr)

        self.play(
            LaggedStartMap(Create, arrows, lag_ratio=0.1),
            FadeIn(center_box), Write(center_text),
            run_time=2,
        )
        self.wait(2)

        # ── Part 3: The pattern ────────────────────────────────────────────
        pattern = VGroup(
            Text("Each approach fails where it needs", font_size=22),
            Text("to become one of the other approaches.", font_size=22),
            Text("", font_size=8),
            Text("The spectral approach needs GEOMETRY for positivity.", font_size=20, color=RED),
            Text("The geometric approach needs ANALYSIS for trace formulas.", font_size=20, color=BLUE),
            Text("The analytic approach needs ALGEBRA for deeper structure.", font_size=20, color=ORANGE),
            Text("", font_size=8),
            Text("The new mathematics is the thing that", font_size=22, color=YELLOW),
            Text("makes them all the same approach.", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.1).shift(DOWN * 3.8)

        self.play(
            VGroup(overview_title, icons, arrows, center_box, center_text).animate.shift(UP * 1.5),
        )
        for mob in pattern:
            self.play(Write(mob), run_time=0.6)
        self.wait(3)

    def show_gap_card(self, gap):
        """Display a single gap as an animated card."""
        # Title
        name = Text(gap["name"], font_size=32, color=gap["color"])
        name.to_edge(UP, buff=0.5)

        # Approach
        approach_label = Text("Approach:", font_size=18, color=GREY_B)
        approach_text = Text(gap["approach"], font_size=22)
        approach = VGroup(approach_label, approach_text).arrange(RIGHT, buff=0.2)

        # What it tries
        tries_label = Text("Strategy:", font_size=18, color=GREY_B)
        tries_text = Text(gap["what"], font_size=20, line_spacing=1.2)
        tries = VGroup(tries_label, tries_text).arrange(RIGHT, buff=0.2, aligned_edge=UP)

        # The wall
        wall_icon = Rectangle(
            width=0.15, height=1.2, fill_color=gap["color"],
            fill_opacity=0.8, stroke_width=0,
        )
        wall_label = Text("THE WALL:", font_size=18, color=gap["color"])
        wall_text = Text(gap["wall"], font_size=20, color=gap["color"], line_spacing=1.2)
        wall = VGroup(
            VGroup(wall_icon, wall_label).arrange(RIGHT, buff=0.15),
            wall_text,
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        # What's needed
        needs_label = Text("Needs:", font_size=18, color=GREEN)
        needs_text = Text(gap["needs"], font_size=20, color=GREEN_B, line_spacing=1.2)
        needs = VGroup(needs_label, needs_text).arrange(RIGHT, buff=0.2, aligned_edge=UP)

        # Layout
        card = VGroup(approach, tries, wall, needs).arrange(
            DOWN, buff=0.35, aligned_edge=LEFT,
        ).next_to(name, DOWN, buff=0.4)

        # Animate
        self.play(Write(name))
        for section in card:
            self.play(Write(section), run_time=0.8)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [name, card]])
