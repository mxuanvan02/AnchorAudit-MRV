#!/usr/bin/env python3
"""Thí nghiệm ngoài-Theta: phá tính tự nhất quán của mô phỏng.

VẤN ĐỀ panel nêu: nhật ký và mô hình kiểm toán cùng dựng trên một phương trình
FAO-56, nên tỷ lệ phát hiện/kết tội oan chỉ đo tính nhất quán nội tại của mã.

CÁCH GIẢI: sinh nhật ký trung thực bằng một MÔ HÌNH NƯỚC KHÁC nằm NGOÀI tập bất
định Θ mà bộ kiểm toán được phép dùng:
  - đất không có trong SOIL_SET (thịt pha sét pha cát, fc/wp khác)
  - độ sâu tầng rễ 0.7 m thay vì 0.5 m
  - Kc cố định 1.15 thay vì 1.05/1.20/0.90
  - rò rỉ bờ 0.05 mm/h thay vì 0..0.02
  - CN dòng chảy khác

Nếu bộ kiểm toán vẫn ít kết tội oan -> lời hứa "không buộc tội nông dân trung thực"
không còn phụ thuộc vào việc dùng chung một phương trình.
Nếu kết tội oan tăng mạnh -> đó là giới hạn thật, phải công bố bằng con số.
"""
from __future__ import annotations

import csv
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments"))

from ncs_loop import load_weather
from water_balance import BucketState, SoilProfile, daily_runoff_share, stress_coefficient
import reality_gap_probe as rgp
from log_filters import (FilterConfig, robust_audit, uncertainty_set,
                         tier1_gap_flag, RecordingNoise, max_event_depth)

START, HOURS = rgp.START, rgp.HOURS
STATIONS = rgp.STATIONS

# ---- Mô hình THẬT nằm ngoài Θ ----
OUT_SOIL = ("sandy_clay_loam", 0.30, 0.20)   # không có trong SOIL_SET
OUT_ROOT_DEPTH = 0.70                        # Θ giả định 0.5
OUT_KC = 1.15                                # Θ dùng 1.05 / theo giai đoạn
OUT_SEEP = 0.05                              # Θ cho 0..0.02


def out_profile() -> SoilProfile:
    return SoilProfile(theta_fc=OUT_SOIL[1], theta_wp=OUT_SOIL[2],
                       root_depth_m=OUT_ROOT_DEPTH)


def out_step(st, prof, precip, irrig_at_root, et0, runoff, seep):
    infil = max(0.0, precip - runoff)
    ks = stress_coefficient(st, prof)
    w = st.w + infil + irrig_at_root - ks * OUT_KC * et0 - seep
    return BucketState(w=min(w, prof.fc_mm))


def build_out_log(rng, weather, cfg):
    """Nhật ký của nông dân TRUNG THỰC trên thửa có mô hình nước ngoài Θ."""
    prof = out_profile()
    span = prof.fc_mm - prof.wp_mm
    eta = rng.uniform(*cfg["eta"])
    rain_bias = rng.uniform(*cfg["rain_bias"])
    thr = rng.uniform(*cfg["thresh"])
    spread = rng.randint(*cfg["spread_h"])
    delay = rng.random() < cfg["p_delay"]
    w0 = prof.fc_mm - rng.uniform(*cfg["w0_depl"]) * span

    rain = [max(0.0, weather[START + h]["p"] * rain_bias
                + rng.gauss(0.0, cfg["rain_noise"])) for h in range(HOURS)]
    day_tot = defaultdict(float)
    for h, r in enumerate(rain):
        day_tot[(START + h) // 24] += r

    st = BucketState(w=w0)
    events, pending = [], {}
    for h in range(HOURS):
        w = weather[START + h]
        ro = daily_runoff_share(day_tot[(START + h) // 24], rain[h], prof.cn_runoff)
        depl = min(1.0, max(0.0, (prof.fc_mm - st.w) / span))
        if depl >= thr and h not in pending:
            u = rng.choice(cfg["depths"])
            events.append((h, u))
            for k in range(spread):
                if h + k < HOURS:
                    pending[h + k] = pending.get(h + k, 0.0) + eta * u / spread
        st = out_step(st, prof, rain[h], pending.pop(h, 0.0), w["et0"], ro, OUT_SEEP)

    rec: dict[int, float] = {}
    for h, u in events:
        if rng.random() < cfg["p_forget"]:
            continue
        v = u
        if rng.random() < cfg["p_depth_err"]:
            v *= rng.uniform(*cfg["depth_err"])
        if cfg["round_mm"]:
            v = round(v / cfg["round_mm"]) * cfg["round_mm"]
        if v <= 0:
            continue
        hh = h + (24 if delay and h + 24 < HOURS else 0)
        rec[hh] = rec.get(hh, 0.0) + v
    return rec, sum(u for _, u in events)


def main():
    seeds = 10
    cfg = dict(rgp.CFG_REAL)
    thetas = uncertainty_set(soils=rgp_small_soils(), kc_modes=("fixed", "stage"),
                             etas=(0.60, 1.00))
    w0set = (0.0, 0.90)
    filt = FilterConfig()
    noise = RecordingNoise()

    rows = []
    for st_name in STATIONS:
        for year in (2024, 2025):
            weather, day_rain = load_weather(st_name, limit=START + HOURS + 20, year=year)
            for seed in range(seeds):
                rng = random.Random(7000 * year + 13 * seed + rgp.station_seed(st_name))
                rec, pumped = build_out_log(rng, weather, cfg)
                if len(rec) < 3:
                    continue
                # kiem toan bang BO DA CONG BO (Theta chuan)
                v2 = robust_audit(rec, weather, day_rain, START, HOURS, thetas, filt, w0set)
                gap = pumped - sum(rec.values())
                t1, gapv, tau = tier1_gap_flag(pumped, sum(rec.values()), len(rec), noise)
                rows.append({
                    "station": st_name, "year": year, "seed": seed,
                    "n_claims": len(rec), "gap_mm": round(gap, 2),
                    "tau_mm": round(tau, 2),
                    "v1_any": int(abs(gap) > 5.0),          # nguong tuyet doi
                    "v2_any": int(v2.flagged),              # bo vat ly ben vung
                    "tier1": int(t1),                       # nguong ty le
                })
                print(f"  {st_name} {year} s{seed}: n={len(rec)} gap={gap:7.2f} "
                      f"tau={tau:6.2f} v1={rows[-1]['v1_any']} v2={rows[-1]['v2_any']} "
                      f"t1={rows[-1]['tier1']}", flush=True)

    n = len(rows)
    print(f"\n=== NGOAI THETA: {n} nhat ky trung thuc ===")
    for k, label in [("v1_any", "don cau hinh + tau0 (5mm)"),
                     ("v2_any", "bo vat ly ben vung (giao tren Theta)"),
                     ("tier1", "nguong ty le tau(n)")]:
        c = sum(r[k] for r in rows)
        print(f"  {label:38s}: danh dau oan {c}/{n} = {c/n*100:.1f}%")

    out = ROOT / "outputs" / "out_of_theta.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"\nghi {out}")


def rgp_small_soils():
    """Ba loai dat rut gon, giong bo kiem toan da cong bo."""
    return (("sandy_loam", 0.21, 0.10),
            ("silty_clay_loam", 0.32, 0.18),
            ("silt_loam", 0.33, 0.15))


if __name__ == "__main__":
    main()
