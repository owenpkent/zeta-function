#!/usr/bin/env bash
# Lean 4 smoke test for the ZetaRH project.
#
# Checks whether the Lean skeleton parses and builds (even with sorry-stubs).
# Useful as a quick sanity check after edits to lean/ZetaRH/ files.
#
# Usage:
#   bash lean/smoke_test.sh
#
# Exits 0 if Lean is installed and the skeleton builds; 1 if not installed
# or build fails. Prints diagnostic output either way.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "[Lean smoke test] working dir: $SCRIPT_DIR"

# Check for elan / lean
if ! command -v lean &> /dev/null; then
    echo "[Lean smoke test] STATUS: lean not found in PATH"
    echo ""
    echo "  Lean 4 / Mathlib is required to run the formal verification stack."
    echo "  Install via elan (https://leanprover-community.github.io/get_started.html):"
    echo ""
    echo "    Windows:  curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh"
    echo "    Mac:      brew install elan-init"
    echo "    Linux:    curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh"
    echo ""
    echo "  After elan is installed, re-run this script. elan will install the"
    echo "  Lean version specified in lean-toolchain on first build."
    echo ""
    echo "  This is NOT a build failure; this is a prerequisite check."
    exit 1
fi

LEAN_VERSION="$(lean --version 2>&1 | head -n 1)"
echo "[Lean smoke test] Lean version: $LEAN_VERSION"

if ! command -v lake &> /dev/null; then
    echo "[Lean smoke test] STATUS: lake not found in PATH"
    echo "  lake should come with Lean 4. Check your elan / Lean installation."
    exit 1
fi

LAKE_VERSION="$(lake --version 2>&1 | head -n 1)"
echo "[Lean smoke test] Lake version: $LAKE_VERSION"

# Try to fetch dependencies (Mathlib) if not already present
if [ ! -d ".lake" ]; then
    echo "[Lean smoke test] No .lake directory found. Fetching dependencies (this can take 10-30 min on first run)..."
    if ! lake update 2>&1 | tail -20; then
        echo "[Lean smoke test] STATUS: lake update failed"
        exit 1
    fi
fi

# Attempt the build. With sorry-stubs everywhere, we expect successful
# compilation but with sorry warnings, not failures.
echo "[Lean smoke test] Running lake build..."
BUILD_OUTPUT=$(lake build 2>&1)
BUILD_STATUS=$?

if [ $BUILD_STATUS -eq 0 ]; then
    echo "[Lean smoke test] STATUS: BUILD SUCCEEDED"
    echo ""
    # Count sorry warnings
    SORRY_COUNT=$(echo "$BUILD_OUTPUT" | grep -c "sorry" || true)
    echo "  Build succeeded with $SORRY_COUNT sorry warnings (expected at this skeleton stage)."
    echo ""
    echo "  Modules built:"
    find ZetaRH -name "*.lean" | sort | sed 's/^/    /'
    echo ""
    echo "  Next steps for VERIFIER agents: replace sorry stubs with real proofs."
    echo "  See lean/README.md and lean/ZetaRH/*.lean for the theorem statements."
    exit 0
else
    echo "[Lean smoke test] STATUS: BUILD FAILED"
    echo ""
    echo "  Build output (last 50 lines):"
    echo "$BUILD_OUTPUT" | tail -50 | sed 's/^/    /'
    echo ""
    echo "  Common causes of failure:"
    echo "    - Mathlib not fetched: run 'lake update' first."
    echo "    - Mathlib version mismatch: check lean-toolchain matches Mathlib's expected version."
    echo "    - Syntax error in lean/ZetaRH/*.lean: re-read the failing module."
    exit 1
fi
