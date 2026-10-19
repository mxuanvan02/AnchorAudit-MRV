# ĐỀ CƯƠNG (viết lại theo hướng VẤN ĐỀ TRƯỚC) — 2026-10-03

Anh Văn chỉnh hướng đúng: *phải xác định vấn đề và khoảng trống của nông nghiệp Việt Nam
tại thời điểm hiện nay cho chuẩn, rồi mới đi sâu vào hệ thống điều khiển qua mạng để giải quyết.*
File này thay thế phần "vấn đề" của `PROPOSAL.md`. Toàn bộ số liệu dưới đây có **ngày tháng và
nguồn tra được**, tra ngày 2026-10-03.

⚠️ **Sửa lỗi của chính em:** em đã thiết kế trên dữ liệu ERA5 **2024** trong khi hôm nay là
**03/10/2026** — mùa khô 2025-2026 đã kết thúc. Phải cập nhật dữ liệu (mục 6).

---

## 1. VẤN ĐỀ: Việt Nam đang ở giữa một chương trình quốc gia có tiền, nhưng thiếu đúng một mắt xích

### 1a. Chương trình và tiến độ (nguồn: Bộ NN&MT, en.mae.gov.vn, 06/03/2026)

- **QĐ 1490/QĐ-TTg** (27/11/2023): "Phát triển bền vững **một triệu héc-ta** chuyên canh lúa
  chất lượng cao và phát thải thấp gắn với tăng trưởng xanh vùng ĐBSCL đến năm 2030".
- Mục tiêu giai đoạn 2024–2025: ~180.000 ha (phần lớn kế thừa từ VnSAT).
- **Kết quả cuối 2025: hơn 354.000 ha** — gần gấp đôi mục tiêu.
- Giảm phát thải **3–4 tấn CO₂tđ/ha** so canh tác truyền thống; thu nhập nông dân **+13.4%**.
- Hơn 5.000 ha đã được chứng nhận nhãn "gạo xanh" phát thải thấp; 100% diện tích mô hình
  đảm bảo tưới–tiêu.
- **Giai đoạn tới 2030: mở thêm 800.000 ha.** Sáu địa phương đã đăng ký: An Giang ~530.000 ha,
  Đồng Tháp ~190.000 ha, Tây Ninh ~140.000 ha.
- **MRV được thí điểm ở 11 mô hình trong năm 2025**; Bộ NN&MT ban hành
  **QĐ 4801/2025/QĐ-BNNMT** về thí điểm hệ thống MRV cho vùng lúa của đề án.
  (Nguồn Bộ cũng ghi: hội nghị 17/11 giữa Bộ NN&MT + UBND Cần Thơ + IRRI về
  "triển khai quy trình MRV và quy trình sản xuất lúa chất lượng cao phát thải thấp ở ĐBSCL".)

### 1b. Mắt xích bị thiếu — do chính IRRI nêu, không phải em suy diễn

**IRRI / Rice Today, 16/04/2026** — *"Why MRV is the missing link for low-emission rice in
Southeast Asia"* (Tobiah Gonzalez & Glenn Concepcion):

- Lúa chiếm **~10% phát thải methane toàn cầu**, **hơn 1/3** từ Đông Nam Á.
- Giải pháp kỹ thuật **đã có sẵn** (AWD) — nhưng *"awareness, adoption, and sustained
  scale-up remain limited"*.
- **Nguyên nhân nghẽn là chi phí MRV cao**, làm cản trở việc hút tài chính khí hậu:
  *"Attracting climate finance for rice-based methane mitigation practices in Southeast Asia
  is hampered by high costs of Measurement, Reporting, and Verification (MRV) systems."*
- *"Without functioning MRV systems, emission reductions — no matter how real at the field
  level — cannot be formalised"* thành tài sản có giá trị trên thị trường tài chính.
- IRRI chỉ ra hướng: *"Various digital platforms and technologies offer potential for making
  MRV cost-efficient and more affordable."*
- Nông dân **risk-averse**, có "blueprint" riêng đã kiểm chứng; lợi ích giảm methane
  **không nhìn thấy được ở cấp nông hộ** ⇒ cần động cơ kinh tế rõ ràng.

**IRRI, 05/02/2026** (hội nghị Hà Nội 21–23/1): kêu gọi ASEAN chuyển nhanh hơn sang lúa
phát thải thấp — cần chính sách, cơ chế đầu tư, điều phối vùng.
**IRRI, 24/04/2026**: chương trình lúa phát thải thấp ĐBSCL **vượt mục tiêu**, hội nghị cấp cao
tại **Vị Thanh** ngày 08/03/2026 do Bộ NN&MT chủ trì.

### 1c. Thị trường carbon đã mở thật — và chuẩn vừa đổi

- **Verra VM0051** "Improved Management in Rice Production Systems" **v1.1 có hiệu lực
  từ 14/07/2026** (sửa đổi nhỏ của v1.0), thay thế AMS-III.AU của CDM. Áp dụng cho dự án
  cải thiện quản lý nước và cây trồng trên ruộng ngập để giảm phát thải KNK.
- **Green Carbon đã đăng ký "AWD rice cultivation project in An Giang Province" theo VM0051
  ngày 01/04/2025** (en.mae.gov.vn, 10/06/2025) — tức là **đã có dự án carbon lúa thật ở ĐBSCL**.
- Hệ quả: để phát hành tín chỉ, dự án phải xác định **ranh giới dự án, đường cơ sở, nguồn phát
  thải, phương pháp giám sát, và lượng giảm phát thải định lượng được** (english.nnmt.net.vn,
  Part 2: "Turning emission reductions into credits").

### 1d. Kỹ thuật cốt lõi và yêu cầu đo của nó

- **AWD (ngập–khô xen kẽ)**: rút nước khỏi ruộng định kỳ cho tới khi đất khô đến
  **ngưỡng an toàn, điển hình 15 cm dưới mặt ruộng** ("safe AWD", Bouman et al. 2007),
  rồi tưới lại. Canh tác truyền thống VN giữ lớp nước mặt **5–10 cm suốt vụ**.
- Hiệu quả đã công bố: **giảm CH₄ 48–93%** (Linquist et al. 2018; Yan et al. 2005; Qin et al. 2010),
  **giảm nước 23–33%** (Carrijo et al.) — doi:10.2136/sssaj2019.04.0113.
- **Điểm mấu chốt cho bài toán của ta:** việc tuân thủ AWD được định nghĩa bằng
  **quỹ đạo mực nước theo thời gian**. Muốn có tín chỉ thì phải **chứng minh được mực nước
  đã thật sự xuống dưới ngưỡng vào đúng các giai đoạn**, trên hàng trăm nghìn ha, với nông hộ nhỏ.
  Hiện trường đang đo bằng **ống quan trắc đục lỗ** (perforated observation tubes) — thủ công,
  thưa, không liên tục.

### 1e. Áp lực vật lý làm vấn đề khó hơn (và rất "Việt Nam")

- **Sụt lún:** Minderhoud et al. 2017, *Environ. Res. Lett.* 12 064006
  (doi:10.1088/1748-9326/aa7146) — mô hình 3D toàn đồng bằng: trong 25 năm đồng bằng
  **chìm trung bình ~18 cm**; tốc độ hiện tại **1.1 cm/năm** (best estimate), có nơi
  **> 2.5 cm/năm**, **nhanh hơn mực nước biển dâng gần một bậc độ lớn**. Phần lớn đồng bằng
  **dưới 2 m so với mực nước biển**.
  ⇒ Cao trình mặt ruộng **không cố định**, nên "15 cm dưới mặt ruộng" là ngưỡng **trôi theo thời
  gian** nếu mốc đo gắn với cao trình tuyệt đối. Đây là chi tiết mà một hệ đo từ xa phải xử lý,
  và gần như chưa bài nào nói tới.
- **Xâm nhập mặn:** Bộ NN&MT (phongchongthientai.mard.gov.vn) dự báo mùa khô **2025-2026
  tương đương 2024-2025** và **thấp hơn 2015-2016, 2019-2020**. Mùa khô 2024-2025 mặn
  **tập trung cao điểm tháng 2–4/2025 với 3 đợt tăng cao**, đặc biệt nửa cuối tháng 3.
  ⇒ **Trùng đúng cửa sổ AWD**: rút nước trong lúc nguồn đang mặn là rủi ro thật.
  Cục KTTV: mưa ĐBSCL tháng 1–3/2026 **cao hơn TBNN**, nhiều khả năng **mưa trái mùa**;
  nắng nóng 2026 xuất hiện **muộn hơn** 2024 và **không gay gắt/kéo dài bằng** 2024.
  **QĐ 4815/QĐ-BNNMT (14/11/2025)** công bố Kịch bản nguồn nước lưu vực sông Cửu Long
  mùa cạn 2025–2026. Đồng Tháp đã ra **Chỉ thị 04** về phòng chống hạn mặn năm 2026.
- **Chuyển đổi số nông nghiệp:** mục tiêu 2030 *"một smartphone/hộ, một tài khoản số/nông trại"*
  (van.nongnghiepmoitruong.vn, 22/09/2025). Diễn đàn Hà Nội cảnh báo **hạ tầng yếu và lao động
  nông thôn thiếu kỹ năng số** (vietnamnews.vn). Thủ tướng gắn KHCN/ĐS với mục tiêu
  **xuất khẩu nông sản 100 tỉ USD**. Đã có nền tảng nội địa (MobiAgri của MobiFone) gắn với
  đề án 1 triệu ha. **Nghị quyết 57-NQ/TW (22/12/2024)** về đột phá KHCN, ĐMST và chuyển đổi số
  quốc gia là khung chính sách cấp cao nhất; đã có **hội nghị sơ kết quý III/2025** và
  **Thông báo kết luận 07-TB/CQTTBCĐ (15/10/2025)** nêu "tồn tại, hạn chế, điểm nghẽn".

---

## 2. KHOẢNG TRỐNG

### 2a. Khoảng trống THỰC TIỄN (đây là cái anh yêu cầu tìm cho chuẩn)

| # | Khoảng trống | Bằng chứng |
|---|---|---|
| G1 | **Chi phí MRV là nút thắt** chặn tài chính khí hậu cho lúa phát thải thấp ở ĐNÁ | IRRI/Rice Today 16/04/2026 (nêu đích danh) |
| G2 | **Bằng chứng tuân thủ AWD hiện đo thủ công bằng ống đục lỗ**, thưa và không liên tục, trong khi diện tích cần MRV tăng thêm **800.000 ha** tới 2030 | QĐ 1490 + tiến độ 354.000 ha (Bộ NN&MT 03/2026); thực hành ống quan trắc (Bouman et al. 2007) |
| G3 | **Chưa có cơ chế định lượng độ tin cậy của bản ghi mực nước** khi dữ liệu thưa/mất — mà VM0051 đòi hỏi "phương pháp giám sát" và lượng giảm phát thải **định lượng được** | Verra VM0051 v1.1 hiệu lực 14/07/2026; nnmt Part 2 |
| G4 | **Ngưỡng AWD gắn với cao trình mặt ruộng đang sụt lún 1.1–2.5 cm/năm** ⇒ mốc đo trôi; chưa thấy công trình nào xử lý | Minderhoud et al. 2017 ERL |
| G5 | **Cửa sổ AWD trùng cửa sổ xâm nhập mặn (tháng 2–4)** ⇒ rút nước/tưới lại phải xét chất lượng nguồn, không chỉ mực nước | MARD dự báo mặn 2024-2025 cao điểm 2–4/2025 |
| G6 | **Hạ tầng số nông thôn yếu, nông hộ nhỏ, nông dân risk-averse** ⇒ hệ đo phải rẻ, ít bảo trì, pin sống cả vụ | IRRI 2026; vietnamnews.vn; SEARCA Mekong Farm app |

### 2b. Khoảng trống KHOA HỌC — đã quét bằng API, không phải ký ức

Quét OpenAlex, **461 bản ghi** (2015–2026), **0 lỗi API**, phân rã thành 6 component:

| Component | n | Ghi chú |
|---|---|---|
| A digital twin | **64** | dày |
| B MRV / carbon credit / verified carbon | **22** | dày |
| C rice methane / paddy / low-emission rice | **93** | dày nhất |
| D AWD / water level / irrigation scheduling | **45** | dày |
| E lossy channel / IoT / WSN / LoRa | **77** | dày |
| **F uncertainty bound / probabilistic guarantee / attestation** | **2** | ⚠️ **gần như vắng mặt** |

**Join table:**

| Join | n | Bài gần nhất |
|---|---|---|
| C∩D (rice+AWD) | **23** | dày — AWD là vùng đã nghiên cứu kỹ |
| C∩D∩E (rice+AWD+IoT) | **4** | bắt đầu thưa |
| B∩C (MRV+rice methane) | **3** | ALOS-2 giám sát trạng thái nước ruộng AWD (RS 2026, doi:10.3390/rs18081183); review methane (ESPР 2025); review MRV chăn nuôi |
| B∩C∩D | **2** | chính 2 bài trên |
| A∩B (twin+MRV) | **2** | **phục hồi rừng** (doi:10.3390/fi17090421) và **AI carbon market + blockchain** (doi:10.9734/jerr/2025/v27i71585) — **không bài nào là lúa** |
| A∩C (twin+rice methane) | **4** | biorefinery, rừng ngập mặn, photoacoustics, **Mapping Indian Rice Yields Using Self-Supervised Digital Twins** (SSRN 2024, cites=0) — bài này là twin cho **năng suất**, không phải MRV/phát thải |
| **A∩B∩C** | **0** | ✅ EMPTY |
| **A∩B∩C∩D** | **0** | ✅ EMPTY |
| **A∩B∩C∩D∩E** | **0** | ✅ EMPTY |
| **A∩B∩C∩D∩E∩F** | **0** | ✅ EMPTY |

**Phát hiện sắc nhất: F = 2 trên 461 bản ghi.** Cả vùng văn liệu lúa/AWD/MRV
**gần như không có ai đặt câu hỏi về bound bất định**. Người ta đo, người ta giám sát bằng viễn
thám, người ta bàn chi phí MRV — nhưng **không ai định lượng "bản ghi này đáng tin đến đâu
khi dữ liệu bị mất"**. Đó chính xác là chỗ mà lý thuyết điều khiển qua mạng của anh có thế mạnh,
và là chỗ em đã có sẵn định lý σ\*.

### 2c. Phát biểu khoảng trống (câu sẽ vào bài)

> Giảm phát thải methane từ lúa ở ĐBSCL **không thiếu giải pháp kỹ thuật** (AWD đã được chứng
> minh giảm CH₄ 48–93%) và **không thiếu chính sách** (QĐ 1490, QĐ 4801/2025, VM0051).
> Nút thắt được IRRI nêu đích danh là **chi phí MRV**. Trên khảo sát 461 công trình
> (OpenAlex, 2015–2026, mức abstract), các nhánh bản sao số, MRV/tín chỉ carbon, phát thải
> methane ruộng lúa, quản lý nước AWD, và IoT trên kênh không tin cậy **đều phát triển độc lập
> với mật độ cao**; chúng tôi không tìm thấy công trình nào kết hợp chúng, và đặc biệt
> **chỉ 2/461 công trình đề cập đến bound bất định hay bảo đảm xác suất** cho dữ liệu giám sát.
> Khoảng trống này khiến **chưa có cách nào định lượng độ tin cậy của bản ghi mực nước
> khi mạng cảm biến thưa và mất gói** — đúng thứ mà một hệ thống MRV khả thi về chi phí
> trên 800.000 ha cần.

### 2d. Lỗ hở của chính lần quét này (khai báo, không giấu)

1. Chỉ mới **OpenAlex**; DBLP vẫn fail ở phiên này (`RemoteDisconnected` + curl 56) ⇒ chưa quét
   venue khu vực VN (KSE/RIVF/ACIIDS/IUKM).
2. `web_search` lỗi **6/21 query** (Firecrawl 403 / Exa malformed) ⇒ một số nhánh tiếng Việt
   (chi phí cảm biến mực nước/ha, trạm đo mặn tự động) **chưa tra được** — cần tra lại.
3. Chưa đọc **toàn văn VM0051 v1.1** ⇒ chưa biết chính xác phương pháp giám sát mà Verra chấp
   nhận (đây là việc **bắt buộc** trước khi claim bài toán khớp chuẩn).
4. Chưa đọc toàn văn **QĐ 4801/2025/QĐ-BNNMT** (thí điểm MRV) — cần để biết yêu cầu dữ liệu cụ thể.
5. Chưa đối chiếu Crossref từng DOI theo quy trình `bibtex-reference-audit`.

---

## 3. VÌ SAO ĐIỀU NÀY DẪN ĐẾN HỆ ĐIỀU KHIỂN QUA MẠNG (mắt xích anh yêu cầu)

Chuỗi lập luận, mỗi bước có nguồn:

1. Tín chỉ carbon lúa đòi hỏi **chứng minh quỹ đạo mực nước** đạt ngưỡng AWD (VM0051, G3).
2. Chứng minh trên 800.000 ha nông hộ nhỏ **không thể làm thủ công** bằng ống đục lỗ (G2, G6).
3. Giải pháp tự nhiên là **mạng cảm biến mực nước không dây** giá rẻ.
4. Nhưng mạng đó ở ĐBSCL **chịu đúng các điều kiện mà hệ điều khiển qua mạng nghiên cứu**:
   mất gói burst, pin hạn chế, vùng phủ chập chờn, và **lệnh điều khiển van/cống cũng đi qua
   chính kênh đó** (G6).
5. ⇒ Dữ liệu MRV sinh ra từ một **mạng không tin cậy**. Câu hỏi khoa học thật sự là:
   **"Bản ghi mực nước được tái dựng từ mạng thưa–mất gói có độ tin cậy bao nhiêu, và độ mất
   dữ liệu tối đa nào vẫn cho phép phát hành bằng chứng kiểm định được?"**
6. Đây là câu hỏi **định lượng được bằng công cụ NCS**: bản sao số của cột nước ruộng (cân bằng
   nước FAO-56 + thuỷ lực ruộng) lấp khoảng trống, và **bound bất định của bản ghi** chính là
   thứ quyết định bằng chứng có dùng được cho MRV hay không.
7. **Định lý σ\* em đã derive và verify trở thành kết quả trung tâm, không còn là phụ:**
   nó trả lời *"bản sao số phải trung thực đến mức nào thì bằng chứng mới phát hành được"*,
   và chỉ ra tồn tại vùng mà **không thể phát hành bằng chứng nào** (cổng rỗng) — tức là
   ngưỡng mà dưới đó hệ đo phải bổ sung cảm biến hoặc đo thủ công.

**Vai trò của digital twin ở khung mới còn vững hơn khung cũ**: twin không chỉ trả lời
*"nếu tôi ra lệnh thì sao"* (what-if), mà còn **điền khoảng trống dữ liệu và cấp bound cho chỗ
đã điền** — tức là một **cỗ máy sinh bằng chứng kiểm toán được**. Đổi chữ "twin" thành
"predictor" thì không có bound để kiểm toán ⇒ phép thử thay từ vẫn trượt.

---

## 4. BA CÂU HỎI NGHIÊN CỨU (viết lại)

**RQ1 — Bound bằng chứng.** Với mạng cảm biến mực nước chịu mất gói burst và tái neo thưa,
độ bất định của bản ghi mực nước tái dựng tăng theo tuổi dữ liệu như thế nào, và tồn tại
**ngưỡng mất dữ liệu tối đa** nào để bản ghi vẫn đủ chặt nhằm khẳng định tuân thủ AWD
(mực nước đã xuống dưới ngưỡng 15 cm trong khoảng thời gian yêu cầu) với xác suất ≥ 1−δ?

**RQ2 — Cấp phát đo tối thiểu.** Dưới ràng buộc chi phí (số cảm biến, pin, số lần đo thủ công),
cần **tái neo thật** ở đâu và khi nào để cực tiểu độ bất định của bằng chứng trên toàn vùng?
Đây là bài toán lập lịch mà hai bài RABS/CAW-VoU của anh đã có công cụ — nhưng **hàm mục tiêu
đổi từ "phát hiện vi phạm an toàn" sang "độ chặt của bằng chứng kiểm định"**.

**RQ3 — Ràng buộc kép của ĐBSCL.** Khi cửa sổ AWD trùng cửa sổ xâm nhập mặn (tháng 2–4) và
cao trình mặt ruộng sụt lún 1.1–2.5 cm/năm, ngưỡng tuân thủ trở thành **ngưỡng động**.
Việc đưa hai yếu tố này vào cổng quyết định thay đổi kết luận tuân thủ và lượng giảm phát thải
khai báo được như thế nào?

---

## 5. ĐÓNG GÓNG DỰ KIẾN (khung mới)

1. **Phát biểu bài toán MRV dưới dạng bài toán hệ điều khiển qua mạng** — chưa thấy trong
   văn liệu (A∩B∩C∩D∩E = 0 trên 461 bản ghi).
2. **Bound bất định cho bản ghi mực nước tái dựng**, với ngưỡng σ\* cho biết khi nào
   **không thể phát hành bằng chứng** — lấp đúng chỗ F = 2/461.
3. **Chính sách tái neo tối thiểu** để đạt độ chặt bằng chứng yêu cầu với chi phí thấp nhất
   — trả lời trực tiếp nút thắt "chi phí MRV cao" mà IRRI nêu.
4. **Ngưỡng tuân thủ động** tính đến sụt lún và xâm nhập mặn — đặc thù ĐBSCL, có số đo thật.
5. **Khung mô phỏng tái lập được** trên dữ liệu ERA5 thật + quy trình AWD công bố, không cần
   số liệu thực địa đắt.

---

## 6. VIỆC PHẢI LÀM NGAY (trước khi code tiếp)

| # | Việc | Vì sao bắt buộc | Trạng thái |
|---|---|---|---|
| 1 | **Đọc toàn văn VM0051 v1.1** (verra.org) | Phải biết Verra chấp nhận phương pháp giám sát nào, không thì bài toán có thể lệch chuẩn | ✅ 03/10/2026 — `refs/VM0051_v1.1.pdf` (90tr, sha256 trong REFERENCES.md), đọc §9.3 + Appendix 4 → `NOTES_MRV.md` |
| 2 | **Đọc QĐ 4801/2025/QĐ-BNNMT** (thí điểm MRV) | Yêu cầu dữ liệu cụ thể của Việt Nam | ✅ 03/10/2026 — toàn văn 37 trang `refs/QD4801_2025.pdf`; quy trình 6 bước, quy tắc AWD-3-ngày, Bảng A12.1 (SFw IPCC), Monte Carlo z=1.96 → `NOTES_MRV.md` |
| 3 | **Đọc QĐ 1490/QĐ-TTg toàn văn** (vanban.chinhphu.vn docid=209054) | Số liệu mục tiêu/chỉ tiêu chính xác để trích | ✅ 03/10/2026 — PDF scan → OCR 11/11 trang `refs/QD1490_2023_ocr.txt`; mục tiêu: >10% KNK, 200k hộ, MRV cấp tín chỉ/TCAF. ⚠️ "giảm 20% nước" là kết quả báo chí, KHÔNG phải mục tiêu QĐ |
| 4 | **Cập nhật ERA5 sang 2025 và 2026** | Hôm nay 10/2026; dữ liệu 2024 đã cũ; mùa khô 2025-2026 đã xảy ra | ✅ 2025 DONE (3 trạm, 8760h, 0 null; full grid 2025 EXIT=0). ⚠️ 2026: ERA5 chưa khép năm (mới tới 10/2026) — nếu cần mùa khô 2026 chạy `--year 2026` với window 3–5/2026 đủ dữ liệu |
| 5 | Tra lại các nhánh tiếng Việt bị lỗi backend (chi phí cảm biến mực nước, trạm đo mặn tự động) | 6/21 query fail | ⬜ |
| 6 | Quét lại DBLP khi sống | Chưa loại trừ prior art venue VN | ⬜ |
| 7 | Tìm **số đo mực nước ruộng thật** ở ĐBSCL (luận văn, báo cáo VnSAT, IRRI) để hiệu chuẩn | Nếu không có thì phải nhãn rõ là mô hình tình huống | ⬜ |

**Tài sản đã code và đã test vẫn dùng được** (`src/water_balance.py`, `src/twin_gate.py`,
2 test suite PASS, định lý σ\* đã verify) — nhưng **phải đổi hàm mục tiêu và metric**:
từ "số giờ vi phạm vùng an toàn / lượng nước" sang **"độ chặt của bằng chứng tuân thủ AWD"**
và **"chi phí đo tối thiểu để đạt độ chặt đó"**.

---

## 7. CÂU HỎI CHO ANH

1. **Anh xác nhận khung mới này không?** (MRV/tín chỉ carbon lúa làm vấn đề trung tâm, NCS làm
   công cụ) — nếu có, em viết lại `PROPOSAL.md` theo khung này và dừng hướng cũ.
2. **Anh có tiếp cận được VM0051 toàn văn hoặc QĐ 4801/2025 không?** Nếu không em tải từ
   verra.org / vanban.chinhphu.vn.
3. **Anh có số đo mực nước ruộng thật nào không** (VnSAT, luận văn, trạm thí nghiệm)?
   Có thì bài mạnh hơn nhiều; không thì em nhãn rõ là mô hình tình huống.
4. **Venue:** khung mới này **nông nghiệp hơn** khung cũ ⇒ có nên chuyển sang
   **HUJOS-ARD** (Nông nghiệp & PTNT, ≥15 TLTK, 8–15 trang) thay vì HUJOS-TT?
   Lưu ý em đã đo: khán giả ARD là nhà nông học (30 bài "tưới" đều là nông học thuần,
   `tưới ∩ IoT = 0`) ⇒ nếu nộp ARD phải giảm toán, đẩy chứng minh xuống phụ lục.
