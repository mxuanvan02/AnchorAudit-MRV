#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Do KHOANG TRANG DOC lon nhat cua moi trang PDF (bang PIL, khong uoc luong).

Dung de bat loi 'muc trong': heading bi mo coi vi bang [!h] bi day sang trang khac,
khien GIUA trang xuat hien khoang trang lon trong khi van con chu phia duoi.

PHEU PHAN BIET (bat buoc, neu khong gate bao duong tinh gia):
  khe co CHU nam phia duoi  -> giua trang -> LOI THAT -> exit 1
  khe khong co chu phia duoi -> trang ket thuc som (\clearpage truoc phu luc,
                               trang cuoi cua bai) -> BINH THUONG -> chi bao tin
Chay: python3 experiments/measure_page_whitespace.py <pdf>
"""
from __future__ import annotations
import subprocess, sys, os, glob, re

def measure(pdf: str, dpi: int = 100):
    out = "/tmp/ws_" + os.path.basename(pdf).replace(".pdf", "")
    for f in glob.glob(out + "*.png"):
        os.remove(f)
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", pdf, out],
                   capture_output=True, check=True)
    from PIL import Image
    rows = []
    for p in sorted(glob.glob(out + "*.png")):
        im = Image.open(p).convert("L")
        w, h = im.size
        px = im.load()
        # voi moi dong y: co phai trang (gan nhu het pixel sang)?
        dark = []
        for y in range(h):
            c = 0
            for x in range(0, w, 4):          # lay mau cach 4 pixel cho nhanh
                if px[x, y] < 200:
                    c += 1
            dark.append(c)
        # tim khoang trang doc dai nhat (o giua trang, bo le tren/duoi)
        best = cur = 0
        y0 = y1 = 0
        st = None
        for y in range(int(h * 0.08), int(h * 0.94)):
            if dark[y] == 0:
                if st is None:
                    st = y
                cur = y - st + 1
                if cur > best:
                    best, y0, y1 = cur, st, y
            else:
                st = None; cur = 0
        nchar = sum(1 for d in dark if d > 0)
        # CO dong chu nao nam DUOI khe khong? Day la pheu phan biet loi that:
        #   co chu duoi khe  -> heading/bang bi tach, khe GIUA trang  => LOI THAT (FAIL)
        #   khong co chu     -> trang ket thuc som (clearpage, trang cuoi) => BINH THUONG
        # Chi quet trong VUNG CHU (toi 0.94h): neu quet den het trang thi so trang o
        # chan trang va running head bi dem la 'chu duoi khe' -> bao duong tinh gia
        # (da mac loi nay: 4 trang ket thuc som bi gan nhan GIUA TRANG).
        below = sum(1 for y in range(y1 + 1, int(h * 0.94)) if dark[y] > 0)
        rows.append((os.path.basename(p), nchar, best, best * 25.4 / dpi,
                     y0 * 25.4 / dpi, y1 * 25.4 / dpi, below))
    return rows

def main():
    pdf = sys.argv[1] if len(sys.argv) > 1 else "paper2_vi_submission/main.pdf"
    if not os.path.exists(pdf):
        raise SystemExit(f"khong tim thay PDF: {pdf} — build truoc khi chay gate nay")
    rows = measure(pdf)
    print(f"{'trang':<26}{'dong co chu':>12}{'khe lon nhat':>16}{'y0..y1 (cm)':>18}{'chu duoi khe':>14}")
    mid = []    # khe GIUA trang: co chu phia duoi -> loi that
    tail = []   # khe CUOI trang: trang ket thuc som -> binh thuong
    for name, nchar, best_px, best_mm, y0, y1, below in rows:
        if best_mm <= 25:
            continue
        kind = "GIUA TRANG <<< LOI" if below > 3 else "cuoi trang (ok)"
        print(f"  {name:<24}{nchar:>12}{best_mm:>13.1f} mm{y0:>9.1f}..{y1:.1f}{below:>11}{kind:>20}")
        (mid if below > 3 else tail).append((name, best_mm))
    print(f"\n  khe GIUA trang (loi that): {len(mid)}/{len(rows)}"
          + (f" -> {', '.join(n for n, _ in mid)}" if mid else ""))
    print(f"  khe CUOI trang (trang ket thuc som, binh thuong): {len(tail)}/{len(rows)}")
    if mid:
        print("  -> FAIL: heading/bang bi tach giua trang, phai sua")
    return 1 if mid else 0

if __name__ == "__main__":
    sys.exit(main())
