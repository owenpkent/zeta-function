"""Zero-cache builder for B2c-deep2: all zeros to T = 600 at 110 digits.
Run: python -m experiments.arithmetic_geometric._e2au_zeros
Writes experiments/_shared/_cache/zeros_dps110_T1500.json (regenerable)."""

import json
import time
from pathlib import Path

import mpmath as mp

CACHE = Path(__file__).resolve().parent.parent / "_shared" / "_cache" / "zeros_dps110_T1500.json"
DPS, T = 110, 1500.0

mp.mp.dps = DPS
done = []
if CACHE.exists():
    done = json.loads(CACHE.read_text())
    print(f"resuming from {len(done)} cached zeros")
out = [mp.mpf(s) for s in done]
k = len(out) + 1
t0 = time.time()
while True:
    g = mp.im(mp.zetazero(k))
    if g > T:
        break
    out.append(g)
    if k % 10 == 0:
        CACHE.write_text(json.dumps([mp.nstr(x, DPS) for x in out]))
        print(f"  {k} zeros, t = {float(g):.1f}  ({time.time() - t0:.0f} s)", flush=True)
    k += 1
CACHE.write_text(json.dumps([mp.nstr(x, DPS) for x in out]))
print(f"done: {len(out)} zeros to T = {T} at {DPS} digits  ({time.time() - t0:.0f} s)")
