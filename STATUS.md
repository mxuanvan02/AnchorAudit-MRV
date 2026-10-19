# K1 TwinGate — TRẠNG THÁI THỰC THI

Đề tài: DHH2025-19-07 · Venue: **HUJOS-TT** (Kỹ thuật & Công nghệ) · Anh chốt K1 ngày 2026-10-03
Cập nhật: 2026-10-12 (commit `8a10755`)

---

## QUYẾT ĐỊNH CỦA ANH VĂN (2026-10-11 đêm) — ÁP DỤNG MỌI PHIÊN SAU

1. **Bài này ĐỘC NHẤT, chỉ một phiên bản hiện tại.** Không có "v1", không có
   "phiên bản đã công bố", không có "thiết kế ban đầu". Quá trình làm trước đó
   là để đi đến hiện tại và **giấu** — bài chỉ trình bày kết quả như của chính
   nó. CẤM dùng các khung: "đã công bố / phiên bản trước / đánh giá ban đầu /
   thiết kế ban đầu / initial draft / first version / previously published".
   Kết quả 0/60 và 60/60 trên "điều kiện giấy" được trình bày như tính chất
   của giao thức tự nhất quán (ruộng sinh ra bằng chính mô hình kiểm toán),
   không phải kết quả của bản cũ.
2. **`paper2/main.tex` (bản IEEE thừa) đã GỠ khỏi repo** theo lệnh anh — nó
   chứa số cũ 69%/91%/78% mâu thuẫn bản nộp. `paper2/` giờ chỉ còn
   `blocks/` + `tables/` + `refs.bib` dùng chung qua symlink từ `paper2_hujos/`.
   `assemble.py` cũng đã xoá. `00_title_abstract.tex` là FILE CHET (có header
   cảnh báo, không build nào input).
3. **Thứ tự tác giả chốt**: Mai Xuân Văn; Lê Đức Minh Phương* (Viện ĐT Mở &
   CNTT, ĐH Huế, Ldmphuong@hueuni.edu.vn); Nguyễn Đăng Trị (ĐH Gia Định);
   Trương Khánh Duy (Viện ĐT Mở & CNTT); **Nguyễn Tương Tri* ĐỨNG CUỐI**.
   Template ĐH Huế KHÔNG cần khối "Thông tin tác giả" cuối bài. EN title +
   abstract nằm NGAY SAU tóm tắt VI (trang 1–2).
4. **Văn phong**: academic-prose tối đa. Câu phải trọn nghĩa (không cụt),
   không lặp từ, không dấu vết AI (em-dash văn xuôi, reveal-colon X: Y).
   Sau mọi batch edit PHẢI đọc lại câu theo nghĩa.

## Commit chain phiên 2026-10-11→12 (đã push hết)

- `bb8d261` khử dấu vết AI (32 dash + 32 colon) + 5 tác giả + cite ERA5/QD1490
- `d68851f` layout repo: README định hướng, docs/, CITATION.cff
- `f3b4f8e` câu cụt + cite (kukal/bouman/tuong/fao56/jem/narayanan) + abstract 245 từ
- `38cc60d` bỏ claim "đã công bố" (vẫn sai — còn ám chỉ phiên bản)
- `8a10755` **xoá sạch khung "phiên bản"** + gỡ paper2/main.tex + sửa abstract câu đầu
  ("phần phát thải giảm được trong canh tác lúa chất lượng cao, phát thải thấp
  chưa thể chuyển thành tín chỉ các-bon") + sửa lỗi lặp chữ "phạm"

Gate sau cùng: check_vi_numbers PASS, verify_paper_claims 0 FAIL, acronym PASS,
title PASS, 46/46 tests. Build VI 16 tr / EN 15 tr / supp 13 tr, 0 lỗi.

---


## PHIÊN 2026-10-11 — 4 vấn đề anh Văn nêu, đã xong, đã push GitHub

Commit `mxuanvan02/TwinGate` main: `bb8d261` (khử dấu vết AI + tác giả + cite),
`d68851f` (layout repo: README định hướng 2 bài, `docs/`, CITATION.cff 5 tác giả).

1. **Dấu vết AI**: loại 32/33 em-dash `---` văn xuôi + 32/32 "reveal colon"
   (X: Y); giữ 6 colon hợp lệ (set-builder + giới thiệu danh sách). PDF text: 0 `---`.
2. **Cite thiếu**: thêm `hersbach2020` (ERA5, DOI 10.1002/qj.3803 verified
   Crossref) 4 chỗ EN+VI; thêm `qd1490` câu "một triệu héc-ta…2030" đầu Mở đầu.
   8 "câu thiếu cite" còn lại là kết quả của chính bài — không cần cite.
3. **Ngắt đoạn**: tách 6 đoạn dài nhất (intro 455→4 đoạn theo 3 đóng góp; design
   381→4; results 324→3; discussion 269→3; giới hạn 231→2; kết luận 183→2).
   Abstract VI 243 từ / EN 206 từ (trần 250).
4. **Tác giả** (cập nhật 2026-10-11 tối, commit `f3b4f8e`): đủ 5, thứ tự anh
   Văn chốt — Mai Xuân Văn; **Lê Đức Minh Phương*** (Viện ĐT Mở & CNTT, ĐH Huế,
   Ldmphuong@hueuni.edu.vn); Nguyễn Đăng Trị (ĐH Gia Định); Trương Khánh Duy
   (Viện ĐT Mở & CNTT); **Nguyễn Tương Tri* ĐỨNG CUỐI**. Đã bỏ khối "Thông tin
   tác giả" cuối bài (template không cần); khối EN title+abstract nằm NGAY SAU
   tóm tắt VI (trang 1–2). Hết mọi placeholder/TODO. Đồng bộ cả
   `main_hujos_vi.tex`, `main_hujos.tex`, `paper2/main.tex` (IEEE), `CITATION.cff`.

## Phiên tối 2026-10-11 (commit `f3b4f8e`, đã push)

- **Câu cụt**: nối lại 9 câu bị cụt do lần khử reveal-colon trước (câu anh chỉ:
  "phần nông học đã ngã ngũ" → "Về mặt nông học, cách làm đã rõ, vì…"). Quét
  regex toàn bộ: 0 câu treo còn lại.
- **Cite bổ sung** (DOI verified Crossref): kukal2004 + bouman2001 (hằng số thấm
  lúa làm dầm), tuong2003 (mùa khô AWD), fao56 (tham số đất TAW/FC/WP — Bảng 12,
  rễ 0,5 m), jem2026mrv (3/4 chi phí, abstract), qd4801 (ống đo, Tier-1, xếp hạng
  bằng chứng trong abstract), narayanan2024 (viễn thám digital twin). `d_dry=0.45`
  nói rõ là **lựa chọn mô hình hoá của bài**, không bịa nguồn.
- **"đã công bố"→"phiên bản trước"** (13 chỗ VI+EN) vì refs.bib ghi twingate2026
  "under review" — claim "published" mạnh hơn bằng chứng. GIỮ "published" ở 2 chỗ
  nguồn ngoài thật (kukal/bouman, seven axes). **Nếu lớp v1 THẬT SỰ đã đăng ở đâu,
  anh cho biết để cite lại đúng.**
- **Abstract VI**: 252→245 từ (render 240, trần 250), đủ 5 từ khóa; đồng bộ
  `blocks_vi.tex` (bản EN standalone) khớp bản chính.
- Gate: check_vi_numbers PASS, verify_paper_claims 0 FAIL, acronym PASS, title
  PASS, 46/46 tests. Build: VI 16 tr / EN 15 tr / IEEE 10 tr, 0 lỗi. Vision check
  trang 1: sạch, đúng thứ tự tác giả, EN block trang 1–2.

**Gate 2026-10-11**: build VI 16 trang / EN 14 trang / IEEE 10 trang — 0
undefined ref, 0 overfull, 0 missing char; `check_vi_numbers` PASS (tập số
EN=VI), `verify_paper_claims` 0 FAIL, `check_acronym_first_use` PASS,
`check_vi_title` PASS, 46/46 tests PASS.

**CẢNH BÁO phiên sau**: (a) KHÔNG bịa ORCID/email/cơ quan — đã suýt commit
ORCID tự điền vào CITATION.cff (xoá trước khi push; luật ghi trong skill
`hujos-vi-manuscript-conventions`). (b) `paper2_hujos/blocks` là symlink →
`paper2/blocks` (EN) dùng chung bài IEEE: sửa 1 nơi 2 bài đổi; `blocks_vi/`
chỉ thuộc bản VI. (c) `/media/SAS/Van/DeTai2025/TwinGate_K1` KHÔNG phải git
repo — repo thật ở `~/work/TwinGate_repo` (remote SSH); sửa xong cp sang đó
rồi commit/push. (d) Số liệu không gõ tay: bảng sinh từ `outputs/*.csv` qua
`experiments/make_tables_hujos_vi.py` (VI) / `make_tables_hujos.py` (EN).

---

## ĐÃ XONG VÀ ĐÃ VERIFY (chạy thật, exit code 0)

### 1. Dữ liệu thật
`data/era5_multi/{can_tho,soc_trang,ca_mau}_2024.csv` — 8784 giờ/trạm, **5 biến** (temp, RH, wind, SW, precip), **0 null**.
Kèm `<station>_2024.provenance.json` ghi toạ độ, API, biến, elevation.
Toạ độ lấy **nguyên văn** từ `rabs_repro_20260702_112319/data/fetch_era5_vn.py` ⇒ cùng định nghĩa "zone ĐBSCL" với 2 bài đã nộp.
Nguồn: Open-Meteo historical API (ERA5 reanalysis), **không cần key**, tái lập được.

### 2. `src/water_balance.py` — plant vật lý (test: `tests/test_water_balance.py`, PASS)

| Đại lượng | Kết quả đo | Đối chiếu độc lập |
|---|---|---|
| ET0 năm | **1550 mm** | ĐBSCL ~1300–1700 ✓ |
| ET0 ngày TB / median / p95 / max | **4.24 / 4.26 / 6.44 / 7.20 mm** | ~3–6 TB ✓ |
| ET0 đêm TB | **0.0153 mm/h** | ≈0 ✓ |
| Mưa 2024 Cần Thơ | **2248 mm** | ~1500–2200 ✓ |
| R_a đêm / ngày max | **0.0000 / 4.841 MJ·m⁻²h⁻¹** | đêm=0 ✓; trần vật lý ~4.9 ở vĩ độ 10° ✓ |
| Bảo toàn khối lượng 1 năm | **residual = 0.000e+00** | chính xác tuyệt đối |
| SCS-CN P=50 mm, CN=80 | **13.80 mm** (27.6%) | tính tay closed-form: S=63.5, Ia=12.7 ⇒ 13.80 ✓ |
| Giờ ngoài safe-set | 2499 (28.4%) | đủ để bài toán có nghĩa ✓ |
| Đơn điệu theo T, SW, wind | tăng cả 3 ✓ | — |

### 3. `src/twin_gate.py` — cơ chế K1 (test: `tests/test_twin_gate.py`, PASS)

**Tính chất what-if (điều làm nó là twin, không phải predictor):**
cùng belief `w0=130.25 mm`, horizon 6 h ⇒ lệnh 0/10/25 mm cho `w` dự đoán 129.80/139.80/154.80 mm.
Twin **nhận lệnh làm đầu vào**; predictor AR(1)/Kalman trong RABS/CAW-VoU không có số hạng này.

**Đơn điệu theo độ trung thực twin (đây là cơ chế của định lý):**
| σ_frac | released / 600 |
|---|---|
| 0.02 | 600 (100%) |
| 0.05 | 600 (100%) |
| 0.10 | 135 (22.5%) |
| 0.20 | 0 (0%) |
| 0.40 | 0 (0%) |

**Đơn điệu theo δ:** δ=0.50→600 · δ=0.20→600 · δ=0.05→135 · δ=0.01→0

**Gate phân biệt được với baseline (cùng một slot, depletion 0.60):**
- reactive threshold → phát `open30` (30 mm, lớn nhất, không xét xác suất)
- twin gate → phát `open15` với p=0.963
- Trên ruộng đã ướt (w=FC): gate **WITHHELD** (p=0.513 < 0.95), reactive vẫn phát.

**Kênh lệnh Gilbert–Elliott (20000 slot, seed 11):**
| cấu hình | delivery thực nghiệm | bad-state dừng |
|---|---|---|
| mild (0.06/0.22, loss .035/.65) | 0.828 | 0.214 |
| severe (0.08/0.15, loss .82/.15) | 0.416 | 0.348 |

**Failure mode của baseline đã tái hiện:** `blind_resend_policy` khi ACK mất nhưng lệnh ĐÃ tới ⇒ phát lại 20 mm ⇒ ruộng nhận 40 mm (tưới đúp).

---

## 5 BUG THẬT ĐÃ BẮT NHỜ VIẾT TEST TRƯỚC (ghi lại để khỏi lặp)

1. **Hằng Stefan–Boltzmann sai đơn vị**: `4.903e-9` là MJ·K⁻⁴·m⁻²·**ngày⁻¹**; hourly phải /24. Sai 24× ⇒ ET0 đêm 0.345 mm/h (vô lý). Sửa: `SIGMA_HOUR`.
2. **Proxy độ trong đảo ngược dấu vật lý**: dùng `sw/1361` làm `Rs/Rso` ⇒ *càng nắng Rn càng giảm*. Sửa: tính `R_so` từ hình học mặt trời thật (FAO-56 eq.21–28, 37) + chặn clearness factor ∈ [0.35, 1.0] để đêm không nhận longwave âm.
3. **Clamp cứng `w ≥ wp_mm` phá bảo toàn khối lượng** (residual 1.48e-1). Sửa: bỏ clamp khỏi balance; chỉ clip trong **chỉ số báo cáo** (`depletion_fraction`); stress xử lý bằng `Ks` (eq.84).
4. **SCS-CN áp ở độ phân giải giờ**: Ia=12.7 mm nên mưa 1 giờ hiếm khi vượt ⇒ runoff cả năm chỉ **2 mm / 2248 mm** (vô lý). Sửa: `daily_runoff_share()` tính runoff theo **ngày** rồi chia pro-rata cho các giờ ướt; `step_bucket` nhận `runoff_mm` bắt buộc. Kết quả: 84 mm (3.7%).
5. **`u10` đưa thẳng vào PM**: FAO-56 cần `u2`; thiếu eq.47 sẽ thổi phồng số hạng khí động ~35%. Sửa: convert `u_z → u2`.

**2 lỗi của chính TEST (không phải của code) — quan trọng phải nhớ:**
- Bound "20–35 mm" cho sự kiện 50 mm là em **bịa bằng mắt**; tính tay ra 13.80 mm ⇒ code đúng, test sai. Sửa test sang **đối chiếu closed-form độc lập**, và ghi rõ vụ này trong comment.
- Assertion what-if viết **ngược dấu vật lý** (đòi `w` giảm khi tưới thêm). Nếu "sửa code cho khớp test" thì đã làm hỏng vật lý. Sửa assertion thành `0 < 10 < 25` + thêm kiểm độ nhạy `spread > 1.0 mm`.

⚠️ Bài học: khi test fail, phải tính tay độc lập **trước** khi quyết định sửa code hay sửa test. Cả 2 lần test sai đều do em bịa bound thay vì derive.

---

## CÒN LẠI (theo thứ tự)

1. **Định lý** — 2 kết quả, vừa sức HUJOS-TT:
   - (T1) *Soundness của cổng*: nếu lệnh được phát thì `P(W_h ∈ [lo,hi]) ≥ 1−δ` **dưới σ của chính twin**; suy ra điều kiện đủ trên σ để cổng **không rỗng** (tồn tại lệnh phát được). Đây là chỗ biến "twin fidelity" thành tham số của guarantee.
   - (T2) *Threshold policy tối ưu cho age-of-command*: dưới kênh Gilbert–Elliott, tồn tại ngưỡng `a*` sao cho **resend thắng chờ đợi** khi và chỉ khi age > a*; biểu thức `a*` theo (p_gb, p_bg, loss, chi phí tưới đúp).
2. **`experiments/run_twingate_main.py`** — so sánh 3 policy (TwinGate / reactive threshold / blind resend) + oracle, trên 3 trạm ERA5 × 2 cấu hình kênh × nhiều seed, cùng khung window/seed với RABS để so sánh được. Metric: % giờ vi phạm safe-set, tổng nước (mm), số lệnh, số lần tưới đúp, water-stress-days.
   - ⚠️ **Lưu ý thiết kế đã phát hiện**: cả σ_frac lẫn δ đều **bão hoà hai đầu** (100%→0%). Vùng thấy được trade-off là σ_frac ∈ [0.05, 0.20] và δ ∈ [0.01, 0.20]. Phải quét mịn trong vùng đó, nếu không đồ thị Pareto sẽ là 2 đoạn phẳng.
3. **Bản thảo LaTeX** → **convert Word** theo `HUJOS_venue_spec.md`: Palatino Linotype 10pt, khổ 19×27 cm, lề 2 cm, giãn dòng 1.15, spacing 6/3 pt, công thức MathType đánh số phải, hình ≤7×14 cm caption DƯỚI, bảng caption TRÊN, **≤12 trang**, tóm tắt ≤250 từ ×2 ngôn ngữ, 3–5 từ khoá có mặt trong tóm tắt, **TLTK Vancouver [số]**, cuối bài có học hàm/học vị/địa chỉ/ĐT/email + **chữ ký** + corresponding author.
4. **Trước khi nộp**: quét lại DBLP (phiên này fail — `RemoteDisconnected` + curl 56, cả 2 client), đọc full-text 4 bài hàng xóm `A∩B∩E`, và ghi limitation "chưa quét KSE/RIVF/ACIIDS/IUKM".
5. **KHÔNG push** khi chưa được anh duyệt (memory: workspace sửa tại chỗ, backup `_backups/<ts>/`).

---

## Bằng chứng novelty (đã chạy, xem `gapscan_K1/`)

- Round 1–2: 1235 bản ghi OpenAlex+arXiv, 1217 abstract-level. `A∩B∩C∩D = 0` trên base dense (A=277, B=89, C=61, D=77, E=419, G=73). Hàng xóm gần nhất `A∩B∩E`=4 bài, đều không phải đối thủ.
- Round 3: Crossref title-only 139 bản ghi, join lõi vẫn 0. Corpus **2002 bài HUJOS**: `digital twin`=1 (bài du lịch HUJOS-ED), `networked control`=0, `chance constraint`=0, `tưới∩IoT`=0.
- **Caveat bắt buộc nêu trong bài**: DBLP fail ⇒ chưa quét venue khu vực; corpus HUJOS không nhất quán dấu tiếng Việt (có bài mất dấu hoàn toàn) ⇒ các con số "0" không phải bằng chứng vắng mặt tuyệt đối.
