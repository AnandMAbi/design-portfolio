# -*- coding: utf-8 -*-
"""All site content in one place. Rebuild with: python portfolio/tools/build_site.py"""

SITE = dict(
    name="Anand M A",
    role="Visual Designer",
    email="anandmabi01@gmail.com",
    location="Kochi, India",
    year="2026",
    title="Anand M A — Visual Designer",
    description="Visual designer working across mobile products, interface systems and brand identity.",
    socials=[
        ("LinkedIn", "#"),
        ("Behance", "#"),
        ("Instagram", "#"),
    ],
    industries="Health · Education · Commerce · Lifestyle",
)

# ---------------------------------------------------------------------------
# Projects. Each one renders as: hero (kicker / title / lede / specs) followed
# by the exported case-study spreads, stacked edge to edge.
# Images live in portfolio/img/<slug>/ and are numbered in display order.
# ---------------------------------------------------------------------------
PROJECTS = [
    dict(
        slug="paperkit", title="Paperkit", draft=False,
        kicker="Brand identity · Mobile accessories",
        lede="A premium accessories brand built from the mark outwards — one idea carried through to the box it ships in.",
        discipline="Brand identity, packaging",
        year="2025",
        cover="img/paperkit/01.jpg",
        specs=[
            ("Client", "Paperkit"),
            ("Year", "2025"),
            ("Role", "Brand identity, packaging"),
            ("Output", "Logo, identity, packaging"),
            ("Scope", "Packaging layouts"),
        ],
        blocks=[("gallery", "img/paperkit")],
    ),
    dict(
        slug="happybump", title="HappyBump", draft=False,
        kicker="Product design · Maternal health",
        lede="A warmer front door to maternal care — consultations, webinars and guidance in one calm place.",
        discipline="Product design, UI/UX",
        year="2023",
        cover="img/happybump/01.jpg",
        specs=[
            ("Client", "HappyBump"),
            ("Year", "2023"),
            ("Role", "Product design, UI/UX"),
            ("Platform", "Android, iOS"),
            ("Scope", "8 screens, end to end"),
        ],
        blocks=[("gallery", "img/happybump")],
    ),
    dict(
        slug="revyu", title="Revyu", draft=False,
        kicker="Brand identity · Shopify app",
        lede="Smarter reviews, simplified. An AI review tool for store owners that needed to look intelligent without looking cold.",
        discipline="Brand identity",
        year="2025",
        cover="img/revyu/01.jpg",
        specs=[
            ("Client", "Revyu"),
            ("Year", "2025"),
            ("Role", "Identity, art direction"),
            ("Output", "Logo, mark, identity"),
            ("Scope", "Shopify app store"),
        ],
        blocks=[("gallery", "img/revyu")],
    ),
    dict(
        slug="amigos", title="Amigos", draft=False,
        kicker="Product design · EdTech",
        lede="Making online learning more engaging — live classes, recordings and resources without the friction.",
        discipline="UI/UX design",
        year="2023",
        cover="img/amigos/01.jpg",
        specs=[
            ("Client", "Amigos"),
            ("Year", "2023"),
            ("Role", "UI/UX design"),
            ("Platform", "Mobile app"),
            ("Scope", "Classroom, sessions, payments"),
        ],
        blocks=[("gallery", "img/amigos")],
    ),
    dict(
        slug="interncan", title="Interncan", draft=False,
        kicker="Web UI/UX · EdTech",
        lede="Bridging the gap between education and real life — a multi-programme platform made simple to navigate.",
        discipline="Web UI/UX, information architecture",
        year="2024",
        cover="img/interncan/01.jpg",
        specs=[
            ("Client", "Interncan"),
            ("Year", "2024"),
            ("Role", "UI/UX, web design"),
            ("Platform", "Website"),
            ("Scope", "Programmes, IA, user journeys"),
        ],
        blocks=[("gallery", "img/interncan")],
    ),
    dict(
        slug="crea", title="Crea", draft=False,
        kicker="Landing page · Online learning",
        lede="Learn. Create. Inspire. A landing page that carries a creative school's energy without losing the hierarchy.",
        discipline="Landing page, visual direction",
        year="2024",
        cover="img/crea/01.jpg",
        specs=[
            ("Client", "Crea"),
            ("Year", "2024"),
            ("Role", "UI/UX, visual direction"),
            ("Platform", "Website"),
            ("Scope", "Landing page, content flow"),
        ],
        blocks=[("gallery", "img/crea")],
    ),
    dict(
        slug="shufflesmart", title="ShuffleSmart", draft=False,
        kicker="Brand identity · Smart home",
        lede="Smarter living, every day. An identity that has to feel premium and practical in the same breath.",
        discipline="Brand identity",
        year="2025",
        cover="img/shufflesmart/01.jpg",
        specs=[
            ("Client", "ShuffleSmart"),
            ("Year", "2025"),
            ("Role", "Identity, brand mark"),
            ("Output", "Logo, mark, identity"),
            ("Scope", "Smart home, lifestyle"),
        ],
        blocks=[("gallery", "img/shufflesmart")],
    ),
    dict(
        slug="cotype", title="Cotype", draft=False,
        kicker="Brand identity · AI product",
        lede="A better way to write emails. A calm, contemporary identity for an assistant that has to disappear into the writing.",
        discipline="Brand identity",
        year="2025",
        cover="img/cotype/01.jpg",
        specs=[
            ("Client", "Cotype"),
            ("Year", "2025"),
            ("Role", "Identity, brand mark"),
            ("Output", "Logo, mark, identity"),
            ("Scope", "AI writing assistant"),
        ],
        blocks=[("gallery", "img/cotype")],
    ),
    dict(
        slug="minimal-mode", title="Minimal Mode", draft=False,
        kicker="Brand identity · Premium apparel",
        lede="Less, but better. A quiet identity system for a label that would rather the garment did the talking.",
        discipline="Brand identity, art direction",
        year="2024",
        cover="img/minimal-mode/01.jpg",
        specs=[
            ("Client", "Minimal Mode"),
            ("Year", "2024"),
            ("Role", "Identity, art direction"),
            ("Output", "Mark, lockup, palette"),
            ("Scope", "Print, apparel, digital"),
        ],
        blocks=[("gallery", "img/minimal-mode")],
    ),
]

ABOUT = [
    "I'm Anand, a visual designer working across mobile products, interface systems and brand "
    "identity. I like briefs that are a little messy at the start — where the problem is real, the "
    "constraints are honest, and the answer has to earn its place.",
    "Most of the work here started as a rough idea on a call. I take it from there: structure first, "
    "then the interface, then the details that make it feel like nothing else.",
]

CAPABILITIES = [
    ("01", "Product thinking", "Briefs, flows and the decisions that shape a product before pixels."),
    ("02", "Interface design", "Screens, states and systems that still hold up after launch."),
    ("03", "Design systems", "Type, colour and components documented so a team can move."),
    ("04", "Brand direction", "Identity work for products that need a voice, not just a UI."),
]
