#!/usr/bin/env python3
"""gta6-meme-x-01 v5 — 'GTA 6 DELAY BINGO' flat bold bingo card.
Format segar (bukan tema jenuh '13 tahun + cuti sakit'), hantu make.fun
sebagai FREE SPACE di tengah, footer jual make.fun.
Output: meme-v5.png 1024x1024."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
ASSETS = "/home/hatch/workspace/makefun/gta6-meme-x-01-assets"
OUT = "/home/hatch/workspace/makefun/gta6-meme-x-01/meme-v5.png"


def font(path, sz):
    return ImageFont.truetype(path, sz)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


# --- background: Vice City sunset gradient ---
top = (59, 15, 102)
mid1 = (194, 24, 91)
mid2 = (255, 107, 74)
bot = (255, 210, 143)
img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)
for y in range(H):
    if y < H * 0.45:
        c = lerp(top, mid1, y / (H * 0.45))
    elif y < H * 0.75:
        c = lerp(mid1, mid2, (y - H * 0.45) / (H * 0.30))
    else:
        c = lerp(mid2, bot, (y - H * 0.75) / (H * 0.25))
    d.line([(0, y), (W, y)], fill=c)

DARK = (24, 8, 46)
CREAM = (255, 246, 232)
YELLOW = (255, 214, 64)
MAGENTA = (255, 45, 120)


def text_center(draw, cx, y, s, fnt, fill, stroke=0, stroke_fill=DARK):
    w = draw.textlength(s, font=fnt)
    draw.text((cx - w / 2, y), s, font=fnt, fill=fill,
              stroke_width=stroke, stroke_fill=stroke_fill)
    return w


# --- title ---
text_center(d, W // 2, 22, "GTA 6 DELAY BINGO", font(BOLD, 76),
            YELLOW, stroke=4)
text_center(d, W // 2, 112, "every square is true", font(REG, 30),
            (255, 255, 255), stroke=2)

# --- grid 3x3 ---
CELL = 240
GAP = 14
GX = (W - (3 * CELL + 2 * GAP)) // 2
GY = 168
cells = [
    "DELAYED AGAIN",
    "TRAILER 3 WHEN?",
    "ROCKSTAR SILENT",
    "LEAKED MAP AGAIN",
    None,  # FREE SPACE = ghost
    "STILL NO DATE",
    "PRE-ORDERED 2013",
    "MY AGENT GOT PAID",
    "2026? 2027?",
]


def wrap_lines(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def draw_cell_text(draw, x0, y0, text):
    """Shrink-to-fit: every line must fit the cell width, max 3 lines."""
    for sz in range(42, 24, -2):
        fnt = font(BOLD, sz)
        lines = wrap_lines(draw, text, fnt, CELL - 28)
        widths = [draw.textlength(ln, font=fnt) for ln in lines]
        if len(lines) <= 3 and max(widths) <= CELL - 28:
            break
    lh = int(sz * 1.18)
    total = lh * len(lines)
    y = y0 + (CELL - total) // 2
    for ln in lines:
        w = draw.textlength(ln, font=fnt)
        draw.text((x0 + (CELL - w) / 2, y), ln, font=fnt, fill=DARK)
        y += lh


for i, text in enumerate(cells):
    r, c_ = divmod(i, 3)
    x0 = GX + c_ * (CELL + GAP)
    y0 = GY + r * (CELL + GAP)
    fill = (255, 255, 255) if text is None else CREAM
    d.rounded_rectangle([x0, y0, x0 + CELL, y0 + CELL], radius=22,
                        fill=fill, outline=DARK, width=5)
    if text:
        draw_cell_text(d, x0, y0, text)

# --- diagonal bingo win line (cells 1 -> 5 -> 9), under the ghost ---
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
x1 = GX + CELL // 2
y1 = GY + CELL // 2
x2 = GX + 2 * (CELL + GAP) + CELL // 2
y2 = GY + 2 * (CELL + GAP) + CELL // 2
od.line([(x1, y1), (x2, y2)], fill=MAGENTA + (110,), width=16)
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
d = ImageDraw.Draw(img)

# --- FREE SPACE: ghost + FREE ---
ghost = Image.open(f"{ASSETS}/mark-1024.png")
cx0 = GX + (CELL + GAP)
cy0 = GY + (CELL + GAP)
g = ghost.resize((170, 170), Image.LANCZOS)
gx = cx0 + (CELL - 170) // 2
gy = cy0 + 8
if g.mode == "RGBA":
    img.paste(g, (gx, gy), g)
else:
    img.paste(g, (gx, gy))
d = ImageDraw.Draw(img)
text_center(d, cx0 + CELL // 2, cy0 + CELL - 48, "FREE", font(BOLD, 38),
            DARK)

# --- footer ---
text_center(d, W // 2, 918, "my agent already won on make.fun",
            font(BOLD, 44), (255, 255, 255), stroke=3)

img.save(OUT)
print("saved", OUT, img.size)
