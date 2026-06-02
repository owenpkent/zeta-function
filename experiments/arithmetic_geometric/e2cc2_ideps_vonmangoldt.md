# 2CC.2 — The Connes-Consani self-composition Id_ε carries the von Mangoldt trace (not the signature)

> Direction 8 / the q-lift (follows [2CC](e2cc_tropical_shadow.md) #40). Probes the diagonal
> self-intersection where 2CC probed the off-diagonal. Code: [`e2cc2_ideps_vonmangoldt.py`](e2cc2_ideps_vonmangoldt.py).
> A connecting/refining coordinate: ~80% confirmatory of [2R](e2r_dynamical_zeta.md) / LEARNINGS #20,
> with new content in the off-diagonal-vs-diagonal contrast and the Id_ε = flow-generator reading.

## The probe

2CC found the C-C square's tropical mixed-volume form is arithmetic-blind: the **off-diagonal**
point count Δ·Γ_p froze at the tropical value p−1 (= q+1−t with t=2), losing the Frobenius
trace. Owen's question: does the **diagonal** self-composition, Connes-Consani's
Ψ(λ)∘Ψ(λ⁻¹) = Id_ε (Thm 7.7, the tangential deformation of the identity), carry the von
Mangoldt / −ζ'/ζ spectrum that 2R pinned as Γ_S²?

**Answer: yes — as the trace.** The Id_ε tangent is
`d/dε [l_ε(qⁿ)/r_ε(qⁿ)]|₀ = d/dε q^{εn}|₀ = n·log q` — the **number / scaling operator** n,
which is the Deninger-Hesselholt **flow generator Θ** (Θ(v) = (2πi/log q)v, q^Θ = Fr; #29).
And `−d/ds log det_∞(s−Θ) = −d/ds log ∏ₚ(1−p⁻ˢ)⁻¹ = −ζ'/ζ(s) = ∑ₙ Λ(n)n⁻ˢ`. The C-C
multiplicative composition `Fr_{1,p}∘…∘Fr_{1,p} = Fr_{1,pᵏ}` (slope pᵏ) is exactly the iterate
structure of the primitive orbit at p: the prime slopes {p} are the primitive periodic orbits,
log-scales {log p}. So Id_ε (the diagonal anomaly) carries the full von Mangoldt arithmetic.

## Results

| # | What | Result |
|---|---|---|
| 1 | C-C prime-slope dynamical zeta | ∏ₚ(1−p⁻ˢ)⁻¹ = ζ(2) (rel err 4.6e-6, converging); −ζ'/ζ = ∑Λ(n)n⁻ˢ (von Mangoldt, **0 off-prime-power leaks** below 200). Reproduces 2R, now tied to the C-C composition law. |
| 2 | **Contrast (refines 2CC)** | off-diagonal Δ·Γ_p = **p−1** (t-frozen tropical shadow); self-intersection coefficient = **Λ(p) = log p** (trace-rich). The diagonal sees the arithmetic the off-diagonal lost. |
| 3 | K2 (Davenport-Heilbronn) | Λ_DH delocalizes onto composites: mass 37.4 off prime powers vs 36.9 on (n≤60), **first leak n=6** (matches 2R/#20 exactly) → no primitive {log p} orbit structure → no Id_ε / flow spectrum. |

(The N=200 von-Mangoldt-sum vs −ζ'/ζ rel err 0.84% is series truncation, not a discrepancy; the identity is classical.)

## The finding (honest)

**Id_ε carries the von Mangoldt / −ζ'/ζ spectrum, as the TRACE.** Its tangent is the flow
generator Θ; the von Mangoldt sum is `−d/ds log det_∞(s−Θ)` — a **determinant / trace**, the
realization of ζ as a flow-determinant. This is the **easy half** ("all roads to the
signature," #30): the realization is buildable; the signature is not. The von Mangoldt sum is
**not a Hodge index**; RH is the signature of the H¹ / TP_odd / numerator (2S), which the C-C
square still lacks (2CC: no signed pairing).

**It refines 2CC** by locating where the arithmetic survives on the C-C square: the **diagonal
self-intersection** (Id_ε, the fixed-point/tangential anomaly) is trace-rich and carries
−ζ'/ζ, whereas the **off-diagonal point count** degenerated to the t-frozen tropical shadow.
So the trace is accessible (via the diagonal anomaly / the flow); the **q-lift gap is
unchanged**: turn the Id_ε trace into a Hodge-index signature (supply the numerator/H¹ that
carries |α|=√q). The probe connects **C-C (Id_ε) ↔ 2R (dynamical zeta) ↔ Deninger/Hesselholt
(Θ, det_∞)** — three realizations of the same trace, none of them the signature.

## Honest scope

- The Id_ε = Θ identification is a **structural reading** (the tangent IS the number operator;
  identifying it with Deninger's flow generator is the natural/consistent reading per #29), not
  a theorem proved inside the C-C framework. The *computed* facts are the classical dynamical-zeta
  identities, the off-diagonal/diagonal contrast, and the D-H delocalization (the latter reproducing
  2R/#20).
- This is a **connecting/refining coordinate**, mostly confirmatory: it does not advance past the
  q-lift gap, it sharpens *where* the trace lives (diagonal) vs where it froze (off-diagonal) and
  confirms the trace/signature dichotomy from the self-intersection side.

## Pointers
- LEARNINGS #41 (this), #40 (2CC), #26 (2R dynamical zeta), #20 (D-H delocalization), #29 (Hesselholt det_∞(s−Θ)), #30 (all roads to the signature).
- 2CC ([e2cc_tropical_shadow.md](e2cc_tropical_shadow.md)), 2R ([e2r_dynamical_zeta.md](e2r_dynamical_zeta.md)), reading note Connes-Consani-2015 (Thm 7.7, Id_ε; point #4).
- References: Connes-Consani, arXiv:1502.05580 (2015), Thm 7.7 / Def 7.6; Hesselholt, *THH and the Hasse-Weil zeta function*; Deninger, regularized determinants.
