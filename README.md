# AnchorAudit-MRV

Mã nguồn tái lập toàn bộ thực nghiệm của bài báo:

> **Giới hạn của kiểm toán vật lý nhật ký tưới và điều kiện áp dụng neo theo thiết bị trong đo đạc, báo cáo, thẩm định lúa phát thải thấp**  
> Mai Xuân Văn, Lê Đức Minh Phương\*, Nguyễn Đăng Trị, Trương Khánh Duy, Nguyễn Tương Tri\*  
> *Tạp chí Khoa học Đại học Huế (Hue University Journal of Science)*, 2026.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Python](https://img.shields.io/badge/python-%E2%89%A53.10-blue.svg)

## Phạm vi nghiên cứu

Kho mã này phục vụ tái lập trực tiếp các bảng kết quả và kiểm định của bài báo về ba tầng kiểm toán nhật ký tưới khô-ướt luân phiên (AWD) trên dữ liệu khí tượng tái phân tích ERA5 (Cần Thơ, Sóc Trăng, Cà Mau; năm 2024--2025):

1. **Tầng 1 — Mô hình đơn cấu hình** ($\theta_0$, ngưỡng tuyệt đối $\tau_0 = 5$~mm, bộ lọc $V_1, V_4, V_5$).
2. **Tầng 2 — Bộ phát hiện bền vững** ($V_{\mathrm{rob}}(L) = \bigcap_{\theta \in \Theta} V_\theta(L)$ kết hợp ngưỡng co giãn $\tau(N_{\mathrm{event}})$ với $\sigma_{\mathrm{event}} = 7{,}67$~mm).
3. **Tầng 3 — Neo theo bản ghi thiết bị** (đối chiếu hai hiệu đa tập $\Delta^-, \Delta^+$ và $\Delta_{\mathrm{depth}}$ với bản ghi có chữ ký $\mathcal{G}$ dưới giả thiết thiết bị toàn vẹn — kiểm tra tính nhất quán nội tại).

## Tái lập nhanh (1 lệnh)

Yêu cầu: Python $\ge$ 3.10 (`numpy`, `scipy`, `matplotlib`). Không cần API key (dữ liệu ERA5 đã được lưu sẵn kèm tệp truy vết trong `data/era5_multi/`).

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.lock
bash reproduce_paper.sh
```

Thời gian chạy toàn bộ kiểm định và thực nghiệm của bài báo: ~1--2 phút trên máy tính cá nhân.

## Ánh xạ Bảng trong bài báo $\leftrightarrow$ Mã nguồn & Đầu ra

| Thành phần bài báo | Script sinh dữ liệu | Tệp đầu ra đối chiếu |
|---|---|---|
| Bảng 1 (Tham số mô hình & ngoài $\Theta$) | `src/log_filters.py`, `experiments/out_of_theta_probe.py` | — |
| Bảng 2 (Thiết kế $2\times 2$ tách $\Theta$ và $\tau$) | `experiments/robust_audit_eval.py --seeds 10` | `outputs/eval_theta_reduced_10seeds.csv` |
| Bảng 3 (Cảnh báo giả trên $60$ nhật ký trung thực) | `experiments/robust_audit_eval.py --seeds 10` | `outputs/eval_theta_reduced_10seeds.csv` |
| Bảng 4 (Số pha khô $n_{\mathrm{dry}}$, ghép cặp) | `experiments/robust_audit_eval.py --seeds 10` / `--full-theta --seeds 3` | `outputs/eval_theta_reduced_10seeds.csv`, `outputs/eval_theta_full_3seeds.csv` |
| Bảng 5 (Độ nhạy theo ngưỡng $d_{\mathrm{dry}}$) | `experiments/sweep_dry_threshold.py` | `outputs/sweep_dry_threshold.csv` |
| Bảng 6 (Tỷ lệ phát hiện trên $116$ nhật ký bị sửa) | `experiments/robust_audit_eval.py --seeds 10` | `outputs/eval_theta_reduced_10seeds.csv` |
| Kiểm tra ngoài $\Theta$ (Mục 3.2) | `experiments/out_of_theta_probe.py`, `experiments/out_of_theta_fraud.py`, `experiments/make_out_of_theta_summary.py` | `outputs/_out_of_theta_summary.json` |

## Tóm tắt kết quả chính (từ bản chạy đối chiếu)

- **Cảnh báo giả (nhật ký có nhiễu, $n=60$):** Đơn cấu hình ($\tau_0$) $16/60$ ($26{,}7\%$); đổi riêng ngưỡng co giãn $\tau(N_{\mathrm{event}})$ còn $5/60$ ($8{,}3\%$); kết hợp giao trên $\Theta$ rút gọn còn $3/60$ ($5{,}0\%$); neo thiết bị $0/60$ (tính nhất quán nội tại).
- **Tấn công dịch thời điểm ($d_{\mathrm{dry}}=0{,}45$):** Tăng trung bình $+0{,}61$ pha trên toàn bộ $23$ nhật ký mục tiêu ($+12{,}5\%$); trên $9$ nhật ký leo đồi sửa thành công tăng $+1{,}56$ pha ($4{,}78 \to 6{,}33$, $+32{,}6\%$); bộ phát hiện bền vững bỏ lọt $8/9$ ca (và $22/24$ ca khi gộp cả $5$ ngưỡng $d_{\mathrm{dry}}\in\{0{,}05;\,0{,}20;\,0{,}45;\,0{,}80;\,0{,}95\}$).
- **Kiểm tra ngoài $\Theta$ ($n=42$ trung thực, $n=20$ dịch thời điểm):** Cảnh báo giả $17/42$ ($40{,}5\%$, đơn cấu hình), $1/42$ ($2{,}4\%$, ngưỡng co giãn), $0/42$ ($0{,}0\%$, bền vững); phát hiện dịch thời điểm lần lượt $6/20$, $1/20$, $0/20$.
- **Neo thiết bị ($281$ nhật ký mô phỏng):** Phát hiện $116/116$ nhật ký bị sửa ($107/107$ gian lận xác nhận sau khi tách $9$ ca bỏ sót lệnh sang đối soát) và $0/120$ cảnh báo giả dưới giả thiết bản ghi thiết bị toàn vẹn.

## Cấu trúc cốt lõi

```text
AnchorAudit-MRV/
├── data/                # Khí tượng ERA5 (Open-Meteo) kèm provenance
├── src/                 # Cân bằng nước FAO-56, bộ lọc vật lý V1/V4/V5, tập bất định Θ
├── experiments/         # Kịch bản đánh giá, quét độ nhạy d_dry và kiểm tra ngoài Θ
├── tests/               # Kiểm tra bất biến vật lý và bộ lọc
├── outputs/             # Tệp CSV/JSON đối chiếu với các bảng trong bài
├── reproduce_paper.sh   # Tái lập một lệnh toàn bộ kết quả bài báo
├── requirements.lock    # Phiên bản phụ thuộc cố định
└── LICENSE              # Giấy phép MIT
```

## Tài trợ & Liên hệ

Nghiên cứu được tài trợ bởi Đại học Huế trong khuôn khổ đề tài mã số **DHH2025-19-07**.

- Tác giả liên hệ: `Ldmphuong@hueuni.edu.vn`; `ntuongtri@hueuni.edu.vn`.
