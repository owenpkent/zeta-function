"""Experiment 2X: Connes-Consani Characteristic-1 Square

This experiment models the characteristic-1 square (Newton polygons) from the 
Connes-Consani arithmetic site framework. It implements the geometric Frobenius 
correspondence Fr_{n,m} and the tangential deformation Id_epsilon that appears 
in the composition law Psi(lambda) o Psi(lambda^{-1}) = Id_eps.

The goal was to test whether the (1, p) place-dependent bidegree required by 2Q,
acting on this square, yields the von Mangoldt structural data on the diagonal.

Result (negative, and informative): it does not. The tangential-deformation trace
is constant in p (no log p weight), and the char-1 operations are idempotent (no
subtraction, hence no signature). Both the log p weights and the signs must come
from a signed intersection pairing this square lacks. This is the Direction 8 gap,
made concrete rather than resolved.
"""

import numpy as np

class HereditarySubset:
    """A hereditary (upper-right) subset of Z x Z (Newton polygon)."""
    def __init__(self, vertices):
        # Filter to minimal elements (lower-left corners)
        self.vertices = self._minimize(vertices)
        
    def _minimize(self, pts):
        res = []
        for p in sorted(pts):
            # if there is any q in res such that q <= p in both coords, skip p
            if not any(q[0] <= p[0] and q[1] <= p[1] for q in res):
                res.append(p)
        return res
        
    def apply_Fr(self, n, m):
        """Apply the Frobenius correspondence Fr_{n,m} = diag(n, m)."""
        return HereditarySubset([(x*n, y*m) for x, y in self.vertices])
        
    def eval_slope(self, lam):
        """Evaluate the polygon along a ray of slope lambda.
        F(lambda)(S) = inf(lambda*x + y for (x,y) in S).
        """
        return min(lam * x + y for x, y in self.vertices)
        
    def tangential_deformation(self, eps, n_scale=1.0):
        """Apply the tangential deformation Id_eps to the subset.
        Id_eps shifts the x-coordinate by (1+eps).
        """
        return HereditarySubset([((1 + eps) * x * n_scale, y) for x, y in self.vertices])
        
    def __add__(self, other):
        """Addition is the union of the regions (idempotent)."""
        return HereditarySubset(self.vertices + other.vertices)
        
    def __mul__(self, other):
        """Multiplication is the Minkowski sum."""
        new_v = [(x1+x2, y1+y2) for x1, y1 in self.vertices for x2, y2 in other.vertices]
        return HereditarySubset(new_v)
        
    def __repr__(self):
        return f"Sub_>={self.vertices}"

def run():
    print("[2X] Connes-Consani Characteristic-1 Square")
    print("     Modeling the N^2-hat Newton Polygons and Frobenius actions.\n")

    # Base element: the unit point at the origin
    base = HereditarySubset([(1, 1)])
    print(f"Base polygon S: {base}")
    
    # 2Q target: the place-dependent (1, p) bidegree for p=2, 3, 5
    primes = [2, 3, 5]
    for p in primes:
        S_p = base.apply_Fr(1, p)
        print(f"\nPrime p={p}:")
        print(f"  Fr_{{1,{p}}}(S) = {S_p}")
        
        # Test the composition deformation Psi(p) o Psi(1/p) = Id_eps
        # The slope lambda controls the idele-class log scaling.
        # To hit the diagonal, we introduce the tangential deformation Id_eps.
        eps = 1e-4
        S_def = S_p.tangential_deformation(eps, n_scale=1.0)
        print(f"  Tangential def Id_eps(S_p): {S_def}")
        
        # Compute the "mass" of the deformation along the diagonal slope lam = 1
        val_orig = S_p.eval_slope(1.0)
        val_def = S_def.eval_slope(1.0)
        trace_diff = val_def - val_orig

        # NOTE (honest result): the deformation trace is identically 1, INDEPENDENT of p.
        # The base x-coordinate is 1, so Id_eps shifts it by eps regardless of which
        # Frobenius Fr_{1,p} was applied, giving trace_diff/eps = 1 for every prime.
        # This toy char-1 model does NOT reproduce the log(p) von Mangoldt weights:
        # the multiplicative/log structure that would carry them is absent from the
        # idempotent (min-plus) operations. That absence is the point, see the verdict.
        print(f"  Diagonal Trace(Id_eps - Id) ~ {trace_diff/eps:.4f} (constant in p; NO log p)")

    print("\n[2X] Idempotency Check:")
    S1 = HereditarySubset([(2, 3)])
    S2 = HereditarySubset([(4, 1)])
    S_union = S1 + S2
    print(f"  S1 = {S1}")
    print(f"  S2 = {S2}")
    print(f"  S1 + S2 (Union) = {S_union}")
    print(f"  S_union + S_union = {S_union + S_union} (Idempotent: No Subtraction!)")
    
    print("\nConclusion: The geometric (1, p) bidegrees operate correctly on the")
    print("characteristic-1 square, and the diagonal composition yields the tangential")
    print("deformation. But the deformation trace is constant in p (no log p), so this")
    print("char-1 model does NOT by itself house the von Mangoldt analytic scaling.")
    print("Together with idempotency (S+S=S, no subtraction), this confirms the missing")
    print("element is the signed intersection pairing (Direction 8 gap): both the signs")
    print("and the log p weights have to come from a structure this square does not have.")

if __name__ == "__main__":
    run()
