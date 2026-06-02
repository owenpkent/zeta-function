"""Experiment M3.3: a SECOND integer-supported off-line control for M_euler.

M3.2 (e3m2) showed M_euler's false-positive discipline rests on Davenport-
Heilbronn alone: every Epstein off-line form has a_1 = 0 and cannot be fed to
the von-Mangoldt split. LEARNINGS #35 made the gating question explicit:

    build a second integer-supported (a_1 != 0) off-line control and confirm
    M_euler < 0 on it.

This script does that, the honest way. It builds a Davenport-Heilbronn-TYPE
function at a NEW conductor q (not 5) and verifies, numerically and from
scratch, that it (i) has a functional equation, (ii) is NOT an Euler product
(it is a genuine 2-term combination, so RH may fail), (iii) has a_1 = 1, and
(iv) actually has an off-line zero at reachable height. Only then is it a
legitimate RH-false control, and only then do we run M_euler on it.

## Construction

For a primitive COMPLEX character chi mod q of odd parity (chi(-1) = -1), the
real-coefficient combination

    c_n = Re chi(n) + kappa * Im chi(n)        (period q, c_1 = 1)

is, as a Dirichlet series f(s) = sum c_n n^{-s}, equal to
c1 L(s,chi) + conj(c1) L(s,chibar) with c1 = (1 - i kappa)/2. Each L(s,chi) is
entire (chi non-principal) with the SAME archimedean Gamma factor, so the
completed Lambda_f(s) = (q/pi)^{(s+1)/2} Gamma((s+1)/2) f(s) satisfies a
functional equation Lambda_f(s) = W Lambda_f(1-s), W in {+1,-1}, for ONE special
value of kappa (the Davenport-Heilbronn tuning, generalized). We PIN kappa by
driving the FE residual to zero numerically and then VERIFY the identity at
several independent points. f is a combination of two distinct L-functions, not
one, so it has no Euler product and (Davenport-Heilbronn-Cassels) has off-line
zeros, which we then exhibit.

This keeps the project's discipline: nothing about the control is asserted, it
is all numerically verified before M_euler is allowed to see it.

Outputs:
  - e3m3_second_offline.npz
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments._shared.lfunction import LFunction
from experiments.positivity.e3m_place_type_balance import (
    pole_block, lambda_coeffs_from_dirichlet, von_mangoldt_zeta,
)
from experiments.positivity.e3m_analytic_domination import split_finite_block
from experiments.arithmetic_geometric.e2v_rosati_balance_M2_5 import arch_block_bombieri


def _primitive_root(q: int) -> int:
    """A primitive root mod q (q prime)."""
    for g in range(2, q):
        seen = set()
        x = 1
        for _ in range(q - 1):
            x = (x * g) % q
            seen.add(x)
        if len(seen) == q - 1:
            return g
    raise ValueError(f"no primitive root found mod {q}")


def _character_values(q: int, order_div: int, dps: int):
    """Values chi(1..q) of a primitive char mod q (q prime) of order
    (q-1)/order_div, via chi(g^k) = exp(2 pi i k / ord). order_div selects which
    power; order_div=1 gives the full-order character (chi of order q-1)."""
    prev = mp.mp.dps
    mp.mp.dps = max(dps, prev)
    try:
        g = _primitive_root(q)
        ord_chi = (q - 1) // order_div
        # discrete log table: dlog[n] = k with g^k = n
        dlog = {}
        x = 1
        for k in range(q - 1):
            x = (x * g) % q if k > 0 else 1
            dlog[x] = k
        # rebuild cleanly (k=0 -> g^0=1)
        dlog = {}
        x = 1
        for k in range(q - 1):
            dlog[x] = k
            x = (x * g) % q
        chi = [mp.mpc(0)] * (q + 1)
        for n in range(1, q):
            k = dlog[n % q]
            chi[n] = mp.e ** (2j * mp.pi * mp.mpf(k * order_div) / (q - 1))
        chi[q] = mp.mpc(0)
        return chi
    finally:
        mp.mp.dps = prev


class DHTypeL(LFunction):
    """Davenport-Heilbronn-type real-coefficient combination at conductor q.

    c_n = Re chi(n) + kappa Im chi(n), period q, with kappa pinned so the
    completed function has a functional equation. No Euler product.
    """

    has_euler_product = False
    has_functional_equation = True

    def __init__(self, q: int, order_div: int = 1, dps: int = 40, name: str = None):
        self.q = q
        chi = _character_values(q, order_div, dps)
        # parity from chi(q-1) = chi(-1)
        self._parity = 0 if mp.re(chi[q - 1]) > 0 else 1
        self._chi = chi
        self._dps = dps
        self.kappa = self._pin_kappa(chi, q, self._parity, dps)
        # real period-q coefficients, c_1 = 1
        self._coeffs = [mp.mpf(0)] + [
            mp.re(chi[n]) + self.kappa * mp.im(chi[n]) for n in range(1, q + 1)
        ]
        self.name = name or f"dhtype_q{q}_o{order_div}"
        self.W = self._best_W(dps)

    # ---- construction -----------------------------------------------------

    @staticmethod
    def _coeffs_for(chi, q, kappa):
        return [mp.mpf(0)] + [mp.re(chi[n]) + kappa * mp.im(chi[n]) for n in range(1, q + 1)]

    @staticmethod
    def _f_eval(coeffs, q, s):
        s = mp.mpc(s)
        return mp.power(q, -s) * sum(coeffs[a] * mp.zeta(s, mp.mpf(a) / q) for a in range(1, q + 1))

    @classmethod
    def _Lambda(cls, coeffs, q, parity, s):
        s = mp.mpc(s)
        a = parity
        return (mp.power(mp.mpf(q) / mp.pi, (s + a) / 2) * mp.gamma((s + a) / 2)
                * cls._f_eval(coeffs, q, s))

    @classmethod
    def _pin_kappa(cls, chi, q, parity, dps):
        """Find kappa making Lambda_f(s) = W Lambda_f(1-s) for W in {+1,-1}.

        At a generic test point s0, the residual r(kappa) = Lambda(s0) -/+
        Lambda(1-s0) is affine in kappa (coeffs are linear in kappa). Solve the
        two linear options and keep the kappa whose identity holds at OTHER
        points too.
        """
        prev = mp.mp.dps
        mp.mp.dps = max(dps, prev)
        try:
            s0 = mp.mpc(mp.mpf("0.3"), mp.mpf("7.0"))
            s1 = mp.mpc(mp.mpf("0.62"), mp.mpf("13.0"))
            best = None
            for W in (mp.mpf(1), mp.mpf(-1)):
                # Lambda is affine in kappa: Lambda = A + kappa B. Get A,B by
                # evaluating at kappa=0 and kappa=1.
                def resid(s, kappa):
                    co = cls._coeffs_for(chi, q, kappa)
                    return cls._Lambda(co, q, parity, s) - W * cls._Lambda(co, q, parity, 1 - s)
                r0 = resid(s0, mp.mpf(0))
                r1 = resid(s0, mp.mpf(1))
                B = r1 - r0
                if abs(B) < mp.mpf(10) ** (-dps + 10):
                    continue
                kappa = -r0 / B  # complex in general; the true tuning is real
                kappa = mp.re(kappa)
                # verify at the independent point s1
                check = abs(resid(s1, kappa))
                scale = abs(cls._Lambda(cls._coeffs_for(chi, q, kappa), q, parity, s1)) + mp.mpf(1)
                rel = check / scale
                if best is None or rel < best[2]:
                    best = (kappa, W, rel)
            if best is None or best[2] > mp.mpf("1e-12"):
                raise ValueError(f"could not pin a real kappa with an FE (best rel {best[2] if best else 'n/a'})")
            return best[0]
        finally:
            mp.mp.dps = prev

    def _best_W(self, dps):
        prev = mp.mp.dps
        mp.mp.dps = max(dps, prev)
        try:
            s0 = mp.mpc(mp.mpf("0.41"), mp.mpf("9.3"))
            co, q, a = self._coeffs, self.q, self._parity
            Ls = self._Lambda(co, q, a, s0)
            L1 = self._Lambda(co, q, a, 1 - s0)
            return 1 if abs(Ls - L1) < abs(Ls + L1) else -1
        finally:
            mp.mp.dps = prev

    # ---- LFunction interface ---------------------------------------------

    def dirichlet_coefficient(self, n: int):
        if n < 1:
            return mp.mpc(0)
        return mp.mpc(self._coeffs[((n - 1) % self.q) + 1])

    def evaluate(self, s):
        return self._f_eval(self._coeffs, self.q, s)

    def fe_residual(self, s):
        co, q, a = self._coeffs, self.q, self._parity
        return self._Lambda(co, q, a, s) - self.W * self._Lambda(co, q, a, 1 - s)

    def zeros(self, T_max: float, prec: int = 30):
        """Minimal LFunction.zeros: return any located off-line zero (and its
        FE/conjugate partners). M_euler needs only the Dirichlet coefficients,
        so a full zero census is unnecessary here; we expose the off-line
        witness that certifies RH is false."""
        z = self.find_offline_zero(T_max=T_max, prec=prec)
        if z is None:
            return []
        partners = [z, mp.mpc(1 - z.real, z.imag)]
        return [p for p in partners if 0 < p.imag <= T_max]

    def find_offline_zero(self, T_max=120.0, prec=30, scan_step=0.5):
        """Locate one off-line zero (Re != 1/2) up to height T_max, to certify
        RH is false for this control. Coarse 2D scan + findroot refine."""
        prev = mp.mp.dps
        mp.mp.dps = max(prec, 30)
        try:
            sigmas = [mp.mpf(s) / 100 for s in range(56, 95, 4)]  # sigma > 1/2 side
            t = scan_step
            while t <= T_max:
                for sg in sigmas:
                    val = abs(self.evaluate(mp.mpc(sg, t)))
                    if float(val) < 0.25:
                        try:
                            root = mp.findroot(self.evaluate, mp.mpc(sg, t),
                                               tol=mp.mpf(10) ** (-prec + 5))
                        except (ValueError, ZeroDivisionError):
                            continue
                        if (mp.mpf(0) < root.imag <= T_max
                                and abs(float(root.real) - 0.5) > 1e-3
                                and abs(self.evaluate(root)) < mp.mpf(10) ** (-prec + 8)):
                            return root
                t += scan_step
            return None
        finally:
            mp.mp.dps = prev


def run(K=8, b_min=1.3, b_max=6.0, prec=30, T_zero=120.0, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2

    print("[M3.3] Second integer-supported off-line control for M_euler.\n")

    # Candidate DH-type functions at new conductors (complex char, odd parity).
    candidates = []
    for q, order_div in [(7, 1), (13, 1), (13, 3)]:
        try:
            L = DHTypeL(q, order_div=order_div, dps=max(prec + 10, 40))
        except ValueError as e:
            print(f"  q={q} o={order_div}: construction failed ({e})")
            continue
        if L._parity != 1:
            print(f"  {L.name}: even parity, skipping (need odd for this Gamma factor)")
            continue
        # verify FE at a few points
        fe = max(float(abs(L.fe_residual(mp.mpc(0.5, t)))) for t in (4.0, 11.0, 19.0))
        a1 = float(mp.re(L.dirichlet_coefficient(1)))
        print(f"  {L.name}: parity={L._parity} kappa={float(L.kappa):+.6f} W={L.W} "
              f"a_1={a1:.3f} FE_resid(max)={fe:.2e}")
        candidates.append(L)

    # Pick the first with a clean FE and a located off-line zero.
    control = None
    for L in candidates:
        z = L.find_offline_zero(T_max=T_zero, prec=prec)
        if z is not None:
            print(f"  -> {L.name}: OFF-LINE ZERO at {complex(z):.4f} "
                  f"(Re-1/2 = {float(z.real)-0.5:+.4f}); RH is FALSE for it.")
            control = (L, z)
            break
        else:
            print(f"  -> {L.name}: no off-line zero found below T={T_zero}; not usable as-is.")

    if control is None:
        print("\n[M3.3] No verified second off-line control found among candidates.")
        print("       (Increase T_zero or add conductors.) M_euler's off-line")
        print("       discipline still rests on Davenport-Heilbronn alone.")
        return None

    L, zoff = control
    log_Q = mp.log(mp.sqrt(L.q))

    # Build M_euler for: zeta (baseline), D-H (known control), the NEW control.
    dh = DavenportHeilbronn()
    targets = [
        ("zeta",          zeta_L, [0.0], mp.mpf(0),          1.0, True,  True),
        ("DH(q=5)",       dh,     [1.0], mp.log(mp.sqrt(5)), 0.0, False, False),
        (f"{L.name}",     L,      [1.0], log_Q,              0.0, False, False),
    ]

    print("\n[M3.3] M_euler on the new control (RH FALSE, a_1=1, FE verified):\n")
    header = f"{'target':<16} {'Euler':>5} {'RH':>5} {'min eig(M_euler)':>17} {'detector':>9}"
    print(header); print("-" * len(header))

    results = {}
    for label, Lf, mu_list, lq, residue, has_euler, rh in targets:
        if label == "zeta":
            lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
        else:
            lam = lambda_coeffs_from_dirichlet(Lf, n_max, prec)
        P_pp, P_comp = split_finite_block(b_vals, lam, prec)
        B = pole_block(b_vals, float(residue), prec)
        A = arch_block_bombieri(b_vals, mu_list, lq, prec)
        M_euler = A + P_pp + B
        min_eig = float(np.linalg.eigvalsh(M_euler).min())
        says_rh = min_eig >= 0.0
        verdict = "ok" if (says_rh == rh) else "BREAK"
        results[label] = dict(min_eig=min_eig, rh=rh, verdict=verdict)
        print(f"{label:<16} {str(has_euler):>5} {str(rh):>5} {min_eig:>+17.4e} {verdict:>9}")

    print("-" * len(header))
    new = results[L.name]
    print("\n[M3.3] ===== VERDICT =====")
    if new["verdict"] == "BREAK":
        print(f"  FALSE POSITIVE on {L.name}: RH is FALSE (off-line zero at")
        print(f"  {complex(zoff):.4f}) but min eig(M_euler) = {new['min_eig']:+.4e} >= 0.")
        print("  M_euler is NOT a valid RH detector: it certified a function with")
        print("  off-line zeros as RH-compatible. M3's 'stealth window broken' claim")
        print("  FAILS on the second control. The hand-deletion of P_comp does not")
        print("  capture RH; it only happened to work for Davenport-Heilbronn.")
    else:
        print(f"  M_euler = {new['min_eig']:+.4e} < 0 on {L.name} (RH FALSE), a SECOND")
        print("  off-line witness beyond the q=5 Davenport-Heilbronn function (different")
        print("  conductor, character order, and tuning kappa; off-line zero verified).")
        print("  HONEST SCOPE: both witnesses are Davenport-Heilbronn-TYPE (real-coeff")
        print("  combinations of a complex character and its conjugate). This removes the")
        print("  literal single-EXAMPLE fragility of LEARNINGS #35, but not the single-")
        print("  FAMILY one: the structurally independent off-line mechanism (Epstein)")
        print("  still cannot be tested (a_1 = 0). And it does NOT prove the 8B/8C")
        print("  geometric conjecture; see e3m3 note / LEARNINGS #36 on why P_comp = 0")
        print("  is vacuous for the only input that has a surface (zeta).")

    np.savez_compressed(
        out_dir / "e3m3_second_offline.npz",
        control_name=L.name, q=L.q, kappa=float(L.kappa), W=L.W,
        offline_zero_re=float(zoff.real), offline_zero_im=float(zoff.imag),
        labels=np.array(list(results.keys()), dtype=object),
        min_eig=np.array([results[n]["min_eig"] for n in results]),
        rh=np.array([results[n]["rh"] for n in results]),
        K=K, prec=prec,
    )
    print(f"\n[M3.3] Saved {out_dir / 'e3m3_second_offline.npz'}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--b-max", type=float, default=6.0)
    parser.add_argument("--prec", type=int, default=30)
    parser.add_argument("--T-zero", type=float, default=120.0)
    args = parser.parse_args()
    run(K=args.K, b_max=args.b_max, prec=args.prec, T_zero=args.T_zero)
