# Beyond Lawn Care — design brief

**Live:** https://beyondlawncares.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/beyond-lawn-care/  
**Shots:** `live-home.png`, `live-hero.png`, `rebuild-home.png`, `rebuild-hero.png`  
**Note:** Live is a photo-forward Duda site; rebuild is scaffold forest-green + serif. Colors sampled from live CSS (`--btn-bg-color: rgb(24,121,63)`, orange `rgb(242,124,33)`) and PNGs (`#f07c20` top bar, `#18783c` GET ESTIMATE).

## 1. Vibe match score
**5 / 10** — Orange/green family is roughly right, but rebuild’s dark forest Georgia “estate” hero misses live’s brighter green + hot orange, Work Sans/Montserrat all-caps marketing density, white nav, and photo hero with “OUR SERVICES” CTA.

## 2. Color tokens (sampled from LIVE)
| Token | Hex | Role |
| --- | --- | --- |
| `--bg` | `#fcfcfc` / light `#eef5ee` | Page wash |
| `--surface` | `#ffffff` | Header, cards, footer columns |
| `--ink` | `#3a3a3a` / near-black | Body |
| `--muted` | `#666666` | Secondary |
| `--brand` | `#18793f` | Primary green (GET ESTIMATE, selected HOME, section fills ~`#217942`) |
| `--brand-2` / `--accent` | `#f27c21` | Top bar, nav links, orange CTAs (PNG ~`#f07c20` / `#f2802d`) |
| `--brand-hover` | `#ff5029` or darker `#d45f10` | Hover / AA-safe button fallback |
| `--hero-ink` | `#ffffff` | Hero title/sub on photo overlay |
| `--font` | `"Work Sans", system-ui, sans-serif` | Body + UI |
| `--font-display` | `Montserrat, "Work Sans", system-ui, sans-serif` | All-caps section titles (not Georgia) |

Update theme away from `#1b4332` / `#e85d04` toward the brighter live pair above.

## 3. Layout intent
- **Nav:** White sticky/header row; logo left (existing BEYOND mark only); all-caps links (HOME green selected; others orange); green “GET ESTIMATE” button right. Orange angled top contact bar (phone + email).
- **Hero:** Full-bleed lawn/crew photo + dark overlay; left/large white uppercase H1 “LAWN CARE & LANDSCAPING”; white subline; orange “OUR SERVICES” button — not a dotted dark-green two-column panel.
- **Density:** Marketing-forward blocks (estimate form band, green About, service cards with photos, gallery energy, Elfsight reviews, multi-column footer). High contrast color banding (orange / green / white / black accents).
- **Typography:** Bold sans, heavy uppercase section labels; avoid serif display.

## 4. Concrete CSS/HTML change list (Engineering)
1. **`theme.css`:** `--brand:#18793f`; `--brand-2`/`--accent:#f27c21`; lighten `--bg` toward `#fcfcfc`/`#eef5ee`; `--ink:#3a3a3a`; `--hero-ink:#ffffff`.
2. **Fonts:** Set `--font-display` to Montserrat/Work Sans stack; remove Georgia.
3. **Header:** Light surface header (not dark forest); green text for selected nav; orange for other links; primary header CTA = green fill “GET ESTIMATE” (or keep call CTA but match live green button styling). Optional thin orange top utility bar for phone/email.
4. **Buttons:** Primary marketing CTAs orange (`#f27c21`) with white text; secondary/estimate green (`#18793f`).
5. **Hero:** Photo-backed treatment (use gallery CDN lawn photos already on live / rebuild assets if present); reduce radial dot pattern; drop serif H1; uppercase sans H1 + orange services CTA.
6. **Services grid:** Keep real service titles; optionally denser cards with image thumbs where assets exist — do not invent services.
7. **Reviews:** Keep Elfsight widget only — no static invented quotes.
8. **Logo:** Keep existing BEYOND logo only — do not redraw.
9. **Packages/Gallery pages:** Photo-first grids + clear orange CTAs to match live marketing density (structure polish only).

## 5. 508-relevant design risks
- **Contrast:** Orange `#f27c21` with white button text is borderline for small text — reserve for large CTAs; if fails, darken to `#d45f10` for text buttons. Body links should use green `#18793f`, not orange.
- **Contrast:** White on `#18793f` for footer/sub-bar generally OK; verify muted gray on mint bg.
- **Focus:** Visible focus on orange and green controls (2px dark + light ring).
- **Alt text:** Logo (“Beyond Lawn Care & Landscaping”); hero crew/lawn photo descriptive alt; gallery images need real captions/alts from published media — no empty decorative-only if informative.
- **Heading order:** One `h1` (hero); About/Services/Reviews as `h2`; service names `h3`. Live uses stacked `h3`/`h4`/`h5`/`h6` oddly — rebuild should stay cleaner.
- **Skip link:** Present — verify on light header.
- **Forms:** Estimate/contact fields need visible labels (live uses NAME/EMAIL/PHONE labels — keep that pattern); don’t rely on placeholder-only.
- **Widget a11y:** Elfsight iframe may need title attribute / adjacent heading.

## 6. What already matches (keep)
- Real Mesquite service-area copy, phone (972) 803-7495, email, hours, full published service tree (mowing through sprinkler/leaf cleanup).
- Existing BEYOND logo asset only.
- Elfsight Google reviews embed (no invented quotes).
- Skip link, tel CTAs, multi-page IA (Services / Packages / Gallery / Contact).
- Green+orange brand family direction (needs brighter live tokens + sans marketing feel, not forest serif).


---

## Content / nav parity (HARD GATE)

**Parity status:** FAIL risk — live Commercial + Residential dropdowns with many service URLs; rebuild flattens to Services/Packages/Gallery/Contact. Every live service URL must remain reachable with same labels.

### Live nav map
- **Home** → `https://www.beyondlawncares.com/`
- **Commercial** (dropdown)
  - Commercial Lawn Care Services → `https://www.beyondlawncares.com/commercial-lawn-care-services`
  - Commercial Landscape Maintenance → `https://www.beyondlawncares.com/commercial-landscape-maintenance`
- **Residential** (dropdown)
  - Lawn Care & Mowing → `https://www.beyondlawncares.com/lawn-care-mowing`
  - Landscape Maintenance → `https://www.beyondlawncares.com/landscape-maintenance`
  - Seasonal Flower Installations → `https://www.beyondlawncares.com/seasonal-flower-installations`
  - Bush & Hedge Trimming → `https://www.beyondlawncares.com/bush-hedge-trimming`
  - Landscape Pruning → `https://www.beyondlawncares.com/landscape-pruning`
  - Property Clean Ups → `https://www.beyondlawncares.com/property-clean-ups`
  - Leaf Cleanup → `https://www.beyondlawncares.com/leaf-cleanup`
  - Mulch Installations → `https://www.beyondlawncares.com/mulch-installations`
  - Overseeding → `https://www.beyondlawncares.com/overseeding`
  - Core Aeration → `https://www.beyondlawncares.com/aeration`
  - Sod Installation → `https://www.beyondlawncares.com/sod-installation`
  - Salt Application → `https://www.beyondlawncares.com/salt-application`
  - Sprinkler System Inspection & Maintenance → `https://www.beyondlawncares.com/sprinkler-system-inspection-maintenance`
- **Gallery** → `https://www.beyondlawncares.com/gallery`
- **Packages** → `https://www.beyondlawncares.com/packages`
- **Contact** → `https://www.beyondlawncares.com/contact`



### Rebuild nav map (current)
- Home → `index.html`
- Services → `services.html`
- Packages → `packages.html`
- Gallery → `gallery.html`
- Contact → `contact.html`

### Eng requirement
Restore **full live header IA** (every top item + dropdown children). Collapsing only OK if every destination stays reachable with the **same labels**. Do not strip Financing / service-area / deep service pages into a thin 4–5 link bar.

## Image inventory (Eng must incorporate)

Homepage (and linked gallery/team) assets from live — download into `assets/` and place in matching sections (hero / gallery / team / services). Do not leave pages image-thin vs live.

1. **content** — `https://irp.cdn-website.com/d4f793c4/dms3rep/multi/opt/BEYOND-1920w.png` alt="Beyond Lawn Care & Landscaping"
2. **content** — `https://irp.cdn-website.com/d4f793c4/dms3rep/multi/opt/Graphic-3-1920w.png` alt="An orange and white triangle on a white background."
3. **content** — `https://irt-cdn.multiscreensite.com/ce0bb35f932b47bb809d0e37905542ba/dms3rep/multi/site_background_education-2087x1173.jpg`

Parsed homepage image count (raw): **3**. Also pull gallery/inner-page images when those routes are restored.

## Favicon

- **Live source:** `https://irp.cdn-website.com/d4f793c4/site_favicon_16_1649959649884.ico`
- **Local capture:** `/workspace/dfw-design-briefs/favicons/beyond-lawn-care.ico`
- **Note:** Ship this favicon (or logo-derived 32/180) — never invent a new mark.

