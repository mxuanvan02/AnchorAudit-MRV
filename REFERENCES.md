# REFERENCES — đã VERIFY (2026-10-03)

Nguyên tắc: **không có mục nào ở đây là em nhớ ra**. Mỗi DOI đã tra trực tiếp qua
`api.crossref.org/works/<doi>` và in lại title/venue/year/vol/issue/page/authors mà Crossref trả về.
Mỗi URL đã gọi HTTP GET thật và ghi status. Mục nào không verify được thì ghi rõ **CHƯA VERIFY**
và không được đưa vào bài.

---

## ⚠️ 0. LỖI CỦA EM TRONG BẢN TRƯỚC — PHẢI THU HỒI

Em đã ghi 4 DOI **bằng cách đoán** (lấy từ text một bài khác trích dẫn lại), và Crossref cho thấy
chúng trỏ sang bài **hoàn toàn khác**:

| Em đã ghi (SAI) | DOI đó thật ra là | DOI ĐÚNG (đã verify) |
|---|---|---|
| Carrijo et al. → `10.1016/j.agwat.2017.03.028` | "Responses of field evapotranspiration to the changes of cropping pattern…" — **Bai, Liangliang** | `10.1016/j.fcr.2016.12.002` |
| Linquist et al. 2018 → `10.1111/gcb.13954` | "Simulating the onset of spring vegetation growth across the Northern Hemisphere" — **Liu, Qiang** | **CHƯA TÌM THẤY** (xem §4) |
| Yan et al. 2005 → `10.1029/2005GB002518` | "Spatial distributions of volatile sulfur compounds in surface seawater" — **Inomata, Yayoi** | `10.1111/j.1365-2486.2005.00976.x` |
| Lampayan et al. 2015 → `10.1016/j.agwat.2014.10.016` | "Treated agro-industrial wastewater irrigation of tomato crop" — **Gatta, Giuseppe** | `10.1016/j.fcr.2014.10.013` |

Đây đúng cái bẫy anh đã ghi trong memory: *"SEARCH TRƯỚC ra link, đoán path SAU"*. Em đã làm ngược.
Bốn mục trên trong `PROBLEM_VN_2026.md` **vô hiệu**, thay bằng danh sách dưới đây.

---

## 1. SÁCH/BÀI HỌC THUẬT — DOI đã verify qua Crossref (18/18 OK)

### 1a. AWD: hiệu quả giảm methane và tiết kiệm nước

**[R1]** Balaine, N.; Carrijo, D. R.; Adviento-Borbe, M. A.; Linquist, B. A. (4 tác giả).
"Greenhouse Gases from Irrigated Rice Systems under Varying Severity of Alternate-Wetting and Drying Irrigation."
*Soil Science Society of America Journal*, **2019**, vol. 83, no. 5, pp. 1533–1541.
DOI: `10.2136/sssaj2019.04.0113` ✅ verified
→ **Đây là nguồn của con số "giảm CH₄ 48–93%" và "giảm nước 23–33"**, vì chính abstract của bài này
trích Linquist et al. 2018, Yan et al. 2005, Qin et al. 2010 và Carrijo et al.
**Dùng R1 làm nguồn trích dẫn là an toàn nhất** (đã verify), thay vì trích 3 bài con chưa verify.

**[R2]** Carrijo, D. R.; Lundy, M. E.; Linquist, B. A. (3 tác giả).
"Rice yields and water use under alternate wetting and drying irrigation: A meta-analysis."
*Field Crops Research*, **2017**, vol. 203, pp. 173–180.
DOI: `10.1016/j.fcr.2016.12.002` ✅ verified
→ Meta-analysis: AWD ảnh hưởng năng suất/nước thế nào.

**[R3]** Yan, X.; Yagi, K.; Akiyama, H.; Akimoto, H. (4 tác giả).
"Statistical analysis of the major variables controlling methane emission from rice fields."
*Global Change Biology*, **2005**, vol. 11, no. 7, pp. 1131–1141.
DOI: `10.1111/j.1365-2486.2005.00976.x` ✅ verified

**[R4]** Enriquez, Y.; Yadav, S.; Evangelista, G. K.; et al. (6 tác giả).
"Disentangling Challenges to Scaling Alternate Wetting and Drying Technology for Rice Cultivation."
*Frontiers in Sustainable Food Systems*, **2021**, vol. 5.
DOI: `10.3389/fsufs.2021.675818` ✅ verified
→ **Rào cản nhân rộng AWD** — dùng cho lập luận "không thiếu kỹ thuật, thiếu cơ chế".

**[R5]** Lampayan, R. M.; Rejesus, R. M.; Singleton, G. R.; Bouman, B. A. M. (4 tác giả).
"Adoption and economics of alternate wetting and drying water management for irrigated lowland rice."
*Field Crops Research*, **2015**, vol. 170, pp. 95–108.
DOI: `10.1016/j.fcr.2014.10.013` ✅ verified
→ Lưu ý: **Bouman là đồng tác giả bài này** ⇒ có thể dùng R5 thay cho sách Bouman 2007 chưa verify.

**[R6]** Sriphirom, P.; Chidthaisong, A.; Yagi, K.; et al. (5 tác giả).
"Evaluation of biochar applications combined with alternate wetting and drying (AWD) water management in rice."
*Soil Science and Plant Nutrition*, **2019**, vol. 66, no. 1, pp. 235–246.
DOI: `10.1080/00380768.2019.1706431` ✅ verified

**[R7]** Echegaray-Cabrera, I.; Cruz-Villacorta, L.; Ramos-Fernández, L.; et al. (6 tác giả).
"Effect of Alternate Wetting and Drying on the Emission of Greenhouse Gases from Rice Fields on the Northeastern…"
*Agronomy*, **2024**, vol. 14, no. 2, p. 248.
DOI: `10.3390/agronomy14020248` ✅ verified

**[R8]** Gonçalves, J. M.; Nunes, M.; Ferreira, S.; et al. (10 tác giả).
"Alternate Wetting and Drying in the Center of Portugal: Effects on Water and Rice Productivity and Contributions…"
*Sensors*, **2022**, vol. 22, no. 10, p. 3632.
DOI: `10.3390/s22103632` ✅ verified

**[R9]** Xuan, T. D.; Minh, T. T. N.; Rayee, R.; et al. (5 tác giả).
"Advances in mitigating methane emissions from rice cultivation: past, present, and future strategies."
*Environmental Science and Pollution Research*, **2025**, vol. 32, no. 34, pp. 20232–20247.
DOI: `10.1007/s11356-025-36776-8` ✅ verified
→ Review mới nhất; **tác giả đầu là người Việt** — thuận lợi khi nộp tạp chí trong nước.

### 1b. Đo lường / cảm biến / viễn thám cho AWD

**[R10]** Dela Cruz, K. M. S.; Ella, V. B.; Suministrado, D. C.; et al. (5 tác giả).
"A Low-Cost Wireless Sensor for Real-Time Monitoring of Water Level in Lowland Rice Field under Alternate Wetting and Drying."
*Water*, **2022**, vol. 14, no. 24, p. 4128.
DOI: `10.3390/w14244128` ✅ verified
→ **Đối thủ gần nhất về phần cứng.** Phải đọc toàn văn và phân biệt rõ: bài này làm cảm biến,
không làm *bound bất định cho bản ghi khi mạng mất gói*.

**[R11]** Islam, M. R.; Oyoshi, K.; Takeuchi, W. (3 tác giả).
"Alternate Wetting and Drying Irrigated Rice Paddy Field Water Status Monitoring with ALOS-2 Three-Component…"
*Remote Sensing*, **2026**, vol. 18, no. 8, p. 1183.
DOI: `10.3390/rs18081183` ✅ verified
→ **Đối thủ gần nhất về viễn thám**, và là bài khớp `B∩C∩D` (MRV+rice+AWD) duy nhất. Mới 2026.

**[R12]** Bwire, D.; Saito, H.; Sidle, R. C.; et al. (4 tác giả).
"Water Management and Hydrological Characteristics of Paddy-Rice Fields under Alternate Wetting and Drying."
*Agronomy*, **2024**, vol. 14, no. 7, p. 1421.
DOI: `10.3390/agronomy14071421` ✅ verified

**[R13]** Lovell, R. J. (1 tác giả).
"Identifying Alternative Wetting and Drying (AWD) Adoption in the Vietnamese Mekong River Delta."
*ISPRS International Journal of Geo-Information*, **2019**, vol. 8, no. 7, p. 312.
DOI: `10.3390/ijgi8070312` ✅ verified qua Crossref
⚠️ Trang mdpi.com trả **HTTP 403** cho cả URL thường lẫn `doi.org` (chặn bot). DOI hợp lệ;
nếu cần toàn văn phải tải qua trình duyệt hoặc qua `blocked-page-recovery`.
→ Abstract nói rõ: *"it is very difficult to determine adoption without deploying thousands of costly household surveys"*
⇒ bằng chứng cho nút thắt chi phí giám sát.

**[R14]** (preprint) "Machine Learning for Sustainable Rice Production: Region-Scale Monitoring of Water-Saving Practices."
arXiv: **2507.08605**, submitted **2025-07-11**. ✅ verified qua arXiv API (không phải Crossref —
Crossref trả null cho DOI arXiv `10.48550/…` vì chúng đăng ký ở DataCite; null ở đó KHÔNG có nghĩa DOI bịa).
→ Nghiên cứu Punjab, Ấn Độ; số liệu nền: lúa dùng **24–30% nước ngọt toàn cầu**; DSR/AWD giảm nước **20–40%**.

### 1b2. Kênh mất gói + ngưỡng mặn (verify bổ sung 03/10/2026, Crossref query.bibliographic)

**[R20]** Gilbert, E. N. "Capacity of a Burst-Noise Channel."
*Bell System Technical Journal*, **1960**, vol. 39. DOI: `10.1002/j.1538-7305.1960.tb03959.x` ✅ verified qua Crossref

**[R21]** Elliott, E. O. "Estimates of Error Rates for Codes on Burst-Noise Channels."
*Bell System Technical Journal*, **1963**, vol. 42. DOI: `10.1002/j.1538-7305.1963.tb00955.x` ✅ verified qua Crossref

**[R22]** Maas, E. V.; Hoffman, G. J. "Crop Salt Tolerance—Current Assessment."
*Journal of the Irrigation and Drainage Division*, **1977**, vol. 103, no. 2. DOI: `10.1061/jrcea4.0001137` ✅ verified qua Crossref

**[R23]** Grattan, S. R. et al. "Rice grain yield under saline conditions" (trong ars.usda.gov P1837.pdf, đo thực địa Sacramento → ngưỡng 1.9 dS/m).
⚠️ Crossref query.bibliographic **KHÔNG tìm ra DOI** cho bài này (nhiều khả năng là chương báo cáo USDA, không DOI). Trích dưới dạng tài liệu USDA P1837.pdf + URL; KHÔNG bịa DOI.

**[R24]** Allen, R. G. et al. *Crop Evapotranspiration — Guidelines for Computing Crop Water Requirements*, FAO Irrigation & Drainage Paper 56, **1998**.
⚠️ Sách FAO — **không có DOI riêng** (Crossref chỉ ra bài review trích dẫn nó). Trích dạng sách + ISBN/URL FAO.

**[R25]** USDA "Crop salt tolerance — current assessment" (P572.pdf) — nguồn cho tranh cãi mẫn cảm mặn theo giai đoạn (mạ nhạy nhất; trổ còn tranh cãi Pearson & Bernstein vs Kaddah). Trích dạng tài liệu USDA + URL.

### 1c. Đồng bằng sông Cửu Long: sụt lún

**[R15]** Minderhoud, P. S. J.; Erkens, G.; Pham, V. H.; Bui, V. T.; Erban, L.; Kooi, H.; Stouthamer, E. (7 tác giả).
"Impacts of 25 years of groundwater extraction on subsidence in the Mekong delta, Vietnam."
*Environmental Research Letters*, **2017**, vol. 12, no. 6, p. 064006.
Published **1 June 2017**. DOI: `10.1088/1748-9326/aa7146` ✅ verified
→ Abstract (đã đọc toàn văn qua web_extract, HTTP 200): *"the delta sank on average ~18 cm as a consequence of
groundwater withdrawal"*; *"Current average subsidence rates … amount to 1.1 cm yr⁻¹, with areas subsiding
over 2.5 cm yr⁻¹, outpacing global sea level rise almost by an order of magnitude"*; phần lớn đồng bằng *"<2 m above sea level"*.

**[R16]** Erban, L. E.; Gorelick, S. M.; Zebker, H. A. (3 tác giả).
"Groundwater extraction, land subsidence, and sea-level rise in the Mekong Delta, Vietnam."
*Environmental Research Letters*, **2014**, vol. 9, no. 8, p. 084010.
DOI: `10.1088/1748-9326/9/8/084010` ✅ verified

### 1d. Digital twin ∩ carbon/MRV — hàng xóm gần nhất (đều KHÔNG phải lúa)

**[R17]** Sasaki, N.; et al. (2 tác giả).
"A Digital Twin Architecture for Forest Restoration: Integrating AI, IoT, and Blockchain for Smart Ecosystem…"
*Future Internet*, **2025**, vol. 17, no. 9, p. 421.
DOI: `10.3390/fi17090421` ✅ verified

**[R18]** Islam, F. A. Samiul (1 tác giả).
"Artificial Intelligence-powered Carbon Market Intelligence and Blockchain-enabled Governance for Climate-…"
*Journal of Engineering Research and Reports*, **2025**, vol. 27, no. 7, pp. 440–472.
DOI: `10.9734/jerr/2025/v27i71585` ✅ verified

**[R19]** Narayanan, M.; et al. (3 tác giả).
"Mapping Indian Rice Yields Using Self-Supervised Digital Twins Reveals Unseen Links to Top-Down Methane Emissions."
*SSRN Electronic Journal*, **2024**. DOI: `10.2139/ssrn.5039208` ✅ verified, cites = 0
→ Bài duy nhất nối digital twin với lúa **và** methane, nhưng mục tiêu là **năng suất**, không phải MRV.
Đây là bài phải trích và phân biệt kỹ nhất.

---

## 2. VĂN BẢN CHÍNH SÁCH / NGUỒN CHÍNH THỐNG VIỆT NAM

| # | Văn bản / bài | Ngày | URL | HTTP |
|---|---|---|---|---|
| [P1] | **QĐ 1490/QĐ-TTg** — "Phát triển bền vững một triệu héc-ta chuyên canh lúa chất lượng cao và phát thải thấp gắn với tăng trưởng xanh vùng ĐBSCL đến năm 2030" | **27/11/2023** | `vanban.chinhphu.vn/?docid=209054&pageid=27160` | **200** ✅ |
| [P2] | Bộ NN&MT — "More than 350,000 hectares of low-emission rice cultivated in Viet Nam" | hiển thị **06/03/2026** | `en.mae.gov.vn/Pages/chi-tiet-tin-Eng.aspx?ItemID=9192` | **200** ✅ |
| [P3] | **QĐ 4801/2025/QĐ-BNNMT** — thí điểm hệ thống MRV cho vùng lúa của đề án | ngày chính xác **chưa xác minh** | được nêu trong [P2] | ⚠️ chưa đọc toàn văn |
| [P4] | **Verra VM0051 v1.1** "Improved Management in Rice Production Systems" | **Active Since 14 July 2026** | `verra.org/methodologies/vm0051-improved-management-in-rice-production-systems-v1-1/` | **200** ✅ |
| [P5] | Bộ NN&MT — "Vietnam's rice cultivation project generates carbon credits under Verra Standard" (Green Carbon, AWD An Giang, đăng ký **01/04/2025**, methodology VM0051) | **10/06/2025** | `en.mae.gov.vn/Pages/chi-tiet-tin-Eng.aspx?ItemID=8918` | **200** ✅ |
| [P6] | **Nghị quyết 57-NQ/TW** — đột phá phát triển KHCN, ĐMST và chuyển đổi số quốc gia | **22/12/2024** | `dangcongsan.org.vn/tuyenquang/nghi-quyet-57-nq-tw` | **200** ✅ (nhưng chỉ 177 bytes — trang ngắn/redirect, **chưa phải toàn văn**) |
| [P7] | MARD — "Xâm nhập mặn mùa khô năm 2025-2026 dự báo tương đương năm 2024-2025" | trang còn cập nhật tin đến **17/07/2026** | `phongchongthientai.mard.gov.vn/Pages/xam-nhap-man-mua-kho-nam-2025--2026-du-bao-tuong-duong-nam-2024--2025.aspx` | **200** ✅ |
| [P8] | Báo NN&MT — "Part 2: Alternate wetting and drying (AWD) — a key pathway to low-emission rice production in Viet Nam" | không ghi rõ | `english.nnmt.net.vn/part-2-alternate-wetting-and-drying-awd-a-key-pathway-to-low-emission-rice-production-in-vietnam` | **200** ✅ |
| [P9] | vietnam.vn — "Applying the MRV process to 300,000 hectares of high-quality rice" (hội nghị **17/11**, Bộ NN&MT + UBND Cần Thơ + IRRI) | không ghi rõ | `vietnam.vn/en/ap-dung-quy-trinh-mrv-cho-300-000ha-lua-chat-luong-cao` | **200** ✅ |
| [P10] | Báo NN&MT — "Towards 'One smartphone per household, one digital account per farm'" (mục tiêu 2030) | **22/09/2025** | `van.nongnghiepmoitruong.vn/towards-one-smartphone-per-household-one-digital-account-per-farm-d774178.html` | **200** ✅ |

### Nguồn IRRI

| # | Bài | Ngày | URL | HTTP |
|---|---|---|---|---|
| [I1] | **Rice Today** — "Why MRV is the missing link for low-emission rice in Southeast Asia" (Tobiah Gonzalez & Glenn Concepcion) | **16/04/2026** | `ricetoday.irri.org/why-mrv-is-the-missing-link-for-low-emission-rice-in-southeast-asia` | **200** ✅ đã đọc toàn văn |
| [I2] | "ASEAN partners, IRRI urge faster transition to low-emission rice" (hội nghị Hà Nội **21–23/01/2026**) | **05/02/2026** | `irri.org/news-and-events/news/asean-partners-irri-urge-faster-transition-low-emission-rice` | **200** ✅ |
| [I3] | "Mekong Delta's Low-Emission Rice Program Surpasses Targets…" (hội nghị **Vị Thanh, 08/03/2026**, Bộ NN&MT chủ trì) | **24/04/2026** | `irri.org/news-and-events/news/mekong-deltas-low-emission-rice-program-surpasses-targets-sets-new-standards` | **200** ✅ (79.608 bytes) |
| [I4] | "Building the evidence for low-emission rice production… REMET-Rice Project" (workshop Los Baños **27/03/2026**) | **24/04/2026** | `irri.org/news-and-events/news/building-evidence-low-emission-rice-production-exploring-findings-over-th` | chưa GET |

⚠️ **URL [I3] trong kết quả search bị CẮT** (`…sets-new-standa`) nên lần GET đầu trả 404. Em đã thử lại
URL đầy đủ `…sets-new-standards` → **HTTP 200**. Bài học: URL từ search snippet có thể bị cắt, phải thử
biến thể trước khi kết luận link chết.

---

## 3. KHUNG THỜI GIAN (timeline) — mọi mốc đều gắn với nguồn ở trên

| Mốc | Sự kiện | Nguồn |
|---|---|---|
| 2005 | Phân tích thống kê biến số kiểm soát phát thải CH₄ ruộng lúa | [R3] |
| 2014 | Phát hiện sụt lún ĐBSCL do khai thác nước ngầm | [R16] |
| 01/06/2017 | Công bố định lượng 25 năm sụt lún: ~18 cm, 1.1 cm/năm, có nơi >2.5 cm/năm | [R15] |
| 2019 | Xác định mức độ áp dụng AWD ở ĐBSCL bằng viễn thám; nêu khó "hàng nghìn khảo sát hộ tốn kém" | [R13] |
| 2021 | Phân tích rào cản nhân rộng AWD | [R4] |
| 2022 | Cảm biến không dây giá rẻ đo mực nước ruộng AWD | [R10] |
| **27/11/2023** | **QĐ 1490/QĐ-TTg** phê duyệt đề án 1 triệu ha lúa CLC phát thải thấp | [P1] |
| **22/12/2024** | **Nghị quyết 57-NQ/TW** về đột phá KHCN, ĐMST, chuyển đổi số quốc gia | [P6] |
| **01/04/2025** | Green Carbon đăng ký dự án "AWD rice cultivation, An Giang" theo **VM0051** | [P5] |
| 2025 | **Thí điểm MRV ở 11 mô hình**; ban hành **QĐ 4801/2025/QĐ-BNNMT** | [P2][P3] |
| 22/09/2025 | Mục tiêu 2030 "một smartphone/hộ, một tài khoản số/nông trại" | [P10] |
| **14/11/2025** | **QĐ 4815/QĐ-BNNMT** công bố Kịch bản nguồn nước lưu vực sông Cửu Long mùa cạn 2025–2026 | ⚠️ chỉ từ snippet, trang nguồn GET fail |
| Mùa khô 2024–2025 | Xâm nhập mặn **cao điểm tháng 2–4/2025**, 3 đợt tăng cao, mạnh nhất nửa cuối tháng 3 | [P7] |
| **Cuối 2025** | Diện tích lúa đề án đạt **>354.000 ha** (gần gấp đôi mục tiêu 180.000 ha); giảm **3–4 t CO₂tđ/ha**; nông dân **+13.4%** thu nhập; >5.000 ha nhãn "gạo xanh" | [P2] |
| 21–23/01/2026 | Hội nghị IRRI–ASEAN tại Hà Nội: kêu gọi chuyển nhanh sang lúa phát thải thấp | [I2] |
| 08/03/2026 | Hội nghị cấp cao tại **Vị Thanh** (Bộ NN&MT): chương trình vượt mục tiêu | [I3] |
| 27/03/2026 | Workshop tổng kết **REMET-Rice** (Los Baños) | [I4] |
| **16/04/2026** | **IRRI/Rice Today: MRV là mắt xích thiếu**, chi phí MRV cao cản trở tài chính khí hậu | [I1] |
| **14/07/2026** | **Verra VM0051 v1.1 có hiệu lực** | [P4] |
| **Hôm nay 03/10/2026** | Đang ở giai đoạn mở rộng **thêm 800.000 ha tới 2030** (An Giang ~530k, Đồng Tháp ~190k, Tây Ninh ~140k) | [P2] |

⚠️ **Một điểm lệch cần xác minh:** trang [P2] có metadata `Published: 2024-07-07` nhưng nội dung hiển thị
`08:14 06/03/2026` và nói về số liệu **cuối 2025**. Có thể 2024-07-07 là ngày tạo trang, 06/03/2026 là ngày
cập nhật bài. Trước khi trích phải mở trang xác nhận, hoặc trích cả hai ngày.

---

## 4. CHƯA VERIFY — KHÔNG ĐƯỢC ĐƯA VÀO BÀI cho tới khi tra được

| Mục | Vấn đề | Cách xử lý |
|---|---|---|
| **Bouman, B. A. M. et al. (2007)**, *Rice water management* / khái niệm "safe AWD" 15 cm dưới mặt ruộng | Crossref `query.bibliographic` **không trả về**; là sách/chương IRRI, có thể không có DOI | Hoặc tra ISBN qua thư viện; **hoặc** dùng [R5] (Lampayan 2015, có Bouman đồng tác giả) và [R2] (Carrijo 2017) làm nguồn cho ngưỡng AWD. Con số "15 cm" hiện chỉ được xác nhận **gián tiếp** qua abstract của một bài ScienceDirect (`S0959652620353543`, chưa verify DOI) |
| **Linquist et al. 2018** | DOI em đoán là sai; Crossref search theo title không tìm ra | Trích gián tiếp qua [R1] |
| **Qin et al. 2010** | như trên | Trích gián tiếp qua [R1] |
| **QĐ 4815/QĐ-BNNMT (14/11/2025)** | Chỉ có từ search snippet; trang `sonnmt.cantho.gov.vn` **CRAWL_TIMEOUT** | Phải tải lại hoặc tìm trên vanban.chinhphu.vn |
| ~~**QĐ 4801/2025/QĐ-BNNMT**~~ | ✅ **ĐÃ VERIFY 03/10/2026**: tải toàn văn PDF 37 trang từ mtnongnghiep.com (WPDM link wpdmdl=3255), sha256 `557b9a6d922ff215bf7a502c2db9e948b2f874611d91878d54885b983d3ee035`, lưu `refs/QD4801_2025.pdf` + `.txt`. Số/ngày: **4801/QĐ-BNNMT, 14/11/2025** (khớp chữ ký số trong PDF). Đọc kỹ trong `NOTES_MRV.md` | — |
| ~~**Toàn văn VM0051 v1.1**~~ | ✅ **ĐÃ VERIFY 03/10/2026**: tải PDF 90 trang từ verra.org (`wp-content/uploads/2026/07/VM0051-Improved-Management-in-Rice-Production-Systems-v1.1.pdf`), sha256 `9b9738840824f5919e3a76f8807c68743ae3d64b5d931cda27598f3ab32c64e2`, lưu `refs/VM0051_v1.1.pdf` + `.txt` (232k ký tự). Đã đọc §9.3 Monitoring Plan + Appendix 4 DMRV — đối chiếu trong `NOTES_MRV.md` | — |
| **QĐ 1490/QĐ-TTg (27/11/2023) toàn văn** | ✅ PDF signed tải từ datafiles.chinhphu.vn (`1490-ttg.signed.pdf`), sha256 `bf9bed53f05e7752cc0c0cc0c34ebdcbc94911da0217b8ab6dc37f1307a69115`, lưu `refs/QD1490_2023.pdf`. ⚠️ Bản **SCAN ẢNH** (text layer = 184 bytes) → đã OCR 11/11 trang qua vision_fallback → `refs/QD1490_2023_ocr.txt` (mục tiêu: giảm >10% KNK, 200k hộ, MRV cấp tín chỉ, TCAF). Trích nguyên văn điều khoản cần OCR chất lượng cao hơn (marker-pdf) | Nếu trích điều khoản → OCR lại |
| **NQ 57-NQ/TW toàn văn** | `xaydungchinhsach.chinhphu.vn/…` → **404** (URL từ search bị cắt); `dangcongsan.org.vn` chỉ 177 bytes | Tìm URL toàn văn đúng |
| Số đo **mực nước ruộng thật** ở ĐBSCL | Chưa có | Cần để hiệu chuẩn; nếu không có phải nhãn rõ là mô hình tình huống |

---

## 5. Kết quả gap-scan (đã lưu JSON, tái kiểm được offline)

- `gapscan_MRV/scan_mrv.json` — **461 bản ghi** OpenAlex 2015–2026, **0 lỗi API**
- `gapscan_K1/scan_classified_v2.json` — **1235 bản ghi** (round 1–2)
- `gapscan_K1/scan_hujos_final.json` — **2002 bài HUJOS** sau dedupe
- `references_verified.json` — kết quả verify DOI của file này

**Lưu ý về bằng chứng gap-scan:** đó là kết quả **phân loại regex trên abstract**, không phải đọc toàn văn.
Các DOI liệt kê ở §1d ([R17][R18][R19]) và §1b ([R10][R11][R13]) là những bài **bắt buộc đọc toàn văn**
trước khi viết claim novelty — skill `literature-gap-recon` ghi rõ *"expect one intended claim to die there"*.
