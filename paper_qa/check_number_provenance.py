#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""GATE: moi con so KET QUA trong ban thao phai truy nguon duoc ve outputs/.

=== VI SAO CO GATE NAY ===
Loi nang nhat cua vong sua nay khong phai loi cong thuc, ma la: mot muc phu luc viet
9 con so ve tan suat cua mot gia thiet, trong do 4 so khong nam trong bat ky artifact
nao (da quet repo, thu muc tam va toan bo lich su git), con 5 so kia chi ton tai trong
mot file ket qua tam ma script sinh ra no da mat. Ban thao vi the "bao cao" mot phep do
ma khong ai tai lap lai duoc, trong khi thu tra loi lai hua moi con so deu do pipeline
cong khai sinh ra. Cac gate cu khong bat duoc vi chung kiem tra tinh nhat quan GIUA HAI
BAN va cac claim DA DUOC KHAI BAO; khong gate nao hoi "co so nao duoc khai ma khong co
nguon khong".

=== LUAT ===
Moi so trong *.tex cua ban thao, sau khi (a) chuan hoa dau thap phan LaTeX {,} -> .,
(b) loai cac con so THUOC VE DANG THUC CHU KHONG PHAI KET QUA, phai khop voi it nhat
mot so trong outputs/*.csv|json theo DUNG SO CHU SO THAP PHAN cua no (khop co lam tron,
vi CSV giu 4.8699 trong khi bai in 4.87).

So bi loai vi la "so cua dang thuc":
  - nam 19xx/20xx; so nguyen <= 20 khong kem %
  - be rong cot / kich thuoc hinh: p{3.00cm}, width=0.9\linewidth, \hspace{2.5pt}
  - so cua \label/\ref/\@namedef (danh muc tham chieu che sinh)
  - so trong comment LaTeX va trong supplementary_stubs.tex (aux sinh tu dong)
  - hang so vat ly/quy uoc khai bao trong ALLOW, kem ly do cua tung muc

=== TU KIEM (bat buoc) ===
--self-test bom 3 so gia vao file tam; gate PHAI bat duoc ca 3. Gate khong co negative
control thi khong dang tin.

Chay:  python3 experiments/check_number_provenance.py [--self-test] [--verbose]
"""
from __future__ import annotations

import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX_DIRS = ["paper2_vi_submission", "paper2_hujos", "paper2"]
OUT = ROOT / "outputs"
SKIP_FILES = ("supplementary_stubs.tex",)          # aux sinh tu dong, so cua no la \ref

# Hang so khong phai ket qua do. Moi muc bat buoc co ly do; neu khong day chi la
# cho de giau mot con so khong nguon.
ALLOW = {
    "15": "nguong AWD 15 cm duoi mat ruong (quy uoc Safe-AWD; QD 4801 khong dinh gia tri nay)",
    "72": "nguong 3 ngay = 72 gio (QD 4801, Phu luc 1: 'it nhat 3 ngay')",
    "3": "it nhat 3 ngay khong tuoi lai (QD 4801)",
    "5": "tau_0 = 5 mm, nguong tuyet doi dung lam moc tham chieu",
    "2": "delta_rel = 2%, dung sai cua dong ho bom",
    "0.5": "p = 0.5, he so depletable cua FAO-56",
    "1.1": "can duoi toc do sut lun cm/nam (Minderhoud 2017, DOI 10.1088/1748-9326/aa7146)",
    "2.5": "can tren toc do sut lun cm/nam (Minderhoud 2017)",
    "5.5": "do dich 5 nam x 1.1 cm/nam",
    "12.5": "do dich 5 nam x 2.5 cm/nam",
    "37": "5.5/15 = 37% cua nguong, va so trang ban VI",
    "83": "12.5/15 = 83% cua nguong",
    "0.7": "can duoi he so lech mua tai ruong (CFG_REAL trong reality_gap_probe.py)",
    "1.4": "can tren he so lech mua tai ruong (CFG_REAL)",
    "0.35": "bien do nhieu mua mm (CFG_REAL)",
    "0.60": "can duoi eta trong luoi kiem toan (S17)",
    "0.75": "eta giua trong luoi kiem toan (S17)",
    "0.85": "can tren eta trong dai sinh ruong (S20)",
    "1.00": "eta tren trong luoi kiem toan (S17)",
    "22": "so trang ban EN",
    "14": "so trang phu luc EN",
    "25": "nguong mm cua gate khoang trang",
    "500": "so gio mua trong cua so mo phong",
    "125": "the tich toi thieu (lit) cua ong do muc nuoc theo QD 4801",
    "36": "the tich toi thieu (lit) cua ong nho theo QD 4801",
    "20": "so (mm) cua xung tuoi quy uoc trong phep chieu tinh",
    "40": "so (mm) cua xung tuoi quy uoc trong phep chieu tinh",
    "0.05": "nguong epsilon cong bo trong phuong trinh (12)",
    "4801": "so hieu van ban phap luat (QD 4801/QD-BNNMT), khong phai ket qua do",
    "1490": "so hieu van ban phap luat (QD 1490/QD-TTg), khong phai ket qua do",
    "0051": "so hieu phuong phap luan VM0051 v1.1, khong phai ket qua do",
    "2025": "nam ban hanh van ban",
    "2026": "nam trong trich dan",
}

# Cac mau so THUOC VE DANG THUC — loai truoc khi quet
LAYOUT_PATTERNS = [
    r"\\begin\{tabular\}.*?\\(?:toprule|midrule|hline)",   # preamble cot p{3.00cm}
    r"p\{[^}]*\}",
    r"m\{[^}]*\}",
    r"width\s*=\s*[\d.]+[^,)\s]*",
    r"\\(?:hspace|vspace|rule|raisebox|kern|hskip|vskip)\*?\{[^}]*\}",
    r"\\fontsize\{[^}]*\}\{[^}]*\}",
    r"\\@namedef\{[^}]*\}\{[^}]*\}",
    r"\\(?:label|ref|eqref|autoref|Cref|cref|pageref)\{[^}]*\}",
    r"\\setlength\{[^}]*\}\{[^}]*\}",
    r"\\addtolength\{[^}]*\}\{[^}]*\}",
    r"\[\s*-?[\d.]+\s*(?:pt|mm|cm|ex|em)\s*\]",
    r"\\(?:textwidth|linewidth|columnwidth|textheight)",
]

NUM_RE = re.compile(r"(?<![\w.\\])(\d+(?:\.\d+)?)\s*(\\%|%)?")


# ---------------------------------------------------------------- outputs
def output_numbers() -> dict[int, set[str]]:
    """So chu so thap phan -> tap chuoi gia tri da lam tron o do chinh xac do.

    Lam tron theo do chinh xac cua con so trong bai (bai in 4.87 thi CSV 4.8699
    phai duoc chap nhan), va giu dang chuoi de khop dung.
    """
    vals: set[float] = set()
    for p in sorted(OUT.rglob("*")):
        if p.suffix.lower() not in (".csv", ".json", ".txt", ".md"):
            continue
        try:
            s = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in re.finditer(r"(?<![\w.])-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", s):
            try:
                vals.add(float(m.group(0)))
            except ValueError:
                pass
    table: dict[int, set[str]] = {}
    for d in range(0, 7):
        table[d] = {f"{v:.{d}f}" for v in vals if abs(v) < 1e12}
    return table


def provenanced(num: str, table: dict[int, set[str]]) -> bool:
    d = len(num.split(".")[1]) if "." in num else 0
    d = min(d, 6)
    try:
        return f"{float(num):.{d}f}" in table[d]
    except ValueError:
        return False

# ---------------------------------------------------------------- reachability
# Chi quet cac file VOI TOI DUOC tu mot main.tex that (tuc thuc su build ra PDF).
# Sua/quet file mo coi la nguon goc cua loi: sua thanh cong, gate xanh, nhung chu
# khong bao gio vao PDF (xem check_no_orphan_tex.py).
ROOTS = {
    "VI main": ROOT / "paper2_vi_submission/main.tex",
    "VI supp": ROOT / "paper2_vi_submission/supplementary_body.tex",
    "EN main": ROOT / "paper2_hujos/main_hujos.tex",
    "EN supp": ROOT / "paper2_hujos/supplementary.tex",
}
SKIP_DIRS = ("_archive", "_backups", "_flatten", "_repo_only_rescue",
             "_repo_cleanup_backup", "docx_build", "out_src", ".git",
             "paper2_hujos_backup", "qa_png", "qa_docx", "_dead")


def _walk(cur: Path, seen: set[Path]) -> None:
    if cur in seen or not cur.exists():
        return
    seen.add(cur)
    try:
        s = cur.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return
    for m in re.finditer(r"\\(?:input|include|subfile)\s*\{([^}]+)\}", s):
        t = m.group(1).strip()
        if not t.endswith(".tex"):
            t += ".tex"
        _walk((cur.parent / t).resolve(), seen)


def live_files() -> tuple[list[Path], list[Path]]:
    """(file song, file chet) trong cac thu muc ban thao."""
    reach: set[Path] = set()
    for rt in ROOTS.values():
        if rt.exists():
            _walk(rt.resolve(), reach)
    live, dead = [], []
    for d in TEX_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        for f in sorted(base.rglob("*.tex")):
            if any(x in str(f) for x in SKIP_DIRS) or f.name in SKIP_FILES:
                continue
            (live if f.resolve() in reach else dead).append(f)
    return live, dead


# ---------------------------------------------------------------- tex
def strip_layout(s: str) -> str:
    for pat in LAYOUT_PATTERNS:
        s = re.sub(pat, " ", s, flags=re.S)
    return s


def tex_numbers(path: Path) -> list[tuple[int, str, str]]:
    s = path.read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"(?<!\\)%.*", "", s)                 # bo comment
    s = s.replace("{,}", ".").replace("{.}", ".")    # dau thap phan LaTeX
    s = strip_layout(s)
    out: list[tuple[int, str, str]] = []
    for m in NUM_RE.finditer(s):
        num, pct = m.group(1), m.group(2)
        if re.fullmatch(r"(19|20)\d\d(\.\d+)?", num) and not pct:
            continue                                 # nam
        if not pct and "." not in num:
            try:
                if int(num) <= 20:
                    continue                         # so dem thong thuong
            except ValueError:
                continue
        line = s[: m.start()].count("\n") + 1
        ctx = re.sub(r"\s+", " ", s[max(0, m.start() - 60): m.start() + 40])
        out.append((line, num, ctx))
    return out


def tex_files_all() -> list[Path]:
    files = [f for d in TEX_DIRS for f in sorted((ROOT / d).rglob("*.tex"))
             if not any(x in str(f) for x in ["_archive", "_backups", "docx_build", "out_src"])]
    return [f for f in files if f.name not in SKIP_FILES]


def scan(files: list[Path], table: dict[int, set[str]], rel_to: Path) -> list[tuple[str, int, str, str]]:
    missing: list[tuple[str, int, str, str]] = []
    for f in files:
        try:
            rel = str(f.relative_to(rel_to))
        except ValueError:
            rel = f.name
        for line, num, ctx in tex_numbers(f):
            if num in ALLOW or provenanced(num, table):
                continue
            missing.append((rel, line, num, ctx))
    return missing


def run(verbose: bool = False) -> int:
    if not OUT.exists():
        print(f"!! khong co {OUT} — chay experiment truoc")
        return 1
    files, dead = live_files()
    if not files:
        print("!! khong tim thay file .tex song nao — kiem tra lai cac GOC")
        return 1
    table = output_numbers()
    if not table[0]:
        print("!! outputs/ khong co so nao — tu choi ket luan (gate ma khong co nguon thi vo nghia)")
        return 1

    total = sum(len(tex_numbers(f)) for f in files)
    missing = scan(files, table, ROOT)

    print("=== GATE nguon goc con so ===")
    print(f"  {len(files)} file .tex SONG (voi toi duoc tu 4 goc) | {total} so duoc quet")
    print(f"  bo qua {len(dead)} file chet/mo coi (khong build ra PDF nao): "
          f"{', '.join(f.name for f in dead[:4])}{'…' if len(dead) > 4 else ''}")
    print(f"  {len(ALLOW)} hang so khai bao trong ALLOW (hang so quy uoc/van ban phap luat)")
    print(f"  nguon: {OUT.relative_to(ROOT)} | {len(table[0])} gia tri nguyen doc duoc tu outputs/")
    if missing:
        print(f"\n  !!! {len(missing)} so KHONG truy nguon duoc ve outputs/:")
        seen: set[tuple[str, str]] = set()
        shown = 0
        for rel, line, num, ctx in missing:
            key = (rel, num)
            if key in seen:
                continue
            seen.add(key)
            shown += 1
            if shown <= 30:
                print(f"    {rel}:{line}  {num}   …{ctx}…")
        if shown > 30:
            print(f"    … va {shown - 30} cap (file, so) khac")
        print("\n  Cach xu ly tung so:")
        print("    (a) la ket qua do  -> ghi script sinh ra no vao experiments/ va commit outputs/")
        print("    (b) la hang so quy uoc -> them vao ALLOW kem ly do cu the")
        print("    (c) khong co nguon that -> BO khoi ban thao")
        return 1
    print("\nGATE PASS: moi so ket qua trong ban thao deu truy nguon duoc ve outputs/.")
    return 0


def self_test() -> int:
    """NEGATIVE CONTROL: bom so gia vao file tam -> gate PHAI bat duoc."""
    tmp = Path(tempfile.mkdtemp(prefix="prov_selftest_"))
    try:
        fake = tmp / "fake.tex"
        fake.write_text(
            "\\documentclass{article}\\begin{document}\n"
            "Ty le phat hien dat $91{,}3726\\%$ tren $4321$ nhat ky,\n"
            "voi do lech chuan $0{,}00431$ va $p=0{,}00021$.\n"
            "\\end{document}\n", encoding="utf-8")
        table = output_numbers()
        bad = scan([fake], table, tmp)
        nums = sorted({n for _, _, n, _ in bad})
        print("=== SELF-TEST (negative control) ===")
        print(f"  bom 4 so gia -> gate bat duoc {len(bad)} cho: {nums}")
        expect = {"91.3726", "4321", "0.00431", "0.00021"}
        lost = expect - set(nums)
        if lost:
            print(f"  !!! FAIL: gate LO MAT {sorted(lost)} — gate vo dung, khong duoc tin")
            return 1
        print("  PASS: gate bat duoc ca 4 so khong nguon, ke ca dang dau phay LaTeX {,}.")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    raise SystemExit(run(verbose="--verbose" in sys.argv))
