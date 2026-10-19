#!/usr/bin/env python3
"""Build bản Word (HUJOS) từ main.tex — xử lý 3 bẫy của pandoc đã đo được:

1. pandoc KHÔNG hiểu môi trường algorithm2e → khối Thuật toán bị băm nát
   (đo trên bản build trước: mất caption/KwIn/nhánh If, toán trộn thứ tự).
   Giải pháp: thay bằng khối "Thuật toán 1" viết bằng enumerate + inline math
   (pandoc chuyển thành OMML đầy đủ), chỉ trong BẢN BIẾN THỂ đưa cho pandoc;
   bản LaTeX/PDF vẫn giữ algorithm2e ruled.
2. pandoc KHÔNG giải \ref/\eqref → DOCX hiện nguyên "[alg:gate]".
   Giải pháp: đọc main.aux (số thật từ lượt compile xelatex), thay \ref{k}
   bằng số đã resolve với đúng prefix theo namespace của key.
3. pandoc KHÔNG áp \renewcommand{\proofname} → "Proof." tiếng Anh lọt vào bài VN.
   Giải pháp: thay \begin{proof}...\end{proof} bằng "Chứng minh." + ∎.

Chạy: python3 build_docx.py   (yêu cầu đã compile main.tex ít nhất 1 lần để có aux)
"""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEX = HERE / "main.tex"
AUX = HERE / "main.aux"
OUT = HERE / "TwinGate_HUJOS_draft.docx"
REFDOC = HERE / "ref_hujos4.docx"   # heading/title gọn + TLTK 9pt theo HUJOS (ref2: 9pt/9pt spacing; ref3: 6/3pt nhưng heading to → 13 trang)
CSL = HERE / "vancouver-brackets.csl"
BIB = HERE / "refs.bib"
TMP = Path("/tmp/main_pandoc.tex")


def load_labels() -> dict[str, str]:
    """label -> số, đọc từ main.aux của lượt compile thật (không đoán)."""
    if not AUX.exists():
        sys.exit("main.aux không tồn tại — compile main.tex bằng xelatex trước.")
    labels: dict[str, str] = {}
    for m in re.finditer(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", AUX.read_text()):
        labels[m.group(1)] = m.group(2)
    return labels


def prefix_for(key: str) -> str:
    if key.startswith("eq:"):
        return "({num})"
    if key.startswith("tab:"):
        return "Bảng~{num}"
    if key.startswith("fig:"):
        return "Hình~{num}"
    if key.startswith("alg:"):
        return "Thuật toán~{num}"
    if key.startswith("sec:"):
        # NGUỒN ĐÃ CÓ chữ "Mục~" trước mọi \ref{sec:...} → prefix rỗng để
        # không thành "Mục Mục 6.6" (lỗi đo được trên bản build đầu tiên).
        return "{num}"
    if key.startswith("thm:"):
        return "Định lý~{num}"
    if key.startswith("cor:"):
        return "Hệ quả~{num}"
    return "{num}"


def resolve_refs(src: str, labels: dict[str, str]) -> tuple[str, list[str]]:
    missing: list[str] = []

    def sub_eqref(m):
        key = m.group(1)
        if key not in labels:
            missing.append(key)
            return m.group(0)
        return f"({labels[key]})"

    def sub_ref(m):
        key = m.group(2)
        if key not in labels:
            missing.append(key)
            return m.group(0)
        return prefix_for(key).replace("{num}", labels[key])

    src = re.sub(r"\\eqref\{([^}]+)\}", sub_eqref, src)
    src = re.sub(r"\\(ref|autoref)\{([^}]+)\}", sub_ref, src)
    return src, missing


ALG_PANDOC = r"""
\medskip
\noindent\textbf{Thuật toán 1.} \emph{Cổng an toàn và cơ chế gửi lại T2 trong một chu kỳ quyết định (24 giờ).}

\smallskip
\noindent\textbf{Đầu vào:} niềm tin trạng thái $\hat w$; tuổi dữ liệu $a$; ngân sách còn lại $B_{rem}$; tập ứng viên $\mathcal{U}=\{0;10;20;35\}$\,mm; tham số $\delta$, $H$, $f_\sigma$.

\noindent\textbf{Đầu ra:} phát một lệnh $u^{*}>0$, hoặc WITHHELD kèm lý do.

\begin{enumerate}
\item $\mathcal{U}_{aff} \leftarrow \{u \in \mathcal{U} : u \le B_{rem}\}$ (chỉ xét các lệnh còn đủ ngân sách).
\item Nếu đã bật ràng buộc mặn theo triều (ký hiệu C2, trình bày ở Mục~\ref{sec:salinity}) và giờ hiện tại nguồn không đủ ngọt:
  \begin{itemize}
  \item nếu trong chu kỳ còn giờ ngọt nào: chờ tới giờ ngọt đó (chờ không tiêu chu kỳ quyết định);
  \item ngược lại: \textbf{WITHHELD} với lý do ``nguồn mặn — không có con nước''.
  \end{itemize}
\item Với mỗi $u \in \mathcal{U}_{aff}$: mô phỏng tiến (rollout) bản sao số $H$ giờ với $u$ áp vào giờ đầu, được $\mu(u)$ và $\sigma_H = \sigma(a+H)$ theo phương trình~(\ref{eq:sigma}); tính $p(u) = \Phi\big(\tfrac{w_{hi}-\mu(u)}{\sigma_H}\big) - \Phi\big(\tfrac{w_{lo}-\mu(u)}{\sigma_H}\big)$.
\item $\mathcal{P} \leftarrow \{u \in \mathcal{U}_{aff} : p(u) \ge 1-\delta,\ u>0\}$.
\item Nếu $\mathcal{P} = \emptyset$: \textbf{WITHHELD} với lý do ``ràng buộc cơ hội không đạt'' (kể cả trường hợp $\sigma_H \ge \sigma^{*}$ theo Hệ quả~\ref{cor:sigma}).
\item $u^{*} \leftarrow \arg\min_{u \in \mathcal{P}} \big|\mu(u) - \tfrac{w_{lo}+w_{hi}}{2}\big|$ (lệnh đưa ruộng về gần tâm tập an toàn nhất); gửi $u^{*}$ qua downlink; đặt $k \leftarrow 1$.
\item Trong khi (không nhận được ACK) và ($\pi_k < \pi^{\dagger}$) và ($u^{*} \le B_{rem}$): cập nhật niềm tin $\pi_k \leftarrow 1-(1-\varphi)^k$; gửi lại $u^{*}$; $k \leftarrow k+1$ (chính sách T2).
\end{enumerate}
\medskip
"""


def transform(src: str) -> str:
    # 1) thay algorithm2e block bằng bản pandoc-safe
    m = re.search(r"\\begin\{algorithm\}.*?\\end\{algorithm\}", src, re.S)
    assert m, "không tìm thấy khối algorithm"
    src = src[: m.start()] + ALG_PANDOC + src[m.end() :]

    # 2) proof -> Chứng minh + ∎ (pandoc bỏ qua \renewcommand{\proofname})
    src = re.sub(r"\\begin\{proof\}", r"\\emph{Chứng minh.}", src)
    src = re.sub(r"\\end\{proof\}", r"\\hfill$\\square$", src)

    # 3) bỏ các lệnh pandoc không cần/không hiểu (không ảnh hưởng nội dung)
    src = re.sub(r"\\SetAlgorithmName\{[^}]*\}\{[^}]*\}\{[^}]*\}", "", src)
    src = src.replace("\\usepackage[ruled,vlined,linesnumbered]{algorithm2e}\n", "")
    return src


def main() -> int:
    src = TEX.read_text(encoding="utf-8")
    labels = load_labels()
    src = transform(src)
    src, missing = resolve_refs(src, labels)
    if missing:
        print("CẢNH BÁO: label chưa resolve:", sorted(set(missing)))
    TMP.write_text(src, encoding="utf-8")

    cmd = [
        "pandoc", str(TMP), "-f", "latex", "-t", "docx",
        f"--reference-doc={REFDOC}", f"--bibliography={BIB}",
        "--citeproc", f"--csl={CSL}", "-o", str(OUT),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[:2000])
        return r.returncode
    print("pandoc OK ->", OUT)

    # verify: không còn [label] chưa resolve, không còn "Proof."
    import zipfile
    with zipfile.ZipFile(OUT) as z:
        d = z.read("word/document.xml").decode("utf-8")
    text = re.sub(r"<[^>]+>", " ", d)
    problems = []
    for pat in [r"\[alg:", r"\[eq:", r"\[sec:", r"\[tab:", r"\[cor:", r"\bProof\."]:
        if re.search(pat, text):
            problems.append(pat)
    for probe in ["Thuật toán 1", "Đầu vào", "Đầu ra", "WITHHELD", "Chứng minh.",
                  "chờ tới giờ ngọt"]:
        if probe not in text:
            problems.append(f"THIẾU '{probe}'")
    if problems:
        print("VERIFY FAIL:", problems)
        return 1
    print("VERIFY OK: refs đã resolve, khối thuật toán nguyên vẹn, 'Proof.' đã dịch.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
