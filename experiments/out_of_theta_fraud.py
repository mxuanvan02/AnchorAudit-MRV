#!/usr/bin/env python3
"""Ngoài-Theta, phần PHÁT HIỆN: tấn công nhật ký của thửa ngoài Θ.

Bổ sung cho out_of_theta_probe.py (đo báo oan). Ở đây sinh nhật ký trung thực
trên mô hình nước NGOÀI Θ, rồi áp cùng ba kiểu tấn công như bài, và đo xem bộ
kiểm toán đã công bố còn bắt được không.

Mục đích: chứng minh bộ bền vững không phải "an toàn vì mù" — nó vẫn phát hiện
khi bằng chứng vật lý thật sự vi phạm, dù thửa nằm ngoài tập bất định giả định.
"""
from __future__ import annotations

import csv
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments"))

from ncs_loop import load_weather
from log_filters import (FilterConfig, robust_audit, uncertainty_set,
                         tier1_gap_flag, RecordingNoise, max_event_depth)
import reality_gap_probe as rgp
from robust_audit_eval import timing_attack, consolidate
from out_of_theta_probe import build_out_log, OUT_SOIL

START, HOURS = rgp.START, rgp.HOURS
STATIONS = rgp.STATIONS
SMALL_SOILS = (("sandy_loam", 0.21, 0.10),
               ("silty_clay_loam", 0.32, 0.18),
               ("silt_loam", 0.33, 0.15))


def main():
    seeds = 10
    cfg = dict(rgp.CFG_REAL)
    thetas = uncertainty_set(soils=SMALL_SOILS, kc_modes=("fixed", "stage"),
                             etas=(0.60, 1.00))
    w0set = (0.0, 0.90)
    filt = FilterConfig()
    noise = RecordingNoise()
    cap = max_event_depth(filt.infil.default_duration_h, filt.infil)

    rows = []
    for st_name in STATIONS:
        for year in (2024, 2025):
            weather, day_rain = load_weather(st_name, limit=START + HOURS + 20, year=year)
            for seed in range(seeds):
                rng = random.Random(7000 * year + 13 * seed + rgp.station_seed(st_name))
                rec, pumped = build_out_log(rng, weather, cfg)
                if len(rec) < 3:
                    continue

                variants = {}
                # gian lận thô: thêm lệnh vào ngày mưa
                wet = dict(rec)
                rainy = [h for h in range(HOURS)
                         if weather[START + h]["p"] > 5.0 and h not in wet]
                if rainy:
                    for h in rng.sample(rainy, min(8, len(rainy))):
                        wet[h] = wet.get(h, 0.0) + rng.choice((20.0, 40.0, 60.0))
                    variants["fraud_added_events"] = wet

                # gian lận độ sâu không khả thi
                depth = dict(rec)
                keys = sorted(depth)
                for h in rng.sample(keys, max(1, len(keys) // 3)):
                    depth[h] = 160.0
                variants["fraud_infeasible_depth"] = depth

                # tấn công dịch thời điểm (leo đồi)
                tlog, _nd = timing_attack(rec, weather, day_rain, max_depth=cap)
                variants["fraud_timing"] = tlog

                for vname, log in variants.items():
                    changed = int(_norm(log) != _norm(rec))
                    v2 = robust_audit(log, weather, day_rain, START, HOURS,
                                      thetas, filt, w0set)
                    gap = pumped - sum(log.values())
                    t1, _, tau = tier1_gap_flag(pumped, sum(log.values()), len(log), noise)
                    rows.append({
                        "station": st_name, "year": year, "seed": seed,
                        "variant": vname, "changed": changed,
                        "n_claims": len(log), "gap_mm": round(gap, 2),
                        "v1_any": int(abs(gap) > 5.0),
                        "v2_any": int(v2.flagged),
                        "tier1": int(t1),
                    })

    n = len(rows)
    print(f"\n=== NGOAI THETA — PHAT HIEN: {n} bien the ===")
    for v in ("fraud_added_events", "fraud_infeasible_depth", "fraud_timing"):
        sub = [r for r in rows if r["variant"] == v and r["changed"] == 1]
        if not sub:
            print(f"  {v:26s}: khong co ca nao thay doi")
            continue
        k = len(sub)
        print(f"  {v:26s} n={k:2d}  v1={sum(r['v1_any'] for r in sub)}/{k}"
              f"  v2={sum(r['v2_any'] for r in sub)}/{k}"
              f"  tau(n)={sum(r['tier1'] for r in sub)}/{k}")

    out = ROOT / "outputs" / "out_of_theta_fraud.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"\nghi {out}")


def _norm(log):
    return tuple(sorted((h, round(v, 6)) for h, v in log.items() if v > 0))


if __name__ == "__main__":
    main()
