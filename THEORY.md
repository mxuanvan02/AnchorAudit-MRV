# LÝ THUYẾT K1 — đã derive và verify bằng số (2026-10-03)

Ký hiệu: safe set `S = [w_lo, w_hi]` (mm nước trong tầng rễ), rộng `W = w_hi − w_lo`;
`TAW` = total available water; twin có predictive std `σ` tại thời điểm xét;
`δ` = xác suất vi phạm cho phép; `z_q` = phân vị chuẩn.

---

## T1 (Soundness của cổng — guarantee chính)

**Phát biểu.** Gọi `μ(u)` là trung bình nước tầng rễ sau horizon `H` khi phát lệnh `u`,
và `σ_H = σ(age + H)` là predictive std của chính twin tại chân trời đó. Nếu cổng phát `u`
thì, với giả định residual của twin là Gaussian,

```
P( W_H ∈ S ) = Φ((w_hi − μ)/σ_H) − Φ((w_lo − μ)/σ_H) ≥ 1 − δ
```

**Chứng minh.** Đây chính là điều kiện lọc của `twin_gate`: lệnh chỉ được phát khi
`safe_probability(μ, σ_H) ≥ 1 − δ`. Phần nội dung nằm ở chỗ `σ_H` là **độ bất định của
chính twin**, suy giảm theo age đúng luật AR(1)/Kalman kế thừa từ CAW-VoU
(`σ(a) = σ₀·sqrt(Σ ρ^{2k}), k=0..a`, chặn trên bởi giá trị dừng `σ₀/sqrt(1−ρ²)`).
∎

**Điểm khoa học:** `δ` và `σ` KHÔNG phải hai tham số độc lập. T1 cho thấy mọi guarantee
đều đi qua tỉ số `W/σ_H` — tức là **chiều rộng vùng an toàn nông học so với độ trung thực
của twin**. Đây là đại lượng đo được trong thực tế, và nó dẫn thẳng tới T1'.

---

## T1' (Hệ quả σ* — điều kiện CẦN để cổng KHÔNG tê liệt) ← kết quả mạnh nhất

**Phát biểu.** Cổng chỉ có thể phát được một lệnh khi tồn tại `u` sao cho
`μ(u) ∈ [w_lo + z_{1−δ/2}·σ_H , w_hi − z_{1−δ/2}·σ_H]`. Do đó **điều kiện cần**,
không phụ thuộc tập lệnh:

```
σ_H  <  σ* ≡ W / (2 · z_{1−δ/2})
```

Khi `σ_H ≥ σ*`, cổng **rỗng với MỌI tập lệnh** — twin quá mờ để khẳng định an toàn,
và hành vi đúng duy nhất là WITHHELD (không phát), chứ không phải phát bừa.

**Suy ra ngưỡng độ trung thực theo age** (vì `σ_H = σ(age+H)`):

```
sigma_frac_crit(age) = σ* / ( TAW · sqrt(Σ_{k=0}^{age+H} ρ^{2k}) )
```

---

## VERIFY T1' bằng số thật (đã chạy, không phải ước đoán)

Cần Thơ, `SoilProfile` mặc định: TAW = 70.0 mm, FC = 160.0, WP = 90.0 mm.
Safe set depletion ∈ [0, 0.85] ⇒ `S = [100.5, 160.0]`, `W = 59.5 mm`. H = 6, ρ = 0.9.

| δ | z_{1−δ/2} | **σ*** (mm) | sigma_frac* (giá trị dừng) |
|---|---|---|---|
| 0.50 | 0.6745 | **44.11** | 0.2747 |
| 0.20 | 1.2816 | **23.21** | 0.1446 |
| 0.05 | 1.9600 | **15.18** | 0.0945 |
| 0.01 | 2.5758 | **11.55** | 0.0719 |

Ngưỡng `sigma_frac_crit` theo age (δ = 0.05): age 0 → 0.1076; age 2 → 0.1025;
age 6 → 0.0977; age 11 → 0.0956; age 20 → 0.0947.

**Đối chiếu với số ĐO trong `tests/test_twin_gate.py` (600 slots, age = k mod 12):**

| σ_frac | σ(age+H) tại age 0 | so với σ*=15.18 | age dùng được | dự đoán | **ĐO** |
|---|---|---|---|---|---|
| 0.02 | 2.82 mm | < | 12/12 | ~600 | **600** ✓ |
| 0.05 | 7.05 mm | < | 12/12 | ~600 | **600** ✓ |
| 0.10 | 14.10 mm | < | 4/12 | ~200 | **135** ✓ cùng bậc |
| 0.20 | 28.21 mm | ≥ | 0/12 | 0 | **0** ✓ |
| 0.40 | 56.41 mm | ≥ | 0/12 | 0 | **0** ✓ |

**⇒ Định lý DỰ ĐOÁN ĐÚNG hiện tượng.** Chênh 200 vs 135 ở hàng σ_frac = 0.10 là do dự đoán
chỉ đếm age khả dụng, còn thực nghiệm đòi `μ(u)` rơi đúng vào lõi — tức điều kiện đủ chặt
hơn điều kiện cần. Đó là **khe hở dự kiến**, không phải mâu thuẫn, và phải ghi rõ trong bài.

⚠️ **Lỗi em đã mắc và sửa khi derive (ghi lại để không lặp):** dự đoán thô đầu tiên dùng
`σ(age)` thay vì `σ(age + H)` nên ra 500/600 thay vì 135/600 — lệch hẳn. Rollout của twin
luôn cộng horizon. Khi derive bất kỳ bound nào trên cơ chế này phải dùng `σ(age+H)`.

---

## T2 (ngưỡng age-of-command — CHƯA derive xong)

Mục tiêu: dưới kênh Gilbert–Elliott, tìm ngưỡng `a*` sao cho **resend thắng chờ đợi** khi và chỉ
khi age của lệnh đang chờ > `a*`, với `a*` biểu thức theo (p_gb, p_bg, loss_in_bad,
chi phí tưới đúp `c_dup`, lợi ích lệnh tới `c_ok`).

Trạng thái: **chưa chứng minh**. `blind_resend_policy` đã tái hiện được failure mode
(tưới đúp 40 mm khi ACK mất nhưng lệnh đã tới) nên bài toán có ý nghĩa thật, nhưng
bound thì chưa có. Không được viết claim này vào bản thảo trước khi derive xong.

---

## Hàm lượng khoa học của bài (tóm tắt để viết Introduction)

1. **Đổi đối tượng khan hiếm**: từ *dữ liệu đi lên* (RABS, CAW-VoU, toàn bộ nhánh AoI/DT-sync)
   sang *lệnh đi xuống*. Đây là trục mới, gap-scan xác nhận empty join.
2. **Đổi vai trò của digital twin**: từ *bộ ước lượng trạng thái* sang *cổng an toàn tiền-phát*.
   Tính chất quyết định là twin nhận `u` làm đầu vào (what-if) — đã verify:
   cùng belief 130.25 mm, lệnh 0/10/25 mm → 129.80/139.80/154.80 mm.
3. **Biến độ trung thực twin thành tham số của guarantee** (T1'), và chỉ ra **ngưỡng σ\*
   mà dưới đó cơ chế chết hẳn** — một kết quả có dạng "twin fidelity budget", chưa thấy
   trong các bài DT-sync (chúng tối ưu E[AoI], không có khái niệm cổng rỗng).
4. **WITHHELD là một hành động hợp lệ**, không phải thất bại: khi `σ_H ≥ σ*`, im lặng là
   quyết định tối ưu. Điều này đối lập với mọi scheduler AoI (luôn phải phát gì đó).
