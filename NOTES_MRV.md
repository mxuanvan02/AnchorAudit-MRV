# NOTES_MRV — ĐỐI CHIẾU TwinGate VỚI CHUẨN MRV (VM0051 v1.1, QĐ 4801/2025, QĐ 1490/2023)

Ngày đọc: 2026-10-03. Trạng thái việc 6 của CHECKPOINT.
Mọi trích dẫn dưới đây đối chiếu với bản PDF/txt trong `refs/`:
- `refs/VM0051_v1.1.pdf` (90 trang, sha256 `9b97388408…`, tải từ verra.org 14/07/2026) → `VM0051_v1.1.txt`
- `refs/QD4801_2025.pdf` (37 trang, sha256 `557b9a6d92…`) → `QD4801_2025.txt` (toàn văn text, đọc được trực tiếp)
- `refs/QD1490_2023.pdf` (11 trang, sha256 `bf9bed53f0…`, BẢN SCAN ẢNH) → `QD1490_2023_ocr.txt` (OCR qua vision_fallback, đang hoàn tất)

---

## 1. VM0051 v1.1 (Verra, hiệu lực 14/07/2026, ICVCM CCP approved, CORSIA approved 16/04/2026)

**Phạm vi:** dự án "improved water and crop management practices in flooded rice systems" giảm phát thải CH4, N2O, CO2. Thay thế CDM AMS-III.AU (Verra ngưng hoạt động 3/2023). v1.0 sẽ bị vô hiệu 01/08/2027 ⇒ dự án mới phải dùng v1.1.

**Các điểm khớp với TwinGate (đọc từ toàn văn):**

| Điểm trong VM0051 | Chỗ khớp của TwinGate | Mức độ |
|---|---|---|
| §9.3 Monitoring Plan: tham số phải được theo dõi **liên tục cả năm**; khuyến nghị dùng **DMRV** (Appendix 4) để validation/verification hiệu quả | Vòng NCS sinh ra **audit trail số theo epoch** (lệnh, thời điểm, độ sâu, delivered/withheld, lý do gate) — chính là "digital record of cultivation practices" mà §5.2 (dòng ~628) chấp nhận: "digital technologies may be used to present information to a farmer and digitally record their acceptance" | **Mạnh** |
| §9.3: "the principle of **conservativeness** must be applied" khi chọn giá trị tham số | I7 đo được σ **bảo thủ** (coverage 0.99–1.00 > 0.95) — trùng hướng với nguyên tắc bảo thủ MRV. Limitation của em (σ inflate ⇒ withhold nhiều hơn) lại LÀ tính chất MRV muốn | Mạnh, và đổi cách kể limitation |
| Appendix 4 (DMRV guidance): RS phát hiện **irrigation events** với tần suất ảnh 2–4 ngày quanh kỳ tưới vì "farmers typically dry their fields for 4–5 days"; radar đo ẩm đất xuyên tán | TwinGate quyết định ở epoch 24h — **độ phân giải thời gian cao hơn** ảnh vệ tinh 2–4 ngày; có thể là ground-truth cho hiệu chỉnh RS | Trung bình (bổ trợ) |
| "A **dynamic baseline** setting approach that accounts for potential impacts due to **actual weather conditions**" (Key Features, v1.0 announcement) | Twin chạy trên ERA5 thật từng giờ, điều kiện theo năm khí hậu (kết quả 2024 vs 2025 của em chứng minh đúng hướng này) | Mạnh |
| Flexible quantification: biogeochemical models; ML/AI trong DMRV | TwinGate là mô hình số (FAO-56 + chance constraint) — họ "decision layer", không phải "emission quantification layer" | **Phải nói rõ giới hạn** |

**GIỚI HẠN PHẢI KHAI BÁO (không được claim quá):** TwinGate **không đo/không lượng hoá CH4-N2O**. Nó là tầng **quyết định điều khiển nước** sinh ra dữ liệu hoạt động (activity data) cho MRV, không thay thế mô hình phát thải của VM0051. Câu claim đúng: *"a command-gating digital-twin layer whose audit trail supplies MRV-grade activity data for the water-management practice"* — không phải "an MRV system".

## 2. QĐ 4801/QĐ-BNNMT ngày 14/11/2025 — Quy trình thí điểm MRV lúa CLC-PTT ĐBSCL

Toàn văn đọc được (37 trang). Thí điểm ~16.000 ha năm 2026 (theo mae.gov.vn), 11 mô hình pilot 2025.

**Cấu trúc 6 bước** (Phụ lục 1): Chuẩn bị → Đăng ký → Thiết lập đường cơ sở → Đo đạc → Báo cáo → Thẩm định (bên thứ ba độc lập do Bộ NNMT ủy quyền; kết quả là cơ sở **cấp tín chỉ carbon + báo cáo NDC**).

**Các điểm khớp trực tiếp:**

1. **Bước 4 Đo đạc**: *"Giám sát rút nước trong mùa vụ bằng ảnh chụp và dữ liệu số"* + *"Thu thập các thông tin, dữ liệu canh tác tại thời điểm cuối vụ"* + *"Kiểm tra chéo dữ liệu"* + *"Quản lý và báo cáo mức độ không chắc chắn trong dữ liệu MRV"*.
   ⇒ Nhật ký lệnh của TwinGate (thời điểm mở cống, độ sâu, withheld + lý do) chính là "dữ liệu số" giám sát chế độ nước **theo giờ**, thay cho ảnh chụp thủ công. Đây là hook cụ thể nhất của bài báo.

2. **Quy tắc AWD 3 ngày** (dòng 399–400): *"Phương pháp rút nước giữa mùa hoặc AWD chỉ được coi là hiệu quả nếu sau ngày rút nước, cánh đồng không được tưới lại trong ít nhất 3 ngày."*
   ⇒ Một ràng buộc **hard-constraint có thể thêm vào gate** (không phát lệnh tưới trong 72h sau lần rút nước) — candidate feature cho bản mở rộng, hoặc ít nhất là thảo luận "gate hiện tại chưa mã hoá quy tắc này".

3. **Bảng A12.1 (Phụ lục 3): hệ số chế độ nước SFw theo IPCC 2019**: CF 0,73–1,27; MSD 0,53–0,94; **AWD 0,41–0,72** (phân phối PERT). Chế độ nước cơ sở được phân loại: Ngập liên tục (CF) / MSD / AWD (dòng 534–541).
   ⇒ Phân loại chế độ nước của một thửa ruộng theo mùa vụ có thể **suy ra tự động từ audit trail** của TwinGate (chuỗi withheld/released theo epoch), thay vì hỏi nông dân + kiểm tra đột xuất (dòng 649–653: thứ tự ưu tiên bằng chứng "hồ sơ tưới tiêu & rút nước thực tế > kế hoạch > lịch trình > ghi chú thực địa > tuyên bố"). **Audit trail của gate là bằng chứng bậc 1 trong đúng thứ tự ưu tiên đó.**

4. **Monte Carlo & bất định (Phụ lục A12, mục 2.1)**: biên độ sai số tính ở **khoảng tin cậy 95%, z = 1,96**: `Margin of error = [(1.96 × σ) ÷ x̄] × 100`; EF đông xuân ±8,9%, hè-thu ±6,2% (dữ liệu IAE).
   ⇒ `Z_CALIB = 1.959963984540054` trong `ncs_loop.py` và invariant I7 (calibration coverage 95%) là **cùng một bộ máy thống kê** mà QĐ 4801 yêu cầu cho QA/QC dữ liệu MRV. Bài báo có thể nói: *"our calibration invariant is the same 95%-interval machinery prescribed by Decision 4801 Appendix A12 for MRV uncertainty reporting"* — đối chiếu số, không claim quá.

5. **QA/QC** (Bước 3+4): kiểm tra nội bộ, kiểm tra đột xuất, tính logic, độ đầy đủ, tính nhất quán, độ không chắc chắn ⇒ invariant suite của em (I1–I7) là bản "QA/QC tự động" của tầng quyết định; nêu tương ứng này là hợp lệ.

6. **SPOT mapping** (Phụ lục 3, Bước 1–4): chia vùng thành SPOT theo đặc trưng; chọn điểm MRV đại diện; 10 tầng sinh thái (Phụ lục A8) ⇒ tương ứng thiết kế 3 trạm × 2 kênh của em (ở mức mô phỏng), và là chỗ phải nói rõ "chưa phải phân tầng SPOT thật".

## 3. QĐ 1490/QĐ-TTg ngày 27/11/2023 — Đề án 1 triệu ha

PDF chính thức là **bản scan** (text layer chỉ có chữ ký số) → đã OCR qua vision_fallback (`QD1490_2023_ocr.txt`, 11 trang). Metadata verify trên vanban.chinhphu.vn: 1490/QĐ-TTg, 27/11/2023, Phó TTg Trần Lưu Quang ký.

**Mục tiêu cụ thể ĐÃ XÁC MINH từ OCR toàn văn (dùng để trích):**
- **Giảm trên 10% lượng phát thải KNK** so với canh tác lúa truyền thống.
- Trên **200.000 hộ** áp dụng quy trình canh tác bền vững; **trên 40% hộ** được tập huấn quy trình ("1 phải 5 giảm", **tưới ngập khô xen kẽ = AWD**, SRP).
- 100% diện tích có liên kết doanh nghiệp–HTX; cơ giới hóa đồng bộ >50%; thất thoát sau thu hoạch <10%; 70% rơm thu gom tái sử dụng.
- Chuỗi giá trị: GTGT +40%, tỷ suất lợi nhuận nông dân >50%; gạo xuất khẩu thương hiệu CLC-PTT >20%.
- **"Xây dựng hệ thống MRV làm cơ sở cấp tín chỉ các-bon"** cho diện tích đã áp dụng quy trình — nguồn lực từ **TCAF (World Bank)**; "hình thành lực lượng cán bộ đo đạc, báo cáo, thẩm định và cấp tín chỉ các-bon".
- ⚠️ OCR KHÔNG thấy mục tiêu "giảm 20% nước tưới" trong phần mục tiêu của QĐ 1490. Con số ~20% nước là **KẾT QUẢ thực hiện** do báo nongnghiepmoitruong.vn (19/06/2026) tường thuật — KHÔNG được trích như mục tiêu của QĐ.
- ⚠️ OCR mức trung bình (~8KB/11 trang, đúng các mục tiêu + nhiệm vụ chính); nếu cần trích điều khoản nguyên văn phải OCR lại bằng marker-pdf/tesseract tiếng Việt.

**Bối cảnh triển khai (nguồn báo chí đã verify, chờ đối chiếu):**
- Bài nongnghiepmoitruong.vn 19/06/2026 (đã trích): sau 2 năm, diện tích đạt **gần 400.000 ha** (gấp đôi mục tiêu 180.000 ha); giống CLC 100% diện tích; giống gieo sạ giảm 30–50%; phân đạm giảm ~30%; thuốc BVTV giảm 2–3 lần; **lượng nước tưới giảm ~20%**; 500 lớp tập huấn / 23.000 nông dân.
- **"Khoảng trống lớn hiện nay là nhiều địa phương đã triển khai sản xuất giảm phát thải nhưng chưa có đủ điều kiện để CHỨNG MINH kết quả"**; Thứ trưởng Hoàng Trung: 2 cấu phần quan trọng nhất giai đoạn tới = **quy trình canh tác + quy trình MRV**; "không chỉ giảm phát thải mà phải chứng minh được đã giảm bao nhiêu".
- **"Quyết định 1490/2023/QĐ-TTg hiện hành chưa quy định rõ nhiệm vụ và nguồn lực dành cho hoạt động này (MRV)"** ⇒ Bộ đang trình phương án điều chỉnh kế hoạch 2026–2030 với MRV làm nền tảng.
- Viện trưởng Viện Môi trường Nông nghiệp Mai Văn Trịnh: cần ~10 tổ hợp tiểu vùng sinh thái × loại đất để xác định hệ số phát thải ĐBSCL; một số tỉnh có quy trình MRV hàng nghìn ha nhưng **thiếu kinh phí đo đạc, giám sát, duy trì hệ thống**.

⇒ **Đây chính là "problem-first" của bài báo** (khớp PROBLEM_VN_2026.md): nút thắt không phải kỹ thuật canh tác (đã giảm được nước/phân/thuốc) mà là **bằng chứng số để chứng minh** — đúng chỗ một command-gating digital twin với audit trail bất biến sinh ra giá trị: chi phí biên thấp, dữ liệu bậc 1 theo đúng thứ tự ưu tiên bằng chứng của QĐ 4801.

## 4. KẾT LUẬN CHO BẢN THẢO (việc 7)

**Được phép claim (có số đối chiếu):**
1. Audit trail của gate cung cấp activity data chế độ nước ở độ phân giải giờ, là bằng chứng bậc cao nhất trong thứ tự ưu tiên của QĐ 4801 (hồ sơ tưới/rút thực tế).
2. Invariant I7 (coverage 95%, z=1,96) dùng đúng bộ máy bất định mà Phụ lục A12 QĐ 4801 quy định cho MRV; σ bảo thủ trùng nguyên tắc conservativeness của VM0051 §9.3.
3. Twin điều kiện theo thời tiết thật (ERA5) khớp "dynamic baseline accounting for actual weather" của VM0051.
4. Hệ quả σ* + C2 mặn cho thấy WITHHELD là hành động tối ưu khi thông tin/nguồn nước không bảo đảm — khớp thực tế vận hành "chờ con nước" mà MRV thủ công không ghi nhận được.

**KHÔNG được claim (giới hạn trung thực):**
- KHÔNG phải hệ thống MRV hoàn chỉnh: không lượng hoá CH4/N2O, không có EF Việt Nam theo vụ (IAE), không thay thế thẩm định bên thứ ba.
- Chưa mã hoá quy tắc AWD-3-ngày của QĐ 4801 (nêu ở Future work hoặc làm tiếp nếu kịp).
- C2 mặn là scenario, không dùng cho claim tuân thủ MRV.
- Phân tầng SPOT/sinh thái thật chưa làm (3 trạm mô phỏng ≠ 10 tổ hợp tiểu vùng × đất).

**Cấu trúc đề xuất cho mục "Relevance to MRV practice"** (1 đoạn ~150 từ trong Discussion, không phải section riêng): nêu 4 claim được phép + 1 câu giới hạn. Trích dẫn: VM0051 v1.1 (Verra 2026), QĐ 4801/QĐ-BNNMT (2025), QĐ 1490/QĐ-TTg (2023), IPCC 2019 Refinement Vol.4 (qua QĐ 4801), và bài báo nongnghiepmoitruong.vn (19/06/2026) cho số liệu triển khai.

## 5. VIỆC CÒN LẠI CỦA MỤC 6

- [ ] Khi OCR QĐ 1490 xong: đối chiếu 6 mục tiêu cụ thể (giảm nước 20%? giảm phát thải 10%?) và trích đúng điều khoản thay vì qua báo.
- [ ] Đưa 3 văn bản vào `REFERENCES.md` (kèm sha256 + ngày tải — đã ghi ở đầu file này).
- [ ] Không đưa gì từ file này vào Abstract; chỉ dùng cho Discussion + Problem statement.
