"""D4b: the D4 loop scaled up to a neural autoregressive policy over FULL Frobenius matrices.

Companion to [`d4_lean_policy_gradient.py`](d4_lean_policy_gradient.py). That rehearsal used a
tabular policy over a single integer (the trace t), with the canonical companion matrix and the
purpose-built `companion_degForm_nonneg` shortcut. This module is the upgrade Owen asked for:
make the action space "genuinely the proof object." The policy now emits a full integer matrix
A = !![a, b; c, d] one entry at a time (an autoregressive trajectory of construction tokens),
and the Lean reward is the GENERAL theorem `functionfield_RH_elliptic_of_matrix` applied to A
directly, with a real general-matrix proof (reduce det(m·1+n·A) via `det_smul_one_add_smul`, then
complete the square), NOT the companion shortcut.

Two things get genuinely harder, by design:

  1. The action space is 4-dimensional and the FEASIBLE set is sparse. The Lean theorem needs
     `det A = p` (an exact equality the policy must hit by choosing a*d - b*c = p) on top of the
     Hasse bound `(tr A)^2 <= 4p`. So the proxy is now

         the Lean file typechecks  <=>  isprime(p) AND det A = p AND (tr A)^2 <= 4p.

     (Confirmed by a live `lake env lean` run on the non-companion witness A = !![2,1;-1,2],
     p=5: clean, exit 0. The companion shortcut is unused; the proof discharges the general
     degree form.)

  2. The policy is a small neural net (1 hidden layer, tanh) decoding autoregressively, trained
     by REINFORCE with a per-prime baseline and Adam. The gradient is still grad_theta log pi
     (off the analytic data), but now it must learn the det = p manifold, which a per-entry
     independent tabular policy cannot represent. Dense shaping (-|det - p| and a Hasse penalty)
     supplies a gradient toward feasibility; the hard (Lean) reward is the spike on it.

This sharpens F1 of the rehearsal: the loop still works, now on an action space that is the
actual proof object and a feasible set the policy has to discover rather than enumerate. F2/F3
(D-H by exclusion, the Spec(Z) kernel cliff) are unchanged and live in the sibling module.

Run: python -m experiments.gradient_descent.d4b_neural_matrix_policy
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from sympy import isprime

from experiments.gradient_descent.d4_lean_policy_gradient import frobenius_eigs
from experiments.lemma_db import shadow_battery as sb


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
ENTRY_MAX = 6
ENTRY_VALUES = list(range(-ENTRY_MAX, ENTRY_MAX + 1))  # the per-entry token vocabulary
N_ENTRIES = 4  # a, b, c, d

CACHE_DIR = Path(__file__).resolve().parent / "_cache"

# Reward weights.
LAM_HARD = 3.0
W_DET = 1.0
W_HASSE = 1.0
W_DETHIT = 1.0   # bonus for landing exactly on the det = p manifold (the hard equality)


# ---------------------------------------------------------------------------
# The reward (full matrix). Hard = the GENERAL Lean theorem typechecks (proxied).
# ---------------------------------------------------------------------------

def matrix_det_trace(a: int, b: int, c: int, d: int) -> tuple:
    return a * d - b * c, a + d


def lean_valid_matrix(a: int, b: int, c: int, d: int, p: int) -> bool:
    """The EXACT predicate the general-matrix Lean instantiation typechecks under.

    `functionfield_RH_elliptic_of_matrix hp hdet hpos hα` at A = !![a,b;c,d] has three numeric
    obligations: `Nat.Prime p`, `A.det = p` (i.e. a*d - b*c = p), and (inside `hpos`, via
    `det_smul_one_add_smul` + the completed square) `(tr A)^2 <= 4p`. Everything else is fixed.
    So it typechecks iff isprime(p) and det = p and tr^2 <= 4p. Faithful, non-circular proxy of
    the Lean typecheck (confirmed live on the non-companion witness A=!![2,1;-1,2], p=5)."""
    det, tr = matrix_det_trace(a, b, c, d)
    return bool(isprime(p) and det == p and tr * tr <= 4 * p)


def reward_matrix(a: int, b: int, c: int, d: int, p: int) -> tuple:
    """Returns (reward, hard). Dense shaping pulls det -> p and tr into the Hasse band; the
    hard (Lean) reward is the spike when both land and p is prime."""
    det, tr = matrix_det_trace(a, b, c, d)
    hard = 1.0 if lean_valid_matrix(a, b, c, d, p) else 0.0
    det_pen = -abs(det - p) / p
    hasse_pen = -max(0, tr * tr - 4 * p) / (4 * p)
    det_hit = W_DETHIT if det == p else 0.0
    r = LAM_HARD * hard + W_DET * det_pen + W_HASSE * hasse_pen + det_hit
    return r, hard


def coverage_of(a: int, b: int, c: int, d: int, p: int) -> float:
    """Shadow-battery CP-fq coverage for the matrix's Frobenius eigenvalues (dense, optional)."""
    det, tr = matrix_det_trace(a, b, c, d)
    if det <= 0:
        return 0.0
    eigs = frobenius_eigs(tr, det)
    cand = sb.BatteryCandidate(node_id="m", spec={"CP-fq": (det, eigs)}, euler_gated=True)
    return sb.score(cand).coverage


# ---------------------------------------------------------------------------
# The neural autoregressive policy. Shared 1-hidden-layer MLP; emits a,b,c,d in
# sequence, each conditioned on (prime, step, prefix). REINFORCE + Adam.
# ---------------------------------------------------------------------------

N_P = len(PRIMES)
N_V = len(ENTRY_VALUES)
D_IN = N_P + N_ENTRIES + N_ENTRIES  # one-hot prime, one-hot step, normalized prefix
H = 128


def _features(pi: int, step: int, prefix: list) -> np.ndarray:
    x = np.zeros(D_IN)
    x[pi] = 1.0
    x[N_P + step] = 1.0
    for i, v in enumerate(prefix):
        x[N_P + N_ENTRIES + i] = v / ENTRY_MAX
    return x


@dataclass
class Net:
    W1: np.ndarray
    b1: np.ndarray
    W2: np.ndarray
    b2: np.ndarray

    @classmethod
    def init(cls, rng: np.random.Generator) -> "Net":
        return cls(
            W1=rng.normal(0, 1 / np.sqrt(D_IN), (H, D_IN)),
            b1=np.zeros(H),
            W2=rng.normal(0, 1 / np.sqrt(H), (N_V, H)),
            b2=np.zeros(N_V),
        )

    def forward(self, x: np.ndarray) -> tuple:
        h = np.tanh(self.W1 @ x + self.b1)
        logits = self.W2 @ h + self.b2
        logits -= logits.max()
        e = np.exp(logits)
        probs = e / e.sum()
        return h, probs


class Adam:
    def __init__(self, params: list, lr: float = 3e-3):
        self.lr = lr
        self.m = [np.zeros_like(p) for p in params]
        self.v = [np.zeros_like(p) for p in params]
        self.t = 0

    def step(self, params: list, grads: list) -> None:
        self.t += 1
        for i, (p, g) in enumerate(zip(params, grads)):
            self.m[i] = 0.9 * self.m[i] + 0.1 * g
            self.v[i] = 0.999 * self.v[i] + 0.001 * (g * g)
            mhat = self.m[i] / (1 - 0.9 ** self.t)
            vhat = self.v[i] / (1 - 0.999 ** self.t)
            p -= self.lr * mhat / (np.sqrt(vhat) + 1e-8)


def sample_trajectory(net: Net, pi: int, rng: np.random.Generator) -> tuple:
    """Emit (a,b,c,d) autoregressively. Returns (entries, steps) where steps is the per-token
    cache (x, h, probs, action_idx) needed for the REINFORCE backward pass."""
    prefix: list = []
    steps = []
    for k in range(N_ENTRIES):
        x = _features(pi, k, prefix)
        h, probs = net.forward(x)
        ai = int(rng.choice(N_V, p=probs))
        steps.append((x, h, probs, ai))
        prefix.append(ENTRY_VALUES[ai])
    return prefix, steps


def reinforce_grads(net: Net, steps: list, advantage: float, beta: float = 0.0) -> list:
    """Accumulate dL/dparams for one trajectory, loss = -advantage*sum_k log pi(a_k) - beta*H(pi).
    The entropy term (beta) keeps the policy from collapsing prematurely onto a single matrix
    before it has found the sparse det = p manifold for the larger primes."""
    dW1 = np.zeros_like(net.W1); db1 = np.zeros_like(net.b1)
    dW2 = np.zeros_like(net.W2); db2 = np.zeros_like(net.b2)
    for x, h, probs, ai in steps:
        dlogits = advantage * probs.copy()
        dlogits[ai] -= advantage  # advantage * (probs - onehot)
        if beta:
            logp = np.log(probs + 1e-12)
            ent = -np.sum(probs * logp)
            dlogits += beta * probs * (logp + ent)  # descent grad of -beta*H
        dW2 += np.outer(dlogits, h)
        db2 += dlogits
        dh = net.W2.T @ dlogits
        dpre = dh * (1 - h * h)
        dW1 += np.outer(dpre, x)
        db1 += dpre
    return [dW1, db1, dW2, db2]


def train(updates: int = 10000, batch: int = 64, lr: float = 3e-3, seed: int = 0,
          beta0: float = 0.06) -> tuple:
    """REINFORCE + Adam with two stabilizers: an annealed entropy bonus (beta0 -> 0) and an
    ADAPTIVE CURRICULUM that oversamples the primes the policy is currently failing. The largest
    prime has the sparsest det = p set (det = p is sparse precisely because p is prime), so a
    difficulty-weighted prime distribution spends the compute where the feasible set is hardest
    to find, rather than uniformly."""
    rng = np.random.default_rng(seed)
    net = Net.init(rng)
    opt = Adam([net.W1, net.b1, net.W2, net.b2], lr=lr)
    baseline = np.zeros(N_P)
    succ = np.zeros(N_P)  # per-prime hard-success EMA, drives the curriculum
    curve = []
    for it in range(updates):
        beta = beta0 * max(0.0, 1.0 - it / (0.8 * updates))
        w = (1.0 - succ) + 0.15
        w /= w.sum()
        gW1 = np.zeros_like(net.W1); gb1 = np.zeros_like(net.b1)
        gW2 = np.zeros_like(net.W2); gb2 = np.zeros_like(net.b2)
        hits = 0
        for _ in range(batch):
            pi = int(rng.choice(N_P, p=w))
            p = PRIMES[pi]
            entries, steps = sample_trajectory(net, pi, rng)
            r, hard = reward_matrix(*entries, p)
            adv = r - baseline[pi]
            baseline[pi] += 0.02 * (r - baseline[pi])
            succ[pi] += 0.02 * (hard - succ[pi])
            g = reinforce_grads(net, steps, adv, beta)
            gW1 += g[0]; gb1 += g[1]; gW2 += g[2]; gb2 += g[3]
            hits += int(hard)
        scale = 1.0 / batch
        opt.step([net.W1, net.b1, net.W2, net.b2],
                 [gW1 * scale, gb1 * scale, gW2 * scale, gb2 * scale])
        if (it + 1) % 100 == 0:
            curve.append((it + 1, hits / batch))
    return net, curve


def greedy_decode(net: Net, pi: int) -> list:
    prefix: list = []
    for k in range(N_ENTRIES):
        x = _features(pi, k, prefix)
        _, probs = net.forward(x)
        prefix.append(ENTRY_VALUES[int(np.argmax(probs))])
    return prefix


def greedy_eval(net: Net) -> tuple:
    rows = []
    for pi, p in enumerate(PRIMES):
        a, b, c, d = greedy_decode(net, pi)
        det, tr = matrix_det_trace(a, b, c, d)
        rows.append((p, (a, b, c, d), det, tr, lean_valid_matrix(a, b, c, d, p)))
    acc = sum(1 for *_, v in rows if v) / len(rows)
    return acc, rows


def sample_feasible_rate(net: Net, n: int = 400, seed: int = 1) -> list:
    """Per-prime: fraction of n sampled matrices that are Lean-valid (the policy's hit-rate at
    temperature 1, a fairer measure than greedy for a stochastic policy)."""
    rng = np.random.default_rng(seed)
    rates = []
    for pi, p in enumerate(PRIMES):
        hits = 0
        for _ in range(n):
            entries, _ = sample_trajectory(net, pi, rng)
            hits += int(lean_valid_matrix(*entries, p))
        rates.append((p, hits / n))
    return rates


# ---------------------------------------------------------------------------
# Tier two: emit a Lean file with the GENERAL-matrix proof for each witness.
# ---------------------------------------------------------------------------

_LEAN_HEADER = """\
import ZetaRH.FunctionFieldRH

open ZetaRH.FunctionFieldRH
open ZetaRH.IsogenyDegree

/- Auto-generated by experiments/gradient_descent/d4b_neural_matrix_policy.py (tier-two
   validation). Each example instantiates `functionfield_RH_elliptic_of_matrix` at a FULL
   integer matrix A = !![a,b;c,d] (NOT the companion) emitted by the neural policy. The proof
   discharges the general degree form via `det_smul_one_add_smul` and a completed square, so it
   typechecks IFF p prime, det A = p, and (tr A)^2 <= 4p. -/
"""

_LEAN_EXAMPLE = """\
-- p={p}: A = !![{a},{b};{c},{d}], det = {det}, trace = {tr}, Hasse {tr}^2 = {trsq} <= 4*{p} = {fourp}
example (α : ℂ)
    (hα : α ∈ spectrum ℂ
      ((!![{a}, {b}; {c}, {d}] : Matrix (Fin 2) (Fin 2) ℤ).map (Int.castRingHom ℂ))) :
    Complex.normSq α = (({p} : ℕ) : ℝ) := by
  set A : Matrix (Fin 2) (Fin 2) ℤ := !![{a}, {b}; {c}, {d}] with hA
  have hp : ({p} : ℕ).Prime := by norm_num
  have htr : A.trace = ({tr} : ℤ) := by rw [hA]; simp [Matrix.trace_fin_two]
  have hq : A.det = ({p} : ℤ) := by rw [hA]; simp [Matrix.det_fin_two]
  have hdet : A.det = (({p} : ℕ) : ℤ) := by rw [hq]; norm_num
  have hpos : ∀ m n : ℤ, 0 ≤ (m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).det := by
    intro m n
    rw [det_smul_one_add_smul, htr, hq]
    nlinarith [sq_nonneg (2 * m + ({tr} : ℤ) * n),
      mul_nonneg (show (0 : ℤ) ≤ 4 * ({p} : ℤ) - ({tr} : ℤ) ^ 2 by norm_num) (sq_nonneg n)]
  exact functionfield_RH_elliptic_of_matrix hp hdet hpos hα
"""


def write_lean_validation_file(witnesses: list, path: Path) -> Path:
    """witnesses = list of (a,b,c,d,p). Emits the general-matrix proof for each."""
    blocks = [_LEAN_HEADER]
    for a, b, c, d, p in witnesses:
        det, tr = matrix_det_trace(a, b, c, d)
        blocks.append(_LEAN_EXAMPLE.format(a=a, b=b, c=c, d=d, p=p, det=det, tr=tr,
                                           trsq=tr * tr, fourp=4 * p))
    path.write_text("\n".join(blocks), encoding="utf-8")
    return path


def demo() -> int:
    CACHE_DIR.mkdir(exist_ok=True)
    print("D4b: neural autoregressive policy over FULL Frobenius matrices (route A, scaled up)\n")
    print(f"  Action: emit A = !![a,b;c,d], entries in [{-ENTRY_MAX},{ENTRY_MAX}], one token at a time.")
    print("  Hard reward proxy: general-matrix Lean typecheck  <=>  p prime AND det A = p AND tr^2 <= 4p.")
    print("  (Confirmed live: lake env lean on non-companion A=!![2,1;-1,2], p=5 -> clean, exit 0.)\n")

    net, curve = train()
    acc, rows = greedy_eval(net)
    print("  TRAINING (REINFORCE + Adam on a 1-hidden-layer policy net)")
    marks = [curve[i] for i in (0, len(curve) // 4, len(curve) // 2, 3 * len(curve) // 4, -1)]
    print("    batch hard-hit-rate:  " + "  ".join(f"it{e}:{h:.2f}" for e, h in marks))
    print(f"    greedy policy accuracy over {len(PRIMES)} primes: {acc:.0%}")
    print("    learned matrices (p: A=[a,b;c,d], det, trace, valid):")
    for p, (a, b, c, d), det, tr, v in rows:
        flag = "ok" if v else "MISS"
        print(f"      p={p:2d}: [{a:+d},{b:+d};{c:+d},{d:+d}]  det={det:+d}  tr={tr:+d}  [{flag}]")

    rates = sample_feasible_rate(net)
    mean_rate = sum(r for _, r in rates) / len(rates)
    print(f"    sampled feasible-rate (temp 1, 400 draws/prime): mean {mean_rate:.2f}")
    misses = [(p, det) for p, _, det, _, v in rows if not v]
    if misses:
        print("    misses (the sparse-target finding): " +
              ", ".join(f"p={p} -> det={det}" for p, det in misses))
        print("      the largest prime is the hardest: det=p is sparse precisely because p is")
        print("      prime (few a*d-b*c = p), while the nearby COMPOSITE determinant has many")
        print("      matrix representations, so the policy is pulled into the denser basin.")

    witnesses = [(a, b, c, d, p) for p, (a, b, c, d), _, _, v in rows if v]
    lean_path = CACHE_DIR / "d4b_validation_witnesses.lean"
    write_lean_validation_file(witnesses, lean_path)
    print(f"\n  Tier-two Lean validation file written ({len(witnesses)} non-companion witnesses):")
    print(f"    {lean_path}")
    print("    Validate with:  cd lean; lake env lean " + str(lean_path).replace('\\', '/'))

    np.savez(CACHE_DIR / "d4b_curves.npz",
             curve=np.array(curve, dtype=float),
             feasible_rates=np.array(rates, dtype=float))

    print("\n  Net: the policy now generates the actual proof OBJECT (a full integer matrix) one")
    print("  token at a time and must discover the sparse det=p AND Hasse feasible set; the")
    print("  gradient is still grad_theta log pi, off the analytic data. Same escape from")
    print("  marginal-positivity flatness, now on an action space that is genuinely the proof.")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
