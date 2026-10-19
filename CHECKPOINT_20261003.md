# CHECKPOINT 2026-10-03 (v2 — cập nhật sau khi xong việc 1–5)

Đây là file đọc ĐẦU TIÊN khi mở lại. Code ở trạng thái **sạch, chạy được, TẤT CẢ gate xanh**.
Bản v1 (trước khi chạy full grid + C2) đã backup tại `_backups/20261003_214251/`.

---

## TRẠNG THÁI: VIỆC 1–5 XONG, VIỆC 6–8 CÒN LẠI

| # | Việc | Trạng thái | Bằng chứng |
|---|---|---|---|
| 1 | Full grid 2024 (1800 ep) | ✅ EXIT=0 | `outputs/main_raw.csv`, DIFFERENTIATION+SANITY OK |
| 2 | Paired Wilcoxon + effect size | ✅ EXIT=0 | `outputs/wilcoxon_results.csv` (120 so sánh) |
| 3 | Quét σ_frac×δ | ✅ EXIT=0 | `outputs/sweep_sigma_delta_raw.csv` (4320 ep) |
| 4 | ERA5 2025 + full grid 2025 | ✅ EXIT=0 | `main_raw_2025.csv`, `wilcoxon_results_2025.csv` |
| 5 | C2 mặn theo triều | ✅ EXIT=0 | `sweep_salinity_raw.csv` (1800 ep), 7/7 gate PASS |
| 6 | Đọc VM0051 + QĐ4801 + QĐ1490 | ✅ XONG | `NOTES_MRV.md` + `refs/` (3 PDF, sha256, OCR QĐ1490 11/11 trang) |
| 7 | LaTeX → Word (HUJOS spec) | ✅ XONG + ĐÃ DUYỆT VENUE HUJOS-TT | `paper/main.tex` (XeLaTeX **12 trang**, 0 lỗi/0 undefined/0 overfull) + `paper/TwinGate_HUJOS_draft.docx` (**12/12 trang**, khổ 19×27cm, Palatino Linotype 10pt, giãn 1.15, 6pt/3pt, OMML 192 eq, cite Vancouver [n], 25 TLTK) + `paper/build_docx.py` (build tái lập được) |
| 8 | KHÔNG push/nộp khi chưa duyệt | 🔒 LUÔN | — |

**Tests 5/5 suite PASS** sau toàn bộ thay đổi (kể cả C2): water_balance, twin_gate, command_resend, ncs_invariants (I1–I7), tide_salinity (29 checks).

---

## 1. FULL GRID 2024 (1800 episodes, `python3 experiments/run_main.py --seeds 10`)

3 trạm × 2 kênh × 5 budgets × 6 policy × 10 seeds. Trade-off thành hình, gate kiểm đơn điệu PASS.

`unsafe%` TwinGate+T2 theo ngân sách (mild): **b=80:42.21 → 140:30.59 → 200:20.46 → 260:9.15 → inf:0.00**
Tại b=80 mild: TwinGate+T2 **42.21** < Reactive+T2 42.82 < Reactive+blindARQ 44.14 < FixedSchedule 54.04. Oracle 26.27 (reference hợp lệ).
T2 < blindARQ ở **mọi cell** (sent & dup). DIFFERENTIATION + AGRONOMIC SANITY: OK.

### Invariant (6/6 PASS, `tests/test_ncs_invariants.py`, exit 0 — giữ nguyên từ v1, code chưa đổi)

- **I1 budget cứng**: 108 episodes, overshoot tệ nhất = 0.000 mm (bản cũ 215/200)
- **I2 one decision/epoch**: commands_generated ≤ 90 epochs
- **I3 không micro-dose**: mean delivered depth 10.0–35.0 mm, nằm đúng candidate set
- **I4 conservation**: delivered ≤ sent, dup_waste ≤ applied
- **I5 Oracle hợp lệ**: không policy nào hơn Oracle quá 0.5 điểm
- **I6 (KHOA HỌC MẠNH NHẤT)**: không tái neo (OFF) ⇒ σ vượt σ\*=15.18mm ⇒ cổng RỖNG với mọi tập lệnh ⇒ 0 lệnh, unsafe 57.82%, rmse=0.000 là degenerate agreement (cả twin lẫn ruộng đều 0 nước). Bằng chứng thực nghiệm trực tiếp cho hệ quả σ\*.
- **I7 calibration**: coverage 95% thực nghiệm = 0.9906–1.0000 (n=6480/cell) ⇒ σ hơi **bảo thủ** (over-cover) — limitation, không phải lỗi.

## 2. PAIRED WILCOXON + EFFECT SIZE (`experiments/stats_analysis.py`)

Thiết kế: trong mỗi cell (station, network, budget), các policy chạy **cùng seed** ⇒ paired.
So TwinGate+T2 vs 4 baseline trên `unsafe%`. **Holm-Bonferroni** trong cell. Effect size = **rank-biserial r**.
Trung thực: n=10 ⇒ p nhỏ nhất có thể = 0.002; không claim "p<0.001".

**Kết quả 2024** (`wilcoxon_results.csv`): 120 so sánh, **79 significant** (Holm p<0.05),
**105/120 median diff ≤ 0** (TwinGate tốt hơn hoặc hoà), chỉ **4 cell kém hơn** (soc_trang/mild/b=80: +0.046pp, ns — không đáng kể). |r| ~0.6–0.9 (large).
- vs FixedSchedule: **significant ở MỌI cell có budget bind** (p≈0.008, mạnh nhất với n=10).
- Điểm yếu phải khai báo: vs Reactive+T2 tại b=80 vài cell **ns** (diff ~0.1pp); vs blindARQ diff 0.2–3pp, significant hầu hết.

**Kết quả 2025** (`wilcoxon_results_2025.csv`): 120 so sánh, **36 significant**, 93/120 ≤ 0, **0 cell TwinGate thua có ý nghĩa**.
📌 Phát hiện: 2025 **ướt hơn** (Oracle chỉ cần 66.7mm vs 156.7mm 2024) ⇒ unsafe% mọi policy thấp hơn (6.57% vs 42.21% tại b=80) ⇒ nhiều tie.
⇒ **Claim phải condition theo năm khí hậu**: "TwinGate không bao giờ thua; thắng rõ khi nước khan (2024), hoà khi nước dư (2025)".

## 3. SWEEP σ_frac × δ (`experiments/sweep_sigma_delta.py`, 4320 episodes)

σ_frac ∈ {0.05,0.08,0.10,0.12,0.15,0.20} × δ ∈ {0.01,0.03,0.05,0.10,0.15,0.20}, 3 trạm × 2 kênh × b{80,200} × 10 seeds.

**Mặt ngưỡng SẮC NÉT** (không trơn): gate **tê liệt** (unsafe 57.8% = FixedSchedule, 0 lệnh) khi σ_frac×z(δ) vượt ngưỡng; **sống** (19.9%) khi dưới. Ranh giới đi chéo:
- (σ=0.10, δ≤0.03) chết; (σ=0.10, δ≥0.05) sống
- (σ=0.15) cần δ≥0.20 mới sống
- Đây là **bằng chứng thực nghiệm 2 chiều cho hệ quả σ\*** — mạnh hơn cả I6 (vốn chỉ 1 chiều).
- ⚠️ Mặt Pareto dạng **BƯỚC NHẢY** (lượng tử hoá theo candidate depth {10,20,35}), không trơn ⇒ mô tả trung thực.
- withheld_frac tại b=80 bị **trần ngân sách** (mean 0.955) ⇒ flat là đúng vật lý, gate loại trừ có ghi chú.

## 4. ERA5 2025 + FULL GRID 2025

`data/fetch_era5_multi.py --year 2025` (đã thêm `--year`). 3 trạm × 8760 giờ × 5 biến, **0 null**, provenance OK.
`load_weather`/`run_episode`/`run_main` đều có `year=`. Full grid 2025 EXIT=0, DIFFERENTIATION+SANITY OK. Tests 4/4 vẫn PASS.

## 5. C2 — MẶN THEO TRIỀU (quyết định đã chốt: SCENARIO, KHÔNG vào Abstract)

**Code mới:** `src/tide_salinity.py` + `tests/test_tide_salinity.py` (29/29 PASS) + `experiments/sweep_salinity.py` (1800 ep, **7/7 gate PASS**).

**Quyết định (tự chốt theo quyền 2026-10-03 + đúng quy tắc (a)(b)(c) DESIGN_VN §3):**
KHÔNG có số đo mặn thực địa tại 3 trạm ⇒ C2 là **scenario model + quét độ nhạy**, KHÔNG vào Abstract. Chỉ `EC_crit` lúa có nguồn (Maas&Hoffman 3.0 / Grattan 1.9 dS/m, USDA P572).

**Mô hình:** triều bán nhật M2 (12.4206h, hằng vật lý) + bảng EC theo tháng (LO/HI, đỉnh mặn III–V) + `intrusion` là **bội số độ mạnh xâm nhập** (quét, không khẳng định). `EC_src = ec_river + intrusion·(ec_table − ec_river)`.

**Cơ chế trong `run_episode` (sal != None):** policy mặn-aware (TwinGate*, Oracle) chỉ mở cống ở **giờ ngọt** (EC_src ≤ EC_crit theo giai đoạn) — "chờ con nước". Chờ KHÔNG tốn epoch; nếu hết epoch không có giờ ngọt ⇒ `withheld_saline`. Baseline (Reactive/Fixed) bơm bất kể ⇒ tích muối. `sal=None` **bit-identical** bản cũ (test 8a).

**Kết quả sweep (mean):**
- **Gate KHÔNG BAO GIỜ bơm mặn**: salt_excess = **0.0 đúng** ở mọi cell (G1).
- Baseline tích muối: Reactive mean 798 / max **2754 dS·mm**; Fixed mean 725 / max 2518.
- **Giá của "chờ con nước"** (Δunsafe gate vs Reactive, i=1.0 central): +1.84 đến +8.90pp unsafe **để tránh 534–795 dS·mm muối**. Tại i≤0.5: gate **thắng cả hai chiều** (ít muối hơn, không kém an toàn hơn).
- **Mặn gắt (i=2.0, grattan_strict)**: fresh 0% ⇒ withheld_saline **100%** epochs, unsafe 56.8–58.8% ⇒ **tê liệt giống hệ quả σ\*** (G7). Đây là hệ quả thứ hai của "cổng rỗng".
- Variant EC_crit **có đổi kết quả** (G6) ⇒ quét variant không trang trí.

**BUG #9 ĐÃ BẮT (vật lý, không phải test):** `salt_load_and_yield_loss` ban đầu ngoại suy tuyến tính −12%/dS·m vô hạn ⇒ est_yield_loss **169–173%** (mất mùa >100% bất khả thi). Sửa: **cap 100%**, `mean_excess` vẫn trả không cap (đại lượng đo thật). Test 7 verify. Limitations: dịch tuyến tính + cap, không phải mô hình năng suất đầy đủ.

---

## 🐛 9 BUG ĐÃ BẮT (1–8 xem bản v1; thêm #9 ở mục 5 trên)

## ⚠️ 3 LỖI CỦA CHÍNH TEST/GATE (bài học lặp lại — QUAN TRỌNG NHẤT)

1. Bound "20–35mm" SCS-CN **bịa bằng mắt** ⇒ test sai, code đúng (13.80mm). (v1)
2. Assertion what-if **ngược dấu vật lý** (đòi w giảm khi tưới). (v1)
3. **LẶP LẠI ở C2:** gate G3 sweep_salinity viết `b < a` ⇒ flag đúng hành vi "fresh_frac giảm khi mặn hơn" là vật lý ĐÚNG. Tính tay [0.497,0.194,0.026] là giảm ⇒ code đúng, gate sai. (Đã sửa + ghi trong code.)

**QUY TẮC (đã thành luật, lặp 3 lần): test/gate fail thì TÍNH TAY/ĐO ĐỘC LẬP trước khi quyết sửa code hay sửa test. Cùng loại lỗi: monotonicity check viết ngược dấu. ĐÃ GHI VÀO MEMORY.**

---

## 🚨 BẪY MÔI TRƯỜNG (giữ nguyên từ v1, vẫn đúng)

1. `execute_code` giữ module trong `sys.modules` — sau patch, kernel import bản CŨ. **Luôn chạy test/experiment qua `terminal` process mới** + `find . -name __pycache__ -type d -exec rm -rf {} +` trước.
2. Không pipe qua `tail` (che fail). Dùng `; echo EXIT=${PIPESTATUS[0]}`.
3. Gate báo động giả ⇒ sửa gate, không sửa experiment. (Đúng 2 lần: budget=inf ở v1, fresh_frac ở C2.)
4. 4 DOI đoán sai — xem `REFERENCES.md` mục 0. Luôn resolve qua Crossref.
5. `web_search` lỗi 6/21 query; `web_extract` fail trên .gov.vn; DBLP chết 2 client.

---

## VIỆC CÒN LẠI (6–8)

6. **Đọc toàn văn VM0051 v1.1 + QĐ 4801/2025 + QĐ 1490** trước khi claim bài toán khớp chuẩn MRV. (web_search/web_extract; nếu .gov.vn CRAWL_TIMEOUT ⇒ xin anh link, không đoán.)
7. **LaTeX → Word** theo `HUJOS_venue_spec.md` (Palatino 10pt, ≤12 trang, Vancouver [số], tóm tắt ≤250 từ ×2 ngôn ngữ, chữ ký tác giả). Dùng skill `latex-to-venue-word-template` / `document-skills:docx`.
8. **KHÔNG push, KHÔNG nộp** khi chưa được anh duyệt.

**Câu hỏi mở cho anh (không tự chốt được):** bài báo sẽ **ghép C2 vào câu chuyện chính** (3 ràng buộc nhiệt↔mặn↔nước, nhấn mạnh sự ghép ngược chiều) hay **giữ C2 là phân tích tình huống riêng** (vì không có số đo mặn)? Điều này quyết định cấu trúc Results + có đưa "chờ con nước" vào Abstract hay không (hiện tại: KHÔNG, đúng quy tắc §3).

## Limitations PHẢI có trong bài (cập nhật, không giấu)

- I7 coverage 0.99–1.00 > 0.95 ⇒ σ **bảo thủ**, gate withhold nhiều hơn tối ưu.
- T2 là nghiệm **myopic**; DP đầy đủ để mở.
- **C2 là scenario model** (không số đo mặn thực địa); bảng EC theo tháng + intrusion là tham số tình huống, bắt buộc quét độ nhạy, **không vào Abstract**.
- `est_yield_loss` là **dịch tuyến tính −12%/dS·m + cap 100%**, không phải mô hình năng suất đầy đủ.
- DBLP chưa quét được ⇒ chưa loại trừ prior art venue VN (KSE/RIVF/ACIIDS/IUKM).
- Mô phỏng, chưa thực địa; N=3 trạm; đất dùng tham số TB FAO-56 Table 2.
- Tranh cãi nông học: USDA ghi lúa mẫn cảm **mặn** nhất ở mạ (trổ còn tranh cãi), mẫn cảm **nhiệt** đỉnh ở trổ ⇒ hai đỉnh lệch giai đoạn, nêu cả hai phía.
- **Kết quả condition theo năm khí hậu**: 2024 khan nước (trade-off rõ), 2025 dư nước (nhiều tie). Không gộp 2 năm thành một claim duy nhất.

## Files (cập nhật)

```
TwinGate_K1/
  CHECKPOINT_20261003.md   ← FILE NÀY (v2)
  _backups/20261003_214251/CHECKPOINT_20261003.md   (v1)
  REFERENCES.md  PROBLEM_VN_2026.md  PROPOSAL.md  THEORY.md  DESIGN_VN.md  STATUS.md(cũ)
  src/water_balance.py     FAO-56 ET0 + bucket        — test PASS
  src/twin_gate.py         cổng chance-constrained    — test PASS
  src/command_resend.py    T2 + belief filter          — test PASS
  src/tide_salinity.py  ★  C2 mặn theo triều (MỚI)    — test PASS
  src/ncs_loop.py          vòng NCS 3 trạng thái + C2  — 6/6 invariant + C2 PASS
  tests/                   5 suite (thêm test_tide_salinity.py) + diag — TẤT CẢ PASS
  experiments/run_main.py         quick+full+--year   — PASS
  experiments/stats_analysis.py ★ Wilcoxon paired     — PASS (nhận argv = raw csv)
  experiments/sweep_sigma_delta.py★ mặt ngưỡng σ×δ    — PASS
  experiments/sweep_salinity.py ★ sweep C2 độ nhạy    — 7/7 gate PASS
  outputs/
    main_raw.csv (1800) + main_summary.csv         [2024 full]
    main_raw_2025.csv + main_2025_summary.csv      [2025 full]
    wilcoxon_results.csv (120) + _2025.csv (120)   [paired stats]
    sweep_sigma_delta_raw.csv (4320)               [mặt ngưỡng σ×δ]
    sweep_salinity_raw.csv (1800)                  [C2 độ nhạy]
    quick_*, sweep_quick, sweep_salinity_quick     [smoke]
  data/era5_multi/         ERA5 2024 + 2025, 3 trạm, 5 biến, 0 null, provenance
  data/fetch_era5_multi.py đã thêm --year
  gapscan_K1/ gapscan_MRV/  1235 + 461 + 2002 bài HUJOS
```

## Chạy lại toàn bộ (fresh process, ~5 phút)

```bash
cd /media/SAS/Van/DeTai2025/TwinGate_K1
find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null
for t in tests/test_*.py; do python3 "$t" >/dev/null 2>&1; echo "$t EXIT=$?"; done
python3 experiments/run_main.py --seeds 10; echo EXIT=$?           # 2024 full
python3 experiments/stats_analysis.py; echo EXIT=$?                # Wilcoxon 2024
python3 experiments/sweep_sigma_delta.py; echo EXIT=$?             # mặt σ×δ
python3 experiments/sweep_salinity.py; echo EXIT=$?                # C2
```
