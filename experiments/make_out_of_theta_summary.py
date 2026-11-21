#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tổng hợp thí nghiệm NGOÀI Θ thành outputs/_out_of_theta_summary.json.

VÌ SAO CÓ FILE NÀY
==================
Đoạn "Kiểm tra ngoài Θ" (Mục 3.2) in sáu tỷ lệ: 17/42, 0/42, 1/42 (báo oan trên
nhật ký trung thực) và 6/20, 0/20, 1/20 (phát hiện trên tấn công dịch thời điểm),
cùng 42/42 cho hai kiểu gian lận thô. Các tỷ lệ đó là SỐ DẪN XUẤT: chúng không
nằm nguyên văn trong CSV nào, mà cộng từ cờ của từng dòng. Nếu chỉ commit CSV
thô, người phản biện không tự kiểm được con số in trong bài.

File này cộng lại từ hai CSV do hai script kia ghi ra, và ghi kèm cả đường dẫn
nguồn + số dòng để truy vết. Không có con số nào được nhập tay.

Đầu vào (phải chạy trước, theo đúng thứ tự):
    python experiments/out_of_theta_probe.py    -> outputs/out_of_theta.csv
    python experiments/out_of_theta_fraud.py    -> outputs/out_of_theta_fraud.csv

Chạy:
    python experiments/make_out_of_theta_summary.py
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"

HONEST_CSV = OUT / "out_of_theta.csv"
FRAUD_CSV = OUT / "out_of_theta_fraud.csv"
DEST = OUT / "_out_of_theta_summary.json"

# Nhãn ba tầng đúng như bài in.
TIERS = (
    ("v1_any", "don_cau_hinh_tau0"),
    ("v2_any", "bo_phat_hien_ben_vung"),
    ("tier1", "nguong_ty_le_tau_n"),
)


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        raise SystemExit(
            f"thiếu {path.name} — chạy trước:\n"
            f"    python experiments/out_of_theta_probe.py\n"
            f"    python experiments/out_of_theta_fraud.py"
        )
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def pct(a: int, b: int) -> float:
    return round(100.0 * a / b, 1) if b else 0.0


def main() -> int:
    honest = read_csv(HONEST_CSV)
    fraud = read_csv(FRAUD_CSV)

    n_honest = len(honest)
    honest_out = {}
    for col, label in TIERS:
        c = sum(int(r[col]) for r in honest)
        honest_out[label] = {
            "count": c,
            "n": n_honest,
            "ratio": f"{c}/{n_honest}",
            "percent": pct(c, n_honest),
        }

    detect_out = {}
    for variant in ("fraud_added_events", "fraud_infeasible_depth", "fraud_timing"):
        # Quy ước của bài: mọi thống kê tấn công tính CÓ ĐIỀU KIỆN trên nhật ký
        # thật sự bị sửa (changed == 1).
        sub = [r for r in fraud if r["variant"] == variant and int(r["changed"]) == 1]
        k = len(sub)
        detect_out[variant] = {
            "n": k,
            "changed": sum(int(r["changed"]) for r in fraud if r["variant"] == variant),
            **{
                label: {
                    "count": sum(int(r[col]) for r in sub),
                    "n": k,
                    "ratio": f"{sum(int(r[col]) for r in sub)}/{k}",
                }
                for col, label in TIERS
            },
        }

    doc = {
        "_what": "Tổng hợp thí nghiệm 'kiểm tra ngoài Θ' (Mục 3.2). Mọi giá trị "
                 "cộng từ cờ từng dòng của hai CSV nguồn; không nhập tay.",
        "_source": {
            "honest": "outputs/out_of_theta.csv (experiments/out_of_theta_probe.py)",
            "fraud": "outputs/out_of_theta_fraud.csv (experiments/out_of_theta_fraud.py)",
        },
        "_model_outside_theta": {
            "soil_fc": 0.30,
            "soil_wp": 0.20,
            "root_depth_m": 0.70,
            "kc_fixed": 1.15,
            "seepage_mm_h": 0.05,
            "note": "Bốn tham số sinh nhật ký, nằm ngoài tập bất định Θ của bộ kiểm toán.",
        },
        "false_accusation_honest_outside_theta": honest_out,
        "detection_on_attacks": detect_out,
    }

    DEST.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"=== NGOAI THETA — TONG HOP ({n_honest} nhat ky trung thuc) ===")
    for _, label in TIERS:
        d = honest_out[label]
        print(f"  bao oan  {label:26s}: {d['ratio']:>7s} = {d['percent']:5.1f}%")
    for variant, d in detect_out.items():
        k = d["n"]
        if not k:
            print(f"  {variant:26s}: khong co ca nao thay doi")
            continue
        parts = "  ".join(
            f"{label}={d[label]['count']}/{k}" for _, label in TIERS
        )
        print(f"  {variant:26s} n={k:2d}  {parts}")
    print(f"\nghi {DEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
