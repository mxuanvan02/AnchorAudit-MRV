#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ĐỘ NHẠY của chỉ báo n_dry theo ngưỡng đếm pha khô d_dry.

VÌ SAO CÓ FILE NÀY
==================
Bài báo (Mục 2.4 dòng 75, 179) định nghĩa một pha khô là khi độ cạn kiệt
d_t >= d_dry = 0,45 liên tục >= 72 giờ, và tự nhận 0,45 là "quy ước đếm trong
nghiên cứu này". Toàn bộ con số trụ của đóng góp thứ hai — n_dry tăng từ 4,78
lên 6,33 (+33%) trên 9 nhật ký, và bộ phát hiện bền vững bỏ lọt 8/9 — đứng trên
quy ước đó.

Người phản biện (GS1) đặt câu hỏi đổi phán quyết: FAO-56 cho lúa có p = 0,20
(stress bắt đầu khi cạn 20% nước hữu dụng), nên d = 0,45 có thể đang đếm những
quãng "đất còn ẩm" chứ không phải "đã rút nước". Nếu +33% chỉ tồn tại ở d = 0,45
thì kết luận chính phải thu hẹp thành "nhạy với quy ước đếm".

CÁCH LÀM
========
Chạy lại ĐÚNG đường ống của bài (cùng seed, cùng rgp.build_truth, cùng
timing_attack) nhưng thay ngưỡng đếm. Ngưỡng tác động hai chỗ và cả hai đều
được quét:
  1. cách ĐẾM n_dry của nhật ký trung thực và nhật ký bị tấn công;
  2. MỤC TIÊU của hill-climb trong timing_attack (nó tối đa hoá chính n_dry).
Vì (2), mỗi ngưỡng sinh ra một nhật ký tấn công khác nhau — đó là điều đúng:
kẻ tấn công tối ưu theo quy ước đếm đang được dùng.

CỔNG KIỂM CHỨNG: ở ngưỡng 0,45 phải ra lại 4,78 -> 6,33 (+33%) và 8/9 lọt.
Nếu không, harness này sai và mọi dòng khác không được dùng.

Chạy:
    python experiments/sweep_dry_threshold.py
    python experiments/sweep_dry_threshold.py --seeds 10
"""
from __future__ import annotations

import argparse
import csv
import random
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments"))

import fraud_detection as fd                                  # noqa: E402
import reality_gap_probe as rgp                               # noqa: E402
import robust_audit_eval as rae                               # noqa: E402
from log_filters import (FilterConfig, RecordingNoise,         # noqa: E402
                         max_event_depth, robust_audit, tier1_gap_flag)
from ncs_loop import load_weather                             # noqa: E402

START, HOURS, MIN_CLAIMS = rae.START, rae.HOURS, rae.MIN_CLAIMS
TWIN = rae.TWIN

# Ngưỡng quét. 0,45 là quy ước của bài (dùng làm cổng kiểm chứng).
#   0,05  ~ vừa ráo mặt ruộng: trong mô hình bucket chỉ giữ tới FC, nên nước
#           đọng vừa rút hết là d vừa vượt 0 -> gần như mọi giờ không tưới
#           đều "khô". Đây là đầu mút dưới của thang.
#   0,20  p của lúa theo FAO-56 (stress bắt đầu)
#   0,45  quy ước đếm của bài
#   0,80  d* của bài (trần công thức hiệu chỉnh p)
#   0,95  sát điểm héo: chỉ những đợt khô sâu mới được tính
THRESHOLDS = (0.05, 0.20, 0.45, 0.80, 0.95)


def with_threshold(t: float):
    """Buộc mọi lời gọi awd_windows trong module đánh giá dùng ngưỡng t."""
    orig = fd.awd_windows

    def patched(depls, log_irrig, threshold=None):
        return orig(depls, log_irrig, t)

    rae.awd_windows = patched
    return orig


def probe_threshold(t: float, seeds: int) -> list[dict]:
    """Chạy lại đường ống của bài ở một ngưỡng; trả về từng nhật ký."""
    with_threshold(t)
    thetas, w0set = rae.THETA_REDUCED, rae.W0_REDUCED
    cfg = FilterConfig()
    noise = RecordingNoise()
    rows: list[dict] = []

    for station in rgp.STATIONS:
        for year in (2024, 2025):
            weather, day_rain = load_weather(station, limit=START + HOURS + 20, year=year)
            for seed in range(seeds):
                rng = random.Random(7000 * year + 13 * seed + rgp.station_seed(station))
                soil = rng.choice(rgp.SOILS)
                _prof, _depl, rec_r, _pump, _eta, _thr = rgp.build_truth(
                    rng, weather, soil, rgp.CFG_REAL)

                if len(rec_r) < MIN_CLAIMS:
                    continue

                attack, _nd = rae.timing_attack(
                    rec_r, weather, day_rain,
                    max_depth=max_event_depth(cfg.infil.default_duration_h, cfg.infil))

                changed = int(rae._norm(attack) != rae._norm(rec_r))
                nd_honest = rae.audit_v1(rec_r, weather, day_rain)["n_dry"]
                nd_attack = rae.audit_v1(attack, weather, day_rain)["n_dry"]

                # bộ phát hiện bền vững: lọt = không bị bắt ở cả hai tầng
                verdict = robust_audit(attack, weather, day_rain, START, HOURS,
                                       thetas=thetas, cfg=cfg, w0_depl_set=w0set)
                t1 = tier1_gap_flag(_pump, sum(attack.values()), max(1, len(attack)), noise)[0]
                escaped = int((not verdict.flagged) and (not t1))

                rows.append({
                    "threshold": t, "station": station, "year": year, "seed": seed,
                    "soil": soil[0], "n_claims": len(rec_r), "changed": changed,
                    "n_dry_honest": nd_honest, "n_dry_attack": nd_attack,
                    "escaped_v2": escaped,
                })
    return rows


def summarise(rows: list[dict]) -> dict:
    honest = [r for r in rows]
    changed = [r for r in rows if r["changed"]]
    base_all = statistics.mean(r["n_dry_honest"] for r in honest) if honest else 0.0
    base_ch = statistics.mean(r["n_dry_honest"] for r in changed) if changed else 0.0
    atk_ch = statistics.mean(r["n_dry_attack"] for r in changed) if changed else 0.0
    gain = (atk_ch - base_ch) / base_ch * 100 if base_ch else float("nan")
    esc = sum(r["escaped_v2"] for r in changed)
    # độ lệch ghép cặp trên các nhật ký thật sự bị sửa
    diffs = [r["n_dry_attack"] - r["n_dry_honest"] for r in changed]
    sd = statistics.stdev(diffs) if len(diffs) > 1 else 0.0
    tstat = (statistics.mean(diffs) / (sd / len(diffs) ** 0.5)) if sd and len(diffs) > 1 else float("nan")
    return {
        "n_honest": len(honest), "n_targeted": len(rows), "n_changed": len(changed),
        "base_all": base_all, "base_changed": base_ch, "attack_mean": atk_ch,
        "gain_pct": gain, "escaped": esc, "n_esc_denom": len(changed),
        "mean_diff": statistics.mean(diffs) if diffs else 0.0, "sd_diff": sd,
        "t": tstat,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=10)
    ap.add_argument("--out", default="sweep_dry_threshold.csv")
    args = ap.parse_args()

    all_rows: list[dict] = []
    summary: list[dict] = []
    t0 = time.time()

    for t in THRESHOLDS:
        rows = probe_threshold(t, args.seeds)
        all_rows.extend(rows)
        s = summarise(rows)
        s["threshold"] = t
        summary.append(s)
        print(f"d_dry={t:.2f} | n_changed={s['n_changed']}/{s['n_targeted']} | "
              f"n_dry {s['base_changed']:.2f} -> {s['attack_mean']:.2f} "
              f"({s['gain_pct']:+.1f}%) | lot {s['escaped']}/{s['n_esc_denom']} | "
              f"t={s['t']:.2f} | {time.time() - t0:.0f}s", flush=True)

    OUT.mkdir(exist_ok=True)
    p = OUT / args.out
    with p.open("w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=sorted({k for r in all_rows for k in r}))
        wr.writeheader()
        wr.writerows(all_rows)

    W = 96
    print("\n" + "=" * W)
    print("ĐỘ NHẠY CỦA CHỈ BÁO n_dry THEO NGƯỠNG ĐẾM PHA KHÔ")
    print("=" * W)
    print(f"{'d_dry':>6}{'n đã sửa':>10}{'n_dry gốc':>11}{'n_dry tấn công':>16}"
          f"{'mức tăng':>11}{'lọt D_rob':>11}{'t':>7}")
    for s in summary:
        star = "  <- quy ước của bài" if abs(s["threshold"] - 0.45) < 1e-9 else ""
        print(f"{s['threshold']:>6.2f}{s['n_changed']:>10}{s['base_changed']:>11.2f}"
              f"{s['attack_mean']:>16.2f}{s['gain_pct']:>+10.1f}%"
              f"{s['escaped']:>7}/{s['n_esc_denom']:<3}{s['t']:>7.2f}{star}")

    gate = next(s for s in summary if abs(s["threshold"] - 0.45) < 1e-9)
    ok_gain = abs(gate["gain_pct"] - 33.0) < 1.5
    ok_esc = gate["escaped"] == 8 and gate["n_esc_denom"] == 9
    print("\nCỔNG KIỂM CHỨNG ở d_dry = 0,45 (phải khớp bài):")
    print(f"  mức tăng +33%: {'ĐẠT' if ok_gain else 'KHÔNG ĐẠT'} ({gate['gain_pct']:+.1f}%)")
    print(f"  lọt 8/9      : {'ĐẠT' if ok_esc else 'KHÔNG ĐẠT'} "
          f"({gate['escaped']}/{gate['n_esc_denom']})")
    print(f"\nghi {p}")
    return 0 if (ok_gain and ok_esc) else 1


if __name__ == "__main__":
    sys.exit(main())
