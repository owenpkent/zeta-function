"""
FunctionalEquation
==================
Graduate course on the Riemann Hypothesis, Episode 2: The Functional Equation.

Rigorously derives the completed zeta function and its symmetry:
    Lambda(s) = pi^{-s/2} Gamma(s/2) zeta(s) = Mellin transform of psi,
    theta(1/x) = sqrt(x) theta(x)  (Jacobi, via Poisson summation),
    Lambda(s) = -1/s - 1/(1-s) + int_1^inf psi(x)(x^{s/2-1} + x^{(1-s)/2-1}) dx,
    Lambda(s) = Lambda(1-s),  xi(s) = (1/2)s(s-1)Lambda(s) entire,  xi(s) = xi(1-s),
    zeta(s) = 2^s pi^{s-1} sin(pi s/2) Gamma(1-s) zeta(1-s).

Audience: graduate (complex analysis, Poisson summation, the Gamma function).
The full narration also appears as on-screen subtitles. Script: NARRATION.md.

Five scenes (render and concatenate):
    manim -qm visualizations/13_functional_equation/functional_equation.py Ep2_Part1_Destination
    manim -qm visualizations/13_functional_equation/functional_equation.py Ep2_Part2_GammaFactor
    manim -qm visualizations/13_functional_equation/functional_equation.py Ep2_Part3_Theta
    manim -qm visualizations/13_functional_equation/functional_equation.py Ep2_Part4_Symmetric
    manim -qm visualizations/13_functional_equation/functional_equation.py Ep2_Part5_Harvest

Part 1 is a ThreeDScene (the |zeta| terrain). The rest are 2D equation scenes.
"""

import re
from manim import *
import numpy as np


# --- palette ----------------------------------------------------------------
INK = WHITE
ACCENT = TEAL
CRIT = YELLOW
POLE = ORANGE
ZERO = RED
REGION = BLUE
SOFT = GREY_B
GOOD = GREEN

KNOWN_ZEROS_T = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]


# --- zeta helpers (terrain height only; copied from scene 09) ----------------
def eta_approx(s, N=80):
    total = complex(0, 0)
    for n in range(1, N + 1):
        total += ((-1) ** (n + 1)) / (n ** s)
    return total


def zeta_approx(s, N=80):
    if abs(s - 1) < 0.05:
        return complex(10, 0)
    eta = eta_approx(s, N)
    denom = 1 - 2 ** (1 - s)
    if abs(denom) < 1e-10:
        return complex(10, 0)
    return eta / denom


def psi_val(x, N=40):
    return sum(np.exp(-np.pi * n * n * x) for n in range(1, N + 1))


# --- text / subtitle helpers ------------------------------------------------
def wrap(text, width=10):
    words = text.split()
    return "\n".join(" ".join(words[i:i + width]) for i in range(0, len(words), width))


def split_sentences(text):
    return [p for p in re.split(r"(?<=[.?!])\s+", text.strip()) if p]


def reading_time(sentence):
    return max(2.4, len(sentence.split()) * 0.32)


def part_title(scene, main, sub=None, fixed=False):
    grp = VGroup(Text(main, font_size=40, color=INK))
    if sub:
        grp.add(Text(sub, font_size=26, color=ACCENT))
    grp.arrange(DOWN, buff=0.35)
    if fixed:
        scene.add_fixed_in_frame_mobjects(grp)
    scene.play(FadeIn(grp, shift=UP * 0.2))
    scene.wait(1.5)
    scene.play(FadeOut(grp))


def headline(scene, line, color=INK, fixed=False):
    h = Text(line, font_size=28, color=color).to_edge(UP, buff=0.55)
    if fixed:
        scene.add_fixed_in_frame_mobjects(h)
    scene.play(FadeIn(h, shift=DOWN * 0.2), run_time=0.5)
    return h


def narrate(scene, narration, fixed=False, fs=23):
    prev = None
    for s in split_sentences(narration):
        txt = Text(wrap(s, 10), font_size=fs, color=INK, line_spacing=0.9)
        if txt.width > 12.6:
            txt.scale_to_fit_width(12.6)
        txt.to_edge(DOWN, buff=0.4)
        bg = BackgroundRectangle(txt, color=BLACK, fill_opacity=0.6, buff=0.18)
        sub = VGroup(bg, txt)
        if fixed:
            scene.add_fixed_in_frame_mobjects(sub)
        if prev is None:
            scene.play(FadeIn(sub), run_time=0.45)
        else:
            scene.play(FadeOut(prev, run_time=0.22), FadeIn(sub, run_time=0.32))
        scene.wait(reading_time(s))
        prev = sub
    return prev


def clear_beat(scene, *mobjects):
    movers = [m for m in mobjects if m is not None]
    if movers:
        scene.play(*[FadeOut(m) for m in movers])


def math_beat(scene, head_text, math_lines, narration, labels=None,
              math_scale=0.9, stagger=True):
    """Generic equation beat: headline + stacked MathTex + subtitle narration."""
    h = headline(scene, head_text)
    group = VGroup(*[MathTex(m) for m in math_lines]).arrange(DOWN, buff=0.42)
    group.scale(math_scale)
    if group.width > 12.2:
        group.scale_to_fit_width(12.2)
    if group.height > 3.6:
        group.scale_to_fit_height(3.6)
    group.move_to(UP * 0.7)
    if stagger:
        for m in group:
            scene.play(Write(m), run_time=0.9)
    else:
        scene.play(Write(group))
    lab = None
    if labels:
        lab = VGroup(*[Text(t, font_size=17, color=SOFT) for t in labels])
        lab.arrange(DOWN, aligned_edge=LEFT, buff=0.14).to_corner(UL, buff=0.4).shift(DOWN * 0.7)
        scene.play(FadeIn(lab))
    narr = narrate(scene, narration)
    clear_beat(scene, h, group, lab, narr)


# ===========================================================================
# PART 1 - The Theorem First (3D terrain destination + recap)
# ===========================================================================
class Ep2_Part1_Destination(ThreeDScene):
    def construct(self):
        part_title(self, "The Riemann Hypothesis, Episode 2",
                   "The Functional Equation", fixed=True)

        # Beat: the destination, seen as the zeta landscape and its mirror.
        self.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES, zoom=0.7)
        axes = ThreeDAxes(
            x_range=[-0.3, 1.5, 0.5], y_range=[0, 35, 5], z_range=[0, 4, 1],
            x_length=6, y_length=8, z_length=4,
        )
        xl = axes.get_x_axis_label(r"\sigma")
        yl = axes.get_y_axis_label(r"t")
        zl = axes.get_z_axis_label(r"|\zeta|")
        self.play(Create(axes), Write(xl), Write(yl), Write(zl))

        def mag(sigma, t):
            try:
                return min(abs(zeta_approx(complex(sigma, t), N=50)), 4.0)
            except Exception:
                return 0.0

        surf = Surface(lambda u, v: axes.c2p(u, v, mag(u, v)),
                       u_range=[-0.2, 1.4], v_range=[1, 34], resolution=(32, 50),
                       fill_opacity=0.7)
        surf.set_fill_by_value(axes=axes, colorscale=[
            (BLUE_E, 0), (BLUE, 0.5), (TEAL, 1.0), (GREEN, 1.5), (YELLOW, 2.5), (RED, 4.0)], axis=2)
        self.play(Create(surf), run_time=3)

        # the critical line and the zeros as dips
        crit_pts = [axes.c2p(0.5, t, mag(0.5, t)) for t in np.linspace(1, 34, 140)]
        crit = VMobject(color=CRIT, stroke_width=4).set_points_smoothly(crit_pts)
        zeros = VGroup(*[Dot3D(axes.c2p(0.5, t0, 0), color=ZERO, radius=0.08) for t0 in KNOWN_ZEROS_T])
        pole = Line3D(axes.c2p(1, 0, 0), axes.c2p(1, 0, 3.8), color=POLE, thickness=0.02)
        self.play(Create(crit), LaggedStartMap(FadeIn, zeros, lag_ratio=0.2), Create(pole))

        # the mirror plane at Re = 1/2
        mirror = Polygon(
            axes.c2p(0.5, 1, 0), axes.c2p(0.5, 34, 0), axes.c2p(0.5, 34, 4), axes.c2p(0.5, 1, 4),
            color=CRIT, fill_opacity=0.12, stroke_width=1)
        self.play(FadeIn(mirror))

        thm = VGroup(
            MathTex(r"\xi(s)=\tfrac12\,s(s-1)\,\pi^{-s/2}\Gamma\!\left(\tfrac s2\right)\zeta(s)").scale(0.7),
            MathTex(r"\xi(s)=\xi(1-s)", color=CRIT).scale(0.8),
        ).arrange(DOWN, buff=0.25).to_corner(UL, buff=0.4)
        self.add_fixed_in_frame_mobjects(thm)
        narr = narrate(self,
            "Here is where this episode lands. The zeta function, defined by a series only for real "
            "part of s greater than one, extends to a meromorphic function on the whole plane. After "
            "multiplying by the right Gamma factor and a quadratic, we get an entire function, xi of s, "
            "perfectly symmetric under s going to one minus s. The pole sits at s equals one, the "
            "nontrivial zeros lie in the strip, and the functional equation forces them to be symmetric "
            "across the line real part one half. We will prove all of this exactly.", fixed=True)
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(surf), FadeOut(crit), FadeOut(zeros), FadeOut(pole), FadeOut(mirror),
                  FadeOut(axes), FadeOut(xl), FadeOut(yl), FadeOut(zl), FadeOut(thm), FadeOut(narr))
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=1)

        # Beat: what we start from (recap), now in 2D.
        head = Text("What we start from (given)", font_size=28, color=INK).to_edge(UP, buff=0.55)
        self.add_fixed_in_frame_mobjects(head)
        self.play(FadeIn(head))
        recap = VGroup(
            MathTex(r"\zeta(s)=\sum_{n=1}^{\infty} n^{-s}, \quad \operatorname{Re}(s)>1"),
            MathTex(r"\zeta(s)=\prod_{p}\left(1-p^{-s}\right)^{-1}"),
            MathTex(r"\operatorname{Res}_{s=1}\,\zeta(s)=1"),
        ).arrange(DOWN, buff=0.45).scale(0.95).move_to(UP * 0.6)
        self.add_fixed_in_frame_mobjects(recap)
        for m in recap:
            self.play(Write(m), run_time=0.9)
        narr = narrate(self,
            "We take three facts as given from the previous episode. The Dirichlet series converges "
            "absolutely for real part greater than one. There it equals the Euler product over primes, "
            "which already shows zeta has no zeros in that half-plane. And zeta has a simple pole at s "
            "equals one with residue one. The series and the product are useless past real part one, so "
            "we need a genuinely new representation that continues zeta and exposes the symmetry.", fixed=True)
        self.play(FadeOut(head), FadeOut(recap), FadeOut(narr))


# ===========================================================================
# PART 2 - The Gamma Factor Completes Zeta
# ===========================================================================
class Ep2_Part2_GammaFactor(Scene):
    def construct(self):
        part_title(self, "Part II", "The Gamma Factor Completes Zeta")

        math_beat(self, "One Gaussian integral per term",
            [r"\Gamma\!\left(\tfrac s2\right)=\int_0^{\infty} t^{\,s/2-1} e^{-t}\,dt",
             r"t=\pi n^2 x",
             r"\pi^{-s/2}\Gamma\!\left(\tfrac s2\right) n^{-s}=\int_0^{\infty} x^{\,s/2-1} e^{-\pi n^2 x}\,dx"],
            "The whole proof begins with one substitution. In the integral for Gamma of s over two, "
            "replace t by pi n squared x. The measure dt over t is scale invariant, so it becomes dx "
            "over x, and the rest pulls out pi n squared to the s over two. Rearranging, pi to the minus "
            "s over two times Gamma of s over two times n to the minus s equals the integral of x to the "
            "s over two minus one times e to the minus pi n squared x. Each term of zeta now carries a "
            "Gaussian integral, and the Gamma and pi factors are forced on us, not decoration.",
            labels=["Substitute t = pi n^2 x", "n^{-s} appears on the left"])

        math_beat(self, "Sum over n: the completed zeta",
            [r"\psi(x):=\sum_{n=1}^{\infty} e^{-\pi n^2 x}",
             r"\Lambda(s):=\pi^{-s/2}\Gamma\!\left(\tfrac s2\right)\zeta(s)",
             r"\Lambda(s)=\int_0^{\infty} x^{\,s/2-1}\,\psi(x)\,dx \quad (\operatorname{Re}(s)>1)"],
            "Now sum over all n at least one. On the left the terms assemble into pi to the minus s over "
            "two, Gamma of s over two, times zeta of s. We call this the completed zeta function, capital "
            "Lambda. On the right the sum of the Gaussians defines psi of x, the half theta function. "
            "Interchanging sum and integral is legal here, because for real part above one the integrand "
            "is positive and the iterated integral is finite, so Tonelli applies. The completed zeta is "
            "exactly the Mellin transform of psi.",
            labels=["Define psi and Lambda", "Tonelli: integrand >= 0", "Lambda = Mellin transform of psi"])

        # Custom visual: the behavior of psi.
        h = headline(self, "All the trouble lives near x = 0")
        ax = Axes(x_range=[0, 2.2, 0.5], y_range=[0, 3, 1], x_length=9, y_length=4.2,
                  axis_config={"include_numbers": True, "font_size": 20}).move_to(UP * 0.3)
        axl = MathTex(r"\psi(x)").scale(0.7).next_to(ax.y_axis, UP, buff=0.1)
        curve = ax.plot(lambda x: min(psi_val(x), 3.0), x_range=[0.06, 2.2, 0.02], color=ACCENT)
        env = ax.plot(lambda x: min(np.exp(-np.pi * x), 3.0), x_range=[0.5, 2.2, 0.02],
                      color=GOOD, stroke_width=2)
        cut = DashedLine(ax.c2p(1, 0), ax.c2p(1, 3), color=SOFT, stroke_opacity=0.6)
        danger = Text("blows up at 0", font_size=18, color=ZERO).next_to(ax.c2p(0.15, 3), RIGHT, buff=0.1)
        tame = Text("decays like e^{-pi x}", font_size=18, color=GOOD).next_to(ax.c2p(1.5, 0.4), UP, buff=0.2)
        self.play(Create(ax), Write(axl))
        self.play(Create(curve))
        self.play(Create(env), FadeIn(tame), FadeIn(danger), Create(cut))
        narr = narrate(self,
            "Look at the two ends. As x goes to infinity, psi is dominated by its first term and decays "
            "like e to the minus pi x, faster than any power, so the tail from one to infinity converges "
            "for every s and is already entire. All the analytic difficulty lives at the other end, near "
            "x equal to zero, where psi blows up. To control that end we need to know exactly how psi "
            "behaves as x goes to zero, and that is what the theta function will give us.")
        clear_beat(self, h, ax, axl, curve, env, cut, danger, tame, narr)


# ===========================================================================
# PART 3 - Theta and Its Modular Symmetry (the engine)
# ===========================================================================
class Ep2_Part3_Theta(Scene):
    def construct(self):
        part_title(self, "Part III", "Theta and Its Modular Symmetry")

        math_beat(self, "Pass to the full lattice sum",
            [r"\theta(x)=\sum_{n\in\mathbb{Z}} e^{-\pi n^2 x}=1+2\,\psi(x)",
             r"\sum_{n\in\mathbb{Z}} f(n)=\sum_{k\in\mathbb{Z}} \hat f(k)",
             r"\hat f(k)=\int_{\mathbb{R}} f(y)\,e^{-2\pi i k y}\,dy"],
            "Extend the sum to all integers and add the n equals zero term. That is the Jacobi theta "
            "function, theta of x, equal to one plus two psi of x. Because the summand depends only on "
            "n squared, the negative terms double the positive ones and n equals zero contributes a lone "
            "one. Theta is a sum over the integer lattice, and the master tool for such sums is Poisson "
            "summation: the sum of f over the integers equals the sum of its Fourier transform over the "
            "integers. We apply it to the Gaussian f of y equal to e to the minus pi x y squared.",
            labels=["theta = 1 + 2 psi", "Tool: Poisson summation"])

        # Custom visual: Gaussian self-duality and the modular law.
        h = headline(self, "The Gaussian is its own Fourier transform")
        ax = Axes(x_range=[-3, 3, 1], y_range=[0, 1.4, 0.5], x_length=8, y_length=2.6,
                  axis_config={"stroke_width": 1.5}).move_to(UP * 0.9)
        xval = 3.0
        narrow = ax.plot(lambda y: np.exp(-np.pi * xval * y * y), x_range=[-3, 3], color=ACCENT)
        wide = ax.plot(lambda y: (1 / np.sqrt(xval)) * np.exp(-np.pi * y * y / xval),
                       x_range=[-3, 3], color=POLE)
        nlab = MathTex(r"e^{-\pi x y^2}", color=ACCENT).scale(0.6).next_to(ax.c2p(0.5, 1.2), RIGHT)
        wlab = MathTex(r"\tfrac{1}{\sqrt{x}}\,e^{-\pi k^2/x}", color=POLE).scale(0.6).next_to(ax.c2p(2, 0.45), UR)
        law = MathTex(r"\theta\!\left(\tfrac1x\right)=\sqrt{x}\,\theta(x)", color=CRIT).scale(1.1)
        law.to_edge(DOWN, buff=2.4)
        self.play(Create(ax))
        self.play(Create(narrow), Write(nlab))
        self.play(Create(wide), Write(wlab))
        self.play(Write(law))
        narr = narrate(self,
            "The Fourier transform of e to the minus pi x y squared is one over root x times e to the "
            "minus pi k squared over x. This is the one computation that makes everything work: the "
            "Gaussian is essentially its own transform, with x inverted to one over x and an amplitude "
            "root x out front. Feeding this into Poisson summation gives the modular law: theta of one "
            "over x equals root x times theta of x. The width inverts, narrow maps to wide, and this "
            "single law is the entire source of the symmetry we are after.")
        clear_beat(self, h, ax, narrow, wide, nlab, wlab, law, narr)

        math_beat(self, "Translate the law to psi",
            [r"1+2\psi\!\left(\tfrac1x\right)=\sqrt{x}\,\big(1+2\psi(x)\big)",
             r"\psi\!\left(\tfrac1x\right)=-\tfrac12+\tfrac12\sqrt{x}+\sqrt{x}\,\psi(x)"],
            "Restate the law in terms of psi, since psi is what appears in Lambda. Substitute theta "
            "equals one plus two psi on both sides and solve for psi of one over x. It equals minus one "
            "half, plus one half root x, plus root x times psi of x. Watch those two extra elementary "
            "terms, the minus one half and the one half root x. They come from the lone n equals zero "
            "term in theta, and they are exactly the algebra that will produce the two poles of Lambda.",
            labels=["Solve for psi(1/x)", "The two extra terms become the poles"])


# ===========================================================================
# PART 4 - The Symmetric Representation (continuation for free)
# ===========================================================================
class Ep2_Part4_Symmetric(Scene):
    def construct(self):
        part_title(self, "Part IV", "The Symmetric Representation")

        math_beat(self, "Split at x = 1 and fold (0,1) over",
            [r"\Lambda(s)=\int_0^1 x^{\,s/2-1}\psi(x)\,dx+\int_1^{\infty} x^{\,s/2-1}\psi(x)\,dx",
             r"x\mapsto \tfrac1x,\qquad \tfrac{dx}{x}\ \text{invariant}",
             r"\int_0^1 x^{\,s/2-1}\psi(x)\,dx=\int_1^{\infty} x^{-s/2-1}\,\psi\!\left(\tfrac1x\right)dx"],
            "Split the Mellin integral at x equals one. The tail from one to infinity is already entire, "
            "so leave it. In the dangerous piece from zero to one, substitute x to one over x. The "
            "interval flips to one to infinity, the measure picks up the right power of x, and crucially "
            "psi of x becomes psi of one over x, where we can now feed in the modular law. This single "
            "substitution converts the divergent end into a convergent one.",
            labels=["Cut at x = 1", "On (0,1) substitute x -> 1/x"])

        math_beat(self, "Insert the theta law; two terms integrate",
            [r"\int_1^{\infty}\! x^{-s/2-1}\!\left(-\tfrac12+\tfrac12 x^{1/2}+x^{1/2}\psi(x)\right)dx",
             r"\int_1^{\infty}\!-\tfrac12 x^{-s/2-1}dx=-\tfrac1s\ (\operatorname{Re}s>0),\ \ \int_1^{\infty}\!\tfrac12 x^{-(s+1)/2}dx=-\tfrac{1}{1-s}\ (\operatorname{Re}s>1)",
             r"x^{1/2}\psi(x)\cdot x^{-s/2-1}=\psi(x)\,x^{(1-s)/2-1}"],
            "Substitute the expression for psi of one over x. Three terms appear, all integrals over one "
            "to infinity. The constant minus one half integrates to minus one over s, for real part "
            "positive. The one half root x term integrates to minus one over one minus s, for real part "
            "greater than one. These are the only elementary integrals, and they are exactly where the "
            "two poles come from. The remaining term gives psi of x times x to the one minus s over two "
            "minus one. Notice the exponent: the substitution has sent s to one minus s. Every piece "
            "converges together on real part greater than one, where we performed the split.",
            labels=["Three terms over [1, infinity)", "Closed forms -1/s and -1/(1-s)", "The psi term sends s -> 1-s"],
            math_scale=0.8)

        math_beat(self, "Riemann's symmetric formula: continuation for free",
            [r"\Lambda(s)=-\frac1s-\frac{1}{1-s}+\int_1^{\infty}\!\psi(x)\left(x^{\,s/2-1}+x^{\,(1-s)/2-1}\right)dx",
             r"\psi(x)=O(e^{-\pi x})\ (x\to\infty)\ \Rightarrow\ \text{integral entire}",
             r"\Lambda\ \text{meromorphic on }\mathbb{C},\ \text{poles only at }s=0,1"],
            "Assemble the pieces. Lambda of s equals minus one over s, minus one over one minus s, plus "
            "the integral from one to infinity of psi times the quantity x to the s over two minus one "
            "plus x to the one minus s over two minus one. We derived this for real part greater than "
            "one, but now read the right side on its own. Because psi decays like e to the minus pi x, "
            "that integral converges for every complex s and is entire. The two fractions are "
            "meromorphic with poles only at zero and one. By analytic continuation the right side equals "
            "Lambda everywhere. We have continued the completed zeta to all of C, essentially for free.",
            labels=["Riemann's symmetric formula", "Derived on Re(s)>1, then everywhere"],
            math_scale=0.82)

        math_beat(self, "The symmetry is now manifest",
            [r"s\;\longmapsto\;1-s",
             r"-\tfrac1s-\tfrac1{1-s}\ \text{ and }\ x^{s/2-1}+x^{(1-s)/2-1}\ \text{ are invariant}",
             r"\Lambda(s)=\Lambda(1-s)"],
            "Now the payoff. Send s to one minus s in the symmetric representation. The pair of fractions "
            "swaps with itself. Inside the integral, the two powers of x interchange, so the integrand is "
            "unchanged. Every single term is invariant. Therefore Lambda of s equals Lambda of one minus "
            "s. The functional equation is not a coincidence checked afterward: it is manifest in a "
            "representation we built symmetrically from the theta law. The mirror at real part one half "
            "was there all along.",
            labels=["Swap s <-> 1-s", "Every term is fixed"])


# ===========================================================================
# PART 5 - Harvest: xi, the Asymmetric Form, and the Zeros
# ===========================================================================
class Ep2_Part5_Harvest(Scene):
    def construct(self):
        part_title(self, "Part V", "Harvest: xi, the Asymmetric Form, the Zeros")

        math_beat(self, "Clearing the poles: the entire function xi",
            [r"\xi(s):=\tfrac12\,s(s-1)\,\Lambda(s)=\tfrac12\,s(s-1)\,\pi^{-s/2}\Gamma\!\left(\tfrac s2\right)\zeta(s)",
             r"\xi\ \text{is entire}\qquad \xi(s)=\xi(1-s)"],
            "Lambda has two simple poles, at zero and one. Multiply by one half times s times s minus "
            "one, which vanishes at exactly those two points and cancels both poles. Define xi of s to be "
            "one half s times s minus one times Lambda. Then xi is entire. The prefactor is itself "
            "invariant under s to one minus s, since s minus one maps to minus s, so xi inherits the "
            "symmetry exactly: xi of s equals xi of one minus s. This is the clean object promised at the "
            "start: a single entire function with a perfect functional equation.",
            labels=["Multiply by (1/2)s(s-1)", "Kills both poles", "xi entire and symmetric"])

        math_beat(self, "The asymmetric functional equation",
            [r"\pi^{-s/2}\Gamma\!\left(\tfrac s2\right)\zeta(s)=\pi^{-(1-s)/2}\Gamma\!\left(\tfrac{1-s}{2}\right)\zeta(1-s)",
             r"\zeta(s)=2^{s}\pi^{\,s-1}\sin\!\left(\tfrac{\pi s}{2}\right)\Gamma(1-s)\,\zeta(1-s)"],
            "Unpack Lambda of s equals Lambda of one minus s into the zeta variables. Solving for zeta of "
            "s, and using the Legendre duplication formula and the reflection formula for Gamma to "
            "simplify the ratio of Gamma factors, gives the classical asymmetric form: zeta of s equals "
            "two to the s, times pi to the s minus one, times sine of pi s over two, times Gamma of one "
            "minus s, times zeta of one minus s. The two faces carry the same content, but the "
            "asymmetric form makes the consequences for the zeros immediate.",
            labels=["Use Gamma duplication + reflection", "The sin factor drives the trivial zeros"])

        math_beat(self, "Trivial zeros and the pole, read off",
            [r"\sin\!\left(\tfrac{\pi s}{2}\right)=0\ \text{at}\ s=-2,-4,-6,\dots\Rightarrow \zeta(s)=0",
             r"\Gamma\!\left(\tfrac s2\right):\ \text{poles at } s=0,-2,-4,\dots;\quad \zeta(0)=-\tfrac12\neq 0",
             r"\zeta\ \text{has its only pole at }s=1"],
            "Read the asymmetric equation at the negative even integers. There the sine factor vanishes "
            "while the other factors are finite and nonzero, forcing zeta to vanish. These are the "
            "trivial zeros at minus two, minus four, minus six, and on. Equivalently, Gamma of s over two "
            "has poles at zero and the negative even integers; at the strictly negative ones zeta must "
            "carry compensating zeros, the trivial ones. At s equals zero the story differs: there the "
            "Gamma pole is matched by Lambda's own pole, and zeta of zero is minus one half, not zero. "
            "The lone pole of zeta at s equals one matches the s equals one pole of Lambda.",
            labels=["Trivial zeros at -2, -4, -6, ...", "s = 0 is NOT a zero", "Only pole at s = 1"],
            math_scale=0.85)

        # Final beat: the critical strip and RH, with the reflection quartet.
        h = headline(self, "The critical strip, and the Riemann Hypothesis")
        plane = Axes(x_range=[-0.5, 1.5, 0.5], y_range=[-30, 30, 10], x_length=5.6, y_length=5.2,
                     axis_config={"include_numbers": True, "font_size": 18}).shift(LEFT * 2.6 + DOWN * 0.2)
        strip = Rectangle(width=plane.c2p(1, 0)[0] - plane.c2p(0, 0)[0],
                          height=plane.c2p(0, 30)[1] - plane.c2p(0, -30)[1],
                          color=REGION, fill_opacity=0.12, stroke_width=0)
        strip.move_to((plane.c2p(0, -30) + plane.c2p(1, 30)) / 2)
        critline = DashedLine(plane.c2p(0.5, -30), plane.c2p(0.5, 30), color=CRIT, stroke_width=3)
        cl_lab = MathTex(r"\operatorname{Re}=\tfrac12", color=CRIT).scale(0.55).next_to(plane.c2p(0.5, 30), UP, buff=0.1)
        beta = 0.74
        quartet = VGroup(
            Dot(plane.c2p(beta, 17), color=ZERO, radius=0.08),
            Dot(plane.c2p(1 - beta, 17), color=ZERO, radius=0.08),
            Dot(plane.c2p(beta, -17), color=ZERO, radius=0.08),
            Dot(plane.c2p(1 - beta, -17), color=ZERO, radius=0.08),
        )
        rect = VGroup(
            DashedLine(plane.c2p(beta, 17), plane.c2p(1 - beta, 17), color=ZERO, stroke_opacity=0.6),
            DashedLine(plane.c2p(beta, -17), plane.c2p(1 - beta, -17), color=ZERO, stroke_opacity=0.6),
            DashedLine(plane.c2p(beta, 17), plane.c2p(beta, -17), color=ZERO, stroke_opacity=0.6),
            DashedLine(plane.c2p(1 - beta, 17), plane.c2p(1 - beta, -17), color=ZERO, stroke_opacity=0.6),
        )
        rh = VGroup(
            MathTex(r"\rho,\ 1-\rho,\ \overline{\rho},\ 1-\overline{\rho}", color=ZERO).scale(0.6),
            Text("all zeros: symmetric about Re = 1/2", font_size=18, color=SOFT),
            MathTex(r"\textbf{RH:}\ \ \operatorname{Re}(\rho)=\tfrac12", color=CRIT).scale(0.8),
        ).arrange(DOWN, buff=0.3).to_edge(RIGHT, buff=0.6)
        self.play(Create(plane), FadeIn(strip), Create(critline), Write(cl_lab))
        self.play(LaggedStartMap(FadeIn, quartet, lag_ratio=0.2), Create(rect))
        self.play(Write(rh[0]), Write(rh[1]))
        narr = narrate(self,
            "Now isolate the remaining zeros. The Euler product gives none for real part above one, and "
            "the functional equation reflects that below zero, leaving only the trivial ones outside. So "
            "every nontrivial zero sits in the closed strip, real part between zero and one. Ruling out "
            "the two boundary lines needs one more input, the nonvanishing of zeta on real part equal to "
            "one, which we prove in Episode five. The symmetry xi of s equals xi of one minus s pairs "
            "each zero rho with one minus rho, and real coefficients pair rho with its conjugate, so the "
            "four points form a rectangle symmetric about the line real part one half.")
        # collapse the quartet onto the line
        onto = VGroup(Dot(plane.c2p(0.5, 17), color=ZERO, radius=0.08),
                      Dot(plane.c2p(0.5, -17), color=ZERO, radius=0.08))
        self.play(Write(rh[2]))
        self.play(Transform(quartet, VGroup(onto[0], onto[0].copy(), onto[1], onto[1].copy())),
                  FadeOut(rect))
        narr2 = narrate(self,
            "The Riemann Hypothesis is the assertion that this enforced symmetry is achieved on the nose: "
            "every nontrivial zero already sits on the critical line, real part exactly one half. We have "
            "proved the functional equation that frames the problem. Whether the zeros truly lie on the "
            "line is the open question this whole course exists to confront.")
        clear_beat(self, h, plane, strip, critline, cl_lab, quartet, rh, narr2)
        end = VGroup(
            Text("Episode 2: The Functional Equation", font_size=30, color=INK),
            MathTex(r"\xi(s)=\xi(1-s)", color=CRIT).scale(1.1),
        ).arrange(DOWN, buff=0.4)
        self.play(Write(end))
        self.wait(2)
        self.play(FadeOut(end))
