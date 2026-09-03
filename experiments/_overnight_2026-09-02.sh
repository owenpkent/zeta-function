#!/usr/bin/env bash
# Overnight sweep (2026-09-02): re-run every experiment that used the Epstein
# control above the height where the old module was inaccurate (LEARNINGS #217,
# TODO "Epstein control defect"), plus two pencil extensions. Jobs run in
# parallel (mpmath is single-threaded; 8 cores here), each under its own
# timeout, each to its own log under a gitignored _cache/ dir. Tracked npz
# outputs ARE overwritten by their scripts: that is the point of the re-run;
# review with git diff, nothing is committed by this script.

set -u
REPO_ROOT="/home/owen/dev/zeta-function"
PY="$REPO_ROOT/.venv/bin/python"
TAG="2026-09-02"
cd "$REPO_ROOT" || exit 1
mkdir -p experiments/positivity/_cache experiments/arithmetic_geometric/_cache experiments/criticality/_cache
LEDGER="$REPO_ROOT/overnight_runs_${TAG}.txt"
SUMMARY="$REPO_ROOT/experiments/positivity/_cache/overnight_${TAG}_summary.log"
: > "$LEDGER"; : > "$SUMMARY"

launch () {
  # launch <label> <logfile> <timeout-seconds> <expect-note> <command...>
  local label="$1" log="$2" tmo="$3" note="$4"; shift 4
  ( t0=$(date +%s)
    nice -n 10 timeout "$tmo" "$@" > "$log" 2>&1
    rc=$?
    t1=$(date +%s)
    echo "$label | rc=$rc | $((t1 - t0)) s | $(date -Is)" >> "$SUMMARY"
  ) &
  echo "$label | PID $! | log $log | timeout ${tmo}s | $note" >> "$LEDGER"
}

# J1: e3l with the fixed module (Schur-count law vs the full certified list).
launch "J1 e3l_epstein_control" experiments/positivity/_cache/e3l_overnight_${TAG}.log 14400 \
  "expect ~1 h; PASS iff Schur neg count = off-line heights for principal d=-15 (4) and non-principal (1)" \
  "$PY" -m experiments.positivity.e3l_epstein_control
# J2: e3n at the height the LEARNINGS #27 record used (120); the d=47 principal control is RH-false there.
launch "J2 e3n_li_signature T=120" experiments/positivity/_cache/e3n_overnight_${TAG}.log 43200 \
  "expect ~3-4 h; does the RH-true-but-fails contrast survive with the corrected label" \
  "$PY" -m experiments.positivity.e3n_li_signature --T-max 120
# J3: e3m place-type balance, default T_max=200.
launch "J3 e3m_place_type_balance" experiments/positivity/_cache/e3m_place_overnight_${TAG}.log 43200 \
  "expect ~5 h; the Selberg-like contrast row is now an RH-false object" \
  "$PY" -m experiments.positivity.e3m_place_type_balance
# J4, J5: the Rosati balance separators M2 and M2.5, default T_max=200.
launch "J4 e2u_rosati_balance_M2" experiments/arithmetic_geometric/_cache/e2u_overnight_${TAG}.log 43200 \
  "expect ~5 h; the balance >= 1 verdict on the principal form" \
  "$PY" -m experiments.arithmetic_geometric.e2u_rosati_balance_M2
launch "J5 e2v_rosati_balance_M2_5" experiments/arithmetic_geometric/_cache/e2v_overnight_${TAG}.log 43200 \
  "expect ~5-10 h (multi-T validation); A_bomb residual convergence" \
  "$PY" -m experiments.arithmetic_geometric.e2v_rosati_balance_M2_5
# J6: the four-way M2.6 pass; T_hi reduced 500 -> 300 for the night (the corrected
# evaluate() costs seconds per value at height 500; the 500 pass is a multi-day job).
launch "J6 e2w_rosati_fourway_M2_6 T_hi=300" experiments/arithmetic_geometric/_cache/e2w_overnight_${TAG}.log 43200 \
  "expect ~8 h; T_hi=300 not 500, say so in any write-up" \
  "$PY" -m experiments.arithmetic_geometric.e2w_rosati_fourway_M2_6 --T-hi 300
# J7: the octave ladder's zero side (non-principal d=47 to 200), separate npz suffix so the tracked file survives.
launch "J7 e3dd_edc_octave_ladder" experiments/positivity/_cache/e3dd_overnight_${TAG}.log 43200 \
  "expect ~5 h; Part B zero side with the corrected d=47 non-principal list; suffix _refit${TAG}" \
  "$PY" -m experiments.positivity.e3dd_edc_octave_ladder --part B --suffix "_refit${TAG}"
# J8: pencil extensions: the wide lambda grid (both ends of the pencil) and the d=-20 replicate at T=60 in a killable subprocess.
launch "J8 euler_pencil wide lambda + d20" experiments/criticality/_cache/pencil_wide_overnight_${TAG}.log 14400 \
  "expect ~30 min; S1 at lambda = +-2..+-128 (off-line zeros should thin toward lambda=inf too), then d=-20 at T=60" \
  bash -c "$PY -c 'from experiments.criticality.e_euler_pencil import run_s1; import time; run_s1(-15, [2.0,-2.0,4.0,-4.0,8.0,-8.0,16.0,-16.0,32.0,-32.0,64.0,-64.0,128.0,-128.0], 200.0, \"flint\", time_budget=3000, t0=time.time(), notes=[])' ; timeout 3000 $PY -m experiments.criticality.e_euler_pencil --d20-only 60 2400"

wait
echo "ALL JOBS FINISHED $(date -Is)" >> "$SUMMARY"
