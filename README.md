# Portfolio — Anand M A

A static portfolio site. No framework, no build step at runtime — plain HTML, one
CSS file, one JS file, self-hosted fonts.

```
portfolio/
  index.html              home — generated
  work/<slug>.html        one page per project — generated
  css/styles.css          all styling
  js/site.js              reveals, cursor previews, marquee, clock
  fonts/                  Inter Tight + JetBrains Mono (woff2, latin)
  img/<slug>/             project images, numbered in display order
  source/                 the nine exported Figma pages (full size PNG)
  content/projects.py     all copy and project structure  ← edit this
  tools/build_site.py     regenerates index.html + work/*.html
  tools/slice_pages.py    re-slices source/*.png into img/<slug>/
  tools/prep_images.py    encodes the older board exports (unused now)
```

## Preview

Double-click `portfolio/index.html`, or for a proper server:

```powershell
cd portfolio
python -m http.server 8765      # http://localhost:8765
```

## Rebuild after editing content

```powershell
python portfolio/tools/build_site.py
```

## How the project pages work

Each project is a short header (kicker / title / lede / spec strip) followed by
the exported case-study spreads, stacked edge to edge. Blocks render top to
bottom:

| Block | Renders as |
|---|---|
| `("gallery", "img/<slug>")` | every JPG in that folder, full width, no gaps |
| `("section", label, title, [paragraphs])` | sticky label + heading + copy |
| `("image", src, caption, "bleed")` | full-width image, caption underneath |
| `("pair", [(src, cap), (src, cap)])` | two images side by side |
| `("quote", text)` | oversized pull quote (`<span>` renders in the accent) |

Adding a project: drop images in `img/<slug>/`, add an entry to `PROJECTS`, add
`("gallery", "img/<slug>")`, rebuild. Numbering, the index list and next-project
links update themselves.

## Re-slicing a Figma page

`source/<slug>.png` holds the exported page at full size. To change where it is
cut (or re-cut after a new export):

```powershell
python portfolio/tools/slice_pages.py amigos     # one project
python portfolio/tools/slice_pages.py            # all of them
```

It composites the transparent page onto white (which drops the draft copy block at
the top), cuts at the uniform gutters between spreads, and splits anything taller
than 2600 px at its quietest row.

## Design tokens

At the top of `css/styles.css`:

```css
--paper:  #F4F1EB;   /* page */
--ink:    #12100E;   /* type */
--accent: #FF3B1F;   /* dot, band, links, quote highlights */
```

Change `--accent` once and the whole site follows.

## Still to confirm

- **Social links** — LinkedIn / Behance / Instagram point at `#` (see `SITE`).
- **Years** — HappyBump and Amigos are 2023 and Minimal Mode 2024 as confirmed;
  Paperkit, Revyu, ShuffleSmart and Cotype are set to 2025, Interncan and Crea
  to 2024. Correct any that are off.
- **HappyBump images** — taken from the local board export (`happybump-portfolio`)
  rather than the Figma page, which has very large gaps between spreads.
