"""
CriticalStrip
=============
Visualizes the critical strip (0 < Re(s) < 1), the critical line Re(s) = 1/2,
the functional equation symmetry s <-> 1-s, and the location of zeros.
"""

from manim import *
import numpy as np


class CriticalStrip(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────────────────
        title = Title("The Critical Strip and Critical Line")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # ── Build the complex plane ────────────────────────────────────────
        plane = ComplexPlane(
            x_range=[-1.5, 2.5, 1],
            y_range=[-5, 35, 5],
            x_length=7,
            y_length=7.5,
            background_line_style={"stroke_color": GREY, "stroke_opacity": 0.35, "stroke_width": 1},
            axis_config={"stroke_width": 1.5},
        ).shift(RIGHT * 0.5)

        sigma_labels = VGroup(*[
            MathTex(str(v)).scale(0.45).next_to(plane.n2p(complex(v, 0)), DOWN, buff=0.12)
            for v in [-1, 0, 1, 2]
        ])
        t_labels = VGroup(*[
            MathTex(str(v)).scale(0.45).next_to(plane.n2p(complex(0, v)), LEFT, buff=0.08)
            for v in [0, 10, 20, 30]
        ])
        re_label = MathTex(r"\text{Re}(s)").scale(0.5).next_to(plane.n2p(complex(2.5, 0)), RIGHT, buff=0.05)
        im_label = MathTex(r"\text{Im}(s)").scale(0.5).next_to(plane.n2p(complex(0, 35)), UP, buff=0.05)

        self.play(Create(plane), FadeIn(sigma_labels), FadeIn(t_labels), Write(re_label), Write(im_label))
        self.wait(0.5)

        # ── Shade the critical strip 0 < Re(s) < 1 ────────────────────────
        strip = Rectangle(
            width=plane.n2p(complex(1, 0))[0] - plane.n2p(complex(0, 0))[0],
            height=plane.n2p(complex(0, 35))[1] - plane.n2p(complex(0, -5))[1],
            fill_color=BLUE, fill_opacity=0.15, stroke_width=0,
        )
        strip.move_to(
            (plane.n2p(complex(0, 0)) + plane.n2p(complex(1, 0))) / 2 * [1, 0, 0]
            + np.array([0, (plane.n2p(complex(0, 35))[1] + plane.n2p(complex(0, -5))[1]) / 2, 0])
        )
        strip_label = MathTex(r"\text{Critical Strip}", color=BLUE).scale(0.5)
        strip_label.move_to(plane.n2p(complex(0.5, 32)))

        self.play(FadeIn(strip), Write(strip_label))
        self.wait(0.8)

        # ── Draw the critical line Re(s) = 1/2 ────────────────────────────
        crit_line = Line(
            plane.n2p(complex(0.5, -5)),
            plane.n2p(complex(0.5, 35)),
            color=YELLOW, stroke_width=2.5,
        )
        crit_label = MathTex(r"\text{Re}(s) = \tfrac{1}{2}", color=YELLOW).scale(0.5)
        crit_label.next_to(plane.n2p(complex(0.5, 34)), UR, buff=0.05)

        self.play(Create(crit_line), Write(crit_label))
        self.wait(0.8)

        # ── Draw the lines Re(s) = 0 and Re(s) = 1 ─────────────────────────
        line0 = DashedLine(
            plane.n2p(complex(0, -5)), plane.n2p(complex(0, 35)),
            color=GREY_B, stroke_width=1.5, dash_length=0.2
        )
        line1 = DashedLine(
            plane.n2p(complex(1, -5)), plane.n2p(complex(1, 35)),
            color=GREY_B, stroke_width=1.5, dash_length=0.2
        )
        label0 = MathTex(r"\sigma=0", color=GREY_B).scale(0.4).next_to(plane.n2p(complex(0, 33)), UL, buff=0.05)
        label1 = MathTex(r"\sigma=1", color=GREY_B).scale(0.4).next_to(plane.n2p(complex(1, 33)), UR, buff=0.05)

        self.play(Create(line0), Create(line1), Write(label0), Write(label1))
        self.wait(0.5)

        # ── Functional equation symmetry: s <-> 1-s ────────────────────────
        sym_label = Text("Functional equation: ζ(s) = ζ(1−s)  [up to known factors]",
                         font_size=20, color=ORANGE).to_edge(DOWN, buff=0.25)
        self.play(Write(sym_label))

        # Animate a point s and its mirror 1-s
        s_val = complex(0.7, 20)
        mirror_val = 1 - s_val.real + 1j * s_val.imag  # same Im, Re -> 1 - Re

        dot_s = Dot(plane.n2p(s_val), color=GREEN, radius=0.1)
        dot_mirror = Dot(plane.n2p(mirror_val), color=PINK, radius=0.1)
        s_dot_label = MathTex(r"s", color=GREEN).scale(0.55).next_to(dot_s, RIGHT, buff=0.08)
        m_dot_label = MathTex(r"1-\bar{s}", color=PINK).scale(0.55).next_to(dot_mirror, LEFT, buff=0.08)

        sym_arrow = DoubleArrow(dot_s.get_center(), dot_mirror.get_center(),
                                buff=0.12, color=ORANGE, stroke_width=1.5, tip_length=0.15)

        self.play(FadeIn(dot_s), Write(s_dot_label))
        self.play(Create(sym_arrow))
        self.play(FadeIn(dot_mirror), Write(m_dot_label))
        self.wait(1.5)
        self.play(FadeOut(dot_s), FadeOut(dot_mirror), FadeOut(s_dot_label),
                  FadeOut(m_dot_label), FadeOut(sym_arrow), FadeOut(sym_label))

        # ── Plot first few known zeros on the critical line ────────────────
        known_zeros_t = [
            14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
        ]

        zero_dots = VGroup()
        zero_labels = VGroup()
        for i, t in enumerate(known_zeros_t):
            if t <= 34:
                d = Dot(plane.n2p(complex(0.5, t)), color=RED, radius=0.1)
                lbl = MathTex(rf"\rho_{{{i+1}}}", color=RED).scale(0.45)
                lbl.next_to(d, RIGHT, buff=0.08)
                zero_dots.add(d)
                zero_labels.add(lbl)

        zeros_title = Text("Non-trivial zeros (first 5)", font_size=22, color=RED).to_edge(DOWN, buff=0.25)
        self.play(Write(zeros_title))
        self.play(LaggedStartMap(FadeIn, zero_dots, lag_ratio=0.3),
                  LaggedStartMap(Write, zero_labels, lag_ratio=0.3))
        self.wait(2)

        # ── Sidebar: Riemann Hypothesis statement ──────────────────────────
        rh_box = VGroup(
            Text("Riemann Hypothesis:", font_size=22, color=YELLOW),
            MathTex(r"\text{All non-trivial zeros have } \text{Re}(\rho) = \tfrac{1}{2}").scale(0.65),
        ).arrange(DOWN, buff=0.2)
        rh_box.to_corner(UL, buff=0.35)
        box_rect = SurroundingRectangle(rh_box, color=YELLOW, buff=0.15, corner_radius=0.1)
        self.play(Write(rh_box), Create(box_rect))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Summary table ──────────────────────────────────────────────────
        table = MobjectTable(
            [
                [Text("Region", font_size=22), Text("What we know", font_size=22)],
                [MathTex(r"\text{Re}(s) > 1"), Text("No zeros (series converges, nonzero)", font_size=20)],
                [MathTex(r"\text{Re}(s) = 1"), Text("No zeros (proved 1896, implies PNT)", font_size=20)],
                [MathTex(r"0 < \text{Re}(s) < 1"), Text("All non-trivial zeros here", font_size=20)],
                [MathTex(r"\text{Re}(s) = 1/2"), Text("All KNOWN zeros here (RH)", font_size=20).set_color(YELLOW)],
                [MathTex(r"\text{Re}(s) < 0"), Text("Trivial zeros at s = -2,-4,-6,...", font_size=20)],
            ],
            include_outer_lines=True,
        ).scale(0.75)
        self.play(Create(table))
        self.wait(3)
