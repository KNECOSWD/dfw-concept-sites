# Forum Terrace Church of Christ — Design Brief

**Live:** http://forumterrace.org/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/forum-terrace-church/  
**Shots:** `live-home.png`, `live-hero.png`, `rebuild-home.png`, `rebuild-hero.png`  
**Constraint:** Match live vibe — polish only, no new brand. Keep existing logo.

## Vibe score: **5 / 10**

Rebuild polish (cards, service panel, skip link) is solid, but **tone drifted**: live is a **dark, atmospheric cloud-photo** site with white sans type, blue FIND US, and a dense right rail (service times + monthly events + schematic map). Rebuild is warm cream + serif display + burnt-orange CTAs — reads “generic traditional church brochure,” not Forum Terrace’s modern dark welcome page.

## Live color tokens (sampled)

| Token | Hex | Use |
|---|---|---|
| `--hero-sky` | `#2F4259` | Cloud photo midtones |
| `--hero-deep` | `#12233E` | Header / dark chrome |
| `--surface-dark` | `#1A2433` | Lower dark bands |
| `--ink-on-dark` | `#FFFFFF` | Headings + body on hero |
| `--brand` | `#1C587B` | Logo blue / map strokes |
| `--cta` | `#293547` → prefer `#1C587B` | FIND US button (live is muted blue) |
| `--accent-cross` | `#EF8224` | Map location cross |
| `--map-fill` | `#DADBDC` / white | Schematic map |
| `--nav` | `#FFFFFF` | Caps nav on dark |

Warm cream `#F6EFE6` / brown `#8B5A2B` in current `theme.css` are **rebuild inventions** — OK for light content bands only if hero stays dark-photo; don’t let them own the brand.

## Layout intent (live)

1. **Dark sticky header** — FTCC mark left; uppercase white nav right (Location, Bulletins, Contact, Tracts, Workbooks, Sermons, Members).
2. **Full-bleed cloud hero** — two columns: **left** welcome H1 + short mission + blue FIND US; **right** Service Times, Scheduled Events list, schematic area map with orange cross.
3. **Continued dark / photo-bleed content** — Who We Are + events echo below; resource hubs link out.
4. Priority above the fold: *who / when / where* — map is part of the brand, not optional decoration.

## Concrete Eng CSS / HTML change list

1. **`theme.css`** — Set `--brand: #1C587B`, `--accent: #EF8224` (map/cross + sparingly), `--hero-ink: #F8F8F8`, `--bg` for below-fold can stay soft warm `#F5EEE5` **or** dark `#1A2433` to mirror live; drop burnt-orange primary buttons.
2. **Hero media** — Use live-style cloud sky image as `.hero` background (`cover`, center). Add dark gradient vignette for type. Retire plain teal→navy CSS-only gradient as the hero’s only story.
3. **Hero grid** — Keep two-column: copy + CTA left; **panel** right must include (a) service times, (b) monthly scheduled events list, (c) simplified map graphic or static map image with cross pin — not just KPIs.
4. **Primary CTA** — Label **Find us** (live wording), solid brand blue `#1C587B`, rectangular or soft-radius — not brown pill “Call” as the hero primary. Phone can remain secondary / header / callbar.
5. **Typography** — Live is **sans throughout**. Prefer sans H1 on hero to match; if serif is kept for section titles on cream, keep hero H1 white sans so it still feels like live.
6. **Header** — Keep `theme-dark-header` + existing `assets/logo.png`. White nav; don’t lighten header to cream.
7. **Events** — Live lists Leadership / Men’s business / Children’s Bible drill / Saturday singing / Singing night / Quarterly prayer in the hero rail — rebuild already has cards below; **also** surface a compact list in the hero panel for parity.
8. **Resources** — Cards linking to live tracts/sermons/workbooks/bulletins are fine; style links in brand blue, not gold-brown.
9. **Footer** — Mid/deep navy; address + Dan Vess + phone; quiet.

## 508 notes

- White on cloud photo needs consistent overlay — check H1 and body ≥ 4.5:1.
- FIND US blue on dark sky: verify button fill vs label contrast.
- Orange `#EF8224` cross is decorative; don’t use orange for small body text on cream (fails).
- Preserve skip link; mark map as image with alt describing “Map: Forum Terrace at Arkansas Lane near Hwy 360 / I-20.”
- Nav on dark is good; ensure focus-visible outlines in light color.
- Members area is gated on live — rebuild correctly omits directory; don’t fake login UI.

## What to keep

- **Existing FTCC logo** (blue square mark + wordmark).
- Cloud / sky atmospheric photography language.
- Welcome copy and Grand Prairie address: 2446 Arkansas Lane, 75052.
- Service times (Sun 9:30 / 10:30 / 5:00; Wed 7:30) and monthly event cadence.
- Dan Vess · `(972) 922-3249`.
- Outbound resource destinations on forumterrace.org (titles unchanged).
- Welcoming, information-first church tone — polish hierarchy and contrast; **do not** reinvent as warm-brochure brand.


---

## Content / nav parity (HARD GATE)

**Parity status:** FAIL risk — Resources (Tracts/Workbooks/Sermons) and Bulletins must stay reachable; Member Directory link OK as gated external.

### Live nav map
- **Home** → `http://forumterrace.org/`
- **Location** → `http://forumterrace.org/location`
- **Bulletins** → `http://forumterrace.org/#blog`
- **Contact Us** → `http://forumterrace.org/#contact`
- **Resources** (dropdown)
  - Tracts → `http://forumterrace.org/tracts/`
  - Workbooks / Bible Classes → `http://forumterrace.org/bible-classes/`
  - Sermons → `http://forumterrace.org/sermons/`
- **Members** (dropdown)
  - Member Directory (gated — do not copy contents) → `http://forumterrace.org/member-directory-2/`
- **Find Us** → `https://www.google.com/maps/place/2446+Arkansas+Ln,+Grand+Prairie,+TX+75052`



### Rebuild nav map (current)
- Home → `index.html`
- Location → `location.html`
- Bible Classes → `classes.html`
- Resources → `resources.html`
- Contact → `contact.html`

### Eng requirement
Restore **full live header IA** (every top item + dropdown children). Collapsing only OK if every destination stays reachable with the **same labels**. Do not strip Financing / service-area / deep service pages into a thin 4–5 link bar.

## Image inventory (Eng must incorporate)

Homepage (and linked gallery/team) assets from live — download into `assets/` and place in matching sections (hero / gallery / team / services). Do not leave pages image-thin vs live.

1. **logo** — `http://forumterrace.org/wp-content/uploads/2018/06/cropped-FTCoC_Logo_646x200.png` alt="Forum Terrace Church of Christ"
2. **content** — `http://forumterrace.org/wp-content/uploads/2018/06/FTCoC_Map_1000x837-300x251.png`
3. **hero/banner** — `http://forumterrace.org/wp-content/uploads/2018/06/photo-1432059964050-d4eba2ef368a.jpg`
4. **hero/banner** — `http://forumterrace.org/wp-content/uploads/2018/06/BoyAndBibleSliderLeftJustified.jpg`

Parsed homepage image count (raw): **4**. Also pull gallery/inner-page images when those routes are restored.

## Favicon

- **Live source:** `http://forumterrace.org/wp-content/uploads/2026/05/cropped-FtCC_Logo-1-32x32.png`
- **Local capture:** `/workspace/dfw-design-briefs/favicons/forum-terrace-church.png`
- **Note:** Ship this favicon (or logo-derived 32/180) — never invent a new mark.

