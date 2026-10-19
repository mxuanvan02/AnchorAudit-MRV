# ĐỀ CƯƠNG BÀI BÁO K1 (TwinGate-VN)

Đề tài: DHH2025-19-07 "Nghiên cứu giải pháp nâng cao hiệu quả trong nông nghiệp thông minh dựa trên mạng điều khiển"
Venue đích: **HUJOS-TT** (Tạp chí Khoa học ĐH Huế: Kỹ thuật & Công nghệ)
Ngày: 2026-10-03 · Trạng thái: **đề cương chờ anh duyệt**; chưa viết bản thảo

---

## 0. Tên bài (3 phương án — cần anh chọn)

Ràng buộc anh đã đặt: từ khoá phải là **thuật ngữ chuẩn tra ra được trong title nguồn**, tên **không lặp từ**, và **không framing hẹp hơn nội dung thật**.

| # | Tên tiếng Việt | Tên tiếng Anh | Nhận xét |
|---|---|---|---|
| **P1** | Cổng an toàn dựa trên bản sao số cho lệnh điều khiển tưới qua mạng mất gói: tiếp cận ràng buộc xác suất ở đồng bằng sông Cửu Long | Digital-Twin-Gated Safe Irrigation Commanding over Lossy Networks: A Chance-Constrained Approach for the Mekong Delta | Đủ 5 thuật ngữ chuẩn (`digital twin`, `chance-constrained`, `packet loss`, `irrigation`, `Mekong Delta`); nhưng **chưa nêu được mối nguy kép** |
| **P2** | Điều khiển tưới an toàn qua mạng mất gói dưới rủi ro kép nhiệt độ và xâm nhập mặn: một cổng bản sao số có ràng buộc xác suất | Safe Irrigation Commanding over Lossy Networks under Coupled Heat and Salinity Risk: A Chance-Constrained Digital-Twin Gate | **Nêu được đóng góp đặc thù VN**; dài hơn |
| **P3** | Khi nào không nên tưới: cổng bản sao số ràng buộc xác suất cho lệnh điều khiển qua mạng mất gói ở đồng bằng sông Cửu Long | When Not to Irrigate: A Chance-Constrained Digital-Twin Gate for Command Delivery over Lossy Networks in the Mekong Delta | Nhấn **WITHHELD là hành động tối ưu** (điểm lý thuyết mới nhất); nhưng tiêu đề dạng câu hỏi có thể bị hội đồng trong nước coi là ít trang trọng |

**Em nghiêng P2** vì nó không framing hẹp hơn nội dung (nội dung có 3 ràng buộc + 2 mối nguy ngược chiều), và mọi từ khoá đều là thuật ngữ chuẩn.

⚠️ Cụm "TwinGate" chỉ là **tên nội bộ của mã nguồn**, không phải thuật ngữ — không được đưa vào tiêu đề hay từ khoá (đúng lỗi "khái niệm tự đặt" anh đã cảnh báo).

---

## 1. Vấn đề nghiên cứu

Ở đồng bằng sông Cửu Long, hệ thống giám sát–điều khiển nông nghiệp vận hành trên hạ tầng vô tuyến chất lượng thấp: mất gói kiểu burst, pin hạn chế, vùng phủ chập chờn. Hai bài đã công bố của đề tài (RABS, CAW-VoU) xử lý chiều **dữ liệu đi lên** — chọn cảm biến nào được truyền. Nhưng giá trị vận hành thật nằm ở chiều **lệnh đi xuống**: mở cống, chạy bơm.

Một lệnh tưới bị mất gói gây hai hậu quả đối lập nhau và cả hai đều tốn kém:
- **không tới** → cây chịu hạn thật trong khi hệ thống tưởng đã tưới;
- **gửi lại mù quáng** → tưới đúp, lãng phí nước và pin.

Nghiêm trọng hơn, ở ĐBSCL **quyết định tưới không chỉ là quyết định về lượng nước**. Trong cùng một thời điểm, một lệnh có thể đồng thời:
- cứu lúa khỏi sốc nhiệt bất thuận nghịch (nếu đang trổ và nhiệt sắp vượt ngưỡng), và
- **chủ động đưa muối vào tầng rễ** (nếu nguồn nước đang mặn theo triều).

Một bộ điều khiển chỉ tối ưu cân bằng nước sẽ phát lệnh trong tình huống thứ hai — tức là **ra quyết định đúng theo mô hình nhưng gây hại theo thực tế nông học**.

**Vấn đề:** làm thế nào để gateway quyết định *có phát lệnh hay không, phát lượng bao nhiêu, và vào giờ nào trong chu kỳ triều*, sao cho trạng thái ruộng sau lệnh nằm trong vùng an toàn với xác suất đảm bảo được, trong điều kiện kênh lệnh mất gói burst và độ tin cậy của mô hình dự báo là hữu hạn?

---

## 2. Khoảng trống nghiên cứu (kèm bằng chứng đã quét, không phải ký ức)

### 2a. Khoảng trống trong văn liệu quốc tế

Quét OpenAlex + arXiv, **1235 bản ghi** (1217 ở mức abstract), 2010–2026, phân rã claim thành 7 component:

| Component | Mật độ |
|---|---|
| A digital twin | 277 |
| B command/actuation | 89 |
| C chance constraint / probabilistic safety | 61 |
| D lossy channel / packet dropout | 77 |
| E agriculture/irrigation | 419 |
| F what-if / counterfactual simulation | 76 |
| G soil water balance / FAO-56 | 73 |

Các cặp nền đều **dày**: B∩C = 9, B∩D = 9, E∩G = 70. Nhưng:

```
A ∩ B ∩ C ∩ D      = 0
A ∩ B ∩ C ∩ D ∩ E  = 0
A ∩ E ∩ G          = 0
```

Hàng xóm gần nhất `A∩B∩E` = **4 bài**, đã đọc ở mức abstract: 2 bài review, 1 bài digital twin của máy kéo tự hành, 1 bài twin cho soft robotics. **Không bài nào là đối thủ trực tiếp.**

Crossref round 3 (139 bản ghi, title-only) cho cùng kết quả 0.

### 2b. Khoảng trống trong chính tạp chí đích

Quét **2002 bài HUJOS** (TT/ARD/NS/ED, sau dedupe theo DOI):

| Thuật ngữ (probe cả tiếng Việt + Anh) | Số bài |
|---|---|
| digital twin / bản sao số / song sinh số | **1** — bài bibliometric về *du lịch thông minh* (HUJOS-ED 2024) |
| điều khiển qua mạng / networked control | **0** |
| ràng buộc xác suất / chance-constrained | **0** |
| tưới ∩ IoT/cảm biến | **0** |

30 bài có từ "tưới" đều là nông học thuần (giống lạc chịu hạn, đậu xanh đất lúa thiếu nước, quản lý rơm rạ, thích hợp đất đai bưởi Thanh Trà, lan hồ điệp in vitro); chỉ 1 bài gần kỹ thuật (hệ thống tưới phun sương nhà lưới, 2019) và **không có mô hình toán**.

### 2c. Phát biểu khoảng trống

> Toàn bộ nhánh đồng bộ bản sao số (AoDT, AoT, AoSync, BAoII, DT placement/offload trong MEC) tối ưu **luồng dữ liệu đi lên** theo tuổi thông tin; nhánh điều khiển qua mạng mất gói tối ưu **tín hiệu điều khiển** theo tiêu chí ổn định; nhánh tưới tiêu tối ưu **lượng nước** theo cân bằng nước. Ba nhánh này **chưa gặp nhau**: chưa có công trình nào dùng bản sao số làm **cổng an toàn tiền-phát cho lệnh điều khiển** trên kênh mất gói, với ràng buộc xác suất, trong đó hành động "không phát" là một lựa chọn tối ưu.

### 2d. Lỗ hở bằng chứng phải khai báo trong bài

- **DBLP không quét được** trong phiên này: `urllib` → `RemoteDisconnected`, `curl` → lỗi 56, cả 2 client. ⇒ chưa quét KSE/RIVF/ACIIDS/IUKM. Đây là **retrieval failure, không phải gap** — phải nêu trong Limitations hoặc quét lại trước khi nộp.
- Semantic Scholar trả 429 khi không có key.
- Corpus HUJOS **không nhất quán dấu tiếng Việt** (có bài mất dấu hoàn toàn) ⇒ các con số "0" không phải bằng chứng vắng mặt tuyệt đối.
- Chưa đọc full-text 4 bài hàng xóm.

---

## 3. Câu hỏi nghiên cứu

**RQ1.** Với một bản sao số của cân bằng nước ruộng có độ bất định dự báo σ, điều kiện nào trên σ bảo đảm tồn tại ít nhất một lệnh tưới giữ trạng thái ruộng trong vùng an toàn với xác suất ≥ 1−δ? Khi điều kiện đó không thoả, hành vi đúng của gateway là gì?

**RQ2.** Dưới kênh lệnh mất gói burst, khi nào **gửi lại** một lệnh đã mất tốt hơn **chờ** thông tin mới, nếu tính đến cả chi phí tưới đúp khi lệnh cũ thật ra đã tới? Có tồn tại ngưỡng theo tuổi của lệnh đang chờ không?

**RQ3.** Khi ràng buộc an toàn gồm nhiều mối nguy **ngược chiều nhau theo không gian và thời gian** (sốc nhiệt trong mùa khô, xâm nhập mặn cũng trong mùa khô, nhưng nặng nhẹ khác nhau theo khoảng cách tới biển), việc ghép chúng vào một cổng xác suất duy nhất thay đổi quyết định vận hành như thế nào so với cổng chỉ xét cân bằng nước?

---

## 4. Giả thuyết / mệnh đề kiểm chứng được

| | Phát biểu | Cách kiểm chứng | Trạng thái |
|---|---|---|---|
| **H1** | Tồn tại ngưỡng σ\* = W/(2·z_{1−δ/2}) sao cho với σ ≥ σ\* cổng **rỗng với mọi tập lệnh** | đã derive + đối chiếu số đo | ✅ **ĐÃ VERIFY** |
| **H2** | Tồn tại ngưỡng tuổi lệnh a\* mà trên đó resend thắng chờ đợi | cần derive | ⬜ chưa |
| **H3** | Cổng chỉ xét cân bằng nước phát lệnh bơm mặn trong cửa sổ sốc nhiệt; cổng 3 ràng buộc chặn được | cần experiment | ⬜ chưa |
| **H4** | Số giờ sốc nhiệt tập trung hoàn toàn vào mùa khô và trùng đỉnh xâm nhập mặn | đã đo trên ERA5 | ✅ **ĐÃ ĐO** |

---

## 5. Đóng góp dự kiến

1. **Đổi đối tượng khan hiếm** từ gói dữ liệu uplink sang **lệnh downlink kèm thời điểm phát** — không gian hành động `(lượng mm, giờ τ)` thay vì chỉ `lượng`.
2. **Đổi vai trò của bản sao số** từ bộ ước lượng trạng thái sang **cổng an toàn tiền-phát**. Tính chất quyết định: twin nhận lệnh `u` làm đầu vào (câu hỏi phản thực what-if) — thứ mà predictor AR(1)/Kalman không có.
3. **Kết quả lý thuyết σ\*** (T1'): biến **độ trung thực của twin thành tham số của guarantee**, và chỉ ra tồn tại vùng mà cơ chế **tê liệt hoàn toàn** — khái niệm không có trong các bài đồng bộ bản sao số (chúng tối ưu E[AoI], không có khái niệm "cổng rỗng").
4. **WITHHELD là hành động tối ưu**, không phải thất bại — đối lập với mọi scheduler AoI (luôn phải phát gì đó). Ngoài đồng tương ứng "chờ con nước".
5. **Ngữ cảnh ĐBSCL có bằng chứng đo**: hai mối nguy ngược chiều, và cấu trúc không gian nhiệt↔mặn ngược nhau giữa trạm nội đồng và trạm ven biển.

---

## 6. Bằng chứng thực nghiệm nền tảng (số ĐÃ ĐO, không phải dự kiến)

Đo trên ERA5 2024, 8784 giờ × 3 trạm, 5 biến, **0 null**, có file provenance. Toạ độ lấy nguyên văn từ repo tái lập RABS nên cùng định nghĩa "zone" với 2 bài đã nộp.

### 6a. Kiểm chứng mô hình vật lý (FAO-56)

| Đại lượng | Đo được | Đối chiếu độc lập |
|---|---|---|
| ET0 năm, Cần Thơ | **1550 mm** | ĐBSCL ~1300–1700 ✓ |
| ET0 ngày TB / median / p95 / max | **4.24 / 4.26 / 6.44 / 7.20 mm** | ~3–6 ✓ |
| ET0 đêm TB | **0.0153 mm/h** | ≈0 ✓ |
| Mưa 2024 Cần Thơ | **2248 mm** | ~1500–2200 ✓ |
| R_a đêm / ngày max | **0.0000 / 4.841 MJ·m⁻²h⁻¹** | đêm = 0 ✓ |
| Bảo toàn khối lượng 1 năm | **residual = 0.000e+00** | chính xác tuyệt đối |
| SCS-CN, P=50 mm, CN=80 | **13.80 mm** | closed-form tính tay: S=63.5, Ia=12.7 → 13.80 ✓ |

### 6b. Cấu trúc hai mối nguy (phát hiện chính)

Ngưỡng có nguồn: **35.0 °C** (ức chế ống phấn), **37.2 ± 0.2 °C** (ngưỡng tới hạn đậu hạt lúc trổ).

| Trạm | giờ >35 °C | giờ >37.2 °C | ngày Tmax>35 | ngày Tmax>37.2 |
|---|---|---|---|---|
| Cần Thơ (10.05°N, **nội đồng**) | **208** (2.37%) | **37** (0.42%) | 46/366 | **12** |
| Cà Mau (9.18°N, ven biển) | 98 (1.12%) | 7 (0.08%) | 28/366 | 5 |
| Sóc Trăng (9.60°N, **ven biển**) | 64 (0.73%) | 1 (0.01%) | 21/366 | 1 |

Giờ >35 °C theo tháng tại Cần Thơ:
`I:0  II:0  III:28  IV:155  V:25  VI:0  VII:0  VIII:0  IX:0  X:0  XI:0  XII:0`

⇒ **100% sốc nhiệt rơi vào tháng III–V; 0 giờ trong VI–XII.** Cả 3 trạm cùng dạng (Sóc Trăng IV=48/64; Cà Mau IV=73/98).
Mưa mùa khô (XII–V) chỉ **420 mm = 18.7%** tổng năm; mùa mưa 1828 mm.

Cần Thơ có **3.25×** số giờ sốc nhiệt của Sóc Trăng (hiệu ứng điều hoà của biển), nhưng xâm nhập mặn thì **ngược chiều**.

### 6c. Kiểm chứng cơ chế cổng (test đã PASS)

Tính chất what-if — cùng belief `w0 = 130.25 mm`, horizon 6 h:

| lệnh | dự đoán w |
|---|---|
| 0 mm | 129.80 mm |
| 10 mm | 139.80 mm |
| 25 mm | 154.80 mm |

Đơn điệu theo độ trung thực twin (600 slots, δ=0.05):

| σ_frac | released |
|---|---|
| 0.02 | 600 (100%) |
| 0.05 | 600 (100%) |
| 0.10 | 135 (22.5%) |
| 0.20 | 0 |
| 0.40 | 0 |

Đối chiếu định lý σ\* = 15.18 mm (δ=0.05, W=59.5 mm): σ(age+H) tại age 0 lần lượt là 2.82 / 7.05 / 14.10 / 28.21 / 56.41 mm ⇒ định lý **dự đoán đúng** hiện tượng.

Gate khác baseline tại cùng một slot (depletion 0.60): reactive threshold phát `open30` (30 mm, lớn nhất, không xét xác suất); cổng twin phát `open15` với p=0.963. Trên ruộng đã ướt: cổng **WITHHELD** (p=0.513), reactive vẫn phát.

Kênh lệnh Gilbert–Elliott (20000 slot, seed 11): mild — delivery 0.828, bad-state 0.214; severe — delivery 0.416, bad-state 0.348.

Failure mode của baseline đã tái hiện: ACK mất nhưng lệnh đã tới → `blind_resend` phát lại 20 mm → ruộng nhận 40 mm (**tưới đúp**).

---

## 7. Phương pháp

### 7a. Kiến trúc

```
        uplink (thưa)                 downlink (khan hiếm, mất gói burst)
 [cảm biến ruộng] --------> [gateway] --------> [cống / bơm]
                              |   ^
                    re-anchor |   | phản hồi vật lý
                              v   |
                    [BẢN SAO SỐ RUỘNG]
                    · cân bằng nước FAO-56 (đã code, đã test)
                    · nguồn nước theo triều + mặn (mô hình tình huống)
                    · nhiệt / giai đoạn sinh trưởng (ERA5 + GDD)
                    · độ bất định σ(age) — luật staleness kế thừa CAW-VoU
```

Vòng kín: cảm biến tái neo (re-anchor) twin; twin vừa là bộ ước lượng vừa là **máy trả lời câu hỏi phản thực có điều kiện vào lệnh**.

### 7b. Không gian hành động

`u = (q, τ)` — lượng nước `q` (mm) và giờ mở trong chu kỳ triều `τ`. Tập ứng viên rời rạc, có cả `q = 0`.

### 7c. Cổng an toàn 3 ràng buộc

Phát `u` chỉ khi **cả ba** đạt `P ≥ 1−δ` dưới σ của chính twin:

| | Ràng buộc | Đại lượng | Nguồn tham số |
|---|---|---|---|
| C1 | Cân bằng nước | `W_H ∈ [w_lo, w_hi]` | FAO-56 ✅ đã code + test |
| C2 | Chất lượng nguồn | `EC_src(τ) ≤ EC_crit(stage)` | triều tất định + mặn **mô hình tình huống** ⚠️ |
| C3 | Rủi ro nhiệt bất thuận nghịch | `T_max trong H ≤ T_crit(stage)` | ERA5 ✅ đo thật; ngưỡng 35.0/37.2 °C có nguồn |

Không ràng buộc nào thoả ⇒ **WITHHELD**.

### 7d. Dữ liệu

| Thành phần | Trạng thái |
|---|---|
| Nhiệt/ẩm/gió/bức xạ/mưa giờ, 3 trạm, 2024 | ✅ ERA5 thật, 0 null, provenance |
| ET0, cân bằng nước, Ks, runoff | ✅ công thức chuẩn, đã verify |
| Số giờ sốc nhiệt, phân bố tháng | ✅ đo từ ERA5 |
| Pha triều bán nhật (~12.4 h) | ✅ tính tất định, không cần API |
| **Nồng độ mặn nguồn theo giờ** | ⚠️ **MÔ HÌNH TÌNH HUỐNG** — em không có số đo mặn 2024 tại 3 trạm |
| Giai đoạn sinh trưởng (GDD) | ⚠️ tính từ ERA5 + lịch thời vụ công khai, phải ghi nguồn |

**Quy tắc tự ràng buộc:** tham số không đo được và không có nguồn công bố thì (a) khai báo là tham số tình huống, (b) quét độ nhạy, (c) **không xuất hiện trong Abstract như kết quả**.

---

## 8. Kết quả lý thuyết

### T1 — Soundness của cổng ✅ đã derive

Nếu cổng phát `u` thì `P(W_H ∈ S) = Φ((w_hi−μ)/σ_H) − Φ((w_lo−μ)/σ_H) ≥ 1−δ`, với `σ_H = σ(age+H)` là bất định của chính twin, suy giảm theo age đúng luật AR(1)/Kalman kế thừa CAW-VoU.

### T1' — Hệ quả σ\* ✅ đã derive + đã verify bằng số đo

Cổng không rỗng **chỉ khi** `σ_H < σ* ≡ W/(2·z_{1−δ/2})`; với `σ_H ≥ σ*` cổng rỗng **với mọi tập lệnh**.

| δ | z_{1−δ/2} | **σ\*** |
|---|---|---|
| 0.50 | 0.6745 | 44.11 mm |
| 0.20 | 1.2816 | 23.21 mm |
| 0.05 | 1.9600 | **15.18 mm** |
| 0.01 | 2.5758 | 11.55 mm |

Ngưỡng theo age: `sigma_frac_crit(age) = σ*/(TAW·sqrt(Σ_{k=0}^{age+H} ρ^{2k}))` → age 0: 0.1076; age 6: 0.0977; age 20: 0.0947.

### T2 — Ngưỡng tuổi lệnh ⬜ CHƯA derive

Mục tiêu: dưới Gilbert–Elliott, tìm `a*` sao cho resend thắng chờ đợi ⟺ age > a\*, biểu thức theo (p_gb, p_bg, loss_in_bad, chi phí tưới đúp `c_dup`, lợi ích `c_ok`).
**Không được viết claim này vào bản thảo trước khi chứng minh xong.**

---

## 9. Thiết kế thực nghiệm

- **Trạm:** Cần Thơ (nội đồng), Sóc Trăng + Cà Mau (ven biển) — giữ đúng cặp tương phản nhiệt↔mặn
- **Kênh:** mild (delivery 0.828) và severe (delivery 0.416)
- **Policy so sánh:** TwinGate-VN (3 ràng buộc) / TwinGate-C1 (chỉ cân bằng nước) / reactive threshold / blind resend / oracle
- **Khung window + seed:** dùng lại đúng khung của RABS (20 seeds, window 720 giờ) để so sánh chéo được
- **Quét:** σ_frac ∈ [0.05, 0.20], δ ∈ [0.01, 0.20] — ⚠️ hai đầu bão hoà (100%→0%) nên phải quét mịn trong vùng này, nếu không đồ thị Pareto chỉ là 2 đoạn phẳng

**Metric:**
1. % giờ vi phạm vùng an toàn
2. **số lần bơm mặn** (metric mới, đặc thù VN — không có trong 2 bài trước)
3. ngày/giờ stress nhiệt trong cửa sổ trổ
4. tổng nước tưới (mm) và số lệnh đã phát
5. số lần **tưới đúp**
6. số lần WITHHELD (và WITHHELD đúng hay sai)

**Kiểm định:** paired Wilcoxon giữa các policy trên cùng seed, kèm effect size — giống chuẩn RABS đã dùng.

⚠️ **Chưa chạy.** Không có số dự kiến; mọi con số trong bài sẽ là số chạy ra, không phải số ước đoán.

---

## 10. Hạn chế (viết sẵn để đưa vào bài, không giấu)

1. **Không có số đo mặn thực địa** tại 3 trạm năm 2024 ⇒ C2 dựa trên mô hình tình huống; phải quét độ nhạy biên độ xâm nhập và nêu rõ đây không phải kết quả thực nghiệm.
2. **DBLP chưa quét được** (retrieval failure cả 2 client) ⇒ chưa loại trừ được prior art ở các hội nghị CNTT khu vực VN (KSE/RIVF/ACIIDS/IUKM).
3. **Tranh cãi nông học phải nêu:** nguồn USDA ghi lúa **mẫn cảm mặn nhất ở giai đoạn mạ**, và *có tranh cãi* về độ nhạy lúc trổ (Pearson & Bernstein vs Kaddah); trong khi mẫn cảm **nhiệt** lại đỉnh lúc trổ. Hai đỉnh nhạy cảm **lệch giai đoạn** nhau. Phải trình bày cả hai phía, không chọn một.
4. **T2 chưa chứng minh** ⇒ nếu không xong thì bài chỉ có T1/T1', phải điều chỉnh claim.
5. Mô phỏng, chưa thực địa — giống hạn chế mà CAW-VoU đã tự ghi nhận.
6. N = 3 trạm. Có thể mở rộng lên 10 trạm (script fetch đã hỗ trợ) nếu hội đồng yêu cầu.
7. Đất: dùng tham số silty-clay loam trung bình của FAO-56 Table 2, không phải số đo đất từng thửa.

---

## 11. Cấu trúc bài theo ràng buộc HUJOS-TT (≤12 trang)

| Phần | Trang dự kiến |
|---|---|
| Tóm tắt (VI + EN, ≤250 từ mỗi bản) + 3–5 từ khoá | 0.5 |
| 1. Đặt vấn đề | 1.5 |
| 2. Tổng quan & khoảng trống | 1.5 |
| 3. Mô hình hệ thống (plant FAO-56, kênh lệnh, twin, σ(age)) | 2 |
| 4. Cổng an toàn & kết quả lý thuyết T1, T1' | 2 |
| 5. Thực nghiệm | 2.5 |
| 6. Kết luận & hạn chế | 1 |
| Tài liệu tham khảo (Vancouver, ≥15 nguồn) | 1 |

**Format cứng** (đã đọc từ jos.hueuni.edu.vn): nộp **Word .docx** (không phải PDF LaTeX); Palatino Linotype 10 pt; khổ 19×27 cm; lề 2 cm; giãn dòng 1.15; spacing 6 pt before / 3 pt after; công thức **MathType** đánh số phải; hình ≤7×14 cm caption **dưới**, bảng caption **trên**, số hình/bảng in đậm; có khoảng trắng giữa số và đơn vị (trừ ° ′ ″); TLTK **Vancouver [số]** từ 2026; tóm tắt + từ khoá cả 2 ngôn ngữ, tiếng Việt đầu bài / tiếng Anh cuối bài; cuối bài có học hàm, học vị, cơ quan, địa chỉ, ĐT, email, **chữ ký tác giả**, và ghi rõ corresponding author.

⇒ Quy trình: viết LaTeX (kiểm soát công thức + bib) → pandoc sang Word → thay công thức bằng MathType/OMML, đổi font/lề/giãn dòng, đổi bib sang Vancouver → in, ký, scan.

---

## 12. Nguồn cho tham số (đã tra, để đưa vào references)

| Tham số | Giá trị | Nguồn |
|---|---|---|
| Ngưỡng nhiệt đậu hạt lúa lúc trổ | **37.2 ± 0.2 °C** | PMC10721465 — "From the floret to the canopy: High temperature tolerance during flowering" |
| Ức chế ống phấn | **> 35 °C** | PMC5847639 — heat stress → spikelet sterility at anthesis |
| Giai đoạn mẫn cảm nhiệt nhất | booting, heading, flowering | PMC9789292 — systematic review |
| Ngưỡng mặn lúa | **3.0 dS/m** (hướng dẫn); **1.9 dS/m** (đo thực địa) | Maas & Hoffman 1977; Grattan et al. 2002 — ars.usda.gov P1837.pdf |
| Độ dốc thiệt hại mặn | **−12% / dS·m⁻¹** trên ngưỡng | ars.usda.gov P1837.pdf |
| Mẫn cảm mặn theo giai đoạn (có tranh cãi) | mạ rất nhạy; trổ còn tranh cãi | ars.usda.gov P572.pdf — "Crop salt tolerance — current assessment" |
| ET0 hourly, Kc, Ks | eq. 7,8,11,13,21–28,37,39–41,47,53,82–84 | Allen et al. 1998, FAO IDP 56 |
| SCS-CN runoff | CN method, Ia = 0.2S | SCS 1972 |
| Prior art phải trích & phân biệt | 11 DOI đã verify | xem `gapscan_K1/GAPSCAN_REPORT_K1.md` §4 |

⚠️ Tất cả nguồn trên mới verify ở mức **tra ra được**; trước khi nộp phải đối chiếu Crossref/DOI từng cái theo quy trình `bibtex-reference-audit`, và tách rõ verified ↔ inferred.

---

## 13. Trình tự thực hiện (không ước lượng thời gian — chưa có bằng chứng để ước lượng)

1. `src/tide_salinity.py` — pha triều tất định + mô hình mặn có nhãn scenario. **Cổng kiểm:** test chu kỳ ~12.4 h, mặn ∈ [0, EC_max], tồn tại "cửa sổ ngọt".
2. Mở rộng `src/twin_gate.py` thành cổng 3 ràng buộc, hành động `(q, τ)`. **Cổng kiểm:** test tái hiện được H3 (cổng 1 ràng buộc phát lệnh bơm mặn, cổng 3 ràng buộc chặn).
3. Derive T2. **Cổng kiểm:** proof đọc được + verify số bằng mô phỏng ngưỡng.
4. `experiments/run_twingate_vn.py` + quét σ_frac/δ mịn. **Cổng kiểm:** số chạy ra, seed tái lập, Wilcoxon có ý nghĩa.
5. Quét lại DBLP + đọc full-text 4 bài hàng xóm. **Cổng kiểm:** novelty claim còn đứng.
6. Bản thảo LaTeX → verify claim↔bằng chứng → convert Word đúng thể lệ. **Cổng kiểm:** ≤12 trang, ≥15 TLTK Vancouver, tóm tắt 2 ngôn ngữ ≤250 từ.
7. **KHÔNG push, KHÔNG nộp** khi chưa được anh duyệt.

---

## 14. Rủi ro chính và cách giảm

| Rủi ro | Mức | Cách giảm |
|---|---|---|
| Không có số đo mặn ⇒ C2 bị hội đồng chê là giả định | **Cao** | Nhãn rõ scenario model + quét độ nhạy biên độ; hoặc **hạ C2 xuống thành phân tích tình huống** ở Discussion thay vì ràng buộc cứng trong cổng |
| T2 không chứng minh được | Trung | Bài vẫn đứng trên T1/T1' + thực nghiệm; bỏ claim T2 |
| Không có reviewer chuyên NCS trong pool HUJOS-TT (chỉ 96 bài được index) | Trung | Viết phần trực giác vận hành rõ cho người không chuyên điều khiển; đẩy chứng minh xuống phụ lục |
| Vùng bão hoà σ_frac/δ làm đồ thị phẳng | Thấp | Đã biết trước: quét mịn [0.05, 0.20] × [0.01, 0.20] |
| Bị coi là "ghép buzzword digital twin" | Thấp | Tính chất what-if đã test: twin nhận `u` làm đầu vào, predictor không làm được |

---

## 15. Câu hỏi cần anh quyết trước khi em code tiếp

1. **Tên bài**: P1 / P2 / P3? (em nghiêng P2)
2. **C2 (mặn) nên là ràng buộc cứng trong cổng, hay hạ xuống phân tích tình huống ở Discussion?** — đây là rủi ro lớn nhất của đề cương vì em không có số đo mặn.
3. **Có cần thêm trạm / thêm năm ERA5** (2023, 2025) để hội đồng khỏi chê N=3, một năm?
4. Em **chưa có** nguồn lịch thời vụ lúa ĐBSCL dạng máy đọc được — anh có, hay em dùng lịch công khai của Sở NN&PTNT/Cục Trồng trọt và ghi rõ nguồn?
