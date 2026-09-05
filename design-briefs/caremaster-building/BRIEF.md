# CareMaster Building Services — Design Brief

**Live:** http://www.caremaster.biz/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/caremaster-building/  
**Shots:** `live-home.png`, `live-hero.png`, `rebuild-home.png`, `rebuild-hero.png`  
**Constraint:** Match live vibe — polish only, no new brand. Keep existing logo.

## Vibe score: **4 / 10**

Rebuild is a clean modern scaffold (sticky header, CTA, KPI panel) but **misses the live brand personality**: centered logo stack, quiet gray caps nav, full-bleed Dallas skyline with one centered white sentence, forest-green + gold identity. Current rebuild leans teal / navy pinstripe and left-aligned sales-card hero — feels like a different company.

## Live color tokens (sampled)

| Token | Hex | Use |
|---|---|---|
| `--surface` | `#FFFFFF` | Header + body |
| `--ink` | `#2A2A2A` | Body copy |
| `--muted` | `#CCCCCC` | Nav links (fails AA) |
| `--brand` | `#1F4A3B` | Logo green / primary |
| `--brand-2` / gold | `#918561` | Logo tower + stars |
| `--hero-ink` | `#FFFFFF` | Hero sentence |
| `--hero-overlay` | `rgba(40,35,40,0.45)` | Skyline wash (~`#382F32` midtones) |
| `--line` | `#E5E2D1` | Soft header divider |

**Do not keep as brand:** rebuild teal `#2A9D8F` — not on live.

## Layout intent (live)

1. **Centered brand header** — large logo alone on white; no left-lock brand row.
2. **Centered all-caps nav** under logo (Home / About Us / Services / Our Commitment). Contact is not a header pill on live.
3. **Full-bleed skyline hero** — single centered H1 sentence, no lede, no buttons, no right panel.
4. **White prose band** below — short “service is our business” paragraphs, max-width readable (~65ch), not a marketing card grid.
5. Polish may add a discreet phone affordance (footer / mobile callbar) without rewriting the hero into a SaaS split.

## Concrete Eng CSS / HTML change list

1. **`theme.css` tokens** — Retune `--brand` → `#1F4A3B`, `--brand-2`/`--accent` → `#918561` (or darker gold `#7A6E4A` for buttons), drop teal. `--bg` → `#FFFFFF` / soft `#F7F7F5`. `--ink` → `#1A1A1A`.
2. **Header structure** — Prefer centered logo treatment (or keep sticky row but **don’t** invent dual wordmark + logo lockup that fights the mark). Keep `assets/logo.jpg` as sole brand mark; hide or demote `.brand-text` if it duplicates the logo words.
3. **Nav** — Style as live: uppercase, letter-spacing ~0.08em, color ≥ `#595959` (not `#CCC`). Hover → brand green underline. Add Contact only if already in IA; don’t invent new brand pages.
4. **Hero** — Restore skyline photo as `.hero` background (cover, center). Center content; remove / relocate the “Talk with CareMaster” aside from the hero. One white sentence as H1; optional thin gold rule under it. Overlay: dark gradient for AA on white text.
5. **CTAs** — Live hero has none. Move `Call` + `See services` under the prose section or into sticky/mobile callbar — gold/green solid, not teal pills.
6. **Typography** — Body: system sans. Avoid display serif competing with logo serif. H1 ~clamp(1.4rem, 2.4vw, 1.85rem), medium weight, centered.
7. **Below fold** — Keep copy; constrain `.prose` width; optional light top border. No fake KPI inventiveness in the hero (1982 / IICRC can live in About or a quiet strip under prose).
8. **Footer** — Dark green `#1F4A3B` or charcoal; white/muted text; phone + PO Box. Match sparse live footer energy.

## 508 notes

- Live nav `#CCC` on `#FFF` fails WCAG AA — darken to ≥ `#595959` or brand green.
- Skyline + white type: keep overlay so contrast ≥ 4.5:1 on H1; avoid light gray lede on photo.
- Logo `alt="CareMaster Building Services"`; skyline is decorative if H1 carries meaning (`alt=""` or CSS bg).
- Ensure skip link, focus rings on nav/buttons, and `aria-expanded` on menu button stay.
- Tel links already good — keep `href="tel:+14692333366"`.
- Don’t rely on gold-on-white for small text; gold is accent only.

## What to keep

- **Existing logo graphic** (tower + stars + wordmark) — do not redraw or replace.
- Exact live hero sentence and “Service is our business” messaging.
- Dallas skyline association (local commercial credibility).
- Simple IA: Home / About / Services / Commitment (+ Contact if present).
- Phone `(469) 233-3366`, email, PO Box 29303 Dallas TX 75229.
- Quiet, established, utility-first corporate tone — polish spacing, contrast, sticky usability; **do not** rebrand into teal startup chrome.


---

## Content / nav / image / favicon parity (Scout fold — authoritative)

_Folded from `/workspace/dfw-parity/caremaster-building.md` (Scout public HTML inventory, 2026-09-05). Supersedes thinner lists for Eng._

# CONTENT PARITY — caremaster-building

**Live source:** http://www.caremaster.biz/  
**Fetched:** 2026-09-05 (HTTP 200; public homepage HTML only)  
**Page title:** Home - CareMaster Building Services  
**Notes:** HTTPS may fail on this host; inventory uses HTTP. No invented URLs or labels.

---

## 1. Primary navigation (+ dropdown children)

Source: `#fm_mnav` / `.sk-menu` menuitem anchors; visible labels from site menu config `"Text"` fields (caption spans in HTML are empty; first item also has `title`/`Alt` = `"Main"`).

| Label | Absolute URL | Dropdown children |
|-------|--------------|-------------------|
| Home | http://www.caremaster.biz/index.html | *(none — flat item; config `elements: []`)* |
| About Us | http://www.caremaster.biz/about-us | *(none)* |
| Services | http://www.caremaster.biz/services | *(none)* |
| Our Commitment | http://www.caremaster.biz/our-commitment | *(none)* |

**Dropdowns:** none on primary nav.

**Related header contact links (not primary nav items):**
- `tel:469.233.3366` — 469.233.3366
- `mailto:customerservice@caremaster.biz` — customerservice@caremaster.biz

**Logo home link:** http://www.caremaster.biz/ (`aria-label` / alt: CareMaster Building Services)

---

## 2. Key live images / heroes (absolute URLs)

### Logo
- https://0201.nccdn.net/1_2/000/000/132/48e/logo-2.jpg#RDAMDAID43011713  
  *(alt: CareMaster Building Services; 245×150)*

### Hero / page image (`.pageImage`, `role="banner"` aria-label: "High rise buildings")
Primary (full) asset:
- https://0201.nccdn.net/1_2/000/000/14d/871/city.png#RDAMDAID42972464

Responsive variants declared in homepage CSS:
- https://0201.nccdn.net/4_2/000/000/05c/240/city-1280x443.png#RDAMDAID42974225
- https://0201.nccdn.net/1_2/000/000/090/63e/city-960x332.png#RDAMDAID42974226
- https://0201.nccdn.net/4_2/000/000/038/2d3/city-640x221.png#RDAMDAID42974227
- https://0201.nccdn.net/4_2/000/000/060/85f/city-480x166.png#RDAMDAID42974223
- https://0201.nccdn.net/1_2/000/000/161/fe9/city-320x111.png#RDAMDAID42974222
- https://0201.nccdn.net/1_2/000/000/0f0/43d/city-160x55.png#RDAMDAID42974224

**Other content `<img>` on homepage:** none beyond logo (system `blank.gif` spacers omitted).

---

## 3. Favicon URL(s)

From `<link>` tags on homepage:

| rel | sizes | type | Absolute URL |
|-----|-------|------|--------------|
| icon | — | image/x-icon | https://img-fl.nccdn.net/favicon.ico?V=4722132f#SYSTEM |
| apple-touch-icon | — | — | https://img-fl.nccdn.net/apple-touch-icon.png?V=4722132f#SYSTEM |
| icon | 32x32 | image/png | https://img-fl.nccdn.net/favicon-32x32.png?V=4722132f#SYSTEM |
| icon | 16x16 | image/png | https://img-fl.nccdn.net/favicon-16x16.png?V=4722132f#SYSTEM |
| icon | 16x16 *(as declared)* | image/png | http://www.caremaster.biz/android-chrome-192x192.png#SYSTEM |
| icon | 16x16 *(as declared)* | image/png | http://www.caremaster.biz/android-chrome-512x512.png#SYSTEM |



### Parity emphasis
- Flat 4-item nav: Home / About Us / Services / Our Commitment.
- **Hero must be skyline** `city.png` (+ responsive variants) — Tick SOFT if lede+CTA replaces skyline-only feel.
- Favicon set from nccdn + android-chrome on caremaster.biz.


