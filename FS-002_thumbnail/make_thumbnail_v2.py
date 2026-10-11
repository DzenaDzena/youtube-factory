"""FS-002 thumbnail v2 (1280x720), layout modelled on competitor formula:
dark velvet bg, big jewel close-up + cut-out portrait, 2-line gold serif hook.
Usage: python3 make_thumbnail_v2.py "LINE 1" "LINE 2" out.jpg
Assets are downloaded once into ./assets (all rights-clear per MANIFEST.csv):
  portrait: LAC/McKague 1959, Public domain (Commons, S119A)
  jewel:    Cleveland Museum of Art Open Access CC0, parure 2001.156
"""
import os, sys, subprocess, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

W, H = 1280, 720
HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "assets"); os.makedirs(A, exist_ok=True)
ASSETS = {
    "portrait.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/11/Queen_Elizabeth_II_official_portrait_for_1959_tour_%28retouched%29_%28cropped%29_%283-to-4_aspect_ratio%29.jpg",
    "jewel.jpg": "https://openaccess-cdn.clevelandart.org/2001.156/2001.156_print.jpg",
}
for n, u in ASSETS.items():
    p = os.path.join(A, n)
    if not os.path.exists(p):
        subprocess.run(["curl", "-sS", "-m", "120", "-A", "youtube-factory/1.0", "-o", p, u], check=True)

l1, l2, out = sys.argv[1], sys.argv[2], sys.argv[3]

# --- velvet background -------------------------------------------------
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
d = np.sqrt(((xx - W * 0.45) / W) ** 2 + ((yy - H * 0.4) / H) ** 2)
base = np.clip(1.15 - d * 1.7, 0.12, 1)
rng = np.random.default_rng(3)
folds = np.sin(xx / 70 + np.sin(yy / 160) * 3) * 0.07 + np.sin(xx / 23 + yy / 90) * 0.03
v = np.clip(base + folds, 0, 1)[..., None]
bg = np.concatenate([v * 105 + 18, v * 8 + 4, v * 22 + 8], axis=2)
bg = Image.fromarray(np.clip(bg + rng.normal(0, 2, bg.shape), 0, 255).astype("uint8"))

# --- jewel: black background -> alpha by luminance ---------------------
j = Image.open(os.path.join(A, "jewel.jpg")).convert("RGB")
j = j.crop((500, 150, 2900, 2650))  # necklace + pendant, drop earrings
j = j.resize((680, int(j.height * 680 / j.width)), Image.LANCZOS)
lum = np.asarray(j.convert("L")).astype(np.float32)
alpha = np.clip((lum - 18) / 70, 0, 1)
alpha = Image.fromarray((alpha * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.2))
j = ImageEnhance.Brightness(ImageEnhance.Contrast(j).enhance(1.25)).enhance(1.25)
glow = Image.new("RGB", bg.size, 0)
jx, jy = -20, -30
gl = Image.new("L", bg.size, 0); gl.paste(alpha, (jx, jy))
glow = Image.composite(Image.new("RGB", bg.size, (255, 190, 110)), glow, gl.filter(ImageFilter.GaussianBlur(40)))
bg = ImageChops.add(bg, glow.point(lambda x: int(x * 0.35)))
bg.paste(j, (jx, jy), alpha)

# --- portrait: flood-fill the blue backdrop from the edges -------------
p = Image.open(os.path.join(A, "portrait.jpg")).convert("RGB")
mark = p.copy()
for pt in [(x, 4) for x in range(4, 740, 60)] + [(4, y) for y in range(4, 450, 60)] + [(735, y) for y in range(4, 450, 60)]:
    ImageDraw.floodfill(mark, pt, (255, 0, 255), thresh=70)
m = np.asarray(mark)
cut = ((m[..., 0] == 255) & (m[..., 1] == 0) & (m[..., 2] == 255))
pm = Image.fromarray(((~cut) * 255).astype("uint8")).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.6))
ph = 690
pw = int(p.width * ph / p.height)
p = p.resize((pw, ph), Image.LANCZOS); pm = pm.resize((pw, ph), Image.LANCZOS)
p = ImageEnhance.Contrast(ImageEnhance.Color(p).enhance(1.15)).enhance(1.08)
px, py = W - pw + 40, H - ph
sh = Image.new("L", bg.size, 0); sh.paste(pm, (px, py))
bg = Image.composite(Image.new("RGB", bg.size, (0, 0, 0)), bg, sh.filter(ImageFilter.GaussianBlur(28)).point(lambda x: int(x * 0.6)))
bg.paste(p, (px, py), pm)

# --- bottom fade + hook text ------------------------------------------
grad = Image.new("L", bg.size, 0)
gd = ImageDraw.Draw(grad)
for y in range(H):
    gd.line([(0, y), (W, y)], fill=int(max(0, (y - H * 0.55) / (H * 0.45)) * 200))
bg = Image.composite(Image.new("RGB", bg.size, (6, 0, 4)), bg, grad)

font_path = os.path.join(HERE, "Cinzel.ttf")
def font(size):
    f = ImageFont.truetype(font_path, size); f.set_variation_by_axes([800]); return f

def gold_text(img, xy, s, size):
    f = font(size)
    mask = Image.new("L", img.size, 0); ImageDraw.Draw(mask).text(xy, s, font=f, fill=255)
    x0, y0, x1, y1 = mask.getbbox()
    g = Image.new("RGB", img.size)
    gd2 = ImageDraw.Draw(g)
    for y in range(y0, y1 + 1):  # vertical gold gradient
        t = (y - y0) / max(1, y1 - y0)
        c = (int(255 - 40 * t), int(226 - 70 * t), int(140 - 80 * t))
        gd2.line([(0, y), (img.width, y)], fill=c)
    shadow = mask.filter(ImageFilter.GaussianBlur(7)).point(lambda x: int(x * 1.0))
    img.paste(Image.new("RGB", img.size, (0, 0, 0)), (6, 8), shadow)
    outline = mask.filter(ImageFilter.MaxFilter(7))
    img.paste(Image.new("RGB", img.size, (30, 8, 0)), (0, 0), outline)
    img.paste(g, (0, 0), mask)

size = 98
for s, y in ((l1, 470), (l2, 575)):
    gold_text(bg, (50, y), s, size)
bg.save(out, quality=93)
