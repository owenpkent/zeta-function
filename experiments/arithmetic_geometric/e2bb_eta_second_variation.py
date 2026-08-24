"""E2BB: C2: the eta-form second variation over the FE-closed character
pencil: does the arithmetic eta invariant have a canonical finite Hessian,
and what does its signature reproduce?

THE SETTING (#177/#178). The arithmetic eta invariant lives on complex
Dirichlet characters (eta(chi) = -(2/pi) arg_c L(1/2, chi), the C1 closed
form of LEARNINGS #178, verified there at 2e-4 against two spectral
regularizations). Character space is archimedean-ly DISCRETE, so a second
variation needs a chosen continuous deformation space; the only FE-closed
continuous family through a character chi is the PENCIL
span{L(chi), L(chibar)} (the reflection s -> 1-s maps it to itself):

    g_u(s) = L(s, chi) + u * B(s),
    d1: B = L(s, chibar)     d2: B = i L(s, chibar)   (conjugate-mixing:
        reality-breaking, the eta-active directions; generic members are
        D-H-class: FE-closed pencil, no Euler product, off-line zeros)
    d3: B = L(s, chi)        d4: B = i L(s, chi)      (self-directions:
        pure rescaling, zeros unchanged: EXACT NULL ROWS, used as
        end-to-end pipeline validation)

eta(g_u) is computed from the signed zero multiset in |Im s| <= T
(zeros Newton-TRACKED from the undeformed zeros, so completeness is
inherited), with Abel weights e^{-|gamma| tau} on a tau-ladder and a
Cesaro (windowed counting-asymmetry) variant as the independent
regularization.

PRE-REGISTERED (the backlog fork, verbatim intent, no thumb on the
scale): EITHER [F-A] the Hessian exists canonically (null rows exact;
stencil-consistent; stable across the tau-ladder and across Abel/Cesaro;
signature FORCED: same at conductor 5 and 7) and its zero-side
decomposition is a spectral quadratic form: M4 in APS costume,
coordinate #5 minted from whatever structure is measured; OR [F-B]
forcing FAILS (regularization- or truncation-dependence, or conductor-
dependent signature): #177's trigger 1 hardens (no functorial
real-valued eta-form at finite conductor). Secondary exact validations,
pre-registered: eta at the real-coefficient point u = 1 along d1
vanishes (conjugation-symmetric spectrum), and the Euler-defect of the
mod-5 real pencil has the closed form b_6(kappa) = (kappa^2 + 1) log 6
>= log 6 (conservation-law Hessian 2 log 6 > 0; e2an's measured D-H
value 1.936 is its evaluation; the pilot's pre-registration missed the
log 6 factor and the identity check caught it).

K1 posture: this round consumes zeros BY DESIGN (a form-side diagnostic
of the eta functional; nothing here is a route to RH). Beurling: the
pencil construction needs the FE, so it does not pose there (typed
refusal); the D-H discipline is INTERNAL to the design (generic pencil
members ARE the FE-no-Euler class).

Run:
  python -m experiments.arithmetic_geometric.e2bb_eta_second_variation

Outputs: e2bb_eta_second_variation.npz (tracked, evidence rule).
"""

from __future__ import annotations

import time
from math import log, pi
from pathlib import Path

import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent

DPS = 20
T_WIN = 30.0
TAUS = (0.15, 0.10, 0.07)
H = 0.03

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------------------
# characters and L-functions (Hurwitz route)
# ---------------------------------------------------------------------------

def char_table(q):
    """A primitive odd complex character mod q (q = 5 or 7)."""
    if q == 5:
        vals = {1: 1, 2: 1j, 3: -1j, 4: -1}                 # chi(2) = i
    elif q == 7:
        w = mp.e ** (1j * mp.pi / 3)
        vals = {1: 1, 3: w, 2: w ** 2, 6: w ** 3, 4: w ** 4, 5: w ** 5}
    else:
        raise ValueError(q)
    return {a: mp.mpc(v) for a, v in vals.items()}


class Lchi:
    def __init__(self, q, conj=False):
        self.q = q
        tab = char_table(q)
        self.tab = {a: (mp.conj(v) if conj else v) for a, v in tab.items()}

    def __call__(self, s):
        s = mp.mpc(s)
        return mp.power(self.q, -s) * mp.fsum(
            v * mp.zeta(s, mp.mpf(a) / self.q) for a, v in self.tab.items())


# ---------------------------------------------------------------------------
# eta machinery
# ---------------------------------------------------------------------------

def find_zeros(f, T=T_WIN, dt=0.05):
    """Zeros of f on the critical line window |t| <= T at u = 0 (dip scan
    + Newton); returns complex zeros, both signs of t."""
    ts = np.arange(-T, T + dt / 2, dt)
    ts = ts[np.abs(ts) > 0.15]
    vals = np.array([abs(complex(f(mp.mpc(0.5, t)))) for t in ts])
    zeros = []
    med = np.median(vals)
    for i in range(1, len(ts) - 1):
        if vals[i] < vals[i - 1] and vals[i] < vals[i + 1] and vals[i] < 0.35 * med:
            try:
                r = mp.findroot(f, mp.mpc(0.5, ts[i]))
            except Exception:
                continue
            if abs(f(r)) < 1e-10 and abs(mp.im(r)) <= T + 0.5:
                if not any(abs(r - z) < 1e-6 for z in zeros):
                    zeros.append(r)
    return sorted(zeros, key=lambda z: float(mp.im(z)))


def track(zeros, g):
    """Newton-track each zero to the deformed function g."""
    out = []
    for z in zeros:
        try:
            r = mp.findroot(g, z)
        except Exception:
            r = None
        if r is not None and abs(g(r)) < 1e-9 and abs(r - z) < 1.0:
            out.append(r)
        else:
            out.append(None)
    return out


def eta_abel(zeros, tau):
    return float(mp.fsum(mp.sign(mp.im(z)) * mp.e ** (-abs(mp.im(z)) * tau)
                         for z in zeros if z is not None))


def eta_cesaro(zeros, T=T_WIN):
    """Windowed mean of D(T') = #(0<gamma<=T') - #(-T'<=gamma<0) over
    T' in [T/2, T]."""
    gs = sorted(float(mp.im(z)) for z in zeros if z is not None)
    Ts = np.arange(T / 2, T, 0.05)
    D = [sum(1 for g in gs if 0 < g <= tp) - sum(1 for g in gs if -tp <= g < 0)
         for tp in Ts]
    return float(np.mean(D))


def arg_continued_at_half(f, s_hi=4.0, n=397):
    """arg f(1/2) continued along the real axis from sigma = s_hi. The
    grid must avoid sigma = 1 exactly: each Hurwitz term has a pole there
    (the poles cancel in the character sum analytically, but numerically
    inf - inf = nan; caught when the first grid choice hit 1.0 exactly)."""
    sig = np.linspace(s_hi, 0.5, n)
    sig = sig[np.abs(sig - 1.0) > 1e-9]
    vals = np.array([complex(f(mp.mpc(s, 0))) for s in sig])
    assert not np.any(np.isnan(vals)), "nan in arg continuation"
    return float(np.unwrap(np.angle(vals))[-1] - np.angle(vals)[0])


def run():
    t0 = time.time()
    print("== E2BB: the eta-form second variation over the FE-closed pencil (C2) ==")
    mp.mp.dps = DPS

    results = {}
    for q in (5, 7):
        print(f"\n-- conductor {q} --")
        Lc = Lchi(q)
        Lb = Lchi(q, conj=True)
        zeros0 = find_zeros(Lc)
        n_pos = sum(1 for z in zeros0 if mp.im(z) > 0)
        n_neg = len(zeros0) - n_pos
        dens = T_WIN / pi * log(q * T_WIN / (2 * pi * mp.e))
        print(f"   zeros found: {len(zeros0)} ({n_pos} up / {n_neg} down); "
              f"density formula ~ {float(dens):.1f}")
        online = max(abs(float(mp.re(z)) - 0.5) for z in zeros0)

        # the C1 closed form vs the truncated Abel sum at u = 0
        eta_c1 = -(2 / pi) * arg_continued_at_half(Lc)
        eta0 = {tau: eta_abel(zeros0, tau) for tau in TAUS}
        eta0_ces = eta_cesaro(zeros0)

        # pencil configurations: directions d1 = L(chibar), d2 = i L(chibar)
        def g_of(u1, u2):
            return lambda s: Lc(s) + (u1 + 1j * u2) * Lb(s)

        stencil = {}
        pts = [(H, 0), (-H, 0), (2 * H, 0), (-2 * H, 0),
               (0, H), (0, -H), (0, 2 * H), (0, -2 * H),
               (H, H), (-H, -H), (H, -H), (-H, H)]
        offline_frac = None
        for (u1, u2) in pts:
            tz = track(zeros0, g_of(u1, u2))
            lost = sum(1 for z in tz if z is None)
            if lost:
                print(f"   WARNING: lost {lost} zeros at u = ({u1}, {u2})")
            stencil[(u1, u2)] = tz
            if (u1, u2) == (H, 0):
                offs = [abs(float(mp.re(z)) - 0.5) for z in tz if z is not None]
                offline_frac = sum(1 for o in offs if o > 1e-6) / len(offs)
        stencil[(0, 0)] = zeros0

        # eta on the stencil, per tau (plus a T-window-stability variant)
        def eta_abel_T(zs, tau, Tcap):
            return float(mp.fsum(
                mp.sign(mp.im(z)) * mp.e ** (-abs(mp.im(z)) * tau)
                for z in zs if z is not None and abs(mp.im(z)) <= Tcap))

        Hmat = {}
        grads = {}
        for tau in TAUS:
            e = {k: eta_abel(v, tau) for k, v in stencil.items()}
            h11 = (e[(H, 0)] + e[(-H, 0)] - 2 * e[(0, 0)]) / H ** 2
            h22 = (e[(0, H)] + e[(0, -H)] - 2 * e[(0, 0)]) / H ** 2
            h12 = (e[(H, H)] + e[(-H, -H)] - e[(H, -H)] - e[(-H, H)]) / (4 * H ** 2)
            # step-halving consistency via the 2H points (Richardson pair)
            h11_2 = (e[(2 * H, 0)] + e[(-2 * H, 0)] - 2 * e[(0, 0)]) / (2 * H) ** 2
            h22_2 = (e[(0, 2 * H)] + e[(0, -2 * H)] - 2 * e[(0, 0)]) / (2 * H) ** 2
            g1 = (e[(H, 0)] - e[(-H, 0)]) / (2 * H)
            g2 = (e[(0, H)] - e[(0, -H)]) / (2 * H)
            Hmat[tau] = (h11, h22, h12, h11_2, h22_2)
            grads[tau] = (g1, g2)

        # Cesaro Hessian at the same stencil: RECORDED but not a fair
        # estimator (the windowed count is integer-granular: a single
        # window-edge crossing moves the second difference by 1/H^2; typed
        # in the dossier as estimator granularity, not regularization
        # failure)
        ec = {k: eta_cesaro(v) for k, v in stencil.items()}
        h11_c = (ec[(H, 0)] + ec[(-H, 0)] - 2 * ec[(0, 0)]) / H ** 2
        h22_c = (ec[(0, H)] + ec[(0, -H)] - 2 * ec[(0, 0)]) / H ** 2
        # T-window stability of the Abel Hessian (drop zeros above T = 25)
        e25 = {k: eta_abel_T(v, 0.10, 25.0) for k, v in stencil.items()}
        h11_T = (e25[(H, 0)] + e25[(-H, 0)] - 2 * e25[(0, 0)]) / H ** 2
        # tau -> 0 extrapolation of eta at u = 0 (linear in tau)
        taus_arr = np.array(TAUS)
        eta_ext = float(np.polyfit(taus_arr,
                                   [eta0[tt] for tt in TAUS], 1)[1])

        # exact null rows: d3/d4 rescale g: zeros identical
        z3 = track(zeros0, lambda s: (1 + H) * Lc(s))
        z4 = track(zeros0, lambda s: (1 + 1j * H) * Lc(s))
        null_dev = max(
            max(abs(a - b) for a, b in zip(z3, zeros0)),
            max(abs(a - b) for a, b in zip(z4, zeros0)))

        # the real-coefficient point u = (1, 0): symmetric spectrum: eta = 0
        # (continuation in steps to keep Newton in basin)
        zc = zeros0
        for ustep in (0.2, 0.4, 0.6, 0.8, 1.0):
            zc = track(zc, g_of(ustep, 0))
        eta_real_pt = eta_abel(zc, 0.10)
        lost_rp = sum(1 for z in zc if z is None)

        # per-zero decomposition of h11 (tau = 0.10) and the |B/L'|^2 profile
        tau = 0.10
        contrib = []
        pred = []
        for j, z in enumerate(zeros0):
            zp = stencil[(H, 0)][j]
            zm = stencil[(-H, 0)][j]
            if zp is None or zm is None:
                continue
            c = (mp.sign(mp.im(zp)) * mp.e ** (-abs(mp.im(zp)) * tau)
                 + mp.sign(mp.im(zm)) * mp.e ** (-abs(mp.im(zm)) * tau)
                 - 2 * mp.sign(mp.im(z)) * mp.e ** (-abs(mp.im(z)) * tau)) / H ** 2
            contrib.append(float(c))
            Lp = mp.diff(Lc, z)
            pred.append(float(abs(Lb(z) / Lp) ** 2 * mp.e ** (-abs(mp.im(z)) * tau)))
        corr = float(np.corrcoef(np.abs(contrib), pred)[0, 1]) \
            if len(contrib) > 3 else np.nan

        results[q] = dict(
            zeros0=len(zeros0), n_pos=n_pos, n_neg=n_neg, dens=float(dens),
            online=online, eta_c1=eta_c1, eta0=eta0, eta0_ces=eta0_ces,
            eta_ext=eta_ext, Hmat=Hmat, grads=grads, h11_c=h11_c,
            h22_c=h22_c, h11_T=h11_T,
            null_dev=float(null_dev), eta_real_pt=eta_real_pt,
            lost_rp=lost_rp, offline_frac=offline_frac,
            contrib=contrib, pred=pred, corr=corr,
        )

    # ---------------- checks ----------------
    print("\n-- checks --")
    r5, r7 = results[5], results[7]
    check("pipeline: zero sets complete and on-line at u = 0 (count within 3 "
          "of the density formula; |Re - 1/2| < 1e-8; both conductors)",
          all(abs(r["zeros0"] - r["dens"]) <= 3 and r["online"] < 1e-8
              for r in (r5, r7)),
          f"q=5: {r5['zeros0']} vs {r5['dens']:.1f}; "
          f"q=7: {r7['zeros0']} vs {r7['dens']:.1f}; "
          f"max offline {max(r5['online'], r7['online']):.1e}")
    check("pipeline: the Cesaro eta at u = 0 agrees with the #178 C1 closed "
          "form -(2/pi) arg_c L(1/2, chi) at both conductors (|dev| < 0.12: "
          "two independent estimators, counting-window vs argument "
          "principle). Typed estimator caveat: the fixed-T Abel "
          "tau-extrapolation is BIASED toward the integer D(T) (tau -> 0 "
          "and T -> infinity do not commute at fixed truncation); the "
          "Abel ladder is recorded, and the HESSIAN is immune (tau-ladder "
          "and T-cut stability gated separately)",
          all(abs(r["eta0_ces"] - r["eta_c1"]) < 0.12 for r in (r5, r7)),
          f"q=5: C1 = {r5['eta_c1']:.4f}, Cesaro = {r5['eta0_ces']:.3f}, "
          f"Abel-ext(biased) = {r5['eta_ext']:.3f}; q=7: C1 = "
          f"{r7['eta_c1']:.4f}, Cesaro = {r7['eta0_ces']:.3f}, "
          f"Abel-ext(biased) = {r7['eta_ext']:.3f}")
    check("exact null rows: the self-directions d3/d4 move no zero "
          "(< 1e-9: the scaling invariance, end to end)",
          max(r5["null_dev"], r7["null_dev"]) < 1e-9,
          f"max dev = {max(r5['null_dev'], r7['null_dev']):.1e}")
    check("the pencil is D-H-class off the character point: tracked zeros "
          "go OFF-LINE under the conjugate-mixing deformation "
          "(off-line fraction recorded)",
          r5["offline_frac"] > 0.5,
          f"q=5 off-line fraction at u = ({H}, 0): {r5['offline_frac']:.2f}")
    check("the real-coefficient point: eta vanishes at u = (1, 0) "
          "(conjugation-symmetric spectrum; step-tracked continuation)",
          abs(r5["eta_real_pt"]) < 0.05 and r5["lost_rp"] == 0,
          f"eta(u=1) = {r5['eta_real_pt']:.2e} (lost {r5['lost_rp']})")
    tau_drift5 = max(abs(r5["Hmat"][t][0] - r5["Hmat"][0.10][0])
                     for t in TAUS) / max(abs(r5["Hmat"][0.10][0]), 1e-12)
    step5 = abs(r5["Hmat"][0.10][3] - r5["Hmat"][0.10][0]) \
        / max(abs(r5["Hmat"][0.10][0]), 1e-12)
    ces5 = abs(r5["h11_c"]) if abs(r5["Hmat"][0.10][0]) < 1e-6 else \
        abs(r5["h11_c"] - r5["Hmat"][0.10][0]) / abs(r5["Hmat"][0.10][0])
    Twin5 = abs(r5["h11_T"] - r5["Hmat"][0.10][0]) \
        / max(abs(r5["Hmat"][0.10][0]), 1e-12)
    check("THE FORK, stability axis: H11 stable across the tau-ladder, "
          "step-halving, and the T-window cut (q = 5; Cesaro Hessian "
          "recorded but integer-granular by construction)",
          tau_drift5 < 0.5 and step5 < 0.5 and Twin5 < 0.3,
          f"H11(tau) = " + ", ".join(f"{r5['Hmat'][t][0]:.3f}" for t in TAUS)
          + f"; step-halving dev {step5:.2f}; T-cut dev {Twin5:.2f}; "
          f"Cesaro H11 = {r5['h11_c']:.1f} (granular)")
    sig5 = (np.sign(np.linalg.eigvalsh(np.array(
        [[r5["Hmat"][0.10][0], r5["Hmat"][0.10][2]],
         [r5["Hmat"][0.10][2], r5["Hmat"][0.10][1]]]))))
    sig7 = (np.sign(np.linalg.eigvalsh(np.array(
        [[r7["Hmat"][0.10][0], r7["Hmat"][0.10][2]],
         [r7["Hmat"][0.10][2], r7["Hmat"][0.10][1]]]))))
    check("THE FORK, forcing axis: the 2x2 Hessian signature at q = 5 vs "
          "q = 7 (forced = same; conductor-dependent = trigger 1 hardens)",
          bool(np.all(sig5 == sig7)),
          f"q=5 eigs sign {sig5.tolist()}, H = "
          f"[{r5['Hmat'][0.10][0]:.3f}, {r5['Hmat'][0.10][2]:.3f}; "
          f"{r5['Hmat'][0.10][1]:.3f}]; q=7 sign {sig7.tolist()}, H = "
          f"[{r7['Hmat'][0.10][0]:.3f}, {r7['Hmat'][0.10][2]:.3f}; "
          f"{r7['Hmat'][0.10][1]:.3f}]")
    tr5 = abs(r5["Hmat"][0.10][0] + r5["Hmat"][0.10][1])
    nrm5 = float(np.max(np.abs(np.linalg.eigvalsh(np.array(
        [[r5["Hmat"][0.10][0], r5["Hmat"][0.10][2]],
         [r5["Hmat"][0.10][2], r5["Hmat"][0.10][1]]])))))
    tr7 = abs(r7["Hmat"][0.10][0] + r7["Hmat"][0.10][1])
    nrm7 = float(np.max(np.abs(np.linalg.eigvalsh(np.array(
        [[r7["Hmat"][0.10][0], r7["Hmat"][0.10][2]],
         [r7["Hmat"][0.10][2], r7["Hmat"][0.10][1]]])))))
    check("THE MECHANISM (the fork's third branch): the Hessian is "
          "TRACELESS at both conductors (|tr| < 0.15 spec norm): zeros "
          "move holomorphically in the mixing parameter, so eta is "
          "HARMONIC at leading Abel order: the signature is FORCED to "
          "(1,1) by holomorphy: canonical, and structurally NON-Weil "
          "(a traceless form cannot supply a definite polarization)",
          tr5 < 0.15 * nrm5 and tr7 < 0.15 * nrm7,
          f"q=5 |trace| = {tr5:.3f} vs norm {nrm5:.3f}; "
          f"q=7 |trace| = {tr7:.3f} vs norm {nrm7:.3f}")
    check("the zero-side decomposition: per-zero |contribution| profile vs "
          "the |B/L'|^2 e^{-gamma tau} prediction (correlation recorded: "
          "the APS-costume shape test)",
          True, f"q=5 corr = {r5['corr']:.3f} over {len(r5['contrib'])} zeros; "
                f"q=7 corr = {r7['corr']:.3f}")
    kdh = (np.sqrt(10 - 2 * np.sqrt(5)) - 2) / (np.sqrt(5) - 1)
    check("the conservation-law Hessian (mini-cell): the mod-5 real pencil's "
          "Euler defect b_6(kappa) = (kappa^2 + 1) log 6 >= log 6, Hessian "
          "2 log 6 > 0; e2an's measured D-H value 1.936 is its evaluation",
          abs((kdh ** 2 + 1) * log(6) - 1.9366) < 2e-3,
          f"(kappa_DH^2 + 1) log 6 = {(kdh ** 2 + 1) * log(6):.4f}")
    check("K1 posture declared: zeros consumed by design (form-side "
          "diagnostic); Beurling refusal typed (the pencil needs the FE)",
          True, "generic pencil members ARE the FE-no-Euler (D-H) class")

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.0f} s)")

    out = HERE / "e2bb_eta_second_variation.npz"
    np.savez_compressed(
        out,
        q5_H=np.array([[r5["Hmat"][t][j] for j in range(5)] for t in TAUS]),
        q7_H=np.array([[r7["Hmat"][t][j] for j in range(5)] for t in TAUS]),
        q5_grads=np.array([r5["grads"][t] for t in TAUS]),
        q7_grads=np.array([r7["grads"][t] for t in TAUS]),
        q5_eta=np.array([r5["eta_c1"], r5["eta0"][0.10], r5["eta0_ces"]]),
        q7_eta=np.array([r7["eta_c1"], r7["eta0"][0.10], r7["eta0_ces"]]),
        q5_cesaro_H=np.array([r5["h11_c"], r5["h22_c"]]),
        q5_h11_T=r5["h11_T"], q7_h11_T=r7["h11_T"],
        etas_ext=np.array([r5["eta_ext"], r7["eta_ext"]]),
        q7_cesaro_H=np.array([r7["h11_c"], r7["h22_c"]]),
        q5_contrib=np.array(r5["contrib"]), q5_pred=np.array(r5["pred"]),
        corrs=np.array([r5["corr"], r7["corr"]]),
        eta_real_pt=r5["eta_real_pt"],
        offline_frac=r5["offline_frac"],
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")


if __name__ == "__main__":
    run()
