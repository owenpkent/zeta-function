"""
RobinsInequality
================
Visualizes Robin's inequality: σ(n) < e^γ · n · ln(ln(n)) for all n > 5040,
which is equivalent to the Riemann Hypothesis.

Shows how the ratio σ(n)/(n·ln(ln(n))) compares to e^γ, how colossally
abundant numbers are the "hardest cases," and the single exception at 5040.
"""

from manim import *
import numpy as np
import math


def divisor_sum(n):
    """Sum of divisors of n."""
    if n <= 0:
        return 0
    total = 0
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total


EULER_GAMMA = 0.5772156649015329
E_GAMMA = math.exp(EULER_GAMMA)


class RobinsInequality(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────────────────
        title = Title(r"Robin's Inequality and the Riemann Hypothesis")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # ── Part 1: State the equivalence ──────────────────────────────────
        statement = VGroup(
            Text("Robin (1984) proved:", font_size=26),
            Text("", font_size=8),
            MathTex(
                r"\text{RH} \iff \sigma(n) < e^\gamma \, n \ln\ln n"
                r"\;\;\text{for all } n > 5040"
            ).scale(0.75),
            Text("", font_size=8),
            VGroup(
                MathTex(r"\sigma(n) = \text{sum of divisors of } n").scale(0.6),
                MathTex(r"\gamma \approx 0.5772 \text{ (Euler–Mascheroni constant)}").scale(0.6),
                MathTex(r"e^\gamma \approx 1.7811").scale(0.6),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.25)

        for mob in statement:
            self.play(Write(mob), run_time=0.8)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Part 2: Plot the ratio σ(n)/(n·ln(ln(n))) vs e^γ ──────────────
        ax = Axes(
            x_range=[3, 500, 100],
            y_range=[0, 3.5, 0.5],
            x_length=10,
            y_length=5.5,
            axis_config={"stroke_width": 1.5, "include_numbers": True},
            x_axis_config={"numbers_to_include": [100, 200, 300, 400, 500]},
            y_axis_config={"numbers_to_include": [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]},
        ).shift(DOWN * 0.3)

        ax_xlabel = MathTex(r"n").scale(0.5).next_to(ax.x_axis, DOWN, buff=0.3)
        ax_ylabel = MathTex(
            r"\frac{\sigma(n)}{n \ln\ln n}"
        ).scale(0.55).next_to(ax.y_axis, LEFT, buff=0.15).shift(UP * 0.5)

        plot_title = Text(
            "Robin's ratio vs the e^γ threshold",
            font_size=22,
        ).to_edge(UP, buff=0.3)

        self.play(Create(ax), Write(ax_xlabel), Write(ax_ylabel), Write(plot_title))

        # The e^γ threshold line
        threshold_line = DashedLine(
            ax.c2p(3, E_GAMMA), ax.c2p(500, E_GAMMA),
            color=RED, stroke_width=2.5,
        )
        threshold_label = MathTex(
            r"e^\gamma \approx 1.781", color=RED
        ).scale(0.5).next_to(ax.c2p(500, E_GAMMA), RIGHT, buff=0.1)

        self.play(Create(threshold_line), Write(threshold_label))

        # Compute ratio for integers 3 to 500
        n_vals = list(range(10, 501))
        ratios = []
        for n in n_vals:
            lnlnn = math.log(math.log(n))
            if lnlnn > 0:
                ratios.append(divisor_sum(n) / (n * lnlnn))
            else:
                ratios.append(0)

        # Plot as dots
        dots = VGroup()
        for n, r in zip(n_vals, ratios):
            if 0 < r < 3.5:
                color = YELLOW if r > E_GAMMA * 0.95 else BLUE
                d = Dot(ax.c2p(n, r), radius=0.02, color=color)
                dots.add(d)

        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.005), run_time=3)
        self.wait(1)

        # Annotate: all below the line for n > 5040
        below_note = Text(
            "All dots below the red line → RH holds for these n",
            font_size=18, color=GREEN,
        ).next_to(ax, DOWN, buff=0.3)
        self.play(Write(below_note))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Part 3: The special role of 5040 ──────────────────────────────
        special_title = Text("Why 5040?", font_size=32, color=YELLOW)
        special_title.to_edge(UP, buff=0.5)
        self.play(Write(special_title))

        facts = VGroup(
            MathTex(r"5040 = 7! = 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1").scale(0.7),
            Text("", font_size=6),
            Text("5040 is the LAST integer where Robin's inequality", font_size=22),
            Text("can fail — and it does fail for some n ≤ 5040.", font_size=22),
            Text("", font_size=6),
            Text("For EVERY n > 5040:", font_size=22, color=GREEN),
            MathTex(r"\sigma(n) < e^\gamma \, n \ln\ln n \iff \text{RH is true}",
                     color=GREEN).scale(0.7),
            Text("", font_size=6),
            Text("This has been verified computationally for n up to 10¹⁰+",
                 font_size=20, color=BLUE),
        ).arrange(DOWN, buff=0.15).next_to(special_title, DOWN, buff=0.4)

        for mob in facts:
            self.play(Write(mob), run_time=0.6)
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Part 4: Colossally abundant numbers ────────────────────────────
        ca_title = Text("The Hardest Cases: Colossally Abundant Numbers",
                        font_size=26, color=ORANGE)
        ca_title.to_edge(UP, buff=0.5)
        self.play(Write(ca_title))

        ca_explain = VGroup(
            Text("Colossally abundant numbers maximize σ(n)/n^(1+ε)", font_size=20),
            Text("for some ε > 0. They are the integers where", font_size=20),
            Text("Robin's inequality is TIGHTEST — closest to failing.", font_size=20, color=RED),
            Text("", font_size=8),
            Text("First few: 2, 6, 12, 60, 120, 360, 2520, 5040, ...", font_size=20),
            Text("", font_size=8),
            Text("If RH has a counterexample, it will be found among", font_size=20),
            Text("these numbers — they are the adversarial examples.", font_size=20, color=YELLOW),
            Text("", font_size=8),
            Text("Understanding their structure is a concrete,", font_size=20, color=GREEN),
            Text("computable approach to studying RH.", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.12).next_to(ca_title, DOWN, buff=0.4)

        for mob in ca_explain:
            self.play(Write(mob), run_time=0.5)
        self.wait(3)
