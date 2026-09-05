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

## Content / nav / image / favicon parity (HTML inventory fold)

_Built from `/workspace/dfw-parity/` live HTML for `victory-pest-control` (supersede if formal Scout `.md` arrives)._  
**Live:** https://www.victorypestcontrol.com/  
**Title:** Pest and Wildlife Control Victory Pest Control DFW Metroplex

### Primary nav
1. **Home** → `/`
2. **Pest Control Services** (dropdown) → Residential & Commercial; Nuisance Wildlife; Bed Bug Control
3. **Specials** → `/specials`
4. **Pest Library** → `/pest-library`
5. **Technician Training** → `/technician-training`
6. **Reviews** → `/reviews`
7. **About** → `/about` (+ FAQs if nested)
8. **Contact** → `/contact` (+ Request Callback)

Do not drop Library / Training / wildlife / bed-bug destinations.


### Key images / heroes
- `https://wsv3cdn.audioeye-services.com/springtimeShim.js`
- `https://wsv3cdn.audioeye-services.com/aem.js`
- `https://le-cdn.hibuwebsites.com/fd3ab55c0a634fe5856b95a43028cb02/dms3rep/multi/opt/victory-pest-control-llc-logo-0510bb09-1920w.jpg`
- `https://le-cdn.hibuwebsites.com/fd3ab55c0a634fe5856b95a43028cb02/dms3rep/multi/opt/victory-pest-control-llc-logo-0510bb09-394w.jpg`
- `https://le-cdn.hibuwebsites.com/8aa30245016342a49a4dad0645e59cd0/dms3rep/multi/opt/vid-splash-play-1920w.png`
- `https://wsmcdn.audioeye.com/aem.js`
- `https://static-res-cdn.websites.hibu.com/libs/jquery/jquery-3.7.0.min.js`
- `https://static-res-cdn.websites.hibu.com/mnlt/production/6747/_dm/s/rt/dist/scripts/d-js-one-runtime-unified-desktop.min.js`
- `https://static-res-cdn.websites.hibu.com/mnlt/production/6747/_dm/s/rt/dist/scripts/d-js-jquery-migrate.min.js`
- `https://dh-static-files.s3.amazonaws.com/prod/AppMeasurement.js`
- `https://dh-static-files.s3.amazonaws.com/prod/hibu-analytics.min.js`
- `https://dh-static-files.s3.amazonaws.com/prod/omn_setting.js`

### Favicon
- `https://cdn.hibuwebsites.com/fd3ab55c0a634fe5856b95a43028cb02/site_favicon_16_1762444308157.ico`

### Capture notes
Hibu. VPC brand logo only (not gen-logo). Navy/gold. Strip live lorem/placeholders. AA: avoid muted gray body on #f5f5f5.

