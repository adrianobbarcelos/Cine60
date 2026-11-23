"""Cine60 brand assets, drawn in code (Pillow): no AI masters, reproducible.

    py tools/brand/cine60_brand.py            (writes every asset below)
    py tools/brand/cine60_brand.py --proof    (also build/brand/cine60-proof.png)

The mark: a play triangle with motion echoes behind it, the in-between pictures smooth motion
draws (60 fps from 24). Cyan -> blue -> violet on a deep navy tile; a "60" badge from 96 px up.

Outputs (committed):
    src/refrata/resources/icon.png                 512 px window icon
    src/refrata/resources/icon.ico                 Windows icon, PNG entries 16..256
    src/refrata/resources/brand/icon-1024.png      master
    src/refrata/resources/brand/icon-256.png, icon-96.png
    src/refrata/resources/brand/symbol.png         the mark without the tile
    src/refrata/resources/brand/splash.png         launch window (340 x 300)
    src/refrata/resources/brand/about.jpg          Settings > About card (1536 x 560)
    packaging/windows/installer/art/wizard*.bmp    Inno Setup side images
    packaging/windows/installer/art/small*.bmp     Inno Setup header images
"""
from __future__ import annotations

import io
import struct
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
RES = ROOT / "src" / "refrata" / "resources"
ART = ROOT / "packaging" / "windows" / "installer" / "art"
ICO_SIZES = [16, 20, 24, 32, 40, 48, 64, 96, 128, 256]

NAVY_TOP = (16, 22, 44)
NAVY_BOTTOM = (7, 10, 22)
STOPS = [(0.0, (34, 211, 238)), (0.55, (59, 130, 246)), (1.0, (139, 92, 246))]   # cyan, blue, violet


def _lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def _gradient(t):
    for (t0, c0), (t1, c1) in zip(STOPS, STOPS[1:]):
        if t <= t1:
            return _lerp(c0, c1, (t - t0) / (t1 - t0))
    return STOPS[-1][1]


def _diag_gradient(size):
    """Cyan (top left) to violet (bottom right)."""
    w, h = size
    small = Image.new("RGB", (64, 64))
    px = small.load()
    for y in range(64):
        for x in range(64):
            px[x, y] = _gradient(min(1.0, max(0.0, (x * 1.4 + y * 0.6 - 20) / 100)))
    return small.resize(size, Image.BICUBIC)


def _vertical(size, top, bottom):
    w, h = size
    col = Image.new("RGB", (1, 256))
    for y in range(256):
        col.putpixel((0, y), _lerp(top, bottom, y / 255))
    return col.resize(size, Image.BICUBIC)


def _triangle(cx, cy, r):
    """A play triangle (pointing right) centred on its centroid, 'radius' r, corners rounded later."""
    return [(cx - r * 0.5, cy - r * 0.866), (cx + r, cy), (cx - r * 0.5, cy + r * 0.866)]


def _rounded_triangle_mask(size, cx, cy, r, round_px):
    """Triangle with rounded corners, crisp: the polygon shrunk by the corner radius, then grown back
    by a disc of that radius (a Minkowski sum: straight edges stay straight)."""
    m = Image.new("L", size, 0)
    d = ImageDraw.Draw(m)
    pts = _triangle(cx, cy, r - round_px * 2.0)
    d.polygon(pts, fill=255)
    for i in range(3):
        x0, y0 = pts[i]; x1, y1 = pts[(i + 1) % 3]
        d.line([x0, y0, x1, y1], fill=255, width=int(round_px * 2))
        d.ellipse([x0 - round_px, y0 - round_px, x0 + round_px, y0 + round_px], fill=255)
    return m


def mark(size, echoes=True, glow=True):
    """The symbol on transparency: two fading echoes behind a gradient play triangle."""
    S = size * 4                                  # supersampled, then reduced: smooth edges
    out = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    cx, cy, r = S * 0.58, S * 0.5, S * 0.33
    if echoes:
        for dx, a, k in ((0.34, 70, 0.80), (0.18, 140, 0.90)):
            m = _rounded_triangle_mask((S, S), cx - S * dx, cy, r * k, S * 0.035)
            layer = _diag_gradient((S, S)).convert("RGBA")
            layer.putalpha(m.point(lambda v, a=a: v * a // 255))
            out = Image.alpha_composite(out, layer)
    m = _rounded_triangle_mask((S, S), cx, cy, r, S * 0.04)
    if glow:
        g = Image.new("RGBA", (S, S), (110, 120, 255, 0))
        g.putalpha(m.filter(ImageFilter.GaussianBlur(S * 0.035)).point(lambda v: v * 110 // 255))
        out = Image.alpha_composite(out, g)
    # a dark gap between the echo and the main triangle reads better at small sizes
    gap = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    gap.putalpha(_rounded_triangle_mask((S, S), cx - S * 0.02, cy, r * 1.06, S * 0.05).point(lambda v: v * 120 // 255))
    out = Image.alpha_composite(out, Image.composite(Image.new("RGBA", (S, S), (6, 9, 20, 255)), Image.new("RGBA", (S, S), (0, 0, 0, 0)), gap.getchannel("A")))
    tri = _diag_gradient((S, S)).convert("RGBA")
    tri.putalpha(m)
    out = Image.alpha_composite(out, tri)
    hl = Image.new("RGBA", (S, S), (255, 255, 255, 0))
    edge = ImageChops.subtract(m, m.filter(ImageFilter.MinFilter(13)))
    top = _vertical((S, S), (255, 255, 255), (0, 0, 0)).convert("L")
    hl.putalpha(ImageChops.multiply(edge, top).point(lambda v: v * 150 // 255))
    out = Image.alpha_composite(out, hl)
    return out.resize((size, size), Image.LANCZOS)


def _font(px, bold=True):
    for name in (["seguisb.ttf", "segoeuib.ttf"] if bold else ["segoeui.ttf"]) + ["arialbd.ttf", "arial.ttf"]:
        try:
            return ImageFont.truetype(name, px)
        except OSError:
            continue
    return ImageFont.load_default()


def icon(size):
    """The app icon: navy rounded tile + mark (+ '60' badge from 96 px)."""
    S = size * 4
    tile = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    mask = Image.new("L", (S, S), 0)
    pad = int(S * (0.04 if size >= 48 else 0.0))
    ImageDraw.Draw(mask).rounded_rectangle([pad, pad, S - pad - 1, S - pad - 1], radius=int(S * 0.23), fill=255)
    bg = _vertical((S, S), NAVY_TOP, NAVY_BOTTOM).convert("RGBA")
    bg.putalpha(mask)
    tile = Image.alpha_composite(tile, bg)
    # faint rim
    rim = Image.new("RGBA", (S, S), (120, 160, 255, 0))
    rim.putalpha(ImageChops.subtract(mask, mask.filter(ImageFilter.MinFilter(max(3, (S // 128) | 1)))).point(lambda v: v * 70 // 255))
    tile = Image.alpha_composite(tile, rim)
    m = mark(S, echoes=size >= 24, glow=size >= 32).resize((int(S * 0.86), int(S * 0.86)), Image.LANCZOS)
    tile.alpha_composite(m, (int(S * 0.05), int(S * 0.07)))
    if size >= 96:
        d = ImageDraw.Draw(tile)
        f = _font(int(S * 0.15))
        t = "60"
        bw = d.textlength(t, font=f)
        bh = S * 0.17
        x1, y1 = S * 0.80, S * 0.80
        x0, y0 = x1 - bw - S * 0.07, y1 - bh
        pill = Image.new("L", (S, S), 0)
        ImageDraw.Draw(pill).rounded_rectangle([x0, y0, x1, y1], radius=int(bh / 2), fill=255)
        pg = _diag_gradient((S, S)).convert("RGBA")
        pg.putalpha(pill)
        tile = Image.alpha_composite(tile, pg)
        ImageDraw.Draw(tile).text(((x0 + x1) / 2, (y0 + y1) / 2), t, font=f, fill=(255, 255, 255, 255), anchor="mm")
    return tile.resize((size, size), Image.LANCZOS)


def _ico(images):
    """Windows .ico with PNG entries (Vista+)."""
    blobs = []
    for im in images:
        b = io.BytesIO()
        im.save(b, "PNG")
        blobs.append(b.getvalue())
    head = struct.pack("<HHH", 0, 1, len(images))
    off = 6 + 16 * len(images)
    dirs = b""
    for im, blob in zip(images, blobs):
        w, h = im.size
        dirs += struct.pack("<BBBBHHII", w % 256, h % 256, 0, 0, 1, 32, len(blob), off)
        off += len(blob)
    return head + dirs + b"".join(blobs)


def scene(size, mark_at, mark_px, title=None, title_px=0, title_at=None):
    """Dark backdrop with a soft glow behind the mark (about card, installer art)."""
    w, h = size
    bg = _vertical(size, (12, 16, 34), (4, 6, 14)).convert("RGBA")
    glow = Image.new("RGBA", size, (0, 0, 0, 0))
    gx, gy = mark_at
    ImageDraw.Draw(glow).ellipse([gx - mark_px * 0.9, gy - mark_px * 0.7, gx + mark_px * 0.9, gy + mark_px * 0.7],
                                 fill=(70, 110, 255, 90))
    bg = Image.alpha_composite(bg, glow.filter(ImageFilter.GaussianBlur(mark_px * 0.35)))
    m = mark(mark_px)
    bg.alpha_composite(m, (int(gx - mark_px / 2), int(gy - mark_px / 2)))
    if title:
        d = ImageDraw.Draw(bg)
        d.text(title_at, title, font=_font(title_px), fill=(240, 244, 255, 255), anchor="mm")
    return bg.convert("RGB")


def build(proof=False):
    master = icon(1024)
    master.save(RES / "brand" / "icon-1024.png")
    icon(512).save(RES / "icon.png")
    icon(256).save(RES / "brand" / "icon-256.png")
    icon(96).save(RES / "brand" / "icon-96.png")
    mark(512).save(RES / "brand" / "symbol.png")
    (RES / "icon.ico").write_bytes(_ico([icon(s) for s in ICO_SIZES]))
    # launch window: tile + name, on the app's dark background
    sp = Image.new("RGB", (340, 300), (14, 13, 12)).convert("RGBA")
    sp.alpha_composite(icon(150), (95, 40))
    ImageDraw.Draw(sp).text((170, 238), "Cine60", font=_font(30), fill=(245, 245, 245, 255), anchor="mm")
    sp.convert("RGB").save(RES / "brand" / "splash.png")
    scene((1536, 560), (1120, 280), 520).save(RES / "brand" / "about.jpg", quality=92)
    for sfx, k in (("", 1.0), ("@2.5x", 2.5)):
        scene((int(164 * k), int(314 * k) + (1 if k > 1 else 0)), (int(82 * k), int(130 * k)), int(130 * k),
              "Cine60", int(26 * k), (int(82 * k), int(250 * k))).save(ART / f"wizard{sfx}.bmp")
        sm = int(round(55 * k))
        Image.new("RGB", (sm, sm), (255, 255, 255)).save(ART / f"small{sfx}.bmp")
        s_img = Image.new("RGBA", (sm, sm), (255, 255, 255, 255))
        s_img.alpha_composite(icon(sm))
        s_img.convert("RGB").save(ART / f"small{sfx}.bmp")
    if proof:
        out = ROOT / "build" / "brand"
        out.mkdir(parents=True, exist_ok=True)
        sheet = Image.new("RGB", (1400, 560), (40, 40, 44))
        x = 20
        for s in (16, 24, 32, 48, 64, 96, 128, 256):
            sheet.paste(icon(s), (x, 20 + (256 - s)), icon(s))
            x += s + 20
        light = Image.new("RGB", (1400, 260), (240, 240, 240))
        x = 20
        for s in (16, 24, 32, 48, 64, 96, 128):
            light.paste(icon(s), (x, 20 + (128 - s)), icon(s))
            x += s + 20
        sheet.paste(light, (0, 300))
        sheet.save(out / "cine60-proof.png")
        print("proof:", out / "cine60-proof.png")


if __name__ == "__main__":
    build(proof="--proof" in sys.argv)
    print("ok")
