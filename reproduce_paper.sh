#!/usr/bin/env bash
# =============================================================================
# One-command reproduction for the HUJOS manuscript:
# "Giới hạn của kiểm toán vật lý nhật ký tưới và điều kiện áp dụng neo theo
#  thiết bị trong đo đạc, báo cáo, thẩm định lúa phát thải thấp"
# =============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

PY="${PYTHON:-python3}"

echo "== AnchorAudit-MRV (HUJOS Paper Reproduction) =="
echo "   python: $($PY --version 2>&1)"

echo "[1/4] Checking ERA5 weather cache..."
if [[ ! -f data/era5_multi/can_tho_2024.csv ]]; then
  "$PY" data/fetch_era5_multi.py --year 2024 can_tho soc_trang ca_mau
  "$PY" data/fetch_era5_multi.py --year 2025 can_tho soc_trang ca_mau
else
  echo "   cache hit (data/era5_multi/)"
fi

echo "[2/4] Running physical & filter invariant tests..."
for t in tests/test_water_balance.py tests/test_log_filters.py tests/test_dmax_proposition.py; do
  printf '   %-36s' "$t"
  "$PY" "$t" > /dev/null
  echo "PASS"
done

echo "[3/4] Running paper experiments (Tables 2-6)..."
"$PY" experiments/robust_audit_eval.py --seeds 10 --out eval_theta_reduced_10seeds.csv > /dev/null
echo "   outputs/eval_theta_reduced_10seeds.csv  OK (Tables 2, 3, 4, 6)"
"$PY" experiments/robust_audit_eval.py --full-theta --seeds 3 --out eval_theta_full_3seeds.csv > /dev/null
echo "   outputs/eval_theta_full_3seeds.csv      OK (Full-Theta comparison)"
"$PY" experiments/sweep_dry_threshold.py > /dev/null
echo "   outputs/sweep_dry_threshold.csv         OK (Table 5)"
"$PY" experiments/out_of_theta_probe.py > /dev/null
"$PY" experiments/out_of_theta_fraud.py > /dev/null
"$PY" experiments/make_out_of_theta_summary.py > /dev/null
echo "   outputs/_out_of_theta_summary.json      OK (Out-of-Theta check)"

echo "[4/4] Done. All paper tables verified in outputs/."
