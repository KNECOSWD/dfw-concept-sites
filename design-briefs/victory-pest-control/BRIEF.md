# Victory Pest Control — design brief

**Live:** https://www.victorypestcontrol.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/victory-pest-control/  
**Capture note:** browserUse Task not available to this worker; headless Chrome screenshots saved instead. Live capture includes cookie banner + a11y widget chrome (ignore for brand match).

**Vibe match: 3/10** — Rebuild invents an olive/forest + mustard “estate” look with Georgia headlines. Live is **navy + gold/yellow** pest-control marketing (Hibu): photo hero (termites), gold Book Online / Request Callback, dense navy nav, VPC logo lockup.

## 1. Vibe match score
**3/10** — Green forest palette and serif display are a different brand; live is navy/gold utility marketing with photo hero and lead form.

## 2. Color tokens from LIVE (hex)
| Token | Hex | Notes |
| --- | --- | --- |
| `--brand` | `#001A54` | Deep navy (top bars, nav, phone) |
| `--brand-2` | `#D4AF37` | Gold buttons / form wash |
| `--accent` | `#F7D000` | Bright yellow CTAs / highlights |
| `--bar-teal` | `#11414B` | Secondary dark teal sections |
| `--ink` | `#2e2e2d` / `#333333` | Body |
| `--muted` | `#666666` / `#888787` | Secondary |
| `--bg` | `#f5f5f5` / `#faf9f9` | Page wash |
| `--surface` | `#ffffff` | Cards / forms |
| `--hero-ink` | `#ffffff` | On photo/navy |
| `--cyan` | `#68ccd1` | Occasional accent (use sparingly) |
| Logo brown | `#4F301C` | VPC mark tones |
| `--font-display` | `Righteous` (logo-adjacent) + `Muli`/system sans body | Not Georgia |

## 3. Layout intent
- Utility pest site: navy header bars, gold CTAs, phone large in header.
- Nav density: Home / Services / Specials / Reviews / About / Contact (live also has Pest Library, Training — include only if already in rebuild IA).
- Hero: **photo background** (termites/wood or published hero CDN) + white claim copy + bullets (24h, warranty, free estimates) + optional callback form panel in gold wash.
- Below: trust/about prose, service cards, specials callouts.
- Keep **VPC logo** (`assets/logo.jpg`) only — do not replace with text wordmark alone.

## 4. Concrete CSS/HTML change list for Eng
1. `theme.css`: replace `--brand:#2d4a22` with `#001A54`; `--brand-2`/`--accent` → `#D4AF37` / `#F7D000`; **drop olive/forest greens**.
2. `--font-display`: drop Georgia → Muli/system (Righteous only if already used for logo-adjacent titles).
3. Header: light or white top with logo + large navy phone; solid navy nav bar with white links (live pattern); gold “Call” / Book-style CTA.
4. Hero: photo-backed (use live CDN hero if licensed in assets, else navy photo-style treatment) — remove diagonal green stripe pattern and yellow radial that reads template.
5. `.btn-primary` → gold/yellow on navy or navy on gold (verify contrast); ghost buttons white on navy.
6. Aside panel: restyle from dark green glass to navy/gold form-like card (phone dual lines, 24h, address) — sell-as-is may omit live reCAPTCHA form fields if not building leads; keep contact facts only.
7. Body `--bg`: light gray/cream `#f5f5f5`, not olive wash `#f4f1e6`.
8. Specials: yellow/gold callouts on navy cards; keep published discount copy only.
9. Strip cookie/a11y third-party chrome from any cloned markup; rebuild already cleaner — keep it.

## 5. 508 notes
- Yellow `#F7D000` on white fails for text; on navy use dark ink or large UI only.
- Gold `#D4AF37` on navy: verify buttons/links ≥4.5:1 (darken gold or use white text on `#001A54`).
- Dual phones as separate `tel:` links with visible numbers.
- Hero photo: meaningful `alt` (e.g. termite damage / inspection context) or empty if purely decorative with adjacent text.
- Keep skip link; visible focus on navy (light outline).
- If callback form kept: labeled inputs, error text not color-only.

## 6. What to keep
- VPC logo asset; owner John Gaines; (972) 230-5526 + mobile (214) 543-6357; Red Oak address.
- Published services (resi/commercial, wildlife, bed bugs, termites, IPM) and specials copy cleaned of any lorem.
- 24/7 availability, warranty, free inspection messaging as published.
- No invented brand greens; polish only toward live navy/gold.


---

## Content / nav parity (HARD GATE)

**Parity status:** FAIL risk — missing Pest Library, Technician Training, Bed Bug / Wildlife destinations as first-class nav; Services dropdown required.

### Live nav map
- **Home** → `https://www.victorypestcontrol.com/`
- **Pest Control Services** (dropdown)
  - Residential & Commercial Pest Control → `https://www.victorypestcontrol.com/residential-commercial-pest-control`
  - Nuisance Wildlife Control → `https://www.victorypestcontrol.com/nuisance-wildlife-control`
  - Bed Bug Control → `https://www.victorypestcontrol.com/bed-bug-control`
- **Specials** → `https://www.victorypestcontrol.com/specials`
- **Pest Library** → `https://www.victorypestcontrol.com/pest-library`
- **Technician Training** → `https://www.victorypestcontrol.com/technician-training`
- **Reviews** → `https://www.victorypestcontrol.com/reviews`
- **About** (dropdown)
  - FAQs → `https://www.victorypestcontrol.com/faqs`
- **Contact** (dropdown)
  - Request Callback → `https://www.victorypestcontrol.com/request-callback-form`



### Rebuild nav map (current)
- Home → `index.html`
- Services → `services.html`
- Specials → `specials.html`
- About → `about.html`
- Reviews → `reviews.html`
- Contact → `contact.html`

### Eng requirement
Restore **full live header IA** (every top item + dropdown children). Collapsing only OK if every destination stays reachable with the **same labels**. Do not strip Financing / service-area / deep service pages into a thin 4–5 link bar.

## Image inventory (Eng must incorporate)

Homepage (and linked gallery/team) assets from live — download into `assets/` and place in matching sections (hero / gallery / team / services). Do not leave pages image-thin vs live.

1. **logo** — `https://le-cdn.hibuwebsites.com/fd3ab55c0a634fe5856b95a43028cb02/dms3rep/multi/opt/victory-pest-control-llc-logo-0510bb09-1920w.jpg` alt="Victory Pest Control - logo"
2. **logo** — `https://le-cdn.hibuwebsites.com/fd3ab55c0a634fe5856b95a43028cb02/dms3rep/multi/opt/victory-pest-control-llc-logo-0510bb09-394w.jpg` alt="Victory Pest Control - logo"
3. **logo** — `https://le-cdn.hibuwebsites.com/fd3ab55c0a634fe5856b95a43028cb02/dms3rep/multi/opt/gen-logo-e5ccbe50-1920w.png`
4. **content** — `https://le-cdn.hibuwebsites.com/8aa30245016342a49a4dad0645e59cd0/dms3rep/multi/opt/vid-splash-play-1920w.png` alt="Play Video"
5. **content** — `https://dd-cdn.multiscreensite.com/runtime-img/galleryLoader.gif`
6. **content** — `https://irt-cdn.multiscreensite.com/ce0bb35f932b47bb809d0e37905542ba/dms3rep/multi/site_background_education-2087x1173.jpg`
7. **content** — `https://le-cdn.hibuwebsites.com/md/dmtmpl/dms3rep/multi/opt/people_pool_party-1920w.jpg`
8. **content** — `https://le-cdn.hibuwebsites.com/md/dmip/dms3rep/multi/opt/woman-boxer-sport-1920w.jpg`
9. **hero/banner** — `https://le-cdn.hibuwebsites.com/fd3ab55c0a634fe5856b95a43028cb02/dms3rep/multi/opt/victory-pest-control-llc-hero-home-1920w.jpg`
10. **content** — `https://le-cdn.hibuwebsites.com/fd3ab55c0a634fe5856b95a43028cb02/dms3rep/multi/opt/victory-pest-control-llc-home-content4-1920w.jpg`

Parsed homepage image count (raw): **10**. Also pull gallery/inner-page images when those routes are restored.

## Favicon

- **Live source:** `https://cdn.hibuwebsites.com/fd3ab55c0a634fe5856b95a43028cb02/site_favicon_16_1762444308157.ico`
- **Local capture:** `/workspace/dfw-design-briefs/favicons/victory-pest-control.ico`
- **Note:** Ship this favicon (or logo-derived 32/180) — never invent a new mark.

