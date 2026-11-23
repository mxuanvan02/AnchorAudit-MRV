import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['mathtext.fontset'] = 'stix'

fig, ax = plt.subplots(figsize=(11.5, 6.4), dpi=300)
ax.set_xlim(0, 11.5)
ax.set_ylim(0, 6.4)
ax.axis('off')

def box(x, y, w, h, title, body="", fc="white", ec="#222222", lw=1.2, title_fs=10, body_fs=9, title_color="#111111", title_y=0.68, body_y=0.30):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06,rounding_size=0.08",
                       facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3)
    ax.add_patch(p)
    if body:
        ax.text(x + w/2, y + h*title_y, title, ha='center', va='center',
                fontsize=title_fs, fontweight='bold', color=title_color, zorder=4)
        ax.text(x + w/2, y + h*body_y, body, ha='center', va='center',
                fontsize=body_fs, color="#222222", zorder=4)
    else:
        ax.text(x + w/2, y + h/2, title, ha='center', va='center',
                fontsize=title_fs, fontweight='bold', color=title_color, zorder=4)

def arrow(x1, y1, x2, y2, color="#222222", ls="-", lw=1.3):
    arr = FancyArrowPatch((x1, y1), (x2, y2),
                          arrowstyle="-|>,head_length=6,head_width=3.5",
                          color=color, linestyle=ls, linewidth=lw, zorder=5)
    ax.add_patch(arr)

# --- Left column: Inputs ---
ax.text(1.35, 6.12, "ĐẦU VÀO", ha='center', va='center', fontsize=10.5, fontweight='bold', color="#333333")
box(0.25, 4.75, 2.2, 0.92, "Nhật ký nông dân $L$", r"$\{(t_i, u_i, \gamma_i)\}$", fc="#F7F9FC", ec="#2C3E50")
box(0.25, 3.35, 2.2, 0.92, "Khí tượng ERA5", r"$T, RH$, gió, $P$ (theo giờ)", fc="#F7F9FC", ec="#2C3E50")
box(0.25, 1.95, 2.2, 0.92, "Tham số đất & cây", r"$\mathrm{FC}, \mathrm{WP}, K_c, \eta$", fc="#F7F9FC", ec="#2C3E50")
box(0.25, 0.45, 2.2, 1.05, r"Bản ghi thiết bị $\mathcal{G}$", r"$\{(t_j, u_j, \sigma_j)\}$" + "\n(append-only, có chữ ký)", fc="#FFF8E7", ec="#B07D18")

# --- Middle: FAO-56 physical replay ---
box(3.05, 2.95, 2.05, 1.70, "Cân bằng nước\nFAO-56 theo giờ",
    r"$w_{t+1}, d_t$" + "\nphát lại quỹ đạo\n" + r"$(\hat{w}_t, \hat{d}_t)$",
    fc="#E8F6EC", ec="#1E6B3A", lw=1.4, title_fs=9.8, body_fs=8.8, title_y=0.72, body_y=0.30)

# Arrows from inputs to FAO-56
arrow(2.45, 5.10, 3.05, 4.18)
arrow(2.45, 3.81, 3.05, 3.81)
arrow(2.45, 2.41, 3.05, 3.38)

# --- Red proposed audit region ---
red_rect = FancyBboxPatch((5.55, 0.30), 5.75, 5.75, boxstyle="round,pad=0.05,rounding_size=0.10",
                          facecolor="#FFF5F5", edgecolor="#C0392B", linewidth=1.8, zorder=1)
ax.add_patch(red_rect)
ax.text(8.42, 5.82, "TẦNG KIỂM TOÁN ĐỀ XUẤT (SO SÁNH BA TẦNG PHÒNG THỦ)",
        ha='center', va='center', fontsize=10, fontweight='bold', color="#B02A1E", zorder=2)

# Three parallel defense tiers
box(5.85, 4.45, 2.95, 0.98, "Tầng 1: Mô hình đơn cấu hình",
    r"$\theta_0$, ngưỡng $\tau_0=5$ mm; lọc $V_1, V_4, V_5$",
    fc="white", ec="#333333", title_fs=9.3, body_fs=8.5)

box(5.85, 3.10, 2.95, 1.04, r"Tầng 2: Bộ phát hiện bền vững",
    r"$V_{\mathrm{rob}}(L)=\bigcap_{\theta\in\Theta}V_\theta(L)$" + "\n" + r"ngưỡng co giãn $\tau(N_{\mathrm{event}})$",
    fc="white", ec="#333333", title_fs=9.3, body_fs=8.4, title_y=0.73, body_y=0.30)

box(5.85, 1.68, 2.95, 1.06, r"Tầng 3: Neo theo thiết bị",
    r"Đối chiếu $L$ với $\mathcal{G}$:" + "\n" + r"$\Delta^-, \Delta^+, \Delta_{\mathrm{depth}}$",
    fc="#FFFDF6", ec="#B07D18", lw=1.4, title_fs=9.3, body_fs=8.5, title_y=0.72, body_y=0.30)

# Analysis note box at bottom inside red region
box(5.85, 0.50, 5.20, 0.86, r"Phân tích tấn công dịch thời điểm (Mệnh đề 1–2) & Kiểm tra ngoài $\Theta$",
    "Vật lý ràng buộc quỹ đạo nước; bản ghi thiết bị đối chiếu ở tầng thời gian",
    fc="#EAF4FB", ec="#2471A3", lw=1.1, title_fs=9.0, body_fs=8.4, title_color="#1A5276")

# Output box on the right inside red region
box(9.20, 2.50, 1.85, 2.25, "ĐẦU RA\nKIỂM TOÁN",
    "• Đề xuất chuyển\n  thẩm định\n• Không kết luận\n\n(Không tự chấp nhận\nhay từ chối tín chỉ)",
    fc="#E8F6EC", ec="#1E6B3A", lw=1.4, title_fs=9.5, body_fs=8.1, title_color="#145A32", title_y=0.80, body_y=0.35)

# Arrows from FAO-56 to Tier 1 and Tier 2
arrow(5.10, 4.10, 5.85, 4.92)
arrow(5.10, 3.68, 5.85, 3.62)

# Arrow from L directly to Tier 3 (cleanly routed from right edge of L, avoiding ĐẦU VÀO)
ax.plot([2.45, 2.72, 2.72, 5.32, 5.32], [5.45, 5.45, 5.82, 5.82, 2.40], color="#2C3E50", lw=1.15, ls="--", zorder=2)
arrow(5.32, 2.40, 5.85, 2.40, color="#2C3E50", ls="--", lw=1.15)
ax.text(4.02, 5.96, "nhật ký $L$ đối chiếu trực tiếp", ha='center', va='center', fontsize=8.4, color="#2C3E50", style='italic')

# Arrow from device log G directly to Tier 3
ax.plot([2.45, 5.32, 5.32], [0.97, 0.97, 1.98], color="#B07D18", lw=1.35, ls="-", zorder=2)
arrow(5.32, 1.98, 5.85, 1.98, color="#B07D18", lw=1.35)
ax.text(3.90, 1.13, r"đối chiếu bản ghi $\mathcal{G}$", ha='center', va='center', fontsize=8.5, color="#9A6B0E", style='italic')

# Arrows from 3 tiers to Output
arrow(8.80, 4.92, 9.20, 4.12)
arrow(8.80, 3.62, 9.20, 3.62)
arrow(8.80, 2.20, 9.20, 3.05)

# Footer note
ax.text(8.42, 0.08, "Vùng khung đỏ = các thành phần đề xuất và đánh giá trong nghiên cứu",
        ha='center', va='center', fontsize=8.8, color="#B02A1E", style='italic')

plt.tight_layout(pad=0.2)
out = "figures/fig_architecture.png"
plt.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
print("Saved:", out)
