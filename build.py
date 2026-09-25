#!/usr/bin/env python3
"""
Builds roofingsanramonca.com into docs/ (GitHub Pages serves main:/docs).

    python3 build.py            # rebuild the whole site
    git add -A && git commit -m "..." && git push   # publish (live in ~1 min)

Words: content.py        Styles: src/site.css        Photos: src/photos/<slug>.jpg (+ a line in content.PHOTOS)
Needs: Python 3 + Pillow (pip install pillow). Nothing else.

Design: Shibga Media's default template, "site 1" (https://site1.roofingsitetemplate1.com/), adapted to
CJ's Roofing — utility bar + sticky header, split hero with a contact card, service strip, why-us icon
boxes, split about block, work photos, review band, service cards, areas, CTA band, footer, and the
floating Call/Text/Email/Reviews bar. Heading font: Teko (SIL OFL, self-hosted in src/fonts/).
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
# CONTACT FORM — posts to our lead handler on Hetzner (shibga-os: automations/webform/, site id
# "cjs-roofing"). The handler checks for spam, emails the lead to CJ's Roofing ("New Lead: <page>"),
# adds a row to the web-form tracking sheet, and redirects to /thank-you/. Who gets the email is set
# there (sites.yaml), not here. Same fields as every Shibga PPL form. Set to None to hide the form.
# Short version in the home hero card, full version on /contact-us/.
CONTACT_FORM = {"action": "https://desk.5-223-88-156.sslip.io/webform/cjs-roofing"}
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
_O = 'viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
IC = {
    "phone": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
    "text": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 3h16a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 1-2zm3 6v2h2V9zm4 0v2h2V9zm4 0v2h2V9z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm9 7.2L4.5 7v1.9l7.5 5.1 7.5-5.1V7z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a7 7 0 0 1 7 7c0 5.2-7 13-7 13S5 14.2 5 9a7 7 0 0 1 7-7zm0 4.5A2.5 2.5 0 1 0 12 11.5 2.5 2.5 0 0 0 12 6.5z"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.5L12 17.3l-5.9 3.2 1.3-6.5L2.5 9.4l6.6-.8z"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 12.5l5 5 10-11"/></svg>',
    "burger": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
    "logo": '<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="4" fill="#a8391f"/><path d="M6 22 20 10l14 12" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M11 27.5 20 20l9 7.5" fill="none" stroke="#f0b541" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "shingle": f'<svg {_O}><path d="M4 24 24 7l20 17"/><path d="M11 22h26M9 28h30M8 34h32"/><path d="M17 22v6M31 22v6M13 28v6M24 28v6M35 28v6"/></svg>',
    "tile": f'<svg {_O}><path d="M4 24 24 7l20 17"/><path d="M8 30c2.5-4 5.5-4 8 0s5.5 4 8 0 5.5-4 8 0 5.5 4 8 0"/><path d="M8 38c2.5-4 5.5-4 8 0s5.5 4 8 0 5.5-4 8 0 5.5 4 8 0"/></svg>',
    "gutters": f'<svg {_O}><path d="M4 14h40"/><path d="M6 18h36v5a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3z"/><path d="M34 26v14"/><path d="M34 40h6"/><path d="M20 32c0 2-1.5 3.5-3 3.5S14 34 14 32s3-6 3-6 3 4 3 6z"/></svg>',
    "owner": f'<svg {_O}><circle cx="24" cy="15" r="7"/><path d="M10 41c1.5-8 7-12 14-12s12.5 4 14 12"/></svg>',
    "focus": f'<svg {_O}><circle cx="24" cy="24" r="17"/><circle cx="24" cy="24" r="9"/><circle cx="24" cy="24" r="1.5" fill="currentColor"/></svg>',
    "badge": f'<svg {_O}><path d="M24 4l16 6v12c0 10-7 18-16 22C15 40 8 32 8 22V10z"/><path d="M16.5 24l5 5 10-11"/></svg>',
    "local": f'<svg {_O}><path d="M24 44s14-13 14-24a14 14 0 0 0-28 0c0 11 14 24 14 24z"/><circle cx="24" cy="20" r="5"/></svg>',
}

TEL = f'tel:{S["phone_tel"]}'
SMS = f'sms:{S.get("sms_tel", S["phone_tel"])}'
MAILTO = f'mailto:{S["email"]}'

SERVICES = [  # home + services hub cards: icon, url, name, blurb, sub-pages, card photo (None = icon panel)
    ("tile", "/services/tile-roofing/", "Tile Roofing",
     "Concrete and clay tile: broken and slipped tiles, leaks, underlayment problems, re-roofs.",
     [("/services/tile-roofing/tile-roof-repair/", "Tile roof repair"),
      ("/services/tile-roofing/tile-roof-replacement/", "Tile roof replacement")], "tile-roof-dublin-closeup"),
    ("shingle", "/services/shingle-roofing/", "Shingle Roofing",
     "Asphalt shingle roofs: leaks, missing and worn shingles, flashing, full replacement.",
     [("/services/shingle-roofing/shingle-roof-repair/", "Shingle roof repair"),
      ("/services/shingle-roofing/shingle-roof-replacement/", "Shingle roof replacement")], "shingle-roof-newark-vents"),
    ("gutters", "/services/gutters/", "Gutters",
     "New gutters and downspouts, and repairs to leaking, sagging or loose gutters.",
     [("/services/gutters/seamless-gutter-installation/", "Seamless gutter installation"),
      ("/services/gutters/gutter-repair/", "Gutter repair")], None),
]
CITY_PAGES = [("/dublin/", "Dublin"), ("/danville/", "Danville"), ("/pleasanton/", "Pleasanton"),
              ("/alamo/", "Alamo"), ("/castro-valley/", "Castro Valley"), ("/fremont/", "Fremont")]

# Home "recent work" strip (site 1's gallery row) — CJ's own photos only.
HOME_WORK = ["tile-roof-repair-dublin-replacement-tiles", "shingle-roof-newark-rooftops",
             "concrete-tile-roof-solar-prep-3", "tile-roof-dublin-ridge"]
WHY_ICONS = ["owner", "focus", "badge", "local"]
CONTACT_PHOTO = "tile-roof-dublin-ridge-2"
REVIEW_PHOTO = "tile-roof-dublin-ridge-2"

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


def two_tone(t):
    """Site 1 headings: dark words + a brand-coloured phrase. 'A — B' colours B; else the last word(s)."""
    if " — " in t:
        a, b = t.split(" — ", 1)
        return f'{E(a)} <span class="hl">{E(b)}</span>'
    w = t.split()
    n = 2 if len(w) >= 4 else 1
    if len(w) < 2:
        return E(t)
    return f'{E(" ".join(w[:-n]))} <span class="hl">{E(" ".join(w[-n:]))}</span>'


def call_btns(text_label="Text a photo", call_label=None):
    call_label = call_label or f'Call {S["phone_display"]}'
    return (f'<div class="btns"><a class="btn pri" href="{TEL}">{IC["phone"]}{call_label}</a>'
            f'<a class="btn ghost" href="{SMS}">{IC["text"]}{text_label}</a></div>')


def cta_box(title="Talk to Chris about your roof"):
    """Inline version (mid-page): site 1's highlighted CTA note."""
    return (f'<div class="note"><h2>{E(title)}</h2>'
            f'<p>Call or text {E(S["phone_display"])}. You\'ll reach the owner, not a call center.</p>{call_btns()}</div>')


def cta_band(title="Talk to Chris about your roof"):
    """Full-width version (end of page): site 1's red band with a white box."""
    return (f'<section class="ctaband"><div class="wrap"><div class="ctabox"><h2>{E(title)}</h2>'
            f'<p>Call or text {E(S["phone_display"])}. You\'ll reach the owner, not a call center.</p>'
            f'{call_btns()}</div></div></section>')


def services_cards():
    out = ['<div class="svc">']
    for icon, url, name, blurb, subs, photo in SERVICES:
        top = (f'<a class="svc-img" href="{url}" tabindex="-1" aria-hidden="true">'
               f'{img_tag(photo, "(min-width:960px) 360px, (min-width:600px) 33vw, 100vw")}</a>' if photo else
               f'<a class="svc-img icon" href="{url}" tabindex="-1" aria-hidden="true">{IC[icon]}</a>')
        links = "".join(f'<li><a href="{u}">{E(n)}</a></li>' for u, n in subs)
        out.append(f'<article class="svc-card">{top}<div class="svc-body"><h3><a href="{url}">{E(name)}</a></h3>'
                   f'<p>{E(blurb)}</p><ul class="sq">{links}</ul>'
                   f'<a class="btn pri sm" href="{url}">{E(name)} &rsaquo;</a></div></article>')
    out.append("</div>")
    return "".join(out)


def cities_list():
    items = [f'<li><a href="/">{IC["pin"]}<b>San Ramon</b><span>Home base</span></a></li>']
    items += [f'<li><a href="{u}">{IC["pin"]}<b>{E(n)}</b><span>Roofing in {E(n)}</span></a></li>' for u, n in CITY_PAGES]
    return (f'<ul class="cities" id="areas">{"".join(items)}</ul>'
            f'<p>We also work across the greater Bay Area. Not sure if you\'re in range? Call {inline("{call}")}.</p>')


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
    return '<div class="faq">' + "".join(f'<div class="qa"><h3>{E(q)}</h3><p>{inline(a)}</p></div>' for q, a in C.FAQ) + "</div>"


def review_links():
    return (f'<div class="contact"><a class="card" href="{S["google_maps"]}" rel="noopener">{IC["star"]}<div><b>Google</b>'
            f'<span>CJ\'s Roofing on Google Maps</span></div></a>'
            f'<a class="card" href="{S["yelp"]}" rel="noopener">{IC["star"]}<div><b>Yelp</b><span>CJ\'s Roofing on Yelp</span></div></a></div>')


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


def contact_form(short=False):
    """The lead form. Field names match every Shibga PPL form (name, email, phone, zipcode, message).
    `website` is a honeypot; page_url / page_title / t_ms are filled by the one-line script below."""
    if not CONTACT_FORM:
        return ""
    fid = "qf" if short else "cf"
    def fld(name, label, typ="text", auto="", req=True, half=False):
        a = f' autocomplete="{auto}"' if auto else ""
        r = " required" if req else ""
        extra = ' inputmode="numeric" pattern="[0-9]{5}" maxlength="5"' if name == "zipcode" else ""
        return (f'<label class="fl{" half" if half else ""}"><span>{label}</span>'
                f'<input id="{fid}-{name}" name="{name}" type="{typ}"{a}{r}{extra}></label>')
    email = "" if short else fld("email", "Email", "email", "email")
    head = "" if short else "<h2>Request a free estimate</h2>"
    return (f'<form class="{"qform" if short else "card form"}" id="{fid}" method="post" action="{E(CONTACT_FORM["action"])}">{head}'
            + fld("name", "Full name", auto="name")
            + email
            + fld("phone", "Phone number", "tel", "tel", half=True)
            + fld("zipcode", "Zip code", auto="postal-code", half=True)
            + f'<label class="fl"><span>Briefly, how can we help?</span><textarea id="{fid}-message" name="message" rows="{2 if short else 4}" required></textarea></label>'
            + '<label class="hp" aria-hidden="true">Website<input name="website" tabindex="-1" autocomplete="off"></label>'
            + '<input type="hidden" name="page_url"><input type="hidden" name="page_title"><input type="hidden" name="t_ms">'
            + f'<button class="btn pri lg" type="submit">{"Get my free estimate" if short else "Send request"}</button>'
            + f'<p class="fine">Goes straight to CJ\'s Roofing. We\'ll call or text you back. See our <a href="/privacy-policy/">privacy policy</a>.</p>'
            + "</form>"
            + f'<script>(function(){{var t=Date.now(),f=document.getElementById("{fid}");f.addEventListener("submit",function(){{'
              'f.page_url.value=location.href;f.page_title.value=document.title;f.t_ms.value=Date.now()-t;});})();</script>')


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
            out.append('<ul class="sq">' + "".join(f"<li>{inline(l.strip()[2:])}</li>" for l in b.splitlines()) + "</ul>")
        else:
            out.append(f"<p>{inline(' '.join(l.strip() for l in b.splitlines()))}</p>")
    return "\n".join(out)


def split_trailing_cta(text):
    """A page body ending in [[cta]] gets site 1's full-width CTA band instead of an inline box."""
    t = text.strip()
    if t.endswith("[[cta]]"):
        return t[: -len("[[cta]]")].rstrip(), True
    return t, False


def home_sections(text):
    """Home body -> [(heading or None, raw block text)] split on '## ' headings."""
    secs, cur_h, cur = [], None, []
    for block in re.split(r"\n\s*\n", text.strip()):
        b = block.strip()
        if b.startswith("## "):
            if cur_h or cur:
                secs.append((cur_h, "\n\n".join(cur)))
            cur_h, cur = b[3:], []
        elif b:
            cur.append(b)
    if cur_h or cur:
        secs.append((cur_h, "\n\n".join(cur)))
    return secs


# ---------------------------------------------------------------- schema
def business_ld():
    return {
        "@context": "https://schema.org", "@type": "RoofingContractor", "@id": f"{DOMAIN}/#business",
        "name": S["name"], "url": f"{DOMAIN}/", "telephone": "+1-925-205-6447", "email": S["email"],
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
def lcp_photo(pg):
    if pg.get("layout") == "contact":
        return None
    return pg.get("hero")


def hero_sizes(pg):
    return "(min-width:960px) 50vw, 100vw" if pg.get("layout") == "home" else "(min-width:960px) 45vw, 100vw"


def head(pg, css_href, font_href):
    robots = "noindex, nofollow" if (not INDEXABLE or pg.get("noindex")) else "index, follow"
    canon = DOMAIN + pg["path"]
    og_img = pg.get("hero") or "tile-roof-dublin-hills"
    og_url = DOMAIN + PHOTO_META[og_img]["sizes"][-1][1]
    preload = f'<link rel="preload" href="{font_href}" as="font" type="font/woff2" crossorigin>\n'
    lp = lcp_photo(pg)
    if lp:
        m = PHOTO_META[lp]
        preload += (f'<link rel="preload" as="image" href="{m["sizes"][0][1]}" '
                    f'imagesrcset="{", ".join(f"{u} {w}w" for w, u in m["sizes"])}" '
                    f'imagesizes="{hero_sizes(pg)}" fetchpriority="high">\n')
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
<meta name="theme-color" content="#a8391f">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{preload}<link rel="stylesheet" href="{css_href}">
{ld_scripts(pg)}
</head>"""


def logo_html():
    return (f'<a class="logo" href="/" aria-label="CJ\'s Roofing home">{IC["logo"]}'
            f'<span><b>CJ\'S ROOFING</b><small>San Ramon · Since 1995</small></span></a>')


def header(pg):
    cur = pg["path"]
    ac = lambda u: ' aria-current="page"' if u == cur else ""
    svc_sub = "".join(f'<a href="{u}"{ac(u)}>{E(n)}</a>' + "".join(f'<a class="sub" href="{su}"{ac(su)}>{E(sn)}</a>' for su, sn in subs)
                      for _, u, n, _, subs, _ in SERVICES)
    svc_sub = f'<a href="/services/"{ac("/services/")}>All services</a>' + svc_sub + f'<a href="/types-of-roofing/"{ac("/types-of-roofing/")}>Shingle vs tile</a>'
    area_sub = f'<a href="/">San Ramon</a>' + "".join(f'<a href="{u}"{ac(u)}>{E(n)}</a>' for u, n in CITY_PAGES)
    in_svc = cur.startswith("/services/") or cur == "/types-of-roofing/"
    in_area = cur in dict(CITY_PAGES)
    desk = (f'<a href="/"{ac("/")}>Home</a><a href="/about-us/"{ac("/about-us/")}>About</a>'
            f'<div class="dd"><a href="/services/"{" class=on" if in_svc else ""}>Services</a><div class="ddm">{svc_sub}</div></div>'
            f'<div class="dd"><a href="/#areas"{" class=on" if in_area else ""}>Areas</a><div class="ddm">{area_sub}</div></div>'
            f'<a href="/gallery/"{ac("/gallery/")}>Gallery</a><a href="/reviews/"{ac("/reviews/")}>Reviews</a>'
            f'<a href="/roofing-faq/"{ac("/roofing-faq/")}>FAQ</a><a href="/contact-us/"{ac("/contact-us/")}>Contact</a>')
    mob = ['<a href="/">Home</a>', '<a href="/about-us/">About</a>', '<a href="/services/">Services</a>']
    for _, u, n, _, subs, _ in SERVICES:
        mob.append(f'<a class="sub" href="{u}">{E(n)}</a>')
    mob += ['<a href="/gallery/">Gallery</a>', '<a href="/reviews/">Reviews</a>', '<a href="/roofing-faq/">FAQ</a>',
            '<a href="/contact-us/">Contact</a>', '<span class="mh">Areas we serve</span>']
    mob += [f'<a class="sub" href="{u}">Roofing in {E(n)}</a>' for u, n in CITY_PAGES]
    mob.append('<a class="sub" href="/types-of-roofing/">Shingle vs tile</a><a class="sub" href="/privacy-policy/">Privacy Policy</a>')
    mob.append(f'<a class="btn pri" href="{TEL}">{IC["phone"]}Call {S["phone_display"]}</a>')
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap"><span>{IC["pin"]}{E(S["street"])}, {E(S["city"])}, {S["region"]}</span><span>CSLB Lic. #{S["license"]} · Since July 1995</span><a href="{TEL}">{IC["phone"]}Call or text {S["phone_display"]}</a></div></div>
<header class="site"><div class="wrap">
<a class="m-call" href="{TEL}" aria-label="Call CJ's Roofing {S["phone_display"]}">{IC["phone"]}<span>Call</span></a>
{logo_html()}
<nav class="desk" aria-label="Main">{desk}</nav>
<a class="btn pri hdr-cta" href="{TEL}">{IC["phone"]}{S["phone_display"]}</a>
<details class="menu"><summary>{IC["burger"]}<span>Menu</span></summary><nav aria-label="Mobile">{"".join(mob)}</nav></details>
</div></header>"""


def aside(pg):
    cur = pg["path"]
    svc = ""
    for _, u, n, _, subs, _ in SERVICES:
        svc += f'<li><a href="{u}"' + (' aria-current="page"' if u == cur else "") + f">{E(n)}</a></li>"
        svc += "".join(f'<li class="sub"><a href="{su}"' + (' aria-current="page"' if su == cur else "") + f">{E(sn)}</a></li>" for su, sn in subs)
    cities = '<li><a href="/">San Ramon</a></li>' + "".join(
        f'<li><a href="{u}"' + (' aria-current="page"' if u == cur else "") + f">{E(n)}</a></li>" for u, n in CITY_PAGES)
    return f"""<aside>
<div class="card callcard"><h2>Call Chris</h2><address class="nap"><strong>{E(S["name"])}</strong><br>{E(S["street"])}<br>{E(S["city"])}, {S["region"]} {S["zip"]}<br>
<a class="ph" href="{TEL}">{S["phone_display"]}</a>CSLB Lic. #{S["license"]}</address>
<div class="btns"><a class="btn pri" href="{TEL}">{IC["phone"]}Call</a><a class="btn ghost" href="{SMS}">{IC["text"]}Text</a></div></div>
<div class="card side"><h2>Services</h2><ul class="links">{svc}</ul></div>
<div class="card side"><h2>Areas we serve</h2><ul class="links">{cities}</ul></div>
</aside>"""


def reviews_band():
    return f"""<section class="revband"><svg class="divider" viewBox="0 0 1000 60" preserveAspectRatio="none" aria-hidden="true"><polygon points="0,44 1000,6 1000,16 0,54" fill="#a8391f"/><polygon points="0,54 1000,16 1000,24 0,60" fill="#1b1f24"/><polygon points="0,60 1000,24 1000,60" fill="#f0b541"/></svg><div class="wrap"><div class="rev-in">
<div class="rev-img">{img_tag(REVIEW_PHOTO, "(min-width:960px) 340px, 240px")}</div>
<div class="rev-txt"><h2>What our customers <span class="hl">say</span></h2>
<p>Most of CJ's Roofing's work comes from people recommended by past customers. Read what customers have written, with their names and dates, where they wrote it.</p>
<div class="btns"><a class="btn dark" href="{S["google_maps"]}" rel="noopener">{IC["star"]}Reviews on Google</a><a class="btn dark" href="{S["yelp"]}" rel="noopener">{IC["star"]}Reviews on Yelp</a></div></div>
</div></div></section>"""


def footer():
    svc = "".join(f'<li><a href="{u}">{E(n)}</a></li>' for _, _, _, _, subs, _ in SERVICES for u, n in subs)
    cities = '<li><a href="/">San Ramon</a></li>' + "".join(f'<li><a href="{u}">{E(n)}</a></li>' for u, n in CITY_PAGES)
    co = "".join(f'<li><a href="{u}">{n}</a></li>' for u, n in [
        ("/about-us/", "About"), ("/gallery/", "Gallery"), ("/reviews/", "Reviews"), ("/types-of-roofing/", "Shingle vs tile"),
        ("/roofing-faq/", "Roofing FAQ"), ("/contact-us/", "Contact")])
    return f"""<footer class="site"><div class="stripes" aria-hidden="true"></div><div class="wrap"><div class="grid">
<div class="fbrand">{logo_html()}<address class="nap">{E(S["street"])}<br>{E(S["city"])}, {S["region"]} {S["zip"]}<br>
<a href="{TEL}">{S["phone_display"]}</a><br><a href="{MAILTO}">{S["email"]}</a><br>
CSLB Lic. #{S["license"]} ({E(S["license_class"])}) · <a href="{S["license_url"]}" rel="noopener">verify</a></address>
<a class="btn pri" href="{TEL}">{IC["phone"]}Call {S["phone_display"]}</a></div>
<div><h2>Services</h2><ul class="sq">{svc}</ul></div>
<div><h2>Areas</h2><ul class="sq">{cities}</ul></div>
<div><h2>Company</h2><ul class="sq">{co}</ul></div>
</div></div><div class="legal"><div class="wrap"><span>© {YEAR} {E(S["name"])} · Roofing contractor in San Ramon, CA since 1995</span><a href="/privacy-policy/">Privacy Policy</a></div></div></footer>
<nav class="actbar" aria-label="Quick contact"><a href="{TEL}">{IC["phone"]}<span>Call</span></a><a href="{SMS}">{IC["text"]}<span>Text</span></a><a href="{MAILTO}">{IC["mail"]}<span>Email</span></a><a href="/reviews/">{IC["star"]}<span>Reviews</span></a></nav>
</body>
</html>
"""


# ---------------------------------------------------------------- home (site 1 section order)
def render_home(pg):
    hero = pg["hero"]
    card_body = (contact_form(short=True)
                 + f'<p class="or">Or call / text Chris: <a href="{TEL}">{E(S["phone_display"])}</a></p>') if CONTACT_FORM else (
        f'<p>Call or text {E(S["phone_display"])}. You\'ll reach the owner, not a call center. '
        f'Texting? Add a couple of photos of the problem area and your address.</p>'
        f'<ul class="ticks"><li>{IC["check"]}In business since July 1995</li>'
        f'<li>{IC["check"]}CSLB Lic. #{S["license"]}, C-39 Roofing</li>'
        f'<li>{IC["check"]}Shingle roofs, tile roofs &amp; gutters</li></ul>{call_btns(call_label="Call Chris")}')
    strip = "".join(f'<a href="{u}">{IC[i]}<span>{E(n)}</span></a>' for i, u, n, _, _, _ in SERVICES)
    out = [f"""<main id="main">
<section class="hero"><div class="hero-media slash"><div class="hm">{img_tag(hero, hero_sizes(pg), eager=True)}</div></div>
<div class="wrap hero-grid"><div class="hero-txt">
<p class="eyebrow">Owner-run roofing · San Ramon, CA</p>
<h1>{two_tone(pg["h1"])}</h1>
<p class="lead">{inline(pg["lead"])}</p>
<a class="hero-phone" href="{TEL}">{IC["phone"]}{S["phone_display"]}</a>
<div class="btns"><a class="btn pri lg" href="{TEL}">Call Chris today</a></div>
</div>
<div class="hero-card"><h2>Talk to Chris about your roof</h2><span class="bar" aria-hidden="true"></span>{card_body}</div>
</div></section>
<div class="wrap"><nav class="strip" aria-label="Services">{strip}</nav></div>"""]

    body, trailing_cta = split_trailing_cta(pg["body"])
    for h, raw in home_sections(body):
        key = slugify(h or "")
        if "[[services]]" in raw:
            rest = render_body(raw.replace("[[services]]", "").strip()) if raw.replace("[[services]]", "").strip() else ""
            svc_block = f"""<section class="band" id="{key}"><div class="wrap">
<h2 class="sec">{two_tone(h)}</h2>{services_cards()}{rest}</div></section>"""
            out.append(("svc", svc_block))
        elif "[[cities]]" in raw:
            out.append(("areas", f"""<section class="band areas" id="{key}"><div class="wrap">
<h2 class="sec">{two_tone(h)}</h2>{render_body(raw)}</div></section>"""))
        elif raw and all(l.strip().startswith("- **") for l in raw.splitlines()):
            boxes = []
            for i, l in enumerate(raw.splitlines()):
                m = re.match(r"-\s*\*\*(.+?)\*\*\s*(.*)", l.strip())
                title, txt = m.group(1).rstrip("."), m.group(2)
                boxes.append(f'<div class="ibox">{IC[WHY_ICONS[i % len(WHY_ICONS)]]}<h3>{E(title)}</h3><p>{inline(txt)}</p></div>')
            out.append(("why", f"""<section class="band grey why" id="{key}"><div class="wrap why-grid">
<div class="why-l"><h2 class="sec">{two_tone(h)}</h2><div class="why-img">{img_tag("tile-roof-dublin-ridge", "(min-width:960px) 440px, 100vw")}</div></div>
<div class="iboxes">{"".join(boxes)}</div></div></section>"""))
        else:
            m = re.search(r"\[\[photos?:([^\]]+)\]\]", raw)
            photos = [s.strip() for s in m.group(1).split(",")] if m else []
            text = re.sub(r"\[\[photos?:[^\]]+\]\]", "", raw).strip()
            side = img_tag(photos[0], "(min-width:960px) 460px, 100vw") if photos else ""
            more = ('<div class="photos two">' + "".join(figure(s, "(min-width:960px) 280px, 50vw") for s in photos[1:]) + "</div>") if len(photos) > 1 else ""
            out.append(("about", f"""<section class="band about" id="{key}"><div class="wrap about-grid">
<div class="about-img">{side}</div>
<div class="about-txt"><h2 class="sec">{two_tone(h)}</h2><div class="dropcap">{render_body(text)}</div>{more}</div>
</div></section>"""))

    # site 1 order: why-us, about, work photos, reviews, service cards, (areas), CTA
    order = {"why": 0, "about": 1, "svc": 3, "areas": 4}
    secs = list(out[1:])
    work = f"""<section class="band grey work"><div class="wrap">
<h2 class="sec center">Recent roofing <span class="hl">work</span></h2>
<div class="gal four">{"".join(figure(s, "(min-width:960px) 270px, 50vw") for s in HOME_WORK)}</div>
<p class="center"><a class="btn pri" href="/gallery/">See all project photos</a></p></div></section>"""
    secs.append(("work", work))
    order["work"] = 2
    secs.sort(key=lambda kv: order.get(kv[0], 9))
    html_secs = []
    for kind, block in secs:
        html_secs.append(block)
        if kind == "work":
            html_secs.append(reviews_band())
    return out[0] + "\n" + "\n".join(html_secs) + ("\n" + cta_band() if trailing_cta else "") + "\n</main>"


# ---------------------------------------------------------------- inner pages
def page_hero(pg):
    trail = crumbs_for(pg["path"])
    crumbs = " / ".join(f'<a href="{u}">{E(n)}</a>' for u, n in trail[:-1]) + f" / <span>{E(trail[-1][1])}</span>"
    lead = f'<p class="lead">{inline(pg["lead"])}</p>' if pg.get("lead") else ""
    if pg.get("hero"):
        media = f'<div class="phero-media slash"><div class="hm">{img_tag(pg["hero"], hero_sizes(pg), eager=True)}</div></div>'
    else:
        icon = IC.get(pg.get("service") or "", IC["tile"])
        media = f'<div class="phero-media slash" aria-hidden="true"><div class="hm icon">{icon}</div></div>'
    return f"""<section class="phero">{media}<div class="wrap"><div class="phero-txt">
<nav class="crumbs" aria-label="Breadcrumb">{crumbs}</nav>
<h1>{two_tone(pg["h1"])}</h1>{lead}{call_btns()}
</div></div></section>"""


def render_contact(pg):
    trail = crumbs_for(pg["path"])
    crumbs = " / ".join(f'<a href="{u}">{E(n)}</a>' for u, n in trail[:-1]) + f" / <span>{E(trail[-1][1])}</span>"
    return f"""<main id="main"><section class="csplit"><div class="csplit-txt">
<nav class="crumbs" aria-label="Breadcrumb">{crumbs}</nav>
<h1>{two_tone(pg["h1"])}</h1><p class="lead">{inline(pg["lead"])}</p>
{render_body(pg["body"])}
</div><div class="csplit-img">{img_tag(CONTACT_PHOTO, "(min-width:960px) 48vw, 100vw")}</div></section></main>"""


def render_page(pg, css_href, font_href):
    if pg.get("layout") == "home":
        main = render_home(pg)
    elif pg.get("layout") == "contact":
        main = render_contact(pg)
    else:
        body, trailing = split_trailing_cta(pg.get("body", ""))
        wide = "[[gallery]]" in body
        inner = f'<div class="body{" wide" if wide else ""}">{render_body(body)}</div>'
        cols = f'<div class="cols{" one" if wide else ""}">{inner}{"" if wide else aside(pg)}</div>'
        rev = reviews_band() if (pg.get("service") or pg.get("city")) else ""
        main = (f'<main id="main">{page_hero(pg)}\n<div class="wrap">{cols}</div>\n{rev}'
                + (cta_band() if trailing else "") + "</main>")
    return head(pg, css_href, font_href) + "\n" + header(pg) + "\n" + main + "\n" + footer()


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
    font_src = os.path.join(ROOT, "src", "fonts", "teko-latin.woff2")
    fver = hashlib.md5(open(font_src, "rb").read()).hexdigest()[:8]
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    shutil.copyfile(font_src, os.path.join(OUT, "assets", "teko-latin.woff2"))
    font_href = f"/assets/teko-latin.woff2?v={fver}"
    css = open(os.path.join(ROOT, "src", "site.css"), encoding="utf-8").read().replace("{FONT}", font_href)
    ver = hashlib.md5(css.encode()).hexdigest()[:8]
    write("/assets/site.css", css)
    css_href = f"/assets/site.css?v={ver}"
    write("/favicon.svg", IC["logo"].replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))

    for pg in C.PAGES:
        write(pg["path"] + "index.html", render_page(pg, css_href, font_href))

    nf = {"path": "/404/", "label": "Not found", "noindex": True, "title": "Page not found | CJ's Roofing",
          "h1": "Page not found", "description": "This page doesn't exist.",
          "lead": "That page isn't here. Try the [home page](/) or call Chris at {call}.", "body": "[[services]]"}
    PAGE_BY_PATH["/404/"] = nf
    write("/404.html", render_page(nf, css_href, font_href))

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
