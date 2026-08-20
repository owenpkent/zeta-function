"""E2AT: the pole-constrained xi ladder: does the constraint reconcile #185
with CCM?

B2c-lit found the candidate explanation for #185's narrowing: CCM ("Zeta
spectral triples", arXiv:2511.22755, Suzuki's [4]) build their ground-state
approximant WITH the vanishing-integral (pole) conditions, while our
instrument minimized over the UNCONSTRAINED window space, where mass may
concentrate at the origin: precisely the measured narrowing. The pole
condition in the additive even picture is
    vhat(i/2) = 0   (equivalently int v(x) cosh(x/2) dx = 0),
and in the B-spline basis the constraint functional has an EXACT closed
form: b_k = psihat_k(i/2) = h (sinh(h/4)/(h/4))^{13} x {1 or 2 cosh(c_k/2)}.

This module reruns the deep ladder (80-digit zeros to T = 350, dps-80
solves, the e2as gates) with that single linear constraint imposed by exact
projection, alongside the unconstrained values from #185 for contrast.

PRE-REGISTERED: if the constrained ground state stays near the xi shape
through a = 2-2.5, the #185 narrowing is a property of the WRONG object and
(1.2) concerns the pole-constrained bottom: reconciliation, and a sharp
statement about which object the conjecture needs. If it still narrows, the
constraint is excluded as the explanation and the tension stands.

Run:
  python -m experiments.arithmetic_geometric.e2at_constrained_xi

Outputs: e2at_constrained_xi.npz (tracked).
"""

from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments.arithmetic_geometric.e2ar_hard_window_xi import (
    DEG, cardinal_spline, sincp)
from experiments.arithmetic_geometric.e2aq_xi_convergence import Xi
from experiments.arithmetic_geometric.e2as_deep_xi_ladder import (
    DPS_DEEP, T_DEEP, ZPTS, zeros_deep)

HERE = Path(__file__).resolve().parent

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


class ConstrainedGS:
    """Bottom of the zero-side Weil form on the even hard-window B-spline
    space, WITH the pole condition vhat(i/2) = 0 imposed by exact projection.
    dps-80 protocol throughout."""

    def __init__(self, a: float, gz, m_knots: int | None = None):
        mp.mp.dps = DPS_DEEP
        self.a = mp.mpf(a)
        if m_knots is None:
            m_knots = int(round(56 * a))
        self.h = 2 * self.a / m_knots
        Kmax = int(mp.floor(m_knots / 2 - (DEG + 1) / 2))
        self.centers = [k * self.h for k in range(0, Kmax + 1)]
        J = len(self.centers)

        def pair(mu, nu):
            return self.h * cardinal_spline(2 * DEG + 1, (mu - nu) / self.h)

        G = mp.zeros(J, J)
        for i in range(J):
            for j in range(i, J):
                mi, mj = self.centers[i], self.centers[j]
                v = pair(mi, mj)
                if i > 0:
                    v += pair(-mi, mj)
                if j > 0:
                    v += pair(mi, -mj)
                if i > 0 and j > 0:
                    v += pair(-mi, -mj)
                G[i, j] = G[j, i] = v if (i > 0 or j > 0) else pair(0, 0)

        def psihat(k, t):
            base = self.h * sincp(t * self.h / 2) ** (DEG + 1)
            return base * (2 * mp.cos(self.centers[k] * t) if k > 0 else mp.mpf(1))

        self._psihat = psihat
        tab = mp.zeros(J, len(gz))
        for k in range(J):
            for b, g in enumerate(gz):
                tab[k, b] = psihat(k, g)
        Qz = 2 * tab * tab.T

        # the pole constraint b_k = psihat_k(i/2): sinc(i h/4) = sinh(h/4)/(h/4)
        shf = mp.sinh(self.h / 4) / (self.h / 4)
        b = mp.matrix([self.h * shf ** (DEG + 1)
                       * (2 * mp.cosh(self.centers[k] / 2) if k > 0 else mp.mpf(1))
                       for k in range(J)])
        self.bvec = b
        # Householder H maps b to |b| e_1; columns 2..J of H span the null space
        nb = mp.sqrt(sum(b[r] ** 2 for r in range(J)))
        w = mp.matrix([b[r] for r in range(J)])
        w[0] = w[0] + (nb if b[0] >= 0 else -nb)
        nw = mp.sqrt(sum(w[r] ** 2 for r in range(J)))
        for r in range(J):
            w[r] = w[r] / nw
        H = mp.eye(J) - 2 * (w * w.T)
        N = H[:, 1:J]                              # J x (J-1), b' N = 0
        Gt = N.T * G * N
        Qt = N.T * Qz * N
        L = mp.cholesky(Gt)
        Li = mp.inverse(L)
        A = Li * Qt * Li.T
        E, V = mp.eigsy(A)
        order = sorted(range(J - 1), key=lambda i: mp.re(E[i]))
        i0, i1 = order[0], order[1]
        self.lam0, self.lam1 = mp.re(E[i0]), mp.re(E[i1])
        y = mp.matrix([V[r, i0] for r in range(J - 1)])
        self.c = N * (Li.T * y)
        nrm = mp.sqrt(mp.re((self.c.T * (G * self.c))[0]))
        for r in range(J):
            self.c[r] = self.c[r] / nrm
        self.J = J
        self.constraint_resid = float(abs(sum(b[r] * self.c[r] for r in range(J))))

    def vhat(self, t):
        tt = mp.mpf(t)
        return sum(self.c[k] * self._psihat(k, tt) for k in range(self.J))


def solve(a, gz, m):
    gs = ConstrainedGS(a, gz, m_knots=m)
    c0 = float(gs.vhat(0.0)) / float(Xi(0.0))
    ratios = [float(gs.vhat(z)) / (c0 * float(Xi(z))) for z in ZPTS]
    lg0 = float(mp.log10(abs(gs.lam0))) if gs.lam0 != 0 else float("-inf")
    gap = float(gs.lam1 / gs.lam0) if gs.lam0 != 0 else float("inf")
    return gs, ratios, lg0, gap


def run():
    t0 = time.time()
    print("== E2AT: the pole-constrained xi ladder (vhat(i/2) = 0) ==")
    gz = zeros_deep()
    mp.mp.dps = DPS_DEEP

    # unconstrained reference (the #185 verdict data)
    ref = np.load(HERE / "e2as_deep_xi_ladder.npz")
    un_ratios = {a: r for a, r in zip(ref["avals"], ref["ratios_ref"])}

    AVALS = [1.0, 1.5, 2.0, 2.5]
    rows = []
    for a in AVALS:
        gsb, rb, lgb, gapb = solve(a, gz, int(round(56 * a)))
        gsr, rr, lgr, gapr = solve(a, gz, int(round(112 * a)))
        shift = float(max(abs(x - y) for x, y in zip(rb, rr)))
        conv = shift < 0.05
        rows.append({"a": a, "ratios": rr, "shift": shift, "conv": conv,
                     "lg0": lgr, "gap": gapr,
                     "bres": gsr.constraint_resid})
        print(f"   a = {a} (J = {gsr.J}): log10 lam0 = {lgr:.2f}, gap = {gapr:.1f}, "
              f"gate shift = {shift:.4f} -> {'CONVERGED' if conv else 'NOT CONVERGED'}")
        print(f"      constrained ratios   = " + ", ".join(f"{r:+.4f}" for r in rr))
        print(f"      unconstrained (#185) = "
              + ", ".join(f"{r:+.4f}" for r in un_ratios[a]))

    print("\n-- checks --")
    # The pre-registered reconciliation hypothesis was REFUTED by this run,
    # and the diagnosis identified the structural reason, verified below:
    # the xi function itself VIOLATES the pole constraint at the boundary.
    check("constraint enforced exactly: |b . c| at machine scale on every rung",
          all(r["bres"] < 1e-30 for r in rows),
          f"max = {max(r['bres'] for r in rows):.1e}")
    check("REFUTATION TYPED: the naive constrained bottom does NOT restore the "
          "xi shape at z0-normalization (v(0)-suppression explodes the ratios)",
          all(abs(r["ratios"][2]) > 5 for r in rows),
          "r(z=6): " + ", ".join(f"{r['ratios'][2]:+.1f}" for r in rows))
    check("INSTRUMENT LIMIT RECORDED: the constrained problem is basis-"
          "unconverged at matched resolution on every rung (no shape claims)",
          all(not r["conv"] for r in rows),
          "shifts: " + ", ".join(f"{r['shift']:.2f}" for r in rows))
    # xi(0) via the regular factorization xi(s) = (s-1) pi^{-s/2} Gamma(s/2+1) zeta(s)
    s0 = mp.mpf(0)
    xi_i2 = float(mp.re((s0 - 1) * mp.pi ** (-s0 / 2) * mp.gamma(s0 / 2 + 1)
                        * mp.zeta(s0)))
    check("THE STRUCTURAL FACT (mp-verified): Xi(i/2) = xi(0) = 1/2, so the "
          "xi function VIOLATES the pole constraint; (1.2)'s limit lives "
          "outside the constrained space and CCM's convergence (Lemma 7.3) is "
          "interior-only: finite-a comparisons must be interior fits",
          abs(xi_i2 - 0.5) < 1e-30, f"Xi(i/2) = {xi_i2}")
    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.0f} s)")

    out = HERE / "e2at_constrained_xi.npz"
    np.savez_compressed(
        out,
        avals=np.array(AVALS),
        ratios=np.array([r["ratios"] for r in rows]),
        shifts=np.array([r["shift"] for r in rows]),
        conv=np.array([r["conv"] for r in rows]),
        lg0=np.array([r["lg0"] for r in rows]),
        gaps=np.array([r["gap"] for r in rows]),
        bres=np.array([r["bres"] for r in rows]),
        un_ratios=np.array([un_ratios[a] for a in AVALS]),
        zpts=np.array(ZPTS),
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")


if __name__ == "__main__":
    run()
