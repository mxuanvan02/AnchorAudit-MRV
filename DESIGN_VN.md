# THIẾT KẾ K1 BẢN VIỆT NAM — dựa trên số ĐO THẬT từ ERA5 2024

Cập nhật 2026-10-03. Mọi con số khí hậu dưới đây **đo trực tiếp** trên
`data/era5_multi/*_2024.csv` (8784 giờ/trạm), không phải ước đoán.

---

## 1. PHÁT HIỆN then chốt: hai mối nguy KHÔNG trùng nhau về không gian lẫn thời gian

### 1a. Sốc nhiệt lúa chỉ xảy ra trong mùa khô — và trùng đỉnh xâm nhập mặn

Ngưỡng có nguồn (xem §5):
- **35.0 °C** — ống phấn bị ức chế mạnh trên ngưỡng này
- **37.2 ± 0.2 °C** — ngưỡng tới hạn cho đậu hạt lúa lúc trổ (PMC10721465)

| Trạm | giờ >35 °C | giờ >37.2 °C | NGÀY Tmax>35 | NGÀY Tmax>37.2 |
|---|---|---|---|---|
| Cần Thơ (10.05°N, nội đồng) | **208** (2.37%) | **37** (0.42%) | 46/366 | **12** |
| Cà Mau (9.18°N, ven biển) | 98 (1.12%) | 7 (0.08%) | 28/366 | 5 |
| Sóc Trăng (9.60°N, ven biển) | 64 (0.73%) | 1 (0.01%) | 21/366 | 1 |

**Phân bố theo tháng (giờ >35 °C) tại Cần Thơ:**
`I:0  II:0  III:28  IV:155  V:25  VI:0  VII:0  VIII:0  IX:0  X:0  XI:0  XII:0`

⇒ **100% số giờ sốc nhiệt rơi vào tháng III–V**, và **0 giờ** trong suốt tháng VI–XII.
Cả 3 trạm đều cùng dạng này (Sóc Trăng: IV=48/64; Cà Mau: IV=73/98).

Mưa: mùa khô (XII–V) chỉ **420 mm = 18.7%** tổng lượng mưa năm; mùa mưa 1828 mm.

### 1b. Đây chính là điểm khoa học — và nó đặc thù Việt Nam

Cửa sổ sốc nhiệt (III–V) **trùng khít** với:
1. **Đỉnh xâm nhập mặn** ĐBSCL (mùa kiệt, dòng thượng nguồn thấp nhất)
2. **Giai đoạn trổ–chín của vụ Đông Xuân** — vụ chính, năng suất cao nhất năm

⇒ Trong cùng một tháng Tư, một lệnh tưới ở ĐBSCL phải đối mặt **đồng thời hai mối nguy**:
- **Nhiệt**: nếu lúa đang trổ mà T > 37.2 °C thì mất hạt **bất thuận nghịch** — tưới lúc này
  là cứu, không tưới là mất trắng.
- **Mặn**: nhưng nước bơm lên lúc triều cao **chính nó là nước mặn**; tưới vào ruộng là
  *chủ động đưa muối vào tầng rễ*. Lúa giảm ~12% năng suất cho mỗi 1 dS/m vượt ngưỡng
  (ngưỡng 1.9–3.0 dS/m).

**Một cổng an toàn chỉ xét cân bằng nước sẽ ra quyết định SAI theo hướng nguy hiểm**:
nó thấy ruộng khô + sắp sốc nhiệt ⇒ phát lệnh tưới ⇒ bơm nước mặn vào ruộng đúng lúc
lúa trổ. Đây là lỗi thật ngoài đồng, không phải lỗi mô hình.

### 1c. Cấu trúc KHÔNG GIAN: hai mối nguy **ngược chiều nhau** giữa các trạm

Cần Thơ (nội đồng) có **3.25×** số giờ sốc nhiệt của Sóc Trăng (ven biển) — đúng với hiệu ứng
điều hoà của biển. Nhưng xâm nhập mặn thì **ngược lại**: càng ven biển càng nặng.

⇒ Một gateway quản nhiều vùng phải đối mặt bài toán **phân bổ không gian** mà *cửa sổ lệnh
an toàn khác nhau theo vùng*: vùng nội đồng cần canh thời điểm theo **nhiệt**, vùng ven biển
cần canh theo **triều/mặn**. Cấu trúc này không có trong bất kỳ bài DT-sync/AoI nào
(chúng giả định các arm đồng chất về loại rủi ro).

---

## 2. Cơ chế mới: TwinGate-VN — cổng an toàn BA ràng buộc ghép, có QUYẾT ĐỊNH THỜI ĐIỂM

Đây là chỗ nâng hàm lượng khoa học so với bản K1 chung chung:

**Không gian hành động mở rộng từ `magnitude` sang `(magnitude, timing)`.**
Ở ĐBSCL nguồn nước ngọt chỉ có trong một phần của chu kỳ triều (bán nhật, ~12.4 h).
Vậy câu hỏi của gateway không phải chỉ "tưới bao nhiêu" mà là
**"mở cống vào giờ nào trong chu kỳ triều"**.

Cổng phát lệnh `u = (mm, τ)` chỉ khi **cả ba** điều kiện sau đạt xác suất ≥ 1−δ
dưới độ bất định của chính twin:

| # | Ràng buộc | Đại lượng | Nguồn tham số |
|---|---|---|---|
| C1 | **Cân bằng nước** — ruộng có thật sự cần nước không, và sau lệnh có ra khỏi safe set không | `W_H ∈ [w_lo, w_hi]` | FAO-56 (đã code, đã test) |
| C2 | **Chất lượng nguồn** — nước định bơm có đủ ngọt không tại thời điểm mở cống | `EC_src(τ) ≤ EC_crit(giai đoạn)` | mô hình triều + bao xâm nhập mặn theo mùa (§3) |
| C3 | **Rủi ro nhiệt bất thuận nghịch** — nếu lúa đang ở cửa sổ trổ thì sốc nhiệt sắp tới có vượt ngưỡng không | `T_max trong H ≤ T_crit(stage)` | ERA5 đo được thật; `T_crit` = 35.0 / 37.2 °C có nguồn |

**Điểm khiến đây là twin chứ không phải predictor:** C2 và C3 là câu hỏi *phản thực có điều
kiện vào lệnh* — "nếu mở cống lúc τ với lượng mm thì EC tầng rễ sau H giờ là bao nhiêu, và
nhiệt có kịp hạ không". Predictor AR(1)/Kalman của RABS/CAW-VoU **không có số hạng `u`**
nên không trả lời được. Đã verify tính chất này: cùng belief 130.25 mm, lệnh 0/10/25 mm →
129.80/139.80/154.80 mm.

**WITHHELD là hành động tối ưu, không phải thất bại.** Định lý σ\* (THEORY.md) cho thấy khi
`σ_H ≥ W/(2·z_{1−δ/2})` thì cổng **rỗng với mọi tập lệnh**. Bản Việt Nam còn một lý do withhold
mạnh hơn và rất thực tế: **không có giờ nào trong chu kỳ triều mà nguồn đủ ngọt** ⇒ đúng đắn
là *không tưới và chờ*, thay vì bơm mặn. Ngoài đồng đây gọi là "chờ con nước".

---

## 3. Cái gì là ĐO ĐƯỢC, cái gì là MÔ HÌNH — phân biệt rạch ròi (chống bịa số)

| Thành phần | Trạng thái | Ghi chú trung thực |
|---|---|---|
| Nhiệt độ giờ, mưa, bức xạ, ẩm, gió | ✅ **ĐO/PHÂN TÍCH THẬT** (ERA5) | 8784 giờ × 3 trạm × 5 biến, 0 null, có provenance |
| ET0, cân bằng nước tầng rễ, Ks, runoff | ✅ **Công thức chuẩn FAO-56/SCS-CN** | đã verify: ET0 năm 1550 mm (văn liệu 1300–1700), mưa 2248 mm (1500–2200), bảo toàn khối lượng residual = 0 |
| Số giờ/ngày sốc nhiệt, phân bố theo tháng | ✅ **ĐO từ ERA5** | §1a — đây là số thật, không mô hình |
| Pha triều (bán nhật) | ✅ **Tính được tất định** từ công thức thiên văn | không cần API, tái lập được |
| **Nồng độ mặn nguồn theo giờ** | ⚠️ **MÔ HÌNH TÌNH HUỐNG** | Em **KHÔNG có** số đo mặn 2024 tại 3 trạm. Phải ghi rõ trong bài là scenario model, và **quét độ nhạy** trên biên độ xâm nhập thay vì khẳng định một giá trị |
| `T_crit` theo giai đoạn (35.0/37.2 °C) | ✅ **Có nguồn công bố** | §5 |
| Ngưỡng mặn lúa (1.9–3.0 dS/m, −12%/dS·m⁻¹) | ✅ **Có nguồn công bố** | §5 |
| Giai đoạn sinh trưởng (GDD) | ⚠️ tính từ ERA5 + lịch thời vụ công khai | cần ghi nguồn lịch thời vụ |

**Quy tắc em tự ràng buộc:** bất kỳ con số nào không đo được và không có nguồn công bố
thì phải (a) khai báo là tham số tình huống, (b) quét độ nhạy, (c) không xuất hiện trong
Abstract như một kết quả. Vi phạm điều này là vi phạm nguyên tắc "không bịa số" của anh.

---

## 4. Vì sao thiết kế này CÓ TÍNH MỚI (đối chiếu gap-scan đã chạy)

| Trục | Toàn bộ nhánh AoI/DT-sync | RABS (của anh) | CAW-VoU (của anh) | **TwinGate-VN** |
|---|---|---|---|---|
| Tài nguyên khan hiếm | gói dữ liệu uplink | ngân sách polling `B_t` | probe+payload slot | **lệnh downlink + thời điểm mở cống** |
| Đối tượng twin | bản sao trạng thái | Kalman predictor | "lightweight twin" = predictor | **twin nhận `u` làm đầu vào (what-if)** |
| Ràng buộc an toàn | không có (tối ưu E[AoI]) | ngưỡng nhiệt **tĩnh** | ngưỡng **tĩnh**, point-in-time | **3 ràng buộc ghép**, ngưỡng **động theo giai đoạn** |
| Mối nguy thứ hai | không | không | không | **chất lượng nguồn nước (mặn theo triều)** |
| Hành động "không làm gì" | không tồn tại | không tồn tại | không tồn tại | **WITHHELD là tối ưu** (định lý σ\*) |
| Cấu trúc không gian rủi ro | arm đồng chất | đồng chất | đồng chất | **nhiệt↔mặn ngược chiều theo khoảng cách biển** |

Gap-scan (1235 bản ghi OpenAlex+arXiv, abstract-level): `digital twin ∩ command/actuation ∩
chance-safety ∩ lossy-channel = 0` trên nền các component đều dày (A=277, B=89, C=61, D=77).
Corpus 2002 bài HUJOS: `digital twin` = 1 bài (du lịch), `networked control` = 0,
`chance constraint` = 0, `tưới ∩ IoT` = 0.

⇒ **Không phải "ghép buzzword"**: bỏ tính chất twin (đầu vào `u`) thì C2 và C3 không phát
biểu được; bỏ bối cảnh ĐBSCL thì không có sự ghép ngược chiều nhiệt↔mặn.

---

## 5. NGUỒN cho các ngưỡng nông học (đã tra, ghi để đưa vào references.bib)

| Tham số | Giá trị | Nguồn |
|---|---|---|
| Ngưỡng nhiệt đậu hạt lúa lúc trổ | **37.2 ± 0.2 °C** | PMC10721465 "From the floret to the canopy: High temperature tolerance during flowering" |
| Ức chế ống phấn | **> 35 °C** | PMC5847639 (heat stress → spikelet sterility at anthesis) |
| Giai đoạn mẫn cảm nhiệt nhất | booting, heading, flowering | PMC9789292 (systematic review) |
| Ngưỡng mặn lúa (EC) | **3.0 dS/m** (hướng dẫn cũ); **1.9 dS/m** (đo thực địa Sacramento) | Maas & Hoffman 1977; Grattan et al. 2002 — ars.usda.gov P1837.pdf |
| Độ dốc thiệt hại | **−12% năng suất / dS·m⁻¹** trên ngưỡng | ars.usda.gov P1837.pdf |
| Mẫn cảm mặn theo giai đoạn | rất nhạy ở mạ, tăng dần chịu mặn khi chín; **trổ còn tranh cãi** (Pearson & Bernstein vs Kaddah) | ars.usda.gov P572.pdf "Crop salt tolerance — current assessment" |
| FAO-56 ET0 hourly, Kc, Ks | eq. 7,8,11,13,21–28,37,39–41,47,53,82–84 | Allen et al. 1998, FAO Irrigation & Drainage Paper 56 |
| SCS-CN runoff | CN method, Ia = 0.2S | SCS 1972 |

⚠️ **Điểm phải xử lý trung thực trong bài:** nguồn USDA ghi nhận lúa **mẫn cảm mặn nhất ở
giai đoạn mạ**, và *có tranh cãi* về độ nhạy lúc trổ. Trong khi đó mẫn cảm **nhiệt** lại cao
nhất lúc trổ. Hai đỉnh nhạy cảm **lệch giai đoạn** nhau ⇒ càng củng cố thiết kế "ngưỡng động
theo giai đoạn" (C3), và phải nêu tranh cãi này trong Limitations thay vì chọn một phía.

---

## 6. Việc còn lại (thứ tự)

1. `src/tide_salinity.py` — pha triều tất định + mô hình mặn nguồn theo giờ, **kèm nhãn
   scenario model** và tham số biên độ để quét độ nhạy. Test: pha triều đúng chu kỳ ~12.4 h,
   mặn ∈ [0, EC_max], có giờ "cửa sổ ngọt".
2. `src/twin_gate.py` — mở rộng `twin_gate` thành cổng 3 ràng buộc, không gian hành động
   `(mm, τ)`.
3. **T2 (ngưỡng age-of-command)** — chưa derive. Không được claim trước khi chứng minh.
4. `experiments/run_twingate_vn.py` — 3 trạm × 2 kênh × seeds, cùng khung window/seed với
   RABS. Metric: % giờ vi phạm, **số lần bơm mặn** (metric mới, đặc thù VN), ngày stress nhiệt,
   tổng nước, số lệnh, số lần tưới đúp.
   ⚠️ Vùng thấy được trade-off: σ_frac ∈ [0.05, 0.20], δ ∈ [0.01, 0.20] (hai đầu bão hoà).
5. Bản thảo → convert Word theo `HUJOS_venue_spec.md` (Palatino 10pt, ≤12 trang, Vancouver).
6. Trước khi nộp: quét lại DBLP (phiên này fail cả 2 client), đọc full-text 4 bài hàng xóm.
7. **KHÔNG push** khi chưa được anh duyệt.
