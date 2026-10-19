# Thư hỏi toà soạn HUJOS — bản thảo TwinGate (chưa gửi)

- **Gửi:** tckh_dhh@hueuni.edu.vn (Toà soạn Tạp chí Khoa học Đại học Huế)
- **CC (đề xuất):** Võ Viết Minh Nhật — Tổng biên tập HUJOS-TT (Techniques & Technology)
- **Người gửi:** TS. Nguyễn Tương Tri (corresponding author) — nguyentuongtri@dhsphue.edu.vn
- **Tiêu đề:** Thắc mắc về giới hạn số trang và định dạng bản nộp — HUJOS-TT

> **Số liệu trong thư này đã đo trên PDF build ngày 04/10/2026** (`paper/main.pdf`, 18 trang):
> thân bài 14 trang · Lời cảm ơn + TLTK 2 trang · Phụ lục/Abstract/Thông tin tác giả 2 trang
> · 13 bảng · 6 hình · 1 thuật toán · 25 tài liệu tham khảo.
> Ghi chú nội bộ, xoá trước khi gửi: bài thuộc đề tài cấp ĐHH mã số DHH2025-19-07.

---

Kính gửi Ban Biên tập Tạp chí Khoa học Đại học Huế,

Chúng tôi đang hoàn thiện bản thảo để nộp vào phân ban **HUJOS-TT (Techniques and Technology)**:

> **"Cổng an toàn bản sao số cho phát lệnh tưới trên mạng mất gói và liên hệ với chuẩn MRV phát thải"**
>
> Tác giả: Mai Xuân Văn (Trường THPT Thuận Hóa, Trường Đại học Sư phạm, Đại học Huế); Nguyễn Tương Tri (Trường Đại học Sư phạm và Viện Đào tạo Mở & Công nghệ thông tin, Đại học Huế — tác giả liên hệ).
>
> Kinh phí: đề tài cấp Đại học Huế, mã số DHH2025-19-07.

Bài báo trình bày một cơ chế điều khiển qua mạng dùng bản sao số để kiểm tra an toàn trước khi phát lệnh tưới trên kênh mất gói, kèm một kết quả lý thuyết về ngưỡng độ trung thực, kiểm chứng bằng mô phỏng trên dữ liệu khí hậu ERA5 tại ba trạm ở Đồng bằng sông Cửu Long, và phân tích liên hệ với yêu cầu đo đạc–báo cáo–thẩm định (MRV) của QĐ 4801/QĐ-BNNMT.

Bản thảo hiện có 18 trang, gồm 14 trang thân bài (từ Tóm tắt đến Kết luận), 2 trang Lời cảm ơn và Tài liệu tham khảo (25 nguồn), 2 trang Phụ lục, Abstract tiếng Anh và Thông tin tác giả. Trước khi nộp, chúng tôi xin phép hỏi năm điểm về thể lệ để bản nộp đúng ngay từ đầu:

1. **Giới hạn 12 trang bao gồm những phần nào?** Thể lệ mục 2 ghi "tối đa 12 trang". Xin hỏi giới hạn này có tính danh mục tài liệu tham khảo, phụ lục, Abstract tiếng Anh và mục Thông tin tác giả hay không?

2. **Có hình thức tài liệu bổ sung tách riêng không?** Nếu giới hạn 12 trang áp dụng cho toàn bộ tệp, chúng tôi có thể chuyển một phần bảng biểu và hình (hiện có 13 bảng, 6 hình, 1 thuật toán) sang tài liệu bổ sung nộp kèm như một tệp riêng hay không, hay phụ lục bắt buộc nằm trong cùng tệp và cùng số trang?

3. **Định dạng tệp ở vòng nộp đầu tiên.** Chúng tôi soạn bài bằng LaTeX (XeLaTeX). Ở vòng sơ khảo, toà soạn nhận tệp PDF dựng từ LaTeX hay bắt buộc nộp tệp Word theo mẫu của tạp chí? Nếu bắt buộc Word, xin cho chúng tôi **tệp mẫu chính thức** — trang thể lệ yêu cầu đăng nhập nên chúng tôi chưa tải được. Chúng tôi sẽ chuyển đổi đầy đủ định dạng: Palatino Linotype 10 pt, lề 2 cm, trích dẫn Vancouver đánh số trong ngoặc vuông.

4. **Trích dẫn và số nguồn tối thiểu.** Xin xác nhận HUJOS-TT dùng kiểu Vancouver [số] và có quy định số tài liệu tham khảo tối thiểu hay không (bài của chúng tôi hiện có 25 nguồn).

5. **Vị trí các phần song ngữ.** Hiện chúng tôi đặt tiêu đề, Tóm tắt tiếng Việt và Từ khoá ở trang đầu; tiêu đề tiếng Anh, Abstract, Keywords cùng mục Thông tin tác giả (kèm chữ ký) ở cuối bài. Cách bố trí này có đúng thể lệ không?

Chúng tôi xin cảm ơn Ban Biên tập và rất mong nhận được hướng dẫn.

Trân trọng,

**TS. Nguyễn Tương Tri**
Trường Đại học Sư phạm, Đại học Huế — 34 Lê Lợi, TP Huế
Viện Đào tạo Mở và Công nghệ thông tin, Đại học Huế
Email: nguyentuongtri@dhsphue.edu.vn / ntuongtri@hueuni.edu.vn
Điện thoại: [điền trước khi gửi]

---

## Nếu toà soạn trả lời

| Trả lời | Việc phải làm |
| --- | --- |
| 12 trang tính cả TLTK + phụ lục | Ép presentation: chuyển ~6 bảng/hình xuống Phụ lục, thu nhỏ hình, bảng scriptsize. **Không cắt chữ.** Hiện thân bài đã 14 trang nên phải ép cả thân bài |
| Phụ lục được nộp tách riêng | Tách Phụ lục A/B + 4–5 bảng phụ ra tệp supplementary; tệp chính còn ~16 trang, vẫn phải ép tiếp |
| Chỉ nhận Word theo mẫu | Dùng skill `latex-to-venue-word-template` + `paper/build_docx.py`; chờ tệp mẫu thật |
| Không trả lời / trả lời chung chung | Giữ 18 trang và nộp bản PDF, kèm thư giải trình ngắn về độ dài |
