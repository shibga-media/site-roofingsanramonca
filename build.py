#!/usr/bin/env python3
"""
Builds roofingsanramonca.com into docs/ (GitHub Pages serves main:/docs).

    python3 build.py            # rebuild the whole site
    git add -A && git commit -m "..." && git push   # publish (live in ~1 min)

Words: content.py        Styles: src/site.css        Photos: src/photos/<slug>.jpg (+ a line in content.PHOTOS)
Needs: Python 3 + Pillow (pip install pillow). Nothing else.
"""
import datetime, hashlib, html, json, os, re, shutil
from PIL import Image

import content as C

# ---------------------------------------------------------------------------
# 🔴 THE SWITCH. False = draft: every page is noindex,nofollow AND robots.txt blocks everything.
#    Flip to True only after Shib approves the draft, then rebuild + push.
INDEXABLE = False
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# CONTACT FORM — deliberately OFF. A form with no working handler loses leads.
# To add one later: set CONTACT_FORM to a dict like
#   {"action": "https://<form handler URL>", "subject": "Shibga Media Leads"}
# The handler must email customerservice@cjs-roofing.com with that subject and
# redirect to /thank-you/. The form then appears on /contact-us/ (see contact_form()).
CONTACT_FORM = None
# ---------------------------------------------------------------------------

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")
SRC_PHOTOS = os.path.join(ROOT, "src", "photos")
KEEP = {"CNAME", ".nojekyll", "img"}          # never deleted from docs/ on rebuild
S = C.SITE
DOMAIN = S["domain"]
YEAR = datetime.date.today().year
E = html.escape

# ---------------------------------------------------------------- icons (inline SVG)
IC = {
    "phone": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
    "text": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 3h16a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 1-2zm3 6v2h2V9zm4 0v2h2V9zm4 0v2h2V9z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm9 7.2L4.5 7v1.9l7.5 5.1 7.5-5.1V7z"/></svg>',
    "logo": '<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="8" fill="#a4402a"/><path d="M6 22 20 10l14 12" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M11 27.5 20 20l9 7.5" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" opacity=".75"/></svg>',
    "shingle": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" aria-hidden="true"><path d="M4 24 24 7l20 17"/><path d="M11 22h26M9 28h30M8 34h32"/><path d="M17 22v6M31 22v6M13 28v6M24 28v6M35 28v6"/></svg>',
    "tile": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 24 24 7l20 17"/><path d="M8 30c2.5-4 5.5-4 8 0s5.5 4 8 0 5.5-4 8 0 5.5 4 8 0"/><path d="M8 38c2.5-4 5.5-4 8 0s5.5 4 8 0 5.5-4 8 0 5.5 4 8 0"/></svg>',
    "gutters": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 14h40"/><path d="M6 18h36v5a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3z"/><path d="M34 26v14"/><path d="M34 40h6"/><path d="M20 32c0 2-1.5 3.5-3 3.5S14 34 14 32s3-6 3-6 3 4 3 6z"/></svg>',
}

TEL = f'tel:{S["phone_tel"]}'
SMS = f'sms:{S["phone_tel"]}'
MAILTO = f'mailto:{S["email"]}'

SERVICES = [  # home + services hub cards
    ("tile", "/services/tile-roofing/", "Tile Roofing",
     "Concrete and clay tile: broken and slipped tiles, leaks, underlayment problems, re-roofs.",
     [("/services/tile-roofing/tile-roof-repair/", "Tile roof repair"),
      ("/services/tile-roofing/tile-roof-replacement/", "Tile roof replacement")]),
    ("shingle", "/services/shingle-roofing/", "Shingle Roofing",
     "Asphalt shingle roofs: leaks, missing and worn shingles, flashing, full replacement.",
     [("/services/shingle-roofing/shingle-roof-repair/", "Shingle roof repair"),
      ("/services/shingle-roofing/shingle-roof-replacement/", "Shingle roof replacement")]),
    ("gutters", "/services/gutters/", "Gutters",
     "New gutters and downspouts, and repairs to leaking, sagging or loose gutters.",
     [("/services/gutters/seamless-gutter-installation/", "Seamless gutter installation"),
      ("/services/gutters/gutter-repair/", "Gutter repair")]),
]
CITY_PAGES = [("/dublin/", "Dublin"), ("/danville/", "Danville"), ("/pleasanton/", "Pleasanton"),
              ("/alamo/", "Alamo"), ("/castro-valley/", "Castro Valley"), ("/fremont/", "Fremont")]

NAV = [("/services/", "Services"), ("/services/tile-roofing/", "Tile"), ("/services/shingle-roofing/", "Shingle"),
       ("/services/gutters/", "Gutters"), ("/gallery/", "Gallery"), ("/reviews/", "Reviews"),
       ("/about-us/", "About"), ("/roofing-faq/", "FAQ"), ("/contact-us/", "Contact")]

PAGE_BY_PATH = {p["path"]: p for p in C.PAGES}

# ---------------------------------------------------------------- photos
PHOTO_META = {}   # slug -> {"w":..,"h":..,"sizes":[(w,url),..]}


def build_photos():
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
    for slug in C.PHOTOS:
        src = os.path.join(SRC_PHOTOS, slug + ".jpg")
        if not os.path.exists(src):
            raise SystemExit(f"missing photo src/photos/{slug}.jpg")
        im = Image.open(src)
        W, H = im.size
        sizes = []
        for target in (480, 960, 1600):
            w = min(target, W)
            if sizes and w == sizes[-1][0]:
                continue
            h = round(H * w / W)
            fn = f"{slug}-{w}.webp"
            dst = os.path.join(OUT, "img", fn)
            if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
                im2 = im.convert("RGB").resize((w, h), Image.LANCZOS)
                im2.save(dst, "WEBP", quality=62, method=6)  # no EXIF written
            sizes.append((w, f"/img/{fn}"))
        PHOTO_META[slug] = {"w": W, "h": H, "sizes": sizes}
    # drop images no longer referenced
    wanted = {u.split("/")[-1] for m in PHOTO_META.values() for _, u in m["sizes"]}
    for f in os.listdir(os.path.join(OUT, "img")):
        if f not in wanted:
            os.remove(os.path.join(OUT, "img", f))


def img_tag(slug, sizes_attr, eager=False, cls=""):
    m, p = PHOTO_META[slug], C.PHOTOS[slug]
    small_w, small_u = m["sizes"][0]
    srcset = ", ".join(f"{u} {w}w" for w, u in m["sizes"])
    h = round(m["h"] * small_w / m["w"])
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{small_u}" srcset="{srcset}" sizes="{sizes_attr}" width="{small_w}" height="{h}" '
            f'alt="{E(p["alt"])}" {load}>')


def figure(slug, sizes_attr="(min-width:960px) 250px, (min-width:600px) 33vw, 100vw", link=False):
    t = img_tag(slug, sizes_attr)
    if link:
        t = f'<a href="{PHOTO_META[slug]["sizes"][-1][1]}">{t}</a>'
    return f'<figure>{t}<figcaption>{E(C.PHOTOS[slug]["caption"])}</figcaption></figure>'


# ---------------------------------------------------------------- text -> HTML
def inline(s):
    s = E(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)

    def link(m):
        text, url = m.group(1), m.group(2)
        ext = url.startswith("http")
        return f'<a href="{url}"' + (' rel="noopener"' if ext else "") + f">{text}</a>"
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
    s = s.replace("{call}", f'<a href="{TEL}">{S["phone_display"]}</a>')
    s = s.replace("{text}", f'<a href="{SMS}">{S["phone_display"]}</a>')
    s = s.replace("{email}", f'<a href="{MAILTO}">{S["email"]}</a>')
    return s


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def cta_box(title="Talk to Chris about your roof"):
    return (f'<section class="cta"><h2>{E(title)}</h2>'
            f'<p>Call or text {E(S["phone_display"])}. You\'ll reach the owner, not a call center.</p>'
            f'<div class="btns"><a class="btn pri" href="{TEL}">{IC["phone"]}Call {S["phone_display"]}</a>'
            f'<a class="btn sec" href="{SMS}">{IC["text"]}Text a photo</a></div></section>')


def services_cards():
    out = ['<div class="svc">']
    for icon, url, name, blurb, subs in SERVICES:
        out.append(f'<a class="card" href="{url}">{IC[icon]}<h3>{E(name)}</h3><p>{E(blurb)}</p>'
                   f'<span class="more">{E(name)} &rarr;</span></a>')
    out.append("</div>")
    return "".join(out)


def cities_list():
    items = ['<li><a href="/">San Ramon<span>Home base</span></a></li>']
    items += [f'<li><a href="{u}">{E(n)}<span>Roofing in {E(n)}</span></a></li>' for u, n in CITY_PAGES]
    return f'<ul class="cities" id="areas">{"".join(items)}</ul><p>We also work across the greater Bay Area. Not sure if you\'re in range? Call {inline("{call}")}.</p>'


def gallery():
    groups = {}
    for slug, p in C.PHOTOS.items():
        groups.setdefault(p["group"], []).append(slug)
    out = []
    for g, slugs in groups.items():
        out.append(f"<h2>{E(g)}</h2><div class=\"gal\">")
        out += [figure(s, "(min-width:960px) 360px, (min-width:600px) 33vw, 50vw", link=True) for s in slugs]
        out.append("</div>")
    return "".join(out)


def faq_html():
    return '<div class="faq">' + "".join(f"<h3>{E(q)}</h3><p>{inline(a)}</p>" for q, a in C.FAQ) + "</div>"


def review_links():
    return (f'<div class="contact"><a class="card" href="{S["google_maps"]}" rel="noopener"><div><b>Google</b>'
            f'<span>CJ\'s Roofing on Google Maps</span></div></a>'
            f'<a class="card" href="{S["yelp"]}" rel="noopener"><div><b>Yelp</b><span>CJ\'s Roofing on Yelp</span></div></a></div>')


def review_cta():
    return f'<p><a class="btn pri" href="{S["google_review"]}" rel="noopener">Leave a Google review</a></p>'


def contact_cards():
    out = (f'<div class="contact">'
           f'<a class="card big" href="{TEL}">{IC["phone"]}<div><b>{S["phone_display"]}</b><span>Call Chris</span></div></a>'
           f'<a class="card" href="{SMS}">{IC["text"]}<div><b>Text us</b><span>{S["phone_display"]}: send photos</span></div></a>'
           f'<a class="card" href="{MAILTO}">{IC["mail"]}<div><b>Email</b><span>{S["email"]}</span></div></a></div>'
           f'<address class="card nap"><strong>{E(S["name"])}</strong><br>{E(S["street"])}<br>'
           f'{E(S["city"])}, {S["region"]} {S["zip"]}<br>CSLB Lic. #{S["license"]} ({E(S["license_class"])})</address>')
    return out + contact_form()


def contact_form():
    if not CONTACT_FORM:
        return ""   # <- form goes here once a working handler exists (see CONTACT_FORM at the top)
    f = CONTACT_FORM
    return (f'<form class="card" method="post" action="{E(f["action"])}"><h2>Send a message</h2>'
            f'<input type="hidden" name="_subject" value="{E(f["subject"])}">'
            f'<input type="hidden" name="_next" value="{DOMAIN}/thank-you/">'
            '<p><label>Name<br><input name="name" required autocomplete="name"></label></p>'
            '<p><label>Phone<br><input name="phone" type="tel" required autocomplete="tel"></label></p>'
            '<p><label>Email<br><input name="email" type="email" autocomplete="email"></label></p>'
            '<p><label>Address and what you need<br><textarea name="message" rows="5"></textarea></label></p>'
            '<p><button class="btn pri" type="submit">Send</button></p></form>')


SHORTCODES = {"cta": cta_box, "services": services_cards, "cities": cities_list, "gallery": gallery,
              "faq": faq_html, "reviewlinks": review_links, "reviewcta": review_cta, "contactcards": contact_cards}


def render_body(text):
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        b = block.strip()
        if not b:
            continue
        m = re.fullmatch(r"\[\[(\w+)(?::([^\]]+))?\]\]", b)
        if m:
            name, arg = m.group(1), m.group(2)
            if name == "photo":
                out.append(f'<div class="photos">{figure(arg.strip())}</div>')
            elif name == "photos":
                out.append('<div class="photos">' + "".join(figure(s.strip()) for s in arg.split(",")) + "</div>")
            else:
                out.append(SHORTCODES[name]())
        elif b.startswith("### "):
            out.append(f"<h3>{inline(b[4:])}</h3>")
        elif b.startswith("## "):
            t = b[3:]
            out.append(f'<h2 id="{slugify(t)}">{inline(t)}</h2>')
        elif all(l.strip().startswith("- ") for l in b.splitlines()):
            out.append("<ul>" + "".join(f"<li>{inline(l.strip()[2:])}</li>" for l in b.splitlines()) + "</ul>")
        else:
            out.append(f"<p>{inline(' '.join(l.strip() for l in b.splitlines()))}</p>")
    return "\n".join(out)


# ---------------------------------------------------------------- schema
def business_ld():
    return {
        "@context": "https://schema.org", "@type": "RoofingContractor", "@id": f"{DOMAIN}/#business",
        "name": S["name"], "url": f"{DOMAIN}/", "telephone": "+1-925-548-0932", "email": S["email"],
        "foundingDate": S["founded"], "founder": {"@type": "Person", "name": S["owner"]},
        "image": f"{DOMAIN}{PHOTO_META['tile-roof-dublin-hills']['sizes'][-1][1]}",
        "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"],
                    "addressRegion": S["region"], "postalCode": S["zip"], "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": f"{c}, CA"} for c in S["areas"]],
        "hasMap": S["google_maps"],
        "sameAs": [S["google_maps"], S["yelp"]],
        "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license",
                          "name": f"California contractor license #{S['license']} ({S['license_class']})",
                          "url": S["license_url"],
                          "recognizedBy": {"@type": "GovernmentOrganization",
                                           "name": "Contractors State License Board"}},
        "knowsAbout": ["Asphalt shingle roofing", "Tile roofing", "Gutters"],
    }


def crumbs_for(path):
    parts = [p for p in path.strip("/").split("/") if p]
    trail = [("/", "Home")]
    for i in range(len(parts)):
        u = "/" + "/".join(parts[:i + 1]) + "/"
        if u in PAGE_BY_PATH:
            trail.append((u, PAGE_BY_PATH[u]["label"]))
    return trail


def ld_scripts(pg):
    blocks = [business_ld()]
    if pg["path"] != "/":
        blocks.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u}
            for i, (u, n) in enumerate(crumbs_for(pg["path"]))]})
    if pg["path"] == "/roofing-faq/":
        strip = lambda s: re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s).replace("{call}", S["phone_display"])
        blocks.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            for q, a in C.FAQ]})
    return "".join(f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in blocks)


# ---------------------------------------------------------------- page chrome
def head(pg, css_href):
    robots = "noindex, nofollow" if (not INDEXABLE or pg.get("noindex")) else "index, follow"
    canon = DOMAIN + pg["path"]
    og_img = pg.get("hero") or "tile-roof-dublin-hills"
    og_url = DOMAIN + PHOTO_META[og_img]["sizes"][-1][1]
    preload = ""
    if pg.get("hero"):
        m = PHOTO_META[pg["hero"]]
        preload = (f'<link rel="preload" as="image" href="{m["sizes"][0][1]}" '
                   f'imagesrcset="{", ".join(f"{u} {w}w" for w, u in m["sizes"])}" '
                   f'imagesizes="{hero_sizes(pg)}" fetchpriority="high">')
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(pg["title"])}</title>
<meta name="description" content="{E(pg["description"])}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{E(S["name"])}">
<meta property="og:title" content="{E(pg["title"])}"><meta property="og:description" content="{E(pg["description"])}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{og_url}">
<meta name="theme-color" content="#1f2a35">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{preload}<link rel="stylesheet" href="{css_href}">
{ld_scripts(pg)}
</head>"""


def hero_sizes(pg):
    return "(min-width:960px) 540px, 100vw" if pg.get("layout") == "home" else "(min-width:1140px) 1108px, 100vw"


def header(pg):
    cur = pg["path"]
    desk = "".join(f'<a href="{u}"' + (' aria-current="page"' if u == cur else "") + f">{n}</a>" for u, n in NAV)
    mob = [f'<a href="/">Home</a>']
    for u, n in NAV:
        mob.append(f'<a href="{u}">{n}{" roofing" if n in ("Tile", "Shingle") else ""}</a>')
    mob += [f'<a class="sub" href="{u}">Roofing in {n}</a>' for u, n in CITY_PAGES]
    mob.append('<a href="/types-of-roofing/">Shingle vs tile</a><a href="/privacy-policy/">Privacy Policy</a>')
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<div class="top"><div class="wrap"><span>San Ramon, CA · Since 1995<span class="hide-s"> · CSLB Lic. #{S["license"]}</span></span><a href="{TEL}">Call or text {S["phone_display"]}</a></div></div>
<header class="site"><div class="wrap">
<a class="logo" href="/" aria-label="CJ's Roofing home">{IC["logo"]}<span><b>CJ'S ROOFING</b><small>San Ramon · Since 1995</small></span></a>
<nav class="desk" aria-label="Main">{desk}</nav>
<a class="hdr-call" href="{TEL}" aria-label="Call CJ's Roofing {S["phone_display"]}">{IC["phone"]}<span class="num">{S["phone_display"]}</span></a>
<details class="menu"><summary>Menu</summary><nav aria-label="Mobile">{"".join(mob)}</nav></details>
</div></header>"""


def aside(pg):
    svc = "".join(f'<li><a href="{u}">{E(n)}</a></li>' for _, u, n, _, _ in SERVICES)
    cities = '<li><a href="/">San Ramon</a></li>' + "".join(f'<li><a href="{u}">{E(n)}</a></li>' for u, n in CITY_PAGES)
    return f"""<aside>
<div class="card"><h2>Call Chris</h2><address class="nap"><strong>{E(S["name"])}</strong><br>{E(S["street"])}<br>{E(S["city"])}, {S["region"]} {S["zip"]}<br>
<a class="ph" href="{TEL}">{S["phone_display"]}</a>CSLB Lic. #{S["license"]}</address>
<div class="btns"><a class="btn pri" href="{TEL}">{IC["phone"]}Call</a><a class="btn sec" href="{SMS}">{IC["text"]}Text</a></div></div>
<div class="card"><h2>Services</h2><ul class="links">{svc}</ul></div>
<div class="card"><h2>Areas we serve</h2><ul class="links">{cities}</ul></div>
</aside>"""


def footer():
    svc = "".join(f'<li><a href="{u}">{E(n)}</a></li>' for _, _, _, _, subs in SERVICES for u, n in subs)
    cities = '<li><a href="/">San Ramon</a></li>' + "".join(f'<li><a href="{u}">{E(n)}</a></li>' for u, n in CITY_PAGES)
    co = "".join(f'<li><a href="{u}">{n}</a></li>' for u, n in [
        ("/about-us/", "About"), ("/gallery/", "Gallery"), ("/reviews/", "Reviews"), ("/types-of-roofing/", "Shingle vs tile"),
        ("/roofing-faq/", "Roofing FAQ"), ("/contact-us/", "Contact"), ("/privacy-policy/", "Privacy Policy")])
    return f"""<footer class="site"><div class="wrap"><div class="grid">
<div><h2>{E(S["name"])}</h2><address class="nap">{E(S["name"])} · {E(S["street"])}, {E(S["city"])}, {S["region"]} {S["zip"]}<br>
<a href="{TEL}">{S["phone_display"]}</a> · <a href="{MAILTO}">{S["email"]}</a><br>
CSLB Lic. #{S["license"]} ({E(S["license_class"])}) · <a href="{S["license_url"]}" rel="noopener">verify</a></address></div>
<div><h2>Services</h2><ul>{svc}</ul></div>
<div><h2>Areas</h2><ul>{cities}</ul></div>
<div><h2>Company</h2><ul>{co}</ul></div>
</div><div class="legal">© {YEAR} {E(S["name"])} · Roofing contractor in San Ramon, CA since 1995</div></div></footer>
<div class="callbar"><a class="c" href="{TEL}">{IC["phone"]}Call {S["phone_display"]}</a><a class="t" href="{SMS}">{IC["text"]}Text</a></div>
</body>
</html>
"""


def render_page(pg, css_href):
    body = render_body(pg.get("body", ""))
    lead = inline(pg["lead"]) if pg.get("lead") else ""
    if pg.get("layout") == "home":
        hero = pg["hero"]
        main = f"""<main id="main">
<section class="hero"><div class="wrap"><div class="txt">
<h1>{E(pg["h1"])}</h1><p class="lead">{lead}</p>
<div class="btns"><a class="btn pri" href="{TEL}">{IC["phone"]}Call {S["phone_display"]}</a><a class="btn sec" href="{SMS}">{IC["text"]}Text a photo</a></div>
</div><div class="img">{img_tag(hero, hero_sizes(pg), eager=True)}</div></div></section>
<div class="trust"><div class="wrap"><ul><li>In business since July 1995</li><li>CSLB Lic. #{S["license"]}, C-39</li><li>Owner answers the phone</li><li>Shingle, tile &amp; gutters</li></ul></div></div>
<div class="wrap"><div class="cols"><div class="body">{body}</div>{aside(pg)}</div></div>
</main>"""
    else:
        trail = crumbs_for(pg["path"])
        crumbs = " › ".join(f'<a href="{u}">{E(n)}</a>' for u, n in trail[:-1]) + f" › <span>{E(trail[-1][1])}</span>"
        heroimg = f'<div class="heroimg">{img_tag(pg["hero"], hero_sizes(pg), eager=True)}</div>' if pg.get("hero") else ""
        main = f"""<main id="main"><div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb">{crumbs}</nav>
<div class="pagehead"><h1>{E(pg["h1"])}</h1>{f'<p class="lead">{lead}</p>' if lead else ''}</div>
{heroimg}
<div class="cols"><div class="body">{body}</div>{aside(pg)}</div>
</div></main>"""
    return head(pg, css_href) + "\n" + header(pg) + "\n" + main + "\n" + footer()


# ---------------------------------------------------------------- write site
def clean_out():
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f in KEEP:
            continue
        p = os.path.join(OUT, f)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)


def write(rel, text):
    p = os.path.join(OUT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    clean_out()
    build_photos()
    css = open(os.path.join(ROOT, "src", "site.css"), encoding="utf-8").read()
    ver = hashlib.md5(css.encode()).hexdigest()[:8]
    write("/assets/site.css", css)
    css_href = f"/assets/site.css?v={ver}"
    write("/favicon.svg", IC["logo"].replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))

    for pg in C.PAGES:
        write(pg["path"] + "index.html", render_page(pg, css_href))

    nf = {"path": "/404/", "label": "Not found", "noindex": True, "title": "Page not found | CJ's Roofing",
          "h1": "Page not found", "description": "This page doesn't exist.",
          "lead": "That page isn't here. Try the [home page](/) or call Chris at {call}.", "body": "[[services]]"}
    PAGE_BY_PATH["/404/"] = nf
    write("/404.html", render_page(nf, css_href))

    today = datetime.date.today().isoformat()
    urls = "".join(f"<url><loc>{DOMAIN}{p['path']}</loc><lastmod>{today}</lastmod></url>"
                   for p in C.PAGES if p.get("in_sitemap", True))
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    if INDEXABLE:
        write("/robots.txt", f"User-agent: *\nDisallow: /thank-you/\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    else:
        write("/robots.txt", "# DRAFT — not approved yet. Flip INDEXABLE in build.py to open the site to search engines.\nUser-agent: *\nDisallow: /\n")
    print(f"built {len(C.PAGES)} pages + 404 · {len(PHOTO_META)} photos · INDEXABLE={INDEXABLE} -> {OUT}")


if __name__ == "__main__":
    main()
