#!/usr/bin/env bash
# Chay TAT CA gate cua ban thao bang MOT lenh.
#
# Dung sau moi vong sua, va TRUOC khi dong goi / nop / gui thu tra loi.
# Mot gate FAIL = dung lai va sua, khong di tiep.
#
#   bash check_all.sh            # chay het
#   bash check_all.sh --fast     # bo qua gate cham (build/goi nguon)
#
# Exit 0 = tat ca xanh. Exit 1 = co gate FAIL (in ten gate that).
#
# GHI CHU: bien dem dat ten n_ok / n_fail (khong dung tu 'pass' o vi tri gan)
# vi tang che ky tu cua agent thay 'pass=0' thanh '***' va lam hong cu phap bash.
set -uo pipefail
cd "$(dirname "$0")"

FAST=0
[ "${1:-}" = "--fast" ] && FAST=1

# Thu tu co y: gate re chay truoc de fail som, gate build/goi chay sau.
GATES=(
  check_no_orphan_tex
  check_number_provenance
  check_vi_numbers
  check_supp_vi_numbers
  check_acronym_first_use
  check_vi_title
  check_vi_foreign_chars
  check_abstract_bytes
  negative_control_supp_gate
  measure_page_whitespace
  verify_paper_claims
  audit_all_numbers
)
SLOW=(
  check_latex_source_package
)

n_ok=0
n_fail=0
failed_list=()

run_gate() {
  local g="$1"
  local f="experiments/${g}.py"
  if [ ! -f "$f" ]; then
    printf '  --   %-30s (khong ton tai)\n' "$g"
    return
  fi
  local out rc tail_line
  out=$(timeout 900 python3 "$f" 2>&1)
  rc=$?
  tail_line=$(printf '%s\n' "$out" \
    | grep -E "GATE: PASS|GATE PASS|KET LUAN|claim PASS|khe GIUA trang \(loi that\): 0" \
    | tail -1 | cut -c1-58)
  if [ $rc -eq 0 ]; then
    printf '  OK   %-30s %s\n' "$g" "$tail_line"
    n_ok=$((n_ok + 1))
  else
    printf '  FAIL %-30s %s\n' "$g" "$tail_line"
    printf '%s\n' "$out" | grep -E '^\s+(!!!|paper2|experiments|outputs)' | head -6 | sed 's/^/         /'
    n_fail=$((n_fail + 1))
    failed_list+=("$g")
  fi
}

echo "=== GATE nhanh ==="
for g in "${GATES[@]}"; do run_gate "$g"; done

if [ $FAST -eq 0 ]; then
  echo
  echo "=== Gate cham (build + goi nguon) ==="
  for g in "${SLOW[@]}"; do run_gate "$g"; done
fi

echo
echo "=============================="
echo "  XANH=$n_ok  FAIL=$n_fail"
if [ $n_fail -gt 0 ]; then
  echo "  Gate FAIL: ${failed_list[*]}"
  echo "  => Dung lai. Khong dong goi, khong nop, khong gui thu."
  exit 1
fi
echo "  => Tat ca xanh. Duoc phep dong goi / nop."
exit 0
