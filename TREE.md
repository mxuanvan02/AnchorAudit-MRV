# Cay lam viec — thu muc nao SONG, thu muc nao chet

Doc file nay TRUOC khi sua bat cu thu gi. Da co vong sua sua vao file mo coi
(khong duoc build) ma moi gate deu xanh, nen chu sua khong bao gio vao PDF.

## 4 GOC build that (moi goc sinh mot PDF)

| goc | PDF | trang |
|---|---|---|
| `paper2_vi_submission/main.tex` | `main.pdf` | 37 (gop ca phu luc) — **ban nop** |
| `paper2_vi_submission/supplementary_body.tex` | (nham trong main) | — |
| `paper2_hujos/main_hujos.tex` | `main_hujos.pdf` | 22 |
| `paper2_hujos/supplementary.tex` | `supplementary.pdf` | 14 |

## Symlink (ly do 3 thu muc thuc ra la mot cay)

- `paper2_hujos/blocks` -> `../paper2/blocks`  (noi dung than bai dung chung)
- `paper2_hujos/preamble.tex` -> `../paper2_vi_submission/preamble.tex`
- `paper2_hujos/refs.bib` -> `../paper2_vi_submission/refs.bib`

He qua: sua `paper2/blocks/*.tex` la sua ca ban EN. Sua `paper2_vi_submission/preamble.tex`
la sua ca ban EN.

## Abstract nam o dau (de khong sua nham)

- EN: **inline** trong `paper2_hujos/main_hujos.tex` (khoi `hujosabstract`) va trong
  `paper2_vi_submission/main.tex`. Khong nam trong `paper2/blocks/00_title_abstract.tex`
  (file do mo coi, da chuyen vao `_archive/dead_tex/`).
- VI: `paper2_hujos/abstract_vi.tex` va `paper2_vi_submission/main.tex`.

## Bang (tables)

- Bang SONG cua ban EN: `paper2_hujos/tables/*.tex`, sinh boi `make_tables_anchored.py`.
- `paper2/tables/*.tex` sinh boi `make_tables_paper2.py` = cay cu, khong duoc \input.
- Bang ban nop VI: `paper2_vi_submission/tab_*.tex`.

## Kiem tra truoc khi sua

```bash
python3 experiments/check_no_orphan_tex.py --list   # file nao thuoc goc nao
bash check_all.sh                                   # tat ca gate
```

## Hien trang thu muc

| ten | loai | kich thuoc |
|---|---|---|
| CHECKPOINT_20261003.md | file | 16K |
| DESIGN_VN.md | file | 12K |
| NOTES_MRV.md | file | 16K |
| PROBLEM_VN_2026.md | file | 24K |
| PROPOSAL.md | file | 28K |
| PROPOSAL_MRV_COST.md | file | 16K |
| PROPOSAL_TWIN_ATTESTED.md | file | 12K |
| REFERENCES.md | file | 24K |
| STATUS.md | file | 16K |
| THEORY.md | file | 8.0K |
| UPGRADE_FINDINGS.md | file | 12K |
| _archive | DIR  | 40M |
| _backups | DIR  | 3.1M |
| data | DIR  | 2.1M |
| experiments | DIR  | 980K |
| figures | DIR  | 2.5M |
| outputs | DIR  | 4.3M |
| paper | DIR  | 1.5M |
| paper2 | DIR  | 677K |
| paper2_hujos | DIR  | 4.6M |
| paper2_vi_submission | DIR  | 2.5M |
| references_verified.json | file | 8.0K |
| refs | DIR  | 4.1M |
| response_to_reviewers.md | file | 16K |
| response_to_reviewers.pdf | file | 48K |
| src | DIR  | 240K |
| tests | DIR  | 120K |
