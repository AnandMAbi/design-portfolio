"""Copy project boards into web-sized JPGs under portfolio/img/<slug>/.

Source folders are the existing case-study builds in the workspace root.
Re-run after dropping new exports in; anything already web-sized is skipped.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1] / "img"

# slug -> (source folder, glob, max width)
SOURCES = {
    "happybump": ("happybump-portfolio/boards", "0[1-7]-*.png", 2000),
    "amigos": ("amigos-portfolio/boards", "0[1-5]-*.png", 2000),
    "minimal-mode": ("minimal-mode-portfolio/boards", "0[1-8]-*.png", 2000),
}


def main():
    for slug, (folder, pattern, width) in SOURCES.items():
        dst_dir = OUT / slug
        dst_dir.mkdir(parents=True, exist_ok=True)
        for src in sorted((ROOT / folder).glob(pattern)):
            dst = dst_dir / (src.stem + ".jpg")
            if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
                continue
            im = Image.open(src).convert("RGB")
            if im.width > width:
                h = round(im.height * width / im.width)
                im = im.resize((width, h), Image.LANCZOS)
            im.save(dst, "JPEG", quality=86, optimize=True, progressive=True)
            print(f"{slug:14} {dst.name:28} {im.width}×{im.height}")


if __name__ == "__main__":
    main()
