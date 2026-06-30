"""
ThreeStageRH
============
The three-stage RH picture as one hall of machines. Stage A builds RH from the
zeta terrain down to beads on the critical line. Stage B funnels four proof roads
into one neck (realization is free, the signature is the open half). Stage C opens
the one empty socket: the missing global indefinite (1, n-1) polarization over
Spec(Z) (M4, the arithmetic Hodge standard conjecture). Supplying it is RH.

Render each Scene separately and concatenate. ThreeDScene only for the terrain
(Stage A) and the saddle (Stage C); everything else is 2D VMobjects.

Faithfulness note: zeta_approx and eta_approx (copied from scene 09) drive the
Stage A terrain HEIGHT only. The pole at s = 1 is finite-capped in those helpers
and the visual is capped at min(val, 4.0). The explicit-formula wave curve in A6
does NOT call those helpers; it is a schematic partial sum. Trivial zeros at
-2, -4, -6 are intentionally out of frame: the story lives in the critical strip.

Render commands (from repo root):
    manim -qm visualizations/11_three_stage_rh/three_stage_rh.py StageA_WaterThenBeads
    manim -qm visualizations/11_three_stage_rh/three_stage_rh.py StageB_Watershed
    manim -qm visualizations/11_three_stage_rh/three_stage_rh.py StageC_EmptySocket
    manim -qm visualizations/11_three_stage_rh/three_stage_rh.py Close_MasterImage
"""

from manim import *
import numpy as np


# ---------------------------------------------------------------------------
# Helpers copied verbatim from scene 09 (terrain HEIGHT only).
# ---------------------------------------------------------------------------
def eta_approx(s, N=80):
    """Dirichlet eta function approximation (converges for Re(s) > 0)."""
    total = complex(0, 0)
    for n in range(1, N + 1):
        total += ((-1) ** (n + 1)) / (n ** s)
    return total


def zeta_approx(s, N=80):
    """Approximate zeta(s) via eta(s) / (1 - 2^{1-s}). Pole is finite-capped."""
    if abs(s - 1) < 0.05:
        return complex(10, 0)  # pole
    eta = eta_approx(s, N)
    denom = 1 - 2 ** (1 - s)
    if abs(denom) < 1e-10:
        return complex(10, 0)
    return eta / denom


# Copied from scene 07 (10 entries).
KNOWN_ZEROS_T = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
]


# ---------------------------------------------------------------------------
# Semantic palette (single source of truth for the whole piece).
# ---------------------------------------------------------------------------
C_VISIBLE = WHITE        # solid, on-screen, "what you can see"
C_INVISIBLE = GREY_B     # ghost / fogged / the one missing object
C_REALIZATION = GREEN    # realization half, free, on-line, perfect pairing
C_SIGNATURE = RED        # signature half, open, off-line, the saddle "down"
C_CRITLINE = YELLOW      # critical line, the FE mirror, the neck
C_LEVEL3 = BLUE          # Level 3, the realization half, the bowl reject
C_DH = "#C2185B"         # Davenport-Heilbronn (the impostor color)
C_POLE = ORANGE          # the s = 1 pole spike (residue 1)
C_UP_AXIS = GREEN        # the single ample / up direction of the saddle
C_DOWN_AXIS = RED        # the orthogonal down directions of the saddle
C_FOG = GREY             # open / unknown overlay fill


# ---------------------------------------------------------------------------
# Persistent-frame and reusable helpers.
# ---------------------------------------------------------------------------
def make_gear_socket(color=C_INVISIBLE, outer=0.22, inner=0.12):
    """Empty gear-shaped socket, drawn as an unfilled annulus (cheap stand-in)."""
    return Annulus(
        inner_radius=inner, outer_radius=outer,
        color=color, fill_opacity=0.0, stroke_width=3,
    )


def make_machine_icon(label_text, scale=1.0):
    """A machine: a body fed by primes, emitting a zero strip, with one socket."""
    body = RoundedRectangle(
        corner_radius=0.08, width=1.0, height=0.8,
        color=C_VISIBLE, stroke_width=2,
    )
    feed = VGroup(*[Dot(radius=0.02, color=C_POLE) for _ in range(4)])
    feed.arrange(DOWN, buff=0.05).next_to(body, LEFT, buff=0.05)
    strip = VGroup(*[Dot(radius=0.02, color=C_REALIZATION) for _ in range(5)])
    strip.arrange(DOWN, buff=0.05).next_to(body, RIGHT, buff=0.05)
    socket = make_gear_socket(outer=0.16, inner=0.08).move_to(body.get_center())
    label = Text(label_text, font_size=11, color=C_VISIBLE).next_to(body, DOWN, buff=0.06)
    icon = VGroup(body, feed, strip, socket, label)
    icon.body = body
    icon.socket = socket
    icon.scale(scale)
    return icon


def make_master_thumb(highlight=None):
    """Top-right thumbnail: a row of machines, a funnel, and an empty socket."""
    machines = VGroup(*[
        RoundedRectangle(corner_radius=0.04, width=0.22, height=0.18,
                         color=C_VISIBLE, stroke_width=1.5)
        for _ in range(3)
    ]).arrange(RIGHT, buff=0.05)
    funnel = Triangle(color=C_CRITLINE, stroke_width=1.5).scale(0.16).rotate(PI)
    socket = make_gear_socket(outer=0.11, inner=0.05)
    group = VGroup(machines, funnel, socket).arrange(RIGHT, buff=0.12)
    group.machines = machines
    group.funnel = funnel
    group.socket = socket
    dim = 0.3
    if highlight == "machines":
        funnel.set_opacity(dim); socket.set_stroke(opacity=dim)
    elif highlight == "funnel":
        machines.set_opacity(dim); socket.set_stroke(opacity=dim)
    elif highlight == "socket":
        machines.set_opacity(dim); funnel.set_opacity(dim)
    group.scale(0.95).to_corner(UR, buff=0.25)
    return group


def make_tracker():
    """Bottom-left two-column tracker: VISIBLE vs THE ONE INVISIBLE THING."""
    head_v = Text("WHAT YOU CAN SEE", font_size=15, color=C_VISIBLE)
    head_i = Text("THE ONE INVISIBLE THING", font_size=15, color=C_INVISIBLE)
    col_v = VGroup(VectorizedPoint(head_v.get_corner(DL)))
    col_i = VGroup(VectorizedPoint(head_i.get_corner(DL)))
    head_v.col = col_v
    head_i.col = col_i
    block_v = VGroup(head_v)
    block_i = VGroup(head_i)
    tracker = VGroup(block_v, block_i).arrange(DOWN, aligned_edge=LEFT, buff=1.1)
    tracker.head_v = head_v
    tracker.head_i = head_i
    tracker.col_v = col_v
    tracker.col_i = col_i
    tracker.scale(0.85).to_corner(DL, buff=0.3).shift(UP * 0.4)
    return tracker


def add_track(scene, tracker, text, which="v", threeD=False):
    """Append a small bullet under the chosen column header, with a fade-in."""
    if which == "v":
        col, head, color = tracker.col_v, tracker.head_v, C_VISIBLE
    else:
        col, head, color = tracker.col_i, tracker.head_i, C_INVISIBLE
    anchor = col[-1] if len(col) > 1 else head
    bullet = Text("- " + text, font_size=11, color=color)
    bullet.next_to(anchor, DOWN, aligned_edge=LEFT, buff=0.06)
    col.add(bullet)
    if threeD:
        scene.add_fixed_in_frame_mobjects(bullet)
    scene.play(FadeIn(bullet, shift=RIGHT * 0.06), run_time=0.4)


def show_caption(scene, text, threeD=False, edge=DOWN, color=C_VISIBLE, fs=18):
    """A short multi-line caption (use \\n in text). Returns the mobject."""
    cap = Text(text, font_size=fs, color=color, line_spacing=0.85)
    if cap.width > 11.5:
        cap.scale_to_fit_width(11.5)
    cap.to_edge(edge, buff=0.3)
    if threeD:
        scene.add_fixed_in_frame_mobjects(cap)
    scene.play(FadeIn(cap), run_time=0.6)
    return cap


def make_bead_wire(heights, color=C_REALIZATION, x=0.0,
                   y_lo=-3.0, y_hi=3.0, t_lo=10.0, t_hi=52.0, radius=0.07):
    """A vertical wire at x with beads placed by height (t -> y mapping)."""
    wire = Line([x, y_lo, 0], [x, y_hi, 0], color=C_CRITLINE, stroke_width=3)
    beads = VGroup()
    for t in heights:
        y = y_lo + (y_hi - y_lo) * (t - t_lo) / (t_hi - t_lo)
        beads.add(Dot([x, y, 0], color=color, radius=radius))
    return wire, beads


def make_road(start, neck, color_left=C_REALIZATION, color_right=C_SIGNATURE, width=8):
    """A road from start to neck, split into a green left half and red right half."""
    start = np.array(start, dtype=float)
    neck = np.array(neck, dtype=float)
    mid = (start + neck) / 2
    left = Line(start, mid, color=color_left, stroke_width=width)
    right = Line(mid, neck, color=color_right, stroke_width=width)
    road = VGroup(left, right)
    road.left = left
    road.right = right
    return road


def make_bar(x, height, base_y=-1.0, width=0.32, color=C_LEVEL3):
    """A bar standing on base_y, signed: positive up, negative below the baseline."""
    bar = Rectangle(width=width, height=max(abs(height), 1e-3),
                    fill_opacity=0.85, color=color, stroke_width=1)
    bar.move_to([x, base_y + height / 2.0, 0])
    return bar


# ===========================================================================
# STAGE A: RH from scratch (water then beads).
# ===========================================================================
class StageA_WaterThenBeads(ThreeDScene):
    def construct(self):
        thumb = make_master_thumb(highlight="machines")
        tracker = make_tracker()

        # Beat A1: title and persistent frame.
        title = Title(r"Stage A: From the Zeta Terrain to the Beads")
        self.add_fixed_in_frame_mobjects(title, thumb, tracker)
        self.play(Write(title), FadeIn(thumb), FadeIn(tracker))
        self.wait(1)
        self.play(FadeOut(title))
        self.remove(title)

        # Beat A2: the terrain (drain-holes and capped pole).
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES, zoom=0.7)
        axes = ThreeDAxes(
            x_range=[-0.5, 1.5, 0.5], y_range=[0, 35, 5], z_range=[0, 4, 1],
            x_length=6, y_length=8, z_length=4,
        )
        x_label = axes.get_x_axis_label(r"\sigma")
        y_label = axes.get_y_axis_label(r"t")
        z_label = axes.get_z_axis_label(r"|\zeta|")
        self.play(Create(axes), Write(x_label), Write(y_label), Write(z_label))

        def zeta_magnitude(sigma, t):
            try:
                return min(abs(zeta_approx(complex(sigma, t), N=60)), 4.0)
            except Exception:
                return 0.0

        surface = Surface(
            lambda u, v: axes.c2p(u, v, zeta_magnitude(u, v)),
            u_range=[-0.3, 1.4], v_range=[1, 34],
            resolution=(32, 50), fill_opacity=0.7,
        )
        surface.set_fill_by_value(
            axes=axes,
            colorscale=[(BLUE_E, 0), (BLUE, 0.5), (TEAL, 1.0),
                        (GREEN, 1.5), (YELLOW, 2.5), (RED, 4.0)],
            axis=2,
        )
        self.play(Create(surface), run_time=3)

        crit_pts = [axes.c2p(0.5, t, zeta_magnitude(0.5, t)) for t in np.linspace(1, 34, 160)]
        crit_curve = VMobject(color=C_CRITLINE, stroke_width=4).set_points_smoothly(crit_pts)
        self.play(Create(crit_curve), run_time=2)

        zero_dots = VGroup(*[
            Dot3D(axes.c2p(0.5, t0, 0), color=C_SIGNATURE, radius=0.08)
            for t0 in KNOWN_ZEROS_T[:5]
        ])
        self.play(LaggedStartMap(FadeIn, zero_dots, lag_ratio=0.2))

        pole = Line3D(axes.c2p(1, 0, 0), axes.c2p(1, 0, 3.8),
                      color=C_POLE, thickness=0.02)
        pole_label = Text("pole at s = 1, residue 1", font_size=16, color=C_POLE)
        pole_label.to_corner(UR, buff=0.25).shift(DOWN * 0.7)
        self.add_fixed_in_frame_mobjects(pole_label)
        self.play(Create(pole), Write(pole_label))

        cap = show_caption(
            self,
            "Height is the size of zeta.\n"
            "Zeros are drain-holes (height 0) on sigma = 1/2.\n"
            "The pole at s = 1 is one spike (capped so it does not flatten the rest).",
            threeD=True,
        )
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        add_track(self, tracker, "the terrain, the zeros, the pole", "v", threeD=True)
        self.play(FadeOut(cap))

        # Beat A3: why zeta is special (Euler product).
        euler = VGroup(
            MathTex(r"\zeta(s)=\sum_{n\ge 1} n^{-s}=\prod_p (1-p^{-s})^{-1}\quad(\sigma>1)"),
            MathTex(r"\text{equal by unique factorization}"),
        ).arrange(DOWN, buff=0.2).scale(0.6).to_edge(UP, buff=1.2)
        self.add_fixed_in_frame_mobjects(euler)
        cap = show_caption(
            self,
            "The series and the Euler product agree for sigma greater than 1.\n"
            "That equality (unique factorization) is what fakes lack.",
            threeD=True,
        )
        self.play(Write(euler))
        self.wait(1.5)
        add_track(self, tracker, "the Euler product", "v", threeD=True)
        self.play(FadeOut(euler), FadeOut(cap), FadeOut(pole_label))
        self.remove(pole_label)

        # Beat A4: flatten, then three symmetries and the off-line quartet.
        self.move_camera(phi=0, theta=-90 * DEGREES, zoom=0.9, run_time=2)
        self.play(FadeOut(surface), FadeOut(axes), FadeOut(crit_curve),
                  FadeOut(zero_dots), FadeOut(pole),
                  FadeOut(x_label), FadeOut(y_label), FadeOut(z_label))

        plane = Axes(
            x_range=[-0.3, 1.3, 0.5], y_range=[-55, 55, 20],
            x_length=6, y_length=6.4,
            axis_config={"stroke_width": 1.5, "include_numbers": True},
            x_axis_config={"numbers_to_include": [0, 0.5, 1]},
        ).shift(LEFT * 0.6 + DOWN * 0.2)
        mirror = Line(plane.c2p(0.5, -55), plane.c2p(0.5, 55), color=C_CRITLINE, stroke_width=4)
        mirror_glow = Line(plane.c2p(0.5, -55), plane.c2p(0.5, 55), color=C_CRITLINE,
                           stroke_width=12, stroke_opacity=0.15)
        conj_axis = DashedLine(plane.c2p(-0.3, 0), plane.c2p(1.3, 0), color=C_CRITLINE,
                               stroke_width=2, stroke_opacity=0.6)
        self.play(Create(plane), Create(mirror_glow), Create(mirror), Create(conj_axis))

        beta, tt = 0.7, 20.0
        quartet = VGroup(
            Dot(plane.c2p(beta, tt), color=C_SIGNATURE, radius=0.09),
            Dot(plane.c2p(1 - beta, tt), color=C_SIGNATURE, radius=0.09),
            Dot(plane.c2p(beta, -tt), color=C_SIGNATURE, radius=0.09),
            Dot(plane.c2p(1 - beta, -tt), color=C_SIGNATURE, radius=0.09),
        )
        rect = DashedLine(plane.c2p(beta, tt), plane.c2p(1 - beta, tt), color=C_SIGNATURE)
        rect2 = VGroup(
            DashedLine(plane.c2p(beta, tt), plane.c2p(beta, -tt), color=C_SIGNATURE),
            DashedLine(plane.c2p(1 - beta, tt), plane.c2p(1 - beta, -tt), color=C_SIGNATURE),
            DashedLine(plane.c2p(beta, -tt), plane.c2p(1 - beta, -tt), color=C_SIGNATURE),
            rect,
        )
        labels = VGroup(
            MathTex(r"\rho \to 1-\rho", color=C_CRITLINE).scale(0.6),
            MathTex(r"\rho \to \bar\rho", color=C_CRITLINE).scale(0.6),
            MathTex(r"\text{RH: coincide on } \sigma=\tfrac12", color=C_CRITLINE).scale(0.6),
        ).arrange(DOWN, buff=0.18).to_corner(UR, buff=0.4)
        self.play(LaggedStartMap(FadeIn, quartet, lag_ratio=0.3), Create(rect2))
        self.play(Write(labels))
        cap = show_caption(
            self,
            "Three symmetries compound: the functional equation (rho to 1 minus rho),\n"
            "conjugation (rho to conjugate rho), and RH (they coincide on the line).\n"
            "One off-line zero is forced into a quartet of four.",
        )
        # Collapse the quartet onto the line.
        on_line = VGroup(Dot(plane.c2p(0.5, tt), color=C_REALIZATION, radius=0.09),
                         Dot(plane.c2p(0.5, -tt), color=C_REALIZATION, radius=0.09))
        self.play(Transform(quartet, VGroup(on_line[0], on_line[0].copy(),
                                            on_line[1], on_line[1].copy())),
                  FadeOut(rect2))
        add_track(self, tracker, "the symmetries, the quartet", "v")
        self.wait(1)
        self.play(FadeOut(labels), FadeOut(cap), FadeOut(quartet))

        # Beat A5: collapse to beads on a wire.
        wire, beads = make_bead_wire(KNOWN_ZEROS_T, x=plane.c2p(0.5, 0)[0])
        density = MathTex(r"\text{density near } T:\ \tfrac{1}{2\pi}\log\!\big(\tfrac{T}{2\pi}\big)").scale(0.6)
        density.to_corner(UR, buff=0.4)
        self.play(ReplacementTransform(VGroup(plane, mirror_glow, conj_axis), wire),
                  Transform(mirror, wire.copy()))
        self.play(LaggedStartMap(FadeIn, beads, lag_ratio=0.25), Write(density))
        cap = show_caption(
            self,
            "Redraw the zeros as beads on one wire at sigma = 1/2,\n"
            "at heights 14.13, 21.02, 25.01, 30.42, 32.94, and on.\n"
            "That promotion (every bead exactly on the wire) is the hypothesis.",
        )
        add_track(self, tracker, "the beads on the wire", "v")
        self.wait(1.5)
        self.play(FadeOut(cap), FadeOut(density), FadeOut(beads),
                  FadeOut(wire), FadeOut(mirror))

        # Beat A6: the explicit formula (schematic wave sum).
        ax6 = Axes(
            x_range=[2, 30, 7], y_range=[0, 12, 4],
            x_length=8, y_length=3.2,
            axis_config={"stroke_width": 1.5, "include_numbers": True},
        ).to_edge(DOWN, buff=0.9)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        stair_pts = [ax6.c2p(2, 0)]
        count = 0
        for p in primes:
            stair_pts.append(ax6.c2p(p, count))
            count += 1
            stair_pts.append(ax6.c2p(p, count))
        stair_pts.append(ax6.c2p(30, count))
        staircase = VMobject(color=C_VISIBLE, stroke_width=3).set_points_as_corners(stair_pts)

        t1, t2, t3 = KNOWN_ZEROS_T[0], KNOWN_ZEROS_T[1], KNOWN_ZEROS_T[2]

        def partial(k):
            ts = [t1, t2, t3][:k]
            def f(x):
                base = 3.2
                wave = sum(np.sqrt(x) * np.cos(t * np.log(x)) for t in ts)
                return base + 0.18 * wave
            return ax6.plot(f, x_range=[2, 30], color=C_REALIZATION)

        formula = MathTex(r"\pi(x)=\mathrm{Li}(x)-\sum_\rho \mathrm{Li}(x^\rho)-\cdots").scale(0.7)
        formula.to_edge(UP, buff=0.6)
        self.play(Write(formula), Create(ax6))
        psum = partial(1)
        self.play(Create(staircase), FadeIn(psum))
        for k in (2, 3):
            nxt = partial(k)
            self.play(ReplacementTransform(psum, nxt))
            psum = nxt
        cap = show_caption(
            self,
            "Each zero is a wave correcting the prime staircase.\n"
            "Height t is the frequency, the real part sigma is the amplitude.\n"
            "At sigma = 1/2 every wave is balanced at the square root of x.",
            edge=DOWN, fs=16,
        )
        add_track(self, tracker, "the explicit-formula waves", "v")
        add_track(self, tracker, "zeros sit EXACTLY on the line (a knife-edge)", "i")
        self.wait(2)
        self.play(*[FadeOut(m) for m in [formula, ax6, staircase, psum, cap]])
        self.wait(0.5)


# ===========================================================================
# STAGE B: All roads converge (watershed funnel).
# ===========================================================================
class StageB_Watershed(Scene):
    def construct(self):
        thumb = make_master_thumb(highlight="funnel")
        tracker = make_tracker()

        # Beat B1: title and frame.
        title = Title(r"Stage B: Four Roads, One Neck")
        self.add(thumb, tracker)
        self.play(Write(title), FadeIn(thumb), FadeIn(tracker))
        self.wait(0.8)
        self.play(FadeOut(title))

        # Beat B2: four roads converging to the neck.
        neck_pt = [3.2, 0.2, 0]
        neck = Dot(neck_pt, color=C_CRITLINE, radius=0.12)
        starts = [[-5.5, y, 0] for y in (2.4, 0.9, -0.6, -2.1)]
        names = [
            "1 Spectral (Hilbert-Polya)",
            "2 Arithmetic-geometric (Deninger / F_1)",
            "3 Direct positivity (Weil / Li)",
            "4 Analytic (zero-free)",
        ]
        roads = VGroup(*[make_road(s, neck_pt) for s in starts])
        road_labels = VGroup(*[
            Text(n, font_size=15, color=C_VISIBLE).next_to(roads[i].left.get_start(), RIGHT, buff=0.1)
            for i, n in enumerate(names)
        ])
        self.play(LaggedStartMap(Create, roads, lag_ratio=0.4),
                  LaggedStartMap(FadeIn, road_labels, lag_ratio=0.4))
        self.play(FadeIn(neck))
        cap = show_caption(
            self,
            "Four roads. Each splits into a left half (REALIZATION: zeta as a trace,\n"
            "often a theorem) and a right half (the SIGNATURE: one positivity\n"
            "statement, the same object every road, open over Z).",
        )
        add_track(self, tracker, "the roads, the realization halves", "v")
        add_track(self, tracker, "the SIGNATURE half, open over Z", "i")
        self.wait(1.5)
        self.play(FadeOut(cap))

        # Beat B3: the neck, right halves collapse to one point.
        rights = VGroup(*[r.right for r in roads])
        merge_text = MathTex(r"\text{one positivity, every road}", color=C_SIGNATURE).scale(0.7)
        merge_text.next_to(neck, UP, buff=0.3)
        self.play(*[ReplacementTransform(r, neck.copy()) for r in rights])
        self.play(Flash(neck, color=C_SIGNATURE, flash_radius=0.5), Write(merge_text))
        cap = show_caption(self, "The right halves are one statement. They collapse to a single neck.")
        self.wait(1.2)
        self.play(FadeOut(cap), FadeOut(merge_text))

        # Beat B4: the Davenport-Heilbronn tollgate.
        gate_x = 0.2
        posts = VGroup(
            Line([gate_x, 3.0, 0], [gate_x, 0.4, 0], color=C_DH, stroke_width=3),
            Line([gate_x, -0.4, 0], [gate_x, -3.0, 0], color=C_DH, stroke_width=3),
        )
        gate_label = Text("Davenport-Heilbronn tollgate", font_size=15, color=C_DH)
        gate_label.next_to(posts, UP, buff=0.1).shift(RIGHT * 0.3)
        # Road 2 detour arc around the gate.
        detour = ArcBetweenPoints([gate_x - 1.2, 0.9, 0], [gate_x + 1.2, 0.6, 0],
                                  angle=-PI / 2, color=C_REALIZATION, stroke_width=8)
        barrier = Line([2.3, 0.2, 0], [2.3, -0.6, 0], color=C_SIGNATURE, stroke_width=4)
        cap23 = MathTex(r"\text{capped at } 2/3", color=C_SIGNATURE).scale(0.5).next_to(barrier, DOWN, buff=0.1)
        verdicts = VGroup(
            Text("1: trace, not signature", font_size=13, color=C_VISIBLE),
            Text("2: unique escape (a polarization)", font_size=13, color=C_REALIZATION),
            Text("3: marginal positivity", font_size=13, color=C_VISIBLE),
            Text("4: capped at 2/3", font_size=13, color=C_VISIBLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_corner(DR, buff=0.4)
        self.play(Create(posts), Write(gate_label))
        self.play(Create(detour), Create(barrier), Write(cap23))
        self.play(LaggedStartMap(FadeIn, verdicts, lag_ratio=0.3))
        cap = show_caption(
            self,
            "Roads 1, 3, 4 must pass the Davenport-Heilbronn tollgate (no Euler product,\n"
            "off-line zeros near 0.8085 plus 85.7 i). Road 2 routes around it: it needs\n"
            "the Euler product D-H lacks. Road 4 only grazes the neck, capped at 2/3.",
            fs=16,
        )
        add_track(self, tracker, "the tollgate, the road-2 escape", "v")
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [cap, posts, gate_label, detour, barrier,
                                         cap23, verdicts, roads, road_labels, neck,
                                         *[r.right for r in []]]])

        # Beat B5: the Level 3 vs Level 4 altitude cut.
        base_y = -1.2
        baseline = Line([-5, base_y, 0], [5, base_y, 0], color=C_VISIBLE, stroke_width=2)
        lvl3 = DashedLine([-5, base_y + 1.6, 0], [5, base_y + 1.6, 0], color=C_LEVEL3, stroke_width=2)
        lvl4 = DashedLine([-5, base_y + 2.4, 0], [5, base_y + 2.4, 0], color=C_SIGNATURE, stroke_width=2)
        lvl3_lab = Text("Level 3 (tolerates)", font_size=14, color=C_LEVEL3).next_to(lvl3, RIGHT, buff=0.1).shift(LEFT*0.2+UP*0.15)
        lvl4_lab = Text("Level 4 (forbids)", font_size=14, color=C_SIGNATURE).next_to(lvl4, RIGHT, buff=0.1).shift(LEFT*0.2+UP*0.15)
        vals = [1.2, 0.8, 1.4, 1.0, 0.6, 1.3, 0.9]
        xs = np.linspace(-3.5, 3.5, len(vals))
        bars = VGroup(*[make_bar(x, v, base_y=base_y, color=C_REALIZATION) for x, v in zip(xs, vals)])
        rogue_i = 4
        self.play(Create(baseline), Create(lvl3), Create(lvl4),
                  Write(lvl3_lab), Write(lvl4_lab))
        self.play(LaggedStartMap(GrowFromEdge, bars, edge=DOWN, lag_ratio=0.1))
        # First pass at Level 3: dip, no alarm.
        dip3 = make_bar(xs[rogue_i], -0.5, base_y=base_y, color=C_LEVEL3)
        cap = show_caption(self, "Level 3 tolerates a rogue zero at beta = 0.51 as a local ripple.")
        self.play(Transform(bars[rogue_i], dip3))
        self.wait(1)
        self.play(FadeOut(cap))
        # Second pass at Level 4: the same dip fires the alarm.
        alarm_box = SurroundingRectangle(bars[rogue_i], color=C_SIGNATURE, buff=0.05)
        alarm_text = Text("ALARM", font_size=22, color=C_SIGNATURE).next_to(bars[rogue_i], DOWN, buff=0.2)
        cap = show_caption(
            self,
            "Level 4 (positivity) forbids it: an eigenvalue dips below 0 and the alarm fires.\n"
            "Note: Level 4 equals positivity is a finding (about 80/20), not a theorem.",
            fs=16,
        )
        self.play(Indicate(bars[rogue_i], color=C_SIGNATURE),
                  Flash(bars[rogue_i].get_bottom(), color=C_SIGNATURE),
                  Create(alarm_box), Write(alarm_text))
        add_track(self, tracker, "the altitude cut, the alarm", "v")
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [cap, baseline, lvl3, lvl4, lvl3_lab, lvl4_lab,
                                         bars, alarm_box, alarm_text]])
        self.wait(0.5)


# ===========================================================================
# STAGE C: The empty socket (the saddle and the missing gear).
# ===========================================================================
class StageC_EmptySocket(ThreeDScene):
    def construct(self):
        thumb = make_master_thumb(highlight="socket")
        tracker = make_tracker()
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        # Beat C1: title and frame.
        title = Title(r"Stage C: The One Empty Socket")
        self.add_fixed_in_frame_mobjects(title, thumb, tracker)
        self.play(Write(title), FadeIn(thumb), FadeIn(tracker))
        self.wait(0.8)
        self.play(FadeOut(title))
        self.remove(title)

        # Beat C2: perfect pairing for free, then the demand.
        pair = MathTex(r"\rho \to 1-\rho", color=C_REALIZATION).scale(0.9)
        pair_note = Text("perfect, non-degenerate, free from the FE", font_size=16, color=C_REALIZATION)
        demand = MathTex(r"\text{RH: } 1-\rho=\bar\rho \iff \mathrm{Re}=\tfrac12", color=C_SIGNATURE).scale(0.9)
        grp = VGroup(pair, pair_note, demand).arrange(DOWN, buff=0.35)
        arrow = Arrow(pair_note.get_bottom(), demand.get_top(), color=C_VISIBLE, buff=0.1)
        self.add_fixed_in_frame_mobjects(grp, arrow)
        self.play(Write(pair), FadeIn(pair_note))
        self.play(Create(arrow), Write(demand))
        cap = show_caption(
            self,
            "The pairing rho to 1 minus rho is perfect for free (even D-H has it).\n"
            "RH demands it equal conjugation: 1 minus rho equals conjugate rho when\n"
            "Re = 1/2. That demand is a polarization (a positivity).",
            threeD=True, fs=16,
        )
        add_track(self, tracker, "the perfect pairing (free)", "v", threeD=True)
        self.wait(1.5)
        self.play(FadeOut(grp), FadeOut(arrow), FadeOut(cap))
        self.remove(grp, arrow)

        # Beat C3: the saddle (1, n-1) versus the rejected bowl (3D insert).
        axes3 = ThreeDAxes(x_range=[-2, 2, 1], y_range=[-2, 2, 1], z_range=[-4, 4, 2],
                           x_length=4.5, y_length=4.5, z_length=4)
        bowl = Surface(lambda u, v: axes3.c2p(u, v, u**2 + v**2),
                       u_range=[-2, 2], v_range=[-2, 2], resolution=(20, 20),
                       fill_opacity=0.7, checkerboard_colors=[C_LEVEL3, BLUE_E])
        saddle = Surface(lambda u, v: axes3.c2p(u, v, u**2 - v**2),
                         u_range=[-2, 2], v_range=[-2, 2], resolution=(24, 24),
                         fill_opacity=0.7)
        saddle.set_fill_by_value(axes=axes3,
                                 colorscale=[(C_LEVEL3, -4), (WHITE, 0), (C_SIGNATURE, 4)], axis=2)
        up_arrow = Arrow3D(axes3.c2p(0, 0, 0), axes3.c2p(1.8, 0, 3.2), color=C_UP_AXIS)
        down_arrows = VGroup(
            Arrow3D(axes3.c2p(0, 0, 0), axes3.c2p(0, 1.8, -3.2), color=C_DOWN_AXIS),
            Arrow3D(axes3.c2p(0, 0, 0), axes3.c2p(0, -1.8, -3.2), color=C_DOWN_AXIS),
        )
        sig_label = MathTex(r"(1,\,n-1)").scale(0.9).to_corner(UL, buff=0.6)
        self.add_fixed_in_frame_mobjects(sig_label)
        cap = show_caption(
            self,
            "The signature is a saddle, not an all-positive bowl. One up-axis\n"
            "(the ample, Euler-pole class), every orthogonal axis down. All-positive\n"
            "(Lee-Yang) is the wrong object. The (1, n-1) count pins every zero to the line.",
            threeD=True, fs=16,
        )
        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=1.5,
                         added_anims=[Create(axes3)])
        self.play(Create(bowl))
        self.wait(0.6)
        self.play(ReplacementTransform(bowl, saddle))
        self.play(Create(up_arrow), LaggedStartMap(Create, down_arrows, lag_ratio=0.3),
                  Write(sig_label))
        self.wait(1.2)
        add_track(self, tracker, "the saddle, the one up-axis", "v", threeD=True)
        add_track(self, tracker, "the missing polarization over Spec(Z)", "i", threeD=True)
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=1.5,
                         added_anims=[FadeOut(saddle), FadeOut(up_arrow),
                                      FadeOut(down_arrows), FadeOut(axes3)])
        self.play(FadeOut(cap), FadeOut(sig_label))
        self.remove(sig_label)

        # Beat C4: two transparencies over the pairing matrix.
        matrix = Matrix([[r"1", r"\bar\rho"], [r"\rho", r"1"]]).scale(0.8).shift(LEFT * 3)
        perfect = Rectangle(width=2.2, height=2.0, color=C_REALIZATION,
                            fill_opacity=0.85).move_to(matrix)
        perfect_lab = VGroup(
            Text("PERFECTNESS", font_size=16, color=C_VISIBLE),
            Text("(free, in Mathlib: riemannZeta_one_sub)", font_size=12, color=C_VISIBLE),
        ).arrange(DOWN, buff=0.1).next_to(perfect, RIGHT, buff=0.5).shift(UP * 0.8)
        positivity = Rectangle(width=2.2, height=2.0, color=C_FOG,
                               fill_opacity=0.4).move_to(matrix).shift(UP * 0.12 + RIGHT * 0.12)
        q = MathTex(r"?", color=C_SIGNATURE).scale(1.4).move_to(positivity)
        positivity_lab = VGroup(
            Text("POSITIVITY sign-pattern (fogged)", font_size=16, color=C_INVISIBLE),
            Text("arithmetic Hodge standard conjecture = M4 = open", font_size=12, color=C_INVISIBLE),
        ).arrange(DOWN, buff=0.1).next_to(perfect, RIGHT, buff=0.5).shift(DOWN * 0.8)
        self.play(Create(matrix))
        self.play(FadeIn(perfect), Write(perfect_lab))
        self.play(FadeIn(positivity), FadeIn(q), Write(positivity_lab))
        cap = show_caption(
            self,
            "Two layers over one pairing matrix. The bottom is PERFECTNESS (solid, free,\n"
            "in Mathlib as riemannZeta one sub). The top is the POSITIVITY sign-pattern\n"
            "(fogged: the arithmetic Hodge standard conjecture, M4, open).",
            threeD=True, fs=16,
        )
        add_track(self, tracker, "perfectness (Mathlib)", "v", threeD=True)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [matrix, perfect, perfect_lab, positivity, q, positivity_lab, cap]])

        # Beat C5: the function-field Rosetta, circle straightens into the line.
        circle = Circle(radius=1.6, color=C_REALIZATION, stroke_width=4).shift(LEFT * 3.2)
        c_dots = VGroup(*[
            Dot(circle.point_at_angle(a), color=C_REALIZATION, radius=0.06)
            for a in np.linspace(0, TAU, 9)[:-1]
        ])
        line = Line([3.2, -2.0, 0], [3.2, 2.0, 0], color=C_CRITLINE, stroke_width=4)
        l_dots = VGroup(*[
            Dot([3.2, y, 0], color=C_REALIZATION, radius=0.06)
            for y in np.linspace(-1.7, 1.7, 8)
        ])
        ghost = DashedLine([3.2, -2.0, 0], [3.2, 2.0, 0], color=C_INVISIBLE,
                           stroke_width=2, stroke_opacity=0.35)
        gram = MathTex(r"\begin{pmatrix}2 & t\\ t & 2q\end{pmatrix}\ \text{PD} \iff |t|<2\sqrt{q}").scale(0.6)
        gram.to_edge(UP, buff=0.7)
        self.add_fixed_in_frame_mobjects(gram)
        self.play(Create(circle), Create(c_dots), Write(gram))
        cap = show_caption(
            self,
            "Over a curve mod q the Weil-Rosati polarization forces the size of alpha\n"
            "to equal root q: zeros on a circle. Over Spec(Z) the circle straightens into\n"
            "the line Re = 1/2, and the polarization becomes a dashed ghost (no carrier).",
            threeD=True, fs=16,
        )
        self.play(ReplacementTransform(circle, line),
                  ReplacementTransform(c_dots, l_dots))
        self.play(Create(ghost))
        self.play(ghost.animate.set_stroke(opacity=0.18))
        add_track(self, tracker, "the function-field circle (a theorem)", "v", threeD=True)
        add_track(self, tracker, "the carrier over Spec(Z) (ghost)", "i", threeD=True)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [line, l_dots, ghost, gram, cap]])
        self.remove(gram)

        # Beat C6: the D-H impostor, one bead leaves the line, one eigenvalue flips.
        wire = Line([-1.5, -2.2, 0], [-1.5, 2.2, 0], color=C_CRITLINE, stroke_width=3)
        on_beads = VGroup(*[Dot([-1.5, y, 0], color=C_REALIZATION, radius=0.06)
                            for y in np.linspace(-1.9, 1.9, 9)])
        self.play(Create(wire), LaggedStartMap(FadeIn, on_beads, lag_ratio=0.08))
        impostor = on_beads[5]
        partner = Dot([-1.5, on_beads[5].get_y(), 0], color=C_DH, radius=0.06)
        disp_label = MathTex(r"|1-2\beta|=0.617", color=C_DH).scale(0.55)
        target_x = -0.2
        partner_x = -2.8
        disp_label.next_to([target_x, impostor.get_y(), 0], UP, buff=0.2)
        base_y = -1.0
        bar = make_bar(2.6, -0.9, base_y=base_y, color=C_REALIZATION)
        flip = make_bar(2.6, 0.9, base_y=base_y, color=C_DH)
        bar_base = Line([2.0, base_y, 0], [3.2, base_y, 0], color=C_VISIBLE, stroke_width=2)
        connector = Arrow([target_x, impostor.get_y(), 0], bar.get_top(), color=C_DH,
                          stroke_width=2, buff=0.2)
        cap = show_caption(
            self,
            "D-H has the same free pairing but an off-line zero at 0.8085 plus 85.7 i\n"
            "(partner 0.1915 plus 85.7 i), displaced by 0.617. That is one eigenvalue\n"
            "flipping above 0: the signature is broken. The defect hides at huge height.",
            threeD=True, fs=16,
        )
        self.play(Create(bar_base), GrowFromEdge(bar, DOWN))
        self.play(impostor.animate.move_to([target_x, impostor.get_y(), 0]).set_color(C_DH),
                  FadeIn(partner.move_to([partner_x, impostor.get_y(), 0])),
                  Write(disp_label))
        self.play(Transform(bar, flip), Create(connector))
        add_track(self, tracker, "the D-H impostor (off-line zero)", "v", threeD=True)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [wire, on_beads, partner, disp_label,
                                         bar, bar_base, connector, cap]])

        # Beat C7: the marginal-positivity razor.
        razor = VGroup(
            Text("Weil cancellation leaves a residue about 1 in 1000.", font_size=18),
            Text("D-H fails Weil positivity by about 78.7 percent per off-line direction.", font_size=18),
            MathTex(r"\Lambda \le 0 \iff \text{RH};\quad \text{Rodgers-Tao 2018: } \Lambda \ge 0").scale(0.7),
            Text("So RH sits on the knife edge Lambda = 0, with no slack. A compass, not a wall.",
                 font_size=18, color=C_CRITLINE),
        ).arrange(DOWN, buff=0.25)
        nl = NumberLine(x_range=[-1, 1, 0.5], length=4, include_numbers=False).next_to(razor, DOWN, buff=0.4)
        tick = Dot(nl.n2p(0), color=C_CRITLINE, radius=0.08)
        tick_lab = MathTex(r"\Lambda=0", color=C_CRITLINE).scale(0.6).next_to(tick, DOWN, buff=0.1)
        self.add_fixed_in_frame_mobjects(razor, nl, tick, tick_lab)
        for line_m in razor:
            self.play(Write(line_m), run_time=0.8)
        self.play(Create(nl), FadeIn(tick), Write(tick_lab), Indicate(tick, color=C_CRITLINE))
        add_track(self, tracker, "the marginal-positivity razor", "v", threeD=True)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [razor, nl, tick, tick_lab]])

        # Beat C8: the hall of machines and the three near-miss gears.
        names = ["Deninger", "Connes-Consani", "prismatic / WCart", "Hesselholt THH/TC",
                 "Arakelov / FH", "F_1", "AHK"]
        machines = VGroup(*[make_machine_icon(n, scale=0.62) for n in names])
        machines.arrange(RIGHT, buff=0.18).scale_to_fit_width(12).to_edge(UP, buff=1.4)
        self.add_fixed_in_frame_mobjects(machines)
        self.play(LaggedStartMap(FadeIn, machines, lag_ratio=0.25))
        self.play(*[Indicate(m.socket, color=C_INVISIBLE) for m in machines])
        # Three near-miss gears bouncing off one socket.
        target_socket = machines[0].socket
        gear_names = ["Faltings-Hriljac\n(too local)", "AHK\n(too blind)", "de Branges\n(too strong)"]
        gears_box = VGroup()
        for i, gn in enumerate(gear_names):
            gear = Annulus(inner_radius=0.06, outer_radius=0.14, color=C_POLE,
                           fill_opacity=0.0, stroke_width=2)
            gear.next_to(machines, DOWN, buff=1.2).shift(RIGHT * (i - 1) * 3)
            lab = Text(gn, font_size=12, color=C_VISIBLE).next_to(gear, DOWN, buff=0.1)
            cross = Cross(gear, stroke_color=C_SIGNATURE, stroke_width=3)
            self.add_fixed_in_frame_mobjects(gear, lab)
            gears_box.add(VGroup(gear, lab, cross))
            self.play(FadeIn(gear), FadeIn(lab), run_time=0.4)
            self.play(gear.animate.move_to(target_socket).scale(1.1), run_time=0.5)
            self.add_fixed_in_frame_mobjects(cross.move_to(target_socket))
            self.play(gear.animate.next_to(machines, DOWN, buff=1.2).shift(RIGHT * (i - 1) * 3).scale(1 / 1.1),
                      FadeIn(cross.next_to(gear, UP, buff=0)), run_time=0.5)
        cap = show_caption(
            self,
            "A hall of machines, all emitting the same zeros, all with the identical empty\n"
            "socket. Three proven near-miss gears bracket the gap: Faltings-Hriljac (too\n"
            "local), AHK (too blind), de Branges (too strong, refuted at the 34th zero).",
            threeD=True, fs=15,
        )
        add_track(self, tracker, "the one missing polarization (global, (1,n-1), RH-equivalent)", "i", threeD=True)
        self.wait(2)
        self.play(*[FadeOut(m) for m in [machines, gears_box, cap]])
        self.wait(0.5)


# ===========================================================================
# CLOSE: collapse to the master image.
# ===========================================================================
class Close_MasterImage(Scene):
    def construct(self):
        title = Title(r"All Three Stages, One Missing Object")
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        # Beat D1: assemble the final master image.
        hall = VGroup(*[
            RoundedRectangle(corner_radius=0.06, width=0.5, height=0.4, color=C_VISIBLE, stroke_width=2)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.18).shift(LEFT * 3.5 + UP * 0.5)
        funnel = VGroup(
            make_road([-1.2, 1.3, 0], [1.2, 0.5, 0]),
            make_road([-1.2, -0.3, 0], [1.2, 0.5, 0]),
        ).shift(UP * 0.0)
        neck = Dot([1.2, 0.5, 0], color=C_CRITLINE, radius=0.1)
        socket = make_gear_socket(outer=0.5, inner=0.32).shift(RIGHT * 3.6 + UP * 0.5)
        stamp = MathTex(r"(1,\,n-1)", color=C_SIGNATURE).scale(0.55).move_to(socket)
        hall_lab = Text("the hall", font_size=14, color=C_VISIBLE).next_to(hall, DOWN, buff=0.2)
        funnel_lab = Text("the funnel-neck", font_size=14, color=C_CRITLINE).next_to(neck, DOWN, buff=0.6)
        socket_lab = Text("the empty socket", font_size=14, color=C_INVISIBLE).next_to(socket, DOWN, buff=0.2)
        self.play(LaggedStart(
            FadeIn(hall), Create(funnel), FadeIn(neck), Create(socket),
            lag_ratio=0.3, run_time=2.5,
        ))
        self.play(Write(hall_lab), Write(funnel_lab), Write(socket_lab))
        self.play(Write(stamp))
        cap = show_caption(
            self,
            "One hall. One funnel-neck. One empty gear-shaped socket,\n"
            "stamped with the (1, n-1) saddle signature.",
        )
        self.wait(1.5)
        self.play(FadeOut(cap))

        # Beat D2: the single invisible object.
        msg = VGroup(
            Text("All three stages share ONE invisible object:", font_size=22, color=C_INVISIBLE),
            Text("the missing polarization over Spec(Z)", font_size=22, color=C_INVISIBLE),
            Text("(M4, the arithmetic Hodge standard conjecture).", font_size=20, color=C_INVISIBLE),
            Text("Every candidate supplies the trace and the free pairing. None supplies this.",
                 font_size=18, color=C_VISIBLE),
            Text("Supplying it is RH.", font_size=26, color=C_SIGNATURE),
        ).arrange(DOWN, buff=0.22).shift(DOWN * 0.6)
        self.play(Indicate(socket, color=C_INVISIBLE, scale_factor=1.2))
        for line_m in msg:
            self.play(Write(line_m), run_time=0.8)
        self.wait(2)
        self.play(*[FadeOut(m) for m in [hall, funnel, neck, socket, stamp,
                                         hall_lab, funnel_lab, socket_lab, msg]])

        # Beat D3: closing stance (directional, not fatalistic).
        c1 = Text("A compass, not a wall.", font_size=30, color=C_CRITLINE)
        c2 = Text("Each dead branch is a coordinate. The target is narrowed, not abandoned.",
                  font_size=22, color=C_VISIBLE)
        close = VGroup(c1, c2).arrange(DOWN, buff=0.4)
        self.play(Write(c1))
        self.play(Write(c2))
        self.wait(3)
        self.play(FadeOut(close))
