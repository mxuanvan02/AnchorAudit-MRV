# TwinGate-MRV — Device-Anchored Irrigation Log Auditor

Mã nguồn tái lập toàn bộ kết quả của bài báo
**"Hạn chế của kiểm toán vật lý nhật ký tưới và giải pháp neo theo thiết bị
trong đo đạc, báo cáo, thẩm định lúa phát thải thấp"** (Hue University
Journal of Science, 2026).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Python](https://img.shields.io/badge/python-%E2%89%A53.10-blue.svg)

## Tổng quan

Khâu đo lường, báo cáo, thẩm định (MRV) chiếm khoảng **77 %** chi phí chuyển
đổi lúa phát thải thấp thành tín chỉ các-bon. Bài báo đề xuất một **tầng kiểm
toán đa tầng** đặt trên lớp "bóng số" (digital shadow) của mô hình cân bằng
nước FAO-56:

1. **Bộ lọc vật lý** ($V_1, V_4, V_5$) — phát hiện khai báo vô lý khi phát lại
   nhật ký trên cân bằng nước FAO-56 theo giờ với dữ liệu ERA5 công khai.
2. **Bộ phát hiện bền vững** — giao trên tập bất định $\Theta$ ($|\Theta| = 150$)
   để hạ tỷ lệ kết tội oan.
3. **Phép đối chiếu thiết bị** — neo nhật ký nông dân vào bản ghi lệnh có chữ ký
   của thiết bị ghi lệnh.
4. **Phân tích tấn công dịch thời điểm** — chứng minh điểm mù của phòng thủ
   tổng hợp (Mệnh đề 1, Mệnh đề 2).

Hệ thống được mô tả đúng như một **bóng số**: dữ liệu chảy một chiều từ thực tế
vào mô hình. Bản sao hai chiều có cổng chặn lệnh tiền phát là hướng phát triển
tương lai, chưa phải nội dung bài báo.

## Cấu trúc thư mục

```
TwinGate-MRV/
├── data/                     # Fetch dữ liệu ERA5 từ Open-Meteo (+ provenance)
│   ├── fetch_era5_multi.py
│   └── era5_multi/*.provenance.json
├── src/                      # Mã nguồn cốt lõi
│   ├── water_balance.py      # Cân bằng nước FAO-56 (bucket, ET0, SCS-CN)
│   ├── log_filters.py        # Bộ lọc vật lý V1/V4/V5 + tập bất định Θ
│   ├── twin_gate.py          # Bản sao số + cổng an toàn (phần NCS)
│   ├── ncs_loop.py           # Vòng lặp mạng có điều khiển
│   ├── command_resend.py     # Chiến lược gửi lại lệnh
│   └── tide_salinity.py      # Thuỷ triều / xâm nhập mặn
├── experiments/              # Thí nghiệm khoa học
│   ├── run_main.py           # Lưới chính (7 560 episodes/năm × 2 năm)
│   ├── fraud_detection.py    # Phát hiện gian lận trên 281 nhật ký
│   ├── robust_audit_eval.py  # Đánh giá bộ lọc bền vững (Θ rút gọn / đầy đủ)
│   ├── reality_gap_probe.py  # Bảy trục khoảng cách thực tế
│   ├── benchmark_confirmation.py, benchmark_mrv.py   # Đối chứng
│   ├── run_ablation.py, run_deployment.py, run_multi_field.py
│   ├── sweep_sigma_delta.py, sweep_salinity.py
│   ├── measure_net_loss_intervals.py  # Nguồn số liệu Mệnh đề 2
│   ├── stats_analysis.py     # Kiểm định ghép cặp Wilcoxon
│   ├── analyze_robust_eval.py
│   ├── make_verified_numbers.py   # Snapshot mọi con số công bố
│   └── diag_f2.py
├── figures/                  # Script vẽ hình (kết quả thí nghiệm)
│   ├── fig_method.py, fig_results.py
│   └── fig*.pdf / fig*.png
├── paper_qa/                 # Script kiểm tra chất lượng bản thảo LaTeX
│   │                         # (KHÔNG phải thí nghiệm; không do reproduce.sh gọi)
│   ├── check_*.py            # Từ viết tắt, số liệu, ký tự lạ, tiêu đề...
│   ├── measure_fonts.py, measure_pagebudget.py, ...
│   ├── verify_paper_claims.py, qa_hujos_layout.py
│   └── make_tables_*.py      # Sinh bảng LaTeX từ outputs/
├── tests/                    # Kiểm tra bất biến vật lý (7 file, xem tests/README.md)
├── outputs/                  # Kết quả CSV/JSON đã commit làm snapshot đối chiếu
├── reproduce.sh              # Một lệnh tái lập toàn bộ
├── requirements.txt          # Phụ thuộc tối thiểu (chạy được)
├── requirements.lock         # Phiên bản đã pin (tái lập bit-level)
├── pyproject.toml            # Metadata dự án
├── CITATION.cff              # Trích dẫn chuẩn (GitHub hiện nút "Cite")
├── LICENSE                   # MIT
└── README.md
```

## Cài đặt

### Yêu cầu

- Python ≥ 3.10 (đã kiểm trên 3.10–3.14)
- Khoảng 2 GB dung lượng trống (dữ liệu ERA5 + kết quả)
- Không cần API key

### Cài phụ thuộc

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt      # phiên bản tối thiểu
# hoặc, để tái lập đúng bản đã dùng khi viết bài:
pip install -r requirements.lock     # phiên bản đã pin
```

Phụ thuộc: `numpy`, `scipy`, `matplotlib`. Không có phụ thuộc nào khác.

## Tái lập kết quả

### Chạy nhanh (smoke test, ~30 giây)

```bash
./reproduce.sh --quick
```

Hai seeds, chỉ lưới chính. Dùng để kiểm tra môi trường.

### Chạy đầy đủ (~2–4 phút trên laptop)

```bash
./reproduce.sh
```

Thực hiện tuần tự:

1. Tạo `.venv`, cài phụ thuộc
2. Fetch dữ liệu ERA5 theo giờ 2024–2025 cho ba trạm (Cần Thơ, Sóc Trăng, Cà Mau);
   dùng lại cache nếu đã có
3. Chạy 7 file kiểm tra bất biến vật lý
4. Chạy toàn bộ thí nghiệm: lưới chính, ablation, deployment, đa thửa ruộng,
   sweep σ×δ, kịch bản xâm nhập mặn, phát hiện gian lận trên 281 nhật ký,
   đánh giá kiểm toán bền vững (Θ rút gọn và Θ đầy đủ)
5. Sinh hai snapshot kiểm toán — nguồn của mọi con số trong bài
6. Phân tích thống kê ghép cặp và vẽ lại mọi hình

Mọi số liệu công bố trong bài đều do các script này ghi ra dưới dạng CSV/JSON,
nên kết quả không thể lệch khỏi mã sinh ra nó.

### Chỉ chạy kiểm tra bất biến

```bash
./reproduce.sh --tests
```

### Kiểm tra chất lượng bản thảo LaTeX (tuỳ chọn)

```bash
python3 paper_qa/check_acronym_first_use.py     # ví dụ
```

Các script trong `paper_qa/` phục vụ kiểm tra bản thảo (từ viết tắt, ký tự lạ,
ngân sách trang, đối chiếu số liệu với `outputs/`). Chúng không thuộc luồng tái
lập khoa học và không được `reproduce.sh` gọi.

## Kết quả

Sau khi chạy `reproduce.sh`:

- **CSV/JSON**: `outputs/*.csv`, `outputs/*.json`
- **Hình vẽ**: `figures/*.pdf`, `figures/*.png`
- **Tổng hợp**: `outputs/_benchmark_summary.json`
- **Mọi con số công bố**: `outputs/_verified_numbers.json`

### Phát hiện chính của bài báo

- **Tấn công dịch thời điểm**: giữ nguyên tổng lượng và độ sâu, chỉ dịch thời
  điểm → số pha khô đủ điều kiện tăng **+33 %** (ghép cặp, $p < 0{,}001$) trên
  chín nhật ký bị sửa. Đây là tăng của một chỉ báo vật lý, chưa phải thiệt hại
  tín chỉ.
- **Bộ phát hiện mô hình đơn cấu hình**: kết tội oan **26,7 %** nông dân trung thực.
- **Bộ phát hiện bền vững**: hạ kết tội oan xuống **5,0 %** nhưng để lọt **8/9**
  tấn công dịch thời điểm.
- **Phép đối chiếu thiết bị**: bắt **116/116** nhật ký bị sửa, **0/60** kết tội oan.

### Bảng đối chứng NCS (phần mở rộng, chưa phải nội dung chính của bài)

| Phương pháp | Nước (mm) | Unsafe (%) |
|-------------|-----------|------------|
| TwinGate+T2 | 232.0 | 8.41 |
| Reactive+T2 | 301.3 | 22.28 |
| FixedSchedule | 468.0 | 36.91 |
| Oracle | 234.7 | 6.57 |

## Dữ liệu

Dữ liệu khí tượng ERA5 được fetch tự động từ
[Open-Meteo Historical API](https://open-meteo.com/en/docs/historical-weather-api):

- **Biến**: nhiệt độ, độ ẩm tương đối, gió, áp suất, mưa
- **Độ phân giải**: theo giờ, ~11 km
- **Trạm**: Cần Thơ (10,05°N), Sóc Trăng (9,60°N), Cà Mau (9,18°N)
- **Thời gian**: 2024 (khan nước) và 2025 (thừa nước)

Không cần API key. Dữ liệu được cache trong `data/era5_multi/`; mỗi lần fetch ghi
một file `*.provenance.json` để truy vết nguồn và thời điểm lấy dữ liệu.

## Kiểm tra tính đúng đắn

Bảy file kiểm tra bất biến vật lý:

1. **Bảo toàn khối lượng** — residual = 0.000e+00
2. **ET0 ban đêm = 0** — đúng vật lý
3. **SCS-CN dạng đóng** — đối chiếu tính tay
4. **Đơn điệu theo độ trung thực của bản sao** — σ tăng → số lệnh phát giảm
5. **Kênh Gilbert–Elliott** — tỷ lệ giao khớp lý thuyết
6. **Bất biến NCS** — các bất biến vòng lặp
7. **Mệnh đề $d_{\max}$** — đối chiếu mệnh đề trong bài

Chạy bằng Python trực tiếp, **không dùng `pytest`** (chi tiết và kết quả kỳ vọng
của từng file: xem [`tests/README.md`](tests/README.md)):

```bash
for f in tests/test_*.py; do python3 "$f" || echo "FAIL: $f"; done
# hoặc
./reproduce.sh --tests
```

## Trích dẫn

```bibtex
@article{van2026twingate,
  author  = {Mai, Xuân Văn and Lê, Đức Minh Phương and Nguyễn, Đăng Trị
             and Trương, Khánh Duy and Nguyễn, Tương Tri},
  title   = {Hạn chế của kiểm toán vật lý nhật ký tưới và giải pháp neo theo
             thiết bị trong đo đạc, báo cáo, thẩm định lúa phát thải thấp},
  journal = {Hue University Journal of Science: Engineering and Technology},
  year    = {2026},
  note    = {Đang phản biện}
}
```

Hoặc dùng file [`CITATION.cff`](./CITATION.cff) (GitHub hiển thị nút **Cite this
repository**).

## Mã đề tài

DHH2025-19-07 — Đại học Huế.

## Giấy phép

[MIT](./LICENSE) — © 2026 các tác giả. Được phép dùng, sửa, phân phối cho mục
đích nghiên cứu và thương mại, kèm giữ nguyên thông báo bản quyền.

## Liên hệ

- Nguyễn Tương Tri (tác giả liên hệ): ntuongtri@hueuni.edu.vn
- Lê Đức Minh Phương (đồng tác giả liên hệ): Ldmphuong@hueuni.edu.vn
- Mã nguồn: <https://github.com/mxuanvan02/TwinGate-MRV>
