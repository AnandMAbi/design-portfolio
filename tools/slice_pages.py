"""Slice the exported Figma case-study pages into stacked section images.

Each page is a long canvas: a block of draft copy at the top, then designed
sections (cream / white / dark posters). Composite on white so the un-backed
draft copy disappears, then cut at the uniform gutters between sections.
"""
from pathlib import Path
from PIL import Image
import sys

SRC = Path(r"C:\Users\XRIG\Documents\Default Project\portfolio\source")
OUT = Path(r"C:\Users\XRIG\Documents\Default Project\portfolio\img")

MIN_RUN = 26          # analysis px of uniform rows = a gutter
MIN_SLICE = 500       # original px — anything shorter merges into the next slice
MAX_SLICE = 2600      # original px — taller slices get split at their quietest row
MAX_W = 2000
ANALYSIS_W = 600


def row_stats(im):
    small = im.resize((ANALYSIS_W, round(im.height * ANALYSIS_W / im.width)), Image.LANCZOS)
    px = small.load()
    out = []
    for y in range(small.height):
        vals = [px[x, y] for x in range(0, ANALYSIS_W, 5)]
        lum = sorted((v[0] + v[1] + v[2]) / 3 for v in vals)
        med = lum[len(lum) // 2]
        spread = lum[-1] - lum[0]
        out.append((med, spread))
    return out, small.height / im.height


def cut_points(rows, scale):
    cuts, start = [], None
    for y, (med, spread) in enumerate(rows):
        uniform = spread < 12
        if uniform and start is None:
            start = y
        elif not uniform and start is not None:
            if y - start >= MIN_RUN:
                cuts.append(((start + y) / 2) / scale)
            start = None
    if start is not None and len(rows) - start >= MIN_RUN:
        cuts.append(((start + len(rows)) / 2) / scale)
    return cuts


def slice_page(path: Path, slug: str):
    im = Image.open(path).convert("RGBA")
    canvas = Image.new("RGB", im.size, (255, 255, 255))
    canvas.paste(im, (0, 0), im)
    im = canvas

    rows, scale = row_stats(im)

    first = 0
    for y, (med, spread) in enumerate(rows):
        if spread >= 12:
            first = y / scale
            break

    bounds = [first] + [c for c in cut_points(rows, scale) if c > first] + [im.height]
    bounds = sorted(bounds)

    chunks = []
    for a, b in zip(bounds, bounds[1:]):
        if chunks and b - a < MIN_SLICE:
            chunks[-1] = (chunks[-1][0], b)
        else:
            chunks.append((a, b))

    # split anything too tall at its quietest interior row
    final = []
    for a, b in chunks:
        while b - a > MAX_SLICE:
            target = a + (b - a) / 2
            lo, hi = int(a + MAX_SLICE * 0.45), int(min(b - 400, a + MAX_SLICE))
            if hi <= lo:
                break
            best, best_dev = target, None
            for y in range(lo, hi, 4):
                dev = rows[min(len(rows) - 1, int(y * scale))][1]
                if best_dev is None or dev < best_dev:
                    best, best_dev = y, dev
            final.append((a, best))
            a = best
        final.append((a, b))

    dst = OUT / slug
    dst.mkdir(parents=True, exist_ok=True)
    for f in dst.glob("*.jpg"):
        f.unlink()

    for i, (a, b) in enumerate(final, 1):
        crop = im.crop((0, int(round(a)), im.width, int(round(b))))
        if crop.width > MAX_W:
            h = round(crop.height * MAX_W / crop.width)
            crop = crop.resize((MAX_W, h), Image.LANCZOS)
        out = dst / f"{i:02d}.jpg"
        crop.save(out, "JPEG", quality=88, optimize=True, progressive=True)
        print(f"  {slug:14} {out.name}  {crop.width}x{crop.height}")


if __name__ == "__main__":
    only = sys.argv[1:] or None
    for f in sorted(SRC.glob("*.png")):
        if only and f.stem not in only:
            continue
        print(f.stem)
        slice_page(f, f.stem)
