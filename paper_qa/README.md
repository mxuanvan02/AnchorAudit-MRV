# paper_qa/ — kiểm tra chất lượng bản thảo LaTeX

Nhóm script này phục vụ **quy trình QA bản thảo** của nhóm tác giả, KHÔNG phải
thí nghiệm khoa học và KHÔNG được `reproduce.sh` gọi.

## Lưu ý quan trọng

Các script đọc bản thảo từ thư mục `paper2_hujos/` — thư mục này **không nằm
trong repo công khai** (chỉ gồm thí nghiệm, dữ liệu, hình). Vì vậy người tái
lập bên ngoài sẽ thấy các gate báo "thiếu file main": đó là hành vi dự kiến,
không phải lỗi.

## Nhóm script

| Nhóm | Ví dụ | Kiểm tra |
|---|---|---|
| Từ viết tắt, ký tự | `check_acronym_first_use.py`, `check_vi_foreign_chars.py` | viết tắt khai triển lần đầu; ký tự lạ trong bản tiếng Việt |
| Số liệu | `check_number_provenance.py`, `verify_paper_claims.py`, `audit_all_numbers.py`, `extract_paper_numbers.py` | mọi con số trong bài phải truy vết được về `outputs/` |
| Bố cục trang | `measure_pagebudget.py`, `measure_whitespace.py`, `measure_fonts.py`, `measure_headings.py`, `qa_hujos_layout.py` | ngân sách trang, phông chữ, lề theo mẫu HUJOS |
| Sinh bảng | `make_tables_hujos_vi.py`, `make_latex_tables.py`, ... | dựng bảng LaTeX trực tiếp từ CSV trong `outputs/` |
| Chốt nguồn | `check_latex_source_package.py`, `check_no_orphan_tex.py`, `negative_control_supp_gate.py` | gói nguồn nộp tạp chí; file mồ côi |

## Cách chạy (chỉ nhóm tác giả, trong cây làm việc có bản thảo)

```bash
python3 paper_qa/check_acronym_first_use.py
python3 paper_qa/verify_paper_claims.py
```

Vài script import module cùng nhóm (`make_tables_hujos.py` →
`make_tables_anchored.py`) hoặc từ `experiments/` (`make_tables_paper2.py` →
`fraud_detection`); các đường dẫn đã được thêm `sys.path` tương ứng nên chạy
trực tiếp bằng `python3` từ gốc repo.
