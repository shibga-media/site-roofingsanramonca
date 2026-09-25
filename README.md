# roofingsanramonca.com — CJ's Roofing (Shibga Media)

Static site, no WordPress. `docs/` is what is published (GitHub Pages from main/docs, custom domain via `docs/CNAME`).
Built and maintained by Shibga Media. Client: CJ's Roofing, San Ramon CA. Never put keys or private data here — this repo is public.

## Change anything

| To change | Edit | Then |
|---|---|---|
| Any words, titles, H1s, meta descriptions, FAQ, NAP | `content.py` | `python3 build.py`, commit, push |
| Look / colors / layout (Shibga default template "site 1", in CJ's colours; section templates in `build.py`) | `src/site.css` | same |
| Add job photos | put `<slug>.jpg` in `src/photos/` (his own photos only, never stock) and add a line to `PHOTOS` in `content.py` | same |
| Open the site to Google (after approval) | `INDEXABLE = True` in `build.py` | same |
| Add a contact form (once a working handler exists) | `CONTACT_FORM` in `build.py` | same |

`python3 build.py` regenerates all of `docs/` (keeps `CNAME`, `.nojekyll`). Needs Python 3 + Pillow. Push to `main` and it is live in about a minute.
