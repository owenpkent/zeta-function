"""
FRONT 1: carrier-spectrum severance, made concrete on the BEST candidate carrier.

The carrier is the universal elliptic curve / Kuga-Sato variety over a modular
curve, whose middle cohomology genuinely REALIZES a modular form's L-function via
Eichler-Shimura. The question Front 1 asks: does Yuan-Zhang's arithmetic Hodge
index theorem on THIS carrier POLARIZE the same data that Eichler-Shimura realizes
(=> a route to RH for L(f)), or does the polarization always attach to the
carrier's OWN height / Neron-Severi data, never to the L-function's zeros?

Two spaces, two pairings:

  REALIZE side  : Frobenius eigenvalues alpha_p, beta_p on the (k-1)-dimensional
                  Eichler-Shimura Galois piece of H^{k-1}_et. For weight k,
                  |alpha_p| = |beta_p| = p^{(k-1)/2} (Deligne / Ramanujan), and
                  the char polys det(1 - Frob_p p^{-s}) reassemble L(f,s), hence
                  the L-zeros. SCALE = p^{(k-1)/2}, p-DEPENDENT (the (1,p)
                  bidegree, LEARNINGS #25).
  POLARIZE side : Neron-Tate / Yuan-Zhang height pairing on ARITHMETIC cycles
                  (sections, CM / Heegner points) in CH-hat. Values are O(1)
                  transcendental regulators, the carrier's OWN arithmetic data.

Worked at weight 2 (f = newform of an elliptic curve E; the universal elliptic
curve over X_0(N) is the Kuga-Sato carrier; H^1 of a fiber = H^1(E)), so the
L-function IS L(E,s) and both sides are computable exactly.

K1-clean: zeta's / L's zeros never enter; only a_p (point counts) and the
Neron-Tate regulator (the carrier's height) are used.
"""
import mpmath as mp
mp.mp.dps = 40

# Carrier: E = 37a1 (conductor 37, weight-2 newform f_37). The Kuga-Sato carrier
# is the universal elliptic curve over X_0(37); H^1 of a fiber = H^1(E).
# Eichler-Shimura: a_p(f) = a_p(E) = p + 1 - #E(F_p) = trace of Frob_p on H^1(E).
ap_37a1 = {2:-2, 3:-3, 5:-2, 7:-1, 11:-5, 13:-2, 17:0, 19:0,
           23:2, 29:6, 31:-4, 41:-9, 43:2}
reg_37a1 = mp.mpf('0.051111')   # <P,P>, P=(0,0), the YZ-polarized pairing value


def realize_side():
    print("REALIZE side (the L-function's data; lives in H^1_et, the Galois rep):")
    print(f"{'p':>4} {'a_p':>5} {'|alpha_p|^2':>12} {'disc=a^2-4p':>12} {'roots':>9}")
    for p in sorted(ap_37a1):
        ap = ap_37a1[p]
        disc = ap * ap - 4 * p
        absq = str(p) if disc < 0 else "n/a"
        rt = "complex" if disc < 0 else "real"
        print(f"{p:>4} {ap:>5} {absq:>12} {disc:>12} {rt:>9}")
    print("=> |alpha_p| = sqrt(p) on every good p: the Hasse/Ramanujan circle =")
    print("   per-prime RH for L(f). Eigenvalue SCALE = p^{1/2}, p-dependent.")


def polarize_side():
    print("POLARIZE side (Yuan-Zhang / Faltings-Hriljac on the carrier's CYCLES):")
    print(f"  Neron-Tate regulator <P,P> on MW(E) = {reg_37a1}")
    print("  YZ-positive-definite value: O(1), transcendental, p-independent.")
    print("  It is the carrier's OWN height datum (an Arakelov self-intersection).")


def severance():
    print("SEVERANCE (scale comparison):")
    print(f"  REALIZE scale at p : p^(1/2)  (p=43 -> {float(mp.sqrt(43)):.6f})")
    print(f"  POLARIZE scale     : O(1) regulator {float(reg_37a1):.6f}")
    print(f"  ratio (p=43)       : {float(mp.sqrt(43)/reg_37a1):.2e}  (diverges with p)")
    print("  No fixed F with YZ_pairing = F(alpha_p) for all p: the polarized")
    print("  value does not grow with p; the eigenvalue scale does.")
    print()
    print("DIMENSIONAL / SPACE separation (the exact obstruction):")
    print("  Eichler-Shimura realizes alpha_p, beta_p as eigenvalues of Frob_p on")
    print("    H^1_et(E_Qbar, Q_l)  (2-dim Galois module; the L-zero carrier).")
    print("  Yuan-Zhang polarizes")
    print("    CH-hat^1(E)_0  (degree-0 arithmetic divisors; height pairing).")
    print("  DIFFERENT objects on the same carrier:")
    print("   - H^1_et: Frobenius is the operator; char poly = L-factor;")
    print("     eigenvalue moduli = RH-for-f content.")
    print("   - CH-hat^1_0: YZ pairing = arithmetic intersection of 1-cycles;")
    print("     signature (neg-def primitive) = the polarization.")
    print("  Frobenius does NOT act on CH-hat^1_0 as the polarized spectrum.")
    print("  The polarization sees HEIGHTS (Arakelov degrees), not eigenvalues.")


if __name__ == "__main__":
    bar = "=" * 72
    print(bar)
    print("CARRIER = universal elliptic curve over X_0(37) (Kuga-Sato, weight 2)")
    print(bar); print()
    realize_side(); print()
    polarize_side(); print()
    severance()
