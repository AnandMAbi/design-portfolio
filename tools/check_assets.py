import re
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
missing = []
for f in list(root.glob("*.html")) + list(root.glob("work/*.html")):
    for src in re.findall(r'src="([^"]+)"', f.read_text(encoding="utf-8")):
        if src.startswith("http"):
            continue
        if not (f.parent / src).resolve().exists():
            missing.append(f"{f.relative_to(root)} -> {src}")
print("missing:", missing if missing else "none")
