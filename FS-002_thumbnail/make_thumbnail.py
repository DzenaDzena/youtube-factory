"""FS-002 thumbnail 1280x720. Usage: python3 make_thumbnail.py portrait.jpg out.jpg"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

W, H = 1280, 720
src, out = sys.argv[1], sys.argv[2]
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
GOLD, WHITE = (255, 200, 60), (255, 255, 255)

bg = Image.new("RGB", (W, H), (14, 10, 40))
d = ImageDraw.Draw(bg)
for x in range(W):  # dark blue -> deep purple horizontal gradient
    t = x / W
    d.line([(x, 0), (x, H)], fill=(int(14 + 30 * t), int(10 + 4 * t), int(40 + 25 * t)))

p = Image.open(src).convert("RGB")
pw = 660
p = p.resize((pw, int(p.height * pw / p.width)), Image.LANCZOS).crop((0, 0, pw, H))
p = ImageEnhance.Contrast(ImageEnhance.Color(p).enhance(1.25)).enhance(1.12)
mask = Image.new("L", (pw, H), 255)  # fade the left edge into the background
md = ImageDraw.Draw(mask)
for x in range(220):
    md.line([(x, 0), (x, H)], fill=int(255 * x / 220))
bg.paste(p, (W - pw, 0), mask)

def text(xy, s, size, fill, stroke=8):
    f = ImageFont.truetype(FONT, size)
    ImageDraw.Draw(bg).text(xy, s, font=f, fill=fill, stroke_width=stroke, stroke_fill=(0, 0, 0))

text((50, 60), "10 ROYAL", 120, WHITE)
text((50, 195), "JEWELS", 150, GOLD, 10)
text((50, 395), "SHE INHERITED", 78, WHITE)
text((50, 520), "...AND WHO WORE THEM FIRST", 40, GOLD, 5)
bg.save(out, quality=92)
