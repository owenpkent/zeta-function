# Setup

How to bring a fresh machine up to a working state for both threads of this repo: the Python experimental thread and the Lean 4 / Mathlib formalization. The commands below are the exact procedure verified working on Windows 11 (PowerShell) on 2026-07-06.

Two independent stacks. You can install either one alone.

- **Python** drives everything under `experiments/` and `visualizations/`.
- **Lean 4 + Mathlib** drives `lean/`.

## Prerequisites

- **Windows** with `winget` (App Installer). On other platforms use the equivalent package manager or the official installers linked below.
- **git** (already required to clone this repo).
- Disk: the Mathlib olean cache is a few GB. Confirm you have headroom before the Lean step.

## Python stack

```powershell
# 1. Install a real Python 3.12 (per-user, no admin prompt).
winget install --id Python.Python.3.12 --scope user --silent --accept-package-agreements --accept-source-agreements

# 2. Open a NEW terminal so the updated PATH takes effect, then from the repo root:
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Verify (should print `Smoke test: 9/9 passed`):

```powershell
python -m experiments._shared.smoke_test
```

Confirmed working versions (2026-07-06): Python 3.12.10, numpy 2.5.1, scipy 1.18.0, mpmath 1.3.0, sympy 1.14.0, matplotlib 3.11.0, cvxpy 1.9.2, manim 0.20.1, plus pdfminer.six, pypdf, duckdb. See `requirements.txt` for the pinned minimums.

### Linux / macOS: use the virtualenv, and call it by path

On a non-Windows host the deps normally live in a repo-local virtualenv rather than on the system
interpreter:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m experiments._shared.smoke_test    # expect 9/9
```

Run every command in this repo as `.venv/bin/python -m ...` from the repo root (or activate the
venv first). Two traps, both of which make a healthy tree look broken:

- There may be no bare `python` on PATH at all, only `python3`. The `python -m ...` form used
  throughout this repo's docs is the Windows form.
- The system `python3` will import fine but have none of the deps, so
  `python3 -m experiments.run_all_tests` reports something like `4/15 modules fully passed` with
  every numeric module raising `ModuleNotFoundError: No module named 'mpmath'`. That is the wrong
  interpreter, not a regression. Under `.venv/bin/python` the same tree is 15/15.

### Windows gotcha: the Microsoft Store python stub

Windows ships a stub `python.exe` in `...\WindowsApps` that redirects to the Store and is NOT a real interpreter. After the winget install above, a fresh shell resolves the real Python because its directory sits earlier on PATH. If `python` ever opens the Store or prints "Python was not found," that is a PATH-order regression: either the real `...\Programs\Python\Python312` entry is missing from PATH, or the App Execution Alias for `python` needs disabling under Settings > Apps > Advanced app settings > App execution aliases.

## Lean 4 / Mathlib stack

Lean is managed by `elan` (the toolchain manager, analogous to rustup). The project pins Lean `v4.30.0` and Mathlib `v4.30.0` (see `lean/lean-toolchain` and `lean/lakefile.lean`); elan installs the right toolchain automatically on first use.

```powershell
# 1. Install elan (the Lean toolchain manager).
winget install --id Lean.Elan --silent --accept-package-agreements --accept-source-agreements

# 2. If elan/lake/lean are not on PATH afterward, bootstrap the canonical layout once:
#    (creates %USERPROFILE%\.elan\bin and adds it to PATH)
#    Run the elan-init.exe that winget placed under
#    %LOCALAPPDATA%\Microsoft\WinGet\Packages\Lean.Elan_*  with:
#        elan-init.exe -y --default-toolchain none
#    Non-Windows: use the official installer at https://github.com/leanprover/elan

# 3. Open a NEW terminal (PATH refresh), then build from the lean directory:
cd lean
lake exe cache get   # REQUIRED: downloads prebuilt Mathlib oleans (~minutes)
lake build           # builds the ZetaRH library
```

`lake exe cache get` is not optional in practice: it downloads the prebuilt Mathlib object files. Skip it and `lake build` will compile Mathlib from source, which takes roughly an hour. A successful build ends with `Build completed successfully (3752 jobs).`

Note: the Lean build prints many `declaration uses 'sorry'` and deprecation warnings. These are expected. The `sorry`s are the intentional research skeletons (HodgeIndex, PrismaticCohomology, LambdaBlueprints, and others); they are not build failures. Every module compiles.

## Running things

Working directory is the repo root for Python (imports resolve as `from experiments._shared import ...`), and `lean/` for Lake. See the "Running things" section of `CLAUDE.md` for common experiment invocations.
