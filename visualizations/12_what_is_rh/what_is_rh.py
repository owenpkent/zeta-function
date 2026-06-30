"""
WhatIsRH
========
A very slow, zero-background explainer: "What is the Riemann Hypothesis?"

Designed to be understood with NO math past arithmetic. Every term is introduced
with an everyday analogy first, then named. One idea per beat. The full spoken
narration also appears on screen as subtitles, so the silent video explains
itself. The matching spoken-narration script lives in NARRATION.md.

Four scenes (render and concatenate):
    manim -qm visualizations/12_what_is_rh/what_is_rh.py Part1_Primes
    manim -qm visualizations/12_what_is_rh/what_is_rh.py Part2_Machine
    manim -qm visualizations/12_what_is_rh/what_is_rh.py Part3_MapAndZeros
    manim -qm visualizations/12_what_is_rh/what_is_rh.py Part4_Hypothesis

Visuals are all 2D and intentionally plain. Nothing here assumes the viewer has
seen the dense version in 11_three_stage_rh.
"""

import re
from manim import *
import numpy as np


# --- palette (friendly, high contrast) --------------------------------------
PRIME = YELLOW
INK = WHITE
ACCENT = TEAL
WAVE = BLUE
WARN = RED
SOFT = GREY_B

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# --- text / subtitle helpers ------------------------------------------------
def wrap(text, width=9):
    """Insert line breaks roughly every `width` words so Text fits the frame."""
    words = text.split()
    lines = [" ".join(words[i:i + width]) for i in range(0, len(words), width)]
    return "\n".join(lines)


def split_sentences(text):
    parts = re.split(r"(?<=[.?!])\s+", text.strip())
    return [p for p in parts if p]


def reading_time(sentence):
    return max(2.6, len(sentence.split()) * 0.36)


def part_title(scene, main, sub=None):
    grp = VGroup(Text(main, font_size=44, color=INK))
    if sub:
        grp.add(Text(sub, font_size=26, color=ACCENT))
    grp.arrange(DOWN, buff=0.35)
    scene.play(FadeIn(grp, shift=UP * 0.2))
    scene.wait(1.6)
    scene.play(FadeOut(grp))


def headline(scene, line, color=INK):
    h = Text(line, font_size=30, color=color).to_edge(UP, buff=0.6)
    scene.play(FadeIn(h, shift=DOWN * 0.2), run_time=0.6)
    return h


def narrate(scene, narration, color=INK, fs=24):
    """Show the narration as bottom subtitles, one sentence at a time."""
    prev = None
    for s in split_sentences(narration):
        txt = Text(wrap(s, 9), font_size=fs, color=color, line_spacing=0.9)
        if txt.width > 12.5:
            txt.scale_to_fit_width(12.5)
        txt.to_edge(DOWN, buff=0.45)
        bg = BackgroundRectangle(txt, color=BLACK, fill_opacity=0.55, buff=0.18)
        sub = VGroup(bg, txt)
        if prev is None:
            scene.play(FadeIn(sub), run_time=0.5)
        else:
            scene.play(FadeOut(prev, run_time=0.25), FadeIn(sub, run_time=0.35))
        scene.wait(reading_time(s))
        prev = sub
    return prev


def clear_beat(scene, *mobjects):
    movers = [m for m in mobjects if m is not None]
    if movers:
        scene.play(*[FadeOut(m) for m in movers])


# --- shared shape helpers ---------------------------------------------------
def prime_staircase(axes, x_max=30, color=PRIME, width=3):
    pts = [axes.c2p(0, 0)]
    count = 0
    for p in PRIMES:
        if p > x_max:
            break
        pts.append(axes.c2p(p, count))
        count += 1
        pts.append(axes.c2p(p, count))
    pts.append(axes.c2p(x_max, count))
    m = VMobject(color=color, stroke_width=width)
    m.set_points_as_corners(pts)
    return m


def make_machine(label="machine"):
    box = RoundedRectangle(corner_radius=0.2, width=2.6, height=2.0,
                           color=INK, stroke_width=3)
    knob = Circle(radius=0.16, color=ACCENT, fill_opacity=1).move_to(box.get_center())
    knob_line = Line(knob.get_center(), knob.get_center() + UP * 0.16, color=BLACK, stroke_width=3)
    in_lab = Text("IN", font_size=18, color=SOFT).next_to(box, UP, buff=0.12)
    out_lab = Text("OUT", font_size=18, color=SOFT).next_to(box, DOWN, buff=0.12)
    name = Text(label, font_size=20, color=ACCENT).move_to(box.get_bottom() + UP * 0.45)
    grp = VGroup(box, knob, knob_line, in_lab, out_lab, name)
    grp.box = box
    return grp


# ===========================================================================
# PART 1 - The Primes and Their Mystery
# ===========================================================================
class Part1_Primes(Scene):
    def construct(self):
        part_title(self, "What is the Riemann Hypothesis?",
                   "Part 1 - The Primes and Their Mystery")

        # Beat 1: The Building Blocks.
        h = headline(self, "The atoms of numbers")
        primes_row = VGroup(*[Text(str(p), font_size=40, color=PRIME) for p in [2, 3, 5, 7, 11, 13]])
        primes_row.arrange(RIGHT, buff=0.5).shift(UP * 1.4)
        self.play(LaggedStartMap(FadeIn, primes_row, lag_ratio=0.25))
        factor = MathTex(r"12 = 2 \times 2 \times 3", font_size=48).shift(DOWN * 0.2)
        balls = VGroup(*[
            VGroup(Circle(radius=0.32, color=PRIME, fill_opacity=0.25, stroke_width=2),
                   Text(t, font_size=26, color=PRIME))
            for t in ["2", "2", "3"]
        ])
        for b in balls:
            b[1].move_to(b[0].get_center())
        balls.arrange(RIGHT, buff=0.5).next_to(factor, DOWN, buff=0.5)
        self.play(Write(factor))
        self.play(LaggedStartMap(FadeIn, balls, lag_ratio=0.3))
        narr = narrate(self,
            "Let's start with a special kind of number. A whole number is a counting number "
            "like 1, 2, 3, with no fractions or pieces. Some whole numbers can't be made by "
            "multiplying smaller whole numbers together. Two, three, five, seven, eleven. "
            "The only way to reach them by multiplying is one times the number itself. "
            "Every other number is built by multiplying these together. Twelve is two times two times three. "
            "Just like every object is built from a small set of atoms, every number is built from these. "
            "Mathematicians call them prime numbers.")
        clear_beat(self, h, primes_row, factor, balls, narr)

        # Beat 2: They Look Random.
        h = headline(self, "Where is the next one?")
        nline = NumberLine(x_range=[0, 30, 5], length=11, include_numbers=True,
                           font_size=22).shift(UP * 0.3)
        self.play(Create(nline))
        pdots = VGroup()
        for p in PRIMES:
            d = Dot(nline.n2p(p), color=PRIME, radius=0.09).shift(UP * 0.0)
            pdots.add(d)
        for d in pdots:
            self.play(FadeIn(d, scale=0.5), run_time=0.25)
        qmark = Text("?", font_size=40, color=SOFT).next_to(nline.n2p(30), UP, buff=0.2)
        self.play(FadeIn(qmark))
        narr = narrate(self,
            "Now look at where the primes actually fall. Two, three, a gap, five, seven, a bigger "
            "gap, eleven. They seem scattered, like raindrops landing on pavement with no steady beat. "
            "The higher you count, the rarer they get, but never in a neat way you can predict ahead of time. "
            "For a long time, finding a simple rule for the next prime looked hopeless.")
        clear_beat(self, h, nline, pdots, qmark, narr)

        # Beat 3: The Counting Staircase.
        h = headline(self, "A ragged staircase")
        axes = Axes(x_range=[0, 30, 5], y_range=[0, 11, 2], x_length=10, y_length=4.6,
                    axis_config={"include_numbers": True, "font_size": 20}).shift(DOWN * 0.2)
        xl = Text("count up to here", font_size=18, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.25)
        yl = Text("primes so far", font_size=18, color=SOFT).next_to(axes.y_axis, UP, buff=0.1)
        stair = prime_staircase(axes)
        self.play(Create(axes), FadeIn(xl), FadeIn(yl))
        self.play(Create(stair), run_time=3)
        narr = narrate(self,
            "So instead of asking where each prime lands, let's just count them. Walk along the "
            "numbers from left to right, and every time you pass a prime, take one step up. "
            "Two, step. Three, step. Five, step. What you draw is a staircase that keeps climbing. "
            "The steps come at uneven moments, so it climbs in a ragged, jumpy way. "
            "The whole mystery of the primes is really a question about the shape of this one staircase.")
        clear_beat(self, h, narr, xl, yl)

        # Beat 4: A Smooth Shadow (keep the staircase + axes from beat 3).
        h = headline(self, "The mystery is the wiggle")
        smooth = axes.plot(lambda x: x / np.log(x), x_range=[2, 30], color=ACCENT, stroke_width=4)
        smooth_lab = Text("smooth average", font_size=18, color=ACCENT).next_to(
            axes.c2p(30, 30 / np.log(30)), UP, buff=0.1).shift(LEFT * 1.2)
        self.play(Create(smooth), FadeIn(smooth_lab))
        narr = narrate(self,
            "Here is the first piece of magic. Zoom out, and that jagged staircase closely follows "
            "a smooth, graceful curve. A curve is just a gently bending line. The individual steps are "
            "unpredictable, but their overall shape is not. On average, we know roughly how fast the "
            "primes thin out, so the average is tame and well behaved. The real mystery is the wiggle: "
            "how far the true staircase is allowed to wander above and below that smooth curve.")
        clear_beat(self, h, axes, stair, smooth, smooth_lab, narr)


# ===========================================================================
# PART 2 - The Machine
# ===========================================================================
class Part2_Machine(Scene):
    def construct(self):
        part_title(self, "Part 2 - The Machine")

        # Beat 5: A Number Machine.
        h = headline(self, "A number machine")
        machine = make_machine("the machine").shift(DOWN * 0.2)
        self.play(FadeIn(machine))
        three = Text("3", font_size=36, color=PRIME).next_to(machine.box, UP, buff=0.9)
        self.play(FadeIn(three))
        self.play(three.animate.move_to(machine.box.get_center() + UP * 0.4).scale(0.6).set_opacity(0.2))
        out = Text("a number", font_size=28, color=ACCENT).next_to(machine.box, DOWN, buff=0.9)
        self.play(FadeIn(out, shift=DOWN * 0.3))
        narr = narrate(self,
            "To tame the wiggle, mathematicians built a special tool. Picture a box with a knob on "
            "the front. You feed a number in one side, and the box does some arithmetic and hands you "
            "a number back out the other side. That's the whole idea. Mathematicians have a fancy word "
            "for a machine like this. They call it a function. But really, it's just a box that turns "
            "one number into another.")
        clear_beat(self, h, machine, three, out, narr)

        # Beat 6: Inside the Machine.
        h = headline(self, "The pieces settle on a total")
        sum_tex = MathTex(r"\tfrac12 + \tfrac14 + \tfrac18 + \cdots", font_size=46).shift(UP * 1.6)
        nline = NumberLine(x_range=[0, 1, 0.25], length=9, include_numbers=True,
                           font_size=22).shift(DOWN * 0.4)
        target = Line(nline.n2p(1), nline.n2p(1) + UP * 0.5, color=PRIME, stroke_width=3)
        target_lab = Text("creeps up to 1, and stops", font_size=20, color=PRIME).next_to(
            nline.n2p(1), UP, buff=0.55).shift(LEFT * 1.6)
        self.play(Write(sum_tex), Create(nline))
        dot = Dot(nline.n2p(0), color=ACCENT, radius=0.1)
        self.play(FadeIn(dot), Create(target), FadeIn(target_lab))
        for frac in [0.5, 0.75, 0.875, 0.9375, 0.96875]:
            self.play(dot.animate.move_to(nline.n2p(frac)), run_time=0.6)
        narr = narrate(self,
            "Here is what is inside our machine. It adds up a never-ending list of fractions. "
            "A fraction is just a piece of a whole, like a half or a quarter. The knob controls how "
            "fast those fractions shrink as you go along the list. Turn it the right way, and the pieces "
            "get tiny so quickly that the whole endless sum settles on a single finite total instead of "
            "growing forever. A half plus a quarter plus an eighth, halving forever, creeps up toward "
            "one and stops there. That settled total is the number that comes out. "
            "Mathematicians call this machine the zeta function.")
        clear_beat(self, h, sum_tex, nline, dot, target, target_lab, narr)

        # Beat 7: The Secret Recipe.
        h = headline(self, "Same machine, two recipes")
        left = VGroup(
            Text("Recipe 1", font_size=22, color=SOFT),
            MathTex(r"\tfrac12 + \tfrac14 + \tfrac18 + \cdots", font_size=34),
            Text("(the endless sum)", font_size=18, color=SOFT),
        ).arrange(DOWN, buff=0.25).shift(LEFT * 3.4 + UP * 0.6)
        right = VGroup(
            Text("Recipe 2", font_size=22, color=SOFT),
            Text("2, 3, 5, 7, 11, ...", font_size=30, color=PRIME),
            Text("(only primes)", font_size=18, color=SOFT),
        ).arrange(DOWN, buff=0.25).shift(RIGHT * 3.4 + UP * 0.6)
        eq = MathTex(r"=", font_size=60).move_to((left.get_right() + right.get_left()) / 2)
        cake = Text("two recipes, the same cake", font_size=24, color=ACCENT).shift(DOWN * 2.2)
        self.play(FadeIn(left))
        self.play(Write(eq), FadeIn(right))
        self.play(FadeIn(cake, shift=UP * 0.2))
        narr = narrate(self,
            "Now the surprise that started everything. Long ago, a mathematician named Euler, whose "
            "name sounds like Oiler, discovered that this exact same machine can be rebuilt a completely "
            "different way, using only the prime numbers, combined in a special pattern. Two recipes, "
            "the endless sum and a recipe made purely of primes, always give the identical answer. "
            "Like two different recipes that bake the exact same cake. So this quiet adding machine "
            "secretly carries all the primes inside it. That is why studying the machine means "
            "studying the primes.")
        clear_beat(self, h, left, right, eq, cake, narr)


# ===========================================================================
# PART 3 - The Map and the Zeros
# ===========================================================================
class Part3_MapAndZeros(Scene):
    def make_map(self):
        plane = Axes(x_range=[0, 1, 0.5], y_range=[0, 30, 10], x_length=4.2, y_length=5.4,
                     axis_config={"include_numbers": True, "font_size": 18}).shift(LEFT * 2.6)
        xlab = Text("how far right", font_size=16, color=SOFT).next_to(plane.x_axis, DOWN, buff=0.2)
        ylab = Text("how far up", font_size=16, color=SOFT).next_to(plane.y_axis, UP, buff=0.1)
        return plane, VGroup(xlab, ylab)

    def construct(self):
        part_title(self, "Part 3 - The Map and the Zeros")

        # Beat 8: Inputs Become Map Points.
        h = headline(self, "Inputs as points on a map")
        plane, labs = self.make_map()
        self.play(Create(plane), FadeIn(labs))
        spot = plane.c2p(0.5, 18)
        ar_right = Arrow(plane.c2p(0, 0), plane.c2p(0.5, 0), color=ACCENT, buff=0, stroke_width=4)
        ar_up = Arrow(plane.c2p(0.5, 0), spot, color=ACCENT, buff=0, stroke_width=4)
        dot = Dot(spot, color=PRIME, radius=0.1)
        dot_lab = Text("one input", font_size=18, color=PRIME).next_to(dot, RIGHT, buff=0.15)
        self.play(GrowArrow(ar_right))
        self.play(GrowArrow(ar_up))
        self.play(FadeIn(dot, scale=0.5), FadeIn(dot_lab))
        narr = narrate(self,
            "To get the real power out of the machine, we feed it a richer kind of input. Instead of "
            "a single number on a line, picture a spot on a flat map. You go a little to the right, "
            "then a little up, and that pair of moves names a place, the way a square on a board game "
            "is named by how far across and how far up it sits. A two-part input like that is called a "
            "complex number. You don't need the details. Just picture the knob roaming a flat map, and "
            "for every spot, the machine still hands back one answer.")
        clear_beat(self, ar_right, ar_up, dot, dot_lab, narr)

        # Beat 9: What Is a Zero? (keep the map)
        h2 = headline(self, "A zero: the machine goes silent")
        self.play(FadeOut(h)); h = h2
        readout = VGroup(
            Text("answer:", font_size=20, color=SOFT),
            Text("0", font_size=40, color=WARN),
        ).arrange(RIGHT, buff=0.2).to_corner(UR, buff=0.8)
        zero_heights = [14, 21, 25]
        zeros = VGroup()
        probe = Dot(plane.c2p(0.5, 6), color=ACCENT, radius=0.08)
        self.play(FadeIn(probe), FadeIn(readout[0]))
        for zh in zero_heights:
            self.play(probe.animate.move_to(plane.c2p(0.5, zh)), run_time=0.7)
            z = Dot(plane.c2p(0.5, zh), color=WARN, radius=0.1)
            zeros.add(z)
            self.play(Flash(z, color=WARN, flash_radius=0.35), FadeIn(z),
                      FadeIn(readout[1]), run_time=0.5)
            self.play(FadeOut(readout[1]), run_time=0.2)
        narr = narrate(self,
            "Now we go hunting. At most spots on the map, the machine hands back some ordinary number. "
            "But at certain rare spots, the answer comes out as exactly zero. The machine goes completely "
            "silent. These silent spots are the heart of the whole mystery. Mathematicians call them the "
            "zeros of the machine. And it turns out these zeros are exactly what control the wiggle in "
            "our ragged prime staircase.")
        clear_beat(self, probe, readout[0], narr)

        # Beat 10: The Zeros Live in a Strip.
        h2 = headline(self, "They all hide in one strip")
        self.play(FadeOut(h)); h = h2
        strip = Rectangle(width=plane.c2p(1, 0)[0] - plane.c2p(0, 0)[0],
                          height=plane.c2p(0, 30)[1] - plane.c2p(0, 0)[1],
                          color=ACCENT, fill_opacity=0.12, stroke_width=2)
        strip.move_to((plane.c2p(0, 0) + plane.c2p(1, 30)) / 2)
        strip_lab = Text("one fenced lane", font_size=18, color=ACCENT).next_to(strip, RIGHT, buff=0.3)
        self.play(FadeIn(strip), FadeIn(strip_lab))
        more_zeros = VGroup(*[Dot(plane.c2p(0.5, zh), color=WARN, radius=0.1)
                              for zh in [9, 17]])
        self.play(LaggedStartMap(FadeIn, more_zeros, lag_ratio=0.3))
        narr = narrate(self,
            "When mathematicians marked these zero spots on the map, the interesting ones didn't scatter "
            "everywhere. They all fell inside one narrow up-and-down strip, like footprints found only "
            "within a single fenced-off lane. So the search shrinks. We no longer scan the whole map, "
            "just this one tall, thin band. And that already feels suspiciously orderly for something "
            "tied to the wild, random-looking primes.")
        zeros.add(*more_zeros)
        clear_beat(self, strip_lab, narr)

        # Beat 11: The Line Down the Middle.
        h2 = headline(self, "They sit on the center line")
        self.play(FadeOut(h)); h = h2
        center = Line(plane.c2p(0.5, 0), plane.c2p(0.5, 30), color=PRIME, stroke_width=4)
        center_lab = Text("the critical line", font_size=20, color=PRIME).next_to(
            plane.c2p(0.5, 30), UP, buff=0.15)
        half_lab = Text("exactly halfway across", font_size=16, color=SOFT).next_to(
            plane.c2p(0.5, 0), DOWN, buff=0.5)
        self.play(Create(center), FadeIn(center_lab), FadeIn(half_lab))
        self.play(*[Indicate(z, color=PRIME, scale_factor=1.3) for z in zeros])
        narr = narrate(self,
            "Here is the jaw-dropping part. Draw one perfectly straight up-and-down line right down the "
            "middle of that strip, exactly halfway between its two edges. Every single zero anyone has "
            "ever found, and we have checked many billions, sits balanced right on that line, like beads "
            "threaded on one perfectly straight wire. Not near it. On it. Mathematicians call this the "
            "critical line.")
        clear_beat(self, h, plane, labs, strip, zeros, center, center_lab, half_lab, narr)


# ===========================================================================
# PART 4 - The Hypothesis and Why It Matters
# ===========================================================================
class Part4_Hypothesis(Scene):
    def construct(self):
        part_title(self, "Part 4 - The Hypothesis, and Why It Matters")

        # Beat 12: The Riemann Hypothesis.
        h = headline(self, "The Riemann Hypothesis")
        wire = Line([0, -3.2, 0], [0, 3.0, 0], color=PRIME, stroke_width=4).shift(LEFT * 0.5)
        beads = VGroup(*[Dot([wire.get_x(), y, 0], color=WARN, radius=0.1)
                         for y in np.linspace(-2.8, 2.6, 11)])
        claim = VGroup(
            Text("EVERY zero is on the line", font_size=26, color=INK),
            Text("forever, no exception", font_size=22, color=SOFT),
            Text("(still unproven)", font_size=20, color=WARN),
        ).arrange(DOWN, buff=0.25).to_edge(RIGHT, buff=0.8)
        self.play(Create(wire))
        self.play(LaggedStartMap(FadeIn, beads, lag_ratio=0.12))
        self.play(FadeIn(claim))
        stray = beads[7]
        x_mark = Cross(stray, stroke_color=WARN, stroke_width=4).scale(1.4)
        q = Text("?", font_size=34, color=WARN).next_to(stray, RIGHT, buff=0.5)
        self.play(stray.animate.shift(RIGHT * 0.8), FadeIn(q))
        self.play(FadeIn(x_mark.move_to(stray)))
        self.play(FadeOut(x_mark), FadeOut(q), stray.animate.shift(LEFT * 0.8))
        narr = narrate(self,
            "And that is the Riemann Hypothesis. A hypothesis is just an educated guess that has not yet "
            "been proven. It is one bold claim: that every last one of these zeros, not just the billions "
            "we have checked but all of them, going on forever, sits exactly on that center line. "
            "No stragglers, no exceptions, ever. We have tested billions and they all obey. But checking "
            "a lot is not the same as proving it for every single one. Nobody has found an exception, and "
            "nobody has proven there couldn't be one. That gap is the whole problem.")
        clear_beat(self, h, wire, beads, claim, narr)

        # Beat 13: The Zeros Are Waves.
        h = headline(self, "The zeros are like sheet music")
        wax = Axes(x_range=[0, 6, 1], y_range=[-1.5, 1.5, 1], x_length=5, y_length=2.2,
                   axis_config={"stroke_width": 1}).shift(LEFT * 3.4 + UP * 0.3)
        w1 = wax.plot(lambda x: np.sin(2 * x), x_range=[0, 6], color=WAVE)
        w2 = wax.plot(lambda x: 0.6 * np.sin(3.3 * x), x_range=[0, 6], color=TEAL)
        w3 = wax.plot(lambda x: 0.4 * np.sin(5.1 * x), x_range=[0, 6], color=GREEN)
        waves = VGroup(w1, w2, w3)
        wlab = Text("each zero = one wave", font_size=18, color=SOFT).next_to(wax, DOWN, buff=0.2)
        sax = Axes(x_range=[0, 30, 10], y_range=[0, 11, 5], x_length=5, y_length=2.6,
                   axis_config={"stroke_width": 1, "include_numbers": False}).shift(RIGHT * 3.2 + UP * 0.3)
        stair = prime_staircase(sax)
        slab = Text("the prime staircase", font_size=18, color=PRIME).next_to(sax, DOWN, buff=0.2)
        arrow = Arrow(wax.get_right(), sax.get_left(), color=INK, buff=0.3)
        addlab = Text("add them up", font_size=18, color=ACCENT).next_to(arrow, UP, buff=0.1)
        self.play(Create(wax), LaggedStartMap(Create, waves, lag_ratio=0.3), FadeIn(wlab))
        self.play(GrowArrow(arrow), FadeIn(addlab))
        self.play(Create(sax), Create(stair), FadeIn(slab))
        narr = narrate(self,
            "So why does anyone care? Remember the wiggle in our staircase. Each of those zeros acts like "
            "a single gentle wave on water. And when you add all those waves together, they reproduce the "
            "ragged prime staircase exactly, step for step. The zeros are like the sheet music, and the "
            "primes are like the song it plays. So where the zeros sit isn't a curiosity. It sets the "
            "deepest rhythm of the primes.")
        clear_beat(self, h, wax, waves, wlab, sax, stair, slab, arrow, addlab, narr)

        # Beat 14: On the Line Means No Wobble.
        h = headline(self, "On the line means no wobble")
        # top: on the line, steady beat
        top_line = Line([-1, 1.6, 0], [-1, 3.0, 0], color=PRIME, stroke_width=3)
        top_beads = VGroup(*[Dot([-1, y, 0], color=WARN, radius=0.07) for y in np.linspace(1.7, 2.9, 5)])
        top_ticks = VGroup(*[Line([x, 1.2, 0], [x, 1.5, 0], color=ACCENT, stroke_width=3)
                             for x in np.linspace(0.5, 5.5, 8)])
        top_lab = Text("zeros on the line -> steady, even primes", font_size=18, color=ACCENT)
        top_lab.move_to([2.2, 2.4, 0])
        # bottom: off the line, wobble
        bot_line = Line([-1, -3.0, 0], [-1, -1.6, 0], color=PRIME, stroke_width=3)
        bot_beads = VGroup(*[Dot([-1, y, 0], color=WARN, radius=0.07) for y in np.linspace(-2.9, -1.7, 5)])
        bot_beads[2].shift(RIGHT * 0.7)  # one off the line
        bunch_x = [0.5, 0.9, 1.2, 2.6, 2.9, 4.4, 5.2, 5.5]
        bot_ticks = VGroup(*[Line([x, -1.5, 0], [x, -1.2, 0], color=WARN, stroke_width=3) for x in bunch_x])
        bot_lab = Text("one zero off -> a hidden clumping", font_size=18, color=WARN)
        bot_lab.move_to([2.2, -2.4, 0])
        divider = DashedLine([-6, 0, 0], [6, 0, 0], color=SOFT, stroke_opacity=0.4)
        self.play(Create(divider))
        self.play(Create(top_line), FadeIn(top_beads), Create(top_ticks), FadeIn(top_lab))
        self.play(Create(bot_line), FadeIn(bot_beads), Create(bot_ticks), FadeIn(bot_lab))
        narr = narrate(self,
            "Now the stakes are clear. If every zero sits dead on the center line, the waves stay "
            "perfectly balanced, and the primes are spread out as smoothly and evenly as they could "
            "ever possibly be, like a steady, well-tuned drumbeat. But if even one zero slipped off the "
            "line, it would mean a hidden wobble in that rhythm, a secret clump or gap in the primes. "
            "So the Riemann Hypothesis is really a promise that the primes hold their beat with no wobble.")
        clear_beat(self, h, divider, top_line, top_beads, top_ticks, top_lab,
                   bot_line, bot_beads, bot_ticks, bot_lab, narr)

        # Beat 15: Still Open, Still Chased.
        h = headline(self, "Open for over 160 years")
        mountain = Polygon([-2, -2.5, 0], [0, 2.2, 0], [2, -2.5, 0], color=SOFT, stroke_width=3)
        cloud = Ellipse(width=2.2, height=0.8, color=SOFT, fill_opacity=0.25).move_to([0, 2.0, 0])
        flag_pole = Line([-0.5, -0.3, 0], [-0.5, 0.4, 0], color=INK, stroke_width=3)
        flag = Polygon([-0.5, 0.4, 0], [-0.5, 0.1, 0], [-0.05, 0.25, 0], color=WARN, fill_opacity=1)
        flag_lab = Text("we are here", font_size=16, color=INK).next_to(flag, RIGHT, buff=0.2)
        year = Text("written down in 1859", font_size=24, color=ACCENT).to_edge(DOWN, buff=2.6)
        self.play(Create(mountain), FadeIn(cloud))
        self.play(Create(flag_pole), FadeIn(flag), FadeIn(flag_lab))
        self.play(FadeIn(year))
        narr = narrate(self,
            "Riemann wrote this down back in 1859, and more than a hundred and sixty years later, no one "
            "has proven it, and no one has found a single zero off the line either. It is one of the most "
            "famous unsolved problems in all of mathematics. But it isn't a locked door. It's a summit, "
            "and people are still climbing toward it, one careful step at a time. And now you know what "
            "they are reaching for, and why a few quiet dots on a map could hold the deepest secret of "
            "the numbers themselves.")
        self.play(FadeOut(year))
        end = Text("What is the Riemann Hypothesis?", font_size=34, color=INK)
        self.play(FadeOut(h), FadeOut(mountain), FadeOut(cloud), FadeOut(flag_pole),
                  FadeOut(flag), FadeOut(flag_lab), FadeOut(narr))
        self.play(Write(end))
        self.wait(2)
        self.play(FadeOut(end))
