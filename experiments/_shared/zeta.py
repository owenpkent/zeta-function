"""The Riemann zeta function as an LFunction.

Wraps mpmath. Zeros are loaded via mp.zetazero, with disk caching of the
high-precision values so we do not recompute across experiments.
"""

from __future__ import annotations

import hashlib
import pickle
from pathlib import Path

import mpmath as mp

from .lfunction import LFunction


CACHE_DIR = Path(__file__).resolve().parent / "_cache"


class ZetaLFunction(LFunction):
    name = "zeta"
    has_euler_product = True
    has_functional_equation = True

    def evaluate(self, s):
        return mp.zeta(s)

    def dirichlet_coefficient(self, n: int):
        return mp.mpc(1) if n >= 1 else mp.mpc(0)

    def zeros(self, T_max: float, prec: int = 30):
        """Non-trivial zeros rho = 1/2 + i*gamma with 0 < gamma <= T_max.

        Cached on disk: (T_max, prec) -> list of mp.mpc.
        Uses mp.zetazero(k) iteratively until gamma exceeds T_max.
        """
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        key = hashlib.sha1(f"zeta|{float(T_max):.6f}|{int(prec)}".encode()).hexdigest()[:16]
        path = CACHE_DIR / f"zeta_zeros_{key}.pkl"
        if path.exists():
            with open(path, "rb") as f:
                return pickle.load(f)

        prev_dps = mp.mp.dps
        mp.mp.dps = max(prec, 30)
        try:
            zeros_list = []
            k = 1
            while True:
                rho = mp.zetazero(k)
                if float(rho.imag) > T_max:
                    break
                zeros_list.append(rho)
                k += 1
                if k > 10_000_000:
                    raise RuntimeError("zeta zero count safety cap hit; raise it if intended")
        finally:
            mp.mp.dps = prev_dps

        with open(path, "wb") as f:
            pickle.dump(zeros_list, f)
        return zeros_list


zeta = ZetaLFunction()
