import matplotlib
matplotlib.use("TkAgg")  # برای پنجره تعاملی در ویندوز
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox, RadioButtons
from matplotlib.patches import Patch

# ---------- ساخت مخروط افقی روی محور X ---------- #
def make_cone(base_radius, length, x0):
    """
    base_radius : شعاع قاعده مخروط
    length      : طول مخروط روی محور X
    x0          : محل نوک مخروط روی محور X
    """
    u = np.linspace(0, length, 80)
    theta = np.linspace(0, 2*np.pi, 60)
    U, TH = np.meshgrid(u, theta)

    R = (base_radius / length) * U
    X = x0 + U
    Y = R * np.cos(TH)
    Z = R * np.sin(TH)
    return X, Y, Z


# ---------- رسم کل صحنه روی یک محور ---------- #
def draw_scene_on_ax(ax,
                     cone1_x0, cone1_length, cone1_radius,
                     cone2_x0, cone2_length, cone2_radius,
                     tissue_center, tissue_thickness, tissue_radius,
                     g1=0.78, g2=0.97):

    ax.cla()

    # بافت: مرکز و ضخامت → x_in و x_out
    x_in  = tissue_center - tissue_thickness/2
    x_out = tissue_center + tissue_thickness/2

    # --- مخروط ۱ (قبل از بافت) ---
    if cone1_length > 0:
        X1, Y1, Z1 = make_cone(cone1_radius, cone1_length, cone1_x0)
        ax.plot_surface(X1, Y1, Z1,
                        color="tab:blue", alpha=0.7,
                        linewidth=0, edgecolor="none", shade=True)

    # --- مخروط ۲ (بعد از بافت) ---
    if cone2_length > 0:
        X2, Y2, Z2 = make_cone(cone2_radius, cone2_length, cone2_x0)
        ax.plot_surface(X2, Y2, Z2,
                        color="tab:red", alpha=0.5,
                        linewidth=0, edgecolor="none", shade=True)

    # --- بلوک بافت سه‌بعدی ---
    r = max(tissue_radius, cone1_radius, cone2_radius) * 1.1
    r = max(r, 0.2)

    y = np.linspace(-r, r, 20)
    z = np.linspace(-r, r, 20)
    Yp, Zp = np.meshgrid(y, z)

    # ورودی و خروجی بافت
    Xin  = np.full_like(Yp, x_in)
    Xout = np.full_like(Yp, x_out)
    ax.plot_surface(Xin,  Yp, Zp, color="lightgray", alpha=0.55, linewidth=0)
    ax.plot_surface(Xout, Yp, Zp, color="lightgray", alpha=0.55, linewidth=0)

    # بالا و پایین
    Z_top    = np.full_like(Yp, r)
    Z_bottom = np.full_like(Yp, -r)
    X_topline      = np.linspace(x_in, x_out, 20)
    X_top, Y_top   = np.meshgrid(X_topline, y)
    ax.plot_surface(X_top, Y_top, Z_top,    color="lightgray", alpha=0.55, linewidth=0)
    ax.plot_surface(X_top, Y_top, Z_bottom, color="lightgray", alpha=0.55, linewidth=0)

    # چپ و راست
    Y_left  = np.full_like(Zp, -r)
    Y_right = np.full_like(Zp,  r)
    X_side, Z_side = np.meshgrid(X_topline, z)
    ax.plot_surface(X_side, Y_left,  Z_side, color="lightgray", alpha=0.55, linewidth=0)
    ax.plot_surface(X_side, Y_right, Z_side, color="lightgray", alpha=0.55, linewidth=0)

    # --- تنظیمات محور ---
    x_min = min(cone1_x0, x_in) - 0.2
    x_max = max(cone2_x0 + cone2_length, x_out) + 0.2

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-r, r)
    ax.set_zlim(-r, r)
    ax.set_box_aspect((x_max - x_min, 2*r, 2*r))

    ax.set_facecolor("white")
    ax.grid(False)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.view_init(elev=15, azim=-60)

    # Legend ثابت (برای توضیح مخروط‌ها و بافت)
    legend_handles = [
        Patch(color="tab:blue",  label=f"Before tissue (g ≈ {g1:.2f})"),
        Patch(color="tab:red",   label=f"After tissue (g ≈ {g2:.2f})"),
        Patch(color="lightgray", label="Tissue block"),
    ]
    ax.legend(handles=legend_handles, loc="upper right")


# ---------- شکل اصلی و اسلایدرها ---------- #
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')

# جا برای اسلایدرها و ویجت‌ها
plt.subplots_adjust(left=0.08, right=0.97, top=0.9, bottom=0.3)

# مقدار اولیه
init_cone1_x0, init_cone1_length, init_cone1_radius = -1.0, 1.0, 0.7
init_tissue_center, init_tissue_thick, init_tissue_radius = 0.15, 0.3, 0.7
init_cone2_x0, init_cone2_length, init_cone2_radius = init_tissue_center + init_tissue_thick/2, 1.2, 0.35
g1, g2 = 0.78, 0.97

# رسم اولیه
draw_scene_on_ax(
    ax,
    init_cone1_x0, init_cone1_length, init_cone1_radius,
    init_cone2_x0, init_cone2_length, init_cone2_radius,
    init_tissue_center, init_tissue_thick, init_tissue_radius,
    g1, g2
)

axcolor = 'lightgoldenrodyellow'

# محورهای اسلایدرهای هندسی
ax_c1x = fig.add_axes([0.08, 0.22, 0.35, 0.02], facecolor=axcolor)
ax_c1l = fig.add_axes([0.08, 0.19, 0.35, 0.02], facecolor=axcolor)
ax_c1r = fig.add_axes([0.08, 0.16, 0.35, 0.02], facecolor=axcolor)

ax_tc  = fig.add_axes([0.08, 0.13, 0.35, 0.02], facecolor=axcolor)
ax_tt  = fig.add_axes([0.08, 0.10, 0.35, 0.02], facecolor=axcolor)
ax_tr  = fig.add_axes([0.08, 0.07, 0.35, 0.02], facecolor=axcolor)

ax_c2x = fig.add_axes([0.55, 0.22, 0.35, 0.02], facecolor=axcolor)
ax_c2l = fig.add_axes([0.55, 0.19, 0.35, 0.02], facecolor=axcolor)
ax_c2r = fig.add_axes([0.55, 0.16, 0.35, 0.02], facecolor=axcolor)

ax_btn = fig.add_axes([0.55, 0.07, 0.12, 0.04])

# خود اسلایدرهای هندسی
s_c1x = Slider(ax_c1x, 'C1 x0',   -3.0, 0.0,  valinit=init_cone1_x0)
s_c1l = Slider(ax_c1l, 'C1 len',  0.05, 3.0,  valinit=init_cone1_length)
s_c1r = Slider(ax_c1r, 'C1 R',    0.05, 2.0,  valinit=init_cone1_radius)

s_tc  = Slider(ax_tc,  'T center', -0.5, 2.0, valinit=init_tissue_center)
s_tt  = Slider(ax_tt,  'T thick',  0.05, 1.5, valinit=init_tissue_thick)
s_tr  = Slider(ax_tr,  'T radius', 0.1,  2.0, valinit=init_tissue_radius)

s_c2x = Slider(ax_c2x, 'C2 x0',   0.0,  3.0,  valinit=init_cone2_x0)
s_c2l = Slider(ax_c2l, 'C2 len',  0.05, 3.0,  valinit=init_cone2_length)
s_c2r = Slider(ax_c2r, 'C2 R',    0.05, 2.0,  valinit=init_cone2_radius)

btn_save = Button(ax_btn, 'Save', color='lightgray', hovercolor='0.8')

# ---------- متن شناور (در کل شکل، نه فقط روی محور) ---------- #
initial_text = "Forward scattering across tissue"
text_obj = fig.text(
    0.5, 0.94, initial_text,
    ha="center", va="top",
    fontsize=12, color="black"
)

# برای درگ‌کردن با ماوس
dragging = False
drag_offset = (0.0, 0.0)

def on_press(event):
    global dragging, drag_offset
    # چک می‌کنیم کلیک روی خود متن بوده یا نه
    contains, _ = text_obj.contains(event)
    if not contains:
        return
    dragging = True
    # تبدیل مختصات پیکسلی ماوس به مختصات نسبی شکل (۰ تا ۱)
    fig_coords = fig.transFigure.inverted().transform((event.x, event.y))
    x0, y0 = text_obj.get_position()
    drag_offset = (x0 - fig_coords[0], y0 - fig_coords[1])

def on_motion(event):
    global dragging
    if not dragging:
        return
    # مختصات جدید ماوس در مختصات شکل
    fig_coords = fig.transFigure.inverted().transform((event.x, event.y))
    new_x = fig_coords[0] + drag_offset[0]
    new_y = fig_coords[1] + drag_offset[1]
    text_obj.set_position((new_x, new_y))
    fig.canvas.draw_idle()

def on_release(event):
    global dragging
    dragging = False

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('button_release_event', on_release)

# ---------- ویجت‌های متن: TextBox + رنگ + اندازه ---------- #

# TextBox برای نوشتن متن دلخواه
ax_textbox = fig.add_axes([0.08, 0.02, 0.48, 0.05])
text_box = TextBox(ax_textbox, "Caption:", initial=initial_text)

def submit_text(new_text):
    text_obj.set_text(new_text)
    fig.canvas.draw_idle()

text_box.on_submit(submit_text)

# RadioButtons برای عوض کردن رنگ متن
ax_color = fig.add_axes([0.58, 0.02, 0.15, 0.12], facecolor="lightgray")
color_radio = RadioButtons(
    ax_color,
    ('black', 'red', 'blue', 'green', 'purple'),
    active=0
)

def change_color(label):
    text_obj.set_color(label)
    fig.canvas.draw_idle()

color_radio.on_clicked(change_color)

# Slider برای اندازه فونت
ax_fs = fig.add_axes([0.75, 0.02, 0.20, 0.02], facecolor=axcolor)
s_fs = Slider(ax_fs, "Size", 8, 24, valinit=12)

def change_fs(val):
    text_obj.set_fontsize(val)
    fig.canvas.draw_idle()

s_fs.on_changed(change_fs)

# ---------- تابع آپدیت ریل‌تایم صحنه (اسلایدرهای هندسی) ---------- #
def update(val=None):
    draw_scene_on_ax(
        ax,
        s_c1x.val, s_c1l.val, s_c1r.val,
        s_c2x.val, s_c2l.val, s_c2r.val,
        s_tc.val,  s_tt.val,  s_tr.val,
        g1, g2
    )
    fig.canvas.draw_idle()

for s in [s_c1x, s_c1l, s_c1r,
          s_tc, s_tt, s_tr,
          s_c2x, s_c2l, s_c2r]:
    s.on_changed(update)

# ---------- دکمه‌ی ذخیره نمودار ---------- #
def save(event):
    # یک شکل جدید برای خروجی تمیز
    fig2 = plt.figure(figsize=(6, 4))
    ax2 = fig2.add_subplot(111, projection='3d')
    draw_scene_on_ax(
        ax2,
        s_c1x.val, s_c1l.val, s_c1r.val,
        s_c2x.val, s_c2l.val, s_c2r.val,
        s_tc.val,  s_tt.val,  s_tr.val,
        g1, g2
    )
    # کپشن را روی شکل خروجی هم کپی می‌کنیم
    tx, ty = text_obj.get_position()
    fig2.text(
        tx, ty,
        text_obj.get_text(),
        ha=text_obj.get_ha(),
        va=text_obj.get_va(),
        fontsize=text_obj.get_fontsize(),
        color=text_obj.get_color()
    )

    fig2.savefig("forward_scattering_cones.png", dpi=300, bbox_inches='tight')
    plt.close(fig2)
    print("Saved as forward_scattering_cones.png")

btn_save.on_clicked(save)

plt.show()
