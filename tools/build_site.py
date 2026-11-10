# -*- coding: utf-8 -*-
"""Static site builder.

    python portfolio/tools/build_site.py

Reads portfolio/content/projects.py and writes:
    portfolio/index.html
    portfolio/work/<slug>.html

Nothing is templated at runtime — the output is plain HTML you can host anywhere.
"""
import sys
import html
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "content"))

from projects import SITE, PROJECTS, ABOUT, CAPABILITIES  # noqa: E402

ARROW = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" '
         'aria-hidden="true"><path d="M3 13 13 3M5.5 3H13v7.5"/></svg>')
ARROW_R = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" '
           'aria-hidden="true"><path d="M1 8h13M9 3l5 5-5 5"/></svg>')
ARROW_L = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" '
           'aria-hidden="true" width="14" height="14"><path d="M15 8H2M7 3 2 8l5 5"/></svg>')

LIVE = [p for p in PROJECTS if not p["draft"]]
COUNT = len(LIVE)


def e(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- fragments
def head(title, description, root, page="home"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{root}css/styles.css">
</head>
<body data-page="{page}">
<div class="progress" aria-hidden="true"></div>
"""


def header(root):
    base = "index.html" if root else ""
    nav = "".join(
        f'<a href="{base}#{anchor}">{label}</a>'
        for anchor, label in (("work", "Work"), ("about", "About"), ("contact", "Contact"))
    )
    return f"""
<header class="site-head">
  <div class="wrap site-head__in">
    <a class="brand" href="{root}index.html" aria-label="{e(SITE['name'])} — home">
      <span class="brand__mark"><span>AM</span></span>
      <span>{e(SITE['name'])}</span>
    </a>
    <nav class="nav" aria-label="Primary">{nav}</nav>
    <div class="site-head__right">
      <a class="head-cta" href="mailto:{SITE['email']}"><i></i>Available for work</a>
    </div>
  </div>
</header>
"""


def contact(root, label="Contact"):
    cols = f"""
      <div class="contact__col"><h4>Email</h4><a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
      <div class="contact__col"><h4>Index</h4><a href="{root}index.html#work">Work</a><br><a href="{root}index.html#about">About</a></div>
    """
    return f"""
<section class="contact" id="contact">
  <div class="wrap">
    <div class="contact__top">
      <div>
        <p class="mono">{e(label)}</p>
        <a class="contact__mail" href="mailto:{SITE['email']}">Say hello &nbsp;↗</a>
      </div>
      <p class="mono" style="max-width:26ch;text-align:right">Open to product design and identity work from {SITE['year']}.</p>
    </div>
    <div class="contact__grid">{cols}</div>
  </div>
</section>
"""


def footer():
    return f"""
<footer class="site-foot wrap">
  <span class="mono">© <span data-year>2026</span> {e(SITE['name'])}</span>
  <span class="mono">Made with intent — no templates</span>
  <span class="mono">{e(SITE['location'])}</span>
</footer>
"""


def script(root):
    return f'<script src="{root}js/site.js" defer></script>\n</body>\n</html>\n'


# ---------------------------------------------------------------- home
def render_home():
    rows = []
    for i, p in enumerate(LIVE, 1):
        rows.append(f"""      <a class="index__row" href="work/{p['slug']}.html" data-preview="{p['cover']}" data-preview-tag="{e(p['title'])} — {e(p['year'])}">
        <span class="index__num">0{i}</span>
        <span class="index__title">{e(p['title'])}</span>
        <span class="index__disc">{e(p['discipline'])}</span>
        <span class="index__year">{e(p['year'])}</span>
        <span class="index__arrow">{ARROW}</span>
      </a>""")

    caps = "".join(f"""
      <article class="cap" data-reveal>
        <span class="cap__num">{n}</span>
        <div><h3>{e(t)}</h3><p>{e(d)}</p></div>
      </article>""" for n, t, d in CAPABILITIES)

    first_year = min(int(p["year"]) for p in LIVE)

    about_paras = "".join(f"<p>{e(t)}</p>" for t in ABOUT)

    marquee_items = "".join(
        f"<span>{t}</span>" for t in [
            "Visual design", "Interface systems", "Brand identity",
            "Prototyping", "Design systems", "Available for select projects",
        ]
    )

    return head(SITE["title"], SITE["description"], "", "home") + header("") + f"""
<main>
  <section class="hero">
    <div class="wrap">
      <div class="hero__meta">
        <span class="mono">Portfolio — {SITE['year']}</span>
        <span class="mono">{e(SITE['location'])} · {e(SITE['role'])}</span>
        <span class="mono mono--ink">● Open for select projects</span>
      </div>
      <div class="hero__body">
        <h1 class="h1 hero__title" data-reveal>
          <span class="line">Visual</span>
          <span class="line line--2">Designer<span class="dot"></span></span>
        </h1>
        <div class="hero__aside">
          <p class="hero__para lede dim" data-reveal data-delay="1">
            I design digital products for health, education and commerce — calm interfaces,
            clear systems, and the small details that make them feel considered.
          </p>
          <a class="hero__scroll" href="#work" data-reveal data-delay="2">
            Selected work
            <svg viewBox="0 0 12 16" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M6 0v14M1 9.5 6 15l5-5.5"/></svg>
          </a>
        </div>
      </div>
    </div>
    <div class="band" aria-hidden="true">
      <div class="band__in"><div class="marquee">{marquee_items}</div></div>
    </div>
  </section>

  <section class="work" id="work">
    <div class="wrap">
      <div class="section-head">
        <span class="mono mono--ink">01 — Selected work</span>
        <span class="mono">{COUNT:02d} projects · {first_year} — {SITE['year']}</span>
      </div>
      <div class="index">
{chr(10).join(rows)}
      </div>
      <div class="index__foot">
        <span class="mono">Case studies, not screenshots</span>
        <span class="mono">01 / {COUNT:02d}</span>
      </div>
    </div>
  </section>

  <section class="section" id="about">
    <div class="wrap">
      <div class="about">
        <div class="about__label mono">02 — About</div>
        <div class="about__main">
          <h2 class="h2" data-reveal>Structure first.<br>Then the details.</h2>
          <div style="max-width:56ch;margin-top:clamp(20px,2.6vw,34px)" data-reveal data-delay="1">
            {about_paras}
          </div>
        </div>
        <aside class="about__side">
          <figure class="about__portrait" data-reveal>
            <img src="img/portrait.jpg" alt="Portrait of Anand M A" width="1200" height="1500" loading="lazy" decoding="async">
          </figure>
          <div class="stats">
            <div class="stat"><span>Focus</span><b>Visual · UI/UX</b></div>
            <div class="stat"><span>Based</span><b>{e(SITE['location'])}</b></div>
            <div class="stat"><span>Status</span><b>Open to work</b></div>
            <div class="stat"><span>Local time</span><b data-clock>—</b></div>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head">
        <span class="mono mono--ink">03 — What I do</span>
        <span class="mono">End to end, or the part you need</span>
      </div>
      <div class="caps">{caps}</div>
    </div>
  </section>
</main>

{contact("", "04 — Contact")}
{footer()}
<div class="preview" aria-hidden="true"><img alt=""><span class="preview__tag"></span></div>
""" + script("")


# ---------------------------------------------------------------- case study
def project_by_slug(slug):
    return next(p for p in LIVE if p["slug"] == slug)


def next_project(p):
    i = LIVE.index(p)
    return LIVE[(i + 1) % len(LIVE)]


def figure(src, caption, cls="", root="../", reveal=True, eager=False):
    att = ' data-reveal' if reveal else ""
    load = 'eager' if eager else 'lazy'
    cap = f'<figcaption><span>{e(caption)}</span></figcaption>' if caption else ""
    return f"""<figure class="plate {cls}"{att}>
        <img src="{root}{src}" alt="{e(caption or '')}" loading="{load}" decoding="async">
        {cap}
      </figure>"""


def render_block(b, root="../"):
    kind = b[0]
    if kind == "section":
        _, label, title, paras = b
        body = f'<h3>{e(title)}</h3>' + "".join(f"<p>{e(t)}</p>" for t in paras)
        return f"""
      <div class="wrap"><section class="case-section">
        <div class="case-section__label"><span class="mono">{e(label)}</span></div>
        <div class="case-section__body" data-reveal>{body}</div>
      </section></div>"""
    if kind == "image":
        _, src, caption, align = b
        cls = "plate--bleed" if align == "bleed" else "plate--framed"
        return f"""
      <div class="wrap"><div class="figure-stack">{figure(src, caption, cls, root)}</div></div>"""
    if kind == "pair":
        items = "".join(f"""<figure class="plate plate--framed">
          <img src="{root}{s}" alt="{e(c)}" loading="lazy" decoding="async">
          <figcaption><span>{e(c)}</span></figcaption>
        </figure>""" for s, c in b[1])
        return f"""
      <div class="wrap"><div class="figure-stack"><div class="fig-pair" data-reveal>{items}</div></div></div>"""
    if kind == "quote":
        return f"""
      <div class="wrap"><section class="case-section case-section--wide">
        <blockquote class="pullquote" data-reveal>{b[1]}</blockquote>
      </section></div>"""
    if kind == "gallery":
        folder = b[1]
        files = sorted((ROOT / folder).glob("*.jpg"))
        imgs = []
        for i, f in enumerate(files):
            with Image.open(f) as im:
                w, h = im.size
            load = "eager" if i == 0 else "lazy"
            imgs.append(
                f'<img src="{root}{folder}/{f.name}" width="{w}" height="{h}" '
                f'alt="" loading="{load}" decoding="async">'
            )
        return f"""
  <div class="gallery" aria-label="Project images">
        {chr(10).join(imgs)}
  </div>"""
    raise ValueError(kind)


def render_project(p):
    specs = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in p["specs"])
    nxt = next_project(p)
    idx = LIVE.index(p) + 1
    blocks = "".join(render_block(b) for b in p["blocks"])

    return head(f"{p['title']} — {SITE['name']}", p["lede"], "../", "case") + header("../") + f"""
<main>
  <div class="wrap case-hero">
    <a class="case-back mono" href="../index.html#work">{ARROW_L} All projects</a>
    <div class="case-hero__top">
      <p class="mono" style="margin:0">{e(p['kicker'])}</p>
      <span class="mono">{idx:02d} / {COUNT:02d}</span>
    </div>
    <div class="case-head">
      <h1 class="case-hero__title">{e(p['title'])}</h1>
      <p class="case-hero__lede">{e(p['lede'])}</p>
    </div>
    <dl class="case-specs">{specs}</dl>
  </div>

  {blocks}

  <div class="wrap">
    <div class="case-more">
  <div class="wrap">
    <div class="case-more">
      <div>
        <p class="mono" style="margin:0 0 10px">Next — {LIVE.index(nxt) + 1:02d}</p>
        <a class="case-more__link" href="{nxt['slug']}.html">{e(nxt['title'])} {ARROW_R}</a>
      </div>
      <span class="mono">{idx:02d} / {COUNT:02d}</span>
    </div>
  </div>
</main>

{contact("../")}
{footer()}
""" + script("../")


# ---------------------------------------------------------------- build
def main():
    (ROOT / "work").mkdir(exist_ok=True)
    out_index = ROOT / "index.html"
    out_index.write_text(render_home(), encoding="utf-8")
    print(f"  index.html                {out_index.stat().st_size / 1024:.0f} kB")
    for p in LIVE:
        path = ROOT / "work" / f"{p['slug']}.html"
        path.write_text(render_project(p), encoding="utf-8")
        print(f"  work/{p['slug']}.html{' ' * max(1, 22 - len(p['slug']))}{path.stat().st_size / 1024:.0f} kB")
    print(f"\n  {len(LIVE)} of {len(PROJECTS)} projects published "
          f"({len(PROJECTS) - len(LIVE)} still draft)")


if __name__ == "__main__":
    main()
