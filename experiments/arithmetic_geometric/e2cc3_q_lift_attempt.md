# 2CC.3 — Trying the q-lift (probe a): the formal half is doable, the global half is the gap

> Direction 8 / the q-lift, the live route after [2CC](e2cc_tropical_shadow.md) #40 and
> [2CC.2](e2cc2_ideps_vonmangoldt.md) #41. Code: [`e2cc3_q_lift_attempt.py`](e2cc3_q_lift_attempt.py).
> This is an honest **attempt** at probe (a) (un-idempotent-ize the C-C square). It decomposes
> the q-lift and crosses the formal/per-prime parts but not the central global part.

## The attempt

2CC found the C-C square's tropical operations are idempotent → no subtraction → the
mixed-volume Hodge index is arithmetic-blind (froze the trace t). The proposed fix (the
"q-lift"): un-idempotent-ize the operations (go from the q→1 characteristic-1 limit back to
genuine arithmetic) and see whether a signed pairing + the trace re-emerge.

## What the attempt achieves, and where it stops

**(1) Un-idempotent-ization — DONE (formal).** Tropical `max` is the β→∞ limit of the soft-max
`a ⊕_β b = (1/β)log(e^{βa}+e^{βb})`. For finite β it is **not idempotent** (`a⊕_β a = a +
(log2)/β ≠ a`), so genuine addition / a Grothendieck completion / **subtraction exists**. The
2CC idempotency obstruction is *formally removable* — a signed pairing becomes possible.

**(2) Per-prime lift — KNOWN.** At a single scale q the un-idempotent-ized form **is** the
finite-q function-field Hodge index (2G): `Δ·Γ = q+1−t`, signature `(1,3) ⟺ |t| < 2g√q`. It
carries the trace. So per place the lift is the known FF form. The obstruction is **global**:
Spec(ℤ) has no single q (#25/2Q).

**(3) The global half — THE GAP (unchanged).** The zeros of ζ — the H¹ whose signature is RH —
live in the **analytic continuation** (Re(s) < 1), where the C-C local data **cannot reach**.
Concretely, the Euler product / orbit spectrum `∏ₚ(1−p⁻ˢ)⁻¹ = ∑Λ(n)n⁻ˢ` converges **only for
Re(s) > 1** (where ζ has no zeros). On the critical line it does **not converge** (at the
generic point s = ½+20i the partial products oscillate 1.30, 1.05, 1.84, 0.40 — no limit;
because ∑ₚ p^{−1/2} diverges). So ζ on Re(s)=½ comes from the *continuation* (functional
equation / archimedean place), **not** the local prime product — and the local C-C/orbit data
is therefore **blind to the zeros**. Realizing that continuation as a **signed pairing** on the
zeros is the missing Weil cohomology = M3/#25.

| s | partial Euler product \|∏_{p≤P}\| (P = 10²…10⁵) | \|ζ(s)\| | |
|---|---|---|---|
| Re = 2.0 | 1.642, 1.645, 1.645, 1.645 | 1.6449 | **converges** |
| Re = ½, t = 20 | 1.30, 1.05, 1.84, 0.40 | 1.148 | **does not converge** |
| Re = ½, t = 14.13 (ζ = 0) | 0.115, 0.061, 0.023, 0.013 | 0.0000 | does not converge |

**(4) K2.** Davenport-Heilbronn has no Euler product → no local orbit data to lift at all
(#41: Λ_DH delocalizes off prime powers; no per-place (1,p) structure).

## Verdict

The q-lift **decomposes** into three parts, and the attempt crosses the first two:
1. **un-idempotent-ization** (soft-max) — formal, done; the idempotency obstruction is removed;
2. **per-prime lift** — the finite-q FF Hodge index (2G), carries t — known;
3. **global assembly** — realize the analytic continuation (the zeros at Re(s)=½, invisible to
   the local Euler/orbit data) as a signed pairing on the H¹ = **the missing Weil cohomology**.

Part 3 is the central gap (M3/#25), **unchanged**. The attempt's value is **localizing** it
sharply: the obstruction is not the idempotency *per se* (removable) and not the per-prime
structure (known), but the **local-to-global continuation** — turning the prime/orbit data
(which lives in Re(s)>1) into the global zeros (Re(s)=½) with a signed pairing. The archimedean
place (A_arch #34; the Γ-factor intrinsic to the C-C site, reading note #5) is the carrier of
the continuation; the gap is its **signed pairing**.

This is consistent with the whole session: the realization / trace / local data is buildable
(here, even the un-idempotent-ization is formal), but the **signature** — the global positivity
on the H¹ that encodes |α|=√q / Re(ρ)=½ — is the irreducible content, and it is exactly what
the local tropical/orbit structure cannot supply.

## Honest scope
- Probe (a) is **not crossed**: the attempt sharpens the gap (localizes it to the local-to-global
  continuation) but does not construct the Weil cohomology / the signed pairing. No new theorem.
- The "Euler product blind to the zeros" demonstration is the classical fact that the product
  converges only for Re(s)>1; the contribution here is tying it to the q-lift decomposition and
  the C-C local data as the precise reason the local route stops at Re(s)=1.

## Pointers
- LEARNINGS #42 (this), #41 (Id_ε trace), #40 (2CC), #34 (A_arch / archimedean dominance), #25 (the bidegree obstruction), #20 (D-H delocalization).
- 2CC / 2CC.2 / 2G / 2Q / 2R; Connes-Consani reading note (the square; §4 Γ-factor; the signed-pairing gap, point #7).
