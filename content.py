# -*- coding: utf-8 -*-
"""
ALL the words on roofingsanramonca.com live in this file.
Edit here, then run:  python3 build.py   (it rewrites docs/)

Body text format (kept deliberately simple):
  ## Heading            -> section heading          ### Heading -> sub-heading
  - item                -> bullet list (consecutive lines)
  blank line            -> new paragraph
  **bold**  [link text](/path/)
  {call}  {text}  {email}   -> phone / text / email links
  [[photo:slug]]            -> one photo (slug = file name in src/photos without .jpg)
  [[photos:slug,slug,slug]] -> row of photos
  [[cta]]                   -> "call Chris" box
  [[services]]  [[cities]]  -> service cards / service-area links
  [[gallery]]               -> every photo in PHOTOS, grouped
  [[faq]]                   -> the FAQ list below

RULE: nothing goes on this site that CJ's Roofing hasn't told us or that isn't public record.
No invented reviews, prices, warranties, awards, brands or numbers.
"""

SITE = {
    "domain": "https://roofingsanramonca.com",
    "name": "CJ's Roofing",
    "owner": "Chris J Montano",
    "founded": "1995-07-17",
    "phone_display": "(925) 205-6447",
    "phone_tel": "+19252056447",
    "sms_tel": "+19255480932",       # texts go to Chris's mobile — the call-tracking number takes calls only
    "email": "customerservice@cjs-roofing.com",
    "street": "9672 Camassia Way",
    "city": "San Ramon",
    "region": "CA",
    "zip": "94582",
    "license": "709867",
    "license_class": "C-39 Roofing",
    "license_url": "https://www.cslb.ca.gov/709867",
    "google_maps": "https://www.google.com/maps?cid=6682285383229526502",
    "google_review": "https://search.google.com/local/writereview?placeid=ChIJzXHnZgnyj4AR5lEu2yY_vFw",
    "yelp": "https://www.yelp.com/biz/cjs-roofing-san-ramon-2",
    "areas": ["San Ramon", "Fremont", "Pleasanton", "Dublin", "Danville", "Alamo", "Castro Valley"],
}

# Photos: only CJ's Roofing's own job photos (from his old website + Facebook page).
# Never add stock photos. Location/date come from the photo files (found by us).
PHOTOS = {
    "tile-roof-dublin-hills": {
        "alt": "Concrete S-tile roof with vents and ridge tiles, green hills behind, Dublin CA",
        "caption": "Tile roof, Dublin, April 2024", "group": "Tile roofs"},
    "tile-roof-dublin-ridge": {
        "alt": "Tile roof ridge on a Dublin home with the neighborhood and hills below",
        "caption": "Tile roof, Dublin, April 2024", "group": "Tile roofs"},
    "tile-roof-dublin-closeup": {
        "alt": "Close view of S-shaped roof tiles meeting at a hip on a Dublin home",
        "caption": "Tile hip and field tiles, Dublin, April 2024", "group": "Tile roofs"},
    "tile-roof-dublin-ridge-2": {
        "alt": "Tan tile roof ridge with trees and lawns behind it, Dublin CA",
        "caption": "Tile roof, Dublin, April 2024", "group": "Tile roofs"},
    "tile-roof-repair-dublin-vents": {
        "alt": "Tile roof with vent pipes and a few tiles out of place during repair, Dublin CA",
        "caption": "Tile roof repair in progress, Dublin, April 2024", "group": "Tile roofs"},
    "tile-roof-repair-dublin-replacement-tiles": {
        "alt": "New replacement roof tiles staged on an older tile roof during repair, Dublin CA",
        "caption": "Replacement tiles staged on the roof, Dublin, April 2024", "group": "Tile roofs"},
    "tile-roof-repair-dublin-staged-tiles": {
        "alt": "Brown tile roof with stacked replacement tiles ready to set, Dublin CA",
        "caption": "Tile repair, Dublin, April 2024", "group": "Tile roofs"},
    "tile-roof-san-ramon-tiles-lifted": {
        "alt": "Tile roof in San Ramon with tiles lifted and stacked, old underlayment exposed",
        "caption": "Tiles lifted, old underlayment exposed, San Ramon, March 2024", "group": "Tile roofs"},
    "tile-roof-new-underlayment": {
        "alt": "New black underlayment installed on a roof section with tiles stacked beside it",
        "caption": "New underlayment going down under a tile roof, March 2024", "group": "Tile roofs"},
    "tile-roof-new-underlayment-battens": {
        "alt": "New underlayment with wood battens ready for tiles to be set back in place",
        "caption": "New underlayment and battens before the tiles go back, March 2024", "group": "Tile roofs"},
    "shingle-roof-newark-vents": {
        "alt": "Gray asphalt shingle roof with vent pipes and a ridge line in Newark CA",
        "caption": "Asphalt shingle roof, Newark, April 2024", "group": "Shingle roofs"},
    "shingle-roof-newark-ridge": {
        "alt": "Asphalt shingle roof with ridge vent and vent pipes over a Newark neighborhood",
        "caption": "Shingle roof and ridge vent, Newark, April 2024", "group": "Shingle roofs"},
    "shingle-roof-newark-street": {
        "alt": "Shingle roof edge with the street and neighboring houses below, Newark CA",
        "caption": "Shingle roof, Newark, April 2024", "group": "Shingle roofs"},
    "shingle-roof-newark-rooftops": {
        "alt": "Several gray asphalt shingle roof planes meeting at hips and valleys, Newark CA",
        "caption": "Shingle roof planes, Newark, April 2024", "group": "Shingle roofs"},
    "shingle-roof-newark-ridge-2": {
        "alt": "Asphalt shingle roof ridge with roof vents, neighborhood in the background",
        "caption": "Shingle roof, Newark, April 2024", "group": "Shingle roofs"},
    "concrete-tile-roof-solar-prep-1": {
        "alt": "Flat concrete tile roof after pressure washing, hillside homes behind",
        "caption": "Concrete tile roof washed for solar prep", "group": "Concrete tile, solar prep"},
    "concrete-tile-roof-solar-prep-2": {
        "alt": "Clean flat concrete tile roof ready for solar panels",
        "caption": "Concrete tile roof washed for solar prep", "group": "Concrete tile, solar prep"},
    "concrete-tile-roof-solar-prep-3": {
        "alt": "Concrete tile roof over a patio being washed before solar installation",
        "caption": "Concrete tile roof during washing for solar prep", "group": "Concrete tile, solar prep"},
    "concrete-tile-roof-solar-prep-4": {
        "alt": "Concrete tile roof ridge and hip after washing for solar",
        "caption": "Concrete tile roof washed for solar prep", "group": "Concrete tile, solar prep"},
}

FAQ = [
    ("Are you licensed?",
     "Yes. CJ's Roofing holds California contractor licence #709867, classification C-39 Roofing, issued "
     "in July 1995. You can check it yourself on the [CSLB website](https://www.cslb.ca.gov/709867)."),
    ("What kinds of roofs do you work on?",
     "Asphalt shingle roofs and tile roofs (concrete and clay), plus gutters. That's the whole list."),
    ("Do you install metal roofs?",
     "No. Metal panels scratch when people walk on them during work, and Chris would rather not hand "
     "you a roof that's marked up on day one. If you want metal, we're not the right company."),
    ("Do you do siding, remodeling or other home work?",
     "No. Roofing and gutters only."),
    ("Do you do repairs, or only full roofs?",
     "Both. Leaks, broken or slipped tiles, missing shingles, flashing and gutter problems are all "
     "repair work we take on. If a repair won't solve the problem, Chris will tell you."),
    ("Which areas do you cover?",
     "We're based in San Ramon and work across the Tri-Valley and the greater Bay Area, including "
     "[Dublin](/dublin/), [Pleasanton](/pleasanton/), [Danville](/danville/), [Alamo](/alamo/), "
     "[Castro Valley](/castro-valley/) and [Fremont](/fremont/). Not sure if you're in range? Call and ask."),
    ("Who will I be dealing with?",
     "Chris Montano, the owner. Calls to {call} ring straight through to his phone."),
    ("How do I get an estimate?",
     "Call or text Chris at {call}. If you text, add a couple of photos of the problem area and "
     "your address, and he'll get back to you."),
    ("Can you get my roof ready for solar panels?",
     "Solar prep is work CJ's Roofing has listed on its Google profile and shown on its Facebook page "
     "(the concrete tile photos in our [gallery](/gallery/) are from a solar-prep job). Call to talk "
     "through your roof before the solar company arrives."),
    ("How long have you been in business?",
     "Since July 17, 1995."),
]

# ---------------------------------------------------------------------------
# Pages. Order here = order in sitemap.xml.
# ---------------------------------------------------------------------------
PAGES = []

def page(**kw):
    PAGES.append(kw)


page(path="/", layout="home", label="Home",
     title="Roofing San Ramon, CA | Shingle & Tile Roofs | CJ's Roofing",
     h1="San Ramon Roofing Contractor — Shingle & Tile Roofs Since 1995",
     description="CJ's Roofing is a San Ramon roofing contractor since 1995: asphalt shingle and tile roof "
                 "repair and replacement, plus gutters. Owner-run. Call Chris at (925) 205-6447.",
     hero="tile-roof-dublin-hills",
     lead="CJ's Roofing is Chris Montano's roofing company, based on Camassia Way in San Ramon. Since 1995 "
          "Chris has repaired and replaced asphalt shingle and tile roofs, and put up and fixed gutters, "
          "for homeowners across the Tri-Valley and the greater Bay Area.",
     body="""
## What we do

[[services]]

## Why San Ramon homeowners call Chris

- **You talk to the owner.** Calls to this number ring straight through to Chris. The person you talk to is the person answering for the work.
- **We stick to what we know.** Shingle roofs, tile roofs and gutters. No metal roofs, no siding, no remodeling.
- **Licensed since 1995.** California contractor licence #709867, C-39 Roofing. [Check it on the CSLB site](https://www.cslb.ca.gov/709867).
- **Local.** San Ramon is home. Most of our service area is a short drive up or down I-680.

## Roofs in San Ramon

San Ramon's housing splits roughly in two. The older west side, around Twin Creeks, Montevideo, the Country Club area and the neighborhoods off Crow Canyon Road, was mostly built in the 1970s and 1980s, and a lot of those homes carry asphalt shingle roofs. The newer east side, including Canyon Lakes, Windemere, Gale Ranch and the rest of Dougherty Valley, went up from the late 1980s onward and has far more concrete tile.

Both have their own problems. San Ramon summers are hot and dry, and years of sun wear shingles down until they curl, crack and shed granules. Tile holds up to sun much better, but the tile is not what keeps the water out: the underlayment beneath it is, and that layer ages even when the tiles still look fine. Winter storms then find whatever has worn out.

Many San Ramon neighborhoods have homeowners associations with rules on roof material and color, so check with your HOA before you pick a new roof. A full re-roof also needs a building permit from the City of San Ramon.

[[photos:tile-roof-san-ramon-tiles-lifted,tile-roof-new-underlayment,tile-roof-new-underlayment-battens]]

## Where we work

[[cities]]

Want to know more first? Read [about CJ's Roofing](/about-us/), compare [shingle and tile roofs](/types-of-roofing/), or see the [roofing FAQ](/roofing-faq/).

[[cta]]
""")

page(path="/about-us/", label="About",
     title="About CJ's Roofing | San Ramon Roofer Since 1995",
     h1="About CJ's Roofing",
     description="CJ's Roofing has been Chris Montano's San Ramon roofing company since July 1995. "
                 "Family-owned, licensed (CSLB #709867), shingle and tile roofs plus gutters.",
     hero="tile-roof-dublin-ridge",
     lead="Chris J Montano started CJ's Roofing on July 17, 1995. It's still his company, still family-owned "
          "and operated, and still based in San Ramon.",
     body="""
## Owner-run from day one

CJ's Roofing is a small company on purpose. When you call {call}, you reach Chris, and he stays your contact from the first call until the job is done. His son works alongside him at times.

Most of Chris's work has always come from word of mouth: past customers passing his number to neighbors, friends and family. This website exists so the people those customers talk to can find him more easily.

## What we do, and what we don't

We work on asphalt shingle roofs, tile roofs and gutters. That's it. Chris doesn't install metal roofs, because metal scratches when people move around on it during the work, and he'd rather turn a job down than leave a roof marked up. We don't do siding or remodeling either.

See all [roofing and gutter services](/services/).

## Where we work

We're based in San Ramon and work throughout the Tri-Valley and the greater Bay Area, from Tracy across to South San Francisco and south toward Morgan Hill. The cities we serve most are listed on our [home page](/#areas).

## Licence

CJ's Roofing is licensed by the California Contractors State License Board: licence #709867, classification C-39 Roofing, first issued in July 1995. [Verify the licence on the CSLB website](https://www.cslb.ca.gov/709867).

[[photos:tile-roof-repair-dublin-replacement-tiles,shingle-roof-newark-ridge,concrete-tile-roof-solar-prep-1]]

[[cta]]
""")

page(path="/services/", label="Services",
     title="Roofing & Gutter Services | CJ's Roofing",
     h1="Roofing and Gutter Services",
     description="Shingle roof repair and replacement, tile roof repair and replacement, and gutter "
                 "installation and repair from CJ's Roofing, San Ramon, CA. Call (925) 205-6447.",
     lead="CJ's Roofing does three things: asphalt shingle roofs, tile roofs and gutters. Pick the one you need below, "
          "or just call Chris and describe the problem.",
     body="""
[[services]]

## Not sure which you need?

A leak doesn't always come from where the stain on the ceiling is. Water can run along the underlayment or the roof deck for several feet before it drips. Call or text {call}, send a few photos if you can, and Chris will tell you what he'd look at first.

## What we don't do

No metal roofing, no siding, no remodeling. If your project is one of those, we'd rather tell you now than waste your time.

[[cta]]
""")

page(path="/services/shingle-roofing/", label="Shingle Roofing", service="shingle",
     title="Shingle Roofing San Ramon, CA | CJ's Roofing",
     h1="Asphalt Shingle Roofing in San Ramon",
     description="Asphalt shingle roof repair and replacement in San Ramon and the Tri-Valley. "
                 "Owner-run since 1995, CSLB #709867. Call Chris at (925) 205-6447.",
     hero="shingle-roof-newark-rooftops",
     lead="Asphalt shingles are the most common roof on Bay Area homes, and they're half of what CJ's Roofing "
          "does. We repair shingle roofs and replace them.",
     body="""
## How shingle roofs wear out here

Shingle roofs in the Tri-Valley take a beating from sun more than anything else. Long, hot, dry summers slowly cook the asphalt. The granules on the surface, which protect the shingle from UV, loosen and wash into the gutters. Once enough of them are gone, shingles harden, curl at the edges and crack.

Wind is the second problem. A strong gust can lift a shingle tab and break its seal, and a lifted shingle is where the next winter storm gets in. Leaks also start around the things that pass through the roof: vent pipes, chimneys, skylights and walls, where metal flashing and rubber pipe boots do the waterproofing and eventually wear out.

## Signs it's time to call

- Shingles curling, cracking or missing
- Lots of granules in the gutters or at the bottom of downspouts
- Bare or dark patches where granules are gone
- A water stain on a ceiling or in the attic
- Daylight or damp wood in the attic
- Shingles lifted or creased after a windy storm

## Repair or replace?

A roof with a few problems in an otherwise sound field of shingles is a repair. A roof that is worn out everywhere is a replacement, and patching it just moves the leak. Chris will look at the whole roof, not only the spot you called about, and tell you which one you're dealing with.

- [Shingle roof replacement](/services/shingle-roofing/shingle-roof-replacement/)
- [Shingle roof repair](/services/shingle-roofing/shingle-roof-repair/)

Weighing up shingle against tile? See [shingle vs tile](/types-of-roofing/).

[[photos:shingle-roof-newark-vents,shingle-roof-newark-ridge,shingle-roof-newark-street]]

[[cta]]
""")

page(path="/services/shingle-roofing/shingle-roof-replacement/", label="Shingle Roof Replacement", service="shingle",
     title="Shingle Roof Replacement San Ramon | CJ's Roofing",
     h1="Shingle Roof Replacement",
     description="Full asphalt shingle roof replacement in San Ramon, Danville, Dublin and Pleasanton from "
                 "CJ's Roofing, licensed since 1995 (CSLB #709867). Call (925) 205-6447.",
     hero="shingle-roof-newark-ridge",
     lead="When a shingle roof is worn out across the board, repairs stop working. A replacement takes the roof "
          "back to the deck and starts again.",
     body="""
## When replacement makes sense

- Shingles are curling, cracking or bare of granules across most of the roof, not just one area
- Leaks keep coming back in different places
- There are already two layers of shingles and the roof needs work again
- The roof deck underneath feels soft or spongy when walked on
- You're planning solar and the roof won't outlast the panels

If only one section is damaged, a [shingle roof repair](/services/shingle-roofing/shingle-roof-repair/) may be all you need. Chris will tell you straight which one it is.

## What a shingle replacement involves

A proper replacement is more than new shingles on top:

- **Tear-off.** The old shingles and underlayment come off so the deck can be seen.
- **Deck check.** Any rotten or damaged sheathing gets replaced before anything goes over it.
- **Underlayment.** New underlayment goes down over the whole deck. This is the layer that stops water that gets past the shingles.
- **Flashing and edges.** Metal at walls, chimneys, valleys and roof edges, and the boots around vent pipes, are where most leaks start, so they are dealt with as part of the job.
- **Shingles, ridge and vents.** The new shingles go on, followed by the ridge cap and roof vents.
- **Clean-up.** Old material is hauled away and the site is cleaned before we leave.

## Permits and HOAs

A full re-roof in California needs a building permit, and the city or county inspects the work. If your neighborhood has an HOA, it will usually want to approve the shingle style and color before work starts, so it's worth getting that request in early.

## Choosing a shingle

Shingles come in a wide range of colors and profiles. Pick something that suits the house and, where there is one, meets your HOA's rules. Chris can talk you through the options for your home when he comes out.

[[photos:shingle-roof-newark-rooftops,shingle-roof-newark-vents,shingle-roof-newark-ridge-2]]

[[cta]]
""")

page(path="/services/shingle-roofing/shingle-roof-repair/", label="Shingle Roof Repair", service="shingle",
     title="Shingle Roof Repair San Ramon | CJ's Roofing",
     h1="Shingle Roof Repair",
     description="Shingle roof leak and repair work in San Ramon and the Tri-Valley: missing shingles, "
                 "flashing, vent pipe boots. Owner-run since 1995. Call (925) 205-6447.",
     hero="shingle-roof-newark-vents",
     lead="Most shingle roof leaks start small: one lifted shingle, one cracked pipe boot, one gap in the flashing. "
          "Caught early, they're repairs, not new roofs.",
     body="""
## Common shingle roof repairs

- **Missing or wind-lifted shingles.** Replaced and sealed down so the next storm can't get under them.
- **Vent pipe boots.** The rubber collars around plumbing vents dry out and crack in the sun. They're one of the most common sources of shingle roof leaks.
- **Flashing.** The metal where the roof meets a wall, chimney or skylight, and in valleys, can lift, rust or lose its seal.
- **Cracked or damaged shingles.** From age, a falling branch, or foot traffic from other trades.
- **Leak tracing.** Finding where water is really getting in, which is often not directly above the stain.

## Finding the leak

Water rarely drips straight down. It gets under a shingle, runs along the underlayment or a rafter, and shows up on the ceiling somewhere else. Chris looks at the roof and, where he can, the attic, to find the entry point rather than patching the spot above the stain and hoping.

## When a repair isn't the answer

If the shingles are worn out across the whole roof, a repair only buys a little time before the next leak. In that case Chris will tell you, explain why, and let you decide. See [shingle roof replacement](/services/shingle-roofing/shingle-roof-replacement/).

## Send photos first

If it's safe to do so from the ground or a window, snap a few photos of the problem area and the ceiling stain and text them to {text}. It helps Chris know what he's walking into.

[[photos:shingle-roof-newark-ridge,shingle-roof-newark-street]]

[[cta]]
""")

page(path="/services/tile-roofing/", label="Tile Roofing", service="tile",
     title="Tile Roofing San Ramon, CA | Concrete & Clay | CJ's Roofing",
     h1="Tile Roofing in San Ramon — Concrete and Clay",
     description="Tile roof repair and replacement in San Ramon, Dublin, Danville and the Tri-Valley. "
                 "Broken and slipped tiles, leaks, re-roofs. Since 1995. Call (925) 205-6447.",
     hero="tile-roof-dublin-closeup",
     lead="Tile is the other half of CJ's Roofing's work. Much of the housing built in San Ramon, Dublin and "
          "Danville from the late 1980s on has concrete tile roofs, and they need a roofer who knows how to "
          "work on them without breaking more than he fixes.",
     body="""
## Concrete and clay tile

Most tile roofs in the Tri-Valley are **concrete tile**, in either a curved S shape or a flatter profile. **Clay tile** is the traditional material and shows up on Spanish and Mediterranean-style homes. Both are heavy, both hold up well to sun, and both are fire-resistant.

## The part of a tile roof you don't see

Tile sheds most of the water, but it isn't what makes the roof waterproof. Underneath the tiles is a layer of underlayment, and that's the real barrier. Tiles can look fine from the street for decades while the underlayment below them dries out, cracks and starts letting water through. That's why an older tile roof can leak even when nothing looks broken.

## Common tile roof problems

- **Cracked and broken tiles**, very often from people walking on the roof: solar installers, satellite and cable techs, painters
- **Slipped tiles** that have slid out of line and left a gap
- **Ridge and hip tiles** that have come loose
- **Debris in valleys** that dams water and pushes it sideways
- **Worn underlayment** on older roofs

## Walking on tile

Tile breaks if you step in the wrong place. Knowing where to put your feet is a big part of tile work, and it's why a tile roof shouldn't be anyone's first roof.

## Tile services

- [Tile roof repair](/services/tile-roofing/tile-roof-repair/)
- [Tile roof replacement](/services/tile-roofing/tile-roof-replacement/)

Trying to decide between tile and shingle? See [shingle vs tile](/types-of-roofing/).

[[photos:tile-roof-repair-dublin-replacement-tiles,tile-roof-san-ramon-tiles-lifted,concrete-tile-roof-solar-prep-2]]

[[cta]]
""")

page(path="/services/tile-roofing/tile-roof-replacement/", label="Tile Roof Replacement", service="tile",
     title="Tile Roof Replacement San Ramon | CJ's Roofing",
     h1="Tile Roof Replacement",
     description="Tile roof replacement in San Ramon, Dublin, Danville and Pleasanton by CJ's Roofing, "
                 "licensed since 1995 (CSLB #709867). Call Chris at (925) 205-6447.",
     hero="tile-roof-san-ramon-tiles-lifted",
     lead="A tile roof can last a long time, but not forever. When leaks keep coming back or the layer under the "
          "tiles has given out, it's time to deal with the whole roof.",
     body="""
## When a tile roof needs more than repairs

- Leaks in more than one place, or leaks that come back after repair
- Underlayment that is brittle, torn or crumbling where tiles have been lifted
- Lots of cracked tiles across the roof
- Rotten roof deck or battens found during a repair
- Planning solar on an older tile roof: it's easier to sort the roof out before panels go on it

## It's usually the underlayment

On most older tile roofs, the tiles themselves are still in decent shape. What has failed is the underlayment underneath. The photos on this page are from a tile roof in San Ramon: the tiles have been lifted and stacked, the old underlayment is exposed, and new underlayment and battens are going down.

Every roof is different. Whether your tiles can be reused, need to be partly replaced, or the roof needs new tile throughout depends on the condition and the tile profile. Chris will look at it and tell you what makes sense.

## What the job involves

- Removing tiles carefully and stacking them on the roof or on the ground
- Removing the old underlayment and checking the deck, replacing damaged sheathing
- New underlayment, battens and flashings at valleys, walls and roof penetrations
- Setting the tile, then the hip and ridge tiles
- Clean-up and hauling away old material

## Permits, HOAs and weight

A tile re-roof needs a building permit. HOAs in tile neighborhoods usually control tile color and profile. And if you are thinking of switching from tile to something else, or from shingle to tile, weight matters: tile is much heavier than shingle, and a house framed for one isn't automatically right for the other. See [shingle vs tile](/types-of-roofing/).

[[photos:tile-roof-san-ramon-tiles-lifted,tile-roof-new-underlayment,tile-roof-new-underlayment-battens]]

[[cta]]
""")

page(path="/services/tile-roofing/tile-roof-repair/", label="Tile Roof Repair", service="tile",
     title="Tile Roof Repair San Ramon | CJ's Roofing",
     h1="Tile Roof Repair",
     description="Tile roof repair in San Ramon, Dublin and the Tri-Valley: cracked and slipped tiles, "
                 "ridge tiles, valley and flashing leaks. Since 1995. Call (925) 205-6447.",
     hero="tile-roof-repair-dublin-replacement-tiles",
     lead="Most tile roof problems are repairs: a few broken tiles, a slipped row, a loose ridge, a leaking valley. "
          "Fixed early, they stay small.",
     body="""
## Tile repairs we do

- **Cracked and broken tiles** replaced one by one
- **Slipped tiles** reset and secured
- **Ridge and hip tiles** re-set where they have loosened
- **Valleys** cleared of debris, with the flashing checked
- **Leaks around vents, skylights and walls** where the flashing has failed
- **Damage from other trades**, especially after solar, satellite or painting work

## Matching tiles

Replacement tiles need to match the profile of the roof so they lock in with the tiles around them. Color is harder: a brand-new tile is often brighter than tiles that have weathered for years, and older colors and profiles are sometimes discontinued. The photos on this page, from a tile repair in Dublin, show new replacement tiles staged on the roof next to the originals.

## Why tile repair takes care

Every step on a tile roof has to land in the right place or another tile cracks. Chris has been working on tile roofs since 1995; he knows where to walk and how to lift tiles without breaking their neighbors.

## When it's more than a repair

If the underlayment beneath the tiles is worn out across the roof, replacing broken tiles won't stop the leaks. In that case see [tile roof replacement](/services/tile-roofing/tile-roof-replacement/), and Chris will explain what he found.

## Send photos

Text a few photos of the problem area and any ceiling stain to {text}. Please don't climb onto a tile roof to take them.

[[photos:tile-roof-repair-dublin-replacement-tiles,tile-roof-repair-dublin-staged-tiles,tile-roof-repair-dublin-vents]]

[[cta]]
""")

page(path="/services/gutters/", label="Gutters", service="gutters",
     title="Gutter Installation San Ramon, CA | CJ's Roofing",
     h1="Seamless Gutters and Gutter Repair in San Ramon",
     description="Gutter installation and gutter repair in San Ramon and the Tri-Valley from CJ's Roofing. "
                 "Owner-run roofing company since 1995. Call (925) 205-6447.",
     lead="Gutters are the only work CJ's Roofing does besides roofs, and they belong together: a roof sheds the "
          "water, and gutters carry it away from the house.",
     body="""
## Why gutters matter here

Bay Area rain mostly comes in a few months, often in heavy bursts. When that water can't get off the roof edge and away from the house, it overflows onto walkways, soaks the soil next to the foundation, splashes up onto siding and stucco, and rots the fascia board behind the gutter.

In the Tri-Valley, the trees are a big part of the problem. Oaks and other mature trees drop leaves and debris into gutters all year, and a clogged gutter overflows no matter how well it's installed.

## Gutter services

- [Seamless gutter installation](/services/gutters/seamless-gutter-installation/): new gutters and downspouts
- [Gutter repair and replacement](/services/gutters/gutter-repair/): leaks, sagging, pulled-away sections, downspouts

## Gutters and a new roof

If you're replacing your roof, it's a good time to look at the gutters too. The roof edge metal and the gutters work together, and it's simpler to deal with both while the roof edge is open.

[[cta]]
""")

page(path="/services/gutters/seamless-gutter-installation/", label="Seamless Gutter Installation", service="gutters",
     title="Seamless Gutter Installation | CJ's Roofing",
     h1="Seamless Gutter Installation",
     description="New seamless gutters and downspouts for homes in San Ramon, Danville, Dublin and "
                 "Pleasanton from CJ's Roofing, since 1995. Call Chris at (925) 205-6447.",
     lead="New gutters done properly: sized for the roof, pitched to drain, and fastened so they stay put.",
     body="""
## What “seamless” means

Seamless gutters are formed in long, continuous runs to fit each side of the house, instead of being pieced together from short sections. The only joints are at the corners and the end caps. Fewer joints means fewer places for gutters to drip and leak over time.

## What makes a gutter install work

- **Pitch.** Gutters need a slight, even fall toward the downspouts. Too flat and water sits; wrong way and it overflows at the end.
- **Downspouts.** Enough of them, in the right places, sized to handle a heavy storm off the roof area they serve.
- **Where the water goes.** Downspouts should discharge away from the foundation, not onto it.
- **Fastening.** Hangers spaced so the gutter doesn't sag when it's full of water and debris.
- **Fascia.** The board behind the gutter needs to be sound. Rotten fascia should be dealt with before new gutters go on it.

## When to replace gutters

- Gutters that leak at many seams or corners
- Sections sagging or pulling away from the house
- Rust or holes
- Water overflowing even when the gutters are clean
- A new roof going on, making it the right moment

Ask Chris about material and color options for your home when he comes out.

If your gutters only need fixing, see [gutter repair](/services/gutters/gutter-repair/).

[[cta]]
""")

page(path="/services/gutters/gutter-repair/", label="Gutter Repair", service="gutters",
     title="Gutter Repair & Replacement | CJ's Roofing",
     h1="Gutter Repair and Replacement",
     description="Gutter repair in San Ramon and the Tri-Valley: leaking seams, sagging and loose gutters, "
                 "downspouts. CJ's Roofing, since 1995. Call (925) 205-6447.",
     lead="Not every gutter problem needs new gutters. Many are a loose hanger, a failed seam or a disconnected "
          "downspout.",
     body="""
## Common gutter repairs

- **Leaking seams and corners**, resealed or the section replaced
- **Sagging gutters**, re-hung and re-fastened
- **Gutters pulling away** from the fascia
- **Wrong pitch**, so water sits or runs the wrong way
- **Downspouts** that are loose, crushed or disconnected, or that dump water against the foundation
- **Damaged sections**, from a ladder, a falling branch or age, replaced

## Look behind the gutter

When a gutter has been overflowing or leaking for a while, the fascia board behind it often rots. Re-hanging a gutter on rotten wood doesn't last. Chris checks what the gutter is fastened to, not just the gutter.

## Repair or replace?

If the gutters are sound apart from a problem or two, repair them. If they are leaking and sagging everywhere, rusted through, or undersized for the roof, new [seamless gutters](/services/gutters/seamless-gutter-installation/) are the better spend. Chris will tell you which.

## Gutters and roof leaks

Sometimes what looks like a roof leak is a gutter problem: water backing up over the edge and running behind the fascia into the wall or eaves. Chris looks at both, since he works on both.

[[cta]]
""")

# ---- City pages (San Ramon is the home page) ---------------------------------

page(path="/fremont/", label="Fremont", city="Fremont",
     title="Roofing Fremont, CA | Shingle & Tile Roofer | CJ's Roofing",
     h1="Fremont Roofing Contractor",
     description="Shingle and tile roof repair and replacement, plus gutters, for Fremont homes in Niles, "
                 "Centerville, Irvington, Mission San Jose and Warm Springs. Call (925) 205-6447.",
     hero="shingle-roof-newark-rooftops",
     lead="CJ's Roofing works in Fremont on asphalt shingle roofs, tile roofs and gutters. We're based in San Ramon, "
          "straight down I-680 over the Sunol Grade.",
     body="""
## Fremont's roofs

Fremont grew fast after the five towns of Centerville, Irvington, Mission San Jose, Niles and Warm Springs incorporated as one city in 1956, and a large share of its homes are single-story and two-story houses from the 1950s through the 1970s. Most of those have asphalt shingle roofs, and many are now on their second or third roof.

Newer neighborhoods, like Ardenwood on the northwest side and the newer parts of Warm Springs, add more recent construction. Up in the hills around Mission San Jose, larger homes and Mission-style houses are more likely to have tile. Niles has some of the city's oldest houses, where roof work often turns up older roof decks that need attention.

## Fremont weather and your roof

West Fremont sits near the bay and gets steady afternoon wind, which lifts shingle tabs and breaks their seals. Homes against the hills to the east get more heat and more debris from trees. Winter storms then find whatever the wind and sun have loosened.

## Permits in Fremont

A re-roof in Fremont needs a permit from the City of Fremont's building division, with an inspection when the work is done. If you're in an HOA neighborhood, get roof material and color approved before work is scheduled.

## What we do in Fremont

- [Shingle roof replacement](/services/shingle-roofing/shingle-roof-replacement/) and [shingle roof repair](/services/shingle-roofing/shingle-roof-repair/)
- [Tile roof repair](/services/tile-roofing/tile-roof-repair/) and [tile roof replacement](/services/tile-roofing/tile-roof-replacement/)
- [Gutter installation](/services/gutters/seamless-gutter-installation/) and [gutter repair](/services/gutters/gutter-repair/)

## Photos from next door

The shingle roof photos below were taken in Newark, which borders Fremont on the west, in April 2024. More in the [gallery](/gallery/).

[[photos:shingle-roof-newark-rooftops,shingle-roof-newark-vents,shingle-roof-newark-street]]

[[cta]]
""")

page(path="/pleasanton/", label="Pleasanton", city="Pleasanton",
     title="Roofing Pleasanton, CA | Shingle & Tile Roofer | CJ's Roofing",
     h1="Pleasanton Roofing Contractor",
     description="Shingle and tile roof repair and replacement, plus gutters, for Pleasanton homes. "
                 "San Ramon-based, owner-run since 1995. Call Chris at (925) 205-6447.",
     hero="tile-roof-dublin-hills",
     lead="CJ's Roofing repairs and replaces shingle and tile roofs and installs gutters in Pleasanton, just down "
          "I-680 from our base in San Ramon.",
     body="""
## Pleasanton's roofs

Pleasanton's housing covers several eras. Around downtown and Main Street there are older homes, some going back to the early 1900s. The big neighborhoods of the 1960s and 1970s, such as Pleasanton Valley, Val Vista and Birdland, are mostly single-family tract homes, and many carry asphalt shingle roofs.

From the 1980s onward, neighborhoods in the southern hills and along the edges of town, such as Vintage Hills, Kottinger Ranch, Laguna Oaks and Ruby Hill, brought larger homes, and with them far more concrete and clay tile. Many of those tile roofs are now old enough that the underlayment beneath the tile deserves a look.

## Pleasanton weather and your roof

The Amador Valley gets hot, dry summers, hotter than the bay side of the hills. That heat and sun are the main thing aging shingle roofs here. Tile handles the sun well, but broken tiles and worn underlayment still let winter storms in. Homes near Pleasanton Ridge and the oak-covered hills also deal with leaves in valleys and gutters.

## HOAs and permits

A lot of Pleasanton neighborhoods have HOAs with architectural review, and they often specify roof material, tile profile or color. Get that approval before booking work. A full re-roof needs a building permit from the City of Pleasanton.

## What we do in Pleasanton

- [Tile roof repair](/services/tile-roofing/tile-roof-repair/) and [tile roof replacement](/services/tile-roofing/tile-roof-replacement/)
- [Shingle roof replacement](/services/shingle-roofing/shingle-roof-replacement/) and [shingle roof repair](/services/shingle-roofing/shingle-roof-repair/)
- [Gutter installation](/services/gutters/seamless-gutter-installation/) and [gutter repair](/services/gutters/gutter-repair/)

[[photos:tile-roof-repair-dublin-replacement-tiles,tile-roof-new-underlayment,concrete-tile-roof-solar-prep-2]]

[[cta]]
""")

page(path="/castro-valley/", label="Castro Valley", city="Castro Valley",
     title="Roofing Castro Valley, CA | CJ's Roofing",
     h1="Castro Valley Roofing Contractor",
     description="Shingle and tile roof repair and replacement, plus gutters, for Castro Valley homes. "
                 "CJ's Roofing, San Ramon, since 1995. Call (925) 205-6447.",
     hero="shingle-roof-newark-ridge",
     lead="CJ's Roofing works on shingle roofs, tile roofs and gutters in Castro Valley. From San Ramon it's a "
          "drive over Crow Canyon Road.",
     body="""
## Castro Valley's roofs

Castro Valley is a mix. The flatter central area around Castro Valley Boulevard has many homes built in the years after World War II through the 1960s, most with asphalt shingle roofs that have been replaced more than once. Hillside areas and newer developments such as Palomares Hills and Five Canyons add larger homes on slopes, with a mix of shingle and tile.

Hillside houses often have more complicated rooflines, with more valleys, hips and walls, and those joints are where leaks start.

## Castro Valley weather and your roof

Castro Valley sits in the hills just east of the bay, and it catches more marine air and fog than the Tri-Valley towns over the ridge. North-facing roof slopes and roofs under trees stay damp longer, which encourages moss and algae on shingles and tile. The canyons are full of oaks and other trees that drop leaves and twigs into valleys and gutters, and a blocked valley pushes water sideways under roofing.

## Permits in Castro Valley

Castro Valley is unincorporated, so it has no city hall of its own. Re-roof permits go through Alameda County's building inspection department rather than a city.

## What we do in Castro Valley

- [Shingle roof repair](/services/shingle-roofing/shingle-roof-repair/) and [shingle roof replacement](/services/shingle-roofing/shingle-roof-replacement/)
- [Tile roof repair](/services/tile-roofing/tile-roof-repair/) and [tile roof replacement](/services/tile-roofing/tile-roof-replacement/)
- [Gutter repair](/services/gutters/gutter-repair/) and [gutter installation](/services/gutters/seamless-gutter-installation/), a big deal under Castro Valley's trees

[[photos:shingle-roof-newark-ridge,tile-roof-repair-dublin-staged-tiles]]

[[cta]]
""")

page(path="/dublin/", label="Dublin", city="Dublin",
     title="Roofing Dublin, CA | Shingle & Tile Roofer | CJ's Roofing",
     h1="Dublin Roofing Contractor",
     description="Tile and shingle roof repair and replacement, plus gutters, for Dublin homes from West "
                 "Dublin to Dublin Ranch. Next door in San Ramon. Call (925) 205-6447.",
     hero="tile-roof-dublin-hills",
     lead="Dublin is right next door to San Ramon, and it's where many of the tile roof photos on this site were "
          "taken. CJ's Roofing works on Dublin's shingle roofs, tile roofs and gutters.",
     body="""
## Dublin's roofs

Dublin has two very different housing stocks. West and central Dublin, including the hillside streets of West Dublin, are mostly homes from the 1960s and 1970s. Many of them have asphalt shingle roofs.

East Dublin is newer. Dublin Ranch, Positano, Wallis Ranch, Jordan Ranch and the neighborhoods around them were built from around 2000 onward, and concrete tile is the norm there. Out in the western hills, Schaefer Ranch is newer construction too. The first East Dublin tile roofs are now more than twenty years old, which is the age when broken tiles and worn underlayment begin to show up.

## Dublin weather and your roof

Dublin sits where the I-580 and I-680 corridors meet, and wind funnels through the valley and Dublin Canyon. Wind lifts shingle tabs and can dislodge ridge and edge tiles. Summers are hot and dry, and winter storms follow.

## HOAs and permits

Most of East Dublin is HOA territory, and associations there usually control tile profile and color, so any replacement tiles need to match. A re-roof needs a permit from the City of Dublin.

## Tile roof photos from Dublin

The photos below are from a tile roof in Dublin in April 2024: the roof, and replacement tiles staged ready to go in. See more in the [gallery](/gallery/).

[[photos:tile-roof-dublin-ridge,tile-roof-repair-dublin-replacement-tiles,tile-roof-dublin-closeup]]

## What we do in Dublin

- [Tile roof repair](/services/tile-roofing/tile-roof-repair/) and [tile roof replacement](/services/tile-roofing/tile-roof-replacement/)
- [Shingle roof repair](/services/shingle-roofing/shingle-roof-repair/) and [shingle roof replacement](/services/shingle-roofing/shingle-roof-replacement/)
- [Gutter installation](/services/gutters/seamless-gutter-installation/) and [gutter repair](/services/gutters/gutter-repair/)

[[cta]]
""")

page(path="/danville/", label="Danville", city="Danville",
     title="Roofing Danville, CA | Shingle & Tile Roofer | CJ's Roofing",
     h1="Danville Roofing Contractor",
     description="Shingle and tile roof repair and replacement, plus gutters, in Danville, Blackhawk and "
                 "Diablo. San Ramon-based since 1995. Call Chris at (925) 205-6447.",
     hero="tile-roof-dublin-ridge-2",
     lead="Danville is San Ramon's neighbor to the north, a few minutes up I-680. CJ's Roofing repairs and replaces "
          "shingle and tile roofs and installs gutters there.",
     body="""
## Danville's roofs

On the valley floor, around downtown and neighborhoods like Greenbrook and Sycamore Valley, many homes date from the 1960s through the 1980s, often single-story ranch homes with long, simple rooflines and asphalt shingle roofs. Toward the east, Blackhawk and the Tassajara area were built later and have many large homes with concrete or clay tile. Diablo, below Mount Diablo, has older estate homes with more varied roofs.

## Trees, heat and fire

Danville's mature oaks are a big part of its character, and a big part of its roof problems: leaves fill valleys and gutters, branches scrape and break shingles and tiles, and shaded slopes grow moss. Summers are hot and dry.

Parts of Danville and the surrounding hills are in state-mapped fire hazard severity zones, where California's building code sets fire-rating rules for roofing. Most asphalt shingles and concrete and clay tiles sold today carry a Class A fire rating, the highest. The building department can confirm what applies to your address.

## Permits: Town or County

Homes inside the Town of Danville get re-roof permits from the Town. Blackhawk and Diablo are unincorporated, so permits there go through Contra Costa County. Many Danville and Blackhawk neighborhoods also have HOAs that approve roof material and color.

## What we do in Danville

- [Shingle roof replacement](/services/shingle-roofing/shingle-roof-replacement/) and [shingle roof repair](/services/shingle-roofing/shingle-roof-repair/)
- [Tile roof repair](/services/tile-roofing/tile-roof-repair/) and [tile roof replacement](/services/tile-roofing/tile-roof-replacement/)
- [Gutter installation](/services/gutters/seamless-gutter-installation/) and [gutter repair](/services/gutters/gutter-repair/)

[[photos:tile-roof-dublin-ridge-2,shingle-roof-newark-ridge-2,tile-roof-repair-dublin-staged-tiles]]

[[cta]]
""")

page(path="/alamo/", label="Alamo", city="Alamo",
     title="Roofing Alamo, CA | Shingle & Tile Roofer | CJ's Roofing",
     h1="Alamo Roofing Contractor",
     description="Shingle and tile roof repair and replacement, plus gutters, for Alamo homes. "
                 "CJ's Roofing, San Ramon, licensed since 1995. Call (925) 205-6447.",
     hero="tile-roof-dublin-closeup",
     lead="CJ's Roofing works on shingle roofs, tile roofs and gutters in Alamo, up I-680 past Danville from our base "
          "in San Ramon.",
     body="""
## Alamo's roofs

Alamo is mostly single-family homes on large lots, from 1950s and 1960s ranch houses to big custom homes, many of them remodeled and added onto over the years. Additions mean more complicated roofs: more valleys, more walls meeting roofs, more flashing, and more places for water to get in. Neighborhoods like Round Hill, Stone Valley and the areas off Livorna Road run the full range of shingle and tile.

## Trees and weather

Alamo has a lot of tall, mature trees. That shade keeps homes cool, but it also means leaves and needles in valleys and gutters, moss on shaded slopes, and branches that can damage shingles and crack tiles in a winter storm. Summers are hot and dry, and the sun still ages the exposed slopes.

Parts of Alamo, especially toward the Las Trampas hills and Mount Diablo side, are in state-mapped fire hazard severity zones, where California's building code sets fire-rating rules for roofing. Most asphalt shingles and concrete and clay tiles sold today carry a Class A fire rating.

## Permits in Alamo

Alamo is unincorporated. Re-roof permits come from Contra Costa County's Department of Conservation and Development rather than a city.

## What we do in Alamo

- [Shingle roof repair](/services/shingle-roofing/shingle-roof-repair/) and [shingle roof replacement](/services/shingle-roofing/shingle-roof-replacement/)
- [Tile roof repair](/services/tile-roofing/tile-roof-repair/) and [tile roof replacement](/services/tile-roofing/tile-roof-replacement/)
- [Gutter repair](/services/gutters/gutter-repair/) and [gutter installation](/services/gutters/seamless-gutter-installation/)

[[photos:tile-roof-dublin-closeup,shingle-roof-newark-rooftops]]

[[cta]]
""")

page(path="/gallery/", label="Gallery",
     title="Roofing Project Photos | CJ's Roofing",
     h1="Recent Roofing Projects",
     description="Photos of CJ's Roofing tile and shingle roof work in San Ramon, Dublin and the Bay Area, "
                 "taken on the job by Chris Montano.",
     lead="These are CJ's Roofing's own job photos, taken on the roof by Chris. No stock photos. "
          "New jobs are added as they're finished.",
     body="""
[[gallery]]

[[cta]]
""")

page(path="/reviews/", label="Reviews",
     title="CJ's Roofing Reviews | San Ramon Roofer",
     h1="What Our Customers Say",
     description="Read CJ's Roofing reviews on Google and Yelp, or leave one. San Ramon roofing contractor "
                 "since 1995. Call (925) 205-6447.",
     lead="Most of CJ's Roofing's work comes from people recommended by past customers. You can read what customers "
          "have written on Google and Yelp.",
     body="""
## Read reviews

[[reviewlinks]]

We don't copy reviews onto this page. Read them where they were written, with the reviewer's name and date attached.

## Had work done by CJ's Roofing?

A short review helps your neighbors find a roofer they can trust, and it helps Chris more than you'd think. Say what was done, where, and how it went.

[[reviewcta]]

[[cta]]
""")

page(path="/types-of-roofing/", label="Types of Roofing",
     title="Types of Roofing: Shingle vs Tile | CJ's Roofing",
     h1="Shingle vs Tile: Which Roof Is Right for You",
     description="Asphalt shingle vs concrete and clay tile roofs for Bay Area homes: look, weight, cost, "
                 "repairs, solar and fire rating. From CJ's Roofing, San Ramon.",
     hero="tile-roof-dublin-closeup",
     lead="CJ's Roofing works on two kinds of roof: asphalt shingle and tile. Here's how they compare, in plain terms.",
     body="""
## Asphalt shingle

Asphalt shingles are the most common roof on Bay Area homes. They're light, go on relatively quickly, and generally cost less to install than tile. They come in a wide range of colors and profiles, from flat three-tab shingles to thicker architectural shingles with more texture.

Their main enemy in the Tri-Valley is sun and heat, which slowly break down the asphalt and loosen the protective granules. When they wear out, they're replaced as a whole roof.

## Concrete and clay tile

Tile is common on homes built in the Tri-Valley from the late 1980s onward and on Spanish and Mediterranean-style houses. Concrete tile is the more common of the two; clay is the traditional material. Tile handles sun and heat very well and doesn't burn.

The tile, though, isn't the waterproof layer. The underlayment beneath it is, and that ages. Tile is also brittle underfoot: it cracks when stepped on in the wrong place, so any work on a tile roof, including other trades like solar or satellite installers, needs care.

## Side by side

- **Look:** shingle is flatter and simpler; tile has depth and shadow lines and suits Mediterranean and Spanish styles.
- **Weight:** tile is several times heavier than shingle. A house framed for shingle may need an engineer's check before switching to tile.
- **Up-front cost:** shingle generally costs less to install.
- **How it wears:** shingles wear out across the whole surface; on tile, the tiles often outlast the underlayment beneath them.
- **Repairs:** shingle repairs are straightforward; tile repairs need matching tiles and careful footwork.
- **Fire:** most asphalt shingles and concrete and clay tiles sold today are Class A fire-rated.
- **HOAs:** in many Tri-Valley neighborhoods, the HOA decides which you can use.

## What about metal?

CJ's Roofing doesn't install metal roofs. Metal panels scratch when people move around on them during work, and Chris would rather not hand over a roof that's marked on day one.

## Still deciding?

Call Chris at {call}. He'll tell you what makes sense for your house, including when the right answer is to keep what you have.

- [Shingle roofing](/services/shingle-roofing/)
- [Tile roofing](/services/tile-roofing/)

[[cta]]
""")

page(path="/roofing-faq/", label="Roofing FAQ",
     title="Roofing FAQ | CJ's Roofing",
     h1="Roofing Questions, Answered",
     description="Answers about CJ's Roofing: licence, services, areas, repairs vs replacement, solar prep and "
                 "how to get an estimate. San Ramon, CA. Call (925) 205-6447.",
     lead="Short answers to the questions people ask Chris most. Anything not here, call or text {call}.",
     body="""
[[faq]]

[[cta]]
""")

page(path="/contact-us/", layout="contact", label="Contact",
     title="Contact CJ's Roofing | San Ramon | 925-205-6447",
     h1="Contact CJ's Roofing",
     description="Call or text Chris at CJ's Roofing on (925) 205-6447, or email customerservice@cjs-roofing.com. "
                 "9672 Camassia Way, San Ramon, CA 94582.",
     lead="The fastest way to reach CJ's Roofing is to call or text Chris directly.",
     body="""
[[contactcards]]

## Texting photos helps

If you're texting about a leak or damage, include your address and a few photos of the problem area and any ceiling stain. Please don't climb onto the roof to take them.

## Where we work

San Ramon and the greater Bay Area, including [Dublin](/dublin/), [Pleasanton](/pleasanton/), [Danville](/danville/), [Alamo](/alamo/), [Castro Valley](/castro-valley/) and [Fremont](/fremont/).
""")

page(path="/privacy-policy/", label="Privacy Policy",
     title="Privacy Policy | CJ's Roofing",
     h1="Privacy Policy",
     description="How CJ's Roofing handles the information you share when you contact us through roofingsanramonca.com.",
     body="""
This policy explains what information CJ's Roofing ("we", "us") collects through roofingsanramonca.com and what we do with it.

## What we collect

This website has no contact form, no user accounts and no advertising or analytics tracking. Calls to the phone number on this site go through a call-tracking service and may be recorded for quality purposes; callers hear a short notice first. We collect information only when you choose to contact us by phone, text message or email. That may include your name, phone number, email address, property address, photos of your roof, and whatever details you choose to send.

Like most websites, our hosting provider may automatically record standard technical information such as IP address, browser type and the pages requested, for security and to keep the site running.

## How we use it

We use the information you send us only to respond to you, to quote and carry out the work you ask for, and to keep records of that work. We don't sell or rent your personal information, and we don't share it except with people who help us do the work you requested, or where the law requires it.

## Your choices

You can ask us what information we hold about you, or ask us to correct or delete it, by contacting us at {email} or {call}.

## Links to other sites

Our pages link to other websites, such as Google, Yelp and the Contractors State License Board. Their privacy practices are their own.

## Children

This website is not directed at children under 13, and we don't knowingly collect their information.

## Changes

If this policy changes, the updated version will be posted on this page.

## Contact

CJ's Roofing, 9672 Camassia Way, San Ramon, CA 94582 · {call} · {email}
""")

page(path="/thank-you/", label="Thank You", noindex=True, in_sitemap=False,
     title="Thank You | CJ's Roofing",
     h1="Thanks — We'll Call You Back",
     description="Thanks for contacting CJ's Roofing.",
     lead="Your message has been sent to CJ's Roofing. Chris will get back to you as soon as he can.",
     body="""
If it's urgent, call or text Chris now at {call}.

[Back to the home page](/)
""")
