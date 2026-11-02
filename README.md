# TwinGate — Device-Anchored Irrigation Log Auditor

Mã nguồn tái lập kết quả bài báo **"Kiểm toán nhật ký tưới neo thiết bị cho chuẩn Đo đạc–Báo cáo–Thẩm định lúa phát thải thấp"** (HUJOS-TT, 2026).

## Tổng quan

Hệ thống MRV (Measurement, Reporting, Verification) chiếm ~75% chi phí chuyển đổi lúa phát thải thấp thành tín chỉ carbon. Bài báo đề xuất tầng kiểm toán đa tầng:

1. **Bộ lọc vật lý** ($V_1, V_4, V_5$): phát hiện khai báo vô lý dựa trên mô hình cân bằng nước FAO-56
2. **Bộ phát hiện bền vững**: giảm kết tội oan bằng tối ưu robust trên tập bất định $\Theta$
3. **Phép đối chiếu thiết bị**: neo nhật ký nông dân vào bản ghi gateway có chữ ký
4. **Phân tích tấn công dịch thời điểm**: chứng minh điểm mù của phòng thủ tổng hợp

## Cấu trúc thư mục

```
TwinGate-MRV/
├── data/                  # Script fetch dữ liệu ERA5 từ Open-Meteo
│   └── fetch_era5_multi.py
├── experiments/           # Script thí nghiệm chính
│   ├── run_main.py        # Lưới chính (7560 episodes/năm)
│   ├── run_ablation.py    # Ablation study
│   ├── run_deployment.py  # Phân tích tham số triển khai
│   ├── run_multi_field.py # Đa thửa ruộng HTX
│   ├── sweep_sigma_delta.py
│   ├── sweep_salinity.py
│   ├── fraud_detection.py # Phát hiện gian lận trên 281 nhật ký
│   ├── robust_audit_eval.py
│   └── ...
├── figures/               # Script vẽ hình (8 hình trong bài)
│   ├── fig_method.py
│   ├── fig_results.py
│   └── ...
├── outputs/               # Kết quả CSV/JSON (sinh tự động)
├── src/                   # Mã nguồn core
│   ├── water_balance.py   # Mô hình cân bằng nước FAO-56
│   ├── twin_gate.py       # Cơ chế cổng TwinGate
│   ├── log_filters.py     # Bộ lọc vật lý V1-V5
│   ├── fraud_detection.py # Logic phát hiện gian lận
│   └── ...
├── tests/                 # Unit tests
│   ├── test_water_balance.py
│   ├── test_twin_gate.py
│   └── ...
├── reproduce.sh           # Script tái lập toàn bộ
└── requirements.txt       # Dependencies Python
```

## Cài đặt

### Yêu cầu

- Python ≥ 3.10
- ~2 GB dung lượng trống (cho dữ liệu ERA5 và kết quả)

### Cài đặt dependencies

```bash
# Tạo virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt
```

Dependencies chính:
- `numpy` ≥ 1.24.0
- `scipy` ≥ 1.10.0
- `matplotlib` ≥ 3.7.0

## Tái lập kết quả

### Chạy nhanh (smoke test)

```bash
./reproduce.sh --quick
```

Chạy 2 seeds, chỉ lưới chính. Thời gian: ~30 giây.

### Chạy đầy đủ

```bash
./reproduce.sh
```

Tái lập toàn bộ kết quả trong bài báo:
1. Fetch dữ liệu ERA5 2024–2025 cho 3 trạm (Cần Thơ, Sóc Trăng, Cà Mau)
2. Chạy 7 unit tests + 1 proposition test
3. Chạy full experiment suite (10 seeds, 2 năm)
4. Phân tích thống kê (Wilcoxon paired test)
5. Vẽ 8 hình trong bài

Thời gian: ~2–4 phút trên laptop.

### Chỉ chạy tests

```bash
./reproduce.sh --tests
```

## Kết quả

Sau khi chạy `reproduce.sh`, kết quả nằm trong:

- **CSV/JSON**: `outputs/*.csv`, `outputs/*.json`
- **Hình vẽ**: `figures/*.pdf`, `figures/*.png`
- **Tổng hợp**: `outputs/_benchmark_summary.json`

### Kết quả chính (từ bài báo)

| Phương pháp | Nước (mm) | Unsafe (%) | AWD (pha khô) |
|-------------|-----------|------------|---------------|
| TwinGate+T2 | 232.0 | 8.41 | — |
| Reactive+T2 | 301.3 | 22.28 | — |
| FixedSchedule | 468.0 | 36.91 | — |
| Oracle | 234.7 | 6.57 | — |

### Phát hiện quan trọng

- **Tấn công dịch thời điểm**: giữ nguyên tổng lượng và độ sâu, chỉ dịch thời điểm → tăng số pha khô giả lên 33% (paired, $p < 0.001$)
- **Bộ phát hiện điểm**: kết tội oan 26.7% nông dân trung thực
- **Bộ phát hiện bền vững**: giảm kết tội oan xuống 5.0% nhưng cho qua hầu hết tấn công
- **Neo thiết bị**: đối chiếu 116/116 nhật ký sửa đổi với 0 kết tội oan

## Dữ liệu

Dữ liệu khí tượng ERA5 được fetch tự động từ [Open-Meteo Historical API](https://open-meteo.com/en/docs/historical-weather-api):

- **Biến**: Nhiệt độ, Độ ẩm tương đối, Gió, Áp suất, Mưa
- **Độ phân giải**: giờ, ~11 km
- **Trạm**: Cần Thơ (10.05°N), Sóc Trăng (9.60°N), Cà Mau (9.18°N)
- **Thời gian**: 2024–2025

Không cần API key. Dữ liệu được cache trong `data/era5_multi/`.

## Kiểm tra tính đúng đắn

Các unit tests kiểm tra:

1. **Bảo toàn khối lượng**: residual = 0.000e+00
2. **ET0 đêm = 0**: vật lý đúng
3. **SCS-CN closed-form**: đối chiếu tính tay
4. **Đơn điệu theo twin fidelity**: σ tăng → lệnh phát giảm
5. **Kênh Gilbert–Elliott**: delivery rate khớp lý thuyết

Chạy tests:

```bash
pytest tests/
# hoặc
python tests/test_water_balance.py
```

## Trích dẫn

```bibtex
@article{twingate2026hujos,
  author  = {Mai, Xuân Văn and Phương, Lê Đức Minh and Trị, Nguyễn Đăng and Duy, Trương Khánh and Tri, Nguyễn Tương},
  title   = {Kiểm toán nhật ký tưới neo thiết bị cho chuẩn {Đo đạc–Báo cáo–Thẩm định} lúa phát thải thấp},
  journal = {Hue University Journal of Science: Engineering and Technology},
  year    = {2026},
  note    = {Đang phản biện}
}
```

## Mã đề tài

DHH2025-19-07 — Đại học Huế

## License

Mã nguồn mở, phục vụ nghiên cứu học thuật.

## Liên hệ

- Nguyễn Tương Tri (corresponding author): ntuongtri@hueuni.edu.vn
- Mã nguồn: https://github.com/mxuanvan02/TwinGate-MRV
