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

## Content / nav / image / favicon parity (Scout fold — authoritative)

_Folded from `/workspace/dfw-parity/forum-terrace-church.md` (Scout public HTML inventory, 2026-09-05). Supersedes thinner lists for Eng._

# CONTENT PARITY — forum-terrace-church

**Live source:** http://forumterrace.org/  
**Fetched:** 2026-09-05 (HTTP 200; public homepage HTML only)  
**Page title:** The Forum Terrace Church of Christ in Grand Prairie welcomes you!  
**Notes:** HTTPS may fail on this host; inventory uses HTTP. No invented URLs or labels.

---

## 1. Primary navigation (+ dropdown children)

Source: `#main-navigation` / `#menu-menu1.nav.navbar-nav`

| Label | Absolute URL | Dropdown children |
|-------|--------------|-------------------|
| Location | http://forumterrace.org/location | *(none)* |
| Bulletins | http://forumterrace.org/#blog | *(none)* |
| Contact Us | http://forumterrace.org/#contact | *(none)* |
| Tracts | http://forumterrace.org/tracts/ | *(none)* |
| Workbooks | http://forumterrace.org/bible-classes/ | *(none)* |
| Sermons | http://forumterrace.org/sermons/ | *(none)* |
| MEMBERS | # | **Member Directory** → http://forumterrace.org/member-directory-2/ |

**Dropdown detail — MEMBERS** (`menu-item-has-children` / `.dropdown-menu`):
- Member Directory — http://forumterrace.org/member-directory-2/

**Also in nav chrome (not a page link):** Hestia search form (`action=http://forumterrace.org/`).

**Navbar brand / logo link:** http://forumterrace.org/

---

## 2. Key live images / heroes (absolute URLs)

### Logo (header)
- http://forumterrace.org/wp-content/uploads/2018/06/cropped-FTCoC_Logo_646x200.png  
  *(alt: Forum Terrace Church of Christ)*

### Hero / header filter background
- http://forumterrace.org/wp-content/uploads/2018/06/photo-1432059964050-d4eba2ef368a.jpg  
  *(used as CSS `background` on `.header-filter` and again on `#about.hestia-about.section-image`)*

### Contact section background
- http://forumterrace.org/wp-content/uploads/2018/06/BoyAndBibleSliderLeftJustified.jpg  
  *(CSS `background` on `#contact.hestia-contact.section-image`)*

### Map image (homepage content)
- http://forumterrace.org/wp-content/uploads/2018/06/FTCoC_Map_1000x837-300x251.png *(src, 300w)*
- http://forumterrace.org/wp-content/uploads/2018/06/FTCoC_Map_1000x837-768x643.png *(srcset 768w)*
- http://forumterrace.org/wp-content/uploads/2018/06/FTCoC_Map_1000x837.png *(srcset 1000w / full)*

### Social / OG share image (meta, not necessarily on-canvas hero)
- og:image: http://forumterrace.org/wp-content/uploads/2018/06/photo-1432059964050-d4eba2ef368a-1024x576.jpg
- twitter:image: http://forumterrace.org/wp-content/uploads/2018/06/photo-1432059964050-d4eba2ef368a.jpg

---

## 3. Favicon URL(s)

From `<link>` / related meta on homepage:

| rel / meta | sizes | Absolute URL |
|------------|-------|--------------|
| icon | 32x32 | http://forumterrace.org/wp-content/uploads/2026/05/cropped-FtCC_Logo-1-32x32.png |
| icon | 192x192 | http://forumterrace.org/wp-content/uploads/2026/05/cropped-FtCC_Logo-1-192x192.png |
| apple-touch-icon-precomposed | — | http://forumterrace.org/wp-content/uploads/2026/05/cropped-FtCC_Logo-1-180x180.png |
| msapplication-TileImage | — | http://forumterrace.org/wp-content/uploads/2026/05/cropped-FtCC_Logo-1-270x270.png |



### Parity emphasis
- Flat items Location / Bulletins / Contact / Tracts / Workbooks / Sermons + **MEMBERS → Member Directory** (gated — link only, don’t copy members).
- Incorporate cloud hero photo, BoyAndBible contact bg, map image.
- Favicon from cropped FtCC_Logo-1 sizes.


