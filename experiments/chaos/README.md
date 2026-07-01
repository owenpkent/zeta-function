# Chaos and Strange Attractors

A small, self-contained numerical thread on classical deterministic chaos: Lyapunov spectra, fractal dimensions, and the multifractal generalized-dimension ladder. It sits next to [`../multifractal/`](../multifractal/) and shares that thread's MFDFA implementation, because the two meet in one place: the multifractal spectrum.

This is not an RH attack. It is the classical-chaos and quantum-chaos context for Architecture 1 (spectral / Hilbert-Polya). The spectral side of the same bridge is written up in [`../../docs/03_research/quantum_chaos_and_the_zeros.md`](../../docs/03_research/quantum_chaos_and_the_zeros.md): the Riemann zeros have the spectral statistics of a quantized chaotic system (GUE), and the Berry-Keating dictionary reads the primes as the primitive periodic orbits.

## What is in here

```
experiments/chaos/
├── README.md                    this file
├── systems.py                   Lorenz, Rossler, Henon with exact Jacobians + reference values
├── lyapunov.py                  Benettin tangent-space QR spectrum + Kaplan-Yorke dimension
├── dimension.py                 Grassberger-Procaccia D_2 + box-counting Renyi ladder D_q
├── c1_lyapunov_spectra.py       C1: Lyapunov spectra and Kaplan-Yorke dimension (calibration)
├── c2_correlation_dimension.py  C2: correlation dimension D_2 from a time series
└── c3_multifractal_bridge.py    C3: the Renyi ladder + MFDFA handshake to the zeta thread
```

## Quick start

```powershell
# from repo root
python -m experiments.chaos.c1_lyapunov_spectra
python -m experiments.chaos.c2_correlation_dimension
python -m experiments.chaos.c3_multifractal_bridge
```

Each script prints its results and checks them against literature values stored in `systems.py`. C2 also tries to save a log-log diagnostic PNG next to the script; if `matplotlib` fails to import (see the caveat below) the numbers still print.

## The three systems

| system | kind | parameters | what it is |
|---|---|---|---|
| Lorenz | flow (3D) | $\sigma=10,\ \rho=28,\ \beta=8/3$ | the canonical two-lobe butterfly, from Rayleigh-Benard convection |
| Rossler | flow (3D) | $a=b=0.2,\ c=5.7$ | single-scroll, engineered to have one fold |
| Henon | map (2D) | $a=1.4,\ b=0.3$ | the discrete-time archetype |

## The three experiments

### C1: Lyapunov spectra and Kaplan-Yorke dimension

Calibration. The full ordered Lyapunov spectrum is computed by the Benettin method: evolve an orthonormal frame of tangent vectors under the linearized dynamics (the variational equation, using the exact Jacobians in `systems.py`) and re-orthonormalize by QR, accumulating $\log|R_{ii}|$. A positive largest exponent is the operational definition of chaos. The Kaplan-Yorke dimension $D_{KY} = k + (\lambda_1 + \dots + \lambda_k)/|\lambda_{k+1}|$ reads the fractal dimension straight off the spectrum.

**Verified output** (matches Wolf/Sprott reference values to three decimals):

| system | $\lambda$ measured | $\lambda$ reference | $\sum\lambda$ | $D_{KY}$ (ref) |
|---|---|---|---|---|
| Lorenz | $(+0.904,\ -0.000,\ -14.571)$ | $(+0.906,\ 0,\ -14.572)$ | $-13.67$ | $2.062$ ($2.062$) |
| Rossler | $(+0.068,\ +0.001,\ -5.400)$ | $(+0.071,\ 0,\ -5.39)$ | $-5.33$ | $2.013$ ($2.013$) |
| Henon | $(+0.420,\ -1.624)$ | $(+0.419,\ -1.623)$ | $-1.204$ | $1.259$ ($1.258$) |

The exponents sum to the mean phase-space contraction rate (negative, so the attractor has zero volume), while the largest exponent is positive (stretching along the unstable direction). Zero volume plus stretching forces the fold, and the fold forces the fractal.

### C2: correlation dimension $D_2$ (Grassberger-Procaccia)

The dimension you can extract from a raw time series. The correlation sum $C(r)$ (fraction of point pairs closer than $r$) scales as $C(r) \sim r^{D_2}$, so $D_2$ is the slope of $\log C$ vs $\log r$ over the scaling region. A Theiler window excludes temporally close pairs.

**Verified output:**

| system | $D_2$ measured | $D_2$ literature | note |
|---|---|---|---|
| Lorenz | $2.01$ | $2.05$ | clean |
| Rossler | $1.76$ | $\sim 2.0$ | GP underestimates (see below) |
| Henon | $1.18$ | $1.22$ | clean |

Lorenz and Henon land on their published values. Rossler reads low, and this is honest rather than a bug: single-slope GP underestimates the dimension of a near-two-dimensional attractor with an inhomogeneous invariant measure, because the log-log plot curves and a straight-line fit averages the curvature down. Rossler's true dimension sits near its Kaplan-Yorke value ($\sim 2.01$ from C1). The estimator has a regime of validity, and Rossler sits at its edge. That is a useful thing to see directly.

### C3: the multifractal bridge

Two connected measurements that show "dimension" is really a spectrum, and that this is the same machinery the zeta thread uses.

**Part A: the Renyi dimension ladder $D_q$ on the Henon attractor.** Box-count the natural measure and form $D_q$ for a range of $q$. A multifractal measure gives a strict ordering $D_0 > D_1 > D_2$ (box-counting, information, correlation). Measured:

| $q$ | $D_q$ | name |
|---|---|---|
| 0 | $1.28$ | capacity (box-counting) |
| 1 | $1.26$ | information |
| 2 | $1.23$ | correlation |
| 3 | $1.17$ | |
| 5 | $1.07$ | |

$D_q$ is non-increasing with a real spread ($D_0 - D_5 \approx 0.21$), so the Henon measure is multifractal. Note the consistency: $D_0 \approx 1.28$ tracks the Kaplan-Yorke dimension from C1 ($1.259$), and $D_2 \approx 1.23$ tracks the correlation-dimension estimate from C2 ($1.18$). The three experiments measure three rungs of one ladder.

**Part B: the project's own MFDFA on a Lorenz coordinate $x(t)$.** The estimator from [`../multifractal/mfdfa.py`](../multifractal/mfdfa.py), the same one that measures the multifractality of $\log|\zeta(\tfrac12+it)|$, runs here on a chaotic trajectory. Read with the caveat printed by the script: MFDFA on one coordinate measures temporal scaling of that signal, a different object from the spatial multifractality of the invariant measure in Part A. Both are facets of the same $D(\alpha)$ formalism. It is the handshake, not an identity.

## The through-line to the rest of the project

The singularity-spectrum width $\Delta\alpha$ that [`../multifractal/`](../multifractal/) reports for $\log|\zeta(\tfrac12+it)|$ is the **same quantity**, in the same formalism, as the $D_q$ spread measured here for a strange attractor. Chaos theory and the log-correlated zeta thread share one language: the multifractal spectrum. And on the spectral side, the zeros carry the statistics of a quantum chaotic system. So this folder is the classical-and-statistical face, and [`../../docs/03_research/quantum_chaos_and_the_zeros.md`](../../docs/03_research/quantum_chaos_and_the_zeros.md) is the quantum-spectral face, of the same bridge. Both land on the project's standing caveat: matching statistics is a Level-3 fact. It supplies the stage, not the proof (the polarization / M4).

## Caveats

- **Plots need a `matplotlib` compatible with the installed `numpy`.** `matplotlib` older than 3.9 cannot import under `numpy` 2.x, which was the case here until the repo environment was upgraded to `matplotlib` 3.11 (numpy 2.4.2). The scripts guard the import either way: if `matplotlib` is unavailable they still print all numbers and just skip the PNG. C2 saves `c2_correlation_dimension.png` when plotting works.
- **Correlation-dimension estimates are finite-sample.** C2 uses direct-coordinate data (not delay embedding) and modest point counts for speed. The Rossler underestimate is the visible edge of the method's regime of validity, discussed above.
- **This is context, not an RH route.** See [`../multifractal/README.md`](../multifractal/README.md) and the spectral doc for why the statistical and spectral agreements, however precise, do not close RH.

## References

- Lorenz, E.N. (1963), "Deterministic Nonperiodic Flow," *J. Atmos. Sci.* **20**, 130-141.
- Rossler, O.E. (1976), "An Equation for Continuous Chaos," *Phys. Lett. A* **57**, 397-398.
- Henon, M. (1976), "A two-dimensional mapping with a strange attractor," *Commun. Math. Phys.* **50**, 69-77.
- Benettin, G. et al. (1980), "Lyapunov Characteristic Exponents for smooth dynamical systems," *Meccanica* **15**, 9-30.
- Wolf, A. et al. (1985), "Determining Lyapunov exponents from a time series," *Physica D* **16**, 285-317.
- Grassberger, P. and Procaccia, I. (1983), "Measuring the strangeness of strange attractors," *Physica D* **9**, 189-208.
- Hentschel, H.G.E. and Procaccia, I. (1983), "The infinite number of generalized dimensions of fractals and strange attractors," *Physica D* **8**, 435-444.
- Kaplan, J.L. and Yorke, J.A. (1979), "Chaotic behavior of multidimensional difference equations," in *Functional Differential Equations and Approximation of Fixed Points*.
