#!/usr/bin/env bash
# Cross-machine replication suite (2026-08-31): full-mode runs of
# e1ad_sum_rules, e1v_christoffel_gauge, e1ae_prony_horizon, e2bg_coupled_sp4
# on this Linux box, to fill the PHASE_STATE "cross-machine replication"
# sliver. Runs sequentially, does NOT stop on failure, records a one-line
# PASS/FAIL/MISMATCH verdict per module by grepping the printed N/N count
# against the pre-registered expectation (e1ae's expectation is 6/7: a
# known-failing check that is itself the finding, not a bug).

set -u

REPO_ROOT="/home/owen/dev/zeta-function"
PY="$REPO_ROOT/.venv/bin/python"
DATE_TAG="2026-08-31"

SPEC_CACHE="$REPO_ROOT/experiments/spectral/_cache"
AG_CACHE="$REPO_ROOT/experiments/arithmetic_geometric/_cache"
mkdir -p "$SPEC_CACHE" "$AG_CACHE"

SUMMARY="$SPEC_CACHE/replication_${DATE_TAG}_summary.log"
: > "$SUMMARY"

cd "$REPO_ROOT" || { echo "FATAL: cannot cd to $REPO_ROOT"; exit 1; }

run_module () {
  local label="$1" module="$2" logfile="$3" expect="$4"
  echo "=== $label: starting $(date -Is) ===" | tee -a "$SUMMARY"
  local t0 t1 dur rc found status
  t0=$(date +%s)
  nice -n 10 "$PY" -m "$module" > "$logfile" 2>&1
  rc=$?
  t1=$(date +%s)
  dur=$((t1 - t0))
  found=$(grep -Eo '[0-9]+/[0-9]+ passed' "$logfile" | tail -1)
  if [ "$found" = "$expect" ]; then
    status="PASS"
  elif [ -n "$found" ]; then
    status="MISMATCH"
  else
    status="FAIL"
  fi
  echo "[$status] $label: exit=$rc found='${found:-none}' expect='$expect' duration=${dur}s log=$logfile" | tee -a "$SUMMARY"
}

run_module "e1ad_sum_rules" \
  "experiments.spectral.e1ad_sum_rules" \
  "$SPEC_CACHE/e1ad_sum_rules_full_${DATE_TAG}.log" \
  "21/21 passed"

run_module "e1v_christoffel_gauge" \
  "experiments.spectral.e1v_christoffel_gauge" \
  "$SPEC_CACHE/e1v_christoffel_gauge_full_${DATE_TAG}.log" \
  "26/26 passed"

run_module "e1ae_prony_horizon" \
  "experiments.spectral.e1ae_prony_horizon" \
  "$SPEC_CACHE/e1ae_prony_horizon_full_${DATE_TAG}.log" \
  "6/7 passed"

run_module "e2bg_coupled_sp4" \
  "experiments.arithmetic_geometric.e2bg_coupled_sp4" \
  "$AG_CACHE/e2bg_coupled_sp4_full_${DATE_TAG}.log" \
  "10/10 passed"

echo "=== suite complete $(date -Is) ===" | tee -a "$SUMMARY"
