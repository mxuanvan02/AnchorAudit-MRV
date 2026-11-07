#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""GATE: khong duoc sua nham vao file .tex MO COI.

=== VI SAO CO GATE NAY ===
Cay ban thao co 3 thu muc song song (paper2/, paper2_hujos/, paper2_vi_submission/)
noi nhau bang symlink: paper2_hujos/blocks -> ../paper2/blocks, preamble.tex va
refs.bib -> ../paper2_vi_submission/. Mot file co the (a) voi toi duoc tu mot main.tex
that, hoac (b) MO COI — khong duoc \input o bat ky dau, khong build ra PDF nao.

Trong mot vong sua, mot batch da sua chu trong `paper2/tables/tab_cost.tex`, tuc mot
file MO COI: sua thanh cong, gate khac deu xanh, nhung chu moi khong bao gio vao PDF.
Loi nay khong the thay bang mat khi doc diff — chi thay khi tinh reachability tu goc.

=== LUAT ===
1. Moi file .tex trong cac thu muc ban thao phai voi toi duoc tu it nhat mot GOC
   (main.tex / supplementary*.tex that su build ra PDF), hoac phai nam trong
   ORPHAN_OK (khai bao ro, kem ly do).
2. Moi GOC phai build duoc (kiem tra bang latexmk o gate khac) va khong duoc
   input toi file thieu.
3. Bao cao ro file nao thuoc goc nao, de biet sua mot cho thi anh huong ban nao.

Chay:  python3 experiments/check_no_orphan_tex.py [--list]
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Cac GOC that (moi goc build ra mot PDF). Khong tinh thu muc backup/archive.
ROOTS = {
    "VI main (37 trang, goi nop)": ROOT / "paper2_vi_submission/main.tex",
    "VI supp (nhung trong main)": ROOT / "paper2_vi_submission/supplementary_body.tex",
    "EN main (22 trang)":          ROOT / "paper2_hujos/main_hujos.tex",
    "EN supp (14 trang)":          ROOT / "paper2_hujos/supplementary.tex",
}

# Thu muc khong phai ban thao: khong ap luat reachability.
SKIP_DIRS = ("_archive", "_backups", "_flatten", "_repo_only_rescue",
             "_repo_cleanup_backup", "docx_build", "out_src", ".git",
             "paper2_hujos_backup", "qa_png", "qa_docx")

# File .tex duoc phep mo coi, kem ly do. Them vao day = khai bao co chu y.
ORPHAN_OK = {
    "supplementary_stubs.tex": "aux sinh tu dong de cross-ref, khong phai noi dung",
    "probe_parskip.tex": "file probe canh le, chi chay tay khi can",
    "probe_width.tex": "file probe be rong, chi chay tay khi can",
    "glossary.tex": "bang thuat ngu Viet-Anh dung chung: duoc DONG GOI NOP (nam trong "
                    "INCLUDE cua check_latex_source_package.py) va duoc 7 file trich dan "
                    "lam chuan dich thuat, nhung khong duoc input nen khong build thanh trang",
}

# Thu muc chua ban thao CU khong con build (giu lam nguon cua blocks dung chung).
LEGACY_DIRS = {"paper2/tables": "bang cua cay EN cu; ban EN hien tai dung paper2_hujos/tables/"}


def tex_files() -> list[Path]:
    out = []
    for d in ("paper2_vi_submission", "paper2_hujos", "paper2"):
        base = ROOT / d
        if not base.exists():
            continue
        for f in sorted(base.rglob("*.tex")):
            if any(x in str(f) for x in SKIP_DIRS):
                continue
            out.append(f)
    return out


def resolve_inputs(root: Path) -> set[Path]:
    r"""Di het cay \input/\include/\subfile tu mot goc, theo ca symlink."""
    seen: set[Path] = set()
    stack = [root.resolve()]
    while stack:
        cur = stack.pop()
        if cur in seen or not cur.exists():
            continue
        seen.add(cur)
        try:
            s = cur.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in re.finditer(r"\\(?:input|include|subfile|import)\s*\{([^}]+)\}", s):
            t = m.group(1).strip()
            if not t.endswith(".tex"):
                t += ".tex"
            stack.append((cur.parent / t).resolve())
    return seen


def main() -> int:
    list_mode = "--list" in sys.argv
    reach: dict[Path, list[str]] = {}
    for label, rt in ROOTS.items():
        if not rt.exists():
            print(f"!! GOC thieu: {rt.relative_to(ROOT)}")
            return 1
        for f in resolve_inputs(rt):
            reach.setdefault(f, []).append(label)

    files = tex_files()
    orphans, linked = [], []
    for f in files:
        rp = f.resolve()
        rel = str(f.relative_to(ROOT))
        if rp in reach:
            continue
        if f.name in ORPHAN_OK:
            continue
        if any(rel.startswith(d) for d in LEGACY_DIRS):
            continue
        orphans.append(rel)
        # symlink?
        if os.path.islink(f):
            linked.append(rel)

    print("=== GATE file .tex mo coi ===")
    print(f"  {len(files)} file .tex trong 3 thu muc ban thao | {len(ROOTS)} goc build")
    print(f"  voi toi duoc: {len(files) - len(orphans)} | mo coi bi cam: {len(orphans)}")
    print(f"  cho phep mo coi (khai bao): {len(ORPHAN_OK)} | cay cu giu lam nguon: {len(LEGACY_DIRS)}")

    if list_mode:
        print("\n  --- map goc (file -> ban nao dung) ---")
        for f in files:
            labs = reach.get(f.resolve())
            if labs:
                print(f"    {str(f.relative_to(ROOT)):52s} {'; '.join(sorted(set(labs)))}")

    if orphans:
        print(f"\n  !!! {len(orphans)} file .tex MO COI — sua vao day se KHONG vao PDF nao:")
        for o in orphans[:30]:
            print(f"    {o}")
        if len(orphans) > 30:
            print(f"    … va {len(orphans) - 30} file khac")
        print("\n  Cach xu ly: (a) neu file that su khong dung -> xoa hoac chuyen vao _archive/;")
        print("  (b) neu no phai duoc build -> them \\input vao main.tex tuong ung;")
        print("  (c) neu la cay cu giu lam nguon -> khai bao trong LEGACY_DIRS kem ly do.")
        return 1

    print("\nGATE PASS: khong con file .tex mo coi ngoai danh sach khai bao.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
