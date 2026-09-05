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

## Content / nav parity (HARD GATE)

**Parity status:** Closer — ensure About/Services/Our Commitment parity; skyline hero image required.

### Live nav map
- **Home** → `http://www.caremaster.biz/`
- **About Us** → `http://www.caremaster.biz/about-us`
- **Services** → `http://www.caremaster.biz/services`
- **Our Commitment** → `http://www.caremaster.biz/our-commitment`

_Note: Live Freemona nav is Home / About Us / Services / Our Commitment (centered caps). Rebuild Contact page OK to keep if destination exists; do not drop About/Services/Commitment._

### Rebuild nav map (current)
- Home → `index.html`
- About Us → `about.html`
- Services → `services.html`
- Our Commitment → `commitment.html`
- Contact → `contact.html`

### Eng requirement
Restore **full live header IA** (every top item + dropdown children). Collapsing only OK if every destination stays reachable with the **same labels**. Do not strip Financing / service-area / deep service pages into a thin 4–5 link bar.

## Image inventory (Eng must incorporate)

Homepage (and linked gallery/team) assets from live — download into `assets/` and place in matching sections (hero / gallery / team / services). Do not leave pages image-thin vs live.

1. **logo** — `https://0201.nccdn.net/1_2/000/000/132/48e/logo-2.jpg#RDAMDAID43011713` alt="CareMaster Building Services"
2. **content** — `https://designs.nccdn.net/Common/Gallery/mat-black-12.png`
3. **content** — `https://designs.nccdn.net/Common/Gallery/mat-black-80.png`
4. **content** — `https://designs.nccdn.net/Common/Gallery/sprite-dots-dark.svg`
5. **content** — `https://designs.nccdn.net/Common/Gallery/nav-numbers-light.svg`
6. **content** — `https://designs.nccdn.net/Common/Gallery/close.svg`
7. **content** — `https://designs.nccdn.net/Common/Gallery/mat-black-60.png`
8. **content** — `https://designs.nccdn.net/Common/Gallery/sprite-scrollbar-arrows-light.svg`
9. **content** — `https://designs.nccdn.net/FinancialAdvisor9/Images/section-arrow-expanded-dark.png`
10. **content** — `https://designs.nccdn.net/FinancialAdvisor9/Images/section-arrow-collapsed-dark.png`
11. **content** — `https://designs.nccdn.net/Common/Section/section-arrow-expanded-white.png`
12. **content** — `https://designs.nccdn.net/Common/Section/section-arrow-collapsed-white.png`
13. **content** — `https://designs.nccdn.net/Common/Navigation/nav_dot_separator_white.png`
14. **content** — `https://designs.nccdn.net/FinancialAdvisor9/Images/menu_icon.svg`
15. **content** — `https://designs.nccdn.net/FinancialAdvisor9/Images/collapsible_panel.svg`
16. **content** — `https://0201.nccdn.net/1_2/000/000/14d/871/city.png#RDAMDAID42972464`
17. **content** — `https://0201.nccdn.net/4_2/000/000/05c/240/city-1280x443.png#RDAMDAID42974225`
18. **content** — `https://0201.nccdn.net/1_2/000/000/090/63e/city-960x332.png#RDAMDAID42974226`
19. **content** — `https://0201.nccdn.net/4_2/000/000/038/2d3/city-640x221.png#RDAMDAID42974227`
20. **content** — `https://0201.nccdn.net/4_2/000/000/060/85f/city-480x166.png#RDAMDAID42974223`
21. **content** — `https://0201.nccdn.net/1_2/000/000/161/fe9/city-320x111.png#RDAMDAID42974222`
22. **content** — `https://0201.nccdn.net/1_2/000/000/0f0/43d/city-160x55.png#RDAMDAID42974224`
23. **content** — `https://si.nccdn.net/pictograms-gray/48/icon_02.png`
24. **content** — `https://si.nccdn.net/pictograms-gray/48/icon_04.png`

Parsed homepage image count (raw): **29**. Also pull gallery/inner-page images when those routes are restored.

## Favicon

- **Live source:** `https://img-fl.nccdn.net/favicon.ico?V=4722132f#SYSTEM`
- **Local capture:** `/workspace/dfw-design-briefs/favicons/caremaster-building.ico`
- **Note:** Ship this favicon (or logo-derived 32/180) — never invent a new mark.

