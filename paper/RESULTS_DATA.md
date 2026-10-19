# SỐ LIỆU GỐC CHO BÀI BÁO — sinh tự động, KHÔNG sửa tay

Nguồn: `experiments/extract_paper_numbers.py` đọc `outputs/*.csv`.
Mọi con số trong `paper/main.tex` phải đối chiếu được với file này.

Hằng số: z = 1.959964; W (chiều rộng tập an toàn) = 59.5 mm.

**Thiếu hụt mùa khô ERA5 2024 (2 160 giờ từ 1/3) — hai định nghĩa, KHÔNG dùng lẫn:**

| trạm | thiếu hụt ròng $K_c\Sigma ET_0-\Sigma P$ (mm) | POS-SUM $\Sigma\max(0,K_c ET_{0,h}-P_h)$ (mm) — cổng dùng để xét khan |
|---|---|---|
| can_tho | 318.4 | 485.1 |
| soc_trang | 301.6 | 468.5 |
| ca_mau | 306.0 | 450.2 |

POS-SUM lớn hơn vì không cho mưa dư bù trừ (cách làm thận trọng, đúng cho câu hỏi "nước còn đủ đến hết mùa không"). Vì mọi ngân sách hữu hạn trong lưới (80–400 mm) đều nhỏ hơn POS-SUM của cả ba trạm (450–485 mm), **tất cả đều là ngân sách ràng buộc** theo định nghĩa của chính bộ điều khiển; chỉ $B=\infty$ là không.

## 1. Lưới chính — giờ mất an toàn (%) theo chính sách × ngân sách

Nguồn `main_raw.csv`, **n = 7560 episode** (3 trạm × 2 kênh × 6 ngân sách × 7 chính sách × 10 seed × 3 dải trung thực). Cửa sổ 2 160 giờ (1/3–29/5), ERA5 thật.

### Kênh severe, dải `awd` (σ_frac = 0.02)

| chính sách | b=80 | b=160 | b=240 | b=320 | b=400 | b=∞ |
|---|---|---|---|---|---|---|
| TwinGate+T2 | 34.79 | 14.47 | 0.81 | 0.26 | 0.10 | 0.02 |
| TwinGate+blindARQ | 36.36 | 17.45 | 2.48 | 0.00 | 0.00 | 0.00 |
| Reactive+T2 | 45.52 | 34.85 | 28.10 | 17.82 | 7.36 | 0.02 |
| Reactive+blindARQ | 46.55 | 36.61 | 36.22 | 25.65 | 16.78 | 0.00 |
| FixedSchedule | 53.78 | 47.98 | 48.39 | 39.07 | 32.23 | 0.00 |
| Oracle | 31.92 | 7.48 | 0.01 | 0.00 | 0.00 | 0.00 |
| TwinGate+T2+centre | 41.27 | 25.87 | 11.30 | 0.04 | 0.02 | 0.02 |

### Kênh severe, dải `mid` (σ_frac = 0.05)

| chính sách | b=80 | b=160 | b=240 | b=320 | b=400 | b=∞ |
|---|---|---|---|---|---|---|
| TwinGate+T2 | 38.17 | 21.75 | 3.84 | 0.02 | 0.02 | 0.02 |
| TwinGate+blindARQ | 40.77 | 25.28 | 9.28 | 1.08 | 0.11 | 0.00 |
| Reactive+T2 | 45.52 | 34.85 | 28.10 | 17.82 | 7.36 | 0.02 |
| Reactive+blindARQ | 46.55 | 36.61 | 36.22 | 25.65 | 16.78 | 0.00 |
| FixedSchedule | 53.78 | 47.98 | 48.39 | 39.07 | 32.23 | 0.00 |
| Oracle | 31.92 | 7.48 | 0.01 | 0.00 | 0.00 | 0.00 |
| TwinGate+T2+centre | 41.27 | 25.87 | 11.30 | 0.04 | 0.02 | 0.02 |

### Kênh severe, dải `narrow` (σ_frac = 0.1)

| chính sách | b=80 | b=160 | b=240 | b=320 | b=400 | b=∞ |
|---|---|---|---|---|---|---|
| TwinGate+T2 | 40.07 | 24.27 | 7.91 | 1.32 | 1.32 | 1.32 |
| TwinGate+blindARQ | 42.00 | 27.31 | 12.95 | 2.34 | 0.33 | 0.00 |
| Reactive+T2 | 45.52 | 34.85 | 28.10 | 17.82 | 7.36 | 0.02 |
| Reactive+blindARQ | 46.55 | 36.61 | 36.22 | 25.65 | 16.78 | 0.00 |
| FixedSchedule | 53.78 | 47.98 | 48.39 | 39.07 | 32.23 | 0.00 |
| Oracle | 31.92 | 7.48 | 0.01 | 0.00 | 0.00 | 0.00 |
| TwinGate+T2+centre | 40.07 | 24.27 | 7.91 | 1.32 | 1.32 | 1.32 |

### Kênh mild, dải `awd` (σ_frac = 0.02)

| chính sách | b=80 | b=160 | b=240 | b=320 | b=400 | b=∞ |
|---|---|---|---|---|---|---|
| TwinGate+T2 | 34.65 | 13.69 | 0.03 | 0.03 | 0.00 | 0.00 |
| TwinGate+blindARQ | 36.55 | 17.73 | 2.77 | 0.00 | 0.00 | 0.00 |
| Reactive+T2 | 46.58 | 34.95 | 31.24 | 21.13 | 11.76 | 0.00 |
| Reactive+blindARQ | 46.60 | 36.62 | 36.44 | 25.86 | 17.00 | 0.00 |
| FixedSchedule | 54.06 | 46.51 | 48.54 | 38.86 | 31.33 | 0.00 |
| Oracle | 31.93 | 7.65 | 0.00 | 0.00 | 0.00 | 0.00 |
| TwinGate+T2+centre | 41.67 | 26.24 | 11.91 | 0.00 | 0.00 | 0.00 |

### Kênh mild, dải `mid` (σ_frac = 0.05)

| chính sách | b=80 | b=160 | b=240 | b=320 | b=400 | b=∞ |
|---|---|---|---|---|---|---|
| TwinGate+T2 | 39.12 | 22.54 | 4.33 | 0.00 | 0.00 | 0.00 |
| TwinGate+blindARQ | 40.94 | 25.59 | 9.73 | 1.29 | 0.15 | 0.00 |
| Reactive+T2 | 46.58 | 34.95 | 31.24 | 21.13 | 11.76 | 0.00 |
| Reactive+blindARQ | 46.60 | 36.62 | 36.44 | 25.86 | 17.00 | 0.00 |
| FixedSchedule | 54.06 | 46.51 | 48.54 | 38.86 | 31.33 | 0.00 |
| Oracle | 31.93 | 7.65 | 0.00 | 0.00 | 0.00 | 0.00 |
| TwinGate+T2+centre | 41.67 | 26.24 | 11.91 | 0.00 | 0.00 | 0.00 |

### Kênh mild, dải `narrow` (σ_frac = 0.1)

| chính sách | b=80 | b=160 | b=240 | b=320 | b=400 | b=∞ |
|---|---|---|---|---|---|---|
| TwinGate+T2 | 40.59 | 24.74 | 8.87 | 0.00 | 0.00 | 0.00 |
| TwinGate+blindARQ | 42.11 | 27.61 | 13.33 | 2.80 | 0.55 | 0.00 |
| Reactive+T2 | 46.58 | 34.95 | 31.24 | 21.13 | 11.76 | 0.00 |
| Reactive+blindARQ | 46.60 | 36.62 | 36.44 | 25.86 | 17.00 | 0.00 |
| FixedSchedule | 54.06 | 46.51 | 48.54 | 38.86 | 31.33 | 0.00 |
| Oracle | 31.93 | 7.65 | 0.00 | 0.00 | 0.00 | 0.00 |
| TwinGate+T2+centre | 40.59 | 24.74 | 8.87 | 0.00 | 0.00 | 0.00 |

## 2. AWD — số chu kỳ đạt chuẩn ≥72 h (QĐ 4801) theo dải trung thực

| dải | σ_frac | b=80 | b=160 | b=240 | b=320 | b=400 | b=∞ |
|---|---|---|---|---|---|---|---|
| awd | 0.02 | 3.17 | 6.17 | 8.73 | 7.63 | 1.97 | 0.17 |
| mid | 0.05 | 0.57 | 1.03 | 1.23 | 1.43 | 0.70 | 0.17 |
| narrow | 0.1 | 0.27 | 0.37 | 0.53 | 0.53 | 0.53 | 0.53 |

Cột = chu kỳ AWD **đạt chuẩn** (pha khô ≥72 h). `awd_short` (mất tín chỉ) cho cùng ô, kênh severe:

| dải | b=240 đạt | b=240 hụt | b=400 đạt | b=400 hụt | b=∞ đạt | b=∞ hụt |
|---|---|---|---|---|---|---|
| awd | 8.73 | 0.00 | 1.97 | 7.77 | 0.17 | 9.03 |
| mid | 1.23 | 8.83 | 0.70 | 9.80 | 0.17 | 9.03 |
| narrow | 0.53 | 9.33 | 0.53 | 11.87 | 0.53 | 11.87 |

## 3. Pareto an toàn–nước (kênh severe, dải `awd`)

| chính sách | nước (mm) | mất an toàn (%) | AWD đạt | giờ stress | nước đúp (mm) |
|---|---|---|---|---|---|
| TwinGate+T2 | 222.7 | 0.81 | 8.73 | 1402 | 55.3 |
| TwinGate+blindARQ | 230.7 | 2.48 | 7.93 | 1359 | 72.0 |
| Reactive+T2 | 240.0 | 28.10 | 0.10 | 1146 | 36.0 |
| Reactive+blindARQ | 240.0 | 36.22 | 0.00 | 1276 | 78.0 |
| FixedSchedule | 240.0 | 48.39 | 0.00 | 1458 | 78.0 |
| Oracle | 200.0 | 0.01 | 10.00 | 1551 | 25.3 |
| TwinGate+T2+centre | 240.0 | 11.30 | 0.17 | 1040 | 53.3 |

## 4. Trade-off: kiểm định xu hướng theo ngân sách

ρ = Spearman giữa ngân sách và giờ mất an toàn (kỳ vọng ρ < 0). Δ và t = kiểm định cặp cho b = 160 → 240 mm, n = 30 cặp (10 seed × 3 trạm).

Ghi chú phân biệt 5 trường hợp theo (Δ, t): cải thiện có ý nghĩa / giảm nhẹ không ý nghĩa / không đổi đáng kể / tăng nhẹ không ý nghĩa / tăng có ý nghĩa — trường hợp cuối phải giải thích được bằng cơ chế, nếu không là lỗi.

| kênh | dải | chính sách | ρ | Δ b=160→240 | t | n | ghi chú |
|---|---|---|---|---|---|---|---|
| severe | awd | TwinGate+T2 | -1.00 | -13.65p | -14.39 | 30 | cải thiện có ý nghĩa |
| severe | awd | Reactive+T2 | -1.00 | -6.75p | -10.44 | 30 | cải thiện có ý nghĩa |
| severe | awd | FixedSchedule | -0.90 | +0.41p | +0.54 | 30 | không đổi đáng kể (nhiễu) |
| severe | awd | Oracle | -0.97 | -7.47p | -11.77 | 30 | cải thiện có ý nghĩa |
| severe | mid | TwinGate+T2 | -0.97 | -17.92p | -52.37 | 30 | cải thiện có ý nghĩa |
| severe | mid | Reactive+T2 | -1.00 | -6.75p | -10.44 | 30 | cải thiện có ý nghĩa |
| severe | mid | FixedSchedule | -0.90 | +0.41p | +0.54 | 30 | không đổi đáng kể (nhiễu) |
| severe | mid | Oracle | -0.97 | -7.47p | -11.77 | 30 | cải thiện có ý nghĩa |
| severe | narrow | TwinGate+T2 | -0.97 | -16.37p | -52.89 | 30 | cải thiện có ý nghĩa |
| severe | narrow | Reactive+T2 | -1.00 | -6.75p | -10.44 | 30 | cải thiện có ý nghĩa |
| severe | narrow | FixedSchedule | -0.90 | +0.41p | +0.54 | 30 | không đổi đáng kể (nhiễu) |
| severe | narrow | Oracle | -0.97 | -7.47p | -11.77 | 30 | cải thiện có ý nghĩa |
| mild | awd | TwinGate+T2 | -0.97 | -13.66p | -23.95 | 30 | cải thiện có ý nghĩa |
| mild | awd | Reactive+T2 | -1.00 | -3.71p | -5.36 | 30 | cải thiện có ý nghĩa |
| mild | awd | FixedSchedule | -0.90 | +2.02p | +2.51 | 30 | **tăng có ý nghĩa** — giải thích được bằng bão hoà độ sâu: mm/lệnh 60.0 ≥ W 59.5 mm nên nước tràn khỏi dung trọng (nước hữu ích vẫn tăng) |
| mild | awd | Oracle | -0.89 | -7.65p | -11.81 | 30 | cải thiện có ý nghĩa |
| mild | mid | TwinGate+T2 | -0.97 | -18.22p | -67.08 | 30 | cải thiện có ý nghĩa |
| mild | mid | Reactive+T2 | -1.00 | -3.71p | -5.36 | 30 | cải thiện có ý nghĩa |
| mild | mid | FixedSchedule | -0.90 | +2.02p | +2.51 | 30 | **tăng có ý nghĩa** — giải thích được bằng bão hoà độ sâu: mm/lệnh 60.0 ≥ W 59.5 mm nên nước tràn khỏi dung trọng (nước hữu ích vẫn tăng) |
| mild | mid | Oracle | -0.89 | -7.65p | -11.81 | 30 | cải thiện có ý nghĩa |
| mild | narrow | TwinGate+T2 | -0.97 | -15.88p | -91.18 | 30 | cải thiện có ý nghĩa |
| mild | narrow | Reactive+T2 | -1.00 | -3.71p | -5.36 | 30 | cải thiện có ý nghĩa |
| mild | narrow | FixedSchedule | -0.90 | +2.02p | +2.51 | 30 | **tăng có ý nghĩa** — giải thích được bằng bão hoà độ sâu: mm/lệnh 60.0 ≥ W 59.5 mm nên nước tràn khỏi dung trọng (nước hữu ích vẫn tăng) |
| mild | narrow | Oracle | -0.89 | -7.65p | -11.81 | 30 | cải thiện có ý nghĩa |

Lưu ý khi viết bài: ρ < 0 ở **mọi** ô xác nhận xu hướng tổng thể (thêm nước thì an toàn hơn). Riêng FixedSchedule ở kênh mild có một cặp tăng có ý nghĩa và đã kiểm chứng được cơ chế — đây là **kết quả** (lịch mù không tận dụng được nước cấp thêm), không phải lỗi cần giấu.

## 5. Kiểm chứng vững: năm 2025 (mùa khô ướt hơn)

Nguồn `main_raw_2025.csv`, n = 7560 episode.

| dải | chính sách | b=80 | b=160 | b=240 | b=320 | b=400 |
|---|---|---|---|---|---|---|
| awd | TwinGate+T2 | 2.29 | 0.04 | 0.04 | 0.02 | 0.00 |
| awd | Reactive+T2 | 9.89 | 2.12 | 1.29 | 0.15 | 0.00 |
| awd | FixedSchedule | 20.20 | 13.80 | 15.34 | 7.02 | 3.24 |
| awd | Oracle | 2.20 | 0.00 | 0.00 | 0.00 | 0.00 |
| mid | TwinGate+T2 | 5.28 | 0.24 | 0.00 | 0.00 | 0.00 |
| mid | Reactive+T2 | 9.89 | 2.12 | 1.29 | 0.15 | 0.00 |
| mid | FixedSchedule | 20.20 | 13.80 | 15.34 | 7.02 | 3.24 |
| mid | Oracle | 2.20 | 0.00 | 0.00 | 0.00 | 0.00 |
| narrow | TwinGate+T2 | 5.86 | 0.99 | 0.64 | 0.64 | 0.64 |
| narrow | Reactive+T2 | 9.89 | 2.12 | 1.29 | 0.15 | 0.00 |
| narrow | FixedSchedule | 20.20 | 13.80 | 15.34 | 7.02 | 3.24 |
| narrow | Oracle | 2.20 | 0.00 | 0.00 | 0.00 | 0.00 |

## 6. Ablation — cái giá của từng thành phần

Nguồn `ablation_raw.csv`, n = 4800 episode. Mỗi biến thể tắt ĐÚNG MỘT thành phần, giữ nguyên phần còn lại, cùng seed/cùng thời tiết/cùng kênh.

### Dải `narrow` (0.1), kênh severe, ngân sách ràng buộc (< 450 mm = POS-SUM nhỏ nhất, nên mọi B hữu hạn trong lưới đều ràng buộc), n = 960

| biến thể | mất an toàn (%) | Δ | nước đúp (mm) | Δ | AWD đạt |
|---|---|---|---|---|---|
| - tai neo cam bien | 57.81 | +39.42 | 0.0 | -44.0 | 0.00 |
| - whatif (twin->predictor) | 45.19 | +26.80 | 31.0 | -13.0 | 0.40 |
| - cong chance-constrained | 31.57 | +13.18 | 24.3 | -19.7 | 0.10 |
| Oracle (thong tin hoan hao) | 9.85 | -8.54 | 24.0 | -20.0 | 7.32 |
| - T2 (gui lai mu) | 21.15 | +2.76 | 65.5 | +21.5 | 0.00 |
| - epoch cap (quyet dinh moi gio) | 20.43 | +2.04 | 49.2 | +5.2 | 0.00 |
| FULL (de xuat) **(đề xuất)** | 18.39 | +0.00 | 44.0 | +0.0 | 0.42 |
| - luat thich ung (centre co dinh) | 18.39 | +0.00 | 44.0 | +0.0 | 0.42 |

### Dải `narrow` (0.1), kênh mild, ngân sách ràng buộc (< 450 mm = POS-SUM nhỏ nhất, nên mọi B hữu hạn trong lưới đều ràng buộc), n = 960

| biến thể | mất an toàn (%) | Δ | nước đúp (mm) | Δ | AWD đạt |
|---|---|---|---|---|---|
| - tai neo cam bien | 57.81 | +39.26 | 0.0 | -60.8 | 0.00 |
| - whatif (twin->predictor) | 41.32 | +22.77 | 51.3 | -9.5 | 0.01 |
| - cong chance-constrained | 33.47 | +14.92 | 45.2 | -15.7 | 0.00 |
| Oracle (thong tin hoan hao) | 9.90 | -8.65 | 49.5 | -11.3 | 7.33 |
| - T2 (gui lai mu) | 21.46 | +2.91 | 65.5 | +4.7 | 0.00 |
| - epoch cap (quyet dinh moi gio) | 20.24 | +1.69 | 62.0 | +1.2 | 0.00 |
| FULL (de xuat) **(đề xuất)** | 18.55 | +0.00 | 60.8 | +0.0 | 0.05 |
| - luat thich ung (centre co dinh) | 18.55 | +0.00 | 60.8 | +0.0 | 0.05 |

### Dải `wide` (0.02), kênh severe, ngân sách ràng buộc (< 450 mm = POS-SUM nhỏ nhất, nên mọi B hữu hạn trong lưới đều ràng buộc), n = 960

| biến thể | mất an toàn (%) | Δ | nước đúp (mm) | Δ | AWD đạt |
|---|---|---|---|---|---|
| - whatif (twin->predictor) | 52.75 | +40.17 | 44.7 | -1.2 | 0.00 |
| - cong chance-constrained | 31.57 | +18.99 | 24.3 | -21.5 | 0.10 |
| - luat thich ung (centre co dinh) | 19.62 | +7.04 | 48.5 | +2.7 | 0.17 |
| - tai neo cam bien | 16.87 | +4.29 | 46.5 | +0.7 | 4.12 |
| Oracle (thong tin hoan hao) | 9.85 | -2.73 | 24.0 | -21.8 | 7.32 |
| - T2 (gui lai mu) | 14.07 | +1.49 | 61.7 | +15.8 | 5.92 |
| - epoch cap (quyet dinh moi gio) | 13.99 | +1.41 | 52.0 | +6.2 | 5.74 |
| FULL (de xuat) **(đề xuất)** | 12.58 | +0.00 | 45.8 | +0.0 | 6.42 |

### Dải `wide` (0.02), kênh mild, ngân sách ràng buộc (< 450 mm = POS-SUM nhỏ nhất, nên mọi B hữu hạn trong lưới đều ràng buộc), n = 960

| biến thể | mất an toàn (%) | Δ | nước đúp (mm) | Δ | AWD đạt |
|---|---|---|---|---|---|
| - whatif (twin->predictor) | 54.09 | +41.99 | 52.7 | -4.5 | 0.00 |
| - cong chance-constrained | 33.47 | +21.37 | 45.2 | -12.0 | 0.00 |
| - luat thich ung (centre co dinh) | 19.96 | +7.85 | 61.2 | +4.0 | 0.00 |
| - tai neo cam bien | 15.35 | +3.25 | 52.8 | -4.3 | 5.42 |
| Oracle (thong tin hoan hao) | 9.90 | -2.20 | 49.5 | -7.7 | 7.33 |
| - T2 (gui lai mu) | 14.26 | +2.16 | 61.8 | +4.7 | 5.93 |
| - epoch cap (quyet dinh moi gio) | 13.77 | +1.67 | 58.2 | +1.0 | 4.92 |
| FULL (de xuat) **(đề xuất)** | 12.10 | +0.00 | 57.2 | +0.0 | 6.61 |

## 7. Triển khai thực tế — quét một yếu tố một lần

Nguồn `deployment_raw.csv`, n = 540 episode. Mức tham chiếu: σ_frac = 0,02; ngân sách 240 mm; 3 trạm × 2 kênh × 5 seed.

### F1_uplink — mất gói uplink

| mức | mất an toàn (%) | AWD đạt | giờ stress | lệnh/ngày | gửi lại/ngày |
|---|---|---|---|---|---|
| 0.05 | 0.28 | 9.10 | 1387 | 0.120 | 0.128 |
| 0.15 | 0.28 | 9.07 | 1381 | 0.120 | 0.127 |
| 0.3 | 0.28 | 9.00 | 1373 | 0.121 | 0.128 |
| 0.5 | 0.33 | 8.97 | 1361 | 0.120 | 0.129 |
| 0.7 | 0.45 | 8.93 | 1358 | 0.120 | 0.131 |
| 0.9 | 0.54 | 8.80 | 1383 | 0.122 | 0.140 |

### F2_soil — loại đất

| mức | mất an toàn (%) | AWD đạt | giờ stress | lệnh/ngày | gửi lại/ngày |
|---|---|---|---|---|---|
| loam_cat (sandy loam) | 0.00 | 7.50 | 1423 | 0.111 | 0.128 |
| thit_pha_set (mac dinh) | 0.28 | 9.07 | 1381 | 0.120 | 0.127 |
| set (clay) | 0.07 | 8.80 | 1419 | 0.122 | 0.148 |

### F3_depth — độ phân giải lệnh

| mức | mất an toàn (%) | AWD đạt | giờ stress | lệnh/ngày | gửi lại/ngày |
|---|---|---|---|---|---|
| agronomic | 0.28 | 9.07 | 1381 | 0.120 | 0.127 |
| fine | 0.23 | 4.43 | 1469 | 0.194 | 0.214 |
| coarse | 9.65 | 5.07 | 1274 | 0.069 | 0.078 |

### F4_horizon — chân trời H (ngày)

| mức | mất an toàn (%) | AWD đạt | giờ stress | lệnh/ngày | gửi lại/ngày |
|---|---|---|---|---|---|
| 3 | 0.32 | 9.03 | 1402 | 0.119 | 0.134 |
| 6 | 0.28 | 9.07 | 1381 | 0.120 | 0.127 |
| 12 | 0.45 | 8.53 | 1342 | 0.126 | 0.136 |
| 24 | 0.97 | 4.43 | 1361 | 0.138 | 0.160 |

### F5_radio — kiểu gửi lại

| mức | mất an toàn (%) | AWD đạt | giờ stress | lệnh/ngày | gửi lại/ngày |
|---|---|---|---|---|---|
| T2 | 0.28 | 9.07 | 1381 | 0.120 | 0.127 |
| blindARQ | 3.19 | 8.03 | 1363 | 0.089 | 0.199 |

## 8. Đa ruộng (HTX) — 6 thửa, 2 loại đất × 3 trạm

Nguồn `multifield_raw.csv`, n = 2700 episode. Xấp xỉ khai báo: chỉ S trong 6 thửa được phục vụ mỗi ngày → epoch hiệu dụng = 24·N/S giờ.

### 8.1 Ba luật phân bổ (kênh severe, slots = 6/ngày)

| tổng ngân sách | mm/thửa | luật | mất an toàn TB (%) | thửa xấu nhất (%) | Gini | AWD đạt | nước (mm) |
|---|---|---|---|---|---|---|---|
| 480.0 | 80 | equal | 38.38 | 41.78 | 0.042 | 1.0 | 480 |
| 480.0 | 80 | deficit | 39.81 | 42.03 | 0.028 | 1.0 | 440 |
| 480.0 | 80 | gate | 30.83 | 36.63 | 0.072 | 20.0 | 480 |
| 960.0 | 160 | equal | 23.92 | 27.09 | 0.059 | 1.0 | 960 |
| 960.0 | 160 | deficit | 25.19 | 27.36 | 0.034 | 1.0 | 920 |
| 960.0 | 160 | gate | 8.22 | 18.06 | 0.465 | 38.6 | 960 |
| 1440.0 | 240 | equal | 9.06 | 13.31 | 0.209 | 1.0 | 1440 |
| 1440.0 | 240 | deficit | 10.86 | 13.31 | 0.078 | 1.0 | 1400 |
| 1440.0 | 240 | gate | 0.27 | 1.33 | 0.586 | 50.0 | 1264 |
| 1920.0 | 320 | equal | 0.02 | 0.08 | 0.138 | 1.2 | 1920 |
| 1920.0 | 320 | deficit | 0.02 | 0.08 | 0.138 | 1.2 | 1880 |
| 1920.0 | 320 | gate | 0.12 | 0.41 | 0.419 | 40.4 | 1544 |
| inf | ∞ | equal | 0.02 | 0.08 | 0.138 | 1.2 | 2040 |
| inf | ∞ | deficit | 0.02 | 0.08 | 0.138 | 1.2 | 2040 |
| inf | ∞ | gate | 0.02 | 0.08 | 0.138 | 1.2 | 2040 |

### 8.2 Nút vặn tần suất quyết định (slots/ngày, luật `equal`, kênh severe)

| tổng ngân sách | slots/ngày | mất an toàn (%) | giờ stress | AWD đạt | im lặng | nước (mm) |
|---|---|---|---|---|---|---|
| 480.0 | 6 | 38.38 | 8668 | 1.0 | 511 | 480 |
| 480.0 | 3 | 37.93 | 8918 | 1.6 | 245 | 480 |
| 480.0 | 2 | 36.87 | 8892 | 3.4 | 156 | 480 |
| 960.0 | 6 | 23.92 | 7326 | 1.0 | 484 | 960 |
| 960.0 | 3 | 23.05 | 7750 | 3.6 | 221 | 960 |
| 960.0 | 2 | 21.70 | 7869 | 6.0 | 136 | 960 |
| 1440.0 | 6 | 9.06 | 6086 | 1.0 | 456 | 1440 |
| 1440.0 | 3 | 6.26 | 6783 | 6.0 | 192 | 1440 |
| 1440.0 | 2 | 4.05 | 7088 | 12.8 | 106 | 1440 |
| 1920.0 | 6 | 0.02 | 3962 | 1.2 | 433 | 1920 |
| 1920.0 | 3 | 0.30 | 4497 | 6.2 | 175 | 1876 |
| 1920.0 | 2 | 0.89 | 5104 | 14.4 | 92 | 1800 |
| inf | 6 | 0.02 | 3020 | 1.2 | 428 | 2040 |
| inf | 3 | 0.30 | 4288 | 6.2 | 174 | 1916 |
| inf | 2 | 0.89 | 5062 | 14.4 | 92 | 1832 |

### 8.3 Kiểm định cặp slots 6 → 2 (n = số cặp seed×thửa×ngân sách×kênh)

| luật | n cặp | Δ im lặng | t | Δ stress (h) | t | Δ mất an toàn | t | Δ AWD | t |
|---|---|---|---|---|---|---|---|---|---|
| equal | 300 | -58.64 | -461.25 | +158.67 | +21.61 | -1.35 | -9.71 | +0.96 | +15.93 |
| deficit | 300 | -58.70 | -475.50 | +142.04 | +20.43 | -1.45 | -9.77 | +0.94 | +15.64 |
| gate | 300 | -58.86 | -461.31 | +62.21 | +6.64 | +0.39 | +1.71 | -0.90 | -8.05 |

### 8.4 Điểm chéo (crossover) — điều kiện áp dụng của cơ chế im lặng

Δ = mất an toàn(`gate`) − mất an toàn(`equal`), kênh severe. **Âm = cơ chế tốt hơn.**

| mm/thửa | slots=6 | slots=3 | slots=2 |
|---|---|---|---|
| 80 | -7.55 | -8.40 | -8.57 |
| 160 | -15.69 | -16.65 | -13.60 |
| 240 | -8.79 | -3.94 | +2.14 |
| 320 | +0.09 | +1.28 | +2.69 |
| ∞ | +0.00 | +0.00 | +0.00 |

## 9. Ngưỡng lý thuyết (derive, không phải kết quả mô phỏng)

| đại lượng | công thức | giá trị |
|---|---|---|
| W (chiều rộng tập an toàn) | (0,85 − 0) × TAW | 59.50 mm |
| TAW | (θ_fc − θ_wp) × Zr × 1000 | 70.00 mm |
| span (θ_fc − θ_wp) | — | 70.0000 |
| σ\* (ngưỡng cổng rỗng) | W / (2z) | 15.18 mm |
| σ tĩnh (tuổi ∞) | f × TAW / √(1−ρ²) | f × 160.59 mm |
| g = √Σρ²ᵏ, k=0..6 | ρ = 0,9 | 2.0147 |
| σ_H nhỏ nhất có thể (tuổi 0) | f × TAW × g | f × 141.03 mm |
| f để cổng sống | σ\* / (TAW/√(1−ρ²)) | 0.0945 |
| σ_H cần cho AWD (d_target = 0,75) | (0,85 − 0,75)·span/z | 3.57 mm |
| f cần cho AWD (tuổi 0) | σ_cần / (TAW·g) | 0.0253 |
| f cần cho AWD (tuổi ∞) | σ_cần / σ_tĩnh | 0.0222 |

**Hệ quả triển khai:** với f = 0,10 thì σ_H ≥ 14.10 mm > 3.57 mm, nên **tăng tần suất cảm biến cũng không cứu được** (tuổi 0 là giới hạn dưới của σ) — phải cải thiện mô hình. Ngược lại với f = 0,02 thì σ tĩnh = 3.21 mm ≤ 3.57 mm, nên cổng vẫn làm AWD được **dù không bao giờ được tái neo** (pin yếu/kênh nghẽn).

## 10. Xâm nhập mặn — PHÂN TÍCH TÌNH HUỐNG (không phải kết quả chính)

**Khai báo trung thực:** KHÔNG có số đo độ mặn thực địa ở 3 trạm. Mọi con số dưới đây là của mô hình tình huống `src/tide_salinity.py`, chỉ dùng cho phân tích độ nhạy, **không đưa vào Abstract như kết quả**.

Nguồn `sweep_salinity_raw.csv`, n = 1800 episode.

| cường độ | chính sách | nước mặn bơm (mm) | giờ nguồn còn ngọt (%) | thiệt hại NS ước tính (%) | im lặng vì mặn |
|---|---|---|---|---|---|
| 0.25 | TwinGate+T2 | 0.00 | 87.8 | 0.00 | 0.0 |
| 0.25 | Reactive+T2 | 24.00 | 87.8 | 0.86 | 0.0 |
| 0.25 | FixedSchedule | 0.00 | 87.8 | 0.00 | 0.0 |
| 0.25 | Oracle | 0.00 | 87.8 | 0.00 | 0.0 |
| 0.5 | TwinGate+T2 | 0.00 | 49.7 | 0.00 | 0.0 |
| 0.5 | Reactive+T2 | 128.00 | 49.7 | 19.04 | 0.0 |
| 0.5 | FixedSchedule | 132.00 | 49.7 | 14.04 | 0.0 |
| 0.5 | Oracle | 0.00 | 49.7 | 0.00 | 0.0 |
| 1.0 | TwinGate+T2 | 0.00 | 19.4 | 0.00 | 29.0 |
| 1.0 | Reactive+T2 | 180.00 | 19.4 | 53.76 | 0.0 |
| 1.0 | FixedSchedule | 192.00 | 19.4 | 45.24 | 0.0 |
| 1.0 | Oracle | 0.00 | 19.4 | 0.00 | 29.0 |
| 1.5 | TwinGate+T2 | 0.00 | 9.1 | 0.00 | 32.1 |
| 1.5 | Reactive+T2 | 220.00 | 9.1 | 79.34 | 0.0 |
| 1.5 | FixedSchedule | 240.00 | 9.1 | 70.49 | 0.0 |
| 1.5 | Oracle | 0.00 | 9.1 | 0.00 | 33.7 |
| 2.0 | TwinGate+T2 | 0.00 | 2.6 | 0.00 | 61.0 |
| 2.0 | Reactive+T2 | 240.00 | 2.6 | 96.39 | 0.0 |
| 2.0 | FixedSchedule | 240.00 | 2.6 | 89.74 | 0.0 |
| 2.0 | Oracle | 0.00 | 2.6 | 0.00 | 61.3 |

Nhạy cảm với bảng ngưỡng chịu mặn (TwinGate+T2, kênh severe, thiệt hại NS %):

| ngưỡng | 0.25 | 0.5 | 1.0 | 1.5 | 2.0 |
|---|---|---|---|---|---|
| central | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| grattan_strict | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| maas_lenient | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## 11. Vùng hoạt động của cổng — quét σ_frac × δ (chính sách đề xuất)

Nguồn `sweep_sigma_delta_raw.csv`, n = 11520 episode.

### ngân sách 80 mm, kênh severe — giờ mất an toàn (%)

| σ_frac \ δ | 0.01 | 0.03 | 0.05 | 0.1 | 0.15 | 0.2 |
|---|---|---|---|---|---|---|
| 0.02 | 36.5 | 35.9 | 34.8 | 32.8 | 32.7 | 31.7 |
| 0.03 | 37.9 | 37.4 | 36.9 | 35.9 | 34.5 | 32.8 |
| 0.05 | 40.2 | 38.8 | 38.2 | 37.5 | 36.8 | 36.1 |
| 0.08 | 40.2 | 41.0 | 40.9 | 39.2 | 38.1 | 37.7 |
| 0.1 | 57.8 | 57.8 | 40.1 | 40.9 | 39.4 | 38.4 |
| 0.12 | 57.8 | 57.8 | 57.8 | 40.2 | 40.8 | 39.2 |
| 0.15 | 57.8 | 57.8 | 57.8 | 57.8 | 57.8 | 41.1 |
| 0.2 | 57.8 | 57.8 | 57.8 | 57.8 | 57.8 | 57.8 |

### ngân sách 80 mm, kênh severe — tỷ lệ quyết định IM LẶNG

| σ_frac \ δ | 0.01 | 0.03 | 0.05 | 0.1 | 0.15 | 0.2 |
|---|---|---|---|---|---|---|
| 0.02 | 0.96 | 0.95 | 0.95 | 0.95 | 0.95 | 0.95 |
| 0.03 | 0.95 | 0.95 | 0.96 | 0.95 | 0.95 | 0.95 |
| 0.05 | 0.94 | 0.94 | 0.94 | 0.95 | 0.95 | 0.95 |
| 0.08 | 0.96 | 0.95 | 0.95 | 0.94 | 0.94 | 0.95 |
| 0.1 | 1.00 | 1.00 | 0.95 | 0.95 | 0.94 | 0.95 |
| 0.12 | 1.00 | 1.00 | 1.00 | 0.95 | 0.95 | 0.94 |
| 0.15 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.95 |
| 0.2 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |

### ngân sách 400 mm, kênh severe — giờ mất an toàn (%)

| σ_frac \ δ | 0.01 | 0.03 | 0.05 | 0.1 | 0.15 | 0.2 |
|---|---|---|---|---|---|---|
| 0.02 | 0.0 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 |
| 0.03 | 0.0 | 0.0 | 0.0 | 0.1 | 0.1 | 0.1 |
| 0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 |
| 0.08 | 19.8 | 0.2 | 0.0 | 0.0 | 0.0 | 0.0 |
| 0.1 | 57.8 | 57.8 | 1.3 | 0.0 | 0.0 | 0.0 |
| 0.12 | 57.8 | 57.8 | 57.8 | 0.6 | 0.0 | 0.0 |
| 0.15 | 57.8 | 57.8 | 57.8 | 57.8 | 57.8 | 0.1 |
| 0.2 | 57.8 | 57.8 | 57.8 | 57.8 | 57.8 | 57.8 |

### ngân sách 400 mm, kênh severe — tỷ lệ quyết định IM LẶNG

| σ_frac \ δ | 0.01 | 0.03 | 0.05 | 0.1 | 0.15 | 0.2 |
|---|---|---|---|---|---|---|
| 0.02 | 0.83 | 0.83 | 0.83 | 0.83 | 0.83 | 0.83 |
| 0.03 | 0.82 | 0.82 | 0.83 | 0.83 | 0.83 | 0.83 |
| 0.05 | 0.81 | 0.82 | 0.82 | 0.82 | 0.82 | 0.83 |
| 0.08 | 0.90 | 0.81 | 0.81 | 0.82 | 0.82 | 0.82 |
| 0.1 | 1.00 | 1.00 | 0.82 | 0.81 | 0.82 | 0.82 |
| 0.12 | 1.00 | 1.00 | 1.00 | 0.81 | 0.81 | 0.82 |
| 0.15 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.81 |
| 0.2 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |

## BLOCKED — thiếu bằng chứng, KHÔNG được viết vào bài

- (không có)

## Đối chiếu hình

| hình | file | nguồn số liệu |
|---|---|---|
| 1 | `figures/fig1_method.pdf` | sơ đồ phương pháp (không có số liệu) |
| 2 | `figures/fig2_ablation.pdf` | `ablation_raw.csv` |
| 3 | `figures/fig3_awd_fidelity.pdf` | `main_raw.csv` (cột `awd_effective`) |
| 4 | `figures/fig4_pass_region.pdf` | `sweep_sigma_delta_raw.csv` |
| 5 | `figures/fig5_deployment.pdf` | `deployment_raw.csv` |
| 6 | `figures/fig6_multifield.pdf` | `multifield_raw.csv` |
| 7 | `figures/fig7_salinity_scenario.pdf` | `sweep_salinity_raw.csv` |
| 8 | `figures/fig8_pareto.pdf` | `main_raw.csv` |
